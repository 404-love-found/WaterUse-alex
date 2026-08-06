"""
Evaluate water-use action-situation extraction outputs against the confirmed
two correct decentralized action situations.

Metrics:
  TP = How many LLM-generated ASs were in the correct set of ASs
  FN = How many correct ASs the LLM missed
  FP = How many LLM-generated ASs were not in the correct set of ASs
  Precision = TP / (TP + FP)
  Recall    = TP / (TP + FN)
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path


CURRENT_DIR = Path(__file__).resolve().parent

EXPERIMENTS = {
    "ODD+game_stuff": {
        "batch_dir": CURRENT_DIR / "Batch_30Runs",
        "report_name": "Water_evaluation_ODD+game_stuff.txt",
        "csv_name": "Water_evaluation_summary_ODD+game_stuff.csv",
        "as_csv_name": "Water_evaluation_as_level_ODD+game_stuff.csv",
    },
    "ODD-only": {
        "batch_dir": CURRENT_DIR / "Batch_30Runs_ODDOnly",
        "report_name": "Water_evaluation_ODD-only.txt",
        "csv_name": "Water_evaluation_summary_ODD-only.csv",
        "as_csv_name": "Water_evaluation_as_level_ODD-only.csv",
    },
}

MODELS = (
    "DeepSeek-R1",
    "DeepSeek-V4-Pro",
    "Llama-3.3-70B",
    "Qwen2.5-7B",
    "Qwen3.7-Plus",
    "gpt-oss-120b",
)


@dataclass(frozen=True)
class GroundTruthAS:
    key: str
    title: str

    @property
    def label(self) -> str:
        return f"{self.key}: {self.title}"


@dataclass(frozen=True)
class ActionSituation:
    title: str
    block: str
    line_no: int
    has_payoff_evidence: bool


@dataclass(frozen=True)
class ASReview:
    index: int
    line_no: int
    title: str
    matched_gt: str
    decision: str
    reason: str
    has_payoff_evidence: bool


@dataclass
class RunResult:
    tp: int
    fn: int
    fp: int
    precision: float
    recall: float
    total_as: int
    found_gt: set[str] = field(default_factory=set)
    details: list[str] = field(default_factory=list)
    fp_titles: list[str] = field(default_factory=list)
    as_reviews: list[ASReview] = field(default_factory=list)


GROUND_TRUTH = {
    "AS1": GroundTruthAS("AS1", "Upstream and downstream withdrawal decisions"),
    "AS2": GroundTruthAS("AS2", "Fish extraction common pool resource game"),
}

DASH_TRANSLATION = str.maketrans({dash: "-" for dash in "‐‑‒–—−"})


def clean_markdown(text: str) -> str:
    cleaned = text.translate(DASH_TRANSLATION).strip()
    cleaned = re.sub(r"^#{1,6}\s*", "", cleaned)
    cleaned = re.sub(r"^\s*[-*]\s+", "", cleaned)
    cleaned = re.sub(r"^\*+|\*+$", "", cleaned.strip())
    cleaned = cleaned.replace("**", "")
    cleaned = re.sub(r"`", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip(" :-")


def canonical_title(text: str) -> str:
    title = clean_markdown(text)
    title = re.sub(r"^\d+\ufe0f?\u20e3\s*", "", title)
    title = re.sub(r"^\d+\s*[.)]\s*(?:title\s*[:.-]\s*)?", "", title, flags=re.IGNORECASE)
    title = re.sub(r"^title\s*[:.-]\s*", "", title, flags=re.IGNORECASE)
    title = re.sub(
        r"^(?:action[- ]+situation|strategic[- ]+dilemma|dilemma|game)\s*[a-z0-9]*\s*[:.)-]\s*",
        "",
        title,
        flags=re.IGNORECASE,
    )
    title = re.sub(
        r"^\d+\s*[.)]\s*(?:strategic\s+)?(?:tension|dilemma|action\s+situation)\s*[:.-]\s*",
        "",
        title,
        flags=re.IGNORECASE,
    )
    return clean_markdown(title)


def normalize(text: str) -> str:
    text = clean_markdown(text).lower()
    return text


def is_terminal_heading(title: str) -> bool:
    return bool(
        re.match(
            r"^(summary|conclusion|notes?|key\s+(constraints|notes|insights|reflections)|"
            r"thought\s+process|final\s+answer|reflections?)\b",
            title.lower(),
        )
    )


def is_generic_heading(title: str) -> bool:
    lower = title.lower()
    if is_terminal_heading(title):
        return True
    if re.search(r"\b(?:normal[- ]form\s+)?payoff matrix\b", lower):
        return True
    if lower in {"matrix", "payoff matrix", "2-player", "justification", "tension", "assumptions"}:
        return True
    if re.match(
        r"^(matrix|payoff matrix|2-player|representation|sequential representation|game tree|"
        r"justification|assumptions|tension|payoff|interpretation)\b",
        lower,
    ):
        return True
    if re.match(r"^(analysis|extracted|distinct action situations|action situation analysis)\b", lower):
        return True
    if re.match(r"^how\s+(?:the\s+)?action[- ]situations?\b", lower):
        return True
    if lower.startswith("title:"):
        stripped = re.sub(r"^title:\s*", "", lower).strip()
        if re.search(r"\b(model|analysis|action situations?|strategic tensions?|strategic dilemmas?)\b", stripped):
            return True
    if re.search(r"\b(action situations?|strategic tensions?)\b", lower) and re.search(
        r"\b(analysis|model|decentralized|distinct|version)\b", lower
    ):
        return True
    return False


def is_structured_field_line(raw_line: str) -> bool:
    """Reject ODD/IAD fields that belong inside an AS block."""
    title = normalize(canonical_title(raw_line))
    if re.match(r"^action[- ]+situations?\b", title):
        return False
    field_names = (
        r"location",
        r"players?",
        r"roles?",
        r"actions?",
        r"control rules?",
        r"information",
        r"outcomes?",
        r"payoffs?",
        r"strategic tension",
        r"strategic classification",
        r"temporal structure",
        r"relevant rules?",
        r"boundary rules?",
        r"position rules?",
        r"choice rules?",
        r"aggregation rules?",
        r"information rules?",
        r"scope rules?",
        r"representation",
        r"sequential representation",
        r"game tree",
        r"matrix",
        r"payoff matrix",
        r"payoff rationale",
        r"justification",
        r"game description",
        r"interpretation",
    )
    return bool(re.match(rf"^(?:{'|'.join(field_names)})(?:\s*[:(\-]|$)", title))


def is_internal_game_tree_step(raw_line: str) -> bool:
    """Reject decision-tree nodes and moves that are not separate AS titles."""
    title = normalize(canonical_title(raw_line))
    if re.match(r"^(?:stage\s*\d+|step\s*\d+|node\s+[a-z0-9]+)\b", title):
        return True
    if re.match(r"^\[[^]]*(?:outcome|state|signal|observation)[^]]*\]", title):
        return True
    return bool(
        re.match(
            r"^(?:(?:focal\s+)?farmer(?:\s*\d+|\s*\([^)]*\))?|staff|peer(?:\s*\([^)]*\))?|"
            r"player\s*\d*|nature|authority|regulator)\s+"
            r"(?:chooses?|decides?|moves?|sets?|observes?|responds?)\b",
            title,
        )
    )


def is_candidate_start(raw_line: str) -> bool:
    stripped = raw_line.strip()
    if not stripped or stripped.startswith("# Run "):
        return False

    is_heading = bool(re.match(r"^#{2,6}\s+", stripped))
    is_plain_title = bool(
        re.match(r"^(?:#{2,6}\s*)?(?:\*\*)?title(?:\*\*)?\s*[:.-]\s*\S", stripped, flags=re.I)
    )
    is_numbered_plain_title = bool(
        re.match(r"^\d+\s*[.)]\s+(?:\*\*)?title(?:\*\*)?\s*[:.-]\s*\S", stripped, flags=re.I)
    )
    is_plain_action_situation = bool(
        re.match(
            r"^(?:action[- ]+situation|strategic[- ]+dilemma|game)\s*[a-z0-9]+\s*[:.)-]\s*\S",
            stripped,
            flags=re.I,
        )
    )
    is_bold_title = bool(
        re.match(
            r"^\*\*(?:title|action[- ]+situation\s*[a-z0-9]*|strategic[- ]+dilemma\s*[a-z0-9]*|game\s*\d*)",
            stripped.translate(DASH_TRANSLATION),
            re.I,
        )
    )
    is_bold_numbered = bool(re.match(r"^\*\*\d+\s*[.)]\s*", stripped))
    is_numbered_bold = bool(re.match(r"^\d+\s*[.)]\s+\*\*", stripped))
    if not (
        is_heading
        or is_plain_title
        or is_numbered_plain_title
        or is_plain_action_situation
        or is_bold_title
        or is_bold_numbered
        or is_numbered_bold
    ):
        return False

    if is_structured_field_line(stripped) or is_internal_game_tree_step(stripped):
        return False

    title = clean_markdown(stripped)
    if is_generic_heading(title):
        return False
    if is_plain_title or is_numbered_plain_title or is_plain_action_situation:
        return len(canonical_title(title)) >= 4

    lower = title.lower()
    candidate_patterns = (
        r"\baction[- ]+situation\s*[a-z0-9]*\b.+",
        r"\bAS\s*[-:]?\s*\d+\b.+",
        r"^(?:\d+\s*[.)]\s*)?(?:strategic\s+)?(?:tension|dilemma|game)\s*\d*\s*[:.-].+",
        r"^(?:title\s*[:.-]\s*)?.*\b(upstream|downstream|farmers?|fields?|water|irrigat\w*|withdraw\w*|"
        r"extract\w*|allocat\w*|forecast\w*|trust|national\s+authority|fish(?:ing|ery|eries)?|"
        r"catch\w*|harvest\w*|over[- ]?fish\w*|larv\w*|reproduc\w*|threshold|budget|income|"
        r"yield|conserv\w*)\b.*",
    )
    return any(re.search(pattern, lower, re.IGNORECASE) for pattern in candidate_patterns)


def is_title_only_line(raw_line: str) -> bool:
    return bool(re.match(r"^\s*(?:#{2,6}\s*)?\*\*title(?:\*\*)?\s*[:.-]", raw_line, flags=re.I))


def is_action_situation_label_line(raw_line: str) -> bool:
    return bool(re.search(r"\baction[- ]+situation\s*[a-z0-9]*\b", clean_markdown(raw_line), flags=re.I))


def is_contextual_bold_title(lines: list[str], index: int) -> bool:
    stripped = lines[index].strip()
    match = re.match(r"^\*\*(?P<title>.+?)\*\*$", stripped)
    if not match:
        return False

    title = canonical_title(match.group("title"))
    if len(title) < 4 or is_generic_heading(title):
        return False

    for probe in range(index + 1, min(index + 4, len(lines))):
        next_line = clean_markdown(lines[probe])
        if not next_line:
            continue
        return bool(re.match(r"^tension\b", next_line, flags=re.I))
    return False


def has_payoff_evidence(block: str) -> bool:
    lower = block.lower()
    return bool(
        "payoff" in lower
        or "matrix" in lower
        or "\\begin{array}" in lower
        or re.search(r"(?m)^\s*\|(?:\s*:?-{3,}:?\s*\|)+\s*$", block)
    )


def split_markdown_table_row(raw_line: str) -> list[str]:
    stripped = raw_line.strip()
    if not stripped.startswith("|"):
        return []

    row = stripped[1:-1] if stripped.endswith("|") else stripped[1:]
    cells = re.split(r"(?<!\\)\|", row)
    return [clean_markdown(cell.replace(r"\|", "|").strip()) for cell in cells]


def find_table_title_column(cells: list[str]) -> int | None:
    for index, cell in enumerate(cells):
        header = normalize(cell)
        if re.search(r"\btitle\b", header):
            return index
        if re.fullmatch(r"(?:action[- ]?situation|strategic dilemma|game)", header):
            return index
    return None


def is_markdown_table_separator(cells: list[str]) -> bool:
    return bool(cells) and all(
        not cell or bool(re.fullmatch(r":?-{3,}:?", cell.replace(" ", ""))) for cell in cells
    )


def extract_table_action_situations(lines: list[str]) -> list[ActionSituation]:
    situations: list[ActionSituation] = []
    title_column: int | None = None
    identifier_column: int | None = None
    waiting_for_separator = False

    for index, line in enumerate(lines):
        cells = split_markdown_table_row(line)
        if not cells:
            title_column = None
            identifier_column = None
            waiting_for_separator = False
            continue

        if title_column is None:
            candidate_title_column = find_table_title_column(cells)
            if candidate_title_column is None:
                continue
            title_column = candidate_title_column
            identifier_column = next(
                (
                    cell_index
                    for cell_index, cell in enumerate(cells)
                    if normalize(cell) in {"#", "no", "number", "as", "as #", "action situation #"}
                ),
                None,
            )
            waiting_for_separator = True
            continue

        if waiting_for_separator:
            if is_markdown_table_separator(cells):
                waiting_for_separator = False
                continue
            title_column = None
            identifier_column = None
            waiting_for_separator = False
            continue

        if title_column >= len(cells) or is_markdown_table_separator(cells):
            continue
        if identifier_column is not None:
            if identifier_column >= len(cells):
                continue
            identifier = normalize(cells[identifier_column])
            if not re.fullmatch(r"(?:as\s*)?\d+", identifier):
                continue

        title = canonical_title(cells[title_column])
        if len(title) < 4 or is_generic_heading(title):
            continue

        block = " | ".join(cell for cell_index, cell in enumerate(cells) if cell_index != title_column)
        situations.append(ActionSituation(title, block, index + 1, has_payoff_evidence(block)))

    return situations


def json_title_key(item: dict) -> str | None:
    for key in item:
        normalized_key = re.sub(r"[^a-z]+", " ", str(key).lower()).strip()
        if normalized_key == "title" or normalized_key.endswith(" title") or normalized_key in {
            "action situation",
            "action situation name",
        }:
            return key
    return None


def json_action_situation_items(payload: object) -> list[dict]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict) and json_title_key(item)]
    if not isinstance(payload, dict):
        return []
    if json_title_key(payload):
        return [payload]

    for key, value in payload.items():
        normalized_key = re.sub(r"[^a-z]+", " ", str(key).lower()).strip()
        if isinstance(value, list) and (
            "action situation" in normalized_key or normalized_key in {"situations", "results", "analysis"}
        ):
            items = [item for item in value if isinstance(item, dict) and json_title_key(item)]
            if items:
                return items
    return []


def extract_json_action_situations(full_text: str) -> list[ActionSituation]:
    decoder = json.JSONDecoder()

    for match in re.finditer(r"(?m)^\s*(?P<start>[\[{])", full_text):
        start_index = match.start("start")
        try:
            payload, _ = decoder.raw_decode(full_text[start_index:])
        except json.JSONDecodeError:
            continue

        items = json_action_situation_items(payload)
        if not items:
            continue

        base_line = full_text.count("\n", 0, start_index) + 1
        situations: list[ActionSituation] = []
        for item_index, item in enumerate(items):
            title_key = json_title_key(item)
            if title_key is None:
                continue
            title = canonical_title(str(item[title_key]))
            if len(title) < 4 or is_generic_heading(title):
                continue

            block_parts = []
            for key, value in item.items():
                if key == title_key:
                    continue
                rendered_value = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, sort_keys=True)
                block_parts.append(f"{key}: {rendered_value}")
            block = "\n".join(block_parts)
            situations.append(ActionSituation(title, block, base_line + item_index, has_payoff_evidence(block)))
        return situations

    return []


def extract_action_situations(filepath: Path) -> list[ActionSituation]:
    full_text = filepath.read_text(encoding="utf-8")
    lines = full_text.splitlines()
    starts: list[tuple[int, str]] = []

    for index, line in enumerate(lines):
        if is_candidate_start(line) or is_contextual_bold_title(lines, index):
            if (
                is_title_only_line(line)
                and starts
                and index - starts[-1][0] <= 2
                and is_action_situation_label_line(lines[starts[-1][0]])
            ):
                continue
            starts.append((index, canonical_title(line)))

    situations: list[ActionSituation] = []
    for pos, (start_index, title) in enumerate(starts):
        next_start = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
        end_index = next_start

        for probe in range(start_index + 1, next_start):
            raw = lines[probe].strip()
            if re.match(r"^#{2,6}\s+", raw):
                heading = clean_markdown(raw)
                if is_terminal_heading(heading):
                    end_index = probe
                    break

        block = "\n".join(lines[start_index + 1 : end_index]).strip()
        if title and len(title) >= 4:
            situations.append(ActionSituation(title, block, start_index + 1, has_payoff_evidence(block)))

    situations_with_evidence = [situation for situation in situations if situation.has_payoff_evidence]
    if situations_with_evidence:
        return situations_with_evidence
    if situations:
        return situations

    table_situations = extract_table_action_situations(lines)
    if table_situations:
        return table_situations

    json_situations = extract_json_action_situations(full_text)
    if json_situations:
        return json_situations

    if has_payoff_evidence(full_text):
        fallback_title = "Single extracted action situation"
        for line in lines:
            title = clean_markdown(line)
            if title and not title.startswith("Run ") and not is_generic_heading(title):
                fallback_title = canonical_title(title)
                break
        return [ActionSituation(fallback_title, full_text, 1, True)]

    return situations


def has_any(text: str, patterns: tuple[str, ...]) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)


def is_centralized_or_forecast_as(title_text: str) -> bool:
    """Identify an explicitly centralized AS from its title, not incidental body text."""
    return has_any(
        title_text,
        (
            r"\bcentrali[sz](?:ed|ation)?\b|\bcv\b",
            r"\bnational\s+authority\b|\bforecaster\b|\bauthority\s+allocation\b",
            r"\brepresentative\s+farmer\b",
            r"\bforecast(?:ing)?\s+(?:trust|allocation|game|interaction)\b",
            r"\btrust\s+interaction\b|\btrust\s+game\b",
        ),
    )


def has_two_farmer_context(text: str) -> bool:
    return bool(
        (re.search(r"\bup[- ]?stream\b", text) and re.search(r"\bdown[- ]?stream\b", text))
        or re.search(r"\b(?:both|two)\s+farmers?\b", text)
        or re.search(r"\beach\s+farmer\b", text)
        or re.search(r"\bfarmer\s+a\b.*\bfarmer\s+b\b", text, flags=re.DOTALL)
    )


def has_two_fish_user_context(text: str) -> bool:
    if has_two_farmer_context(text):
        return True
    return bool(
        re.search(r"\b(?:both|two)\s+(?:farmers?|fishers?)\b", text)
        or re.search(r"\beach\s+(?:farmer|fisher)\b", text)
        or (
            re.search(r"\b(?:farmer|fisher)\s*a\b", text)
            and re.search(r"\b(?:farmer|fisher)\s*b\b", text)
        )
        or (
            re.search(r"\b(?:(?:down[- ]?stream)(?:\s+(?:farmer|fisher))?|(?:farmer|fisher))\s*1\b", text)
            and re.search(r"\b(?:(?:down[- ]?stream)(?:\s+(?:farmer|fisher))?|(?:farmer|fisher))\s*2\b", text)
        )
        or re.search(r"\bamong\s+(?:the\s+)?down[- ]?stream\s+farmers\b", text)
    )


def title_supports_water_withdrawal(title_text: str) -> bool:
    water_action = has_any(
        title_text,
        (
            r"\bwater[- ]?(?:extraction|withdrawal|appropriation|allocation|competition|conflict|use)\b",
            r"\bwithdraw(?:al|s|ing)?\b|\birrigat(?:e|ion|ing)?\b",
            r"\b(?:field|agricultural)\s+expansion\b",
            r"\bresource\s+extraction\b",
        ),
    )
    strategic_scope = has_any(
        title_text,
        (
            r"\bup[- ]?stream\b|\bdown[- ]?stream\b|\bspatial\b|\basymmetr",
            r"\bsequential\b|\bcompeti(?:tion|ng)\b|\bconflict\b|\brivalry\b|\bdilemma\b|\bgame\b",
            r"\bcommon[- ]pool\b|\bcommons\b|\bdecentrali[sz]ed\b",
        ),
    )
    wrong_domain = has_any(
        title_text,
        (
            r"\bfish(?:ing|ery|eries)?\b|\bcatch\b|\bharvest\b|\blarv",
            r"\bforecast\b|\btrust\b|\bnational\s+authority\b",
            r"\bfarmer\s+vs\.?\s+(?:nature|environment)\b",
            r"\bbounded\s+rationality\b|\bincome\s+threshold\b|\bbudget[- ]risk\b|\brisk[- ]taking\b",
        ),
    )
    return water_action and strategic_scope and not wrong_domain


def matches_upstream_downstream_withdrawal(title_text: str, block_text: str) -> bool:
    full_text = normalize(f"{title_text}\n{block_text}")
    exact_title = bool(
        re.search(r"\bup[- ]?stream\b", title_text)
        and re.search(r"\bdown[- ]?stream\b", title_text)
        and re.search(r"\b(?:water[- ]?)?(?:withdraw|extraction|irrigat|appropriat|allocat)", title_text)
        and not re.search(r"\bfish(?:ing|ery|eries)?\b|\bcatch\b|\bharvest\b", title_text)
    )
    body_has_water_action = has_any(
        full_text,
        (
            r"\bwithdraw(?:al|s|ing)?\b",
            r"\bwater\s+(?:extraction|withdrawal|appropriation|allocation|use|demand|scarcity|stress|access)\b",
            r"\birrigat(?:e|ion|ing)?\b|\bover[- ]?extract(?:ion|s|ing)?\b",
            r"\b(?:low|high|expand|maximi[sz]e|conserve|hold)\b.{0,80}\bfields?\b",
        ),
    )
    return bool(
        (exact_title or title_supports_water_withdrawal(title_text))
        and has_two_farmer_context(full_text)
        and body_has_water_action
    )


def title_supports_fish_extraction(title_text: str) -> bool:
    fish_domain = has_any(title_text, (r"\bfish(?:ing|ery|eries)?\b", r"\blake[- ]fishing\b"))
    extraction_scope = has_any(
        title_text,
        (
            r"\bfishing\b|\bfish(?:ery)?\s+extraction\b",
            r"\bharvest(?:ing)?\b|\bcatch\b|\bover[- ]?fish(?:ing)?\b|\bover[- ]?harvest",
            r"\bexploitation\b|\bpressure\b|\baccess\b|\bpriority\b|\beffort\b|\brace\b",
            r"\bcompetition\b|\bcoordination\b|\bcommon[- ]pool\b|\bcommons\b",
            r"\bcollapse\b|\bdepletion\b|\bsustainability\b|\bdilemma\b|\bgame\b",
        ),
    )
    explicit_harvest = has_any(
        title_text,
        (
            r"\bfishing\b|\bfish\s+extraction\b|\bharvest(?:ing)?\b|\bcatch\b",
            r"\bover[- ]?fish(?:ing)?\b|\bover[- ]?harvest|\bexploitation\b",
        ),
    )
    reproduction_focus = has_any(
        title_text,
        (
            r"\breproduction\b|\blarv|\brecruitment\b|\blake\s+inflow\b|\benvironmental\s+flow\b",
        ),
    )
    cross_resource = has_any(
        title_text,
        (
            r"\bwater[- ]fish\b|\bwater\b.{0,40}\b(?:vs\.?|versus)\b.{0,40}\bfish",
            r"\birrigat\w*\b.{0,50}\bfish|\bfish\w*\b.{0,50}\birrigat",
        ),
    )
    return fish_domain and extraction_scope and not cross_resource and (explicit_harvest or not reproduction_focus)


def has_fish_extraction_choice(text: str) -> bool:
    text = normalize(text)
    return has_any(
        text,
        (
            r"\b(?:both|each)\b.{0,180}\b(?:catch|harvest|fishing\s+(?:effort|strategy|level))\b",
            r"\b(?:choose|decide|select|set|target)\w*\b.{0,120}\b(?:catch|harvest|fishing|fish\s+extraction)\b",
            r"\b(?:low|high|moderate|maximum|maximal|aggressive|conservative|sustainable)\b"
            r"[- ]*(?:catch|harvest|fishing|effort)\b",
            r"\b(?:catch|harvest|fishing\s+(?:effort|strategy)|target\s+catch)\b.{0,120}"
            r"\b(?:low|high|moderate|maximum|maximal|aggressive|conservative|sustainable|restrain|maximi[sz]e)\b",
            r"\bover[- ]?(?:fish|harvest|exploit)\w*\b",
        ),
    )


def is_cross_resource_water_fish_game(block_text: str) -> bool:
    """Reject games where one axis chooses water use and the other chooses fishing."""
    text = block_text.translate(DASH_TRANSLATION).lower()
    compact_text = normalize(block_text)
    upstream_water_role = has_any(
        compact_text,
        (
            r"\bup[- ]?stream\b.{0,180}\b(?:irrigat|water|agricultur|fields?|spring\s+flow)",
            r"\b(?:irrigat|water|agricultur|fields?|spring\s+flow)\b.{0,180}\bup[- ]?stream\b",
        ),
    )
    downstream_fish_role = has_any(
        compact_text,
        (
            r"\bdown[- ]?stream\b.{0,180}\b(?:fish|catch|harvest)",
            r"\b(?:fish|catch|harvest)\b.{0,180}\bdown[- ]?stream\b",
        ),
    )
    role_cross = upstream_water_role and downstream_fish_role

    table_groups: list[list[str]] = []
    current_group: list[str] = []
    for line in text.splitlines():
        if line.lstrip().startswith("|"):
            current_group.append(line)
        elif current_group:
            table_groups.append(current_group)
            current_group = []
    if current_group:
        table_groups.append(current_group)

    table_cross = False
    for group in table_groups:
        if len(group) < 3:
            continue
        header_cells = split_markdown_table_row(group[0])
        separator_cells = split_markdown_table_row(group[1])
        if len(header_cells) < 2 or not is_markdown_table_separator(separator_cells):
            continue

        row_cells = [split_markdown_table_row(line) for line in group[2:]]
        row_labels = " ".join(cells[0] for cells in row_cells if cells)
        column_labels = " ".join(header_cells[1:])

        def has_fish_axis(axis: str) -> bool:
            return has_any(axis, (r"\bfish", r"\bcatch\b|\bharvest|\bover[- ]?fish"))

        def has_water_axis(axis: str) -> bool:
            direct_water = has_any(
                axis,
                (r"\bwater\b|\birrigat|\bfields?\b|\bagri\b|\bagricultur|\bspring\s+flow\b",),
            )
            implicit_water_extraction = role_cross and bool(
                re.search(r"\b(?:over[- ]?)?extract(?:ion)?\b|\bbreach\s+threshold\b", axis)
            )
            return direct_water or implicit_water_extraction

        column_fish = has_fish_axis(column_labels)
        row_fish = has_fish_axis(row_labels)
        column_water = has_water_axis(column_labels)
        row_water = has_water_axis(row_labels)
        if (column_fish and row_water and not row_fish) or (row_fish and column_water and not column_fish):
            table_cross = True
            break

    strategy_cross = has_any(
        compact_text,
        (
            r"\bstrateg(?:y|ies)\s*:?\s*.{0,100}\bup[- ]?stream\b.{0,180}"
            r"\b(?:water|irrigat|fields?|agricultur).{0,300}\bdown[- ]?stream\b.{0,180}"
            r"\b(?:fish|catch|harvest)",
            r"\bactions?\s+(?:for\s+)?(?:the\s+)?up[- ]?stream\b.{0,200}"
            r"\b(?:water|irrigat|fields?|agricultur).{0,500}\bactions?\s+(?:for\s+)?(?:the\s+)?"
            r"down[- ]?stream\b.{0,200}\b(?:fish|catch|harvest)",
        ),
    )
    return table_cross or strategy_cross


def matches_fish_extraction_cpr(title_text: str, block_text: str) -> bool:
    full_text = normalize(f"{title_text}\n{block_text}")
    exact_title = bool(
        re.search(r"\bfish\s+extraction\b", title_text)
        and re.search(r"\bcommon[- ]pool\b|\bcpr\b", title_text)
    )
    self_contained_title = bool(
        re.search(r"\bfish(?:ing|ery)?\b", title_text)
        and re.search(r"\bharvest|\bcatch|\bextraction\b", title_text)
        and re.search(r"\bcoordination\b|\bcompetition\b|\bcommon[- ]pool\b|\bcommons\b|\bgame\b", title_text)
    )
    return bool(
        title_supports_fish_extraction(title_text)
        and not is_cross_resource_water_fish_game(block_text)
        and (
            exact_title
            or self_contained_title
            or (has_two_fish_user_context(full_text) and has_fish_extraction_choice(block_text))
        )
    )


def classify_against_correct_set(situation: ActionSituation) -> str | None:
    title_text = normalize(situation.title)
    full_text = normalize(f"{situation.title}\n{situation.block}")

    # A generated AS number is only formatting; semantic title/body evidence decides the match.
    title_text = re.sub(
        r"^(?:(?:AS\s*[-:]?\s*\d+)|(?:action\s+situation\s*[-:]?\s*\d+))\s*[:.)-]*\s*",
        "",
        title_text,
        flags=re.IGNORECASE,
    )

    if is_centralized_or_forecast_as(title_text):
        return None

    water_match = matches_upstream_downstream_withdrawal(title_text, situation.block)
    fish_match = matches_fish_extraction_cpr(title_text, situation.block)
    title_is_explicit_fish = has_any(
        title_text,
        (
            r"\bfish(?:ing|ery)?\b",
            r"\bcatch\b|\bharvest\b|\bover[- ]?fish|\bover[- ]?exploitation\b",
        ),
    )

    if water_match and not title_is_explicit_fish:
        return "AS1"

    if fish_match:
        return "AS2"

    if water_match:
        return "AS1"

    return None


def calculate_metrics(tp: int, fn: int, fp: int) -> tuple[float, float]:
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    return precision, recall


def evaluate_run(filepath: Path) -> RunResult:
    situations = extract_action_situations(filepath)
    found_gt: set[str] = set()
    fp = 0
    details: list[str] = []
    fp_titles: list[str] = []
    as_reviews: list[ASReview] = []

    for as_index, situation in enumerate(situations, start=1):
        matched_key = classify_against_correct_set(situation)
        title = f"L{situation.line_no}: {situation.title}"

        if matched_key and matched_key not in found_gt:
            found_gt.add(matched_key)
            matched_label = GROUND_TRUTH[matched_key].label
            decision = "TP"
            reason = f"generated AS matches {matched_label}"
            details.append(f"TP [{matched_label}] {title}")
        else:
            fp += 1
            if matched_key:
                matched_label = GROUND_TRUTH[matched_key].label
                decision = "FP-duplicate"
                reason = f"duplicate generated AS for {matched_label}"
            else:
                matched_label = "None"
                decision = "FP-wrong"
                reason = "generated AS is not one of the two confirmed correct ASs"
            details.append(f"{decision} [{matched_label}] {title}")
            fp_titles.append(situation.title)

        as_reviews.append(
            ASReview(
                index=as_index,
                line_no=situation.line_no,
                title=situation.title,
                matched_gt=matched_label,
                decision=decision,
                reason=reason,
                has_payoff_evidence=situation.has_payoff_evidence,
            )
        )

    tp = len(found_gt)
    fn = len(GROUND_TRUTH) - tp
    for key, gt_as in GROUND_TRUTH.items():
        if key not in found_gt:
            details.append(f"FN missed: {gt_as.label}")

    if tp + fp != len(situations):
        raise ValueError(f"Metric invariant failed for {filepath}: TP + FP must equal generated AS count.")
    if tp + fn != len(GROUND_TRUTH):
        raise ValueError(
            f"Metric invariant failed for {filepath}: TP + FN must equal {len(GROUND_TRUTH)} correct ASs."
        )

    precision, recall = calculate_metrics(tp, fn, fp)
    return RunResult(tp, fn, fp, precision, recall, len(situations), found_gt, details, fp_titles, as_reviews)


def write_report_header(out, experiment_name: str) -> None:
    out.write("=" * 78 + "\n")
    out.write(f"TWO-GT EVALUATION: TP / FN / FP ({experiment_name})\n")
    out.write("=" * 78 + "\n\n")
    out.write(f"Correct action situations ({len(GROUND_TRUTH)}):\n")
    for gt_as in GROUND_TRUTH.values():
        out.write(f"  {gt_as.label}\n")
    out.write("\nMetrics:\n")
    out.write("  TP = How many LLM-generated ASs were in the correct set of ASs\n")
    out.write("  FN = How many correct ASs the LLM missed\n")
    out.write("  FP = How many LLM-generated ASs were not in the correct set of ASs\n")
    out.write("  Precision = TP / (TP + FP)\n")
    out.write("  Recall    = TP / (TP + FN)\n\n")
    out.write("Scoring rules:\n")
    out.write("  Each generated AS is reviewed against only the two confirmed correct ASs.\n")
    out.write("  The first generated AS matching a correct AS counts as TP.\n")
    out.write("  Additional generated ASs matching the same correct AS count as FP-duplicate.\n")
    out.write("  Generated ASs matching neither correct AS count as FP-wrong.\n")
    out.write(f"  Missing correct ASs count as FN, so TP + FN = {len(GROUND_TRUTH)} for every run.\n")
    out.write("  Generated AS titles are included with body/matrix text when judging correctness.\n\n")


def evaluate_experiment(experiment_name: str, config: dict) -> tuple[dict, Path, Path, Path]:
    batch_dir = config["batch_dir"]
    report_path = batch_dir / config["report_name"]
    csv_path = batch_dir / config["csv_name"]
    as_csv_path = batch_dir / config["as_csv_name"]
    model_results: dict[str, dict] = {}

    with (
        report_path.open("w", encoding="utf-8") as out,
        csv_path.open("w", newline="", encoding="utf-8") as csvf,
        as_csv_path.open("w", newline="", encoding="utf-8") as as_csvf,
    ):
        writer = csv.writer(csvf, lineterminator="\n")
        as_writer = csv.writer(as_csvf, lineterminator="\n")
        writer.writerow(["Experiment", "Model", "Run", "TP", "FN", "FP", "Precision", "Recall"])
        as_writer.writerow(
            [
                "Experiment",
                "Model",
                "Run",
                "AS_Index",
                "Line",
                "Title",
                "Matched_GT",
                "Decision",
                "Reason",
                "Has_Payoff_Evidence",
            ]
        )

        write_report_header(out, experiment_name)

        for model_index, model_name in enumerate(MODELS, start=1):
            files = sorted((batch_dir / model_name).glob("run_*.md"))
            totals = Counter()
            fp_title_counter: Counter[str] = Counter()

            out.write("\n" + "#" * 78 + "\n")
            out.write(f"MODEL {model_index}: {model_name} ({len(files)} runs)\n")
            out.write("#" * 78 + "\n")

            for filepath in files:
                run_result = evaluate_run(filepath)
                totals.update({"tp": run_result.tp, "fn": run_result.fn, "fp": run_result.fp})
                fp_title_counter.update(run_result.fp_titles)

                out.write(
                    f"\n{filepath.name} | TP={run_result.tp} FN={run_result.fn} FP={run_result.fp} "
                    f"Precision={run_result.precision:.4f} Recall={run_result.recall:.4f}\n"
                )
                for detail in run_result.details:
                    out.write(f"  {detail}\n")

                writer.writerow(
                    [
                        experiment_name,
                        model_name,
                        filepath.name,
                        run_result.tp,
                        run_result.fn,
                        run_result.fp,
                        f"{run_result.precision:.4f}",
                        f"{run_result.recall:.4f}",
                    ]
                )
                for review in run_result.as_reviews:
                    as_writer.writerow(
                        [
                            experiment_name,
                            model_name,
                            filepath.name,
                            review.index,
                            review.line_no,
                            review.title,
                            review.matched_gt,
                            review.decision,
                            review.reason,
                            1 if review.has_payoff_evidence else 0,
                        ]
                    )

            tp = totals["tp"]
            fn = totals["fn"]
            fp = totals["fp"]
            precision, recall = calculate_metrics(tp, fn, fp)
            model_results[model_name] = {
                "tp": tp,
                "fn": fn,
                "fp": fp,
                "runs": len(files),
                "precision": precision,
                "recall": recall,
                "top_fp_titles": fp_title_counter.most_common(5),
            }

            out.write("\n" + "-" * 78 + "\n")
            out.write(f"{model_name} TOTALS\n")
            out.write("-" * 78 + "\n")
            out.write(f"TP = {tp:<5} FN = {fn:<5} FP = {fp}\n")
            out.write(f"Precision = TP/(TP+FP) = {tp}/({tp}+{fp}) = {precision:.4f}\n")
            out.write(f"Recall    = TP/(TP+FN) = {tp}/({tp}+{fn}) = {recall:.4f}\n")

            print(
                f"{experiment_name} | {model_name}: TP={tp}, FN={fn}, FP={fp}, "
                f"Precision={precision:.4f}, Recall={recall:.4f}"
            )

        out.write("\n\n" + "#" * 78 + "\n")
        out.write(f"FINAL MODEL COMPARISON: {experiment_name}\n")
        out.write("#" * 78 + "\n\n")
        out.write(f"{'Model':<20} {'TP':>4} {'FN':>4} {'FP':>4} {'Precision':>10} {'Recall':>8}\n")
        out.write("-" * 70 + "\n")
        for model_name, result in model_results.items():
            out.write(
                f"{model_name:<20} {result['tp']:>4} {result['fn']:>4} {result['fp']:>4} "
                f"{result['precision']:>10.4f} {result['recall']:>8.4f}\n"
            )

    return model_results, report_path, csv_path, as_csv_path


def write_cross_comparison(results_by_experiment: dict[str, dict]) -> Path:
    comparison_path = CURRENT_DIR / "Water_evaluation_comparison_ODD+game_stuff_vs_ODD-only.txt"

    with comparison_path.open("w", encoding="utf-8") as out:
        out.write("=" * 78 + "\n")
        out.write("TWO-GT COMPARISON: ODD+game_stuff VS ODD-only\n")
        out.write("=" * 78 + "\n\n")
        out.write(f"Correct action situations ({len(GROUND_TRUTH)}):\n")
        for gt_as in GROUND_TRUTH.values():
            out.write(f"  {gt_as.label}\n")
        out.write("\n")

        out.write("Side-by-side totals:\n")
        out.write(
            f"{'Model':<20} {'Evaluation':<16} {'TP':>4} {'FN':>4} {'FP':>4} "
            f"{'Precision':>10} {'Recall':>8}\n"
        )
        out.write("-" * 76 + "\n")
        for model_name in MODELS:
            for experiment_name in ("ODD+game_stuff", "ODD-only"):
                result = results_by_experiment[experiment_name][model_name]
                out.write(
                    f"{model_name:<20} {experiment_name:<16} {result['tp']:>4} "
                    f"{result['fn']:>4} {result['fp']:>4} {result['precision']:>10.4f} "
                    f"{result['recall']:>8.4f}\n"
                )

        out.write("\nDifferences (ODD+game_stuff minus ODD-only):\n")
        out.write(
            f"{'Model':<20} {'Delta TP':>8} {'Delta FN':>8} {'Delta FP':>8} "
            f"{'Delta Prec':>11} {'Delta Recall':>13}\n"
        )
        out.write("-" * 78 + "\n")
        for model_name in MODELS:
            game = results_by_experiment["ODD+game_stuff"][model_name]
            odd = results_by_experiment["ODD-only"][model_name]
            out.write(
                f"{model_name:<20} "
                f"{game['tp'] - odd['tp']:>+8} "
                f"{game['fn'] - odd['fn']:>+8} "
                f"{game['fp'] - odd['fp']:>+8} "
                f"{game['precision'] - odd['precision']:>+11.4f} "
                f"{game['recall'] - odd['recall']:>+13.4f}\n"
            )

        out.write("\nAudit notes:\n")
        out.write("  Only TP, FN, FP, Precision, and Recall are evaluated.\n")
        out.write("  AS-level CSVs list every generated AS and whether it is TP, FP-duplicate, or FP-wrong.\n")
        out.write(f"  Per-run invariant: TP + FN = {len(GROUND_TRUTH)} confirmed correct ASs.\n")
        out.write("  Generated AS titles are included with body/matrix text when judging correctness.\n")

    return comparison_path


def main() -> None:
    results_by_experiment: dict[str, dict] = {}
    report_paths: list[tuple[Path, Path, Path]] = []

    for experiment_name, config in EXPERIMENTS.items():
        results, report_path, csv_path, as_csv_path = evaluate_experiment(experiment_name, config)
        results_by_experiment[experiment_name] = results
        report_paths.append((report_path, csv_path, as_csv_path))

    comparison_path = write_cross_comparison(results_by_experiment)

    print("\nReports:")
    for report_path, csv_path, as_csv_path in report_paths:
        print(f"  Detailed: {report_path}")
        print(f"  CSV:      {csv_path}")
        print(f"  AS audit: {as_csv_path}")
    print(f"  Compare:  {comparison_path}")


if __name__ == "__main__":
    main()

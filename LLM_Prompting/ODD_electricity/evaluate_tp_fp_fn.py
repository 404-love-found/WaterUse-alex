"""
Evaluate electricity action-situation extraction outputs against the six
ground-truth action situations in Txts/TXT/odd.txt section III.iv.a.

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
        "batch_dir": CURRENT_DIR / "ODD_alex+desciption_alex" / "Result-30Runs_ODD+gamestuff" / "Result",
        "report_name": "Electricity_evaluation_ODD+game_stuff.txt",
        "csv_name": "Electricity_evaluation_summary_ODD+game_stuff.csv",
        "as_csv_name": "Electricity_evaluation_as_level_ODD+game_stuff.csv",
    },
    "ODD-only": {
        "batch_dir": CURRENT_DIR / "ODD_alex+desciption_alex" / "Result-30Runs_ODD" / "Result",
        "report_name": "Electricity_evaluation_ODD-only.txt",
        "csv_name": "Electricity_evaluation_summary_ODD-only.csv",
        "as_csv_name": "Electricity_evaluation_as_level_ODD-only.csv",
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
    has_representation_evidence: bool


@dataclass(frozen=True)
class ASReview:
    index: int
    line_no: int
    title: str
    matched_gt: str
    decision: str
    reason: str
    has_representation_evidence: bool


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
    "AS1": GroundTruthAS("AS1", "Capacitor-adoption assurance game between neighbouring farmers"),
    "AS2": GroundTruthAS("AS2", "Sequential social-learning process in capacitor adoption"),
    "AS3": GroundTruthAS("AS3", "Asymmetric transformer-capacity authorization dilemma between farmers"),
    "AS4": GroundTruthAS("AS4", "Mutual-exchange coordination game between farmer and sub-station staff"),
    "AS5": GroundTruthAS("AS5", "Authorization-and-investment asymmetric coordination between farmer and staff"),
    "AS6": GroundTruthAS("AS6", "Groundwater-extraction prisoner's dilemma between farmers"),
}


def clean_markdown(text: str) -> str:
    cleaned = text.strip()
    cleaned = re.sub(r"^#{1,6}\s*", "", cleaned)
    cleaned = re.sub(r"^\s*[-*]\s+", "", cleaned)
    cleaned = re.sub(r"^\*+|\*+$", "", cleaned.strip())
    cleaned = cleaned.replace("**", "")
    cleaned = re.sub(r"`", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip(" :-")


def canonical_title(text: str) -> str:
    title = clean_markdown(text)
    title = re.sub(r"^\d+\s*[.)]\s*(?:title\s*[:.-]\s*)?", "", title, flags=re.IGNORECASE)
    title = re.sub(r"^title\s*[:.-]\s*", "", title, flags=re.IGNORECASE)
    title = re.sub(
        r"^(?:action\s+situation|strategic\s+dilemma|dilemma|game)\s*\d*\s*[:.)-]\s*",
        "",
        title,
        flags=re.IGNORECASE,
    )
    title = re.sub(
        r"^\d+\s*[.)]\s*(?:strategic\s+)?(?:tension|dilemma|game|action\s+situation)\s*[:.-]\s*",
        "",
        title,
        flags=re.IGNORECASE,
    )
    return clean_markdown(title)


def normalize(text: str) -> str:
    text = clean_markdown(text).lower()
    for dash in ("‐", "‑", "‒", "–", "—", "−"):
        text = text.replace(dash, "-")
    return text


def has_any(text: str, patterns: tuple[str, ...]) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)


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
    if lower in {
        "matrix",
        "payoff matrix",
        "sequential representation",
        "game tree",
        "justification",
        "tension",
        "assumptions",
    }:
        return True
    if re.match(
        r"^(matrix|payoff matrix|representation|sequential representation|game tree|justification|"
        r"assumptions|tension|payoff|interpretation)\b",
        lower,
    ):
        return True
    if re.match(r"^(analysis|extracted|distinct action situations|action situation analysis)\b", lower):
        return True
    if lower.startswith("title:"):
        stripped = re.sub(r"^title:\s*", "", lower).strip()
        if re.search(r"\b(model|analysis|action situations?|strategic tensions?|strategic dilemmas?)\b", stripped):
            return True
    if re.search(r"\b(action situations?|strategic tensions?)\b", lower) and re.search(
        r"\b(analysis|model|distinct|version)\b", lower
    ):
        return True
    return False


def is_structured_field_line(raw_line: str) -> bool:
    """Reject numbered ODD/IAD fields that belong inside an AS block."""
    title = normalize(canonical_title(raw_line))
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
        r"compliance with odd\+?d",
    )
    return bool(re.match(rf"^(?:{'|'.join(field_names)})(?:\s*[:(\-]|$)", title))


def is_internal_game_tree_step(raw_line: str) -> bool:
    """Reject decision-tree nodes and moves that are not separate AS titles."""
    title = normalize(canonical_title(raw_line))
    if re.match(r"^(?:stage\s*\d+|node\s+[a-z0-9]+)\b", title):
        return True
    return bool(
        re.match(
            r"^(?:farmer|staff|player\s*\d*|nature|utility|regulator)\s+"
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
        re.match(
            r"^(?:#{2,6}\s*)?(?:\*\*)?title(?:\*\*)?\s*[:.-]\s*\S",
            stripped,
            flags=re.I,
        )
    )
    is_numbered_plain_title = bool(
        re.match(
            r"^\d+\s*[.)]\s+(?:\*\*)?title(?:\*\*)?\s*[:.-]\s*\S",
            stripped,
            flags=re.I,
        )
    )
    is_plain_action_situation = bool(
        re.match(
            r"^(?:action\s+situation|strategic\s+dilemma|game)\s*\d+\s*[:.)-]\s*\S",
            stripped,
            flags=re.I,
        )
    )
    is_bold_title = bool(
        re.match(r"^\*\*(?:title|action\s+situation\s*\d*|strategic\s+dilemma\s*\d*|game\s*\d*)", stripped, re.I)
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
        r"\baction\s+situation\s*\d*\b.+",
        r"\bAS\s*[-:]?\s*\d+\b.+",
        r"^(?:\d+\s*[.)]\s*)?(?:strategic\s+)?(?:tension|dilemma|game)\s*\d*\s*[:.-].+",
        r".*\b(capacitor|voltage|social[- ]?learning|diffusion|imitat|peer|sequential|transformer|"
        r"capacity|authori[sz]ation|authori[sz]e|free[- ]?rid|contribut|volunteer|mutual[- ]?exchange|"
        r"informal[- ]?exchange|recipro|collusion|staff|sub[- ]?station|formal|informal|enforcement|"
        r"maintenance|connection|groundwater|aquifer|over[- ]?extract|depletion|prisoner|coordination|"
        r"assurance)\b.*",
    )
    return any(re.search(pattern, lower, re.IGNORECASE) for pattern in candidate_patterns)


def is_title_only_line(raw_line: str) -> bool:
    return bool(
        re.match(
            r"^\s*(?:#{2,6}\s*)?(?:\*\*)?title(?:\*\*)?\s*[:.-]",
            raw_line,
            flags=re.I,
        )
    )


def is_action_situation_label_line(raw_line: str) -> bool:
    return bool(re.search(r"\baction\s+situation\s*\d*\b", clean_markdown(raw_line), flags=re.I))


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


def has_representation_evidence(block: str) -> bool:
    lower = block.lower()
    return bool(
        "payoff" in lower
        or "matrix" in lower
        or "sequential representation" in lower
        or "game tree" in lower
        or "sequence" in lower
        or "\\begin{array}" in lower
        or re.search(r"\n\s*\|.+\|\s*\n\s*\|[-:|\s]+\|", block)
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
        not cell or bool(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")))
        for cell in cells
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
        situations.append(
            ActionSituation(
                title=title,
                block=block,
                line_no=index + 1,
                has_representation_evidence=has_representation_evidence(block),
            )
        )

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
                if isinstance(value, str):
                    rendered_value = value
                else:
                    rendered_value = json.dumps(value, ensure_ascii=False, sort_keys=True)
                block_parts.append(f"{key}: {rendered_value}")
            block = "\n".join(block_parts)
            situations.append(
                ActionSituation(
                    title=title,
                    block=block,
                    line_no=base_line + item_index,
                    has_representation_evidence=has_representation_evidence(block),
                )
            )
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
            situations.append(ActionSituation(title, block, start_index + 1, has_representation_evidence(block)))

    situations_with_evidence = [s for s in situations if s.has_representation_evidence]
    if situations_with_evidence:
        return situations_with_evidence

    table_situations = extract_table_action_situations(lines)
    if table_situations:
        return table_situations

    json_situations = extract_json_action_situations(full_text)
    if json_situations:
        return json_situations

    if has_representation_evidence(full_text):
        fallback_title = "Single extracted action situation"
        for line in lines:
            title = clean_markdown(line)
            if title and not title.startswith("Run ") and not is_generic_heading(title):
                fallback_title = canonical_title(title)
                break
        return [ActionSituation(fallback_title, full_text, 1, True)]

    return situations


def classify_against_correct_set(situation: ActionSituation) -> str | None:
    title_text = normalize(situation.title)
    full_text = normalize(f"{situation.title}\n{situation.block}")

    # A model-assigned AS number is not evidence of correctness. Strip it and
    # classify the generated title/body against the ground-truth semantics.
    title_text = re.sub(
        r"^(?:(?:AS\s*[-:]?\s*\d+)|(?:action\s+situation\s*[-:]?\s*\d+))\s*[:.)-]*\s*",
        "",
        title_text,
        flags=re.IGNORECASE,
    )

    staff_context = has_any(full_text, (r"\bstaff\b|\bsub[- ]?station\b|\butility\b",))
    farmer_context = has_any(full_text, (r"\bfarmer",))
    farmer_farmer_context = has_any(
        full_text,
        (r"\btwo farmers\b|\bfarmer[- ]?farmer\b|\bneighbou?ring farmers\b|\bfarmer 1\b|\bfarmer 2\b",),
    )

    # Title-first rules avoid generic explanatory text pulling a block into the wrong class.
    if has_any(
        title_text,
        (r"\bgroundwater\b|\baquifer\b|\bover[- ]?extract|\bdepletion\b|\brecharge\b|\bwater\s+table\b",),
    ):
        return "AS6"
    if has_any(
        title_text,
        (r"\bsocial[- ]?learning\b|\bdiffusion\b|\bimitat|\bobserv|\blearn(?:ing)?\b|\btrial\b",),
    ):
        return "AS2"
    if has_any(title_text, (r"\bmutual[- ]?exchange\b|\binformal[- ]?exchange\b|\brecipro|\bcollusion|collusive|\bfavor|\bfavour\b",)):
        return "AS4"

    title_has_authorization = has_any(
        title_text,
        (
            r"\bauthori[sz](?:e[ds]?|ation)?\b",
            r"\bformal[- ]?connection\b",
            r"\bregulari[sz](?:e[ds]?|ation)\b",
            r"\bformalisation\b|\bformalization\b",
        ),
    )
    title_has_investment = has_any(title_text, (r"\binvest|\bcapacity\s+upgrade",))
    title_has_as5_pairing = has_any(
        title_text,
        (
            r"\bauthori[sz]ation.*(?:investment|enforcement)\b",
            r"\b(?:investment|enforcement).*authori[sz]ation\b",
            r"\bformal[- ]?connection\b",
            r"\binvest.*(?:regulari[sz]|formali[sz])\b",
            r"\b(?:regulari[sz]|formali[sz]).*invest\b",
            r"\bauthori[sz]ation\s+(?:game|decision|coordination)\b",
            r"\bconnection\s+authori[sz]ation\b",
        ),
    )
    if title_has_authorization and title_has_investment:
        return "AS5"
    if title_has_as5_pairing and not farmer_farmer_context and (staff_context or not farmer_context):
        return "AS5"
    if title_has_authorization and staff_context and farmer_context and not farmer_farmer_context:
        return "AS5"

    if has_any(title_text, (r"\bcapacitor\b|\bvoltage[- ]?stabili|\bassurance\b",)):
        return "AS1"
    if has_any(
        title_text,
        (r"\bauthori[sz](?:ed|ation)?\s+connections?\b|\bconnections?\s+authori[sz]ation\b",),
    ) and (farmer_farmer_context or not staff_context):
        return "AS3"
    if has_any(title_text, (r"\btransformer\b|\bcapacity\b|\bfree[- ]?rid|\bvolunteer|\bcontribut",)):
        if farmer_farmer_context or not staff_context:
            return "AS3"

    # These are distinct extra situations; generic body text must not turn them into AS5.
    if has_any(
        title_text,
        (
            r"\bmaintenance\b|\bworkload\b",
            r"\benforcement\s+(?:game|decision|dilemma)\b",
            r"\bcapacity\s+provision\b",
        ),
    ) and not (title_has_authorization or title_has_as5_pairing):
        return None

    social_score = len(re.findall(r"social[- ]?learning|diffusion|imitat|observ|learn(?:ing)?|trial", full_text))
    capacitor_score = len(re.findall(r"capacitor", full_text))
    voltage_stability_score = len(re.findall(r"voltage[- ]?stabili", full_text))
    adoption_score = len(re.findall(r"adopt", full_text))
    groundwater_score = len(re.findall(r"groundwater|aquifer|over[- ]?extract|extraction|depletion|recharge", full_text))
    exchange_score = len(re.findall(r"mutual[- ]?exchange|informal[- ]?exchange|recipro|collusion|collusive|favor|favour|trust", full_text))
    staff_score = len(re.findall(r"staff|sub[- ]?station|utility", full_text))
    formal_score = len(re.findall(r"formal|informal|authori[sz]ation|authori[sz]e|enforce|withhold|maintenance|connection|invest", full_text))
    transformer_score = len(re.findall(r"transformer|capacity|free[- ]?rid|contribut|volunteer|upgrade", full_text))
    farmer_farmer_score = len(re.findall(r"two farmers|farmer[- ]?farmer|neighbou?r|farmer 1|farmer 2", full_text))

    if social_score >= 2 and (capacitor_score >= 1 or voltage_stability_score >= 1 or adoption_score >= 1):
        return "AS2"
    if groundwater_score >= 2:
        return "AS6"
    if exchange_score >= 2 and staff_score >= 1:
        return "AS4"
    has_staff_authorization_core = has_any(
        full_text,
        (
            r"\bauthori[sz](?:e[ds]?|ation)?\b.*\binvest",
            r"\binvest.*\bauthori[sz](?:e[ds]?|ation)?\b",
            r"\bformal[- ]?connection\b",
            r"\bregulari[sz](?:e[ds]?|ation)\b.*\binvest",
            r"\binvest.*\bregulari[sz](?:e[ds]?|ation)\b",
        ),
    )
    if staff_score >= 1 and farmer_context and formal_score >= 2 and has_staff_authorization_core:
        return "AS5"
    has_capacity_authorization_core = has_any(
        full_text,
        (
            r"\btransformer\s+capacity\b",
            r"\bauthori[sz](?:ed|ation)?\s+connections?\b",
            r"\bcapacity\s+(?:contribut|provision|upgrade|authori[sz])",
        ),
    )
    if (
        transformer_score >= 2
        and has_capacity_authorization_core
        and (farmer_farmer_score >= 1 or staff_score == 0)
    ):
        return "AS3"
    if capacitor_score >= 1:
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
                reason = "generated AS is not one of the six confirmed correct ASs"
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
                has_representation_evidence=situation.has_representation_evidence,
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
    out.write(f"ELECTRICITY EVALUATION: TP / FN / FP ({experiment_name})\n")
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
    out.write("  Each generated AS is reviewed against only the six confirmed correct ASs.\n")
    out.write("  The first generated AS matching a correct AS counts as TP.\n")
    out.write("  Additional generated ASs matching the same correct AS count as FP-duplicate.\n")
    out.write("  Generated ASs matching none of the correct ASs count as FP-wrong.\n")
    out.write(f"  Missing correct ASs count as FN, so TP + FN = {len(GROUND_TRUTH)} for every run.\n")
    out.write("  Generated AS titles are included with body/matrix/sequential text when judging correctness.\n\n")


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
        writer = csv.writer(csvf)
        as_writer = csv.writer(as_csvf)
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
                "Has_Representation_Evidence",
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
                            1 if review.has_representation_evidence else 0,
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
    comparison_path = (
        CURRENT_DIR
        / "ODD_alex+desciption_alex"
        / "Electricity_evaluation_comparison_ODD+game_stuff_vs_ODD-only.txt"
    )

    with comparison_path.open("w", encoding="utf-8") as out:
        out.write("=" * 78 + "\n")
        out.write("ELECTRICITY COMPARISON: ODD+game_stuff VS ODD-only\n")
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
        out.write("  Generated AS titles are included with body/matrix/sequential text when judging correctness.\n")

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

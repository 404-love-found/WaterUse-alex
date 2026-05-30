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

MODELS = ("DeepSeek-R1", "DeepSeek-V4-Pro", "Llama-3.3-70B", "Qwen2.5-7B")


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
    title = clean_markdown(text).replace("**", "")
    title = re.sub(r"^\*\*(title|action\s+situation\s*\d*|strategic\s+dilemma\s*\d*)\*\*\s*[:.-]\s*", "", title, flags=re.I)
    title = re.sub(r"^title\s*[:.-]\s*", "", title, flags=re.IGNORECASE)
    title = re.sub(
        r"^(?:action\s+situation|strategic\s+dilemma|tension)\s*\d*\s*[:.)-]\s*",
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
    if lower in {"matrix", "payoff matrix", "2-player", "justification", "tension", "assumptions"}:
        return True
    if re.match(r"^(matrix|payoff matrix|2-player|justification|assumptions)\b", lower):
        return True
    if re.match(r"^(analysis|extracted|distinct action situations|action situation analysis)\b", lower):
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


def is_candidate_start(raw_line: str) -> bool:
    stripped = raw_line.strip()
    if not stripped or stripped.startswith("# Run "):
        return False

    is_heading = bool(re.match(r"^#{2,6}\s+", stripped))
    is_bold_title = bool(re.match(r"^\*\*(?:title|action\s+situation\s*\d*|strategic\s+dilemma\s*\d*)", stripped, re.I))
    if not is_heading and not is_bold_title:
        return False

    title = clean_markdown(stripped)
    if is_generic_heading(title):
        return False

    lower = title.lower()
    candidate_patterns = (
        r"\baction\s+situation\s*\d*\b.+",
        r"^(?:\d+\s*[.)]\s*)?(?:strategic\s+)?(?:tension|dilemma)\s*\d*\s*[:.-].+",
        r"^(?:title\s*[:.-]\s*)?.*\b(upstream|downstream|farmer|water|irrigat|withdraw|extract|"
        r"allocat|forecast|trust|national\s+authority|fish|fishing|fishery|catch|harvest|"
        r"overfish|larv|reproduction|threshold|budget|income|yield|conservation)\b.*",
    )
    return any(re.search(pattern, lower, re.IGNORECASE) for pattern in candidate_patterns)


def is_title_only_line(raw_line: str) -> bool:
    return bool(re.match(r"^\s*(?:#{2,6}\s*)?\*\*title(?:\*\*)?\s*[:.-]", raw_line, flags=re.I))


def is_action_situation_label_line(raw_line: str) -> bool:
    return bool(re.search(r"\baction\s+situation\s*\d*\b", clean_markdown(raw_line), flags=re.I))


def has_payoff_evidence(block: str) -> bool:
    lower = block.lower()
    return bool(
        "payoff" in lower
        or "matrix" in lower
        or "\\begin{array}" in lower
        or re.search(r"\n\s*\|.+\|\s*\n\s*\|[-:|\s]+\|", block)
    )


def extract_action_situations(filepath: Path) -> list[ActionSituation]:
    lines = filepath.read_text(encoding="utf-8").splitlines()
    starts: list[tuple[int, str]] = []

    for index, line in enumerate(lines):
        if is_candidate_start(line):
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

    situations_with_evidence = [s for s in situations if s.has_payoff_evidence]
    if situations_with_evidence:
        return situations_with_evidence

    full_text = "\n".join(lines)
    if has_payoff_evidence(full_text):
        fallback_title = "Single extracted action situation"
        for line in lines:
            title = clean_markdown(line)
            if title and not title.startswith("Run ") and not is_generic_heading(title):
                fallback_title = canonical_title(title)
                break
        return [ActionSituation(fallback_title, full_text, 1, True)]

    return situations


def normalize(text: str) -> str:
    text = clean_markdown(text).lower()
    return text.replace("‐", "-").replace("–", "-").replace("—", "-")


def has_any(text: str, patterns: tuple[str, ...]) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)


def is_centralized_or_forecast_as(text: str) -> bool:
    return has_any(
        text,
        (
            r"\bcentralized\s+version\b|\bcv\b",
            r"\bnational\s+authority\b|\bforecaster\b|\ballocator\b",
            r"\bforecast(?:ing|s|er)?\b",
            r"\brepresentative\s+farmer\b",
            r"\btrust\s+interaction\b|\btrust\s+game\b",
        ),
    )


def is_fish_reproduction_only(text: str) -> bool:
    reproduction_cues = has_any(
        text,
        (
            r"\bfish[- ]?reproduction\b|\breproduction\b|\breproductive\b",
            r"\blarv(?:a|ae|al)\b|\brecruitment\b",
            r"\bmay\b.*\b(irrigat|flow|withdraw|conserv|delay)\b",
            r"\bthreshold\b.*\b(fish|larv|lake|inflow|reproduction|stock)\b",
            r"\b(fish|lake)\b.*\bthreshold\b",
            r"\bhold\s+irrigation\b|\bdelay\b.*\birrigat",
        ),
    )
    extraction_cues = has_any(
        text,
        (
            r"\bcatch(?:es|ing)?\b|\btarget\s+catch\b|\bcatch\s+level\b",
            r"\bharvest(?:ing|ed|s)?\b|\bover[- ]?harvest(?:ing|ed|s)?\b",
            r"\bfishing\s+(decision|effort|access|competition|priority|order|race|resource|management|game|dilemma)\b",
            r"\bfish\s+extraction\b|\bover[- ]?fish(?:ing)?\b",
        ),
    )
    return reproduction_cues and not extraction_cues


def matches_fish_extraction_cpr(title_text: str, full_text: str) -> bool:
    direct_extraction = has_any(
        full_text,
        (
            r"\bfish\s+extraction\b",
            r"\bfishing\s+(decision|effort|access|competition|priority|order|race|resource|management|game|dilemma|lake)\b",
            r"\bfishing\s+over(?:exploitation|extraction)\b",
            r"\bfishery\b|\bfisheries\b|\bfisher\b",
            r"\bcatch(?:es|ing)?\b|\btarget\s+catch\b|\bcatch\s+level\b|\bamount\s+of\s+fish\b",
            r"\bharvest(?:ing|ed|s)?\b|\bover[- ]?harvest(?:ing|ed|s)?\b",
            r"\bover[- ]?fish(?:ing)?\b|\bsustainable\s+catch\b",
            r"\bcommon[- ]pool\s+fish(?:ery|eries|resource)?\b",
        ),
    )
    strategic_resource = has_any(
        full_text,
        (
            r"\bcommon[- ]pool\b|\bcpr\b",
            r"\bstock\s+(collapse|depletion|sustainability|coordination|management)\b",
            r"\bpopulation\s+(declines?|collapse|sustainability|healthy)\b",
            r"\bover(?:exploitation|harvest|fishing)\b",
            r"\bconserv(?:e|es|ation)\b",
            r"\bcoordination\b|\bassurance\b|\bstag[- ]?hunt\b|\bdilemma\b|\bgame\b",
        ),
    )
    title_is_fish_cpr = has_any(
        title_text,
        (
            r"\bfish(?:ing|ery)?\b.*\b(common[- ]pool|over[- ]?exploitation|harvest|catch|coordination|sustainability|dilemma|game|competition|access|priority|race)\b",
            r"\b(common[- ]pool|over[- ]?exploitation|harvest|catch|coordination|sustainability|dilemma|game|competition|access|priority|race)\b.*\bfish(?:ing|ery)?\b",
            r"\bover[- ]?exploitation\b.*\bfish\b|\bfish\b.*\bover[- ]?exploitation\b",
        ),
    )
    return (direct_extraction and strategic_resource) or title_is_fish_cpr


def matches_upstream_downstream_withdrawal(title_text: str, full_text: str) -> bool:
    spatial = has_any(
        full_text,
        (
            r"\bupstream\b",
            r"\bdownstream\b",
            r"\bspatial\s+asymmetr",
            r"\briver\s+position\b",
        ),
    )
    withdrawal = has_any(
        full_text,
        (
            r"\bwithdraw(?:al|s|ing)?\b",
            r"\bwater\s+(extraction|withdrawal|allocation|use|demand|scarcity|stress|access)\b",
            r"\birrigat(?:e|ion|ing)?\b",
            r"\bfields?\b",
            r"\bconserv(?:e|es|ing|ation)\s+water\b",
            r"\bover[- ]?extract(?:ion|s|ing)?\b",
        ),
    )
    title_support = has_any(
        title_text,
        (
            r"\bupstream\b|\bdownstream\b|\bspatial\s+asymmetr",
            r"\bwater\b|\birrigat|\bwithdraw|\bextraction\b|\ballocation\b",
        ),
    )
    title_not_other_as = not has_any(
        title_text,
        (
            r"\bfish[- ]?reproduction\b|\blarv|\bforecast|\bnational\s+authority\b|\btrust\b",
            r"\bbudget\s+constraints?\b",
        ),
    )
    return spatial and withdrawal and title_support and title_not_other_as


def classify_against_correct_set(situation: ActionSituation) -> str | None:
    title_text = normalize(situation.title)
    full_text = normalize(f"{situation.title}\n{situation.block}")

    if is_centralized_or_forecast_as(full_text):
        return None

    water_match = matches_upstream_downstream_withdrawal(title_text, full_text)
    fish_match = matches_fish_extraction_cpr(title_text, full_text) and not is_fish_reproduction_only(full_text)
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

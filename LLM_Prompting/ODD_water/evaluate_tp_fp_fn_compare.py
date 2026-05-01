"""
Evaluate water-use action-situation extraction outputs.

Ground truth:
  AS1: Upstream and downstream withdrawal decisions
  AS2: Fish extraction common pool resource game

This is the single scorer for both experiments:
  - ODD+game_stuff: Batch_30Runs/
  - ODD-only:       Batch_30Runs_ODDOnly/
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
    },
    "ODD-only": {
        "batch_dir": CURRENT_DIR / "Batch_30Runs_ODDOnly",
        "report_name": "Water_evaluation_ODD-only.txt",
        "csv_name": "Water_evaluation_summary_ODD-only.csv",
    },
}

MODELS = ("DeepSeek-R1", "Llama-3.3-70B", "Qwen2.5-7B")


@dataclass(frozen=True)
class ActionSituation:
    title: str
    block: str
    line_no: int
    has_payoff_evidence: bool


@dataclass
class RunResult:
    tp: int
    fp: int
    fn: int
    total_as: int
    precision: float
    recall: float
    f1: float
    found_water: bool
    found_fish: bool
    details: list[str] = field(default_factory=list)
    fp_titles: list[str] = field(default_factory=list)


def clean_markdown(text: str) -> str:
    """Strip Markdown markers while preserving the semantic title text."""
    cleaned = text.strip()
    cleaned = re.sub(r"^#{1,6}\s*", "", cleaned)
    cleaned = re.sub(r"^\s*[-*]\s+", "", cleaned)
    cleaned = cleaned.strip()
    cleaned = re.sub(r"^\*+|\*+$", "", cleaned)
    cleaned = re.sub(r"`", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip(" :-")


def canonical_title(text: str) -> str:
    title = clean_markdown(text)
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
    lower = title.lower()
    return bool(
        re.match(
            r"^(summary|conclusion|notes?|key\s+(constraints|notes|insights|reflections)|"
            r"thought\s+process|final\s+answer|reflections?)\b",
            lower,
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
        if re.search(
            r"\b(model|analysis|action situations?|strategic tensions?|strategic dilemmas?|"
            r"decentralized water use)\b",
            stripped,
        ):
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
    is_bold_title = bool(
        re.match(r"^\*\*(?:title|action\s+situation\s*\d*|strategic\s+dilemma\s*\d*)\s*:", stripped, re.I)
    )
    if not is_heading and not is_bold_title:
        return False

    title = clean_markdown(stripped)
    lower = title.lower()
    if is_generic_heading(title):
        return False

    candidate_patterns = (
        r"\baction\s+situation\s*\d*\b.+",
        r"^(?:\d+\s*[.)]\s*)?(?:strategic\s+)?(?:tension|dilemma)\s*\d*\s*[:.-].+",
        r"^(?:title\s*[:.-]\s*)?.*\b(upstream|downstream|water|irrigat|withdraw|extract|allocat|"
        r"fish|fishing|fishery|fisheries|catch|harvest|overfish|common[- ]pool|commons|cpr|"
        r"lake|threshold|risk|budget|memory|income|yield|conservation|sustainability)\b.*",
    )
    return any(re.search(pattern, lower, re.IGNORECASE) for pattern in candidate_patterns)


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
        if not title or len(title) < 4:
            continue
        situations.append(
            ActionSituation(
                title=title,
                block=block,
                line_no=start_index + 1,
                has_payoff_evidence=has_payoff_evidence(block),
            )
        )

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
        return [
            ActionSituation(
                title=fallback_title,
                block=full_text,
                line_no=1,
                has_payoff_evidence=True,
            )
        ]

    return situations


def has_water_as(text: str) -> bool:
    lower = text.lower()
    has_spatial_players = bool(re.search(r"\b(upstream|downstream)\b|spatial\s+asymmetr", lower))
    has_withdrawal_decision = bool(
        re.search(r"\b(water|irrigat|withdraw|extraction|allocation|fields?|flow|demand)\b", lower)
    )
    return has_spatial_players and has_withdrawal_decision


def has_fish_cpr_as(text: str) -> bool:
    lower = text.lower()
    has_fish_resource = bool(re.search(r"\b(fish|fishing|fishery|fisheries)\b", lower))
    has_extraction_action = bool(
        re.search(
            r"\b(fishing\s+(decision|effort|access|competition|pressure|level|needs)|"
            r"decision\s+to\s+fish|fish(?:ing)?\s+decision|fish(?:ing)?\s+commons|"
            r"common[- ]pool\s+fish|fish\s+extraction|sustainable\s+fishing|"
            r"fish\s+responsibly|fish(?:es|ing)?\s+\d+|fish\s+(more|less)|"
            r"fishing\s+activities|over[- ]?fish(?:ing)?|target\s+catch|catch\s+level|"
            r"catch\s+(amount|level|more|less)|amount\s+of\s+fish|fish\s+catch\s+decision|"
            r"fish\s+harvest|harvest\s+fish|harvest\s+sustainably|over[- ]?harvest|"
            r"over-catch|race\s+to\s+fish)\b",
            lower,
        )
    )
    return has_fish_resource and has_extraction_action


def classify_action_situation(situation: ActionSituation) -> str:
    title_text = situation.title
    full_text = f"{situation.title}\n{situation.block}"

    title_is_water = has_water_as(title_text)
    title_is_fish = has_fish_cpr_as(title_text)

    if title_is_water and not title_is_fish:
        return "water"
    if title_is_fish and not title_is_water:
        return "fish"
    if has_water_as(full_text) and not has_fish_cpr_as(title_text):
        return "water"
    if has_fish_cpr_as(full_text):
        return "fish"
    return "other"


def calculate_metrics(tp: int, fp: int, fn: int) -> tuple[float, float, float]:
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    return precision, recall, f1


def evaluate_run(filepath: Path) -> RunResult:
    situations = extract_action_situations(filepath)
    found_water = False
    found_fish = False
    fp = 0
    details: list[str] = []
    fp_titles: list[str] = []

    for situation in situations:
        category = classify_action_situation(situation)
        title = f"L{situation.line_no}: {situation.title}"

        if category == "water" and not found_water:
            found_water = True
            details.append(f"TP [water] {title}")
        elif category == "fish" and not found_fish:
            found_fish = True
            details.append(f"TP [fish]  {title}")
        else:
            fp += 1
            label = "duplicate" if category in {"water", "fish"} else "wrong"
            details.append(f"FP [{label}] {title}")
            fp_titles.append(situation.title)

    tp = int(found_water) + int(found_fish)
    fn = int(not found_water) + int(not found_fish)
    if not found_water:
        details.append("FN missed: Upstream and downstream withdrawal decisions")
    if not found_fish:
        details.append("FN missed: Fish extraction common pool resource game")

    precision, recall, f1 = calculate_metrics(tp, fp, fn)
    return RunResult(
        tp=tp,
        fp=fp,
        fn=fn,
        total_as=len(situations),
        precision=precision,
        recall=recall,
        f1=f1,
        found_water=found_water,
        found_fish=found_fish,
        details=details,
        fp_titles=fp_titles,
    )


def write_report_header(out, experiment_name: str) -> None:
    out.write("=" * 78 + "\n")
    out.write(f"FINAL EVALUATION: TP / FP / FN ({experiment_name})\n")
    out.write("=" * 78 + "\n\n")
    out.write("Ground Truth (2 correct action situations):\n")
    out.write("  AS1: Upstream and downstream withdrawal decisions\n")
    out.write("  AS2: Fish extraction common pool resource game\n\n")
    out.write("Metrics:\n")
    out.write("  TP = How many LLM-generated ASs were correct\n")
    out.write("  FN = How many correct ASs the LLM missed\n")
    out.write("  FP = How many LLM-generated ASs were wrong\n")
    out.write("  Precision = TP / (TP + FP)\n")
    out.write("  Recall    = TP / (TP + FN)\n")
    out.write("  F1 Score  = 2 * Precision * Recall / (Precision + Recall)\n\n")


def summarize_failure_pattern(result: dict) -> str:
    if result["fp"] > result["fn"]:
        return "main loss: extra or duplicate action situations"
    if result["fn"] > result["fp"]:
        return "main loss: missed ground-truth action situations"
    if result["fp"] == 0 and result["fn"] == 0:
        return "perfect against this scorer"
    return "balanced FP/FN errors"


def evaluate_experiment(experiment_name: str, config: dict) -> tuple[dict, Path, Path]:
    batch_dir = config["batch_dir"]
    report_path = batch_dir / config["report_name"]
    csv_path = batch_dir / config["csv_name"]
    model_results: dict[str, dict] = {}

    with report_path.open("w", encoding="utf-8") as out, csv_path.open("w", newline="", encoding="utf-8") as csvf:
        writer = csv.writer(csvf)
        writer.writerow(
            [
                "Experiment",
                "Model",
                "Run",
                "TP",
                "FP",
                "FN",
                "Total_AS",
                "Precision",
                "Recall",
                "F1",
                "Found_Water",
                "Found_Fish",
            ]
        )

        write_report_header(out, experiment_name)

        for model_index, model_name in enumerate(MODELS, start=1):
            model_dir = batch_dir / model_name
            files = sorted(model_dir.glob("run_*.md"))
            totals = Counter()
            water_found_count = 0
            fish_found_count = 0
            fp_title_counter: Counter[str] = Counter()

            out.write("\n" + "#" * 78 + "\n")
            out.write(f"MODEL {model_index}: {model_name} ({len(files)} runs)\n")
            out.write("#" * 78 + "\n")

            for filepath in files:
                run_result = evaluate_run(filepath)
                totals.update({"tp": run_result.tp, "fp": run_result.fp, "fn": run_result.fn})
                water_found_count += int(run_result.found_water)
                fish_found_count += int(run_result.found_fish)
                fp_title_counter.update(run_result.fp_titles)

                out.write(
                    f"\n{filepath.name} | TP={run_result.tp} FP={run_result.fp} FN={run_result.fn} "
                    f"Precision={run_result.precision:.4f} Recall={run_result.recall:.4f} "
                    f"F1={run_result.f1:.4f}\n"
                )
                out.write(f"Generated ASs evaluated: {run_result.total_as}\n")
                for detail in run_result.details:
                    out.write(f"  {detail}\n")

                writer.writerow(
                    [
                        experiment_name,
                        model_name,
                        filepath.name,
                        run_result.tp,
                        run_result.fp,
                        run_result.fn,
                        run_result.total_as,
                        f"{run_result.precision:.4f}",
                        f"{run_result.recall:.4f}",
                        f"{run_result.f1:.4f}",
                        1 if run_result.found_water else 0,
                        1 if run_result.found_fish else 0,
                    ]
                )

            n_runs = len(files)
            tp = totals["tp"]
            fp = totals["fp"]
            fn = totals["fn"]
            precision, recall, f1 = calculate_metrics(tp, fp, fn)
            result = {
                "tp": tp,
                "fp": fp,
                "fn": fn,
                "runs": n_runs,
                "precision": precision,
                "recall": recall,
                "f1": f1,
                "water_count": water_found_count,
                "fish_count": fish_found_count,
                "water_pct": water_found_count / n_runs * 100 if n_runs else 0.0,
                "fish_pct": fish_found_count / n_runs * 100 if n_runs else 0.0,
                "top_fp_titles": fp_title_counter.most_common(5),
            }
            model_results[model_name] = result

            out.write("\n" + "-" * 78 + "\n")
            out.write(f"{model_name} TOTALS\n")
            out.write("-" * 78 + "\n")
            out.write(f"TP = {tp:<5} FP = {fp:<5} FN = {fn}\n")
            out.write(f"Avg/run: TP={tp / n_runs:.2f} FP={fp / n_runs:.2f} FN={fn / n_runs:.2f}\n")
            out.write(f"Precision = TP/(TP+FP) = {tp}/({tp}+{fp}) = {precision:.4f}\n")
            out.write(f"Recall    = TP/(TP+FN) = {tp}/({tp}+{fn}) = {recall:.4f}\n")
            out.write(f"F1 Score  = {f1:.4f}\n")
            out.write(f"Water AS correctly identified: {water_found_count}/{n_runs} runs ({result['water_pct']:.1f}%)\n")
            out.write(f"Fish  AS correctly identified: {fish_found_count}/{n_runs} runs ({result['fish_pct']:.1f}%)\n")
            out.write(f"Assessment: {summarize_failure_pattern(result)}\n")
            if fp_title_counter:
                out.write("Most common FP titles:\n")
                for title, count in fp_title_counter.most_common(5):
                    out.write(f"  {count}x {title}\n")

            print(
                f"{experiment_name} | {model_name}: TP={tp}, FP={fp}, FN={fn}, "
                f"Precision={precision:.4f}, Recall={recall:.4f}, F1={f1:.4f}"
            )

        out.write("\n\n" + "#" * 78 + "\n")
        out.write(f"FINAL MODEL COMPARISON: {experiment_name}\n")
        out.write("#" * 78 + "\n\n")
        out.write(f"{'Model':<20} {'TP':>4} {'FP':>4} {'FN':>4} {'Precision':>10} {'Recall':>8} {'F1':>8}\n")
        out.write("-" * 78 + "\n")
        for model_name, result in model_results.items():
            out.write(
                f"{model_name:<20} {result['tp']:>4} {result['fp']:>4} {result['fn']:>4} "
                f"{result['precision']:>10.4f} {result['recall']:>8.4f} {result['f1']:>8.4f}\n"
            )

    return model_results, report_path, csv_path


def explain_delta(game_result: dict, odd_result: dict) -> str:
    delta_f1 = game_result["f1"] - odd_result["f1"]
    delta_fp = game_result["fp"] - odd_result["fp"]
    delta_fn = game_result["fn"] - odd_result["fn"]

    if delta_f1 > 0:
        return "ODD+game_stuff is better: higher F1 under the same scorer."
    if delta_f1 == 0:
        return "Tie: both prompts have the same F1 under the same scorer."
    if delta_fp > 0 and delta_fn <= 0:
        return "ODD+game_stuff is worse mainly because it generated more extra or duplicate ASs."
    if delta_fn > 0 and delta_fp <= 0:
        return "ODD+game_stuff is worse mainly because it missed more ground-truth ASs."
    return "ODD+game_stuff is worse because the FP/FN tradeoff lowered F1."


def write_cross_comparison(results_by_experiment: dict[str, dict]) -> Path:
    comparison_path = CURRENT_DIR / "Water_evaluation_comparison_ODD+game_stuff_vs_ODD-only.txt"
    game_results = results_by_experiment["ODD+game_stuff"]
    odd_results = results_by_experiment["ODD-only"]

    with comparison_path.open("w", encoding="utf-8") as out:
        out.write("=" * 78 + "\n")
        out.write("COMPARISON EVALUATION: ODD+game_stuff VS ODD-only\n")
        out.write("=" * 78 + "\n\n")
        out.write("Ground Truth (2 correct action situations):\n")
        out.write("  AS1: Upstream and downstream withdrawal decisions\n")
        out.write("  AS2: Fish extraction common pool resource game\n\n")
        out.write("Both experiments were evaluated with the same Markdown parser and scorer.\n\n")

        out.write("Side-by-side totals:\n")
        out.write(
            f"{'Model':<20} {'Evaluation':<16} {'TP':>4} {'FP':>4} {'FN':>4} "
            f"{'Precision':>10} {'Recall':>8} {'F1':>8} {'Water':>12} {'Fish':>12}\n"
        )
        out.write("-" * 110 + "\n")
        for model_name in MODELS:
            for experiment_name in ("ODD+game_stuff", "ODD-only"):
                result = results_by_experiment[experiment_name][model_name]
                water = f"{result['water_count']}/{result['runs']}"
                fish = f"{result['fish_count']}/{result['runs']}"
                out.write(
                    f"{model_name:<20} {experiment_name:<16} {result['tp']:>4} "
                    f"{result['fp']:>4} {result['fn']:>4} {result['precision']:>10.4f} "
                    f"{result['recall']:>8.4f} {result['f1']:>8.4f} {water:>12} {fish:>12}\n"
                )

        out.write("\nDifferences (ODD+game_stuff minus ODD-only):\n")
        out.write(
            f"{'Model':<20} {'Delta TP':>8} {'Delta FP':>8} {'Delta FN':>8} "
            f"{'Delta Prec':>11} {'Delta Recall':>13} {'Delta F1':>10} "
            f"{'Delta Water':>13} {'Delta Fish':>11}\n"
        )
        out.write("-" * 112 + "\n")
        for model_name in MODELS:
            game = game_results[model_name]
            odd = odd_results[model_name]
            out.write(
                f"{model_name:<20} "
                f"{game['tp'] - odd['tp']:>+8} "
                f"{game['fp'] - odd['fp']:>+8} "
                f"{game['fn'] - odd['fn']:>+8} "
                f"{game['precision'] - odd['precision']:>+11.4f} "
                f"{game['recall'] - odd['recall']:>+13.4f} "
                f"{game['f1'] - odd['f1']:>+10.4f} "
                f"{game['water_count'] - odd['water_count']:>+13} "
                f"{game['fish_count'] - odd['fish_count']:>+11}\n"
            )

        out.write("\nExpectation check:\n")
        out.write("  Expected: ODD+game_stuff should outperform ODD-only.\n")
        for model_name in MODELS:
            game = game_results[model_name]
            odd = odd_results[model_name]
            out.write(f"  {model_name}: {explain_delta(game, odd)}\n")
            if game["f1"] < odd["f1"]:
                out.write(f"    ODD+game_stuff top FP titles: {format_top_titles(game['top_fp_titles'])}\n")
                out.write(f"    ODD-only top FP titles:       {format_top_titles(odd['top_fp_titles'])}\n")

        out.write("\nInput and scorer audit notes:\n")
        out.write("  Batch_30Runs is generated from Txts/odd.txt + Txts/game_stuff.txt.\n")
        out.write("  Batch_30Runs_ODDOnly is generated from Txts/odd.txt only.\n")
        out.write(
            "  Txts/odd.txt already contains detailed Fishing, Fish population growth, "
            "WaterFlow, and Budget calculation submodel text, so ODD-only is not a "
            "minimal baseline without game mechanics.\n"
        )
        out.write(
            "  The scorer skips document-level Title headings and only evaluates blocks "
            "with payoff-matrix evidence; fish AS detection requires fish extraction "
            "actions such as fishing decision, overfishing, catch level, or harvest.\n"
        )

    return comparison_path


def format_top_titles(items: list[tuple[str, int]]) -> str:
    if not items:
        return "none"
    return "; ".join(f"{count}x {title}" for title, count in items[:3])


def main() -> None:
    results_by_experiment: dict[str, dict] = {}
    report_paths: list[tuple[Path, Path]] = []

    for experiment_name, config in EXPERIMENTS.items():
        results, report_path, csv_path = evaluate_experiment(experiment_name, config)
        results_by_experiment[experiment_name] = results
        report_paths.append((report_path, csv_path))

    comparison_path = write_cross_comparison(results_by_experiment)

    print("\nReports:")
    for report_path, csv_path in report_paths:
        print(f"  Detailed: {report_path}")
        print(f"  CSV:      {csv_path}")
    print(f"  Compare:  {comparison_path}")


if __name__ == "__main__":
    main()

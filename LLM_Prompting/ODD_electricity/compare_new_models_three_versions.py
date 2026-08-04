"""Compare Qwen3.7-Plus and gpt-oss-120b across three electricity versions."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import evaluate_tp_fp_fn as base


CURRENT_DIR = Path(__file__).resolve().parent
NEW_MODELS = ("Qwen3.7-Plus", "gpt-oss-120b")

VERSIONS = {
    "ODD_alex+desciption_alex": {
        "root": CURRENT_DIR / "ODD_alex+desciption_alex",
        "csv_prefix": "Electricity_evaluation_summary_",
    },
    "ODD_jennifer+desciption_jennifer": {
        "root": CURRENT_DIR / "ODD_jennifer+desciption_jennifer",
        "csv_prefix": "Jennifer_Electricity_evaluation_summary_",
    },
    "ODD_jennifer+desciption_alex": {
        "root": CURRENT_DIR / "ODD_jennifer+desciption_alex",
        "csv_prefix": "AlexPrompt_JenniferODD_evaluation_summary_",
    },
}

CONDITIONS = {
    "ODD+game_stuff": {
        "directory": "Result-30Runs_ODD+gamestuff",
        "filename_suffix": "ODD+game_stuff.csv",
    },
    "ODD-only": {
        "directory": "Result-30Runs_ODD",
        "filename_suffix": "ODD-only.csv",
    },
}


def calculate_metrics(tp: int, fn: int, fp: int) -> tuple[float, float]:
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return precision, recall


def load_totals(csv_path: Path, model: str) -> dict[str, int | float]:
    totals: Counter[str] = Counter()
    runs = 0
    generated_counts: list[int] = []
    perfect_runs = 0
    low_as_runs = 0
    trailing_whitespace_runs = 0

    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            if row["Model"] != model:
                continue
            runs += 1
            tp = int(row["TP"])
            fn = int(row["FN"])
            fp = int(row["FP"])
            totals.update(
                {
                    "tp": tp,
                    "fn": fn,
                    "fp": fp,
                }
            )
            generated_count = tp + fp
            generated_counts.append(generated_count)
            perfect_runs += int(tp == len(base.GROUND_TRUTH) and fp == 0)
            low_as_runs += int(generated_count <= 1)

            result_path = csv_path.parent / model / row["Run"]
            if not result_path.is_file():
                raise FileNotFoundError(f"Missing result referenced by evaluation CSV: {result_path}")
            result_text = result_path.read_text(encoding="utf-8")
            trailing_whitespace_runs += int(len(result_text) - len(result_text.rstrip()) > 10_000)

    if runs != 30:
        raise ValueError(f"Expected 30 runs for {model} in {csv_path}, found {runs}.")
    if totals["tp"] + totals["fn"] != len(base.GROUND_TRUTH) * runs:
        raise ValueError(f"TP + FN invariant failed for {model} in {csv_path}.")

    precision, recall = calculate_metrics(totals["tp"], totals["fn"], totals["fp"])
    return {
        "runs": runs,
        "tp": totals["tp"],
        "fn": totals["fn"],
        "fp": totals["fp"],
        "precision": precision,
        "recall": recall,
        "mean_generated": sum(generated_counts) / runs,
        "perfect_runs": perfect_runs,
        "low_as_runs": low_as_runs,
        "trailing_whitespace_runs": trailing_whitespace_runs,
    }


def collect_results() -> dict[str, dict[str, dict[str, dict[str, int | float]]]]:
    results: dict[str, dict[str, dict[str, dict[str, int | float]]]] = {}

    for version, version_config in VERSIONS.items():
        results[version] = {}
        for condition, condition_config in CONDITIONS.items():
            csv_path = (
                version_config["root"]
                / condition_config["directory"]
                / "Result"
                / f"{version_config['csv_prefix']}{condition_config['filename_suffix']}"
            )
            if not csv_path.is_file():
                raise FileNotFoundError(f"Missing evaluation CSV: {csv_path}")
            results[version][condition] = {
                model: load_totals(csv_path, model) for model in NEW_MODELS
            }

    return results


def write_csv(results: dict) -> Path:
    output_path = CURRENT_DIR / "Electricity_new_models_three_versions_summary.csv"
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            ["Version", "Condition", "Model", "Runs", "TP", "FN", "FP", "Precision", "Recall"]
        )
        for version in VERSIONS:
            for condition in CONDITIONS:
                for model in NEW_MODELS:
                    result = results[version][condition][model]
                    writer.writerow(
                        [
                            version,
                            condition,
                            model,
                            result["runs"],
                            result["tp"],
                            result["fn"],
                            result["fp"],
                            f"{result['precision']:.4f}",
                            f"{result['recall']:.4f}",
                        ]
                    )
    return output_path


def write_report(results: dict) -> Path:
    output_path = CURRENT_DIR / "Electricity_new_models_three_versions_comparison.txt"
    with output_path.open("w", encoding="utf-8") as report:
        report.write("=" * 100 + "\n")
        report.write("ELECTRICITY: TWO NEW MODELS ACROSS THREE ODD/DESCRIPTION VERSIONS\n")
        report.write("=" * 100 + "\n\n")
        report.write("Models: Qwen3.7-Plus and gpt-oss-120b\n")
        report.write("Runs: 30 per model, version, and condition\n")
        report.write("Metrics: TP, FN, FP, Precision, Recall only\n")
        report.write(f"Ground truth: {len(base.GROUND_TRUTH)} correct action situations per run\n\n")

        report.write(
            f"{'Version':<40} {'Condition':<16} {'Model':<15} {'TP':>4} {'FN':>4} "
            f"{'FP':>4} {'Precision':>10} {'Recall':>8}\n"
        )
        report.write("-" * 107 + "\n")
        for version in VERSIONS:
            for condition in CONDITIONS:
                for model in NEW_MODELS:
                    result = results[version][condition][model]
                    report.write(
                        f"{version:<40} {condition:<16} {model:<15} "
                        f"{result['tp']:>4} {result['fn']:>4} {result['fp']:>4} "
                        f"{result['precision']:>10.4f} {result['recall']:>8.4f}\n"
                    )

        report.write("\nODD+game_stuff minus ODD-only:\n")
        report.write(
            f"{'Version':<40} {'Model':<15} {'Delta TP':>8} {'Delta FN':>8} "
            f"{'Delta FP':>8} {'Delta Prec':>11} {'Delta Recall':>13}\n"
        )
        report.write("-" * 108 + "\n")
        for version in VERSIONS:
            for model in NEW_MODELS:
                game = results[version]["ODD+game_stuff"][model]
                odd = results[version]["ODD-only"][model]
                report.write(
                    f"{version:<40} {model:<15} "
                    f"{game['tp'] - odd['tp']:>+8} "
                    f"{game['fn'] - odd['fn']:>+8} "
                    f"{game['fp'] - odd['fp']:>+8} "
                    f"{game['precision'] - odd['precision']:>+11.4f} "
                    f"{game['recall'] - odd['recall']:>+13.4f}\n"
                )

        report.write("\nOutput-quality diagnostics (audit evidence, not evaluation metrics):\n")
        report.write(
            f"{'Version':<40} {'Condition':<16} {'Model':<15} {'Mean AS':>8} "
            f"{'Runs <=1 AS':>12} {'Perfect':>8} {'Whitespace':>11}\n"
        )
        report.write("-" * 116 + "\n")
        for version in VERSIONS:
            for condition in CONDITIONS:
                for model in NEW_MODELS:
                    result = results[version][condition][model]
                    report.write(
                        f"{version:<40} {condition:<16} {model:<15} "
                        f"{result['mean_generated']:>8.2f} {result['low_as_runs']:>12} "
                        f"{result['perfect_runs']:>8} {result['trailing_whitespace_runs']:>11}\n"
                    )

        report.write("\nInterpretation:\n")
        report.write(
            "- Qwen3.7-Plus is effectively tied at ceiling for ODD_alex+desciption_alex: "
            "ODD+game_stuff missed one correct AS, while both conditions produced no FP.\n"
        )
        report.write(
            "- For both Jennifer-ODD versions, Qwen3.7-Plus improves with game_stuff: "
            "it recovers more correct capacity/authorization situations while generating fewer wrong or duplicate ASs.\n"
        )
        report.write(
            "- gpt-oss-120b is worse in recall with game_stuff in all three versions. In the Alex and hybrid "
            "versions, game_stuff also has more runs with only zero/one extracted AS and more large trailing-whitespace "
            "outputs, showing incomplete or degenerate completions despite successful API calls. The longer prompt is "
            "a plausible contributor, but this is an inference from the observed outputs rather than a proven API cause.\n"
        )
        report.write(
            "- In ODD_jennifer+desciption_jennifer, gpt-oss-120b shows a precision-recall tradeoff rather than a pure "
            "decline: game_stuff loses three TP but removes nine FP, so precision rises while recall falls slightly.\n"
        )
        report.write("\nEvaluation audit rules:\n")
        report.write("- Only TP, FN, FP, Precision, and Recall are performance metrics.\n")
        report.write("- Generated titles and their associated body/representation are reviewed together.\n")
        report.write("- Model-assigned AS numbers do not establish correctness.\n")
        report.write("- ODD/IAD fields, payoff-matrix headings, and game-tree steps are not counted as separate ASs.\n")

    return output_path


def main() -> None:
    results = collect_results()
    csv_path = write_csv(results)
    report_path = write_report(results)
    print(f"CSV: {csv_path}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()

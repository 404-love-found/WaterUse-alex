"""
Evaluate Jennifer electricity action-situation extraction outputs with the
same TP/FN/FP rules used by evaluate_tp_fp_fn.py.

This wrapper keeps the original evaluator as the single source of scoring logic
and only changes the input/output directories for Jennifer's 30-run results.
"""

from __future__ import annotations

from pathlib import Path

import evaluate_tp_fp_fn as base


CURRENT_DIR = Path(__file__).resolve().parent

MODELS = ("DeepSeek-V4-Pro", "Llama-3.3-70B", "Qwen2.5-7B")

EXPERIMENTS = {
    "ODD+game_stuff": {
        "batch_dir": CURRENT_DIR / "Result-jennifer" / "Result-30Runs_ODD+gamestuff" / "Result",
        "report_name": "Jennifer_Electricity_evaluation_ODD+game_stuff.txt",
        "csv_name": "Jennifer_Electricity_evaluation_summary_ODD+game_stuff.csv",
        "as_csv_name": "Jennifer_Electricity_evaluation_as_level_ODD+game_stuff.csv",
    },
    "ODD-only": {
        "batch_dir": CURRENT_DIR / "Result-jennifer" / "Result-30Runs_ODD" / "Result",
        "report_name": "Jennifer_Electricity_evaluation_ODD-only.txt",
        "csv_name": "Jennifer_Electricity_evaluation_summary_ODD-only.csv",
        "as_csv_name": "Jennifer_Electricity_evaluation_as_level_ODD-only.csv",
    },
}


def write_jennifer_cross_comparison(results_by_experiment: dict[str, dict]) -> Path:
    comparison_path = (
        CURRENT_DIR
        / "Result-jennifer"
        / "Jennifer_Electricity_evaluation_comparison_ODD+game_stuff_vs_ODD-only.txt"
    )

    with comparison_path.open("w", encoding="utf-8") as out:
        out.write("=" * 78 + "\n")
        out.write("JENNIFER ELECTRICITY COMPARISON: ODD+game_stuff VS ODD-only\n")
        out.write("=" * 78 + "\n\n")
        out.write(f"Correct action situations ({len(base.GROUND_TRUTH)}):\n")
        for gt_as in base.GROUND_TRUTH.values():
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
        out.write(f"  Per-run invariant: TP + FN = {len(base.GROUND_TRUTH)} confirmed correct ASs.\n")
        out.write("  Generated AS titles are included with body/matrix/sequential text when judging correctness.\n")

    return comparison_path


def main() -> None:
    base.MODELS = MODELS

    results_by_experiment: dict[str, dict] = {}
    report_paths: list[tuple[Path, Path, Path]] = []

    for experiment_name, config in EXPERIMENTS.items():
        results, report_path, csv_path, as_csv_path = base.evaluate_experiment(experiment_name, config)
        results_by_experiment[experiment_name] = results
        report_paths.append((report_path, csv_path, as_csv_path))

    comparison_path = write_jennifer_cross_comparison(results_by_experiment)

    print("\nJennifer reports:")
    for report_path, csv_path, as_csv_path in report_paths:
        print(f"  Detailed: {report_path}")
        print(f"  CSV:      {csv_path}")
        print(f"  AS audit: {as_csv_path}")
    print(f"  Compare:  {comparison_path}")


if __name__ == "__main__":
    main()

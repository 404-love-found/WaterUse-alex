"""Evaluate the Alex-prompt + Jennifer-ODD electricity experiment.

The scoring logic and six ground-truth action situations come directly from
evaluate_tp_fp_fn.py. Generated AS titles remain part of the text used for
classification, together with each AS body and representation.
"""

from __future__ import annotations

from pathlib import Path

import evaluate_tp_fp_fn as base


CURRENT_DIR = Path(__file__).resolve().parent
RESULT_ROOT = CURRENT_DIR / "ODD_jennifer+desciption_alex"

MODELS = (
    "DeepSeek-V4-Pro",
    "Llama-3.3-70B",
    "Qwen2.5-7B",
    "Qwen3.7-Plus",
    "gpt-oss-120b",
)

EXPERIMENTS = {
    "ODD+game_stuff": {
        "batch_dir": RESULT_ROOT / "Result-30Runs_ODD+gamestuff" / "Result",
        "report_name": "AlexPrompt_JenniferODD_evaluation_ODD+game_stuff.txt",
        "csv_name": "AlexPrompt_JenniferODD_evaluation_summary_ODD+game_stuff.csv",
        "as_csv_name": "AlexPrompt_JenniferODD_evaluation_as_level_ODD+game_stuff.csv",
    },
    "ODD-only": {
        "batch_dir": RESULT_ROOT / "Result-30Runs_ODD" / "Result",
        "report_name": "AlexPrompt_JenniferODD_evaluation_ODD-only.txt",
        "csv_name": "AlexPrompt_JenniferODD_evaluation_summary_ODD-only.csv",
        "as_csv_name": "AlexPrompt_JenniferODD_evaluation_as_level_ODD-only.csv",
    },
}


def write_cross_comparison(results_by_experiment: dict[str, dict]) -> Path:
    comparison_path = (
        RESULT_ROOT
        / "AlexPrompt_JenniferODD_comparison_ODD+game_stuff_vs_ODD-only.txt"
    )

    with comparison_path.open("w", encoding="utf-8") as out:
        out.write("=" * 78 + "\n")
        out.write("ALEX PROMPT + JENNIFER ODD: ODD+game_stuff VS ODD-only\n")
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
                    f"{result['fn']:>4} {result['fp']:>4} "
                    f"{result['precision']:>10.4f} {result['recall']:>8.4f}\n"
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
        out.write("  Metrics: TP, FN, FP, Precision, and Recall only.\n")
        out.write("  AS titles and AS body text are both used during classification.\n")
        out.write("  Duplicate matches count as FP; each correct AS can count once per run.\n")
        out.write(f"  Per-run invariant: TP + FN = {len(base.GROUND_TRUTH)}.\n")

    return comparison_path


def main() -> None:
    base.MODELS = MODELS
    results_by_experiment: dict[str, dict] = {}
    report_paths: list[tuple[Path, Path, Path]] = []

    for experiment_name, config in EXPERIMENTS.items():
        results, report_path, csv_path, as_csv_path = base.evaluate_experiment(
            experiment_name,
            config,
        )
        results_by_experiment[experiment_name] = results
        report_paths.append((report_path, csv_path, as_csv_path))

    comparison_path = write_cross_comparison(results_by_experiment)

    print("\nAlex-prompt + Jennifer-ODD reports:")
    for report_path, csv_path, as_csv_path in report_paths:
        print(f"  Detailed: {report_path}")
        print(f"  CSV:      {csv_path}")
        print(f"  AS audit: {as_csv_path}")
    print(f"  Compare:  {comparison_path}")


if __name__ == "__main__":
    main()

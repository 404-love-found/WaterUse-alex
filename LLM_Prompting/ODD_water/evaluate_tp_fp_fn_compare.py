"""
Evaluate and compare water-use ODD+game_stuff vs ODD-only runs with one scorer.

This script exists to avoid comparing reports produced by different scoring
passes. Both experiments use evaluate_tp_fp_fn.evaluate_run.
"""

import csv
import os

from evaluate_tp_fp_fn import evaluate_run


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

EXPERIMENTS = {
    "ODD+game_stuff": {
        "batch_dir": os.path.join(CURRENT_DIR, "Batch_30Runs"),
        "report_name": "Water_evaluation_ODD+game_stuff.txt",
        "csv_name": "Water_evaluation_summary_ODD+game_stuff.csv",
    },
    "ODD-only": {
        "batch_dir": os.path.join(CURRENT_DIR, "Batch_30Runs_ODDOnly"),
        "report_name": "Water_evaluation_ODD-only.txt",
        "csv_name": "Water_evaluation_summary_ODD-only.csv",
    },
}

MODELS = {
    "DeepSeek-R1": "DeepSeek-R1",
    "Llama-3.3-70B": "Llama-3.3-70B",
    "Qwen2.5-7B": "Qwen2.5-7B",
}


def calculate_metrics(tp, fp, fn):
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = (2 * precision * recall / (precision + recall)
          if (precision + recall) > 0 else 0)
    return precision, recall, f1


def format_detail(detail):
    text = detail.strip()
    if text.startswith("TP(water):"):
        return "  TP: [water] " + text.replace("TP(water):", "", 1).strip()
    if text.startswith("TP(fish):"):
        return "  TP: [fish]  " + text.replace("TP(fish):", "", 1).strip()
    if text.startswith("FP(dup):"):
        return "  FP: [duplicate] " + text.replace("FP(dup):", "", 1).strip()
    if text.startswith("FP:"):
        return "  FP: " + text.replace("FP:", "", 1).strip()
    if "FN: missed" in text and "upstream/downstream" in text:
        return "  FN missed: Upstream and downstream withdrawal decisions"
    if "FN: missed" in text and "fish extraction" in text:
        return "  FN missed: Fish extraction CPR"
    return "  " + text


def write_header(out, experiment_name):
    out.write("=" * 70 + "\n")
    out.write(f"  FINAL EVALUATION: TP / FP / FN ({experiment_name})\n")
    out.write("=" * 70 + "\n\n")
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


def evaluate_experiment(experiment_name, config):
    batch_dir = config["batch_dir"]
    report_path = os.path.join(batch_dir, config["report_name"])
    csv_path = os.path.join(batch_dir, config["csv_name"])
    all_model_results = {}

    with open(report_path, "w", encoding="utf-8") as out, \
         open(csv_path, "w", newline="", encoding="utf-8") as csvf:
        writer = csv.writer(csvf)
        writer.writerow([
            "Experiment", "Model", "Run", "TP", "FP", "FN", "Total_AS",
            "Precision", "Recall", "F1", "Found_Water", "Found_Fish",
        ])

        write_header(out, experiment_name)

        for model_index, (model_name, model_subdir) in enumerate(MODELS.items(), start=1):
            model_dir = os.path.join(batch_dir, model_subdir)
            files = sorted([f for f in os.listdir(model_dir) if f.endswith(".md")])
            all_tp = all_fp = all_fn = 0
            water_found_count = 0
            fish_found_count = 0

            out.write("\n" + "#" * 70 + "\n")
            out.write(f"  MODEL {model_index}: {model_name}  ({len(files)} runs)\n")
            out.write("#" * 70 + "\n")

            for fname in files:
                fpath = os.path.join(model_dir, fname)
                tp, fp, fn, n_as, details, fw, ff = evaluate_run(fpath)
                precision, recall, f1 = calculate_metrics(tp, fp, fn)

                all_tp += tp
                all_fp += fp
                all_fn += fn
                water_found_count += int(fw)
                fish_found_count += int(ff)

                run_no = os.path.splitext(fname)[0].replace("run_", "")
                out.write(f"\nRun {run_no} | TP={tp}  FP={fp}  FN={fn}\n")
                out.write(f"  Generated ASs: {n_as}\n")
                for detail in details:
                    out.write(format_detail(detail) + "\n")

                writer.writerow([
                    experiment_name, model_name, fname, tp, fp, fn, n_as,
                    f"{precision:.4f}", f"{recall:.4f}", f"{f1:.4f}",
                    1 if fw else 0, 1 if ff else 0,
                ])

            n = len(files)
            total_precision, total_recall, total_f1 = calculate_metrics(all_tp, all_fp, all_fn)
            result = {
                "tp": all_tp,
                "fp": all_fp,
                "fn": all_fn,
                "runs": n,
                "precision": total_precision,
                "recall": total_recall,
                "f1": total_f1,
                "water_count": water_found_count,
                "fish_count": fish_found_count,
                "water_pct": water_found_count / n * 100 if n else 0,
                "fish_pct": fish_found_count / n * 100 if n else 0,
            }
            all_model_results[model_name] = result

            out.write("\n" + "-" * 70 + "\n")
            out.write(f"  {model_name} TOTALS\n")
            out.write("-" * 70 + "\n")
            out.write(f"  TP = {all_tp:<5} FP = {all_fp:<5} FN = {all_fn}\n")
            out.write(f"  Avg/run:  TP={all_tp/n:.2f}  FP={all_fp/n:.2f}  FN={all_fn/n:.2f}\n")
            out.write(f"  Precision = TP/(TP+FP) = {all_tp}/({all_tp}+{all_fp}) = {total_precision:.4f}\n")
            out.write(f"  Recall    = TP/(TP+FN) = {all_tp}/({all_tp}+{all_fn}) = {total_recall:.4f}\n")
            out.write(f"  F1 Score  = {total_f1:.4f}\n\n")
            out.write(f"  Water AS correctly identified: {water_found_count}/{n} runs ({water_found_count/n*100:.1f}%)\n")
            out.write(f"  Fish  AS correctly identified: {fish_found_count}/{n} runs ({fish_found_count/n*100:.1f}%)\n")

            print(
                f"{experiment_name} | {model_name}: "
                f"TP={all_tp}, FP={all_fp}, FN={all_fn}, "
                f"Precision={total_precision:.4f}, Recall={total_recall:.4f}, F1={total_f1:.4f}"
            )

        out.write("\n\n" + "#" * 70 + "\n")
        out.write(f"  FINAL COMPARISON: {experiment_name}\n")
        out.write("#" * 70 + "\n\n")
        out.write(f"{'Model':<20} {'TP':>4} {'FP':>4} {'FN':>4} {'Precision':>10} {'Recall':>8} {'F1':>8}\n")
        out.write("-" * 70 + "\n")
        for model_name, result in all_model_results.items():
            out.write(
                f"{model_name:<20} {result['tp']:>4} {result['fp']:>4} {result['fn']:>4} "
                f"{result['precision']:>10.4f} {result['recall']:>8.4f} {result['f1']:>8.4f}\n"
            )

    return all_model_results, report_path, csv_path


def write_cross_comparison(results_by_experiment):
    comparison_paths = [
        os.path.join(CURRENT_DIR, "Water_evaluation_comparison_ODD+game_stuff_vs_ODD-only.txt"),
    ]

    for comparison_path in comparison_paths:
        with open(comparison_path, "w", encoding="utf-8") as out:
            out.write("=" * 70 + "\n")
            out.write("  COMPARISON EVALUATION: ODD+game_stuff VS ODD-only\n")
            out.write("=" * 70 + "\n\n")
            out.write("Ground Truth (2 correct action situations):\n")
            out.write("  AS1: Upstream and downstream withdrawal decisions\n")
            out.write("  AS2: Fish extraction common pool resource game\n\n")
            out.write("Both experiments below were evaluated with the same evaluate_run() scorer.\n\n")

            out.write("Side-by-side totals:\n")
            out.write(
                f"{'Model':<20} {'Evaluation':<16} {'TP':>4} {'FP':>4} {'FN':>4} "
                f"{'Precision':>10} {'Recall':>8} {'F1':>8} {'Water':>12} {'Fish':>12}\n"
            )
            out.write("-" * 110 + "\n")
            for model_name in MODELS:
                for experiment_name, results in results_by_experiment.items():
                    result = results[model_name]
                    water = f"{result['water_count']}/{result['runs']}"
                    fish = f"{result['fish_count']}/{result['runs']}"
                    out.write(
                        f"{model_name:<20} {experiment_name:<16} {result['tp']:>4} "
                        f"{result['fp']:>4} {result['fn']:>4} {result['precision']:>10.4f} "
                        f"{result['recall']:>8.4f} {result['f1']:>8.4f} "
                        f"{water:>12} {fish:>12}\n"
                    )

            if "ODD+game_stuff" in results_by_experiment and "ODD-only" in results_by_experiment:
                old_results = results_by_experiment["ODD+game_stuff"]
                new_results = results_by_experiment["ODD-only"]
                out.write("\nDifferences (ODD-only minus ODD+game_stuff):\n")
                out.write(
                    f"{'Model':<20} {'Delta TP':>8} {'Delta FP':>8} {'Delta FN':>8} "
                    f"{'Delta Prec':>11} {'Delta Recall':>13} {'Delta F1':>10} "
                    f"{'Delta Water':>13} {'Delta Fish':>11}\n"
                )
                out.write("-" * 112 + "\n")
                for model_name in MODELS:
                    old = old_results[model_name]
                    new = new_results[model_name]
                    out.write(
                        f"{model_name:<20} "
                        f"{new['tp'] - old['tp']:>+8} "
                        f"{new['fp'] - old['fp']:>+8} "
                        f"{new['fn'] - old['fn']:>+8} "
                        f"{new['precision'] - old['precision']:>+11.4f} "
                        f"{new['recall'] - old['recall']:>+13.4f} "
                        f"{new['f1'] - old['f1']:>+10.4f} "
                        f"{new['water_count'] - old['water_count']:>+13} "
                        f"{new['fish_count'] - old['fish_count']:>+11}\n"
                    )

    return comparison_paths


def main():
    results_by_experiment = {}
    report_paths = []

    for experiment_name, config in EXPERIMENTS.items():
        results, report_path, csv_path = evaluate_experiment(experiment_name, config)
        results_by_experiment[experiment_name] = results
        report_paths.append((report_path, csv_path))

    comparison_paths = write_cross_comparison(results_by_experiment)

    print("\nReports:")
    for report_path, csv_path in report_paths:
        print(f"  Detailed: {report_path}")
        print(f"  CSV:      {csv_path}")
    for comparison_path in comparison_paths:
        print(f"  Compare:  {comparison_path}")


if __name__ == "__main__":
    main()

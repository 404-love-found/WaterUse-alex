"""
Evaluate TP, FP, FN for the ODD-only 30-run outputs.

The report follows the suffixed water-use evaluation style and appends a
comparison table between ODD+game_stuff and ODD-only.
"""

import csv
import os
import re

from evaluate_tp_fp_fn import evaluate_run

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BATCH_DIR = os.path.join(CURRENT_DIR, "Batch_30Runs_ODDOnly")
ORIGINAL_EVALUATION_PATH = os.path.join(
    CURRENT_DIR,
    "Batch_30Runs",
    "Water_evaluation_ODD+game_stuff.txt",
)
REPORT_NAME = "Water_evaluation_ODD-only.txt"
CSV_NAME = "Water_evaluation_summary_ODD-only.csv"

MODELS = {
    "DeepSeek-R1":   os.path.join(BATCH_DIR, "DeepSeek-R1"),
    "Llama-3.3-70B": os.path.join(BATCH_DIR, "Llama-3.3-70B"),
    "Qwen2.5-7B":    os.path.join(BATCH_DIR, "Qwen2.5-7B"),
}


def calculate_metrics(tp, fp, fn):
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = (2 * precision * recall / (precision + recall)
          if (precision + recall) > 0 else 0)
    return precision, recall, f1


def format_run_detail(detail):
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


def parse_original_evaluation(filepath):
    """Read the ODD+game_stuff evaluation totals for comparison."""
    if not os.path.exists(filepath):
        return {}

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    results = {}
    for model_name in MODELS:
        section_match = re.search(
            rf"{re.escape(model_name)} TOTALS\s*\n-+\n(?P<body>.*?)(?=\n\n#{{6,}}|\Z)",
            content,
            re.DOTALL,
        )
        if not section_match:
            continue

        body = section_match.group("body")
        totals_match = re.search(r"TP\s*=\s*(\d+)\s+FP\s*=\s*(\d+)\s+FN\s*=\s*(\d+)", body)
        water_match = re.search(r"Water AS correctly identified:\s*(\d+)/(\d+)", body)
        fish_match = re.search(r"Fish\s+AS correctly identified:\s*(\d+)/(\d+)", body)

        if not totals_match:
            continue

        tp, fp, fn = [int(x) for x in totals_match.groups()]
        precision, recall, f1 = calculate_metrics(tp, fp, fn)
        n = int(water_match.group(2)) if water_match else 30
        water_count = int(water_match.group(1)) if water_match else 0
        fish_count = int(fish_match.group(1)) if fish_match else 0

        results[model_name] = {
            "tp": tp,
            "fp": fp,
            "fn": fn,
            "runs": n,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "water_count": water_count,
            "fish_count": fish_count,
            "water_pct": water_count / n * 100 if n else 0,
            "fish_pct": fish_count / n * 100 if n else 0,
        }

    return results


def write_header(out):
    out.write("=" * 70 + "\n")
    out.write("  FINAL EVALUATION: TP / FP / FN (ODD-ONLY)\n")
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


def write_model_summary(out, model_name, results):
    n = results["runs"]
    tp = results["tp"]
    fp = results["fp"]
    fn = results["fn"]
    precision = results["precision"]
    recall = results["recall"]
    f1 = results["f1"]
    water_count = results["water_count"]
    fish_count = results["fish_count"]

    out.write("\n" + "-" * 70 + "\n")
    out.write(f"  {model_name} TOTALS\n")
    out.write("-" * 70 + "\n")
    out.write(f"  TP = {tp:<5} FP = {fp:<5} FN = {fn}\n")
    out.write(f"  Avg/run:  TP={tp/n:.2f}  FP={fp/n:.2f}  FN={fn/n:.2f}\n")
    out.write(f"  Precision = TP/(TP+FP) = {tp}/({tp}+{fp}) = {precision:.4f}\n")
    out.write(f"  Recall    = TP/(TP+FN) = {tp}/({tp}+{fn}) = {recall:.4f}\n")
    out.write(f"  F1 Score  = {f1:.4f}\n\n")
    out.write(f"  Water AS correctly identified: {water_count}/{n} runs ({water_count/n*100:.1f}%)\n")
    out.write(f"  Fish  AS correctly identified: {fish_count}/{n} runs ({fish_count/n*100:.1f}%)\n")


def write_final_comparison(out, all_model_results):
    out.write("\n\n" + "#" * 70 + "\n")
    out.write("  FINAL COMPARISON: ODD-ONLY EVALUATION\n")
    out.write("#" * 70 + "\n\n")
    out.write(f"{'Model':<20} {'TP':>4} {'FP':>4} {'FN':>4} {'Precision':>10} {'Recall':>8} {'F1':>8}\n")
    out.write("─" * 70 + "\n")
    for model_name, result in all_model_results.items():
        out.write(
            f"{model_name:<20} {result['tp']:>4} {result['fp']:>4} {result['fn']:>4} "
            f"{result['precision']:>10.4f} {result['recall']:>8.4f} {result['f1']:>8.4f}\n"
        )

    out.write("\n")
    out.write(f"{'Model':<20} {'Water AS found':>18} {'Fish AS found':>18}\n")
    out.write("─" * 70 + "\n")
    for model_name, result in all_model_results.items():
        water = f"{result['water_count']}/{result['runs']} ({result['water_pct']:.1f}%)"
        fish = f"{result['fish_count']}/{result['runs']} ({result['fish_pct']:.1f}%)"
        out.write(f"{model_name:<20} {water:>18} {fish:>18}\n")


def write_experiment_difference(out, original_results, odd_only_results):
    out.write("\n\n" + "#" * 70 + "\n")
    out.write("  DIFFERENCE TABLE: ODD+GAME_STUFF VS ODD-ONLY\n")
    out.write("#" * 70 + "\n\n")

    if not original_results:
        out.write(f"Original evaluation not found: {ORIGINAL_EVALUATION_PATH}\n")
        return

    out.write("Baseline files:\n")
    out.write("  ODD+game_stuff evaluation: Batch_30Runs/Water_evaluation_ODD+game_stuff.txt\n")
    out.write("  ODD-only evaluation: Batch_30Runs_ODDOnly/Water_evaluation_ODD-only.txt\n\n")

    out.write("Side-by-side totals:\n")
    out.write(
        f"{'Model':<20} {'Evaluation':<16} {'TP':>4} {'FP':>4} {'FN':>4} "
        f"{'Precision':>10} {'Recall':>8} {'F1':>8} {'Water':>12} {'Fish':>12}\n"
    )
    out.write("─" * 110 + "\n")
    for model_name in MODELS:
        for label, source in (
            ("ODD+game_stuff", original_results.get(model_name)),
            ("ODD-only", odd_only_results.get(model_name)),
        ):
            if not source:
                continue
            water = f"{source['water_count']}/{source['runs']}"
            fish = f"{source['fish_count']}/{source['runs']}"
            out.write(
                f"{model_name:<20} {label:<16} {source['tp']:>4} {source['fp']:>4} {source['fn']:>4} "
                f"{source['precision']:>10.4f} {source['recall']:>8.4f} {source['f1']:>8.4f} "
                f"{water:>12} {fish:>12}\n"
            )

    out.write("\nDifferences (ODD-only minus ODD+game_stuff):\n")
    out.write(
        f"{'Model':<20} {'Delta TP':>8} {'Delta FP':>8} {'Delta FN':>8} "
        f"{'Delta Prec':>11} {'Delta Recall':>13} {'Delta F1':>10} "
        f"{'Delta Water':>13} {'Delta Fish':>11}\n"
    )
    out.write("─" * 112 + "\n")
    for model_name in MODELS:
        old = original_results.get(model_name)
        new = odd_only_results.get(model_name)
        if not old or not new:
            continue
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


def main():
    output_path = os.path.join(BATCH_DIR, REPORT_NAME)
    csv_path = os.path.join(BATCH_DIR, CSV_NAME)
    original_results = parse_original_evaluation(ORIGINAL_EVALUATION_PATH)

    with open(output_path, "w", encoding="utf-8") as out, \
         open(csv_path, "w", newline="", encoding="utf-8") as csvf:

        writer = csv.writer(csvf)
        writer.writerow(["Model", "Run", "TP", "FP", "FN", "Total_AS",
                         "Precision", "Recall", "Found_Water", "Found_Fish"])

        write_header(out)

        all_model_results = {}

        for model_index, (model_name, model_dir) in enumerate(MODELS.items(), start=1):
            all_tp, all_fp, all_fn = 0, 0, 0
            water_found_count = 0
            fish_found_count = 0

            out.write("\n" + "#" * 70 + "\n")
            out.write(f"  MODEL {model_index}: {model_name}  (30 runs)\n")
            out.write("#" * 70 + "\n")

            files = sorted([f for f in os.listdir(model_dir) if f.endswith(".md")])

            for fname in files:
                fpath = os.path.join(model_dir, fname)
                tp, fp, fn, n_as, details, fw, ff = evaluate_run(fpath)
                all_tp += tp
                all_fp += fp
                all_fn += fn
                water_found_count += int(fw)
                fish_found_count += int(ff)

                prec, rec, _ = calculate_metrics(tp, fp, fn)

                run_no = os.path.splitext(fname)[0].replace("run_", "")
                out.write(f"\nRun {run_no} | TP={tp}  FP={fp}  FN={fn}\n")
                out.write(f"  Generated ASs: {n_as}\n")
                for d in details:
                    out.write(format_run_detail(d) + "\n")

                writer.writerow([model_name, fname, tp, fp, fn, n_as,
                                 f"{prec:.4f}", f"{rec:.4f}",
                                 1 if fw else 0, 1 if ff else 0])

            n = len(files)
            total_prec, total_rec, f1 = calculate_metrics(all_tp, all_fp, all_fn)

            all_model_results[model_name] = {
                "tp": all_tp,
                "fp": all_fp,
                "fn": all_fn,
                "runs": n,
                "precision": total_prec,
                "recall": total_rec,
                "f1": f1,
                "water_count": water_found_count,
                "fish_count": fish_found_count,
                "water_pct": water_found_count / n * 100 if n else 0,
                "fish_pct": fish_found_count / n * 100 if n else 0,
            }

            write_model_summary(out, model_name, all_model_results[model_name])
            print(
                f"{model_name}: TP={all_tp}, FP={all_fp}, FN={all_fn}, "
                f"Precision={total_prec:.4f}, Recall={total_rec:.4f}, F1={f1:.4f}"
            )

        write_final_comparison(out, all_model_results)
        write_experiment_difference(out, original_results, all_model_results)

    print(f"Detailed results: {output_path}")
    print(f"CSV summary:      {csv_path}")


if __name__ == "__main__":
    main()

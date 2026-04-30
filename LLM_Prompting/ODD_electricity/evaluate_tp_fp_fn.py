"""
Evaluate TP, FP, FN for electricity action-situation extraction runs.

Ground truth is taken from ODD_electricity/Txts/TXT/odd.txt, section III.iv.a:
  AS1: capacitor-adoption assurance game
  AS2: sequential social-learning process in capacitor adoption
  AS3: asymmetric transformer-capacity authorization dilemma between farmers
  AS4: mutual-exchange coordination game between farmer and sub-station staff
  AS5: authorization-and-investment asymmetric coordination between farmer and staff
  AS6: groundwater-extraction prisoner's dilemma
"""

import csv
import os
import re


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

EXPERIMENTS = {
    "ODD + game_stuff": os.path.join(CURRENT_DIR, "Batch_30Runs"),
    "ODD-only": os.path.join(CURRENT_DIR, "Batch_30Runs_ODDOnly"),
}

MODELS = {
    "DeepSeek-R1": "DeepSeek-R1",
    "Llama-3.3-70B": "Llama-3.3-70B",
    "Qwen2.5-7B": "Qwen2.5-7B",
}

GROUND_TRUTH = {
    "as1_capacitor": "Capacitor-adoption assurance game between neighbouring farmers",
    "as2_social_learning": "Sequential social-learning process in capacitor adoption",
    "as3_transformer_farmer": "Asymmetric transformer-capacity authorization dilemma between farmers",
    "as4_mutual_exchange": "Mutual-exchange coordination between farmer and sub-station staff",
    "as5_authorization_staff": "Authorization-and-investment asymmetric coordination between farmer and staff",
    "as6_groundwater": "Groundwater-extraction prisoner's dilemma between farmers",
}

DISPLAY_NAMES = {
    "as1_capacitor": "AS1 capacitor adoption",
    "as2_social_learning": "AS2 social learning",
    "as3_transformer_farmer": "AS3 transformer authorization",
    "as4_mutual_exchange": "AS4 mutual exchange",
    "as5_authorization_staff": "AS5 authorization/investment",
    "as6_groundwater": "AS6 groundwater extraction",
}

SECTION_WORDS = (
    "action situation",
    "title:",
    "capacitor",
    "transformer",
    "groundwater",
    "aquifer",
    "mutual exchange",
    "informal exchange",
    "reciprocity",
    "authorization",
    "authorisation",
    "enforcement",
    "capacity",
    "social learning",
    "social-learning",
    "learning",
    "diffusion",
    "coordination",
    "investment",
    "formal",
    "informal",
    "dilemma",
    "game",
)

NON_TITLE_WORDS = (
    "tension",
    "matrix",
    "justification",
    "note",
    "interpretation",
    "equilibrium",
    "payoff",
)


def clean_heading(line):
    text = re.sub(r"^#{1,6}\s*", "", line.strip())
    text = text.strip("* ").strip()
    text = re.sub(r"^\d+[\.\)]\s*", "", text)
    text = re.sub(r"^\*\*\d+[\.\)]\s*", "", text)
    text = re.sub(r"^\*\*Title\*\*\s*:\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^Title:\s*", "", text, flags=re.IGNORECASE)
    return text.strip("* ").strip()


def is_section_start(line):
    stripped = line.strip()
    lower = stripped.lower().strip("* ")

    if not stripped:
        return False
    if lower.startswith("# run "):
        return False
    if any(word in lower for word in ("analysis", "summary", "key exclusions")):
        return False

    is_markdown_heading = bool(re.match(r"^#{2,6}\s+", stripped))
    is_bold_title = bool(re.match(r"^\*\*Title\s*:", stripped, flags=re.IGNORECASE))
    is_bold_numbered = bool(re.match(r"^\*\*\d+[\.\)]\s+", stripped))
    is_plain_numbered_title = bool(re.match(r"^\d+[\.\)]\s+\*\*Title\*\*\s*:", stripped, flags=re.IGNORECASE))
    is_numbered_heading = bool(re.match(r"^#{2,6}\s*\d+[\.\)]\s+", stripped))

    if not (is_markdown_heading or is_bold_title or is_bold_numbered or is_plain_numbered_title or is_numbered_heading):
        return False

    heading = clean_heading(stripped)
    heading_lower = heading.lower()
    if not heading or len(heading) < 4:
        return False
    if any(heading_lower.startswith(word) for word in NON_TITLE_WORDS):
        return False
    if any(word in heading_lower for word in NON_TITLE_WORDS) and not any(
        word in heading_lower for word in ("dilemma", "game", "coordination", "adoption")
    ):
        return False

    return any(word in heading_lower for word in SECTION_WORDS)


def extract_action_situations(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    starts = []
    offset = 0
    for line in content.splitlines(keepends=True):
        if is_section_start(line):
            starts.append((offset, clean_heading(line)))
        offset += len(line)

    situations = []
    for i, (start, title) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(content)
        block = content[start:end]
        block_lower = block.lower()
        if "matrix" not in block_lower or ("tension" not in block_lower and "justification" not in block_lower):
            continue
        situations.append({
            "title": title,
            "block": block_lower,
        })

    return situations


def count(pattern, text):
    return len(re.findall(pattern, text, flags=re.IGNORECASE))


def classify_as(title, block):
    t = title.lower()
    combined = f"{t}\n{block}"

    social_score = count(r"social[- ]?learning|diffusion|imitat|observ|peer|neighbor|neighbour|sequential|trial", combined)
    capacitor_score = count(r"capacitor|voltage.?stabili|adopt", combined)
    groundwater_score = count(r"groundwater|aquifer|over.?extract|extraction|depletion|recharge", combined)
    exchange_score = count(r"mutual.?exchange|informal.?exchange|recipro|collusion|collusive|favor|favour|trust", combined)
    staff_score = count(r"staff|sub.?station|utility", combined)
    formal_score = count(r"formal|informal|authori[sz]ation|authori[sz]e|enforce|withhold|maintenance|connection|invest", combined)
    transformer_score = count(r"transformer|capacity|free.?rid|contribut|volunteer|upgrade", combined)
    farmer_farmer_score = count(r"two farmers|farmer.?farmer|neighbou?r|farmer 1|farmer 2", combined)

    explicit_labels = {
        r"\bAS1\b": "as1_capacitor",
        r"\bAS2\b": "as2_social_learning",
        r"\bAS3\b": "as3_transformer_farmer",
        r"\bAS4\b": "as4_mutual_exchange",
        r"\bAS5\b": "as5_authorization_staff",
        r"\bAS6\b": "as6_groundwater",
    }
    for pattern, label in explicit_labels.items():
        if re.search(pattern, t, flags=re.IGNORECASE):
            return label

    # Title-first rules avoid Note/Summary text pulling a block into the wrong class.
    if re.search(r"groundwater|aquifer|over.?extract|extraction|depletion|recharge", t):
        return "as6_groundwater"
    if re.search(r"social[- ]?learning|diffusion|imitat|observ|sequential|peer", t):
        return "as2_social_learning"
    if re.search(r"capacitor|voltage.?stabili", t):
        return "as1_capacitor"
    if re.search(r"mutual.?exchange|informal.?exchange|recipro|collusion|collusive", t):
        return "as4_mutual_exchange"
    if re.search(r"authori[sz]ation.*investment|authori[sz]ation.*enforcement|formal.*informal|formal|informal access|staff|sub.?station|maintenance|connection", t):
        return "as5_authorization_staff"
    if re.search(r"transformer|capacity|free.?rid|volunteer|contribut", t):
        if staff_score >= 1 and formal_score >= 2:
            return "as5_authorization_staff"
        return "as3_transformer_farmer"

    # AS2 must be checked before AS1 in fallback because both may mention capacitor adoption.
    if social_score >= 2 and capacitor_score >= 1:
        return "as2_social_learning"

    if groundwater_score >= 2:
        return "as6_groundwater"

    if exchange_score >= 2 and staff_score >= 1:
        return "as4_mutual_exchange"

    if staff_score >= 1 and formal_score >= 2:
        return "as5_authorization_staff"

    if transformer_score >= 2 and staff_score == 0:
        return "as3_transformer_farmer"
    if transformer_score >= 2 and farmer_farmer_score >= 1 and staff_score == 0:
        return "as3_transformer_farmer"

    if capacitor_score >= 2:
        return "as1_capacitor"

    return "other"


def evaluate_run(filepath):
    situations = extract_action_situations(filepath)
    found = {key: False for key in GROUND_TRUTH}
    fp_count = 0
    details = []

    for situation in situations:
        cls = classify_as(situation["title"], situation["block"])
        title = situation["title"]

        if cls in GROUND_TRUTH and not found[cls]:
            found[cls] = True
            details.append(f"  TP: {DISPLAY_NAMES[cls]} - {title}")
        elif cls in GROUND_TRUTH:
            fp_count += 1
            details.append(f"  FP duplicate: {DISPLAY_NAMES[cls]} - {title}")
        else:
            fp_count += 1
            details.append(f"  FP: {title}")

    tp = sum(1 for value in found.values() if value)
    fn = len(GROUND_TRUTH) - tp

    for key, was_found in found.items():
        if not was_found:
            details.append(f"  FN missed: {DISPLAY_NAMES[key]}")

    return tp, fp_count, fn, len(situations), details, found


def calculate_metrics(tp, fp, fn):
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = (2 * precision * recall / (precision + recall)
          if (precision + recall) > 0 else 0)
    return precision, recall, f1


def write_header(out, experiment_name):
    out.write("=" * 70 + "\n")
    out.write(f"  FINAL EVALUATION: TP / FP / FN ({experiment_name})\n")
    out.write("=" * 70 + "\n\n")
    out.write("Ground Truth (6 correct action situations):\n")
    for key, description in GROUND_TRUTH.items():
        out.write(f"  {DISPLAY_NAMES[key]}: {description}\n")
    out.write("\n")
    out.write("Metrics:\n")
    out.write("  TP = How many ground-truth electricity ASs the LLM identified\n")
    out.write("  FN = How many ground-truth electricity ASs the LLM missed\n")
    out.write("  FP = How many generated ASs were extra, duplicate, or wrong\n")
    out.write("  Precision = TP / (TP + FP)\n")
    out.write("  Recall    = TP / (TP + FN)\n")
    out.write("  F1 Score  = 2 * Precision * Recall / (Precision + Recall)\n\n")


def evaluate_experiment(experiment_name, batch_dir):
    output_path = os.path.join(batch_dir, "evaluation_final.txt")
    csv_path = os.path.join(batch_dir, "evaluation_summary.csv")
    all_model_results = {}

    with open(output_path, "w", encoding="utf-8") as out, \
         open(csv_path, "w", newline="", encoding="utf-8") as csvf:
        writer = csv.writer(csvf)
        writer.writerow([
            "Experiment", "Model", "Run", "TP", "FP", "FN", "Total_AS",
            "Precision", "Recall", "F1", *DISPLAY_NAMES.values()
        ])

        write_header(out, experiment_name)

        for model_index, (model_name, model_subdir) in enumerate(MODELS.items(), start=1):
            model_dir = os.path.join(batch_dir, model_subdir)
            files = sorted([f for f in os.listdir(model_dir) if f.endswith(".md")])

            all_tp = all_fp = all_fn = 0
            found_counts = {key: 0 for key in GROUND_TRUTH}

            out.write("\n" + "#" * 70 + "\n")
            out.write(f"  MODEL {model_index}: {model_name}  ({len(files)} runs)\n")
            out.write("#" * 70 + "\n")

            for fname in files:
                fpath = os.path.join(model_dir, fname)
                tp, fp, fn, n_as, details, found = evaluate_run(fpath)
                precision, recall, f1 = calculate_metrics(tp, fp, fn)

                all_tp += tp
                all_fp += fp
                all_fn += fn
                for key, value in found.items():
                    found_counts[key] += int(value)

                run_no = os.path.splitext(fname)[0].replace("run_", "")
                out.write(f"\nRun {run_no} | TP={tp}  FP={fp}  FN={fn}\n")
                out.write(f"  Generated ASs: {n_as}\n")
                for detail in details:
                    out.write(detail + "\n")

                writer.writerow([
                    experiment_name, model_name, fname, tp, fp, fn, n_as,
                    f"{precision:.4f}", f"{recall:.4f}", f"{f1:.4f}",
                    *[1 if found[key] else 0 for key in GROUND_TRUTH],
                ])

            n = len(files)
            total_precision, total_recall, total_f1 = calculate_metrics(all_tp, all_fp, all_fn)
            all_model_results[model_name] = {
                "tp": all_tp,
                "fp": all_fp,
                "fn": all_fn,
                "runs": n,
                "precision": total_precision,
                "recall": total_recall,
                "f1": total_f1,
                "found_counts": found_counts,
            }

            out.write("\n" + "-" * 70 + "\n")
            out.write(f"  {model_name} TOTALS\n")
            out.write("-" * 70 + "\n")
            out.write(f"  TP = {all_tp:<5} FP = {all_fp:<5} FN = {all_fn}\n")
            out.write(f"  Avg/run:  TP={all_tp/n:.2f}  FP={all_fp/n:.2f}  FN={all_fn/n:.2f}\n")
            out.write(f"  Precision = TP/(TP+FP) = {all_tp}/({all_tp}+{all_fp}) = {total_precision:.4f}\n")
            out.write(f"  Recall    = TP/(TP+FN) = {all_tp}/({all_tp}+{all_fn}) = {total_recall:.4f}\n")
            out.write(f"  F1 Score  = {total_f1:.4f}\n\n")
            for key in GROUND_TRUTH:
                out.write(f"  {DISPLAY_NAMES[key]} found: {found_counts[key]}/{n} runs ({found_counts[key]/n*100:.1f}%)\n")

            print(
                f"{experiment_name} | {model_name}: "
                f"TP={all_tp}, FP={all_fp}, FN={all_fn}, "
                f"Precision={total_precision:.4f}, Recall={total_recall:.4f}, F1={total_f1:.4f}"
            )

        out.write("\n\n" + "#" * 70 + "\n")
        out.write("  FINAL COMPARISON\n")
        out.write("#" * 70 + "\n\n")
        out.write(f"{'Model':<20} {'TP':>4} {'FP':>4} {'FN':>4} {'Precision':>10} {'Recall':>8} {'F1':>8}\n")
        out.write("-" * 70 + "\n")
        for model_name, result in all_model_results.items():
            out.write(
                f"{model_name:<20} {result['tp']:>4} {result['fp']:>4} {result['fn']:>4} "
                f"{result['precision']:>10.4f} {result['recall']:>8.4f} {result['f1']:>8.4f}\n"
            )

    return all_model_results, output_path, csv_path


def write_cross_experiment_comparison(results_by_experiment):
    output_path = os.path.join(CURRENT_DIR, "evaluation_comparison.txt")
    with open(output_path, "w", encoding="utf-8") as out:
        out.write("=" * 80 + "\n")
        out.write("  ELECTRICITY EVALUATION COMPARISON: ODD + GAME_STUFF VS ODD-ONLY\n")
        out.write("=" * 80 + "\n\n")

        out.write("Side-by-side totals:\n")
        out.write(
            f"{'Model':<20} {'Experiment':<18} {'TP':>4} {'FP':>4} {'FN':>4} "
            f"{'Precision':>10} {'Recall':>8} {'F1':>8}\n"
        )
        out.write("-" * 92 + "\n")
        for model_name in MODELS:
            for experiment_name, results in results_by_experiment.items():
                result = results[model_name]
                out.write(
                    f"{model_name:<20} {experiment_name:<18} {result['tp']:>4} "
                    f"{result['fp']:>4} {result['fn']:>4} {result['precision']:>10.4f} "
                    f"{result['recall']:>8.4f} {result['f1']:>8.4f}\n"
                )

        if "ODD + game_stuff" in results_by_experiment and "ODD-only" in results_by_experiment:
            out.write("\nDifferences (ODD-only minus ODD + game_stuff):\n")
            out.write(
                f"{'Model':<20} {'Delta TP':>8} {'Delta FP':>8} {'Delta FN':>8} "
                f"{'Delta Prec':>11} {'Delta Recall':>13} {'Delta F1':>10}\n"
            )
            out.write("-" * 82 + "\n")
            old_results = results_by_experiment["ODD + game_stuff"]
            new_results = results_by_experiment["ODD-only"]
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
                    f"{new['f1'] - old['f1']:>+10.4f}\n"
                )

        out.write("\nGround-truth AS hit counts by experiment/model:\n")
        for experiment_name, results in results_by_experiment.items():
            out.write(f"\n{experiment_name}\n")
            out.write(f"{'Model':<20} " + " ".join(f"{name[:10]:>10}" for name in DISPLAY_NAMES.values()) + "\n")
            out.write("-" * 90 + "\n")
            for model_name, result in results.items():
                counts = " ".join(f"{result['found_counts'][key]:>10}" for key in GROUND_TRUTH)
                out.write(f"{model_name:<20} {counts}\n")

    return output_path


def main():
    results_by_experiment = {}
    report_paths = []

    for experiment_name, batch_dir in EXPERIMENTS.items():
        results, output_path, csv_path = evaluate_experiment(experiment_name, batch_dir)
        results_by_experiment[experiment_name] = results
        report_paths.append((output_path, csv_path))

    comparison_path = write_cross_experiment_comparison(results_by_experiment)

    print("\nReports:")
    for output_path, csv_path in report_paths:
        print(f"  Detailed: {output_path}")
        print(f"  CSV:      {csv_path}")
    print(f"  Compare:  {comparison_path}")


if __name__ == "__main__":
    main()

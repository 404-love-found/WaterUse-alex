"""
Evaluate TP, FP, FN for the 3 LLM models' 30 runs.

Correct Action Situations (Ground Truth):
  AS1: Upstream and downstream withdrawal decisions (water irrigation game)
  AS2: Fish extraction common pool resource game (fishing CPR)

For each run:
  TP = how many of the 2 correct ASs the LLM identified
  FP = how many extra/wrong ASs the LLM generated
  FN = how many of the 2 correct ASs the LLM missed
"""

import os
import re
import csv

BATCH_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Batch_30Runs")

MODELS = {
    "DeepSeek-R1":   os.path.join(BATCH_DIR, "DeepSeek-R1"),
    "Llama-3.3-70B": os.path.join(BATCH_DIR, "Llama-3.3-70B"),
    "Qwen2.5-7B":    os.path.join(BATCH_DIR, "Qwen2.5-7B"),
}


def extract_action_situations(filepath):
    """Extract action situation blocks: title + surrounding text."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    situations = []

    # Find all action situation headers (various formats)
    # Pattern: markdown headers with numbers or "Action Situation"
    header_pattern = re.compile(
        r"^(#{2,4})\s*\**\s*"                          # markdown header
        r"(?:Action Situation\s*\d+[:\.\)]?\s*[:\-—]?\s*"  # "Action Situation 1:"
        r"|(\d+)[\.\)]\s*"                              # "1." or "1)"
        r")"
        r"(.*)",                                        # title text
        re.MULTILINE
    )

    matches = list(header_pattern.finditer(content))

    if not matches:
        # Fallback: try to find titled sections
        alt_pattern = re.compile(
            r"^(#{2,4})\s*\**\s*(.*?(?:Tension|Dilemma|Game|Situation|Decision).*?)\**\s*$",
            re.MULTILINE | re.IGNORECASE
        )
        matches = list(alt_pattern.finditer(content))

    for i, match in enumerate(matches):
        title = match.group(0).strip().strip("#").strip("*").strip().strip(":").strip()
        # Get text block until next header or end
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else min(start + 1500, len(content))
        block = content[start:end]

        if len(title) < 5:  # skip empty/trivial headers
            continue

        situations.append({
            "title": title,
            "block": block.lower(),
        })

    return situations


def classify_as(title, block):
    """
    Classify based on TITLE first (most reliable), then block text.
    Returns: 'water', 'fish', or 'other'
    """
    t = title.lower()

    # ---- TITLE-based classification (high confidence) ----

    # Fish CPR: title mentions fish/fishing/harvest/catch/overfish
    fish_title = bool(re.search(
        r"fish|fishing|overfish|harvest|catch|aquatic|common.?pool.*resource",
        t, re.IGNORECASE
    ))

    # Water/Irrigation: title mentions upstream/downstream + water/irrigation
    water_title = bool(re.search(
        r"(upstream|downstream).*(water|irrig|withdraw|alloc|field|extract)"
        r"|water.*(alloc|extract|withdraw|usage|dilemma).*(upstream|downstream|farmer)"
        r"|(irrig|water).*(upstream|downstream)"
        r"|upstream.*downstream",
        t, re.IGNORECASE
    ))

    # If title clearly indicates one, return it
    if fish_title and not water_title:
        return "fish"
    if water_title and not fish_title:
        return "water"

    # ---- BLOCK-based classification (for ambiguous titles) ----

    # Count keyword occurrences in block
    fish_signals = len(re.findall(
        r"fish(?:ing|ery|eries)?|overfish|harvest|catch|common.?pool|cpr|"
        r"deplet.*stock|fish.*popul|aquatic",
        block
    ))
    water_signals = len(re.findall(
        r"upstream.*downstream|downstream.*upstream|"
        r"water.*withdraw|irrig.*decision|water.*alloc|"
        r"spatial.*asymmetr|water.*priority|water.*access",
        block
    ))

    # If title mentions water extraction/allocation but content is mostly about
    # upstream-downstream irrigation → water
    if re.search(r"water.*(extract|alloc|usage|withdraw)", t):
        return "water"

    # Risk-taking, conservation, income threshold → other (FP)
    if re.search(r"risk.*(tak|avers)|conserv.*(invest|dilemma)|"
                 r"income.*threshold|budget.*dilemma|"
                 r"threshold.*dilemma|memory|prediction",
                 t, re.IGNORECASE):
        return "other"

    # If title mentions irrigation dilemma → water
    if re.search(r"irrig.*(dilemma|decision|strateg)", t):
        return "water"

    # Use signal counts as tiebreaker
    if fish_signals > water_signals and fish_signals >= 3:
        return "fish"
    if water_signals > fish_signals and water_signals >= 2:
        return "water"

    # Ecological threshold without specific fish focus → other
    if re.search(r"ecolog|threshold|tipping", t):
        if fish_signals >= 3:
            return "fish"
        return "other"

    return "other"


def evaluate_run(filepath):
    """Evaluate a single run. Returns (TP, FP, FN, n_as, details)."""
    situations = extract_action_situations(filepath)

    found_water = False
    found_fish = False
    fp_count = 0
    details = []

    for s in situations:
        cls = classify_as(s["title"], s["block"])

        if cls == "water" and not found_water:
            found_water = True
            details.append(f"  TP(water): {s['title']}")
        elif cls == "fish" and not found_fish:
            found_fish = True
            details.append(f"  TP(fish):  {s['title']}")
        elif cls in ("water", "fish"):
            fp_count += 1
            details.append(f"  FP(dup):   {s['title']}")
        else:
            fp_count += 1
            details.append(f"  FP:        {s['title']}")

    tp = int(found_water) + int(found_fish)
    fn = int(not found_water) + int(not found_fish)

    if not found_water:
        details.append("  FN: missed — upstream/downstream withdrawal decisions")
    if not found_fish:
        details.append("  FN: missed — fish extraction CPR game")

    return tp, fp_count, fn, len(situations), details, found_water, found_fish


def main():
    output_path = os.path.join(BATCH_DIR, "evaluation_results.txt")
    csv_path = os.path.join(BATCH_DIR, "evaluation_summary.csv")

    with open(output_path, "w", encoding="utf-8") as out, \
         open(csv_path, "w", newline="", encoding="utf-8") as csvf:

        writer = csv.writer(csvf)
        writer.writerow(["Model", "Run", "TP", "FP", "FN", "Total_AS",
                         "Precision", "Recall", "Found_Water", "Found_Fish"])

        out.write("=" * 70 + "\n")
        out.write("  EVALUATION: TP / FP / FN for LLM Action Situation Extraction\n")
        out.write("=" * 70 + "\n")
        out.write("Ground Truth (2 correct action situations):\n")
        out.write("  AS1: Upstream and downstream withdrawal decisions\n")
        out.write("  AS2: Fish extraction common pool resource game\n\n")

        all_model_results = {}

        for model_name, model_dir in MODELS.items():
            all_tp, all_fp, all_fn = 0, 0, 0
            water_found_count = 0
            fish_found_count = 0

            out.write(f"\n{'='*70}\n  MODEL: {model_name}\n{'='*70}\n")

            files = sorted([f for f in os.listdir(model_dir) if f.endswith(".md")])

            for fname in files:
                fpath = os.path.join(model_dir, fname)
                tp, fp, fn, n_as, details, fw, ff = evaluate_run(fpath)
                all_tp += tp
                all_fp += fp
                all_fn += fn
                water_found_count += int(fw)
                fish_found_count += int(ff)

                prec = tp / (tp + fp) if (tp + fp) > 0 else 0
                rec = tp / (tp + fn) if (tp + fn) > 0 else 0

                out.write(f"\n--- {fname} (ASs generated: {n_as}) ---\n")
                out.write(f"  TP={tp}  FP={fp}  FN={fn}  "
                          f"Precision={prec:.2f}  Recall={rec:.2f}\n")
                for d in details:
                    out.write(d + "\n")

                writer.writerow([model_name, fname, tp, fp, fn, n_as,
                                 f"{prec:.4f}", f"{rec:.4f}",
                                 1 if fw else 0, 1 if ff else 0])

            # Aggregate
            n = len(files)
            total_prec = all_tp / (all_tp + all_fp) if (all_tp + all_fp) > 0 else 0
            total_rec = all_tp / (all_tp + all_fn) if (all_tp + all_fn) > 0 else 0
            f1 = (2 * total_prec * total_rec / (total_prec + total_rec)
                  if (total_prec + total_rec) > 0 else 0)

            summary = (
                f"\n  SUMMARY — {model_name} ({n} runs)\n"
                f"  {'─'*50}\n"
                f"  Total:    TP={all_tp}  FP={all_fp}  FN={all_fn}\n"
                f"  Avg/run:  TP={all_tp/n:.2f}  FP={all_fp/n:.2f}  FN={all_fn/n:.2f}\n"
                f"  Precision = TP/(TP+FP) = {all_tp}/({all_tp}+{all_fp}) = {total_prec:.4f}\n"
                f"  Recall    = TP/(TP+FN) = {all_tp}/({all_tp}+{all_fn}) = {total_rec:.4f}\n"
                f"  F1 Score  = {f1:.4f}\n"
                f"  Water AS found: {water_found_count}/{n} runs ({water_found_count/n*100:.1f}%)\n"
                f"  Fish  AS found: {fish_found_count}/{n} runs ({fish_found_count/n*100:.1f}%)\n"
            )
            out.write(summary)
            print(summary)

            all_model_results[model_name] = {
                "tp": all_tp, "fp": all_fp, "fn": all_fn,
                "precision": total_prec, "recall": total_rec, "f1": f1,
                "water_pct": water_found_count / n * 100,
                "fish_pct": fish_found_count / n * 100,
            }

        # Final comparison table
        comp = "\n" + "=" * 70 + "\n  COMPARISON TABLE\n" + "=" * 70 + "\n"
        comp += f"{'Model':<20} {'TP':>4} {'FP':>4} {'FN':>4} {'Prec':>8} {'Recall':>8} {'F1':>8} {'Water%':>8} {'Fish%':>8}\n"
        comp += "─" * 70 + "\n"
        for m, r in all_model_results.items():
            comp += (f"{m:<20} {r['tp']:>4} {r['fp']:>4} {r['fn']:>4} "
                     f"{r['precision']:>8.4f} {r['recall']:>8.4f} {r['f1']:>8.4f} "
                     f"{r['water_pct']:>7.1f}% {r['fish_pct']:>7.1f}%\n")

        with open(output_path, "a", encoding="utf-8") as out:
            out.write(comp)
        print(comp)

    print(f"Detailed results: {output_path}")
    print(f"CSV summary:      {csv_path}")


if __name__ == "__main__":
    main()

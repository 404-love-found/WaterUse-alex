import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def calculate_metrics(ground_truth, predictions):
    """
    Calculate TP, FP, FN, Precision, and Recall, and return the specific game sets.
    """
    gt_set = set(ground_truth)
    pred_set = set(predictions)

    tp_set = gt_set.intersection(pred_set)
    fp_set = pred_set.difference(gt_set)
    fn_set = gt_set.difference(pred_set)

    tp = len(tp_set)
    fp = len(fp_set)
    fn = len(fn_set)

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0

    return {
        "TP": tp, "FP": fp, "FN": fn,
        "Precision": round(precision, 3),
        "Recall": round(recall, 3),
        "True Positive": list(tp_set),
        "False Positives": list(fp_set),
        "False Negatives": list(fn_set)
    }


def run_evaluation():
    # ---------------------------------------------------------
    # 1. Ground Truth Baselines (6 Action Situations from ODD+D)
    # ---------------------------------------------------------
    official_baselines = [
        "DSM_Adoption_Coordination",
        "Social_Learning_Sequential_Adoption",
        "Infrastructure_Capacity_Provision",
        "Mutual_Exchange_and_Collusion",
        "Authorization_and_Capacity_Investment",
        "Groundwater_Extraction_Dilemma"
    ]

    # ---------------------------------------------------------
    # 2. Model Predictions (TXT_electricity dataset)
    #    NOTE: Fill in actual LLM outputs after running the scripts.
    #    Below are placeholder predictions based on expected behavior.
    # ---------------------------------------------------------
    model_predictions = [
        {"Model": "DeepSeek-R1", "Dataset": "TXT_electricity",
         "Preds": [
             "DSM_Adoption_Coordination",
             "Social_Learning_Sequential_Adoption",
             "Infrastructure_Capacity_Provision",
             "Mutual_Exchange_and_Collusion",
             "Authorization_and_Capacity_Investment",
             "Groundwater_Extraction_Dilemma"
         ]},
        {"Model": "Llama-3.3-70B", "Dataset": "TXT_electricity",
         "Preds": [
             "DSM_Adoption_Coordination",
             "Social_Learning_Sequential_Adoption",
             "Infrastructure_Capacity_Provision",
             "Mutual_Exchange_and_Collusion",
             "Authorization_and_Capacity_Investment",
             "Groundwater_Extraction_Dilemma"
         ]},
        {"Model": "Qwen2.5-7B", "Dataset": "TXT_electricity",
         "Preds": [
             "DSM_Adoption_Coordination",
             "Social_Learning_Sequential_Adoption",
             "Infrastructure_Capacity_Provision",
             "Mutual_Exchange_and_Collusion",
             "Authorization_and_Capacity_Investment",
             "Groundwater_Extraction_Dilemma"
         ]},
    ]

    # 3. Calculation
    results = []
    for entry in model_predictions:
        metrics = calculate_metrics(official_baselines, entry["Preds"])
        row = {"Model": entry["Model"], "Dataset": entry["Dataset"]}
        row.update(metrics)
        results.append(row)

    df = pd.DataFrame(results)

    # ---------------------------------------------------------
    # PART A: Terminal Detailed Analysis
    # ---------------------------------------------------------
    print("\n🚀 === Standardized Evaluation Metrics ===")
    print(df[["Model", "Dataset", "Precision", "Recall", "TP", "FP", "FN"]].to_string(index=False))

    print("\n🔍 === Detailed Game Classification Breakdown ===")
    for index, row in df.iterrows():
        print(f"[{row['Model']} | {row['Dataset']}]")
        print(f"   True Positive:   {row['True Positive'] if row['True Positive'] else 'None'}")
        print(f"   False Positives: {row['False Positives'] if row['False Positives'] else 'None'}")
        print(f"   False Negatives: {row['False Negatives'] if row['False Negatives'] else 'None'}")
        print("-" * 60)

    # ---------------------------------------------------------
    # PART B: Generate Markdown Report
    # ---------------------------------------------------------
    current_dir = os.path.dirname(os.path.abspath(__file__))
    md_file = os.path.join(current_dir, "evaluation_report.md")

    with open(md_file, "w", encoding="utf-8") as f:
        f.write("# 📊 Comprehensive LLM Evaluation Report\n\n")
        f.write("### 1. Summary Table\n")
        f.write(df[["Model", "Dataset", "Precision", "Recall", "TP", "FP", "FN"]].to_markdown(index=False))

        f.write("\n\n### 2. 🎯 Individual Game Analysis (Breakdown)\n")
        f.write("Specific games categorized as True Positive, False Positives, and False Negatives.\n\n")

        for index, row in df.iterrows():
            f.write(f"#### 🤖 {row['Model']} - `{row['Dataset']}`\n")
            f.write(f"- **True Positive:** `{row['True Positive'] if row['True Positive'] else 'None'}`\n")
            f.write(f"- **False Positives:** `{row['False Positives'] if row['False Positives'] else 'None'}`\n")
            f.write(f"- **False Negatives:** `{row['False Negatives'] if row['False Negatives'] else 'None'}`\n")
            f.write("\n")

    print(f"\n✅ Detailed Markdown report saved to: {md_file}")


if __name__ == "__main__":
    run_evaluation()
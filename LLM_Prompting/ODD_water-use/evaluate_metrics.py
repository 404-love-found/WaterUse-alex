import pandas as pd


def calculate_metrics(ground_truth, predictions):
    """
    Calculate TP, FP, FN, Precision, Recall, and F1-Score
    """
    # Convert lists to sets for intersection and difference operations
    gt_set = set(ground_truth)
    pred_set = set(predictions)

    # Calculate True Positives (Intersection: Games correctly predicted by the model)
    tp_set = gt_set.intersection(pred_set)
    tp = len(tp_set)

    # Calculate False Positives (Difference: Games predicted by the model but NOT in Ground Truth)
    fp_set = pred_set.difference(gt_set)
    fp = len(fp_set)

    # Calculate False Negatives (Difference: Games in Ground Truth but missed by the model)
    fn_set = gt_set.difference(pred_set)
    fn = len(fn_set)

    # Calculate metrics (avoid division by zero)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

    return {
        "TP": tp,
        "FP": fp,
        "FN": fn,
        "Precision": round(precision, 3),
        "Recall": round(recall, 3),
        "F1-Score": round(f1, 3),
        "Missed Games (FN)": list(fn_set),
        "Hallucinated Games (FP)": list(fp_set)
    }


def run_evaluation():
    # 1. Define your Ground Truth (The correct set of games for each txt version)
    # Customize these lists based on what is ACTUALLY in your text files
    ground_truth_db = {
        "Txts": ["Upstream_vs_Downstream", "Farmer_vs_Authority", "Ecological_Tipping_Point"],
        "TXT_new": ["Upstream_vs_Downstream", "Farmer_vs_Authority", "Groundwater_Depletion", "Subsidies_Game"]
    }

    # 2. Record the model's extraction results (mapped to tags after human review)
    # Fill in the lists below based on what the models generated in the Markdown files
    model_predictions = [
        # Performance on Txts dataset
        {"Model": "DeepSeek-R1", "Dataset": "Txts", "Preds": ["Upstream_vs_Downstream", "Farmer_vs_Authority"]},
        {"Model": "Llama-3.3-70B", "Dataset": "Txts",
         "Preds": ["Upstream_vs_Downstream", "Farmer_vs_Authority", "Ecological_Tipping_Point",
                   "Irrelevant_Weather_Game"]},
        {"Model": "Qwen2.5-7B", "Dataset": "Txts", "Preds": ["Upstream_vs_Downstream", "Crop_Selection_Game"]},

        # Performance on TXT_new dataset
        {"Model": "DeepSeek-R1", "Dataset": "TXT_new",
         "Preds": ["Upstream_vs_Downstream", "Farmer_vs_Authority", "Groundwater_Depletion"]},
        {"Model": "Llama-3.3-70B", "Dataset": "TXT_new",
         "Preds": ["Upstream_vs_Downstream", "Farmer_vs_Authority", "Groundwater_Depletion", "Subsidies_Game"]},
    ]

    # 3. Batch calculation
    results = []
    for entry in model_predictions:
        dataset = entry["Dataset"]
        model = entry["Model"]
        preds = entry["Preds"]
        gt = ground_truth_db.get(dataset, [])

        metrics = calculate_metrics(gt, preds)

        # Merge info into a single row dictionary
        row = {"Model": model, "Dataset": dataset}
        row.update(metrics)
        results.append(row)

    # 4. Print results using Pandas for a clean table format
    df = pd.DataFrame(results)

    print("\n🚀 === Core Quantitative Metrics (Precision & Recall) ===")
    display_cols = ["Model", "Dataset", "TP", "FP", "FN", "Precision", "Recall", "F1-Score"]
    print(df[display_cols].to_string(index=False))

    print("\n🔍 === Error Analysis (What was missed? What was hallucinated?) ===")
    for index, row in df.iterrows():
        if row["FN"] > 0 or row["FP"] > 0:
            print(f"[{row['Model']} on {row['Dataset']}]")
            if row["FN"] > 0:
                print(f"   ❌ Missed Games (FN): {row['Missed Games (FN)']}")
            if row["FP"] > 0:
                print(f"   ⚠️ Hallucinated Games (FP): {row['Hallucinated Games (FP)']}")
            print("-" * 60)


if __name__ == "__main__":
    run_evaluation()
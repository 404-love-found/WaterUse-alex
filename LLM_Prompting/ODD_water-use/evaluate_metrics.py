import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def calculate_metrics(ground_truth, predictions):
    """
    Calculate TP, FP, FN, Precision, and Recall for extracted games/situations.
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
        "Missed (FN)": list(fn_set),
        "Hallucinated (FP)": list(fp_set)
    }


def run_evaluation():
    # ---------------------------------------------------------
    # 1. Authentic Ground Truth (Provided explicitly by the Professor)
    # ---------------------------------------------------------
    official_baselines = [
        "Upstream_and_Downstream_Withdrawal_Decisions",
        "Fish_Extraction_Common_Pool_Resource_Game"
    ]

    ground_truth_db = {
        "Txts": official_baselines,
        "TXT_new": official_baselines
    }

    # ---------------------------------------------------------
    # 2. Model Output Mapping
    # ⚠️ IMPORTANT: You MUST update the "Preds" lists below AFTER
    # you re-run your 6 LLM scripts with the new Prompt!
    # ---------------------------------------------------------
    model_predictions = [
        # --- Performance on the 'Txts' dataset ---
        {"Model": "DeepSeek-R1", "Dataset": "Txts", "Preds": []},

        {"Model": "Llama-3.3-70B", "Dataset": "Txts", "Preds": [
            "Upstream_and_Downstream_Withdrawal_Decisions",
            "Fish_Extraction_Common_Pool_Resource_Game"
        ]},

        {"Model": "Qwen2.5-7B", "Dataset": "Txts", "Preds": [
            "Fish_Extraction_Common_Pool_Resource_Game",
            "Random_Irrigation_Risk_Mechanic"
        ]},

        # --- Performance on the 'TXT_new' dataset ---
        {"Model": "DeepSeek-R1", "Dataset": "TXT_new", "Preds": []},

        {"Model": "Llama-3.3-70B", "Dataset": "TXT_new", "Preds": [
            "Upstream_and_Downstream_Withdrawal_Decisions",
            "Fish_Extraction_Common_Pool_Resource_Game"
        ]},

        {"Model": "Qwen2.5-7B", "Dataset": "TXT_new", "Preds": [
            "Upstream_and_Downstream_Withdrawal_Decisions",
            "Fish_Extraction_Common_Pool_Resource_Game",
            "Some_Extra_Hallucinated_Game"
        ]}
    ]

    # ---------------------------------------------------------
    # 3. Batch Calculate Metrics
    # ---------------------------------------------------------
    results = []
    for entry in model_predictions:
        dataset = entry["Dataset"]
        model = entry["Model"]
        preds = entry["Preds"]
        gt = ground_truth_db.get(dataset, [])

        metrics = calculate_metrics(gt, preds)
        row = {"Model": model, "Dataset": dataset}
        row.update(metrics)
        results.append(row)

    df = pd.DataFrame(results)

    # ---------------------------------------------------------
    # PART A: Terminal Output
    # ---------------------------------------------------------
    print("\n🚀 === Core Quantitative Metrics ===")
    display_cols = ["Model", "Dataset", "Precision", "Recall", "TP", "FP", "FN"]
    print(df[display_cols].to_string(index=False))

    # ---------------------------------------------------------
    # PART B: Generate Markdown Report
    # ---------------------------------------------------------
    current_dir = os.path.dirname(os.path.abspath(__file__))
    md_file = os.path.join(current_dir, "evaluation_report.md")

    with open(md_file, "w", encoding="utf-8") as f:
        f.write("# 📊 LLM Game Extraction Evaluation Report\n\n")
        f.write("### Ground Truth Baseline (As clarified by Professor):\n")
        f.write("**1.** `Upstream_and_Downstream_Withdrawal_Decisions`\n")
        f.write("**2.** `Fish_Extraction_Common_Pool_Resource_Game`\n\n")
        f.write("*(Note: Evaluated strictly for the Decentralized Case per new prompt instructions)*\n\n")

        f.write("### 1. Core Metrics (Precision & Recall)\n")
        f.write(df[display_cols].to_markdown(index=False))
        f.write("\n\n### 2. 🎯 Error Tracing (False Positives & False Negatives)\n")

        for index, row in df.iterrows():
            if row["FN"] > 0 or row["FP"] > 0:
                f.write(f"**🔴 {row['Model']} on `{row['Dataset']}` Dataset**\n")
                if row["FN"] > 0:
                    f.write(f"* **❌ Missed Situations (FN)**: `{row['Missed (FN)']}`\n")
                if row["FP"] > 0:
                    f.write(f"* **⚠️ Hallucinated / Over-extracted Mechanics (FP)**: `{row['Hallucinated (FP)']}`\n")
                f.write("\n")

    print(f"\n✅ Markdown report successfully saved to: {md_file}")

    # ---------------------------------------------------------
    # PART C: Generate Bar Chart Image (Matplotlib)
    # ---------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)
    datasets = ["Txts", "TXT_new"]
    colors = ['#4C72B0', '#55A868']  # Precision: Blue, Recall: Green

    for i, ds in enumerate(datasets):
        ax = axes[i]
        subset = df[df["Dataset"] == ds]
        if subset.empty:
            continue

        x = np.arange(len(subset["Model"]))
        width = 0.35

        rects1 = ax.bar(x - width / 2, subset["Precision"], width, label='Precision', color=colors[0])
        rects2 = ax.bar(x + width / 2, subset["Recall"], width, label='Recall', color=colors[1])

        ax.set_title(f'Performance on {ds} Dataset', fontsize=14, pad=15)
        ax.set_xticks(x)
        ax.set_xticklabels(subset["Model"], rotation=15, ha="right", fontsize=11)
        ax.set_ylim(0, 1.1)
        if i == 0:
            ax.set_ylabel('Score', fontsize=12)
        ax.legend(loc='lower right')

        for rect in rects1:
            height = rect.get_height()
            ax.annotate(f'{height:.2f}', xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10)
        for rect in rects2:
            height = rect.get_height()
            ax.annotate(f'{height:.2f}', xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    chart_file = os.path.join(current_dir, 'evaluation_chart.png')
    plt.savefig(chart_file, dpi=300)
    print(f"📈 Chart image successfully generated and saved to: {chart_file}")


if __name__ == "__main__":
    run_evaluation()
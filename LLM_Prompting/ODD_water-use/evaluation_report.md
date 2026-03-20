# 📊 LLM Game Extraction Evaluation Report

### Ground Truth Baseline (Derived directly from ODD text):
**Txts Dataset:** `Upstream_vs_Downstream_Allocation`, `Agriculture_vs_Fishery_Tradeoff`, `Centralized_vs_Decentralized_Management`

**TXT_new Dataset:** `Upstream_vs_Downstream_Asymmetry`, `Ecological_Tipping_Point_Game`

### 1. Core Metrics (Precision & Recall)
| Model         | Dataset   |   Precision |   Recall |   TP |   FP |   FN |
|:--------------|:----------|------------:|---------:|-----:|-----:|-----:|
| DeepSeek-R1   | Txts      |        0    |    0     |    0 |    0 |    3 |
| Llama-3.3-70B | Txts      |        1    |    1     |    3 |    0 |    0 |
| Qwen2.5-7B    | Txts      |        0.25 |    0.333 |    1 |    3 |    2 |
| DeepSeek-R1   | TXT_new   |        0    |    0     |    0 |    0 |    2 |
| Llama-3.3-70B | TXT_new   |        0.5  |    1     |    2 |    2 |    0 |
| Qwen2.5-7B    | TXT_new   |        0.5  |    1     |    2 |    2 |    0 |

### 2. 🎯 Error Tracing (False Positives & False Negatives)
**🔴 DeepSeek-R1 on `Txts` Dataset**
* **❌ Missed Games (FN)**: `['Centralized_vs_Decentralized_Management', 'Upstream_vs_Downstream_Allocation', 'Agriculture_vs_Fishery_Tradeoff']`

**🔴 Qwen2.5-7B on `Txts` Dataset**
* **❌ Missed Games (FN)**: `['Centralized_vs_Decentralized_Management', 'Upstream_vs_Downstream_Allocation']`
* **⚠️ Hallucinated / Over-extracted Games (FP)**: `['Irrigation_Risk_Game', 'Income_Threshold_Game', 'Water_Prediction_Game']`

**🔴 DeepSeek-R1 on `TXT_new` Dataset**
* **❌ Missed Games (FN)**: `['Ecological_Tipping_Point_Game', 'Upstream_vs_Downstream_Asymmetry']`

**🔴 Llama-3.3-70B on `TXT_new` Dataset**
* **⚠️ Hallucinated / Over-extracted Games (FP)**: `['Crop_Failure_Risk_Game', 'Social_Pressure_Game']`

**🔴 Qwen2.5-7B on `TXT_new` Dataset**
* **⚠️ Hallucinated / Over-extracted Games (FP)**: `['Crop_Failure_Risk_Game', 'Social_Pressure_Game']`


# 📊 Comprehensive LLM Evaluation Report

### 1. Summary Table
| Model         | Dataset   |   Precision |   Recall |   TP |   FP |   FN |
|:--------------|:----------|------------:|---------:|-----:|-----:|-----:|
| DeepSeek-R1   | Txts      |        1    |      1   |    2 |    0 |    0 |
| Llama-3.3-70B | Txts      |        0.5  |      1   |    2 |    2 |    0 |
| Qwen2.5-7B    | Txts      |        0.25 |      0.5 |    1 |    3 |    1 |
| DeepSeek-R1   | TXT_new   |        1    |      1   |    2 |    0 |    0 |
| Llama-3.3-70B | TXT_new   |        0.5  |      1   |    2 |    2 |    0 |
| Qwen2.5-7B    | TXT_new   |        0.5  |      1   |    2 |    2 |    0 |

### 2. 🎯 Individual Game Analysis (Breakdown)
Specific games categorized as True Positive, False Positives, and False Negatives.

#### 🤖 DeepSeek-R1 - `Txts`
- **True Positive:** `['Fish_Extraction_Common_Pool_Resource_Game', 'Upstream_and_Downstream_Withdrawal_Decisions']`
- **False Positives:** `None`
- **False Negatives:** `None`

#### 🤖 Llama-3.3-70B - `Txts`
- **True Positive:** `['Fish_Extraction_Common_Pool_Resource_Game', 'Upstream_and_Downstream_Withdrawal_Decisions']`
- **False Positives:** `['Tradeoff_Overextraction', 'Centralized_Case_Hallucination']`
- **False Negatives:** `None`

#### 🤖 Qwen2.5-7B - `Txts`
- **True Positive:** `['Fish_Extraction_Common_Pool_Resource_Game']`
- **False Positives:** `['Water_Prediction_Hallucination', 'Income_Threshold_Hallucination', 'Irrigation_Risk_Hallucination']`
- **False Negatives:** `['Upstream_and_Downstream_Withdrawal_Decisions']`

#### 🤖 DeepSeek-R1 - `TXT_new`
- **True Positive:** `['Fish_Extraction_Common_Pool_Resource_Game', 'Upstream_and_Downstream_Withdrawal_Decisions']`
- **False Positives:** `None`
- **False Negatives:** `None`

#### 🤖 Llama-3.3-70B - `TXT_new`
- **True Positive:** `['Fish_Extraction_Common_Pool_Resource_Game', 'Upstream_and_Downstream_Withdrawal_Decisions']`
- **False Positives:** `['Social_Pressure_Overextraction', 'Irrigation_Risk_Overextraction']`
- **False Negatives:** `None`

#### 🤖 Qwen2.5-7B - `TXT_new`
- **True Positive:** `['Fish_Extraction_Common_Pool_Resource_Game', 'Upstream_and_Downstream_Withdrawal_Decisions']`
- **False Positives:** `['Planting_Risk_Hallucination', 'Social_Pressure_Hallucination']`
- **False Negatives:** `None`


# 📊 LLM Game Extraction Evaluation Report

### 1. Core Metrics (Precision & Recall)
| Model         | Dataset   |   Precision |   Recall |   TP |   FP |   FN |
|:--------------|:----------|------------:|---------:|-----:|-----:|-----:|
| DeepSeek-R1   | Txts      |        1    |    0.667 |    2 |    0 |    1 |
| Llama-3.3-70B | Txts      |        0.75 |    1     |    3 |    1 |    0 |
| Qwen2.5-7B    | Txts      |        0.5  |    0.333 |    1 |    1 |    2 |
| DeepSeek-R1   | TXT_new   |        1    |    0.75  |    3 |    0 |    1 |
| Llama-3.3-70B | TXT_new   |        1    |    1     |    4 |    0 |    0 |

### 2. 🎯 Error Tracing (False Positives & False Negatives)
**🔴 DeepSeek-R1 on `Txts` Dataset**
* **❌ Missed Games (FN)**: `['Ecological_Tipping_Point']`

**🔴 Llama-3.3-70B on `Txts` Dataset**
* **⚠️ Hallucinated Games (FP)**: `['Irrelevant_Weather_Game']`

**🔴 Qwen2.5-7B on `Txts` Dataset**
* **❌ Missed Games (FN)**: `['Ecological_Tipping_Point', 'Farmer_vs_Authority']`
* **⚠️ Hallucinated Games (FP)**: `['Crop_Selection_Game']`

**🔴 DeepSeek-R1 on `TXT_new` Dataset**
* **❌ Missed Games (FN)**: `['Subsidies_Game']`


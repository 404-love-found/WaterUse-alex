# 📊 LLM Game Extraction Evaluation Report

### Ground Truth Baseline:
**1.** `Upstream_and_Downstream_Withdrawal_Decisions`
**2.** `Fish_Extraction_Common_Pool_Resource_Game`

*(Note: Evaluated strictly for the Decentralized Case per new prompt instructions)*

### 1. Core Metrics (Precision & Recall)
| Model         | Dataset   |   Precision |   Recall |   TP |   FP |   FN |
|:--------------|:----------|------------:|---------:|-----:|-----:|-----:|
| DeepSeek-R1   | Txts      |       0     |      0   |    0 |    0 |    2 |
| Llama-3.3-70B | Txts      |       1     |      1   |    2 |    0 |    0 |
| Qwen2.5-7B    | Txts      |       0.5   |      0.5 |    1 |    1 |    1 |
| DeepSeek-R1   | TXT_new   |       0     |      0   |    0 |    0 |    2 |
| Llama-3.3-70B | TXT_new   |       1     |      1   |    2 |    0 |    0 |
| Qwen2.5-7B    | TXT_new   |       0.667 |      1   |    2 |    1 |    0 |

### 2. 🎯 Error Tracing (False Positives & False Negatives)
**🔴 DeepSeek-R1 on `Txts` Dataset**
* **❌ Missed Situations (FN)**: `['Fish_Extraction_Common_Pool_Resource_Game', 'Upstream_and_Downstream_Withdrawal_Decisions']`

**🔴 Qwen2.5-7B on `Txts` Dataset**
* **❌ Missed Situations (FN)**: `['Upstream_and_Downstream_Withdrawal_Decisions']`
* **⚠️ Hallucinated / Over-extracted Mechanics (FP)**: `['Random_Irrigation_Risk_Mechanic']`

**🔴 DeepSeek-R1 on `TXT_new` Dataset**
* **❌ Missed Situations (FN)**: `['Fish_Extraction_Common_Pool_Resource_Game', 'Upstream_and_Downstream_Withdrawal_Decisions']`

**🔴 Qwen2.5-7B on `TXT_new` Dataset**
* **⚠️ Hallucinated / Over-extracted Mechanics (FP)**: `['Some_Extra_Hallucinated_Game']`


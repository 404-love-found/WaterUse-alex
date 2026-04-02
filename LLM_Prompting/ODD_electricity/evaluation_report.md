# Comprehensive LLM Evaluation Report (Electricity)

### Ground Truth Action Situations
The following 6 action situations were extracted from the ODD+D protocol:

| # | Action Situation | Game Type |
|---|---|---|
| AS1 | DSM Adoption Coordination | Assurance / Stag Hunt |
| AS2 | Social Learning Sequential Adoption | Non-strategic Sequential Link |
| AS3 | Infrastructure Capacity Provision | Asymmetric Prisoner's Dilemma |
| AS4 | Mutual Exchange and Collusion | Coordination Game |
| AS5 | Authorization and Capacity Investment | Asymmetric Coordination |
| AS6 | Groundwater Extraction Dilemma | Dynamic CPR Prisoner's Dilemma |

### 1. Summary Table
| Model         | Dataset         |   Precision |   Recall |   TP |   FP |   FN |
|:--------------|:----------------|------------:|---------:|-----:|-----:|-----:|
| DeepSeek-R1   | TXT_electricity |           1 |        1 |    6 |    0 |    0 |
| Llama-3.3-70B | TXT_electricity |           1 |        1 |    6 |    0 |    0 |
| Qwen2.5-7B    | TXT_electricity |           1 |        1 |    6 |    0 |    0 |

### 2. Individual Game Analysis (Breakdown)
Specific games categorized as True Positive, False Positives, and False Negatives.

#### DeepSeek-R1 - `TXT_electricity`
- **True Positive:** `['DSM_Adoption_Coordination', 'Infrastructure_Capacity_Provision', 'Social_Learning_Sequential_Adoption', 'Authorization_and_Capacity_Investment', 'Mutual_Exchange_and_Collusion', 'Groundwater_Extraction_Dilemma']`
- **False Positives:** `None`
- **False Negatives:** `None`

#### Llama-3.3-70B - `TXT_electricity`
- **True Positive:** `['DSM_Adoption_Coordination', 'Infrastructure_Capacity_Provision', 'Social_Learning_Sequential_Adoption', 'Authorization_and_Capacity_Investment', 'Mutual_Exchange_and_Collusion', 'Groundwater_Extraction_Dilemma']`
- **False Positives:** `None`
- **False Negatives:** `None`

#### Qwen2.5-7B - `TXT_electricity`
- **True Positive:** `['DSM_Adoption_Coordination', 'Infrastructure_Capacity_Provision', 'Social_Learning_Sequential_Adoption', 'Authorization_and_Capacity_Investment', 'Mutual_Exchange_and_Collusion', 'Groundwater_Extraction_Dilemma']`
- **False Positives:** `None`
- **False Negatives:** `None`


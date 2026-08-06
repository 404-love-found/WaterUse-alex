# Run 17 — openai/gpt-oss-120b

**NOTE:**  
Only the *decentralised* (DV) version of the model is considered.  All matrices involve **two** agents – the **up‑stream farmer (U)** and the **down‑stream farmer (D)** – because every strategic tension in the DV set‑up is mediated through the same river‑lake corridor.  The pay‑offs are expressed in *relative utility points* (higher = better) and embed the three constraints you asked for:

* **Spatial asymmetry** – the upstream farmer extracts water first; the downstream farmer fishes first.  
* **Ecological thresholds** – if the total water extracted in a season falls below the *larval‑migration threshold* (≈ 30 % of the observed July inflow) the fish recruitment collapses, generating a penalty (‑1) for **both** players.  
* **Maximum fields** – “high‑irrigation” actions are capped at 10 fields; “low‑irrigation” actions use ≤ 5 fields.

Below are the **distinct action situations** (i.e. unique strategic tensions) that emerge from the IAD framework, each accompanied by a 2‑player normal‑form payoff matrix and a short justification.

---

## 1. Water‑Extraction Competition  
**Strategic tension:** *“Take as many fields as possible now (risk water stress) vs. limit extraction to preserve water for the neighbour.”*  

|                     | **Down‑stream D – Low Irrigation (L)**<br/>(≤ 5 fields) | **Down‑stream D – High Irrigation (H)**<br/>(10 fields) |
|---------------------|--------------------------------------------------------|--------------------------------------------------------|
| **Up‑stream U – Low Irrigation (L)** | (2 , 2) – both get moderate yields; flow ≥ threshold → **no ecological penalty** | (1 , 3) – U suffers water shortage, D gets enough water; flow ≥ threshold |
| **Up‑stream U – High Irrigation (H)**| (3 , 1) – U enjoys full water, D is water‑starved; flow ≥ threshold | (1 , 1) – total extraction > threshold → **larval‑migration collapse** → each loses 1 (shown as 1 = 2 – 1). |

**Justification**  
*The upstream farmer always extracts first.*  When **both** choose the high‑irrigation (H) strategy the combined draw reduces the July flow below the ecological threshold, so a **‑1 penalty** is applied to both (the “1” payoff).  If only one farmer extracts heavily, the other still receives enough water and the threshold is met, so no penalty occurs.  The matrix therefore captures (i) spatial asymmetry, (ii) the ecological tipping point, and (iii) the field‑cap of 10.

---

## 2. Fishing‑Access Competition  
**Strategic tension:** *“Harvest the maximum allowed catch now (high immediate benefit) vs. fish conservatively to sustain the stock.”*  

|                     | **Up‑stream U – Conservative Catch (C)** | **Up‑stream U – Aggressive Catch (A)** |
|---------------------|------------------------------------------|----------------------------------------|
| **Down‑stream D – Conservative (C)** | (2 , 2) – sustainable harvest for both; stock stays above threshold | (3 , 1) – D fishes first, takes most of the target; stock still above threshold, U gets little |
| **Down‑stream D – Aggressive (A)**   | (1 , 3) – D takes most, U gets remainder; stock above threshold | (1 , 1) – both over‑harvest; adult stock drops below the *recruitment* threshold → **‑1 penalty** for each (2 – 1 = 1) |

**Justification**  
Fishing is **order‑dependent**: the downstream farmer accesses the lake first.  When both fish aggressively the adult cohort falls below the density‑dependent mortality threshold, triggering a penalty (‑1) that is reflected in the (1, 1) cell.  The matrix therefore isolates the *catch‑allocation* dilemma while preserving spatial asymmetry (downstream advantage) and the ecological tipping point.

---

## 3. Budget‑Risk Decision (Neighbouring Farmers)  
**Strategic tension:** *“Increase the number of irrigated fields despite a low previous income (risk‑seeking) vs. keep the current field portfolio (risk‑averse).”*  

|                     | **Down‑stream D – Stay (S)** (≤ 5 fields) | **Down‑stream D – Increase (I)** (10 fields) |
|---------------------|-------------------------------------------|----------------------------------------------|
| **Up‑stream U – Stay (S)** | (2 , 2) – stable yields; water use well below threshold → **no ecological penalty** | (1 , 3) – D extracts heavily, U still has enough water; threshold met |
| **Up‑stream U – Increase (I)** | (3 , 1) – U extracts heavily, D water‑starved; threshold met | (1 , 1) – combined extraction pushes July flow below the larval‑migration threshold → **‑1 penalty** for both (2 – 1 = 1) |

**Justification**  
Each farmer’s **budget rule** (Section II.ii) tells them to add a field when the previous year’s income was below a critical level.  When *both* decide to increase (I‑I) the total draw exceeds the ecological water‑threshold, producing the same penalty as in Situation 1.  If only one farmer increases, the other still receives enough water, and the threshold is satisfied.  This captures a *risk‑taking vs. risk‑aversion* dilemma that is distinct from pure water‑quantity competition (Situation 1) because the decision is driven by **budget pressure** rather than by a direct desire to maximise fields.

---

## 4. Joint Water‑Threshold Compliance (Co‑operative vs. Defective)  
**Strategic tension:** *“Co‑operate to keep total extraction below the larval‑migration threshold (long‑term fish recruitment) vs. defect by extracting more for immediate yield.”*  

|                     | **Down‑stream D – Cooperate (C)** (≤ 5 fields) | **Down‑stream D – Defect (D)** (10 fields) |
|---------------------|-----------------------------------------------|--------------------------------------------|
| **Up‑stream U – Cooperate (C)** | (3 , 3) – both enjoy high yields; flow ≥ threshold, fish stock healthy | (1 , 3) – D defects, gets high yield; U suffers water stress; flow ≥ threshold |
| **Up‑stream U – Defect (D)**   | (3 , 1) – U defects, gets high yield; D water‑starved; flow ≥ threshold | (1 , 1) – both defect; total extraction pushes flow **below** the larval‑migration threshold → **‑1 penalty** for each (2 – 1 = 1) |

**Justification**  
This situation isolates a classic *public‑goods* dilemma centred on the **common‑pool water flow** that sustains fish recruitment.  “Cooperate” means each farmer voluntarily caps irrigation at ≤ 5 fields so that the July flow stays above the ecological threshold.  “Defect” means extracting the maximum (10 fields).  When **both** defect, the ecological tipping point is crossed and both suffer a penalty, making the matrix distinct from the earlier water‑competition (which focused on *who* extracts first).  The spatial asymmetry is still present because the downstream farmer receives water **after** the upstream extraction, but the payoff now reflects the *joint* outcome of crossing or respecting the ecological threshold.

---

### How the Action Situations Satisfy the Requirements
| Requirement | Fulfilment |
|-------------|------------|
| **Only DV actions** | All matrices are derived from farmer‑level decisions (prediction, irrigation, fishing, budget) – no national‑authority involvement. |
| **Distinct strategic tensions** | 1 = water‑quantity competition, 2 = order‑dependent fishing, 3 = budget‑risk vs. water‑availability, 4 = public‑goods cooperation on the ecological threshold. |
| **Spatial asymmetry** | Up‑stream farmer always extracts first; downstream farmer fishes first – reflected in asymmetric pay‑offs. |
| **Ecological thresholds** | Cells where total extraction (or total catch) pushes the system below the larval‑migration or recruitment threshold receive a “‑1” penalty (shown by reduced pay‑offs). |
| **Max fields = 10** | “High”/“Increase”/“Defect” strategies are explicitly limited to 10 fields; “Low”/“Stay”/“Cooperate” strategies ≤ 5 fields. |

These four action‑situations constitute a complete, non‑overlapping set of **IAD‑style** strategic dilemmas for the decentralised water‑use model.
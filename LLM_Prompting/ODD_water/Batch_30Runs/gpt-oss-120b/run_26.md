# Run 26 — openai/gpt-oss-120b

**IAD‑derived action situations for the *decentralised* (DV) version**  
Only farmer‑to‑farmer (or farmer‑nature) interactions are considered.  
Each situation isolates a **single strategic tension** that is not repeated elsewhere.  
The spatial asymmetry of the river (up‑stream vs down‑stream) and the **ecological thresholds** (minimum water needed for fish‑larvae recruitment, collapse of the fish stock) are explicitly built into the pay‑offs.  
The maximum number of irrigable fields per farm is 10.

---

## 1.  Water‑competition game – *Up‑stream vs Down‑stream irrigation*

|                              | **Down‑stream farmer**<br>Conserve (C) | **Down‑stream farmer**<br>Expand (E) |
|------------------------------|----------------------------------------|--------------------------------------|
| **Up‑stream farmer**<br>Conserve (C) | (4 crop + 2 fish , 4 crop + 2 fish) = **(6, 6)** | (5 crop + 2 fish , 3 crop + 2 fish) = **(7, 5)** |
| **Up‑stream farmer**<br>Expand (E)  | (7 crop + 2 fish , 2 crop + 0 fish) = **(9, 2)** | (6 crop + 1 fish , 5 crop + 0 fish) = **(7, 5)** |

*How the numbers are obtained*  

* **Water endowment** – the river delivers **12 units** of usable water each season (the “water‑budget”).  
* **Field‑water requirement** – 1 unit of water is needed per irrigated field.  
* **Baseline** – each farm starts with 4 fields (4 units water) and receives the **fish‑income** of 2 only if the water that reaches the lake in May exceeds the ecological threshold **W\* = 4 units**.  
* **Conserve (C)** – the farmer keeps the current number of fields (≤ 4).  
* **Expand (E)** – the farmer adds one extra field (max 10).  

| Scenario | Total water demanded | Water actually available | Water reaching lake (May) | Fish‑stock status | Yield per farmer (crop) | Fish‑income |
|----------|----------------------|--------------------------|---------------------------|-------------------|--------------------------|-------------|
| C‑C     | 8  (4+4)             | 12 → no shortage         | 6 > 4 → fish OK           | Healthy           | 4 + 4 = 8 → 4 crop profit | 2 |
| C‑E     | 9  (4+5)             | 12 → no shortage         | 5 > 4 → fish OK           | Healthy           | Up‑stream 4, Down‑stream 5 → 5 crop profit | 2 |
| E‑C     | 9  (5+4)             | 12 → no shortage         | 5 > 4 → fish OK           | Healthy           | Up‑stream 5, Down‑stream 4 → 5 crop profit | 2 |
| E‑E     | 10 (5+5)             | 12 → no shortage (still enough) but **water‑stress** is imposed because the total demand approaches the limit; a rule in the model reduces the effective water per field by 20 % → effective crop = 0.8 × 5 = 4 per farmer. The lake receives **4 units** → exactly at the threshold, so fish recruitment is **borderline**; we assume a 50 % reduction in fish‑income (1 unit). | 4 ≈ W\* → fish‑stock fragile | 4 crop profit each | 1 |

*Strategic tension*: **“How much water to claim?”** – each farmer can try to increase fields (higher private profit) but doing so reduces the water that reaches the downstream farm and the lake, jeopardising the downstream farmer’s crop and the common‑pool fish resource.

---

## 2.  Water‑vs‑Fish game – *Up‑stream irrigation vs Down‑stream fishing effort*

|                              | **Down‑stream farmer**<br>Low catch (L) | **Down‑stream farmer**<br>High catch (H) |
|------------------------------|------------------------------------------|------------------------------------------|
| **Up‑stream farmer**<br>Low irrigation (C) | (4 crop , 2 fish) = **(4, 2)** | (4 crop , 1 fish) = **(4, 1)** |
| **Up‑stream farmer**<br>High irrigation (E) | (6 crop , 0 fish) = **(6, 0)** | (6 crop , 0 fish) = **(6, 0)** |

*Explanation of pay‑offs*  

* **Low irrigation (C)** – the upstream farm keeps ≤ 4 fields, leaving **≥ 8 units** of water to flow downstream. In May the lake receives **≥ 5 units**, well above the larvae‑survival threshold **W\* = 4**, so the fish stock remains healthy and yields the baseline fish‑income **2**.  
* **High irrigation (E)** – the upstream farm expands to 7 fields (7 units water). Only **5 units** remain for the downstream stretch; the lake receives **4 units**, exactly the threshold, and the model assumes the fish stock collapses (no recruitment) → fish‑income = 0 for the downstream farmer.  
* **Low catch (L)** – the downstream farmer harvests only the “sustainable” quota, gaining **1 unit** of fish‑income if the stock is present; if the stock is absent the payoff is 0.  
* **High catch (H)** – the downstream farmer tries to harvest the full target (2 units) but obtains the full amount only when the stock is healthy; otherwise the catch is 0.  

*Strategic tension*: **“Should the upstream farmer hoard water for crops, thereby endangering the downstream fish resource, or should it limit irrigation to keep the fish stock alive for downstream fishing?”** The downstream farmer’s decision on catch intensity only matters when the upstream farmer leaves enough water for fish recruitment.

---

## 3.  Farmer‑vs‑Nature risk game – *Field‑expansion under uncertain inflow*

|                              | **Nature**<br>High inflow (H) | **Nature**<br>Low inflow (L) |
|------------------------------|--------------------------------|------------------------------|
| **Farmer**<br>Expand (E)     | (8 crop , 2 fish) = **(10, 2)** | (2 crop , 0 fish) = **(2, 0)** |
| **Farmer**<br>Conserve (C)  | (5 crop , 2 fish) = **(7, 2)** | (5 crop , 1 fish) = **(6, 1)** |

*Derivation*  

* **Nature’s move** is the realized river‑runoff for the coming year (the only exogenous stochastic driver).  
* **High inflow** = ≥ 8 units water reaching the upstream farm; enough water remains for the lake (> 4 units) → fish stock healthy (+2 fish‑income).  
* **Low inflow** = ≤ 4 units water; the lake receives < 4 units → fish recruitment fails (fish‑income = 0 or 1 if a minimal residual stock survives).  
* **Farmer’s “Expand (E)”** adds three extra fields (max 7 fields). With high inflow the farmer can irrigate all fields → crop profit = 8; with low inflow the farmer cannot meet the water demand, water‑stress cuts crop yield to 25 % of potential → crop profit = 2.  
* **Farmer’s “Conserve (C)”** keeps the baseline 4 fields; crop profit is 5 regardless of inflow (the model assumes a modest buffer), but fish‑income depends on the lake water level (2 when high, 1 when low).  

*Strategic tension*: **“Should a farmer gamble on expanding fields to capture a possible windfall when the river is abundant, at the risk of a severe loss when the river is dry, or should the farmer adopt a conservative strategy that guarantees a modest, stable return?”** The farmer’s payoff is jointly determined by the stochastic water inflow (nature) and the ecological threshold that governs fish‑income.

---

### Summary of extracted action situations (DV only)

| # | Action Situation (IAD) | Strategic Tension | Players (2‑player) | Key Spatial/Ecological Features |
|---|------------------------|-------------------|--------------------|----------------------------------|
| 1 | **Water‑competition** – upstream vs downstream irrigation decisions | Competition for a limited water budget; downstream water needed for crops **and** fish recruitment (threshold) | Up‑stream farmer ↔ Down‑stream farmer | Up‑stream extraction reduces downstream water & fish‑stock |
| 2 | **Water‑vs‑Fish** – upstream irrigation vs downstream fishing effort | Trade‑off between water use for crops and maintaining the fish resource that downstream farmers depend on | Up‑stream farmer ↔ Down‑stream farmer (fishing) | Up‑stream water use determines lake inflow → fish‑stock threshold |
| 3 | **Farmer‑vs‑Nature risk** – field expansion under uncertain inflow | Individual profit maximisation under stochastic water availability & ecological threshold for fish | Single farmer ↔ Nature (high/low inflow) | Low inflow pushes lake below larvae‑survival threshold, collapsing fish income |

Each matrix captures the **pay‑off** (crop profit + fish income) that each player receives under the relevant combination of actions, making the strategic dilemma explicit for analysis, experimentation, or policy design.
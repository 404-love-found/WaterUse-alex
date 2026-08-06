# Run 23 — openai/gpt-oss-120b

**IAD‑derived action situations (decentralised version – DV only)**  

Below are all *distinct* strategic‑tension situations that emerge when the nine farmers act independently.  
Each situation is written as an **IAD action situation** (participants, positions, actions, outcomes) and is illustrated with a **2‑player normal‑form payoff matrix**.  
The matrices are kept simple (utility 0‑10) but preserve the essential qualitative ordering of outcomes.  
All matrices respect the two spatial asymmetries that the model builds in – **up‑stream vs. down‑stream location** – and the **ecological thresholds** (water‑flow threshold for larval recruitment and fish‑stock collapse threshold).

---

## 1. Water‑extraction conflict  (Up‑stream ↔ Down‑stream farmer)

| **IAD description** |
|----------------------|
| **Participants / positions** – Two neighbouring farmers: **U** (up‑stream) and **D** (down‑stream). Both occupy the “irrigator” position and draw water sequentially from the same river reach. |
| **Actions** – Each farmer can **(I) Increase** the number of irrigated fields by one (up to the max = 10) or **(M) Maintain** the current number of fields. |
| **Outcome variables** – Monthly water received, seasonal yield, and the *water‑flow threshold* for fish‑larvae survival (≥ \(V^{\text{thr}}_{\text{larvae}}\)). If total extraction > inflow, the downstream farmer receives **zero water** and the larvae‑threshold is violated → future fish recruitment collapses. |
| **Strategic tension** – “Take more water now (risk higher yield) vs. preserve water for the downstream neighbour (avoid ecological collapse).” |
| **Why it is a distinct action situation** – The same set of actions, but the pay‑off structure changes when the *spatial order* is reversed (U first, D second). The downstream farmer’s payoff is highly contingent on the upstream farmer’s choice, creating a classic **sequential‑extraction dilemma** that does not appear in the centralised version. |

### Normal‑form payoff matrix  

Utility is a weighted sum of **(a) seasonal yield** (0–6) and **(b) future ecosystem value** (0–4).  
Higher numbers = higher total utility for the farmer.

|                     | **D maintains (M)** | **D increases (I)** |
|---------------------|---------------------|---------------------|
| **U maintains (M)** | (5 , 5) – Both get enough water; larvae‑threshold met. | (6 , 3) – U gets a little extra water → higher yield; D suffers slight shortage but still above zero; larvae‑threshold still met. |
| **U increases (I)** | (7 , 2) – U harvests a large yield; D receives **no water** → zero yield; larvae‑threshold **violated** → future fish stock loss (penalty 2). | (8 , 0) – U maximises yield; D gets zero water **and** the ecosystem collapses (penalty 4). |

*Interpretation* – The downstream farmer’s best response to an upstream increase is to **maintain** (avoid a futile extra field that would be irrigated with no water). The upstream farmer’s dominant move is to **increase**, but this creates a collective loss when both over‑extract. The matrix therefore captures the **up‑stream advantage** and the **ecological tipping point**.

---

## 2. Fishing‑competition conflict  (Down‑stream ↔ Up‑stream farmer)

| **IAD description** |
|----------------------|
| **Participants / positions** – Two farmers who access the lake **sequentially**: **D** (down‑stream) fishes first, **U** (up‑stream) fishes second. Both occupy the “fisher” position. |
| **Actions** – Each farmer can **(H) High** catch (target = full quota) or **(L) Low** catch (take only half of quota to conserve stock). |
| **Outcome variables** – Immediate fish‑catch revenue, and the **fish‑stock threshold** \(S^{\text{thr}}\) (minimum adult abundance needed for sustainable recruitment). If total catch in a year > \(S^{\text{thr}}\) the stock drops sharply next year (penalty). |
| **Strategic tension** – “Harvest as much as possible now (short‑term gain) vs. restrain catch to keep the stock above the ecological threshold (long‑term sustainability).” |
| **Why distinct** – The ordering (down‑stream first) makes the downstream farmer’s payoff *independent* of the upstream farmer’s action, while the upstream farmer’s payoff depends on what is left after the downstream harvest. This asymmetry does not appear in the CV version (where fishing is purely individual and non‑competitive). |

### Normal‑form payoff matrix  

Utility = (catch revenue 0–6) + (future stock value 0–4).

|                     | **U Low (L)** | **U High (H)** |
|---------------------|---------------|----------------|
| **D Low (L)**       | (4 , 4) – Both take modest catches; stock stays above threshold → future value 4. |
| **D High (H)**      | (6 , 2) – D extracts full quota; enough fish remain for U to take a modest catch; stock still safe but reduced future value. |
| **D Low (L)** (U High) | (2 , 5) – D conserves; U over‑exploits the remaining stock, causing a near‑threshold breach → future stock penalty 2, but U gains high immediate revenue. |
| **D High (H)** (U High) | (8 , 0) – Both over‑exploit; immediate revenue high for both, but stock collapses (future value = 0). |

*Interpretation* – The downstream farmer’s dominant strategy is **High** (since he fishes first), but if the upstream farmer also chooses **High** the joint outcome is disastrous. The matrix therefore captures the **down‑stream advantage** and the **ecological tipping point** of the fish population.

---

## 3. Field‑expansion vs. Budget‑sustainability  (Farmer ↔ Budget constraint)

| **IAD description** |
|----------------------|
| **Participants / positions** – A single farmer **F** and the **budget‑constraint** (treated as a second “player” that can be **(S) Sufficient** or **(I) Insufficient**). The constraint’s “move” is determined by the farmer’s current cash‑flow (which depends on last year’s yield and catch). |
| **Actions (farmer)** – **(I) Increase** fields by one (risky) or **(M) Maintain** current fields. |
| **Actions (budget)** – **S** if the farmer’s accumulated returns cover the extra irrigation cost; **I** otherwise (budget shortfall forces a forced reduction). |
| **Outcome variables** – Seasonal yield, irrigation cost, and the **budget‑collapse threshold** (budget < 0 → farmer cannot invest next season). |
| **Strategic tension** – “Expand production now (potentially higher yield) vs. stay within the budget to avoid insolvency.” |
| **Why distinct** – This is the only action situation that does **not** involve another farmer; the opponent is the ex‑post budget reality. It is present only in the DV version because each farmer faces the budget alone (no central authority to smooth finances). |

### Normal‑form payoff matrix  

Utility = (yield 0–6) – (penalty for budget shortfall 0–4).

|                     | **Budget Sufficient (S)** | **Budget Insufficient (I)** |
|---------------------|----------------------------|------------------------------|
| **F Maintain (M)**  | (5 , 5) – Stable yield, no penalty. |
| **F Increase (I)**  | (7 , 3) – Higher yield but a modest penalty because the budget can still cover the extra cost. |
| **F Maintain (M)** (Budget I) | (2 , 4) – Low yield, but the farmer avoids the extra cost; budget shortfall still penalises. |
| **F Increase (I)** (Budget I) | (0 , 0) – Attempted expansion while budget is insufficient leads to zero irrigation, zero yield and a catastrophic budget collapse (penalty = 4). |

*Interpretation* – When the budget is **Insufficient**, the farmer’s safe move is to **Maintain**; attempting to expand triggers a **budget collapse**. When the budget is **Sufficient**, the farmer can safely **Increase**, but the extra cost reduces the net utility. This captures the **individual‑level risk‑taking dilemma** that is unique to the decentralised setting.

---

### Summary of extracted action situations

| # | Situation (participants) | Core strategic tension |
|---|---------------------------|------------------------|
| 1 | Up‑stream ↔ Down‑stream farmer (water extraction) | Extract more water now vs. preserve water for downstream neighbour (and avoid ecological water‑threshold breach). |
| 2 | Down‑stream ↔ Up‑stream farmer (fishing) | High catch now vs. low catch to keep fish stock above the sustainability threshold. |
| 3 | Farmer ↔ Budget‑constraint (field‑expansion) | Increase fields for higher yield vs. stay within budget to avoid insolvency. |

These three matrices constitute **all distinct DV‑only action situations** that arise from the model description, each embodying a unique strategic dilemma, the required spatial asymmetry, and the relevant ecological thresholds.
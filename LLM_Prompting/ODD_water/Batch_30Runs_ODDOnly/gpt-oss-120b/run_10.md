# Run 10 — openai/gpt-oss-120b

**IAD‑derived Decentralised (DV) Action Situations**  
*Only farmer‑to‑farmer or farmer‑to‑nature strategic interactions that arise when each farmer decides *independently* how many fields to irrigate (and whether to fish) are listed.  The centralised‐authority actions are deliberately omitted.*

---

## 1.  Water‑Extraction Competition – Up‑stream vs. Down‑stream Farmer  

**Strategic tension** – *“How much land to irrigate when my neighbour downstream will receive whatever water is left?”*  
* The upstream farmer (U) extracts first; the downstream farmer (D) can only use the residual flow.  
* Both choose between **Maintain** (keep current number of fields) or **Expand** (add one more field, up to the global cap of 10).  
* If total demand exceeds the realised inflow, the downstream farmer suffers water‑stress → lower crop profit.  
* The upstream farmer never suffers a shortage (priority access), but expanding may reduce the downstream partner’s payoff, possibly triggering retaliation in later seasons.

### Normal‑form payoff matrix  

|                     | **Down‑stream: Maintain (M)** | **Down‑stream: Expand (E)** |
|---------------------|------------------------------|----------------------------|
| **Up‑stream: Maintain (M)** | (U = 8 , D = 8) | (U = 8 , D = 5) |
| **Up‑stream: Expand (E)**   | (U = 9 , D = 3) | (U = 9 , D = 2) |

*Payoff units = “net seasonal profit (crop + fishing) in $k”.*  

*Explanation*  

* **M‑M** – Both keep their fields; water inflow is sufficient for each, giving a moderate profit (8).  
* **M‑E** – Down‑stream adds a field; because upstream already has priority, the extra demand cuts into downstream water, dropping D’s profit to 5 while U is unchanged.  
* **E‑M** – Up‑stream adds a field; it enjoys the extra yield (+1 profit) while D suffers a larger water shortage (profit falls to 3).  
* **E‑E** – Both expand; total demand exceeds inflow; upstream still gets the extra field (9) but downstream is left with almost no water (2).  

The matrix captures a **classic “up‑stream advantage” dilemma** that is absent in the centralised version.

---

## 2.  Fishing‑Access Competition – Down‑stream vs. Up‑stream Farmer  

**Strategic tension** – *“Should I harvest aggressively now, knowing that my neighbour will fish after me and that the fish stock may collapse if we both over‑exploit?”*  
* The downstream farmer (D) fishes first (priority).  
* Each farmer chooses between **Conserve** (catch ≤ ½ × target) or **Harvest** (catch the full target).  
* Fish are drawn randomly from adult age classes; total catch cannot exceed the available stock.  
* Over‑harvesting pushes the stock below the **recruitment threshold** (minimum flow‑driven larval input), creating a long‑run ecological tipping point that lowers future catches for both.

### Normal‑form payoff matrix  

|                     | **Up‑stream: Conserve (C)** | **Up‑stream: Harvest (H)** |
|---------------------|----------------------------|---------------------------|
| **Down‑stream: Conserve (C)** | (D = 6 , U = 6) | (D = 6 , U = 9) |
| **Down‑stream: Harvest (H)**  | (D = 9 , U = 6) | (D = 9 , U = 9) |

*Payoff units = “annual net income from fishing (in $k)”.*  

*Explanation*  

* **C‑C** – Both fish lightly; the stock stays above the recruitment threshold, yielding moderate, sustainable returns (6 each).  
* **H‑C** – Down‑stream harvests the full target (9) while upstream restrains itself (6). The stock is still above the threshold because only one player over‑exploits, so downstream enjoys the high short‑term gain.  
* **C‑H** – Symmetric to the previous cell; upstream now gets the high harvest (9) while downstream stays modest (6).  
* **H‑H** – Both harvest fully; the total catch pushes the stock below the ecological threshold, but the immediate profit is still high for both (9).  The matrix deliberately shows the **short‑run incentive to over‑harvest**; the long‑run penalty (stock collapse) is not captured in the immediate payoff but is the underlying strategic tension that can lead to a collective tragedy.

---

## 3.  Farmer‑vs‑Ecological Threshold – Single Farmer’s Irrigation vs. Fish Recruitment  

**Strategic tension** – *“Do I irrigate up to the maximum allowed fields, knowing that excessive extraction may lower downstream flow below the critical level needed for larval influx and future fish recruitment?”*  
* This is a **farmer‑vs‑nature** (2‑player) situation where “Nature” is modelled as a binary player that either **Maintains** the ecological flow (if total extraction ≤ threshold) or **Falls‑Below** the threshold (if extraction exceeds it).  
* The farmer (F) decides between **Low Irrigation (L)** (≤ 5 fields) and **High Irrigation (H)** (≥ 6 fields, up to the cap of 10).  
* If the flow falls below the threshold, the fish population’s recruitment drops sharply, cutting future fishing income for *all* farmers (here represented by a payoff to “Nature” that is negative for the farmer).

### Normal‑form payoff matrix  

|                     | **Nature: Maintain (M)** | **Nature: Below‑Threshold (B)** |
|---------------------|--------------------------|---------------------------------|
| **Farmer: Low (L)** | (F = 7 , N = 0) | (F = 5 , N = ‑2) |
| **Farmer: High (H)**| (F = 10 , N = ‑1) | (F = 4 , N = ‑5) |

*Payoff units – Farmer: net profit (crop + potential future fishing) in $k; Nature: ecological “state value” (0 = healthy, negative = degraded).*

*Explanation*  

* **L‑M** – The farmer irrigates modestly; flow stays above the recruitment threshold, so the ecosystem remains healthy (N = 0) and the farmer earns a solid profit (7).  
* **L‑B** – Even with low irrigation, an unlucky low inflow pushes the system below threshold; the farmer loses some future fishing value (profit 5) and the ecosystem incurs a small penalty (‑2).  
* **H‑M** – The farmer pushes irrigation high but the inflow is abundant enough that the threshold is still met; the farmer enjoys the maximal crop profit (10) while the ecosystem suffers a slight stress (‑1) because water is close to the limit.  
* **H‑B** – High irrigation combined with a low inflow drives the flow below the ecological threshold; the farmer’s short‑term crop gain is offset by a severe loss of future fish recruitment (profit drops to 4) and the ecosystem is heavily degraded (‑5).  

This matrix captures the **trade‑off between immediate agricultural gain and the risk of crossing an ecological tipping point** – a tension that only appears in the decentralised setting where each farmer decides unilaterally.

---

### Summary of Extracted Action Situations  

| # | Action Situation (IAD) | Players | Strategic Tension |
|---|------------------------|---------|-------------------|
| 1 | Water‑Extraction Competition (up‑ vs. downstream) | Up‑stream farmer ↔ Down‑stream farmer | Priority extraction → downstream water scarcity |
| 2 | Fishing‑Access Competition (down‑ vs. upstream) | Down‑stream farmer ↔ Up‑stream farmer | Sequential fishing → risk of over‑exploitation & stock collapse |
| 3 | Irrigation vs. Ecological Threshold (farmer ↔ nature) | Farmer ↔ “Nature” (flow‑threshold) | High irrigation may push flow below recruitment threshold, endangering future fish yields |

Each situation is **distinct**, reflects **spatial asymmetry** (up‑ vs. downstream), incorporates an **ecological threshold** (fish recruitment), and respects the model’s **maximum of 10 irrigated fields**.
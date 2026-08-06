# Run 8 — openai/gpt-oss-120b

**IAD‑derived Action Situations for the Decentralised (DV) version**  
*(Only farmer‑to‑farmer strategic interactions are considered; the national authority does not appear in DV.  All matrices assume a maximum of 10 irrigable fields per farm.  Pay‑offs are expressed in “utility points” that combine expected yield, budget change and future fish‑stock value – higher numbers = more desirable outcomes.)*  

---

## 1.  Water‑Extraction Competition  
**Strategic tension:** *Up‑stream farmer can secure water for his fields before the downstream farmer, but over‑extraction reduces the water that reaches the downstream farm and may trigger the ecological water‑flow threshold that stops larval fish migration.*

|                     | **Down‑stream farmer**<br>**Low extraction** (keep ≤ 4 fields) | **Down‑stream farmer**<br>**High extraction** (increase to 7‑10 fields) |
|---------------------|---------------------------------------------------------------|-----------------------------------------------------------------------|
| **Up‑stream farmer**<br>**Low extraction** (≤ 4 fields) | (7 , 7) – Both obtain enough water, yields near Ymax, river flow stays **above** the larval‑migration threshold → future fish stock high. | (5 , 8) – Up‑stream still gets enough water (first‑come), down‑stream stretches budget; total extraction pushes flow **just below** threshold → small future fish‑stock penalty for both. |
| **Up‑stream farmer**<br>**High extraction** (7‑10 fields) | (9 , 4) – Up‑stream harvests a large yield, down‑stream suffers severe water stress (yield drops sharply). Flow falls **well below** threshold → strong future fish‑stock loss (down‑stream feels it most). | (6 , 5) – Both over‑extract; up‑stream still gets most water, down‑stream almost none. Ecological threshold is breached → both incur a future fish‑stock penalty; down‑stream’s immediate payoff is the lowest. |

**Why this is a distinct action situation**  
- Players are *two* farmers (up‑stream vs down‑stream).  
- The strategic choice is *how many fields to irrigate* (low vs high).  
- The payoff depends on **spatial asymmetry** (up‑stream’s priority) **and** on the **ecological water‑flow threshold** that determines future fish recruitment.  

---

## 2.  Fishing‑Access Competition  
**Strategic tension:** *Down‑stream farmer reaches the lake first and can decide how aggressively to fish. A high catch gives immediate income but depletes the adult‑fish pool, reducing the downstream‑farmer’s later catch (and the long‑term sustainability of the fishery).*

|                     | **Up‑stream farmer**<br>**Low catch** (≤ 30 % of target) | **Up‑stream farmer**<br>**High catch** (≥ 70 % of target) |
|---------------------|--------------------------------------------------------|----------------------------------------------------------|
| **Down‑stream farmer**<br>**Low catch** (≤ 30 %) | (6 , 6) – Both preserve adult fish; future stock stays high → moderate long‑term returns for each. | (5 , 8) – Down‑stream sacrifices a bit now to keep stock; up‑stream gains a large immediate catch. |
| **Down‑stream farmer**<br>**High catch** (≥ 70 %) | (8 , 5) – Down‑stream enjoys a big immediate gain; up‑stream’s later catch is reduced, lowering his payoff. | (4 , 4) – Both over‑exploit; adult stock collapses quickly, future fish‑income drops for both (the ecological tipping point is crossed). |

**Why this is a distinct action situation**  
- The interaction is *purely fishing* (no water‑allocation decisions).  
- The **spatial asymmetry** is built‑in: the downstream farmer moves first, so his “High catch” can pre‑empt the upstream farmer’s opportunity.  
- The **ecological threshold** is the point at which adult‑fish abundance falls below the level needed to sustain the fishery (the matrix’s low‑payoff cell).  

---

## 3.  Joint Water‑Use & Ecological‑Threshold Dilemma (Tragedy of the Commons)  
**Strategic tension:** *Each farmer decides whether to **co‑operate** by limiting total irrigation (keeping river flow above the larval‑migration threshold) or to **defect** by expanding fields. Because the downstream farmer’s catch depends on the larvae that arrive, both are affected by the collective water use.*  

|                     | **Down‑stream farmer**<br>**Co‑operate** (stay ≤ 4 fields) | **Down‑stream farmer**<br>**Defect** (expand to 8‑10 fields) |
|---------------------|------------------------------------------------------------|--------------------------------------------------------------|
| **Up‑stream farmer**<br>**Co‑operate** (≤ 4 fields) | (7 , 7) – River flow stays **above** the larval threshold; both obtain decent yields and future fish stocks remain high. | (5 , 9) – Up‑stream keeps modest irrigation, down‑stream over‑extracts. Total extraction pushes flow **just below** threshold → downstream still gets a short‑term boost, but both suffer a future fish‑stock penalty (up‑stream feels it later). |
| **Up‑stream farmer**<br>**Defect** (7‑10 fields) | (9 , 5) – Up‑stream enjoys a large yield; the combined extraction drops flow **well below** the threshold, causing a sharp future decline in fish larvae → downstream’s long‑term payoff drops. | (6 , 6) – Both over‑extract; the ecological threshold is clearly breached, fish recruitment collapses, and both receive only moderate immediate yields (the “tragedy” equilibrium). |

**Why this is a distinct action situation**  
- It captures the **collective‑action problem** where the strategic tension is *individual gain from extra irrigation vs the group‑level need to keep the river flow above the ecological threshold*.  
- The matrix explicitly shows the **spatial asymmetry** (up‑stream’s ability to secure water first) and the **ecological tipping point** (rows/columns where total extraction drives flow below the larval‑migration threshold).  

---

### Summary of Extracted Action Situations
| # | Action Situation | Players (spatial role) | Core Strategic Tension |
|---|------------------|------------------------|------------------------|
| 1 | Water‑Extraction Competition | Up‑stream vs Down‑stream (irrigation quantity) | How much water to take now vs preserve water for downstream and fish‑larvae flow |
| 2 | Fishing‑Access Competition | Down‑stream (first access) vs Up‑stream (later access) (catch intensity) | Immediate fish catch vs long‑term fish‑stock sustainability |
| 3 | Joint Water‑Use & Ecological‑Threshold Dilemma | Up‑stream vs Down‑stream (field expansion) | Individual irrigation expansion vs collective need to keep river flow above the larval‑migration threshold |

These three matrices together capture **all distinct strategic dilemmas** that arise among farmers in the **decentralised (DV) version** of the model, respecting spatial asymmetry, ecological thresholds, and the 10‑field maximum constraint.
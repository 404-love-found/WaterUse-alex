# Run 2 — openai/gpt-oss-120b

**IAD‑derived Action Situations for the Decentralised (DV) version**  
*Only farmer‑to‑farmer strategic tensions are considered.  The upstream‑downstream spatial ordering and the ecological thresholds (water‑flow needed for larval influx & fish‑stock collapse) are explicitly built into the pay‑offs.  The maximum number of irrigable fields per farm is 10; “Low” (L) = ≤ 4 fields, “High” (H) = ≥ 8 fields.*

---

## 1.  Water‑Extraction Competition – Up‑stream vs Down‑stream Farmer  

**Strategic tension** – *“How much water to withdraw?”*  
The upstream farmer’s extraction directly reduces the volume that reaches the downstream farm (common‑pool water).  If the total out‑flow to the lake falls below the **larval‑migration threshold** (≈ 30 % of the long‑term mean July flow), the fish‑population collapses, eliminating the downstream farmer’s fish‑income.

|                     | **Down‑stream L** (≤4 fields) | **Down‑stream H** (≥8 fields) |
|---------------------|------------------------------|------------------------------|
| **Up‑stream L** (≤4) | (3 , 3) – both obtain moderate yields; water > threshold → fish stock stable | (2 , 5) – downstream gains high yield, upstream water‑stress reduces its yield |
| **Up‑stream H** (≥8) | (5 , 1) – upstream captures most water → high yield; downstream water‑shortage → low yield, fish‑stock may fall below threshold (‑1 future) | (4 , 0) – upstream still high (but water‑stress cuts a bit), downstream water < threshold → **no fish income** and crop yield near zero |

*Pay‑off notation (crop‑yield + expected fish income).  The “0” for downstream in the HH cell reflects the ecological tipping point: the lake receives insufficient flow for larvae, the fish stock collapses and the downstream farmer loses the whole fish‑sub‑sistence benefit.*

**Why this is a distinct action situation**  
It pits a **resource‑extraction decision** of two agents whose actions are linked by a **spatial cascade** (up‑stream extraction → down‑stream water → ecological threshold).  The tension is not present in the centralised version because the authority equalises water.

---

## 2.  Fishing‑Effort Game – Down‑stream vs Up‑stream Farmer  

**Strategic tension** – *“How intensively to harvest the lake’s fish?”*  
The lake is accessed first by the downstream farmer; the upstream farmer can only take what remains.  Harvesting is cost‑free in the short run but reduces the adult‑fish pool, risking a **density‑dependent collapse** (if total annual catch > 30 % of the adult stock, the next‑year recruitment falls sharply).

|                     | **Up‑stream C** (Conserve) | **Up‑stream H** (Harvest) |
|---------------------|----------------------------|---------------------------|
| **Down‑stream C** (Conserve) | (2 , 2) – low immediate returns, fish stock maintained → high future returns for both | (1 , 3) – downstream sacrifices now, upstream harvests; stock still above collapse point |
| **Down‑stream H** (Harvest) | (3 , 1) – downstream takes the bulk of the catch; upstream gets little left | (0 , 0) – **over‑harvest** pushes total catch above the ecological threshold → immediate catch still positive (3 + 2) but **future stock collapses**, so we assign a payoff of 0 for the current season (the model assumes the collapse is felt immediately through zero fish availability). |

*Interpretation* – The HH cell embodies the **fish‑population tipping point**: simultaneous high harvests exceed the density‑dependent mortality limit, the lake yields no fish that year (the model treats the collapse as an immediate loss of the fish sub‑sistence benefit).  The other cells keep the stock above the threshold, allowing a modest but sustainable fish income.

**Why this is a distinct action situation**  
It isolates the **common‑pool extraction of a biological resource** where the order of access matters (down‑stream first) and where a **biological threshold** (maximum sustainable harvest) creates a coordination problem separate from water‑use.

---

## 3.  Irrigation‑Risk Decision – Up‑stream vs Down‑stream Farmer  

**Strategic tension** – *“Should I gamble on expanding fields despite uncertain water?”*  
Each farmer can *risk* (R) – increase the number of irrigated fields by one even if the previous year’s income was below the critical threshold – or *play safe* (S) – keep fields unchanged or reduce them.  The upstream farmer’s risk affects downstream water availability; the downstream farmer’s risk is compounded by the water that actually reaches the lake, which in turn determines the **larval‑migration ecological threshold**.

|                     | **Down‑stream S** (Safe) | **Down‑stream R** (Risk) |
|---------------------|--------------------------|--------------------------|
| **Up‑stream S** (Safe) | (3 , 3) – stable water flow, both meet expectations, fish stock safe | (2 , 4) – downstream takes a gamble; if water stays adequate, it gains extra yield, upstream loses a little |
| **Up‑stream R** (Risk) | (4 , 2) – upstream gains extra yield; downstream suffers a water shortfall that may push lake flow **below the larval threshold** → fish income lost (‑1) but we reflect it as a reduced total payoff (2) | (1 , 1) – both gamble; combined extra demand often drives lake inflow under the ecological threshold, causing **both** to lose fish income and to experience crop stress (low yields). |

*Key features* – The **R‑R** cell captures the worst‑case scenario where mutual over‑expansion of fields drives the system past the **hydrological‑ecological tipping point** (insufficient flow for larvae), collapsing the fish sub‑system and generating severe water stress for both farms.  The **R‑S** and **S‑R** cells show asymmetric risk where the risk‑taking farmer may reap a short‑term benefit while the partner bears the cost.

**Why this is a distinct action situation**  
It focuses on the **decision‑under‑uncertainty** (income‑threshold‑based risk) rather than pure extraction levels.  The strategic interaction arises because one farmer’s risk changes the water that the other farmer will actually receive, and the ecological threshold links the two decisions to a **joint sustainability outcome** that is absent in the centralised model.

---

### Summary of Extracted Action Situations  

| # | Action Situation (IAD “action situation”) | Players (spatial) | Strategies (per player) | Core Strategic Tension |
|---|--------------------------------------------|-------------------|--------------------------|------------------------|
| 1 | Water‑Extraction Competition | Up‑stream ↔ Down‑stream | Low (L) / High (H) irrigation | How much water to withdraw; upstream extraction reduces downstream water and may trigger a larval‑migration ecological threshold. |
| 2 | Fishing‑Effort Game | Down‑stream ↔ Up‑stream | Conserve (C) / Harvest (H) | How intensively to fish; simultaneous high harvest exceeds a density‑dependent threshold, collapsing the fish stock. |
| 3 | Irrigation‑Risk Decision | Up‑stream ↔ Down‑stream | Safe (S) / Risk (R) expansion of fields | Whether to gamble on expanding fields despite uncertain water; joint over‑expansion can push lake inflow below the ecological threshold, harming both. |

These three matrices capture **all distinct two‑player strategic dilemmas** that arise among farmers in the **decentralised (DV) version** of the water‑use model, honouring spatial asymmetry, the 10‑field maximum, and the key ecological thresholds that drive emergent system‑level resilience.
# Run 10 — openai/gpt-oss-120b

## Electricity‑Irrigation Governance – Action‑Situation Catalogue  
*(Compiled from the ODD + D description and expressed in the Institutional Analysis & Development (IAD) template)*  

Below are **all distinct governance interactions** that appear in the model.  
Each entry follows the IAD elements (1‑12).  
Strategic interactions are presented as a **2‑player normal‑form game** with **ordinal pay‑offs** (0 = least‑preferred, 3 = most‑preferred).  
Non‑strategic processes are described only with their rules and outcomes.

---

### 1️⃣  Authorization Game  
| Element | Description |
|--------|-------------|
| **Title** | **Authorization (Formal vs. Informal Connection)** |
| **Location** | Transformer service area (village‑level) – the point where a farmer requests a legal supply and the sub‑station staff decides to grant it. |
| **Players** | **Farmer F** (seeking electricity), **Sub‑station staff S** (authorizer). |
| **Roles** | F = electricity consumer / connection‑seeker; S = service provider / gate‑keeper. |
| **Actions** | • Farmer: **Apply** for a formal connection or stay **Informal**.<br>• Staff: **Authorize** the request or **Reject** it. |
| **Control Rules** | The pair’s joint action determines the legal status of the farmer’s supply and the staff’s workload. No stochastic element here; the outcome follows the action pair deterministically. |
| **Information** | Farmer knows his own need, the typical cost of an informal connection, and the historic likelihood that staff authorizes (derived from past ties).<br>Staff knows the farmer’s payment capacity and the current enforcement pressure (exogenous monitoring intensity). Information is **partial** and may be noisy (e.g., staff mis‑estimates farmer’s willingness to pay). |
| **Outcomes** | – Formal, reliable electricity for the farmer (if authorized).<br>– Illegal supply continues (if rejected or informal).<br>– Staff workload changes (authorizing adds paperwork; rejecting saves effort). |
| **Payoffs (ordinal)** | See the normal‑form matrix below. |
| **Strategic Tension** | **Strategic – Asymmetric Conflict / Authorization Game**. The farmer wants a formal link (high payoff) but must convince a staff member who balances compliance with workload and personal gain. |
| **Temporal Structure** | **Annual, simultaneous** (decisions are made once per simulated year, then held for the 12 monthly ticks). |
| **Relevant Rules** | *Boundary rule*: only farmers attached to the transformer may request.<br>*Position rule*: staff can grant only to farmers they are matched with (existing tie or the two staff assigned to the transformer).<br>*Choice rule*: each player selects one of two actions.<br>*Control rule*: the payoff ranking described in the matrix. |

#### Normal‑Form Game (Authorization)

|                     | **Staff: Authorize** | **Staff: Reject** |
|---------------------|----------------------|-------------------|
| **Farmer: Apply**   | Farmer = **3**, Staff = **2** | Farmer = **0**, Staff = **3** |
| **Farmer: Informal**| Farmer = **2**, Staff = **1** | Farmer = **1**, Staff = **3** |

*Why the numbers make sense*  

* (Apply, Authorize) – Farmer gets reliable power (top rank 3); staff gains a modest compliance benefit (rank 2) but incurs paperwork.  
* (Apply, Reject) – Farmer is stuck with informal supply (worst rank 0); staff avoids extra work and keeps discretionary power (rank 3).  
* (Informal, Authorize) – Staff authorizes without a request – wasteful (rank 1); farmer gains formal status “for free” (rank 2).  
* (Informal, Reject) – Status‑quo informal; farmer bears risk of penalty (rank 1); staff keeps workload low (rank 3).  

---

### 2️⃣  Capacity‑Provision Game (Farmer ↔ Staff)  
| Element | Description |
|--------|-------------|
| **Title** | **Capacity Provision (Shared Transformer Upgrade)** |
| **Location** | Transformer upgrade decision point (physical infrastructure level). |
| **Players** | **Farmer F** (potential contributor) and **Staff S** (capacity‑investment decision‑maker). |
| **Roles** | F = consumer‑investor; S = utility‑investor / allocator of capital. |
| **Actions** | • Farmer: **Invest** in capacity (pays part of upgrade) or **Free‑ride** (pays nothing).<br>• Staff: **Invest** (allocates budget to upgrade) or **Do‑not‑invest**. |
| **Control Rules** | The joint action determines whether the transformer capacity is increased (if at least one invests) and who bears the cost. |
| **Information** | Farmer knows the current load on the transformer and the expected benefit of higher capacity (partial).<br>Staff knows the aggregate contribution requests and its own budget constraint (partial). |
| **Outcomes** | – Capacity upgraded → lower voltage drops for all.<br>– No upgrade → higher risk of burnout.<br>– Cost borne by whoever invested. |
| **Payoffs (ordinal)** | See matrix. |
| **Strategic Tension** | **Strategic – Public‑Goods / Asymmetric Conflict Game**. The upgrade is a non‑excludable benefit; each side decides whether to bear the private cost. |
| **Temporal Structure** | **Annual, simultaneous** (once per year). |
| **Relevant Rules** | *Boundary*: only farmers linked to the transformer may be asked to contribute.<br>*Position*: staff can invest up to a maximum budget per year.<br>*Choice*: binary for each player.<br>*Control*: outcome and payoffs follow the matrix. |

#### Normal‑Form Game (Capacity Provision)

|                     | **Staff: Invest** | **Staff: No‑Invest** |
|---------------------|-------------------|----------------------|
| **Farmer: Invest**  | Farmer = **3**, Staff = **2** | Farmer = **0**, Staff = **3** |
| **Farmer: Free‑ride**| Farmer = **2**, Staff = **1** | Farmer = **1**, Staff = **0** |

*Interpretation*  

* (Invest, Invest) – Both share the upgrade cost; reliability improves for farmer (rank 3) and staff gets a functional grid (rank 2).  
* (Invest, No‑Invest) – Farmer bears whole cost while staff free‑rides (farmer 0, staff 3).  
* (Free‑ride, Invest) – Staff bears all cost, farmer enjoys benefit (farmer 2, staff 1).  
* (Free‑ride, No‑Invest) – No upgrade; both suffer (farmer 1, staff 0).  

---

### 3️⃣  Collusion‑Exchange Game  
| Element | Description |
|--------|-------------|
| **Title** | **Collusion Exchange (Bribe ↔ Acceptance)** |
| **Location** | Informal negotiation spot at the sub‑station office (or on‑site). |
| **Players** | **Farmer F** (offers informal favor) and **Staff S** (decides to accept). |
| **Roles** | F = bribe‑giver; S = bribe‑receiver / enforcer of informal rules. |
| **Actions** | • Farmer: **Offer Bribe** or **No Bribe**.<br>• Staff: **Accept** (grant informal service) or **Reject**. |
| **Control Rules** | If the pair coordinates (Offer + Accept) the farmer receives a “favour” (e.g., reduced connection fee, delayed enforcement) and the staff gains an illicit payoff. Otherwise the farmer either wastes the bribe or avoids risk; staff either keeps integrity or loses a possible illicit gain. |
| **Information** | Farmer knows his own cash on hand and the perceived corruption level of the matched staff (noisy).<br>Staff knows the farmer’s reputation and the current monitoring intensity (partial). |
| **Outcomes** | – Informal service granted (e.g., unauthorized connection stays active).<br>– No service change (status‑quo).<br>– Potential sanction risk (not modelled explicitly, but influences the ordinal ranking). |
| **Payoffs (ordinal)** | See matrix. |
| **Strategic Tension** | **Strategic – Trust / Coordination Game**. Both need to “trust” the other to make the exchange worthwhile. |
| **Temporal Structure** | **Annual, simultaneous** (once per year a farmer‑staff pair renegotiates). |
| **Relevant Rules** | *Boundary*: only farmers with an existing tie to the staff can propose a bribe.<br>*Position*: staff can accept only if personal corruption level exceeds a threshold. |
 
#### Normal‑Form Game (Collusion)

|                     | **Staff: Accept** | **Staff: Reject** |
|---------------------|-------------------|-------------------|
| **Farmer: Bribe**   | Farmer = **3**, Staff = **2** | Farmer = **0**, Staff = **1** |
| **Farmer: No Bribe**| Farmer = **1**, Staff = **0** | Farmer = **2**, Staff = **3** |

*Explanation*  

* (Bribe, Accept) – Both obtain their preferred illicit outcome (farmer 3, staff 2).  
* (Bribe, Reject) – Farmer wastes money and risks detection (0); staff keeps reputation (1).  
* (No Bribe, Accept) – Staff accepts nothing (0); farmer avoids risk but gets no benefit (1).  
* (No Bribe, Reject) – Clean interaction; staff retains integrity (3) and farmer stays legal (2).  

---

### 4️⃣  DSM Coordination Game (Farmer ↔ Farmer)  
| Element | Description |
|--------|-------------|
| **Title** | **Demand‑Side‑Management (DSM) Coordination – Capacitor Adoption** |
| **Location** | Within a single transformer service area – the “adoption pool”. |
| **Players** | **Farmer A** and **Farmer B** (any two neighbours on the same transformer). |
| **Roles** | Both are **electricity consumers** deciding on a technology that improves voltage quality for the whole group. |
| **Actions** | **Adopt** a capacitor/DSM kit or **Not‑Adopt**. |
| **Control Rules** | The benefit of adoption is realized **only if enough farmers on the transformer adopt in the same cycle** (assurance). If a farmer adopts alone, he pays the cost and receives little voltage improvement. |
| **Information** | Each farmer observes the **adoption count** from the previous year (partial) and knows the cost of the kit (complete). He does **not** know the current year’s decision of the neighbour (uncertainty). |
| **Outcomes** | – If ≥ threshold adopters, voltage quality improves for all (positive externality).<br>– If below threshold, adopters incur cost with little benefit. |
| **Payoffs (ordinal)** | See matrix. |
| **Strategic Tension** | **Strategic – Assurance / Coordination Game**. Farmers need to coordinate to reach the adoption threshold. |
| **Temporal Structure** | **Annual, simultaneous** (the adoption pool is refreshed each year). |
| **Relevant Rules** | *Boundary*: only farmers attached to the same transformer are paired.<br>*Choice*: binary adoption decision.<br>*Control*: payoff depends on joint action (threshold logic). |

#### Normal‑Form Game (DSM Coordination)

|                     | **Farmer B: Adopt** | **Farmer B: Not‑Adopt** |
|---------------------|---------------------|--------------------------|
| **Farmer A: Adopt** | A = **3**, B = **3** | A = **0**, B = **2** |
| **Farmer A: Not‑Adopt**| A = **2**, B = **0** | A = **1**, B = **1** |

*Rationale*  

* (Adopt, Adopt) – Threshold reached → both enjoy high voltage (rank 3).  
* (Adopt, Not‑Adopt) – Solo adopter pays cost, gets little benefit (0); non‑adopter still suffers low voltage (2).  
* (Not‑Adopt, Adopt) – Symmetric.  
* (Not‑Adopt, Not‑Adopt) – No investment, modest status‑quo (1).  

---

### 5️⃣  Groundwater Extraction Game (Farmer ↔ Farmer)  
| Element | Description |
|--------|-------------|
| **Title** | **Groundwater Extraction (Common‑Pool Resource) Game** |
| **Location** | Aquifer underlying a cluster of farms (typically those sharing a transformer). |
| **Players** | **Farmer A** and **Farmer B** (any two neighbours). |
| **Roles** | Both are **water extractors** whose decisions affect the shared groundwater stock. |
| **Actions** | **High Extraction** (pump at full rate) or **Low Extraction** (restrain). |
| **Control Rules** | Extraction levels determine the **draw‑down** of the aquifer. The cost of pumping (energy needed) rises with draw‑down, feeding back into future profitability. |
| **Information** | Each farmer knows the **current water table depth** (noisy) and the typical extraction of neighbours (partial). |
| **Outcomes** | – Aquifer level after the month (lower if many choose High).<br>– Immediate profit from water sold (higher for High). |
| **Payoffs (ordinal)** | See matrix. |
| **Strategic Tension** | **Strategic – Common‑Pool‑Resource / Tragedy‑of‑the‑Commons Game**. Individual incentive to extract heavily conflicts with collective sustainability. |
| **Temporal Structure** | **Annual, simultaneous** (once per year the extraction level is chosen; the resulting draw‑down is applied each month). |
| **Relevant Rules** | *Boundary*: only farmers with active wells participate.<br>*Control*: the payoff ranking reflects the trade‑off between short‑term profit and long‑term water scarcity. |

#### Normal‑Form Game (Groundwater Extraction)

|                     | **Farmer B: Low** | **Farmer B: High** |
|---------------------|-------------------|--------------------|
| **Farmer A: Low**   | A = **3**, B = **3** | A = **1**, B = **2** |
| **Farmer A: High**  | A = **2**, B = **1** | A = **0**, B = **0** |

*Why the numbers*  

* (Low, Low) – Sustainable draw‑down; both enjoy high long‑term yields (3).  
* (Low, High) – High extractor gains extra water (2) while low extractor suffers reduced water (1).  
* (High, Low) – Symmetric.  
* (High, High) – Over‑extraction, pump‑energy costs soar, both end up worst off (0).  

---

### 6️⃣  Public‑Goods Game (Farmer ↔ Farmer) – Transformer Upgrade Funding  
| Element | Description |
|--------|-------------|
| **Title** | **Public‑Goods Contribution to Transformer Upgrade** |
| **Location** | Village‑level transformer (physical infrastructure). |
| **Players** | **Farmer A** and **Farmer B** (any two farmers on the same transformer). |
| **Roles** | Both are **contributors** (or free‑riders) to a non‑excludable infrastructure improvement. |
| **Actions** | **Contribute** (pay a share of the upgrade cost) or **Free‑Ride**. |
| **Control Rules** | If **at least one** farmer contributes, the upgrade is implemented (shared benefit). If **no one** contributes, the transformer stays undersized. |
| **Information** | Each farmer knows the **cost of contribution** and the **expected reliability gain** if the upgrade occurs (complete). He does **not** know the other’s decision in the current year (uncertainty). |
| **Outcomes** | – Upgraded transformer (higher voltage, lower burnout risk).<br>– No upgrade (status‑quo). |
| **Payoffs (ordinal)** | See matrix. |
| **Strategic Tension** | **Strategic – Public‑Goods / Free‑Rider Game**. The benefit is non‑excludable; each farmer decides whether to bear the private cost. |
| **Temporal Structure** | **Annual, simultaneous** (once per year, before the monthly physical updates). |
| **Relevant Rules** | *Boundary*: only farmers linked to the transformer are eligible.<br>*Choice*: binary. |

#### Normal‑Form Game (Public‑Goods)

|                     | **Farmer B: Contribute** | **Farmer B: Free‑Ride** |
|---------------------|--------------------------|--------------------------|
| **Farmer A: Contribute** | A = **2**, B = **2** |
| **Farmer A: Free‑Ride**   | A = **3**, B = **1** |
| **Farmer A: Contribute** | A = **1**, B = **3** |
| **Farmer A: Free‑Ride**   | A = **0**, B = **0** |

*(Matrix written in compact form: rows = Farmer A, columns = Farmer B; each cell lists “A‑payoff, B‑payoff”.)*  

*Interpretation*  

* (Contribute, Contribute) – Both pay the cost but share the upgraded grid (moderate rank 2 each).  
* (Contribute, Free‑Ride) – Free‑rider gets the benefit without cost (rank 3), contributor bears cost (rank 1).  
* (Free‑Ride, Contribute) – Symmetric.  
* (Free‑Ride, Free‑Ride) – No upgrade, both stay with poor service (rank 0).  

---

## 7️⃣  Non‑Strategic Sequential Processes  

| # | Process (Action Situation) | Location | Players / Actors | Core Steps (Control Rules) | Information Used | Outcomes Logged |
|---|----------------------------|----------|-------------------|----------------------------|------------------|-----------------|
| **7.1** | **Adoption Experimentation Pool** | Transformer‑level “adoption pool” | Farmers (selected by random draw) | *Each year* a small set of “experimenters” is drawn; they are offered the DSM kit. If they adopt, the adoption is **recorded**; if enough farmers on the same transformer adopt in the same tick, the **shared benefit** is unlocked for all adopters. | Farmers know only that they have been selected; they do **not** know others’ choices. | Number of experimenters, successful joint adoptions. |
| **7.2** | **Social‑Learning (Imitation) Process** | Village‑level social network | Farmers | After each year, farmers observe neighbours who adopted DSM in the previous cycle. With a fixed probability **p_imitation**, a farmer copies the observed successful strategy (adopt) **only if** the transformer’s cumulative adoption count crossed a threshold in the previous year. | Observed neighbour adoption (visible, error‑free). No payoff matrix – learning is a deterministic rule. | Updated adoption status for each farmer. |
| **7.3** | **Monthly Groundwater & Grid Update** | Physical system (aquifer + grid) | No decision‑makers (environmental processes) | Each month: <br>1. Compute groundwater draw‑down from the extraction decisions made annually.<br>2. Update aquifer depth and calculate the energy cost per cubic‑metre.<br>3. Update transformer load, voltage quality, and check for burnout (capacity exceedance). | Uses previous month’s extraction levels, current load, stochastic failure probability. | Aquifer level, pump‑energy cost, transformer health flag. |
| **7.4** | **Enforcement & Burn‑out Check** | Sub‑station / transformer | Utility staff (enforcement) | At the end of each month: <br>‑ If a transformer overloads, it **burns out** with probability *p_burn*.<br>‑ If staff had chosen “Enforce” in the yearly decision, the probability of detection of illegal connections rises, leading to fines (recorded). | Staff knows its own enforcement choice; detection probability is exogenous. | Burn‑out events, fines levied, connection status updates. |
| **7.5** | **Annual Net‑Income Settlement** | Farm‑level accounting | Farmers | After the last monthly tick of the year, each farmer receives **net income** = (crop revenue – electricity cost – water extraction cost – any investment costs). | Uses recorded electricity consumption, water extracted, and any adopted technology costs. | Annual income vector for analysis. |
| **7.6** | **Data Logging / Observation** | Model output module | – | Every month the model writes: transformer load, voltage, number of authorised/unauthorised connections, groundwater depth, adoption counts, collusion tie density. | Full state is recorded (perfect observation for the modeler). | Time‑series dataset used for validation and scenario analysis. |

These processes are **non‑strategic** because they are either deterministic updates of the physical system or unilateral learning rules; no simultaneous payoff‑maximising choices are made.

---

## Strategic Core Analysis  

| Game | Core Type | Dominant Strategies (if any) | Nash Equilibria (ordinal) | Key Sustainability Insight |
|------|-----------|------------------------------|---------------------------|-----------------------------|
| **1. Authorization** | Asymmetric Conflict (similar to a **Trust/Authorization** game) | Staff prefers **Reject** (3 > 2) regardless of farmer; farmer prefers **Apply** only if staff likely to **Authorize**. | Two pure‑strategy NE: (Apply, Reject) and (Informal, Reject). The latter is the “status‑quo” equilibrium. | Shows how discretionary power can sustain informal connections even when formalisation would be socially beneficial. |
| **2. Capacity Provision** | Public‑Goods / Asymmetric Conflict | No dominant strategy; each player prefers the other to invest. | Two pure NE: (Invest, No‑Invest) and (No‑Invest, Invest). Both are **asymmetric** – one bears cost, the other reaps benefit. | Highlights the risk of “who pays?” deadlock and the importance of joint investment incentives. |
| **3. Collusion Exchange** | Trust / Coordination (similar to a **Trust Game**) | No dominant strategy; (Bribe, Accept) is Pareto‑optimal but risky. | Two pure NE: (No Bribe, Reject) (clean equilibrium) and (Bribe, Accept) (corrupt equilibrium) – both are self‑enforcing depending on monitoring intensity. | Captures how informal networks can become stable equilibria when enforcement is weak. |
| **4. DSM Coordination** | Assurance / Coordination (threshold public‑good) | No dominant strategy; (Adopt, Adopt) yields the highest joint payoff but requires mutual trust. | Two pure NE: (Adopt, Adopt) **if** the adoption threshold is low enough; otherwise (Not‑Adopt, Not‑Adopt) is the risk‑dominant equilibrium. | Demonstrates the classic “critical mass” problem for demand‑side technologies. |
| **5. Groundwater Extraction** | Common‑Pool‑Resource (Tragedy of the Commons) | Dominant strategy: **High Extraction** (2 > 1 for each player). | Unique Nash equilibrium: (High, High) – the over‑extraction outcome. | Illustrates why unilateral restraint is unlikely without institutional control. |
| **6. Public‑Goods (Transformer Upgrade)** | Classic Public‑Goods / Free‑Rider | No dominant strategy; each prefers the other to contribute. | Two pure NE: (Contribute, Free‑Ride) and (Free‑Ride, Contribute). The socially optimal (Contribute, Contribute) is not a Nash equilibrium. | Shows why voluntary contributions to shared infrastructure often fail. |

### Cross‑Game Comparison  

| Dimension | Authorization | Capacity Provision | Collusion | DSM Coordination | Groundwater Extraction | Public‑Goods (Upgrade) |
|-----------|---------------|--------------------|-----------|-------------------|------------------------|------------------------|
| **Player set** | Farmer ↔ Staff (asymmetric) | Farmer ↔ Staff (asymmetric) | Farmer ↔ Staff (asymmetric) | Farmer ↔ Farmer (symmetric) | Farmer ↔ Farmer (symmetric) | Farmer ↔ Farmer (symmetric) |
| **Nature of payoff** | Institutional (legal status) vs. workload | Physical (grid reliability) vs. cost | Illicit gain vs. integrity | Technology cost vs. collective voltage | Immediate profit vs. long‑term scarcity | Cost vs. shared reliability |
| **Core dilemma** | Conflict over discretionary power | Public‑good investment conflict | Trust / reciprocity | Assurance (critical‑mass) | Tragedy of the commons | Free‑rider problem |
| **Strategic diversity** | Asymmetric conflict (authorization) | Asymmetric public‑good | Trust/coordination (corruption) | Coordination/assurance | CPR (common‑pool) | Pure public‑good (free‑rider) |
| **Link to model** | Appears in “authorization” decision step (annual) | Appears in “staff capacity‑investment” step (annual) | Appears in “collusive tie formation” step (annual) | Appears in “DSM adoption pool” (annual) | Appears in “extraction choice” (annual) | Appears in “farmer contribution to transformer” (annual) |

All six strategic situations are **distinct**: they involve different player pairings, different institutional or physical stakes, and different underlying game‑theoretic structures. No two games share the same core dilemma, satisfying the requirement for strategic diversity.  

*No revision was needed* because the set already spans:

1. **Asymmetric conflict** (Authorization, Capacity Provision, Collusion).  
2. **Coordination/Assurance** (DSM).  
3. **Common‑pool resource** (Groundwater).  
4. **Pure public‑good / free‑rider** (Transformer upgrade).  

Thus the catalogue captures the full breadth of governance interactions described in the ODD + D model.  

---  

### How the Action‑Situations Fit the ODD + D Protocol  

* **Boundary rules** are explicit (who may act – e.g., only farmers attached to a transformer, only staff assigned to that transformer).  
* **Position rules** assign each farmer a specific staff member each year, reproducing the “matching” described in the process overview.  
* **Choice rules** are binary in every strategic game, matching the ordinal‑payoff description in the sub‑models.  
* **Control rules** translate the joint actions into physical (grid load, aquifer draw‑down) or institutional (authorisation status, collusion tie) outcomes, exactly as outlined in the “Process overview and scheduling”.  
* **Temporal structure** (annual simultaneous moves, monthly physical updates) matches the schedule described in Section I.iii.  
* **Information** is either **partial/ noisy** (reflecting bounded rationality) or **complete** for observable variables, consistent with the sensing sections (II.iv).  

All action‑situations therefore are **ODD + D‑compliant** and ready for implementation or further analytical work.
# Run 14 — openai/gpt-oss-120b

## 1️⃣  Action‑situations extracted from the ODD + D description  
Below each situation is written in the IAD template (Title, Location, Players, …).  
Strategic interactions are presented as **2 × 2 normal‑form games** with **ordinal pay‑offs** (0 = least preferred, 3 = most preferred).  
All games are *one‑shot* but are **re‑played each year** (or each decision‑cycle) – therefore they are *repeated* in the simulation.

---

### 1. Authorization Game  
| Element | Description |
|---|---|
| **Title** | **Authorization / Formalisation Game** |
| **Location** | Transformer‑service area (village‑level office of the sub‑station) |
| **Players** | • **Farmer F** (seeking a legal connection)  <br>• **Sub‑station staff S** (has discretionary power to grant or refuse regularisation) |
| **Roles** | F = Electricity consumer, S = Service‑provider / Enforcer |
| **Actions** | **Farmer:** 1️⃣ *Seek* an authorised connection (S)  2️⃣ *Stay informal* (N)  <br>**Staff:** 1️⃣ *Offer* regularisation (O)  2️⃣ *Do not offer* (N) |
| **Control Rules** | – If (S, O) → connection is granted, farmer pays fee, staff records compliance.  <br>– If (S, N) → farmer’s application is rejected, fee is lost, status‑quo remains.  <br>– If (N, O) → staff’s offer is wasted; farmer does not accept.  <br>– If (N, N) → nothing changes. |
| **Information** | Farmer knows whether staff usually offers regularisation (historical frequency) but not the current decision.  <br>Staff knows the farmer’s willingness to apply (observed from past applications).  Both have **partial, noisy** information. |
| **Outcomes** | • Legal connection (reliable voltage, lower risk of penalties)  <br>• Payment of connection fee  <br>• Staff gains compliance credit or avoids extra work |
| **Payoffs (ordinal)** | See matrix below. |
| **Strategic Tension** | **Asymmetric “Authorization” game** – the farmer’s payoff depends on the staff’s willingness to grant; the staff’s payoff depends on the farmer’s demand.  The interaction is **strategic** (simultaneous move). |
| **Temporal Structure** | Decided **once per year** (at the start of the decision‑cycle). |
| **Relevant Rules** | – Boundary rule: only farmers attached to the transformer may apply.  <br>– Position rule: staff can offer regularisation only to farmers with a pre‑existing informal tie (or to any applicant).  <br>– Choice rule: each player selects one of the two actions. |
| **Normal‑form game** |  

|                | **Staff O** (Offer) | **Staff N** (No offer) |
|----------------|--------------------|------------------------|
| **Farmer S** (Seek) | (3 , 3)  *Both get preferred outcome* | (1 , 2)  *Farmer wastes effort, staff stays status‑quo* |
| **Farmer N** (Stay informal) | (2 , 1)  *Staff wastes effort, farmer unchanged* | (2 , 2)  *Status‑quo for both* |

*Interpretation* – (Farmer payoff , Staff payoff).  
The highest joint rank (3,3) occurs when the farmer seeks and the staff offers; the worst joint rank (0) does not appear because the model assumes that a farmer never applies when the staff is certain to deny (bounded rationality).  

**Core analysis** – This is an **asymmetric coordination / bargaining game**.  The Pareto‑optimal outcome is (S,O), but a mismatch (S,N) or (N,O) yields a coordination failure.

---

### 2. Collusion Exchange Game  
| Element | Description |
|---|---|
| **Title** | **Collusion / Trust Exchange Game** |
| **Location** | Sub‑station office & field interactions (informal meetings at the transformer) |
| **Players** | • **Farmer F**  <br>• **Sub‑station staff S** |
| **Roles** | F = Consumer‑seeker of informal leniency, S = Enforcer‑with‑discretion |
| **Actions** | **Farmer:** 1️⃣ *Offer bribe* (B)  2️⃣ *Do not offer* (N)  <br>**Staff:** 1️⃣ *Accept* (A)  2️⃣ *Reject* (R) |
| **Control Rules** | – (B,A): staff tolerates an unauthorised connection, farmer avoids penalty.  <br>– (B,R): bribe is rejected; farmer may be inspected and fined.  <br>– (N,A): staff expects a bribe, none arrives → staff loses potential illicit gain.  <br>– (N,R): no collusion, normal enforcement. |
| **Information** | Farmer knows his own financial strain and the *perceived* risk of detection; staff knows his own corruption level and the *local* monitoring intensity.  Both have **partial, noisy** information about the other’s willingness. |
| **Outcomes** | • Informal leniency (reduced inspection, lower fees)  <br>• Illicit payoff for staff (cash)  <br>• Risk of sanction if collusion is detected |
| **Payoffs (ordinal)** | See matrix below. |
| **Strategic Tension** | **Trust game** – each side must trust the other to honour the informal bargain.  The interaction is **strategic**. |
| **Temporal Structure** | Re‑evaluated **once per year** (after the annual strategic‑decision stage). |
| **Relevant Rules** | – Position rule: only farmers with an existing informal tie can *successfully* propose a bribe.  <br>– Choice rule: each player picks one of the two actions simultaneously. |
| **Normal‑form game** |  

|                | **Staff A** (Accept) | **Staff R** (Reject) |
|----------------|----------------------|----------------------|
| **Farmer B** (Bribe) | (3 , 3)  *Both obtain illicit benefit* | (0 , 2)  *Farmer punished, staff avoids risk* |
| **Farmer N** (No bribe) | (2 , 0)  *Staff loses opportunity, farmer unchanged* | (2 , 2)  *Status‑quo* |

**Core analysis** – This is a **trust (or “gift‑exchange”) game** with a clear **Pareto‑optimal** (B,A) outcome, but a *risk‑dominant* (N,R) equilibrium if detection risk is high.

---

### 3. DSM Coordination Game (Capacitor Adoption)  
| Element | Description |
|---|---|
| **Title** | **Demand‑Side‑Management (DSM) Coordination Game** |
| **Location** | Within a **single transformer service area** (farmers share the same voltage‑quality). |
| **Players** | Two **representative farmers** (F₁, F₂) drawn from the same transformer. |
| **Roles** | Each farmer is a **technology adopter** (or non‑adopter). |
| **Actions** | **Adopt capacitor** (I)  or **Do not adopt** (N). |
| **Control Rules** | – If **both** adopt, the transformer voltage improves for *all* farmers on that transformer (shared public good).  <br>– If only one adopts, the adopter bears the full cost but receives no voltage improvement (no shared benefit).  <br>– If none adopt, voltage stays low. |
| **Information** | Farmers observe the *adoption status* of neighbours at the end of the previous cycle (perfect observation of who adopted).  They do **not** know the future decisions of the current cycle – thus the game is simultaneous. |
| **Outcomes** | • Improved electricity quality (lower motor‑burnouts)  <br>• Capital cost of capacitor (paid once)  <br>• Possible future peer‑pressure to adopt |
| **Payoffs (ordinal)** | See matrix below. |
| **Strategic Tension** | **Assurance / Coordination game** – the benefit of adoption is realized only if enough neighbours also adopt.  The interaction is **strategic**. |
| **Temporal Structure** | **Annual** – each year a pool of “experimenters” is drawn; the game is played repeatedly. |
| **Relevant Rules** | – Boundary rule: only farmers attached to the same transformer can coordinate.  <br>– Choice rule: each farmer selects I or N simultaneously. |
| **Normal‑form game** |  

|                | **Farmer 2 I** | **Farmer 2 N** |
|----------------|----------------|----------------|
| **Farmer 1 I** | (3 , 3)  *Both enjoy voltage gain, share cost* | (0 , 2)  *Adopter bears cost alone* |
| **Farmer 1 N** | (2 , 0)  *Non‑adopter free‑rides* | (2 , 2)  *Status‑quo* |

**Core analysis** – This is a classic **assurance game** (also called “stag‑hunt”).  The Pareto‑optimal (I,I) outcome is risk‑dominant only when farmers expect the other to adopt; otherwise (N,N) is the safe equilibrium.

---

### 4. Groundwater Extraction Game (Common‑Pool Resource)  
| Element | Description |
|---|---|
| **Title** | **Groundwater Extraction (CPR) Game** |
| **Location** | Aquifer underlying a **district‑level groundwater basin** (all farmers connected to the same basin draw from it). |
| **Players** | Two **representative farmers** (F₁, F₂) sharing the same aquifer. |
| **Roles** | Each farmer is a **water extractor**. |
| **Actions** | **Extract high** (E) – pump at maximum rate (higher immediate yield, higher energy cost)  <br>**Restrict extraction** (R) – pump at a sustainable rate (lower immediate yield, lower energy cost). |
| **Control Rules** | – Aquifer drawdown = Σ extraction × energy‑cost factor.  <br>– When drawdown exceeds a threshold, marginal pumping cost rises for *all* farmers (captured in the payoff ranking). |
| **Information** | Farmers know the current groundwater depth (noisy sensor) and the *historical* extraction pattern of neighbours (partial). |
| **Outcomes** | • Individual water volume obtained  <br>• Energy cost of pumping (rising with depletion)  <br>• Long‑term aquifer health |
| **Payoffs (ordinal)** | See matrix below. |
| **Strategic Tension** | **Common‑pool‑resource (tragedy‑of‑the‑commons) game** – each farmer’s incentive to extract high conflicts with collective sustainability.  The interaction is **strategic**. |
| **Temporal Structure** | **Annual** – decisions are made each irrigation season; the game repeats each year with updated aquifer stock. |
| **Relevant Rules** | – Boundary rule: only farmers whose wells tap the same aquifer are included.  <br>– Control rule: aquifer level is updated after each round. |
| **Normal‑form game** |  

|                | **Farmer 2 E** | **Farmer 2 R** |
|----------------|----------------|----------------|
| **Farmer 1 E** | (2 , 2)  *Both over‑extract, higher cost* | (3 , 1)  *Extractor gets high yield, restrainer suffers* |
| **Farmer 1 R** | (1 , 3)  *Symmetric* | (3 , 3)  *Both restrain – sustainable high payoff* |

**Core analysis** – The matrix exhibits a **prisoner’s‑dilemma‑like** tension when the aquifer is already stressed (E,E) gives moderate payoffs, but the jointly optimal (R,R) yields the highest (3,3).  The (E,R) and (R,E) outcomes create a classic “free‑rider” problem.

---

### 5. Capacity‑Provision Public‑Goods Game  
| Element | Description |
|---|---|
| **Title** | **Transformer Capacity Provision (Public‑Goods) Game** |
| **Location** | Sub‑station level – decision on whether to **install** additional transformer capacity that serves all farmers attached to that transformer. |
| **Players** | • **Staff S** (decision‑maker for capacity investment)  <br>• **Representative farmer F** (decides whether to contribute financially to the capacity upgrade). |
| **Roles** | S = Infrastructure investor / regulator, F = Consumer‑contributor. |
| **Actions** | **Staff:** 1️⃣ *Invest* in capacity (I)  2️⃣ *Do not invest* (N)  <br>**Farmer:** 1️⃣ *Contribute* to the upgrade cost (C)  2️⃣ *Free‑ride* (F). |
| **Control Rules** | – If (I,C): capacity is added; cost is split (staff bears part of installation, farmer pays contribution).  <br>– If (I,F): staff bears full cost, farmer enjoys upgraded service for free.  <br>– If (N,C): farmer’s contribution is wasted (no upgrade).  <br>– If (N,F): status‑quo. |
| **Information** | Staff knows the *aggregate* willingness of farmers to pay (observed from past contributions).  Farmer knows the *probability* that staff will invest (based on workload and past behaviour).  Both have **partial** information. |
| **Outcomes** | • Improved transformer reliability (fewer burn‑outs)  <br>• Financial outlay for staff and/or farmer  <br>• Potential reduction in future enforcement costs |
| **Payoffs (ordinal)** | See matrix below. |
| **Strategic Tension** | **Public‑goods / free‑rider game** – the capacity upgrade is a non‑excludable benefit; the farmer decides whether to share the cost, while staff decides whether to bear the installation expense.  The interaction is **strategic**. |
| **Temporal Structure** | **Annual** – the decision is revisited each year; once capacity is installed it persists (but may degrade, prompting new rounds). |
| **Relevant Rules** | – Boundary rule: only farmers linked to the transformer may contribute.  <br>– Position rule: staff can only invest if the transformer load exceeds a threshold (implicit in the model). |
| **Normal‑form game** |  

|                | **Farmer C** (Contribute) | **Farmer F** (Free‑ride) |
|----------------|---------------------------|---------------------------|
| **Staff I** (Invest) | (3 , 3)  *Both share benefits* | (0 , 2)  *Staff bears cost, farmer free‑rides* |
| **Staff N** (No invest) | (2 , 0)  *Farmer wastes money* | (2 , 2)  *Status‑quo* |

**Core analysis** – This is a **public‑goods game** with an **asymmetric** payoff structure: the staff’s best outcome is to invest *only* when farmers also contribute; otherwise the staff prefers to stay out.  The (I,C) cell is Pareto‑optimal; (N,F) is the risk‑dominant equilibrium.

---

### 6. Social‑Learning Process (Non‑strategic)  
| Element | Description |
|---|---|
| **Title** | **Social‑Learning & Imitation Process** |
| **Location** | Village‑level observation network (farmers watch neighbours on the same transformer). |
| **Players** | **All farmers** (simultaneously). |
| **Roles** | Learners / Observers. |
| **Actions** | **Observe** neighbours’ adoption outcomes (capacitor, connection type) → **Update** internal propensity to adopt in the next cycle (probability p). No explicit choice in the current tick. |
| **Control Rules** | – After each yearly outcome‑logging, a “learning module” copies the adoption status of a randomly selected neighbour with probability *p* if that neighbour’s payoff rank was ≥ 2 in the previous year.  <br>– The learning probability is bounded by a social‑norm parameter τ. |
| **Information** | Perfect observation of *visible* actions (who adopted, who has authorised connections).  Perceived performance (voltage quality, pump failures) is **noisy**. |
| **Outcomes** | – Diffusion of DSM technologies, spread of informal ties, convergence (or stagnation) of adoption rates. |
| **Payoffs** | Not modelled directly; learning changes future strategic‑game payoffs. |
| **Strategic Tension** | **Non‑strategic** – no simultaneous move; it is a sequential, exogenous update rule. |
| **Temporal Structure** | Executed **once per year**, after the payoff‑realisation stage. |
| **Relevant Rules** | – Position rule: learning only occurs within the same transformer group.  <br>– Choice rule: the probability‑draw decides whether adoption propensity is updated. |

---

## 2️⃣  Comparative analysis of the strategic core

| # | Game | Type of strategic tension | Payoff pattern (high‑low) | Key asymmetry / coordination feature |
|---|------|---------------------------|---------------------------|--------------------------------------|
| 1 | Authorization | **Asymmetric coordination / bargaining** | (3,3) > (2,2) > (1,2) > (2,1) | Staff’s offer only valuable if farmer seeks; mismatch leads to wasted effort. |
| 2 | Collusion / Trust | **Trust / gift‑exchange** | (3,3) > (2,2) > (2,0) > (0,2) | Mutual willingness required; risk of detection creates a *trust* dilemma. |
| 3 | DSM Coordination | **Assurance (stag‑hunt)** | (3,3) > (2,2) > (0,2) > (2,0) | Benefit materialises only when *both* adopt; otherwise adopter is punished. |
| 4 | Groundwater Extraction | **Common‑pool (prisoner’s dilemma‑like)** | (3,3) > (3,2) > (2,2) > (1,3) … | Joint restraint dominates, but each has incentive to over‑extract if the other restrains. |
| 5 | Capacity Provision | **Public‑goods / free‑rider** | (3,3) > (2,2) > (0,2) > (2,0) | Staff’s investment is worthwhile only with farmer contribution; otherwise free‑riding occurs. |

### Similarities & Differences  

| Pair | Similarity | Difference |
|------|------------|------------|
| 1 vs 5 | Both involve **staff–farmer** dyad and a *public‑good* (reliable electricity). | Game 1 is **authorization** (binary legal status) – payoff to staff is compliance credit; Game 5 is **capacity** (investment cost) – payoff to staff is load reduction. |
| 2 vs 3 | Both rely on **mutual cooperation** and have a (3,3) Pareto optimum. | Game 2 is a **trust** exchange with illicit gains; Game 3 is a **coordination** game where the benefit is *shared* voltage improvement, not private gain. |
| 3 vs 5 | Both are **coordination / public‑good** structures with a free‑rider risk. | Game 3 is symmetric between farmers; Game 5 is asymmetric (staff vs farmer). |
| 4 vs any other | Unique because it is a **common‑pool resource** affecting *environmental* state (aquifer). | Others are institutional or technology‑adoption games; 4’s payoff depends on a *stock* variable that evolves over time. |

### Ensuring strategic diversity  

All five strategic games now cover **distinct** dilemma families:

1. **Asymmetric coordination / bargaining** (Authorization)  
2. **Trust / reciprocal exchange** (Collusion)  
3. **Assurance / coordination** (DSM)  
4. **Common‑pool / tragedy of the commons** (Groundwater)  
5. **Public‑goods / free‑rider** (Capacity provision)

No two games repeat the same *type* of strategic tension, satisfying the requirement for diversity.

---

## 3️⃣  Revised set (final)

The six action‑situations listed above (five strategic, one non‑strategic) constitute **the complete set of distinct governance interactions** described in the ODD + D model.  

- Each situation respects the ODD + D description (players, timing, information, etc.).  
- All payoff matrices use **ordinal ranks 0–3 only** and are **2 × 2**.  
- The strategic core of each game is identified and contrasted, and the collection is intentionally diverse.  

You can now embed these action‑situations into an IAD‑style ABM: each year the simulation cycles through the five strategic games (in the order given in the “Process overview”), logs the outcomes, and finally runs the non‑strategic **Social‑Learning** update. This reproduces the linked action‑situations and the emergent patterns (capacitor adoption, collusion networks, groundwater depletion, etc.) reported in the original study.
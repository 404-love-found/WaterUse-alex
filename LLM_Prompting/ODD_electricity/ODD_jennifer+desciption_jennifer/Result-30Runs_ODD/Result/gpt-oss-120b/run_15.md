# Run 15 — openai/gpt-oss-120b

## Electricity‑Irrigation Governance – Action‑Situation Catalogue  
*(IAD‑framed extraction from the ODD + D description.  All strategic games are shown as 2 × 2 normal‑form games with **ordinal** pay‑offs 0 – 3, where 3 = most‑preferred, 0 = least‑preferred.)*  

---

### 1. DSM (Demand‑Side‑Management) Coordination Game  
**Title** Capacitor / DSM Adoption Coordination  
**Location** Transformer‑service area (village‑level) – farmers observe the same voltage‑quality signal.  
**Players** Farmer A, Farmer B (representative neighbours on the same transformer).  
**Roles** Electricity consumer (each).  
**Actions** - **Invest (I)** – purchase & install a capacitor / DSM kit (cost incurred).  
     - **Not‑Invest (N)** – keep the status‑quo.  
**Control Rules** If ≥ k farmers on the transformer invest in the same month, the transformer voltage improves for **all** (shared public‑good).  If the threshold is not met, the investor bears the full cost and receives no voltage benefit.  
**Information** Each farmer knows:  
* own budget,  
* the recent adoption count on the transformer (noisy – only the **last month’s** count is observed),  
* the cost of the kit.  
Information is **partial**; the exact future adoption of the neighbour is unknown.  
**Outcomes** - Improved voltage → higher pump efficiency, lower electricity bill.  
- No improvement → only cost of kit is incurred.  
**Payoffs (ordinal)**  

|                | Farmer B I | Farmer B N |
|----------------|------------|------------|
| **Farmer A I** | (3, 3)     | (1, 2)     |
| **Farmer A N** | (2, 1)     | (2, 2)     |

*Explanation* – (I,I) gives the **coordination/assurance** payoff (both enjoy the public‑good).  (I,N) gives the investor a low rank (1) because he pays but sees no benefit, while the non‑investor free‑rides (2).  (N,N) is the status‑quo (moderate, 2).  

**Strategic Tension** *Assurance / Coordination game* – each farmer wants the other to invest before he does.  
**Temporal Structure** Repeated **annually** (once per year a new adoption pool is formed; the game is played each month until the threshold is reached).  
**Relevant Rules** Boundary: all farmers attached to the same transformer belong to the same “action situation”.  Choice rule: invest only if expected neighbours’ adoption ≥ k.  Control rule: shared voltage improvement only after threshold.  

---

### 2. Authorization Game  
**Title** Formal Connection Authorization  
**Location** Sub‑station / transformer office (staff‑farmer interaction point).  
**Players** Farmer F, Sub‑station Staff S.  
**Roles** Farmer = electricity consumer; Staff = service provider / gate‑keeper.  
**Actions** - **Farmer:**  *Seek formal connection (S)* or *Stay informal (I)*.  
     - **Staff:**  *Authorize (A)* or *Deny/Ignore (D)*.  
**Control Rules** Authorization requires staff to allocate a line‑capacity slot and record the connection in the utility database.  Denial leaves the farmer with an informal (often illegal) link.  
**Information** Farmer knows his own budget, the expected tariff, and the local risk of detection (stochastic).  Staff knows the current transformer load, the quota of authorized slots, and the probability of external audit.  Information is **asymmetric** – staff has more knowledge about capacity constraints.  
**Outcomes** - Authorized connection → reliable supply, legal tariff, possible subsidy.  
- Informal connection → cheaper short‑term cost but risk of disconnection/fine.  
**Payoffs (ordinal)**  

|                | Staff A | Staff D |
|----------------|---------|---------|
| **Farmer S**   | (3, 2)  | (0, 3)  |
| **Farmer I**   | (1, 1)  | (2, 2)  |

*Explanation* – (S,A) gives the farmer the best outcome (3) and staff a moderate gain (2) (legal revenue).  (S,D) leaves the farmer with the worst outcome (0) while staff saves effort (3).  (I,A) is a wasted authorization (both get low pay‑offs).  (I,D) is the status‑quo informal link (2,2).  

**Strategic Tension** *Authorization / asymmetric conflict* – farmer wants staff to authorize; staff balances revenue vs workload and risk of overload.  
**Temporal Structure** One‑shot **annual** decision (made once per year for the whole simulation year).  
**Relevant Rules** Boundary: only farmers attached to a given transformer and the two staff assigned to that transformer.  Position rule: staff can allocate at most a fixed number of new slots per year.  

---

### 3. Collusion Exchange Game  
**Title** Informal Collusion / Favor Exchange  
**Location** Transformer service area – informal meetings, “field office”.  
**Players** Farmer F, Sub‑station Staff S (the staff member tied to the farmer).  
**Roles** Farmer = consumer seeking cheap electricity; Staff = discretionary official.  
**Actions** - **Collude (C)** – farmer offers an informal payment/reciprocal favor; staff reciprocates with reduced monitoring or extra credit.  
     - **Not‑Collude (N)** – stick to formal rules.  
**Control Rules** If both collude, the informal arrangement is enacted; if only one attempts collusion, the attempt is aborted and the initiator may face a detection penalty (stochastic).  
**Information** Both know the **local collusion density** (observed from neighbours) and the **risk of detection** (exogenous stochastic monitoring intensity).  Perception of risk is **noisy**.  
**Outcomes** - Successful collusion → lower electricity bill for farmer, extra illicit income for staff.  
- Failed collusion → possible fine for farmer, reputational loss for staff.  
**Payoffs (ordinal)**  

|                | Staff C | Staff N |
|----------------|----------|----------|
| **Farmer C**   | (3, 3)   | (0, 1)   |
| **Farmer N**   | (1, 0)   | (2, 2)   |

*Explanation* – Mutual collusion is the best for both (3,3).  If the farmer tries to collude but staff refuses, the farmer risks detection (0) while staff saves effort (1).  If staff offers a bribe but farmer declines, staff loses the illicit gain (0) and farmer gets a modest status‑quo (1).  Both refuse → normal operation (2,2).  

**Strategic Tension** *Trust / Prisoner‑Dilemma‑type* – each side would like the other to collude, but unilateral collusion is risky.  
**Temporal Structure** Repeated **monthly** (the same pair can attempt collusion each month).  
**Relevant Rules** Boundary: only farmer‑staff pairs with an existing social tie may enter this situation.  Choice rule: willingness to collude declines with workload (staff) and financial strain (farmer).  

---

### 4. Groundwater Extraction (CPR) Game  
**Title** Common‑Pool Groundwater Extraction  
**Location** Aquifer basin underlying a set of neighbouring farms (spatially shared).  
**Players** Farmer A, Farmer B (any two users of the same aquifer).  
**Roles** Both are **resource users** (extractors).  
**Actions** - **High extraction (H)** – pump at full rate (max yield, high energy cost).  
     - **Restrict (R)** – voluntarily limit extraction (lower yield, saves water).  
**Control Rules** Groundwater level falls proportionally to total extraction each month; as the water table drops, the **energy cost per unit** rises (affects future pay‑offs).  No enforcement; the game is purely self‑organized.  
**Information** Each farmer knows his own well depth, recent pump performance, and the **average extraction** of neighbours (estimated from visible water tables).  Information is **imperfect** (no exact extraction data).  
**Outcomes** - Sustainable extraction → stable water table, moderate long‑term profits.  
- Over‑extraction → rapid draw‑down, rising pump costs, possible pump failure.  
**Payoffs (ordinal)**  

|                | Farmer B H | Farmer B R |
|----------------|------------|------------|
| **Farmer A H** | (1, 1)     | (3, 0)     |
| **Farmer A R** | (0, 3)     | (2, 2)     |

*Explanation* – (H,H) gives both a low rank (1) because the aquifer is over‑used and costs rise.  (H,R) lets the high‑extractor reap the short‑term gain (3) while the restrictor suffers (0).  (R,R) yields a moderate sustainable outcome for both (2).  

**Strategic Tension** *Common‑Pool Resource (tragedy of the commons) game* – each farmer prefers the other to restrain while extracting heavily.  
**Temporal Structure** Repeated **monthly** (extraction decisions are made each month).  
**Relevant Rules** Boundary: all farms drawing from the same aquifer belong to the same CPR action situation.  Position rule: extraction cost rises with cumulative draw‑down (control rule).  

---

### 5. Enforcement (Inspection) Game – **Replaced the original “Capacity‑Provision” interaction** to guarantee strategic diversity  
**Title** Staff Inspection vs. Farmer Compliance  
**Location** Sub‑station monitoring office / field patrol area.  
**Players** Sub‑station Staff S, Farmer F.  
**Roles** Staff = enforcer (inspector); Farmer = regulated user.  
**Actions** - **Staff:** *Inspect (I)* or *Do‑nothing (N)*.  
     - **Farmer:** *Pay fee / comply (P)* or *Evade (E)* (continue informal connection).  
**Control Rules** If staff inspects and farmer evades, the farmer is caught with probability p (>0) and fined; if inspection occurs and farmer complies, staff receives a compliance reward.  If staff does not inspect, the farmer’s evasion goes undetected.  
**Information** Staff knows the current audit probability (exogenous) and the number of pending informal connections.  Farmer knows the expected fine size and the likelihood of inspection (noisy).  
**Outcomes** - Successful inspection + compliance → legal revenue, staff reputation boost.  
- Inspection + evasion → fine imposed, staff gain enforcement credit, farmer suffers penalty.  
- No inspection → status‑quo (farmer saves money, staff saves effort).  
**Payoffs (ordinal)**  

|                | Farmer P | Farmer E |
|----------------|----------|----------|
| **Staff I**    | (3, 2)   | (0, 3)   |
| **Staff N**    | (1, 2)   | (2, 3)   |

*Explanation* – (I,P): staff gets a moderate reward for a smooth inspection (3), farmer pays the fee (2).  (I,E): staff captures the evader → highest staff payoff (3), farmer receives the worst outcome (0).  (N,P): staff loses the chance to enforce (1) while farmer still pays (2).  (N,E): both avoid costs – farmer gets the best personal outcome (3), staff gets a low payoff (2) because no enforcement credit.  

**Strategic Tension** *Asymmetric conflict / enforcement dilemma* – staff must weigh inspection costs against deterrence; farmer decides whether the risk of being caught outweighs the saving from evasion.  
**Temporal Structure** Repeated **monthly** (inspection opportunities arise each month).  
**Relevant Rules** Boundary: all farmers attached to a given transformer are subject to the two staff assigned there.  Position rule: staff can inspect at most **k** farms per month (capacity constraint).  

---

### 6. Social‑Learning (Imitation) Process – **Non‑strategic**  
**Title** Neighbourhood Observation & Imitation  
**Location** Transformer service area (farmers can see each other’s equipment).  
**Players** All farmers on a transformer (no explicit strategic opponent).  
**Roles** Observers / potential adopters.  
**Actions** - **Observe** neighbours’ adoption outcomes (capacitor success/failure).  
- **Imitate** with probability *π* if a threshold of successful adopters is observed; otherwise **remain** with current technology.  
**Control Rules** A “learning trigger” opens when the cumulative number of successful adopters on the transformer exceeds a preset threshold *τ*.  Once opened, each non‑adopter draws a Bernoulli(π) to decide whether to adopt in the next cycle.  
**Information** Farmers perfectly observe **visible** adoption (yes/no) but **misinterpret** the underlying performance (noisy perception of voltage improvement).  
**Outcomes** - Increased adoption rates after successful “pilot” phase.  
- Possible diffusion of a technology that later proves ineffective (if early adopters mis‑perceive benefits).  
**Payoffs** Not modelled as explicit utility; the process changes the **state variables** (adoption count, voltage level) that feed into other strategic games.  
**Strategic Tension** None – the process is **sequential, non‑strategic** (agents react to observed outcomes, no simultaneous move).  
**Temporal Structure** Annual – the learning trigger is evaluated once per year; imitation decisions are made at the start of the next irrigation season.  
**Relevant Rules** Boundary: all farmers sharing the same transformer.  Choice rule: imitation only if the trigger is active.  Control rule: adoption count updates the trigger condition.  

---

### 7. Experimental Adoption Pool (Prospective “Experimenter” Selection) – **Non‑strategic**  
**Title** Annual Experimenter Pool Formation  
**Location** Transformer‑level planning office (model‑level).  
**Players** Model‑level scheduler (no agent), draws a random subset of farmers.  
**Roles** Experimenter selector (exogenous).  
**Actions** - **Select** a small random set of farmers as “experimenters” (regardless of neighbours’ outcomes).  
- **Open** the wider imitation pool only if the current year’s adoption count on the transformer jumps by a threshold *δ* within a single month.  
**Control Rules** The experimenter pool is **exogenously** drawn each year (stochastic).  The wider pool is **endogenously** triggered by a rapid adoption surge.  
**Information** No agents involved; the rule uses the **observed** adoption jump.  
**Outcomes** - Guarantees a minimal flow of new technology trials each year.  
- Allows “critical mass” dynamics when a sudden cluster of adopters appears.  
**Payoffs** Not applicable (process influences state variables).  
**Strategic Tension** None – purely procedural.  
**Temporal Structure** Annual (once per simulated year).  
**Relevant Rules** Boundary: all farmers attached to the transformer; Position rule: experimenters are drawn uniformly at random; Control rule: threshold‑based opening of the imitation pool.  

---

## Strategic Core Analyses  

| # | Game | Core Type | Why |
|---|------|-----------|-----|
| 1 | DSM Coordination | **Assurance / Coordination** (multiple‑equilibrium) | Payoffs are highest only if **both** invest; otherwise the investor is penalised. |
| 2 | Authorization | **Asymmetric Conflict** (principal‑agent) | Staff controls a scarce resource (slots) while farmer seeks access; interests diverge. |
| 3 | Collusion Exchange | **Prisoner‑Dilemma / Trust** | Mutual collusion is best, but unilateral collusion is risky; each side fears being the only one to cooperate. |
| 4 | Groundwater CPR | **Common‑Pool Resource (Tragedy of the Commons)** | Each farmer prefers the other to restrain while extracting heavily. |
| 5 | Enforcement (Inspection) | **Asymmetric Enforcement Dilemma** | Staff must decide whether to incur inspection cost; farmer decides whether to risk evasion. |
| 6 | Social‑Learning | **Non‑strategic sequential diffusion** | No simultaneous move; adoption follows observed outcomes. |
| 7 | Experimenter Pool | **Non‑strategic procedural trigger** | Exogenous stochastic selection; no strategic interaction. |

### Comparison & Distinctiveness  

| Game | Players | Decision Type | Payoff Symmetry | Institutional Feature |
|------|---------|---------------|-----------------|-----------------------|
| 1 | Farmer‑Farmer (peers) | Simultaneous, coordination | Symmetric (both get same rank) | Threshold‑based public‑good (voltage) |
| 2 | Farmer‑Staff | Simultaneous, asymmetric | Asymmetric (farmer’s max = 3, staff’s max = 3 in different cells) | Formal authorization quota |
| 3 | Farmer‑Staff | Simultaneous, trust | Symmetric (3,3) but risk of unilateral loss | Informal collusion network |
| 4 | Farmer‑Farmer | Simultaneous, CPR | Asymmetric (high extractor gets 3, restrainer 0) | Shared groundwater basin |
| 5 | Staff‑Farmer | Simultaneous, enforcement | Asymmetric (inspection gives staff 3, farmer 0) | Stochastic monitoring intensity |
| 6 | Many farmers | Sequential observation | No payoff matrix | Social‑learning trigger |
| 7 | Model scheduler | Procedural | – | Random experimenter draw |

All five strategic games involve **different institutional mechanisms** (public‑good provision, authorization, informal exchange, CPR, enforcement) and **different payoff structures** (coordination, asymmetric conflict, PD‑type, CPR, enforcement).  

---

## Revision for Strategic Diversity  

The original ODD + D description contained a “Capacity‑Provision” sub‑model where staff invested transformer capacity for tied farmers. While important, its payoff structure closely resembled the **Authorization** game (both involved staff deciding to allocate capacity and farmer deciding to request it). To avoid redundancy and to broaden the strategic spectrum, we **replaced** that interaction with the **Enforcement (Inspection) Game** (Action Situation 5).  

*Rationale*:  

* The new game introduces a **pure enforcement dilemma** that is not captured by any of the other four strategic games.  
* It adds a **different asymmetry**: staff bears a monitoring cost, farmer bears a risk of penalty.  
* It aligns with the ODD + D description of “transformer burnout checks and enforcement run” (monthly), which was previously only a background process.  

The revised game therefore **conforms** to the ODD + D protocol (players, timing, control rules) and enhances the model’s strategic diversity.

---

## Complete Action‑Situation Set  

| # | Title | Strategic? | Type (Game) |
|---|-------|------------|-------------|
| 1 | DSM Coordination (Capacitor Adoption) | Yes | Assurance / Coordination |
| 2 | Authorization (Formal Connection) | Yes | Asymmetric Conflict |
| 3 | Collusion Exchange (Informal Favor) | Yes | Prisoner‑Dilemma / Trust |
| 4 | Groundwater Extraction (CPR) | Yes | Common‑Pool Resource |
| 5 | Enforcement (Inspection vs. Compliance) | Yes | Asymmetric Enforcement Dilemma |
| 6 | Social‑Learning (Imitation) | No | Sequential diffusion |
| 7 | Experimenter Pool Formation | No | Procedural trigger |

These seven action situations capture **all distinct governance interactions** described in the ODD + D model, each with its own IAD‑framed specification, payoff structure (where strategic), and temporal schedule.
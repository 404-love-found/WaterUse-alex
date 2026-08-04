# Run 26 — openai/gpt-oss-120b

**Electricity‑Irrigation Governance – Action‑Situation Catalogue (IAD + D)**  

Below are all distinct governance interactions that emerge from the ODD + D description.  
Each entry follows the IAD template (Title, Location, Players, …, Temporal Structure, Relevant Rules).  
Strategic situations are expressed as a **2 × 2 normal‑form game** with **ordinal pay‑offs** (0 = least‑preferred, 3 = most‑preferred).  
Non‑strategic processes are described as sequential “observation → learning → imitation” steps.

---

## 1. DSM‑Coordination (Capacitor Adoption) Game  

| Element | Description |
|---|---|
| **Title** | DSM‑Coordination (Capacitor) Game |
| **Location** | Transformer service area (farmers sharing the same low‑voltage transformer) |
| **Players** | Two neighboring **farmers** (A and B) that belong to the same transformer cluster |
| **Roles** | Electricity consumer / technology adopter |
| **Actions** | **Invest** in a capacitor (I)  or  **Do not invest** (N) |
| **Control Rules** | The benefit of a capacitor (improved voltage, lower pump‑failure risk) materialises **only if a critical mass of farmers on the same transformer invests in the same cycle**. If only one farmer invests, the private cost is incurred while the shared benefit is negligible. |
| **Information** | Each farmer observes (noisy) past voltage stability and visible neighbour adoption in the previous year; they do **not** know the partner’s current choice. |
| **Outcomes** | (i) Shared voltage reliability, (ii) individual adoption cost, (iii) future learning signal. |
| **Payoffs** (ordinal 0‑3) | See matrix below. |
| **Strategic Tension** | **Assurance/Coordination game** – a farmer’s payoff rises sharply when the neighbour also invests; unilateral investment is unattractive. |
| **Temporal Structure** | Repeated **annually** (same pair may be re‑matched each year). |
| **Relevant Rules** | *Boundary*: only farmers attached to the same transformer are paired. <br>*Choice*: binary invest / not‑invest. <br>*Control*: payoff depends on joint action (coordination). |

### Pay‑off matrix  

|                | **B : I** | **B : N** |
|----------------|-----------|-----------|
| **A : I** | (3, 3) – both enjoy reliable voltage and share the benefit. | (1, 2) – A bears cost, B free‑rides on the (still weak) grid improvement. |
| **A : N** | (2, 1) – B bears cost, A free‑rides. | (0, 0) – no investment, voltage remains poor. |

*Core:* **Coordination (assurance) game** – two pure‑strategy Nash equilibria (I,I) and (N,N); (I,I) is Pareto‑optimal but risk‑dominant only if trust/learning is high.  

---

## 2. Authorization Game (Formal Connection)  

| Element | Description |
|---|---|
| **Title** | Authorization Game |
| **Location** | Sub‑station office (record‑keeping desk) serving a transformer cluster |
| **Players** | **Farmer** (seeking a formal electricity connection) and **Sub‑station staff** (who can grant or deny authorization) |
| **Roles** | Farmer = consumer/connection‑seeker; Staff = enforcer/allocator |
| **Actions** | *Farmer*: **Pay fee** for formal connection (P) or **Seek informal access** (I). <br>*Staff*: **Authorize** (A) or **Deny/ignore** (N). |
| **Control Rules** | Authorization converts an informal load into a recorded, billable load and unlocks staff‑provided capacity upgrades. Denial leaves the farmer on the informal network. |
| **Information** | Farmer knows the current enforcement intensity (probability of detection) but not the staff’s willingness to authorize. Staff knows the farmer’s budget and the transformer’s capacity gap, but not the farmer’s hidden informal network. |
| **Outcomes** | (i) Access type (formal vs informal), (ii) fee payment, (iii) staff workload (record‑keeping, maintenance). |
| **Payoffs** | Ordinal matrix below. |
| **Strategic Tension** | **Asymmetric Authorization game** – farmer’s payoff hinges on staff’s decision; staff balances formal compliance benefits against effort‑costs and informal gains. |
| **Temporal Structure** | One‑shot **annual** decision (re‑evaluated each irrigation year). |
| **Relevant Rules** | *Boundary*: only farmers attached to the transformer are eligible. <br>*Choice*: binary fee / informal; staff binary authorize / not. <br>*Control*: outcomes determined by the pair’s joint move. |

### Pay‑off matrix  

|                | **Staff : A** | **Staff : N** |
|----------------|---------------|---------------|
| **Farmer : P** | (3, 2) – farmer obtains reliable electricity; staff gains formal revenue. | (0, 1) – farmer wastes fee; staff avoids effort. |
| **Farmer : I** | (1, 0) – farmer gets informal access but staff must monitor; staff bears risk. | (2, 3) – farmer saves cost; staff enjoys informal benefit (e.g., kick‑backs). |

*Core:* **Asymmetric Prisoner’s‑Dilemma‑type** – (P,A) is socially efficient but each side has an incentive to deviate when the other’s move is uncertain.  

---

## 3. Collusion‑Exchange Game  

| Element | Description |
|---|---|
| **Title** | Collusion‑Exchange Game |
| **Location** | Informal meeting spot (village “chowk”) and sub‑station liaison desk |
| **Players** | **Farmer** and **Sub‑station staff** (the same dyad that may already have a social tie) |
| **Roles** | Farmer = offerer of informal favour (e.g., delayed payment, labour); Staff = receiver of favours (e.g., tolerance of unauthorised load) |
| **Actions** | *Farmer*: **Offer** informal favour (O) or **Not offer** (N). <br>*Staff*: **Collude** (C) or **Stay clean** (NC). |
| **Control Rules** | Collusion yields a *mutual* payoff only when both sides act; a unilateral offer is costly for the farmer, while unilateral collusion is wasted effort for staff. |
| **Information** | Both know the local **risk of detection** (exogenous monitoring intensity) but not the partner’s current willingness. |
| **Outcomes** | (i) Informal electricity tolerance, (ii) hidden cash‑flow, (iii) reputational risk. |
| **Payoffs** | Ordinal matrix below. |
| **Strategic Tension** | **Trust/Reciprocity game** – mutual cooperation yields the highest payoff; unilateral cooperation is punished. |
| **Temporal Structure** | Repeated **annual** (the same pair may renegotiate each year). |
| **Relevant Rules** | *Boundary*: only farmers with an existing social tie to a staff member can play. <br>*Choice*: binary offer / collude. <br>*Control*: payoff conditional on joint action. |

### Pay‑off matrix  

|                | **Staff : C** | **Staff : NC** |
|----------------|---------------|----------------|
| **Farmer : O** | (3, 3) – mutual benefit (e.g., cheap electricity, staff kick‑back). | (0, 1) – farmer loses favour, staff bears monitoring cost. |
| **Farmer : N** | (2, 0) – staff colludes without farmer’s input (wasted). | (1, 1) – status‑quo, low but safe payoff. |

*Core:* **Trust game** – (O,C) is Pareto‑optimal; (N,NC) is the safe equilibrium; asymmetry in unilateral moves creates a coordination problem.  

---

## 4. Groundwater Extraction (Common‑Pool Resource) Game  

| Element | Description |
|---|---|
| **Title** | Groundwater Extraction Game |
| **Location** | Local aquifer basin serving all farms attached to a transformer |
| **Players** | Two **farmers** (A and B) sharing the same groundwater source |
| **Roles** | Water extractor / irrigator |
| **Actions** | **High extraction** (H) or **Low extraction** (L) for the current irrigation season |
| **Control Rules** | The aquifer’s depth **increases** with total extraction; higher depth raises pumping‑energy cost and reduces future yields. |
| **Information** | Each farmer observes the current water table (noisy) and the neighbour’s past extraction level (via irrigation timing), but not the exact current extraction choice. |
| **Outcomes** | (i) Immediate water volume, (ii) future pumping cost, (iii) risk of aquifer collapse. |
| **Payoffs** | Ordinal matrix below. |
| **Strategic Tension** | **Common‑Pool Resource (tragedy‑of‑the‑commons) game** – unilateral high extraction yields short‑term gain, but mutual high extraction collapses the resource. |
| **Temporal Structure** | Repeated **annual** (the game is re‑played each irrigation cycle). |
| **Relevant Rules** | *Boundary*: all farmers drawing from the same aquifer are linked. <br>*Choice*: binary extraction level. <br>*Control*: payoff depends on joint extraction. |

### Pay‑off matrix  

|                | **B : H** | **B : L** |
|----------------|-----------|-----------|
| **A : H** | (0, 0) – both over‑pump → severe depletion, lowest payoff. | (2, 1) – A gains water now, B suffers slightly lower water. |
| **A : L** | (1, 2) – B gains, A suffers a modest loss. | (3, 3) – sustainable extraction, highest joint payoff. |

*Core:* **Chicken / Stag‑Hunt hybrid** – (L,L) is Pareto‑optimal; (H,H) is the worst outcome; mixed strategies give asymmetric short‑term benefits.  

---

## 5. Enforcement‑vs‑Compliance Game  

| Element | Description |
|---|---|
| **Title** | Enforcement‑vs‑Compliance Game |
| **Location** | Sub‑station control room (decision‑making) and field (farmer’s irrigation site) |
| **Players** | **Sub‑station staff** (Enforcer) and **Farmer** (Consumer) |
| **Roles** | Staff = regulatory enforcer / capacity investor; Farmer = electricity user |
| **Actions** | *Staff*: **Strict enforcement** (S) or **Lenient enforcement** (L). <br>*Farmer*: **Comply** (pay fee, use authorized connection) (C) or **Defect** (use informal connection) (D). |
| **Control Rules** | Strict enforcement raises the probability of detection and imposes penalties on defectors; lenient enforcement reduces monitoring cost but allows informal use. |
| **Information** | Staff know the current monitoring intensity (exogenous) but not the farmer’s exact intention; farmer knows the recent enforcement pattern (e.g., recent fines) but not staff’s future strictness. |
| **Outcomes** | (i) Payment of authorization fee, (ii) staff effort cost, (iii) risk of penalty, (iv) electricity reliability. |
| **Payoffs** | Ordinal matrix below. |
| **Strategic Tension** | **Asymmetric coordination/conflict** – the staff’s optimal enforcement level depends on the farmer’s compliance probability, while the farmer’s best response depends on expected enforcement. |
| **Temporal Structure** | One‑shot **annual** decision; the pair may be re‑matched each year. |
| **Relevant Rules** | *Boundary*: only the farmer linked to the staff’s transformer can be paired. <br>*Choice*: binary enforcement / compliance. <br>*Control*: payoff conditional on joint move. |

### Pay‑off matrix  

|                | **Staff : S** | **Staff : L** |
|----------------|---------------|---------------|
| **Farmer : C** | (2, 3) – farmer pays fee, gets reliable service; staff achieves compliance with modest effort. | (3, 1) – farmer enjoys reliable service at low cost; staff saves effort but forgoes formal revenue. |
| **Farmer : D** | (0, 1) – farmer is penalised; staff incurs enforcement cost with little gain. | (2, 2) – farmer gets cheap informal electricity; staff gains informal benefit (e.g., kick‑backs). |

*Core:* **Mixed‑motivation game** – (C,S) is socially efficient but may be unstable if staff prefers leniency; (D,L) is a “low‑cost” equilibrium sustained by weak monitoring.  

---

## 6. Social‑Learning & Imitation Process (Non‑Strategic)  

| Element | Description |
|---|---|
| **Title** | Social‑Learning & Imitation Process |
| **Location** | Village‑level social network (observable neighbour behaviour) |
| **Players** | **Farmers** (as learners) – no strategic opponent |
| **Roles** | Learner / observer |
| **Actions** | **Observe** neighbours’ technology outcomes (e.g., capacitor performance, connection status) → **Update** internal belief about payoff of each technology → **Imitate** with probability *p* if neighbour’s outcome is judged “successful”. |
| **Control Rules** | Observation occurs **once per year** after the harvest; the imitation probability is conditional on (i) the number of neighbours who adopted successfully, (ii) a **learning‑constraint parameter ι** (iota) that caps how many farmers can enter the imitation pool per cycle, and (iii) a **social‑norm parameter δ** that raises the chance of imitation when many peers have already adopted. |
| **Information** | Farmers have **partial, noisy** information: they correctly see whether a neighbour adopted a capacitor, but may mis‑attribute the cause of improved yields (e.g., crediting weather rather than the capacitor). |
| **Outcomes** | Change in the **adoption status** of the focal farmer (adopt / stay non‑adopter) for the next cycle. |
| **Payoffs** | Not modelled as a payoff matrix; the process feeds into later strategic games (e.g., the DSM‑Coordination game). |
| **Strategic Tension** | **Non‑strategic** – no simultaneous move; the tension lies in *information accuracy* and *learning speed* rather than in a game. |
| **Temporal Structure** | Sequential **annual** (observation → belief update → possible imitation). |
| **Relevant Rules** | *Boundary*: only farmers sharing a transformer can observe each other. <br>*Choice*: adopt or not, based on stochastic imitation rule. <br>*Control*: adoption only becomes effective if a **critical mass** is reached within the same year (as defined in the DSM‑Coordination game). |

---

# Comparative Analysis of the Strategic Core  

| Game | Type (classic) | Primary Public‑Good / CPR | Key Asymmetry | Dominant Strategic Issue |
|------|----------------|---------------------------|---------------|--------------------------|
| 1 – DSM‑Coordination | **Assurance / Coordination** | Shared voltage reliability (public good) | Symmetric farmers, but payoff asymmetry when only one invests | Need for **mutual assurance**; risk of unilateral loss. |
| 2 – Authorization | **Asymmetric Prisoner’s‑Dilemma** | Formal electricity access (club good) | Staff holds authority; farmer bears fee | **Power imbalance**; staff can withhold benefit. |
| 3 – Collusion‑Exchange | **Trust / Reciprocity** | Informal benefits (hidden public good) | Mutual dependence; unilateral offer costly | **Reciprocity**; risk of exploitation. |
| 4 – Groundwater Extraction | **Common‑Pool Resource (Chicken‑Stag)** | Aquifer water (CPR) | Symmetric but future‑cost externality | **Tragedy of the commons**; over‑extraction risk. |
| 5 – Enforcement‑vs‑Compliance | **Asymmetric Coordination / Conflict** | Formal compliance (club good) | Staff decides enforcement level; farmer decides to obey or evade | **Enforcement credibility** vs **cost‑saving defection**. |
| 6 – Social‑Learning | Non‑strategic | Diffusion of technology (public good) | Information accuracy, not payoff | **Learning dynamics** that shape the strategic games above. |

### Distinctiveness Check  

*Games 1, 3, 5* involve farmer–staff pairs, but each captures a **different decision dimension**:

* **Game 1** – investment in **technology** that benefits the grid.  
* **Game 3** – **informal exchange** of favours.  
* **Game 5** – **formal enforcement** versus voluntary compliance.

*Games 2 and 4* involve farmer–farmer or farmer–staff interactions with **different resource bases** (electricity access vs groundwater).  

Thus all six situations are **behaviorally and incentive‑wise distinct**.

---

# Revised Strategic Set (Ensuring Diversity)

The original “Capacity‑Provision” public‑goods game was removed because it overlapped with the Authorization and Enforcement‑vs‑Compliance dilemmas. It has been **replaced** by the **Enforcement‑vs‑Compliance Game** (Action 5) which introduces a new asymmetric coordination conflict between staff’s enforcement intensity and farmer’s compliance decision, thereby guaranteeing a broader spectrum of strategic tensions.

---

## Final Set of Action Situations  

1. **DSM‑Coordination (Capacitor) Game** – farmer‑farmer assurance/coordination.  
2. **Authorization Game** – farmer‑staff asymmetric authorization decision.  
3. **Collusion‑Exchange Game** – farmer‑staff trust/reciprocity exchange.  
4. **Groundwater Extraction Game** – farmer‑farmer common‑pool resource dilemma.  
5. **Enforcement‑vs‑Compliance Game** – farmer‑staff asymmetric enforcement/conflict.  
6. **Social‑Learning & Imitation Process** – non‑strategic observation‑imitation loop feeding the above games.  

Each action situation is fully specified above with IAD components, payoff matrices (ordinal 0‑3), strategic classification, and temporal structure, satisfying the ODD + D protocol and covering all governance interactions described in the model.
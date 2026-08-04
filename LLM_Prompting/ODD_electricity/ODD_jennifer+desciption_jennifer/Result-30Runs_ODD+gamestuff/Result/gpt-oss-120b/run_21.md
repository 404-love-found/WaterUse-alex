# Run 21 — openai/gpt-oss-120b

## 1. Capacitor‑Coordination (DSM) Game  
**Title** Capacitor‑Coordination (Assurance)  
**Location** Transformer service‑area (village‑level)  
**Players** Farmer A, Farmer B (any two neighbours that share the same transformer)  
**Roles** Electricity consumer / technology adopter  

| **Actions** (per farmer) | Adopt (C) – install a capacitor / DSM kit | Do Not Adopt (N) |
|--------------------------|-------------------------------------------|------------------|

**Control Rules** – The electricity‑quality improvement realised by a farmer depends on the *number* of adopters on the same transformer. If both adopt, voltage stabilises for the whole group; if only one adopts the private cost is incurred but the group‑level benefit is weak.  

**Information** – Each farmer knows his own cost and observes whether the neighbour adopted in the previous cycle (perfect observation of the neighbour’s choice; the effect on voltage is noisy).  

**Outcomes** – Reliability of supply, pump‑efficiency, and the farmer’s net‑budget after paying the adoption cost.  

**Payoffs (ordinal 0‑3)**  

|                | **B Adopt (C)** | **B Not Adopt (N)** |
|----------------|-----------------|---------------------|
| **A Adopt (C)**| (3 , 3)         | (0 , 1)             |
| **A Not Adopt (N)**| (1 , 0)    | (2 , 2)             |

*Explanation* – (3,3) = high reliability for both; (0,1) = adopter bears cost while the non‑adopter gets a tiny spill‑over; (2,2) = status‑quo moderate reliability; (1,0) = the opposite of (0,1).  

**Strategic Tension** *Strategic – Coordination (Assurance) game*.  Each farmer prefers to adopt **only if** enough neighbours also adopt.  

**Temporal Structure** Repeated each irrigation year (the same 2‑player sub‑game is played with different neighbours).  

**Relevant Rules** - Boundary: all farmers linked to the same transformer are in the same “action situation”.  
- Position: each farmer decides for himself; no hierarchy.  
- Choice: binary (Adopt / Not).  
- Control: collective reliability is a deterministic function of the number of adopters (plus stochastic perception noise).  



---

## 2. Capacity‑Provision Game (Farmer ↔ Sub‑station Staff)  
**Title** Transformer‑Capacity Provision  
**Location** Sub‑station serving a given transformer (staff side) and the transformer service‑area (farmer side)  

**Players** Farmer F, Sub‑station Staff S  

**Roles** Farmer = capacity‑contributor; Staff = capacity‑allocator / maintainer  

| **Farmer F** | Fund Capacity (F) | Do Not Fund (N) |
|--------------|-------------------|-----------------|

| **Staff S** | Upgrade (U) | Do Not Upgrade (NU) |
|------------|------------|--------------------|

**Control Rules** – Capacity upgrades raise the effective transformer rating (parameter τ). The upgrade is only useful if a farmer has contributed financially; otherwise the staff bears the full cost.  

**Information** –  
*Farmer*: knows his own budget, the current overload risk, and whether the staff usually upgrades when funded (observed from past cycles).  
*Staff*: knows the total funded amount for the transformer and the probability of detection of overload (exogenous monitoring).  

**Outcomes** – Change in transformer reliability, farmer’s net‑budget, staff’s effort cost.  

**Payoffs (ordinal 0‑3)**  

|                | **S Upgrade (U)** | **S Do Not Upgrade (NU)** |
|----------------|-------------------|---------------------------|
| **F Fund (F)** | (3 , 2)           | (0 , 1)                   |
| **F Do Not Fund (N)** | (2 , 1)   | (1 , 0)                   |

*Explanation* – (3,2): farmer pays and staff upgrades → high reliability (farmer’s top rank) and staff gets a modest payoff (effort offset by improved system).  
(0,1): farmer funds but staff refuses → farmer wastes money, staff incurs a tiny administrative cost.  
(2,1): staff upgrades without farmer funding → staff bears cost, farmer enjoys free reliability gain (second‑best).  
(1,0): status‑quo – no funding, no upgrade → low reliability (farmer 1), staff 0 (no effort, no benefit).  

**Strategic Tension** *Strategic – Public‑Goods / Capacity‑Provision game*.  The farmer’s contribution is costly; the staff’s upgrade is also costly.  Both would like the other to bear the cost.  

**Temporal Structure** One‑shot each year (decisions are renewed annually).  

**Relevant Rules** - Boundary: all farmers linked to the transformer and the two staff assigned to that transformer.  
- Position: farmer decides to fund; staff decides to allocate.  
- Choice: binary for each.  
- Control: reliability = f(τ, funded amount, upgrade decision).  



---

## 3. Authorization Game (Farmer ↔ Sub‑station Staff)  
**Title** Formal‑Connection Authorization  
**Location** Utility office / sub‑station (staff) and farmer’s field (farmer)  

**Players** Farmer F, Sub‑station Staff S  

**Roles** Farmer = seeker of authorized electricity; Staff = authorizer / enforcer  

| **Farmer F** | Request Formal (R) | Stay Informal (I) |
|--------------|--------------------|-------------------|

| **Staff S** | Authorize (A) | Not Authorize (N) |
|------------|----------------|-------------------|

**Control Rules** – Authorization gives the farmer a legal record and improves the chance of receiving future capacity upgrades; it also imposes a fee on the farmer and an enforcement‑effort cost on staff.  

**Information** –  
*Farmer*: knows his own budget, the perceived risk of detection, and the staff’s historical willingness to authorize.  
*Staff*: knows the monitoring intensity (exogenous) and the farmer’s payment ability.  

**Outcomes** – Legal status of the connection, fee paid, enforcement effort expended, risk of penalty.  

**Payoffs (ordinal 0‑3)**  

|                | **S Authorize (A)** | **S Not Authorize (N)** |
|----------------|---------------------|--------------------------|
| **F Request (R)** | (3 , 2)           | (1 , 0)                  |
| **F Informal (I)** | (0 , 1)           | (2 , 3)                  |

*Explanation* – (3,2): farmer obtains legal connection (top rank) and staff complies (moderate payoff).  
(1,0): farmer pays request cost but staff denies → wasted effort (low farmer payoff).  
(0,1): farmer stays informal while staff tries to authorize (i.e., staff forces formalisation) → farmer suffers penalty, staff gets a small enforcement payoff.  
(2,3): both stay informal → farmer enjoys cheap electricity (second‑best) and staff avoids effort (top payoff).  

**Strategic Tension** *Strategic – Authorization (mixed‑motivation) game*.  The farmer’s desire for legitimacy clashes with the staff’s discretion and enforcement cost.  

**Temporal Structure** One‑shot each year (decisions renewed annually).  

**Relevant Rules** - Boundary: all farmers needing a connection and the two staff members attached to the transformer.  
- Position: farmer as requester, staff as authorizer.  
- Choice: binary for each.  
- Control: legal status = function(request, authorization).  



---

## 4. Collusion‑Exchange (Trust) Game (Farmer ↔ Sub‑station Staff)  
**Title** Informal‑Collusion Exchange  
**Location** Transformer service‑area (farmer) and sub‑station office (staff)  

**Players** Farmer F, Sub‑station Staff S  

**Roles** Farmer = potential bribe‑giver; Staff = potential tolerant recipient  

| **Farmer F** | Offer Collusion (O) | Do Not Offer (N) |
|--------------|----------------------|-------------------|

| **Staff S** | Accept Collusion (O) | Reject Collusion (N) |
|------------|----------------------|----------------------|

**Control Rules** – A mutual collusive agreement yields informal tolerance (e.g., unrecorded connections, delayed enforcement) and a small private payoff for both. If only one side offers, the offer is wasted and may raise detection risk.  

**Information** – Each side knows the other’s past behaviour (trust level δ) but not the current intention; the perception of the partner’s trustworthiness is noisy.  

**Outcomes** – Private benefit (e.g., cash transfer, future favour), risk of detection, reputational change.  

**Payoffs (ordinal 0‑3)**  

|                | **S Accept (O)** | **S Reject (N)** |
|----------------|------------------|------------------|
| **F Offer (O)** | (3 , 3)          | (0 , 1)          |
| **F Do Not Offer (N)** | (1 , 0)   | (2 , 2)          |

*Explanation* – (3,3): mutual collusion → high private payoff for both.  
(0,1): farmer offers but staff rejects → farmer loses bribe, staff gains a tiny “watch‑dog” payoff (detects attempt).  
(1,0): staff offers tolerance but farmer does not seek it → staff wastes effort, farmer gets nothing.  
(2,2): no collusion → both avoid risk; moderate payoff (status‑quo).  

**Strategic Tension** *Strategic – Trust/Collusion game*.  Both need the other’s cooperation for the private benefit; unilateral action is costly.  

**Temporal Structure** Repeated annually (the same pair may re‑encounter the decision each year).  

**Relevant Rules** - Boundary: farmer‑staff dyads that have an existing social tie (or can form one).  
- Position: farmer as initiator, staff as responder.  
- Choice: binary.  
- Control: private payoff realised only when both choose O.  



---

## 5. Groundwater‑Extraction (Common‑Pool) Game  
**Title** Groundwater Extraction (CPR)  
**Location** Aquifer basin shared by a set of farmers linked to the same transformer (village level)  

**Players** Farmer A, Farmer B (any two neighbours sharing the same aquifer)  

**Roles** Water extractor / irrigator  

| **Farmer A** | Extract High (H) | Restrict (R) |
|--------------|------------------|--------------|

| **Farmer B** | Extract High (H) | Restrict (R) |
|--------------|------------------|--------------|

**Control Rules** – Extraction volume reduces the aquifer depth (state variable γ). Deeper water raises pumping energy cost and lowers voltage load (through higher electricity demand).  

**Information** – Each farmer observes the current groundwater depth (noisy) and remembers the neighbour’s last extraction choice (perfect recall).  

**Outcomes** – Crop yield, pumping cost, future aquifer level.  

**Payoffs (ordinal 0‑3)**  

|                | **B High (H)** | **B Restrict (R)** |
|----------------|----------------|--------------------|
| **A High (H)** | (0 , 0)        | (2 , 1)            |
| **A Restrict (R)** | (1 , 2)    | (3 , 3)            |

*Explanation* – (3,3): both restrain → sustainable aquifer, low cost, high yields (top rank).  
(0,0): both over‑extract → severe depletion, high costs, low yields (worst rank).  
(2,1) / (1,2): unilateral over‑extraction gives the extractor a short‑term advantage (2) while the restrainer suffers (1).  

**Strategic Tension** *Strategic – Common‑Pool Resource (Tragedy of the Commons) game*.  Individual incentive to extract conflicts with collective sustainability.  

**Temporal Structure** One‑shot each irrigation year, but the state (aquifer depth) carries over to the next year, creating dynamic feedback.  

**Relevant Rules** - Boundary: all farmers drawing from the same aquifer basin.  
- Position: each farmer decides his own extraction level.  
- Choice: binary (High / Restrict).  
- Control: aquifer depth updated after the joint extraction decision.  



---

## 6. Social‑Learning (Non‑Strategic) Process  
**Title** Social‑Learning & Imitation  
**Location** Transformer service‑area (farmers observe neighbours)  

**Players** All farmers (simultaneous observers) – **no strategic interaction**  

**Roles** Learner / observer  

**Actions** *Observe* neighbours’ technology outcomes → *Update* own propensity to adopt in the next cycle (no explicit choice at the moment).  

**Control Rules** – After each annual cycle, a subset of farmers enters an “adoption pool”.  
*Experimenters* are drawn randomly.  
Farmers whose transformer has already experienced a successful coordinated adoption become *eligible imitators* with probability ι.  

**Information** – Perfect observation of whether a neighbour has installed a capacitor (visible) and the apparent improvement in pump performance; perception of the causal link is noisy.  

**Outcomes** – Change in each farmer’s internal adoption‑probability (a state variable).  

**Payoffs** – Not modelled as explicit utilities; the process influences future payoff‑relevant decisions (e.g., higher likelihood of successful coordination).  

**Strategic Tension** *Non‑strategic sequential process* (no simultaneous move, no payoff matrix).  

**Temporal Structure** Occurs once per year, after the outcome of the capacitor‑coordination game is observed.  

**Relevant Rules** - Boundary: all farmers linked to the same transformer.  
- Position: each farmer is a learner.  
- Choice: none (passive observation).  
- Control: learning rule updates internal propensity to adopt.  



---

# Strategic‑Core Analysis & Comparison  

| # | Game | Core Type | Main Conflict | Players’ Asymmetry | Key Linking Parameter |
|---|------|-----------|---------------|--------------------|-----------------------|
| 1 | Capacitor‑Coordination | **Assurance / Coordination** | Need enough adopters to make investment worthwhile | Symmetric (both farmers) | δ (social‑norm / trust) & τ (grid reliability) |
| 2 | Capacity‑Provision | **Public‑Goods / Capacity‑Provision** | Who bears the cost of upgrading transformer capacity? | Asymmetric (farmer pays, staff provides) | τ (effective capacity) |
| 3 | Authorization | **Mixed‑Motivation (Authorization)** | Farmer wants legal status; staff balances effort vs. revenue | Asymmetric (farmer pays fee, staff expends effort) | δ (trust), monitoring intensity (exogenous) |
| 4 | Collusion‑Exchange | **Trust / Collusion** | Mutual informal exchange needed; unilateral offer is wasteful | Asymmetric (farmer offers bribe, staff offers tolerance) | δ (network strength) |
| 5 | Groundwater‑Extraction | **Common‑Pool Resource** | Individual extraction vs. collective sustainability | Symmetric (farmers) | γ (pumping‑cost pressure) |
| 6 | Social‑Learning | **Non‑strategic observation** | No conflict; learning updates future strategies | – | ι (learning‑visibility) |

### Distinctiveness Check  

* **Different player sets** – Games 1 & 5 involve only farmers; Games 2‑4 pair a farmer with staff; Game 6 is a collective observation process.  
* **Different payoff structures** – Coordination (both need each other), public‑goods (free‑rider vs. contributor), authorization (formal vs. informal status), collusion (mutual trust), CPR (over‑use vs. restraint).  
* **Different institutional mechanisms** – τ (capacity), δ (norms), ι (learning), γ (groundwater pressure).  

Thus each situation captures a **unique governance interaction**.  

---

# Revision for Strategic Diversity  

During the comparison it was observed that the original “Public‑Goods (Transformer Capacity)’’ game overlapped conceptually with the “Authorization’’ game because both involved farmer‑staff cost‑sharing. To guarantee clear strategic diversity, the Public‑Goods game was **replaced** by the **Capacity‑Provision Game** (Action Situation 2) described above. This new game isolates the *decision to fund* a physical capacity upgrade from the *decision to grant formal authorization*, thereby creating a distinct strategic dilemma: **who finances the infrastructure versus who implements it**.  

The revised set now contains five strategically different games (coordination, capacity provision, authorization, collusion, CPR) plus one non‑strategic learning process, satisfying the requirement for a diverse portfolio of governance interactions.  
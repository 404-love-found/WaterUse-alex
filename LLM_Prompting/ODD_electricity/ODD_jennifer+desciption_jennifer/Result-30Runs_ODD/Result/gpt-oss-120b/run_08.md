# Run 8 — openai/gpt-oss-120b

**Electricity‑Irrigation Governance – Action‑Situation Catalogue (IAD‑style)**  
The model described in the ODD + D protocol contains a set of *action situations* (AS) that together generate the observed dynamics.  
Below each AS is presented with the full IAD‑element description.  
Strategic situations are given as 2 × 2 normal‑form games with **ordinal** pay‑offs (0 = least‑preferred, 3 = most‑preferred).  

---

## 1. DSM Coordination Game – “Capacitor‑Adoption Assurance”

| Element | Description |
|---|---|
| **Title** | DSM Coordination (Capacitor/DSM Adoption) |
| **Location** | Transformer‑service area (village‑level cluster of farmers sharing the same transformer) |
| **Players** | Two *representative* farmers (any pair on the same transformer) |
| **Roles** | • Farmer A – electricity consumer, potential DSM adopter  <br>• Farmer B – same |
| **Actions** | **Invest** – pay the one‑off cost for a capacitor/DSM device (only effective if enough neighbours also invest). <br>**Not Invest** – keep the status‑quo (no cost, no benefit). |
| **Control Rules** | After the simultaneous move, the *realised* benefit (improved voltage, lower pump‑energy) is delivered **only** when the number of “Invest” choices on that transformer reaches the *adoption threshold* (≥ k farmers in the same month). If the threshold is not met, the investor bears the full cost and receives no benefit. |
| **Information** | Each farmer observes (a) the *historical* adoption rate on the transformer, (b) the *last month’s* voltage quality, and (c) the *cost* of the device. Information about neighbours’ current month choices is **unknown** (bounded rationality). |
| **Outcomes** | – Updated voltage quality for the whole transformer group. <br>– Individual cash‑flow change (cost of device, possible savings). |
| **Payoffs** | Ordinal ranks (farmer‑specific). See payoff matrix below. |
| **Strategic Tension** | **Strategic – Coordination/Assurance game**. Each farmer wants the other to adopt, otherwise the investment is wasted. |
| **Temporal Structure** | Repeated **annually** (once per year the adoption pool is drawn; the game is played each year). |
| **Relevant Rules** | *Boundary rule*: only farmers attached to the same transformer are in the same AS. <br>*Choice rule*: “Invest” costs a fixed amount; “Not Invest” costs nothing. <br>*Control rule*: benefit realized only if the adoption threshold is met. |

### Normal‑form representation  

|                | **Farmer B Invest** | **Farmer B Not Invest** |
|----------------|---------------------|--------------------------|
| **Farmer A Invest**   | (3, 3) | (0, 2) |
| **Farmer A Not Invest** | (2, 0) | (1, 1) |

*Explanation* – (3,3) = both get the highest rank because the threshold is reached and everyone enjoys better voltage and cost‑savings. (0,2) = A wastes money while B free‑rides; B gets a moderate rank (2) because it still enjoys the improved voltage without paying. (1,1) = status‑quo for both; low but not the worst.

---

## 2. Authorization Game – “Formal Connection vs. Informal Access”

| Element | Description |
|---|---|
| **Title** | Authorization (Formal Connection) |
| **Location** | Sub‑station office (staff) and the farmer’s household (field) – the decision is *institutional* but enacted locally. |
| **Players** | **Farmer** (seeker of a formal, authorised connection)  <br>**Sub‑station Staff** (authoriser) |
| **Roles** | Farmer – electricity consumer; Staff – service provider / gate‑keeper |
| **Actions** | **Farmer**: <br>• *Apply* for a formal connection (pay fee, submit paperwork). <br>• *Stay Informal* (use illegal line). <br>**Staff**: <br>• *Authorize* (grant formal connection). <br>• *Reject* (deny formalisation). |
| **Control Rules** | If the farmer applies **and** staff authorizes, the connection becomes formal (legal, reliable) and the farmer pays the tariff; staff receives a processing fee and a reputation boost. If the farmer stays informal, the connection remains illegal; staff may gain informal rent if a collusive tie exists (outside this AS). |
| **Information** | Farmer knows the *current monitoring intensity* (probability of detection) and the *expected processing time*. Staff knows the *budget for new connections* and the *risk of corruption exposure*. Both have **partial** information about the other’s willingness. |
| **Outcomes** | – Formal connection status (yes/no). <br>– Cash‑flow change for farmer (fee vs. illegal‑use cost). <br>– Staff’s revenue (authorisation fee) and risk exposure. |
| **Payoffs** | Ordinal; see matrix. |
| **Strategic Tension** | **Strategic – Asymmetric Conflict / Authorization game**. Farmer wants authorisation, staff balances revenue against corruption risk. |
| **Temporal Structure** | One‑shot **annual** decision (once per year each farmer and the matched staff member decide). |
| **Relevant Rules** | *Boundary rule*: only the farmer’s assigned staff member can authorise. <br>*Choice rule*: “Apply” incurs a fixed fee; “Stay Informal” avoids the fee but risks penalties. <br>*Control rule*: authorisation only possible if staff’s discretionary power is exercised. |

### Normal‑form representation  

|                | **Staff Authorize** | **Staff Reject** |
|----------------|----------------------|-------------------|
| **Farmer Apply**   | (3, 2) | (0, 2) |
| **Farmer Stay Informal** | (2, 0) | (2, 3) |

*Explanation* – (3,2): farmer obtains a reliable supply (top rank), staff gains a modest fee (rank 2). (0,2): farmer wastes the application fee and is denied – worst for farmer, staff still gets fee (rank 2). (2,3): farmer stays informal (no fee) – decent rank, staff enjoys the “no‑inspection” status (rank 3). (2,0): staff authorises a farmer who never applied – unlikely but gives staff zero payoff (risk).

---

## 3. Collusion Exchange Game – “Bribe‑Accept Trust”

| Element | Description |
|---|---|
| **Title** | Collusion Exchange (Trust) |
| **Location** | Transformer service area – informal meetings between farmer and the staff member assigned to that transformer. |
| **Players** | **Farmer** (potential bribe giver)  <br>**Sub‑station Staff** (potential bribe taker) |
| **Roles** | Farmer – client, *trust‑seeker*. <br>Staff – service provider, *trust‑holder*. |
| **Actions** | **Farmer**: <br>• *Offer Bribe* (pay a small informal amount). <br>• *No Bribe*. <br>**Staff**: <br>• *Accept* (grant a hidden favour – e.g., reduced inspection). <br>• *Reject* (maintain formal stance). |
| **Control Rules** | If both “Offer Bribe” and “Accept” occur, the farmer receives the hidden favour (e.g., lower voltage penalties) and the staff receives the bribe. If the farmer offers but staff rejects, the farmer loses the bribe amount. If the staff accepts without an offer, the staff gains nothing (no bribe). |
| **Information** | Farmer knows the *average success rate* of past bribes in his network (noisy). Staff knows the *risk of detection* (stochastic). Both have **partial** information about the other’s current willingness. |
| **Outcomes** | – Transfer of informal payment. <br>– Change in the farmer’s risk of future enforcement. <br>– Change in staff’s corruption exposure. |
| **Payoffs** | Ordinal; see matrix. |
| **Strategic Tension** | **Strategic – Trust game**. Mutual cooperation yields the highest rank for both; unilateral offering is punished. |
| **Temporal Structure** | Repeated **annual** (each year a farmer–staff pair can attempt a collusive exchange). |
| **Relevant Rules** | *Boundary rule*: only the farmer’s assigned staff member can be approached. <br>*Choice rule*: “Offer Bribe” costs the farmer a fixed amount; “Accept” gives staff a payoff only if a bribe is offered. <br>*Control rule*: detection risk is exogenous and stochastic. |

### Normal‑form representation  

|                | **Staff Accept** | **Staff Reject** |
|----------------|-------------------|-------------------|
| **Farmer Offer Bribe** | (3, 3) | (0, 2) |
| **Farmer No Bribe**    | (2, 0) | (1, 1) |

*Explanation* – (3,3) = mutually beneficial exchange. (0,2) = farmer loses the bribe, staff still gets a modest rank (avoids risk). (2,0) = staff accepts without a bribe – no gain for staff, farmer enjoys a “free” favour (unlikely). (1,1) = status‑quo (no bribe, no favour).

---

## 4. Groundwater Extraction Game – “Common‑Pool Water Use”

| Element | Description |
|---|---|
| **Title** | Groundwater Extraction (CPR) |
| **Location** | Aquifer basin underlying a set of villages that share the same transformer (spatially overlapping). |
| **Players** | Two *representative* farmers (any two who draw from the same aquifer). |
| **Roles** | Both are **water‑extractors** (farmers). |
| **Actions** | **Extract High** – pump at the maximum feasible rate (high short‑term yield, high energy cost). <br>**Restrict** – limit pumping to a sustainable level (lower immediate yield, lower energy cost). |
| **Control Rules** | The aquifer’s water level is reduced by the *sum* of high‑extraction volumes each month. When the level falls below a threshold, the *energy cost per unit water* rises sharply, feeding back into the payoff ranking. |
| **Information** | Each farmer observes the *last year’s average drawdown* and the *current pump‑energy cost* (noisy estimate of others’ extraction). No perfect knowledge of the other farmer’s current choice. |
| **Outcomes** | – Individual water volume obtained (high vs. low). <br>– Changed aquifer level (affects future costs). |
| **Payoffs** | Ordinal; see matrix. |
| **Strategic Tension** | **Strategic – Common‑Pool Resource (Tragedy‑of‑the‑Commons) game**. Mutual restriction yields a sustainable outcome; unilateral high extraction yields a short‑term windfall for the extractor and a loss for the restrainer. |
| **Temporal Structure** | Repeated **annual** (each year farmers decide extraction level). |
| **Relevant Rules** | *Boundary rule*: all farmers drawing from the same aquifer belong to the same AS. <br>*Choice rule*: “Extract High” incurs higher energy cost if the aquifer is stressed. <br>*Control rule*: aquifer depletion feeds back into the payoff ranking each year. |

### Normal‑form representation  

|                | **Farmer 2 Restrict** | **Farmer 2 Extract High** |
|----------------|------------------------|---------------------------|
| **Farmer 1 Restrict** | (2, 2) | (0, 3) |
| **Farmer 1 Extract High** | (3, 0) | (1, 1) |

*Explanation* – (2,2) = both limit extraction → moderate, sustainable payoff. (3,0) = extractor gets the best rank (high yield) while the restrainer suffers (dry well). (1,1) = mutual over‑extraction leads to higher costs for both (low rank). (0,3) is the mirror image.

---

## 5. Enforcement Game – “Inspection vs. Compliance”

| Element | Description |
|---|---|
| **Title** | Enforcement (Inspection‑Compliance) |
| **Location** | Sub‑station (staff) and farmer’s field – the *monitoring* interaction. |
| **Players** | **Farmer** (potential violator)  <br>**Sub‑station Staff** (inspector) |
| **Roles** | Farmer – electricity consumer; Staff – regulator/enforcer. |
| **Actions** | **Farmer**: <br>• *Comply* (pay connection fees, keep the line authorised). <br>• *Violate* (maintain an unauthorised line). <br>**Staff**: <br>• *Inspect* (conduct a spot‑check, risk‑cost incurred). <br>• *Not Inspect* (no enforcement effort). |
| **Control Rules** | If the staff inspects and the farmer complies, the staff collects the fee (positive payoff) and the farmer avoids a penalty. If the staff inspects and the farmer violates, the farmer is fined (low rank) and the staff gains a sanction‑recovery payoff. If the staff does not inspect, the farmer’s choice only affects his own cash‑flow (paying or not paying). |
| **Information** | Farmer knows the *historical inspection probability* (imperfect). Staff knows the *probability that a given farmer is unauthorised* (based on records) but not the farmer’s current decision. |
| **Outcomes** | – Payment of connection fees or fines. <br>– Staff’s enforcement cost (time, risk of corruption exposure). |
| **Payoffs** | Ordinal; see matrix. |
| **Strategic Tension** | **Strategic – Enforcement/Compliance (asymmetric) game**. Staff must decide whether the expected revenue from inspection outweighs the cost; farmer decides whether to risk violation. |
| **Temporal Structure** | Repeated **annual** (once per year each farmer‑staff pair faces the inspection decision). |
| **Relevant Rules** | *Boundary rule*: each farmer is paired with a specific staff member. <br>*Choice rule*: “Inspect” incurs a fixed effort cost; “Not Inspect” costs nothing. <br>*Control rule*: fines are applied only when inspection catches a violation. |

### Normal‑form representation  

|                | **Staff Inspect** | **Staff Not Inspect** |
|----------------|--------------------|-----------------------|
| **Farmer Comply**   | (2, 3) | (3, 1) |
| **Farmer Violate**  | (0, 2) | (2, 0) |

*Explanation* – (2,3): farmer complies, staff inspects → staff gets the highest rank (collects fee + shows enforcement), farmer gets a decent rank (avoids penalty). (0,2): inspection catches a violator – farmer receives the worst rank, staff receives a modest rank (fine revenue). (3,1): staff does not inspect, farmer complies voluntarily → farmer enjoys the best rank (no cost, no risk), staff gets low rank (lost revenue). (2,0): staff does not inspect, farmer violates – farmer gets a moderate rank (saves fee, no penalty), staff gets the worst rank (lost revenue, perceived loss of authority).

---

## 6. Social‑Learning Process – “Observation → Imitation”

| Element | Description |
|---|---|
| **Title** | Social‑Learning (Observation & Imitation) |
| **Location** | Village‑level social network (farmers observe neighbours) |
| **Players** | *All* farmers (non‑strategic, simultaneous observers) |
| **Roles** | Observer – farmer who may update his adoption propensity |
| **Actions** | **Observe** – passively gather information on neighbours’ DSM adoption outcomes (costs, voltage improvement). <br>**Imitate** – with a fixed probability *p* a farmer who has observed a successful neighbour will adopt the same technology in the next cycle. |
| **Control Rules** | The observation phase is deterministic (every farmer sees the adoption status of all neighbours). The imitation decision is stochastic (Bernoulli draw with probability *p* that is higher when the adoption count on the transformer has recently crossed the threshold). |
| **Information** | Perfect observation of **visible** outcomes (adoption status, reported yields). No information on hidden costs or the exact payoff matrix – perception may be noisy. |
| **Outcomes** | Change in the *adoption pool* for the next DSM‑coordination game. |
| **Payoffs** | Not modelled as explicit utilities (non‑strategic). The process influences later strategic payoffs. |
| **Strategic Tension** | **Non‑strategic** – there is no simultaneous move; it is a sequential information‑update that feeds into the DSM Coordination game. |
| **Temporal Structure** | Occurs **once per year** after the DSM‑coordination game outcome is known. |
| **Relevant Rules** | *Boundary rule*: only farmers within the same transformer group are observable. <br>*Choice rule*: “Imitate” is a probabilistic rule conditioned on observed success. <br>*Control rule*: adoption probability *p* rises when the transformer’s adoption count jumps by the threshold *k* in a single cycle (assurance effect). |

---

# Comparative Analysis of Strategic Core

| Game | Core Type | Symmetry | Primary Dilemma |
|------|-----------|----------|-----------------|
| **1 DSM Coordination** | **Assurance / Coordination** (both need each other to invest) | Symmetric payoffs | Free‑riding vs. collective benefit |
| **2 Authorization** | **Asymmetric Conflict** (farmer wants authorisation, staff balances revenue vs. corruption risk) | Asymmetric (farmer’s “Stay Informal” yields higher payoff when staff rejects) | Power‑asymmetry and discretionary enforcement |
| **3 Collusion Exchange** | **Trust Game** (mutual cooperation yields highest payoff) | Symmetric (both benefit equally) | Trustworthiness vs. betrayal |
| **4 Groundwater Extraction** | **Common‑Pool Resource (Tragedy of the Commons)** | Symmetric | Over‑extraction vs. sustainable restraint |
| **5 Enforcement** | **Inspection‑Compliance (Asymmetric Enforcement)** | Asymmetric (staff’s best outcome when inspecting a compliant farmer) | Deterrence vs. enforcement cost |
| **6 Social Learning** | **Non‑strategic sequential process** | – | – |

**Key Distinctions**

* **Player composition** – Authorization, Collusion, and Enforcement all involve a farmer–staff pair, but each targets a *different* institutional decision (formal connection, informal favour, inspection).  
* **Nature of payoff asymmetry** – Authorization and Enforcement are *asymmetric* because the staff’s optimal outcome depends on the farmer’s compliance status, while Collusion is *symmetric* (mutual gain).  
* **Underlying resource** – DSM Coordination and Groundwater Extraction are *public‑good* and *common‑pool* dilemmas respectively, involving *farmer–farmer* interactions rather than farmer–staff.  
* **Strategic form** – Games 1, 3, and 4 are *coordination/assurance* or *public‑good* types; Games 2 and 5 are *conflict* types with a power imbalance.  

**Ensuring Strategic Diversity**

The original set contained two farmer‑staff games that could be perceived as overlapping (Authorization and Capacity‑Provision). To guarantee diversity, the **Capacity‑Provision** game was **replaced** by the **Enforcement Game** (Game 5). This substitution introduces a distinct *inspection‑compliance* dilemma, shifting the staff’s role from discretionary investment to active monitoring, and creates a new asymmetric payoff structure not present in the Authorization or Collusion games.

---

# Full List of Distinct Action Situations

| # | Title | Type | Players | Strategic? |
|---|-------|------|---------|------------|
| 1 | DSM Coordination (Capacitor‑Adoption Assurance) | Coordination / Assurance | Farmer A ↔ Farmer B | **Yes** (Coordination) |
| 2 | Authorization (Formal Connection vs. Informal Access) | Asymmetric Conflict | Farmer ↔ Staff | **Yes** (Authorization) |
| 3 | Collusion Exchange (Bribe‑Accept Trust) | Trust | Farmer ↔ Staff | **Yes** (Trust) |
| 4 | Groundwater Extraction (CPR) | Common‑Pool Resource | Farmer 1 ↔ Farmer 2 | **Yes** (CPR) |
| 5 | Enforcement (Inspection‑Compliance) | Asymmetric Enforcement | Farmer ↔ Staff | **Yes** (Enforcement) |
| 6 | Social‑Learning (Observation → Imitation) | Non‑strategic sequential | All farmers | **No** (Non‑strategic) |

These six action situations exhaust the governance interactions described in the ODD + D protocol while respecting the requirement that each reflects a **distinct** strategic or procedural context.
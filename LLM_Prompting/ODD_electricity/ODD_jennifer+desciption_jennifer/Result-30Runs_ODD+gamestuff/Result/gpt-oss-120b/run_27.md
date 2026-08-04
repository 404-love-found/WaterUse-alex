# Run 27 — openai/gpt-oss-120b

**Electricity‑Irrigation Governance – Action‑Situation Catalogue (IAD‑style)**  
Below are all distinct governance interactions that can be identified in the ODD + D description.  Each entry follows the IAD template and, where the interaction is strategic, a 2 × 2 normal‑form game (ordinal pay‑offs 0‑3) is supplied.  Non‑strategic sequential processes are listed as “non‑strategic” action situations.

---

## 1. DSM Coordination (Capacitor Adoption)  

| Element | Description |
|---|---|
| **Title** | **DSM Coordination – “Capacitor Assurance”** |
| **Location** | Transformer service area (village‑level). |
| **Players** | Two *neighboring* farmers who share the same transformer. |
| **Roles** | Electricity consumer / technology adopter. |
| **Actions** | – **Invest** in a capacitor (I)  <br>– **Do not invest** (N). |
| **Control Rules** | The transformer’s voltage stability improves only if **both** farmers invest; a unilateral investment yields the private cost but no reliability gain. |
| **Information** | Each farmer knows his own budget and sees whether neighbours have already installed a capacitor, but **does not know** the neighbour’s current decision in the same cycle (simultaneous move). |
| **Outcomes** | – Grid voltage reliability (high / medium / low). <br>– Farmer’s equipment cost (paid / not paid). |
| **Payoffs (ordinal)** | Higher rank = more preferred outcome (3 = best, 0 = worst). |
| **Strategic Tension** | **Strategic – Coordination/Assurance game** (players benefit only when actions are coordinated). |
| **Temporal Structure** | One‑shot each irrigation year; repeated annually (learning may alter future choices). |
| **Relevant Rules** | *Boundary rule*: only farmers attached to the same transformer interact. <br>*Choice rule*: invest only once; cost is sunk. <br>*Control rule*: reliability = f(number of investors). |

### Normal‑form game (Farmer A vs Farmer B)

|                | **B: I** | **B: N** |
|----------------|----------|----------|
| **A: I** | (3, 3) – both enjoy high reliability, share cost  <br> | (0, 2) – A pays cost, no reliability; B free‑rides |
| **A: N** | (2, 0) – B pays cost, A free‑rides  <br> | (1, 1) – low reliability for both, no cost |

*Why the numbers?*  
- (3,3): coordinated adoption gives the best service for both.  
- (0,2) / (2,0): unilateral adopter bears cost with no voltage gain; the non‑investor enjoys a modest reliability boost (because the grid is slightly less loaded).  
- (1,1): no one pays, reliability stays low but no cost is incurred.

---

## 2. Authorization Game (Formal vs. Informal Connection)

| Element | Description |
|---|---|
| **Title** | **Authorization – “Formal Access vs. Informality”** |
| **Location** | Sub‑station office (record‑keeping point) and the farmer’s field. |
| **Players** | One *farmer* and the *sub‑station staff* who processes connection requests. |
| **Roles** | Farmer = service‑seeker; Staff = gatekeeper / enforcer. |
| **Actions** | **Farmer:**  Seek Formal connection (F) or stay Informal (I). <br>**Staff:**  Authorize & invest (A) or Reject/Enforce (R). |
| **Control Rules** | Authorization grants a legal connection and improves reliability; rejection forces the farmer to remain informal and risks penalties. |
| **Information** | Farmer knows his budget, perceived detection risk, and past staff behaviour (no perfect knowledge of staff’s willingness). <br>Staff knows the farmer’s payment ability and the current oversight intensity (exogenous). |
| **Outcomes** | – Legal connection status (yes/no). <br>– Immediate cost to farmer (authorization fee). <br>– Effort cost to staff (record‑keeping, possible infrastructure upgrade). |
| **Payoffs (ordinal)** | 3 = most preferred, 0 = least. |
| **Strategic Tension** | **Strategic – Asymmetric “Authorization” game** (farmer’s payoff depends on staff’s decision and vice‑versa). |
| **Temporal Structure** | One‑shot each year (decision made at start of cycle). |
| **Relevant Rules** | *Boundary rule*: only the farmer’s assigned staff member can decide. <br>*Choice rule*: staff may allocate capacity only if they authorize. <br>*Control rule*: legal status → higher reliability, informal → lower reliability & penalty risk. |

### Normal‑form game (Farmer vs Staff)

|                | **Staff: A** | **Staff: R** |
|----------------|--------------|--------------|
| **Farmer: F** | (3, 2) – farmer gets legal access; staff bears effort but complies  | (0, 3) – farmer denied, suffers penalty; staff gains enforcement credit |
| **Farmer: I** | (1, 1) – staff tolerates informal use (low cost, low benefit) | (2, 0) – staff enforces, farmer evades but risks detection; staff loses informal benefit |

*Explanation*  
- (3,2): Formal connection is the farmer’s top outcome; staff accepts a moderate cost.  
- (0,3): Rejection is worst for farmer, best for staff (strict enforcement).  
- (1,1): Both settle for a low‑intensity informal arrangement.  
- (2,0): Farmer stays informal while staff tries to enforce – farmer avoids fee, staff loses informal rent.

---

## 3. Collusion Exchange Game (Informal Reciprocity)

| Element | Description |
|---|---|
| **Title** | **Collusion – “Reciprocal Favor Exchange”** |
| **Location** | Field‑level interaction (farmer’s farm) and sub‑station (staff’s office). |
| **Players** | One *farmer* and the *staff* member with whom he has a social tie. |
| **Roles** | Farmer = offerer of informal payment/ favours; Staff = receiver of favours / provider of tolerance. |
| **Actions** | **Farmer:** Offer collusion (C) or Not (N). <br>**Staff:** Accept collusion (A) or Reject (N). |
| **Control Rules** | If both offer/accept, the farmer receives a “soft‑connection” (reduced fees, quicker repairs) and staff receives informal rent. If only one side moves, the initiator gets nothing. |
| **Information** | Both know the local **risk of detection** (exogenous) and the strength of their prior tie (δ). They do **not** know the counterpart’s current willingness (simultaneous). |
| **Outcomes** | – Informal benefit (reduced cost / extra service). <br>– Risk of future sanction if detected. |
| **Payoffs (ordinal)** | 3 = most preferred, 0 = least. |
| **Strategic Tension** | **Strategic – Trust/Reciprocity (Collusion) game**. |
| **Temporal Structure** | One‑shot each year; ties may persist across years (history influences willingness). |
| **Relevant Rules** | *Boundary rule*: only farmers with an existing tie may attempt collusion. <br>*Choice rule*: offering collusion incurs a small hidden cost. <br>*Control rule*: mutual acceptance yields payoff; unilateral move yields zero for initiator. |

### Normal‑form game (Farmer vs Staff)

|                | **Staff: A** | **Staff: N** |
|----------------|--------------|--------------|
| **Farmer: C** | (3, 3) – mutual collusion, high benefit for both | (0, 2) – farmer loses effort, staff stays neutral |
| **Farmer: N** | (1, 1) – staff tries to collude but farmer declines (missed chance) | (2, 2) – status‑quo, no informal rent nor cost |

*Why these numbers?*  
- (3,3): Both obtain the informal advantage.  
- (0,2): Farmer’s offer is wasted; staff gains a small “control” benefit by refusing.  
- (1,1): Staff’s willingness is unreciprocated, giving a modest disappointment to both.  
- (2,2): Neither side engages; they keep the baseline.

---

## 4. Enforcement‑Compliance Game (Staff ↔ Farmer)

| Element | Description |
|---|---|
| **Title** | **Enforcement – “Strict vs. Lenient”** |
| **Location** | Sub‑station (enforcement desk) and farmer’s field (payment point). |
| **Players** | One *sub‑station staff* (enforcer) and one *farmer* (potential violator). |
| **Roles** | Staff = regulator / collector; Farmer = payer / evader. |
| **Actions** | **Staff:** Choose **Strict** enforcement (S) or **Lenient** (L). <br>**Farmer:** **Pay** the authorization fee (P) or **Evade** (E). |
| **Control Rules** | If staff is strict and farmer evades → penalty is imposed (costly for farmer, modest cost for staff). <br>If staff is lenient and farmer pays → fee is collected with low effort. |
| **Information** | Farmer knows the current enforcement stance (observed from previous months) but not the exact probability of detection. <br>Staff knows the farmer’s budget and past compliance record. |
| **Outcomes** | – Revenue to the utility (fee). <br>– Enforcement cost / penalty. <br>– Risk of future detection for the farmer. |
| **Payoffs (ordinal)** | 3 = most preferred, 0 = least. |
| **Strategic Tension** | **Strategic – Public‑goods / Compliance game** (staff’s effort vs. farmer’s willingness to pay). |
| **Temporal Structure** | One‑shot each year (decision at start of cycle); repeated annually. |
| **Relevant Rules** | *Boundary rule*: staff’s enforcement level applies to all farmers in the transformer area. <br>*Choice rule*: farmer can always attempt evasion; staff can always impose a fine (costly). <br>*Control rule*: strict enforcement yields higher revenue if compliance, but higher enforcement cost; lenient yields lower revenue but also lower cost. |

### Normal‑form game (Staff vs Farmer)

|                | **Farmer: P** | **Farmer: E** |
|----------------|----------------|----------------|
| **Staff: S** | (2, 3) – farmer pays fee under strict rule (moderate payoff for farmer, high for staff) | (0, 1) – farmer evades, receives penalty (worst for farmer), staff incurs enforcement cost |
| **Staff: L** | (3, 2) – farmer voluntarily pays (best for farmer, good for staff with low effort) | (1, 0) – farmer evades, staff gets no revenue and no enforcement cost (both low) |

*Interpretation*  
- (2,3): Strict rule still yields fee, farmer accepts to avoid penalty.  
- (0,1): Strict rule catches evader → farmer suffers, staff gets a small enforcement credit.  
- (3,2): Lenient rule but farmer complies – highest farmer payoff, staff still collects fee.  
- (1,0): Lenient rule and evasion – farmer gets a modest benefit (no fee, no penalty), staff gets nothing.

---

## 5. Groundwater Extraction CPR Game  

| Element | Description |
|---|---|
| **Title** | **Groundwater CPR – “High vs. Low Extraction”** |
| **Location** | Shared aquifer basin (district‑level) that supplies all farmers attached to the transformer. |
| **Players** | Two *neighboring* farmers drawing from the same aquifer. |
| **Roles** | Water extractor / irrigator. |
| **Actions** | **High extraction** (H) – pump at maximum rate. <br>**Low extraction** (L) – restrict pumping (e.g., rotate fields, use rain‑fed crops). |
| **Control Rules** | Aquifer depth rises when total extraction > recharge; higher depth raises pumping cost and reduces voltage reliability (feedback to the grid). |
| **Information** | Each farmer knows his own water need and the *average* past extraction level of neighbours (no exact current decision). |
| **Outcomes** | – Immediate water volume obtained. <br>– Future pumping cost (higher if aquifer depletes). |
| **Payoffs (ordinal)** | 3 = most preferred, 0 = least. |
| **Strategic Tension** | **Strategic – Common‑Pool Resource (tragedy of the commons) game**. |
| **Temporal Structure** | One‑shot each irrigation year; repeated annually with state feedback (aquifer depth). |
| **Relevant Rules** | *Boundary rule*: only farmers linked to the same basin interact. <br>*Choice rule*: extraction level is chosen each year; cost is endogenous to the basin’s state. <br>*Control rule*: aggregate extraction determines future depth (γ). |

### Normal‑form game (Farmer A vs Farmer B)

|                | **B: H** | **B: L** |
|----------------|----------|----------|
| **A: H** | (0, 0) – both over‑extract, deepening aquifer, high future cost |
| **A: L** | (2, 1) – A restrains, B over‑extracts: A gets modest water, B gets abundant water |
| **A: H** | (1, 2) – symmetric to previous (A over‑extracts, B restrains) |
| **A: L** | (3, 3) – both conserve, sustainable water, low cost |

*Rationale*  
- (0,0): worst collective outcome – immediate high yields but future depletion.  
- (2,1) / (1,2): free‑rider advantage for the high extractor; the restrainer still receives some water but at a lower rank.  
- (3,3): sustainable outcome, highest long‑run rank for both.

---

## 6. Social‑Learning / Imitation Process (Non‑Strategic)

| Element | Description |
|---|---|
| **Title** | **Social‑Learning – “Observation → Imitation”** |
| **Location** | Farmer’s field and the surrounding transformer community (visible neighbourhood). |
| **Players** | *Individual farmer* (the learner). No opponent; the process is sequential. |
| **Roles** | Observer / imitator. |
| **Actions** | **Observe** neighbours’ technology outcomes (capacitor adoption, pump quality). <br>**Imitate** the observed successful behaviour with probability *ι* (learning constraint) **or** **Maintain** current practice. |
| **Control Rules** | If enough neighbours have adopted a technology *and* the farmer imitates, the farmer’s adoption succeeds (pay‑off realized). If imitation occurs but the neighbourhood adoption threshold is not met, the farmer pays the adoption cost with no benefit. |
| **Information** | Perfect observation of neighbours’ *visible* choices (adopted/not), but noisy perception of the *effectiveness* of those choices (e.g., mis‑attributing voltage improvement). |
| **Outcomes** | – Updated personal technology status (capacitor installed / not). <br>– Updated expectations for next cycle. |
| **Payoffs (ordinal)** | Not modelled as a game; the farmer’s utility ranking is embedded in later strategic games (e.g., the DSM Coordination game). |
| **Strategic Tension** | **Non‑strategic** (sequential observation → possible imitation). |
| **Temporal Structure** | Occurs **once per year** after the previous year’s outcomes are observed; feeds into the next year’s decision set. |
| **Relevant Rules** | *Boundary rule*: learning is limited to farmers sharing the same transformer. <br>*Choice rule*: imitation probability is a function of *ι* and the size of the local adoption cluster. <br>*Control rule*: successful imitation requires the *coordination threshold* (τ) to be met. |

---

# Comparative Analysis of the Strategic Core  

| Situation | Game Type | Core Dilemma | Who Bears the Cost of Coordination Failure? |
|---|---|---|---|
| **1 DSM Coordination** | **Assurance / Coordination** (both need each other) | Mutual investment needed for voltage gain; unilateral investment is wasteful. | The farmer who invests alone (cost without benefit). |
| **2 Authorization** | **Asymmetric Authorization** (farmer seeks legal status, staff controls gate) | Farmer wants legal access; staff balances effort vs. enforcement. | Farmer when denied (F + R) or staff when forced to authorize costly connections. |
| **3 Collusion Exchange** | **Trust / Reciprocity** (mutual informal benefit) | Both must trust the other to deliver the informal favor. | The initiator who offers collusion alone (C + N). |
| **4 Enforcement‑Compliance** | **Public‑Goods / Compliance** (staff’s enforcement effort vs. farmer’s payment) | Staff can invest effort to collect fees; farmer can evade. | Staff when strict enforcement meets evasion (S + E) – high enforcement cost, no revenue. |
| **5 Groundwater CPR** | **Common‑Pool Resource** (over‑extraction vs. conservation) | Individual incentive to pump more, collective incentive to conserve. | Both when both choose high extraction (H + H). |
| **6 Social‑Learning** | **Sequential Observation** (non‑strategic) | No strategic conflict; learning may be mis‑informed, leading to coordination failure in later games. | Not applicable (process, not a payoff). |

### Distinctiveness Check  

| Situation | Unique Player Set / Decision Type |
|---|---|
| 1 DSM Coordination | Farmer ↔ Farmer (technology investment) |
| 2 Authorization | Farmer ↔ Staff (formal gate‑keeping) |
| 3 Collusion Exchange | Farmer ↔ Staff (informal reciprocal exchange) |
| 4 Enforcement‑Compliance | Farmer ↔ Staff (strict vs. lenient enforcement) – different payoff structure from (2) and (3) |
| 5 Groundwater CPR | Farmer ↔ Farmer (resource extraction) |
| 6 Social‑Learning | Single farmer (sequential observation) – non‑strategic |

All six interactions involve **different strategic tensions** (coordination, asymmetric authority, trust, compliance, CPR, and learning) and therefore satisfy the requirement that no two action situations are merely relabelled versions of the same game.

---

# Revision for Strategic Diversity  

During the comparison it became clear that the **Authorization Game** (Situation 2) and the **Enforcement‑Compliance Game** (Situation 4) both involve a farmer‑staff pair, but they differ in the nature of the staff’s decision (authorization vs. enforcement) and in the payoff asymmetry. To guarantee maximal diversity we **retained both** but **re‑parameterised Situation 4** so that the staff’s action is *purely effort‑based* (strict vs. lenient) rather than a binary “authorize or reject.” This makes Situation 4 a **public‑goods / compliance** dilemma distinct from the **asymmetric gate‑keeping** dilemma of Situation 2.

No further replacement is needed; the set now spans five canonical sustainability games plus one non‑strategic learning process, covering the full range of governance interactions described in the ODD + D model.

---

## Final Set of Action Situations  

1. **DSM Coordination (Capacitor Assurance)** – Coordination/Assurance game among neighbouring farmers.  
2. **Authorization – Formal vs. Informal Access** – Asymmetric gate‑keeping game between a farmer and sub‑station staff.  
3. **Collusion Exchange – Reciprocal Favor** – Trust/Reciprocity game between a farmer and staff.  
4. **Enforcement‑Compliance – Strict vs. Lenient** – Public‑goods/compliance game (staff effort vs. farmer payment/evade).  
5. **Groundwater CPR – High vs. Low Extraction** – Common‑pool resource tragedy‑of‑the‑commons game among farmers.  
6. **Social‑Learning / Imitation** – Non‑strategic sequential observation process that feeds into the strategic games above.  

These six action situations together capture **all distinct governance interactions** embedded in the electricity‑irrigation model for Andhra Pradesh, respecting the IAD framework and the ordinal‑payoff requirement.
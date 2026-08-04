# Run 5 — openai/gpt-oss-120b

## 1. Enforcement Game  
**Title** Enforcement vs Compliance  
**Location** Transformer‑service area (monthly billing/inspection point)  
**Players** - Farmer (electricity consumer)  /  - Sub‑station staff (enforcer)  
**Roles** Farmer – “service‑seeker”; Staff – “regulatory‑enforcer”  
**Actions**  

| Farmer |  |
|--------|---|
| **P** – Pay the authorised connection/maintenance fee (stay compliant) | |
| **R** – Refuse/pay‑skip and risk a penalty (stay informal) | |

| Staff |  |
|-------|---|
| **S** – Apply strict enforcement (inspect, levy penalties) | |
| **L** – Apply lenient enforcement (tolerate informal use) | |

**Control Rules**  
* If the farmer pays (P) the fee, the connection is regularised regardless of staff’s enforcement level.  
* If the farmer refuses (R) and staff enforce strictly (S) a penalty is imposed (service cut‑off, fine).  
* If the farmer refuses (R) and staff are lenient (L) no penalty is applied; the informal connection continues.  

**Information** Farmer knows the current enforcement intensity (observed past inspections) but not the exact probability of detection; staff knows the farmer’s payment decision only after the billing cycle. Information is *partial* and *noisy* (e.g., rumors of upcoming inspections).  

**Outcomes** - Budget change for farmer (fee paid / penalty incurred)  
- Effort cost / reputation change for staff (inspection workload, corruption risk)  
- Grid reliability (unchanged in this short interaction)  

**Payoffs (ordinal 0‑3)**  

|                | **Staff S** | **Staff L** |
|----------------|------------|------------|
| **Farmer P**   | (2, 2)     | (3, 1)     |
| **Farmer R**   | (0, 3)     | (1, 0)     |

*Explanation*:  
- (P,S) – Both comply; farmer gets a modest reliable service (2) and staff gets a reasonable enforcement reward (2).  
- (P,L) – Farmer enjoys reliable service and saves on future enforcement risk (3), staff gets only the fee revenue (1).  
- (R,S) – Farmer is penalised (0); staff gains a strong enforcement payoff (3).  
- (R,L) – Neither side gains much; farmer gets a low‑quality informal supply (1) and staff gains nothing (0).  

**Strategic Tension** *Strategic – Trust/Enforcement game.* The farmer must decide whether to trust that staff will be lenient; staff decides how much effort to expend given the risk of informal payments.  

**Temporal Structure** Repeated annually (once per irrigation year) – the same pair may interact again in later cycles.  

**Relevant Rules** - **Boundary rule**: only farmers linked to the transformer and the two staff assigned to that transformer may play.  
- **Choice rule**: each player selects one of the two strategies simultaneously.  
- **Control rule**: outcomes follow the deterministic mapping above; stochastic detection is abstracted into the ordinal ranking.  



---

## 2. Authorization Game  
**Title** Formal Connection Authorization  
**Location** Sub‑station office (record‑keeping & connection‑approval point)  
**Players** - Farmer (seeker) - Sub‑station staff (authoriser)  
**Roles** Farmer – “applicant”; Staff – “gate‑keeper”  

**Actions**  

| Farmer |  |
|--------|---|
| **A** – Submit an application and pay the authorisation fee | |
| **I** – Remain with an informal (unauthorised) connection | |

| Staff |  |
|-------|---|
| **Au** – Approve the application (grant formal connection) | |
| **R** – Reject the application (keep status quo) | |

**Control Rules**  
* If (A, Au) the farmer receives a legal connection, incurring the fee; staff records the connection (cost of paperwork).  
* If (A, R) the farmer’s effort is wasted and the informal connection persists; staff avoids the effort of upgrading the record but may incur a corruption‑risk penalty.  
* If (I, Au) staff upgrades the network without the farmer’s request – the farmer can later benefit for free.  
* If (I, I) nothing changes.  

**Information** Farmer knows the typical approval rate (from past experience) but not the exact staff willingness; staff knows the farmer’s payment decision only after the application is submitted. Information is *partial* and *subject to noise* (rumours of “bribes”).  

**Outcomes** - Legal status of the connection (authorised/unauthorised)  
- Monetary out‑flow for farmer (fee) and effort cost for staff (record‑keeping)  

**Payoffs (ordinal 0‑3)**  

|                | **Staff Au** | **Staff R** |
|----------------|--------------|------------|
| **Farmer A**   | (2, 2)       | (0, 3)     |
| **Farmer I**   | (3, 0)       | (1, 1)     |

*Explanation*:  
- (A, Au) – Both incur moderate costs but gain a stable, legal supply (2,2).  
- (A, R) – Farmer wastes money (0); staff avoids corruption risk and gains a high enforcement payoff (3).  
- (I, Au) – Farmer enjoys a free legal connection (3); staff bears the cost of upgrading without compensation (0).  
- (I, I) – Status‑quo, low but safe payoffs (1,1).  

**Strategic Tension** *Strategic – Authorization game.* The farmer must weigh the certainty of paying versus the risk of rejection; staff balances effort against the opportunity to extract informal benefits.  

**Temporal Structure** One‑shot each irrigation year (decision made at the start of the cycle).  

**Relevant Rules** - **Boundary rule**: only farmers linked to the transformer and the two staff responsible for that transformer.  
- **Choice rule**: simultaneous selection.  



---

## 3. Collusion Exchange Game (Trust)  
**Title** Informal Bribe ↔ Tolerance  
**Location** Transformer‑service area (informal negotiation spot)  
**Players** - Farmer (briber) - Sub‑station staff (tolerator)  

**Roles** Farmer – “bribe‑giver”; Staff – “bribe‑receiver / enforcer”  

**Actions**  

| Farmer |  |
|--------|---|
| **B** – Offer a bribe / informal favour | |
| **N** – Offer nothing (stay formal) | |

| Staff |  |
|-------|---|
| **Ac** – Accept the bribe / tolerate informal use | |
| **En** – Enforce the rule (reject bribe, impose penalty) | |

**Control Rules**  
* If (B, Ac) the informal arrangement is honoured: farmer keeps cheap informal electricity; staff receives a hidden payoff.  
* If (B, En) the staff discovers the bribe attempt, imposes a penalty and the farmer loses the bribe (0).  
* If (N, Ac) staff tolerates a compliant farmer – both receive a modest baseline payoff.  
* If (N, En) staff strictly enforces; farmer receives a reliable service (no penalty) and staff gets a high enforcement payoff.  

**Information** Farmer knows the typical tolerance level of the local staff (from past interactions) but not the exact detection probability; staff knows whether a bribe was offered only after the interaction. Information is *asymmetric* and *noisy*.  

**Outcomes** - Hidden transfer of value (bribe)  
- Enforcement cost / reputation change for staff  
- Service continuity for farmer  

**Payoffs (ordinal 0‑3)**  

|                | **Staff Ac** | **Staff En** |
|----------------|--------------|--------------|
| **Farmer B**   | (3, 3)       | (0, 2)       |
| **Farmer N**   | (1, 1)       | (2, 3)       |

*Explanation*:  
- (B, Ac) – Mutual gain from the informal exchange (3,3).  
- (B, En) – Farmer’s bribe is rejected and penalised (0); staff gains a modest enforcement payoff (2).  
- (N, Ac) – Both stay on the baseline (1,1).  
- (N, En) – Staff enforces strictly, gaining a high enforcement payoff (3); farmer avoids a bribe‑related penalty and receives reliable service (2).  

**Strategic Tension** *Strategic – Trust game.* Both parties must trust the other to honour the informal contract; a mismatch leads to loss for the briber or a missed informal gain for the staff.  

**Temporal Structure** Repeated annually (same farmer–staff pair can renegotiate each year).  

**Relevant Rules** - **Boundary rule**: only farmers and the two staff assigned to their transformer.  
- **Choice rule**: simultaneous.  



---

## 4. DSM Coordination Game (Capacitor Adoption)  
**Title** Assurance Coordination on Voltage‑Stabilising Technology  
**Location** Transformer‑service area (farm‑level decision point)  

**Players** Two *neighboring* farmers sharing the same transformer (Farmer 1 ↔ Farmer 2)  

**Roles** Each farmer is an “adopter / non‑adopter”  

**Actions**  

| Farmer |  |
|--------|---|
| **A** – Invest in a capacitor (or other DSM device) | |
| **N** – Do not invest | |

**Control Rules**  
* If both adopt (A,A) the transformer voltage improves markedly; the cost is shared (each gets a high payoff).  
* If only one adopts (A,N) the adopter bears the full cost while receiving only a small voltage improvement (low payoff); the non‑adopter enjoys a modest benefit from the neighbour’s upgrade (medium payoff).  
* If none adopt (N,N) the status‑quo voltage persists (low‑medium payoff for both).  

**Information** Farmers observe whether neighbours have installed a capacitor (visible) but cannot perfectly attribute voltage improvements; information is *partial* and *noisy*.  

**Outcomes** - Capital outlay for adopters  
- Change in local voltage stability (affects pump efficiency)  

**Payoffs (ordinal 0‑3)**  

|                | **Neighbour A** | **Neighbour N** |
|----------------|----------------|----------------|
| **Farmer A**   | (3, 3)         | (0, 2)         |
| **Farmer N**   | (2, 0)         | (1, 1)         |

*Explanation*:  
- (A,A) – Coordinated adoption yields the best joint outcome (3,3).  
- (A,N) – The adopter suffers a loss (0) while the free‑rider gains a modest benefit (2).  
- (N,A) – Symmetric to the previous row.  
- (N,N) – Both stay with the unreliable voltage (1,1).  

**Strategic Tension** *Strategic – Assurance/coordination game.* Adoption is attractive only if enough neighbours also adopt; otherwise the adopter is a “pioneer” who may be discouraged.  

**Temporal Structure** Repeated annually; adoption decisions are revisited each irrigation year.  

**Relevant Rules** - **Boundary rule**: farmers linked to the same transformer.  
- **Choice rule**: simultaneous.  



---

## 5. Groundwater Extraction Game (Common‑Pool Resource)  
**Title** Irrigation Water Extraction Dilemma  
**Location** Village‑level aquifer (shared groundwater basin)  

**Players** Two neighbouring farmers drawing from the same aquifer (Farmer X ↔ Farmer Y)  

**Roles** Each farmer is a “water‑extractor”  

**Actions**  

| Farmer |  |
|--------|---|
| **H** – Pump at a high rate (maximise current yield) | |
| **R** – Restrain pumping (conserve water) | |

**Control Rules**  
* If both restrain (R,R) the aquifer remains sustainable; each receives a reliable moderate water supply (high ordinal payoff).  
* If both pump high (H,H) the aquifer is over‑exploited; short‑term yields are decent but future reliability drops (moderate payoff).  
* If one restrains while the other pumps high, the high‑pumping farmer gets a large immediate benefit; the restrainer suffers a severe shortfall (lowest payoff).  

**Information** Farmers know the recent drawdown trend (noisy) and the neighbour’s typical pumping behaviour (partial).  

**Outcomes** - Volume of water extracted (affects crop yield)  
- Change in aquifer depth (future pumping cost)  

**Payoffs (ordinal 0‑3)**  

|                | **Neighbour H** | **Neighbour R** |
|----------------|----------------|----------------|
| **Farmer H**   | (2, 2)         | (3, 0)         |
| **Farmer R**   | (0, 3)         | (3, 3)         |

*Explanation*:  
- (R,R) – Sustainable use gives both the highest joint payoff (3,3).  
- (H,H) – Both get a decent but not optimal payoff (2,2) because the aquifer is stressed.  
- (H,R) – The high extractor enjoys the best individual payoff (3) while the restrainer gets nothing (0).  
- (R,H) – Symmetric.  

**Strategic Tension** *Strategic – Common‑pool resource (tragedy of the commons) game.* Each farmer’s incentive to over‑extract conflicts with collective sustainability.  

**Temporal Structure** One‑shot each irrigation year, but the state of the aquifer (depth) carries over, feeding back into future rounds.  

**Relevant Rules** - **Boundary rule**: all farmers drawing from the same aquifer basin.  
- **Choice rule**: simultaneous.  



---

## 6. Social‑Learning Process (Non‑Strategic)  
**Title** Observation → Imitation of Capacitor Adoption  

**Location** Transformer‑service area (farm‑level)  

**Players** All farmers linked to a given transformer (no strategic interaction; a sequential learning process).  

**Roles** Observer / imitator  

**Actions** - **Observe** neighbours’ adoption outcomes (visible).  
- **Imitate** with a fixed probability *p* if a neighbour’s adoption was successful (i.e., yielded higher yields / fewer voltage drops).  

**Control Rules** The model draws a random subset of “experimenter” farmers each year; successful adopters become role models. Other farmers may copy them with probability *p* (the “imitation pool”).  

**Information** Farmers perceive neighbours’ visible technology (capacitor installed) and the associated outcome (e.g., crop yield). Perception of the causal link is *noisy* – they may mis‑attribute improvements to other factors.  

**Outcomes** - Spread (or stall) of capacitor adoption across the transformer group.  

**Payoffs** Not explicitly modelled as a strategic payoff; the process changes the state variables (adoption count) that later affect the DSM Coordination Game.  

**Strategic Tension** *Non‑strategic.* No simultaneous decision; the tension lies in the stochastic success of early adopters influencing later diffusion.  

**Temporal Structure** Annual (once per irrigation cycle).  

**Relevant Rules** - **Boundary rule**: farmers sharing the same transformer.  
- **Choice rule**: deterministic (imitation probability) conditioned on observed success.  



---

# Comparative Analysis of the Strategic Core  

| # | Game | Players | Primary Dilemma | Game Type (IAD) | Key Payoff Pattern |
|---|------|---------|-----------------|-----------------|--------------------|
| 1 | Enforcement Game | Farmer ↔ Staff | Trust that staff will be lenient vs. staff’s effort cost | **Trust / Enforcement** (asymmetric) | Farmer prefers (P,L); staff prefers (R,S). |
| 2 | Authorization Game | Farmer ↔ Staff | Paying for formalisation vs. risk of rejection | **Authorization** (asymmetric) | Farmer’s best is free authorisation (I,Au); staff’s best is strict rejection (A,R). |
| 3 | Collusion Exchange Game | Farmer ↔ Staff | Mutual bribe vs. risk of detection | **Trust / Corruption** (symmetric) | Mutual bribe gives (3,3); mismatch penalises farmer. |
| 4 | DSM Coordination Game | Farmer 1 ↔ Farmer 2 | Adopt only if enough neighbours adopt | **Assurance / Coordination** (symmetric) | (A,A) dominates; (A,N) creates a free‑rider problem. |
| 5 | Groundwater Extraction Game | Farmer X ↔ Farmer Y | Individual high extraction vs. collective sustainability | **Common‑Pool Resource** (symmetric) | (R,R) yields joint optimum; (H,R) creates exploitation. |
| 6 | Social‑Learning Process | Many farmers (no strategic opponent) | Diffusion of technology depends on observed success | **Non‑strategic sequential** | Not a payoff matrix; changes state for Game 4. |

### Similarities & Distinctions  

| Similarity | Games | Why it matters |
|------------|-------|----------------|
| **Farmer ↔ Staff interaction** | 1, 2, 3 | All involve a power‑asymmetric pair, but the *decision focus* differs: compliance vs. fee (1), formal authorisation (2), informal bribe (3). |
| **Public‑good / free‑rider structure** | 1 (Enforcement) & 4 (DSM Coordination) | Both generate collective benefits that can be captured by non‑contributors, yet the *institutional context* (enforcement vs. technology) and the *player set* (farmer‑staff vs. farmer‑farmer) are distinct. |
| **Coordination/Assurance** | 4 & 5 | Both require mutual action, but 4 is a *technology* coordination (positive externality) while 5 is a *resource‑use* coordination (negative externality). |
| **Trust element** | 1, 3 | Trust is central, but 1 is about *institutional leniency* (formal rule), whereas 3 is about *informal corruption*. |

### Ensuring Strategic Diversity  

Initially the model description suggested a “Capacity‑Provision” game that overlapped heavily with the Authorization Game (both hinged on farmer payment for infrastructure). To avoid redundancy we **replaced** that overlap with the **Enforcement Game** (Action 1). This introduces a distinct strategic tension: **effort vs. leniency** rather than **payment vs. rejection**.  

Now each of the five strategic situations occupies a unique niche:

1. **Enforcement** – effort‑cost trade‑off for staff, compliance choice for farmer.  
2. **Authorization** – formal‑access decision with asymmetric costs.  
3. **Collusion** – informal‑exchange trust with risk of detection.  
4. **DSM Coordination** – assurance problem among peers.  
5. **Groundwater Extraction** – CPR tragedy of the commons.  

The non‑strategic **Social‑Learning** process links the games by altering the state (adoption counts) that feed into Game 4, but it does **not** constitute a simultaneous strategic interaction, satisfying the requirement to include a sequential process.

---

## Final Set of Distinct Action Situations  

| # | Title | Strategic? | Core Game Type |
|---|-------|------------|----------------|
| 1 | Enforcement vs Compliance | Yes | Trust / Enforcement (asymmetric) |
| 2 | Formal Connection Authorization | Yes | Authorization (asymmetric) |
| 3 | Informal Bribe ↔ Tolerance | Yes | Trust / Corruption (symmetric) |
| 4 | Capacitor Adoption Assurance | Yes | Coordination / Assurance (symmetric) |
| 5 | Groundwater Extraction Dilemma | Yes | Common‑Pool Resource (symmetric) |
| 6 | Observation → Imitation (Social Learning) | No | Sequential learning process |

These six action situations fully capture the governance interactions described in the ODD + D specification while respecting the requirement that each reflects a **different** strategic or procedural tension.
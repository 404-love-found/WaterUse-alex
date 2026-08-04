# Run 20 — openai/gpt-oss-120b

## Electricity‑Irrigation Governance – Action‑Situation Catalogue  
*(IAD‑framed, each situation is a distinct “governance interaction”.  Strategic games are shown as 2 × 2 normal‑form matrices with **ordinal** pay‑offs 0 = least‑preferred, 3 = most‑preferred.)*  

---

### 1. **Authorization Game**  
| Element | Description |
|---|---|
| **Title** | Formal‑Connection Authorization |
| **Location** | Sub‑station office (transformer‑service area) |
| **Players** | **Farmer F** (seeking a legal electricity connection) – **Utility‑Staff S** (authorizer) |
| **Roles** | F = electricity consumer / applicant; S = regulator‑enforcer / service‑provider |
| **Actions** | • **Farmer**: *Apply* for an authorised connection or *Remain Unauthorised*.<br>• **Staff**: *Approve* the application (grant connection) or *Reject* (keep informal status). |
| **Control Rules** | - If **Apply + Approve** → legal connection is created; farmer pays tariff & fee, staff records connection (cost to staff = paperwork & monitoring). <br>- **Apply + Reject** → farmer stays informal, pays informal “bribe” (if any) or no fee; staff avoids paperwork but may incur detection risk. <br>- **Remain Unauthorised** → status quo; no new fees; staff incurs no extra effort. |
| **Information** | Farmer knows his own budget, local voltage quality, and the historical probability of approval (estimated from past outcomes).  Staff knows the farmer’s payment capacity and the current monitoring intensity, but does **not** know the farmer’s willingness to pay a bribe.  Information is **partial & noisy**. |
| **Outcomes** | - Legal connection (recorded, tariff‑based revenue).<br>- Continued informal connection (no official revenue, possible illegal‑use sanction).<br>- Staff workload change (approval paperwork vs. monitoring). |
| **Payoffs** (ordinal) | See matrix below. |
| **Strategic Tension** | **Asymmetric Conflict / Authorization Game** – farmer wants approval, staff balances revenue vs. risk of corruption. |
| **Temporal Structure** | Repeated **annually** (once per decision‑year). |
| **Relevant Rules** | *Boundary rule*: only farmers attached to the transformer are eligible.<br>*Position rule*: staff assigned to that transformer can decide.<br>*Choice rule*: binary “Apply/Remain” and “Approve/Reject”.<br>*Control rule*: outcomes as described above. |

#### Normal‑Form (ordinal)  

|                     | **Staff – Approve** | **Staff – Reject** |
|---------------------|---------------------|--------------------|
| **Farmer – Apply**  | (F: 3, S: 2)        | (F: 1, S: 1)       |
| **Farmer – Remain** | (F: 0, S: 0)        | (F: 2, S: 3)       |

*Why these numbers?*  
- **Apply + Approve** gives the farmer a reliable, tariff‑based supply (top rank 3) and staff modest revenue plus compliance credit (rank 2).  
- **Apply + Reject** leaves farmer worse off (rank 1) and staff gains a small informal benefit but loses legitimacy (rank 1).  
- **Remain + Approve** is impossible (staff cannot approve a non‑applicant) → worst for farmer (0) and staff (0).  
- **Remain + Reject** leaves the status‑quo; farmer keeps cheap informal supply (rank 2) and staff avoids paperwork while keeping informal “rent” (rank 3).  

**Strategic core:** *asymmetric conflict* (similar to a “trust‑but‑verify” game).  

---

### 2. **Collusion Exchange Game**  
| Element | Description |
|---|---|
| **Title** | Informal Collusion Exchange |
| **Location** | Transformer‑service area (field visits, informal meetings) |
| **Players** | **Farmer F** – informal client; **Utility‑Staff S** – discretionary officer |
| **Roles** | F = service‑seeker; S = “gate‑keeper” who can provide favors (e.g., reduced fees, delayed shut‑offs). |
| **Actions** | • **Farmer**: *Offer Bribe* (pay informal “kick‑back”) or *Refuse*.<br>• **Staff**: *Accept* the bribe (grant lenient service) or *Reject* (enforce formal rules). |
| **Control Rules** | - **Offer + Accept** → farmer receives informal benefit (e.g., lower bill, delayed disconnection); staff receives illicit gain (cash) but incurs detection risk.<br>- Any other combination → no informal benefit; status‑quo (formal enforcement). |
| **Information** | Both know the local **risk of detection** (probability p) – common knowledge.  Farmer knows his own willingness to pay; staff knows his own corruption level.  Information is **partial** (exact detection probability is noisy). |
| **Outcomes** | - Informal benefit (lower cost, continued supply).<br>- Illicit gain for staff.<br>- Potential sanction if detection occurs (modeled as stochastic loss of rank). |
| **Payoffs** (ordinal) | See matrix below. |
| **Strategic Tension** | **Trust/Reciprocity (Collusion Exchange) Game** – each side must trust the other to honor the informal deal. |
| **Temporal Structure** | Repeated **annually** (once per decision‑year). |
| **Relevant Rules** | *Boundary*: only farmers with a prior tie to the staff are in the pool.<br>*Position*: staff assigned to the transformer.<br>*Choice*: binary “Offer/Refuse” and “Accept/Reject”.<br>*Control*: outcomes as above, plus stochastic detection. |

#### Normal‑Form (ordinal)  

|                     | **Staff – Accept** | **Staff – Reject** |
|---------------------|--------------------|--------------------|
| **Farmer – Offer**  | (F: 3, S: 2)       | (F: 0, S: 1)       |
| **Farmer – Refuse** | (F: 1, S: 0)       | (F: 2, S: 3)       |

*Explanation*  
- **Offer + Accept** gives farmer the best informal service (3) and staff a decent illicit gain (2).  
- **Offer + Reject** leaves farmer with a sanction‑risk (0) and staff with a small “wasted” effort (1).  
- **Refuse + Accept** cannot happen (staff cannot accept a non‑existent bribe) → farmer gets a modest formal service (1) while staff loses a potential gain (0).  
- **Refuse + Reject** keeps formal rules; farmer retains baseline service (2) and staff avoids risk (3).  

**Strategic core:** *trust/reciprocity* (a variant of the Trust Game).  

---

### 3. **Capacity‑Provision Public‑Goods Game**  
| Element | Description |
|---|---|
| **Title** | Transformer‑Capacity Contribution |
| **Location** | Village‑level transformer cluster |
| **Players** | **Farmer A** and **Farmer B** (any two farmers sharing the same transformer) |
| **Roles** | Both are **contributors** to a shared electrical infrastructure (capacity). |
| **Actions** | Each farmer chooses **Invest** (pay a one‑time fee to fund capacity upgrade) or **Free‑Ride** (pay nothing, hope others invest). |
| **Control Rules** | - If **both Invest** → capacity is upgraded; both enjoy higher voltage reliability (benefit shared).<br>- If **one Invest + one Free‑Ride** → upgrade still occurs (threshold met), investor bears full cost, free‑rider enjoys benefit without cost.<br>- If **both Free‑Ride** → no upgrade; voltage remains poor for both. |
| **Information** | Farmers observe the **historical investment rate** on their transformer but cannot know the current year’s decision of the counterpart before acting (simultaneous).  Information is **partial**. |
| **Outcomes** | - Upgraded transformer (higher reliability, lower pump‑breakdowns).<br>- Cost borne by investors (one‑time fee). |
| **Payoffs** (ordinal) | See matrix below. |
| **Strategic Tension** | **Public‑Goods / Coordination Game** – each farmer benefits from the upgrade but prefers the other to pay. |
| **Temporal Structure** | Repeated **annually** (each year a new coordination round). |
| **Relevant Rules** | *Boundary*: only farmers attached to the same transformer interact.<br>*Choice*: binary “Invest/Free‑Ride”.<br>*Control*: upgrade occurs if at least one invests (threshold τ = 1). |

#### Normal‑Form (ordinal)  

|                     | **Farmer B – Invest** | **Farmer B – Free‑Ride** |
|---------------------|-----------------------|--------------------------|
| **Farmer A – Invest**   | (A: 2, B: 2)            | (A: 1, B: 3)               |
| **Farmer A – Free‑Ride**| (A: 3, B: 1)            | (A: 0, B: 0)               |

*Explanation*  
- **Both Invest**: each pays cost (rank 2) but gets reliable power (rank 2). <br>- **A Invest + B Free‑Ride**: A bears cost → lower rank 1; B enjoys benefit free → rank 3. <br>- **Both Free‑Ride**: no upgrade → worst outcome for both (0).  

**Strategic core:** *public‑goods dilemma* (asymmetric payoff because the free‑rider gets the highest rank).  

---

### 4. **Groundwater Extraction Common‑Pool Resource (CPR) Game**  
| Element | Description |
|---|---|
| **Title** | Shared‑Aquifer Extraction |
| **Location** | Groundwater basin underlying a cluster of farms (same transformer area) |
| **Players** | **Farmer A** and **Farmer B** (two neighboring pump owners) |
| **Roles** | Both are **extractors** of a common water stock. |
| **Actions** | Each chooses **Extract High** (pump at full rate) or **Extract Low** (restrain extraction). |
| **Control Rules** | - The **aquifer draw‑down** each month equals the sum of extractions.<br>- If total extraction exceeds a **sustainable threshold** (θ), future water tables fall, raising energy‑cost per unit water (penalty).<br>- A **per‑unit tax** may be imposed on high extractors (exogenous). |
| **Information** | Farmers know the **current water table depth** (noisy) and the **average past extraction** of neighbours, but not the exact current decision of the counterpart. |
| **Outcomes** | - Immediate water volume obtained (higher for “High”).<br>- Future cost increase if over‑extraction occurs (affects both). |
| **Payoffs** (ordinal) | See matrix below. |
| **Strategic Tension** | **Common‑Pool Resource (Tragedy‑of‑the‑Commons) Game** – each prefers high extraction, but mutual over‑use harms both. |
| **Temporal Structure** | Repeated **monthly** within each simulated year (but strategic decision is made **annually** and held for the year). |
| **Relevant Rules** | *Boundary*: all farmers drawing from the same aquifer interact.<br>*Choice*: binary “High/Low”.<br>*Control*: sustainability threshold determines future degradation. |

#### Normal‑Form (ordinal)  

|                     | **Farmer B – Extract High** | **Farmer B – Extract Low** |
|---------------------|-----------------------------|----------------------------|
| **Farmer A – Extract High** | (A: 1, B: 1)                | (A: 2, B: 3)               |
| **Farmer A – Extract Low**  | (A: 3, B: 2)                | (A: 2, B: 2)               |

*Explanation*  
- **Both High**: short‑term water gain but triggers over‑draw → both rank low (1).  
- **A High + B Low**: A gets high immediate water (rank 2) while B enjoys lower cost and avoids future penalty (rank 3).  
- **A Low + B High** symmetric.  
- **Both Low**: moderate water for both, sustainability preserved → middle rank (2) for each.  

**Strategic core:** *CPR dilemma* (asymmetric payoffs reflect the advantage of being the sole high extractor).  

---

### 5. **Trust Game (Farmer‑Staff Service Trust)**  
| Element | Description |
|---|---|
| **Title** | Trust in Service Reliability |
| **Location** | Sub‑station / field interaction point |
| **Players** | **Farmer F** (trustor) – pays a **pre‑payment** for guaranteed voltage quality; **Utility‑Staff S** (trustee) – decides whether to honour the promise. |
| **Roles** | F = client who can **trust** staff with a pre‑payment; S = provider who can **keep** the promise or **defect** (keep money, provide low‑quality service). |
| **Actions** | • **Farmer**: *Pre‑pay* (deposit a lump‑sum) or *Not Pre‑pay*.<br>• **Staff**: *Honour* (maintain voltage, invest in maintenance) or *Defect* (use the money but neglect service). |
| **Control Rules** | - **Pre‑pay + Honour** → farmer receives high‑quality electricity for the year; staff gains reputation (rank 2) and a modest fee (rank 2).<br>- **Pre‑pay + Defect** → farmer gets poor service (rank 0) while staff pockets money (rank 3).<br>- **No Pre‑pay + Honour** → baseline service (rank 1 for farmer, rank 1 for staff).<br>- **No Pre‑pay + Defect** → same baseline (no extra loss) (farmer 1, staff 0). |
| **Information** | Farmer knows the **historical reliability** of staff (noisy estimate). Staff knows the **size of the pre‑payment** and the **monitoring intensity** (probability of external audit). Both have **partial** information. |
| **Outcomes** | - Service quality (high vs. low).<br>- Financial transfer (pre‑payment retained or returned).<br>- Reputation change for staff (affects future enforcement). |
| **Payoffs** (ordinal) | See matrix below. |
| **Strategic Tension** | **Trust Game** – farmer must decide whether to trust staff; staff decides whether to reciprocate. |
| **Temporal Structure** | One‑shot **annual** decision (pre‑payment made at start of irrigation season). |
| **Relevant Rules** | *Boundary*: only farmers with a standing relationship to the staff may pre‑pay.<br>*Choice*: binary “Pre‑pay/Not” and “Honour/Defect”.<br>*Control*: outcomes as listed; external audit adds stochastic penalty (modelled implicitly). |

#### Normal‑Form (ordinal)  

|                     | **Staff – Honour** | **Staff – Defect** |
|---------------------|--------------------|--------------------|
| **Farmer – Pre‑pay**| (F: 3, S: 2)       | (F: 0, S: 3)       |
| **Farmer – Not**   | (F: 1, S: 1)       | (F: 1, S: 0)       |

*Why these ranks?*  
- **Pre‑pay + Honour** gives farmer the best reliable service (3) and staff a decent reputation gain (2).  
- **Pre‑pay + Defect** gives staff the highest illicit gain (3) while farmer is left with the worst service (0).  
- **No Pre‑pay + Honour** yields modest baseline service (1) and modest reputation (1).  
- **No Pre‑pay + Defect** leaves staff with no extra gain (0) and farmer unchanged (1).  

**Strategic core:** *trust* (asymmetric payoff, classic trust‑game structure).  

---

### 6. **Social‑Learning / Observation Process** *(Non‑strategic)*  
| Element | Description |
|---|---|
| **Title** | Observation & Imitation of DSM Adoption |
| **Location** | Transformer service area (farmers observe neighbours) |
| **Players** | **Individual farmer** (decision‑maker) – no direct opponent |
| **Roles** | Learner / observer |
| **Actions** | *Observe* neighbours’ capacitor/DSM outcomes (success or failure) → *Update* internal belief about adoption payoff; *Imitate* with a fixed probability **ι** if enough neighbours have succeeded. |
| **Control Rules** | - Observation is **sequential**: first the adoption pool runs, then outcomes are recorded.<br>- If the number of successful adopters on the transformer exceeds a threshold **τ**, the farmer’s imitation probability rises to **ι** (e.g., 0.4). |
| **Information** | Farmer sees **visible outcomes** (whether neighbours have installed capacitors and whether their pumps burnt out).  Perception of *why* the outcome occurred is **noisy** (misattribution). |
| **Outcomes** | Updated propensity to adopt DSM in the next annual decision round. |
| **Payoffs** | Not modelled as explicit utility; learning influences future strategic payoffs (e.g., higher probability of a successful adoption). |
| **Strategic Tension** | **Non‑strategic** – no simultaneous choice; the tension is between *learning speed* and *misinformation*. |
| **Temporal Structure** | Occurs **monthly** after the physical update, feeding into the **annual** decision stage. |
| **Relevant Rules** | *Boundary*: only farmers on the same transformer are observable.<br>*Position*: none (individual).<br>*Choice*: “Observe → Update → Possibly Imitate”.<br>*Control*: threshold‑based increase in imitation probability. |

---

## Comparative Analysis of the Strategic Core

| Situation | Game Type (per list) | Core Dilemma | Symmetry | Primary Asymmetry |
|-----------|----------------------|--------------|----------|-------------------|
| 1 – Authorization | **Asymmetric Conflict** | Farmer wants approval; staff balances revenue vs. risk. | Asymmetric (different action sets). |
| 2 – Collusion Exchange | **Trust/Reciprocity** | Both need mutual cooperation; risk of defection. | Asymmetric (bribe vs. acceptance). |
| 3 – Capacity‑Provision | **Public‑Goods / Coordination** | Free‑riding vs. joint investment. | Symmetric actions, asymmetric payoffs (free‑rider gets highest rank). |
| 4 – Groundwater Extraction | **CPR (Tragedy of the Commons)** | Over‑extraction harms all; incentive to restrain. | Symmetric actions, asymmetric payoffs (solo high extractor best). |
| 5 – Trust Game (Service) | **Trust Game** | Farmer’s pre‑payment vs. staff’s honesty. | Asymmetric (trustor vs. trustee). |
| 6 – Social‑Learning | Non‑strategic | – | – | – |

### Redundancy Check
- Situations **3** (Capacity‑Provision) and **5** (Trust Game) both involve farmer‑staff interactions, but **3** is a *public‑goods* dilemma about **infrastructure investment**, whereas **5** is a *trust* dilemma about **service reliability after a pre‑payment**. Their payoff structures and institutional logic differ markedly, so they are retained.
- Situations **2** (Collusion Exchange) and **5** (Trust) both involve trust, yet **2** focuses on **informal bribery** (mutual exchange) while **5** concerns **formal pre‑payment for quality**. Both are kept because the underlying institutional mechanisms (informal vs. formal) are distinct.
- Situations **3** and **4** are both coordination‑type games, but **3** is a **public‑goods** (capacity) problem, while **4** is a **common‑pool resource** (groundwater) problem; the resource type and externalities differ, so they are distinct.

**Result:** The set already exhibits sufficient strategic diversity (five different game families). No further replacement is required.

---

## Full Set of Distinct Action Situations (Final)

1. **Authorization Game** – farmer vs. staff decision on formal connection.  
2. **Collusion Exchange Game** – farmer vs. staff informal bribe/leniency exchange.  
3. **Capacity‑Provision Public‑Goods Game** – farmer vs. farmer contribution to transformer upgrades.  
4. **Groundwater Extraction CPR Game** – farmer vs. farmer extraction choices on a shared aquifer.  
5. **Trust Game (Service Trust)** – farmer pre‑payment vs. staff honouring service quality.  
6. **Social‑Learning / Observation Process** – non‑strategic sequential learning of DSM adoption.

Each situation is described above with the full IAD specification and, for the five strategic interactions, an explicit 2 × 2 ordinal payoff matrix. This catalogue captures **all** governance interactions embedded in the ODD+D model while guaranteeing that each interaction presents a **unique strategic tension** relevant to electricity‑irrigation governance in Andhra Pradesh.
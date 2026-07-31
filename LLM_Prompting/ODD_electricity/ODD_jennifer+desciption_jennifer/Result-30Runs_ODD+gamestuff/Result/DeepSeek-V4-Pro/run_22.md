# Run 22 — deepseek-ai/DeepSeek-V4-Pro

### 1. DSM Coordination Game  
**Title:** Capacitor Adoption Assurance Game  
**Location:** Village-level transformer service area  
**Players:** Two representative farmers sharing the same transformer (Farmer A, Farmer B)  
**Roles:** Electricity consumers who can invest in demand‑side management  
**Actions:**  
- Farmer A: **Adopt** a capacitor / voltage‑stabilising equipment, or **Not Adopt**  
- Farmer B: **Adopt** or **Not Adopt**  
**Control Rules:**  
- If both adopt, the transformer’s voltage stability improves markedly, lowering pump burn‑outs and raising effective pumping hours.  
- If only one adopts, the local voltage improvement is negligible and the adopter bears the full equipment cost with no observable benefit.  
- If neither adopts, the status‑quo (moderate reliability) persists.  
**Information:** Farmers observe neighbours’ past adoption choices and the resulting voltage quality, but cannot perfectly foresee the other’s current‑year decision. Sensing is local and may misattribute voltage changes.  
**Outcomes:**  
- (Adopt, Adopt) → improved voltage stability, lower motor burn‑outs, net benefit after cost.  
- (Adopt, Not) → adopter pays cost, no reliability gain; non‑adopter keeps status‑quo.  
- (Not, Adopt) → symmetric.  
- (Not, Not) → status‑quo reliability.  
**Payoffs:** Ordinal preference ranks (3 = best, 0 = worst)  
- Mutual adoption: (3,3) – best collective outcome, cost shared, high reliability.  
- Unilateral adoption: adopter 0 (cost, no benefit), non‑adopter 2 (status‑quo).  
- Mutual non‑adoption: (2,2) – moderate reliability, no extra cost.  

**Strategic Tension:** Assurance game (Stag Hunt). Both farmers prefer to adopt only if the other also adopts; otherwise they prefer to stay out. This creates a coordination problem where a critical mass of simultaneous adopters is needed to unlock the shared benefit.  
**Temporal Structure:** Repeated annually; adoption decision is made once per year.  
**Relevant Rules:** Choice rules allow investment in capacitors; boundary rules group farmers by transformer; information rules permit observation of neighbours’ visible adoption.  

**Normal‑form game**  
Players: Farmer A (row), Farmer B (col)  
Actions: A = Adopt, N = Not adopt  

|       | A     | N     |
|-------|-------|-------|
| **A** | 3,3   | 0,2   |
| **N** | 2,0   | 2,2   |

---

### 2. Capacity Provision Game  
**Title:** Transformer Capacity Contribution Dilemma  
**Location:** Shared transformer group  
**Players:** Two farmers connected to the same transformer (Farmer 1, Farmer 2)  
**Roles:** Potential contributors to shared electricity infrastructure  
**Actions:**  
- Each farmer chooses to **Contribute** (pay for authorised capacity upgrade) or **Free‑ride** (withhold contribution).  
**Control Rules:**  
- If both contribute, transformer capacity expands, voltage quality improves for all.  
- If only one contributes, the upgrade still occurs (or is partially effective) – the contributor bears the full private cost while the free‑rider enjoys the improved reliability without paying.  
- If neither contributes, capacity remains inadequate, reliability stays low.  
**Information:** Farmers know past contributions and current reliability, but cannot perfectly predict the other’s current choice.  
**Outcomes:**  
- (Contribute, Contribute) → high reliability, cost shared.  
- (Contribute, Free‑ride) → contributor pays, gets some benefit; free‑rider gets full benefit without cost.  
- (Free‑ride, Contribute) → symmetric.  
- (Free‑ride, Free‑ride) → low reliability, no extra cost.  
**Payoffs (ordinal):**  
- Mutual contribution: (3,3) – best collective outcome.  
- Unilateral contribution: contributor 1 (costly, partial benefit), free‑rider 3 (full benefit, no cost).  
- Mutual free‑riding: (1,1) – poor reliability.  

**Strategic Tension:** Prisoner’s Dilemma. Free‑riding is a dominant strategy, leading to the collectively inferior outcome (1,1) even though (3,3) is Pareto‑superior.  
**Temporal Structure:** Repeated annually; contribution decisions made once per year.  
**Relevant Rules:** Choice rules permit voluntary financial contribution to transformer capacity; boundary rules define the transformer group.  

**Normal‑form game**  
Players: Farmer 1 (row), Farmer 2 (col)  
Actions: C = Contribute, F = Free‑ride  

|       | C     | F     |
|-------|-------|-------|
| **C** | 3,3   | 1,3   |
| **F** | 3,1   | 1,1   |

---

### 3. Groundwater Extraction Game  
**Title:** Shared Aquifer Extraction Dilemma  
**Location:** District‑level groundwater basin, accessed by farmers on neighbouring wells  
**Players:** Two representative farmers pumping from the same aquifer (Farmer X, Farmer Y)  
**Roles:** Groundwater users  
**Actions:**  
- Each farmer chooses a pumping rate: **Restrain** (limit extraction) or **Full** (extract at maximum feasible rate).  
**Control Rules:**  
- If both restrain, the water table declines slowly, keeping pumping energy costs manageable.  
- If one restrains and the other extracts fully, the full extractor gains high short‑term irrigation benefit; the restrainer still suffers some depletion and higher pumping cost but avoids the worst collapse.  
- If both extract fully, the aquifer is rapidly depleted, pumping costs soar, and both face severe water shortages.  
**Information:** Farmers sense groundwater depth, pumping costs, and neighbour’s past extraction behaviour, but cannot perfectly observe the current choice.  
**Outcomes:**  
- (Restrain, Restrain) → sustainable water table, moderate pumping costs.  
- (Restrain, Full) → restrainer gets reduced water and rising costs; full extractor gets high short‑term yield.  
- (Full, Restrain) → symmetric.  
- (Full, Full) → severe depletion, very high pumping costs, crop failure risk.  
**Payoffs (ordinal):**  
- Mutual restraint: (2,2) – sustainable, acceptable cost.  
- Unilateral full extraction: full extractor 3 (high gain), restrainer 1 (some depletion, lower extraction).  
- Mutual full extraction: (0,0) – worst outcome, resource collapse.  

**Strategic Tension:** Chicken (Hawk‑Dove). No dominant strategy; each farmer prefers to be the sole full extractor while the other restrains, but mutual full extraction is disastrous. Two asymmetric pure‑strategy equilibria exist: (Restrain, Full) and (Full, Restrain).  
**Temporal Structure:** Repeated annually; extraction decision made each irrigation cycle.  
**Relevant Rules:** Choice rules allow selection of pumping rate; the aquifer is a common‑pool resource with no formal allocation rule.  

**Normal‑form game**  
Players: Farmer X (row), Farmer Y (col)  
Actions: R = Restrain, F = Full extraction  

|       | R     | F     |
|-------|-------|-------|
| **R** | 2,2   | 1,3   |
| **F** | 3,1   | 0,0   |

---

### 4. Authorization Game  
**Title:** Formal Connection and Service Provision Coordination  
**Location:** Transformer group and local sub‑station  
**Players:** One farmer (F) and one sub‑station staff member (S)  
**Roles:**  
- Farmer: electricity consumer seeking connection  
- Staff: service provider with discretionary enforcement and investment power  
**Actions:**  
- Farmer: **Authorize** (apply and pay for a formal, metered connection) or **Not Authorize** (remain informal, risk penalty).  
- Staff: **Invest** (provide capacity, maintain records, enforce formal rules) or **Not Invest** (withhold effort, tolerate informal connections).  
**Control Rules:**  
- If the farmer authorizes and the staff invests, the farmer receives reliable, legal service; staff gains compliance and avoids blame.  
- If the farmer authorizes but the staff does not invest, the farmer pays the fee but gets poor service (staff withholds maintenance); staff saves effort but faces reputational risk.  
- If the farmer does not authorize but the staff invests, the farmer free‑rides on improved reliability without paying; staff bears the cost of investment without formal compliance, leading to frustration and wasted effort.  
- If neither authorizes nor invests, informal tolerance prevails: farmer gets some service with risk of penalty, staff saves effort but may suffer if failures occur.  
**Information:** Both players know the history of service quality and the other’s past behaviour. The farmer cannot be sure whether staff will invest; staff cannot be sure whether the farmer will authorize.  
**Outcomes:**  
- (Authorize, Invest) → formal, reliable connection.  
- (Authorize, Not Invest) → farmer pays, poor service.  
- (Not Authorize, Invest) → free‑ride on investment, staff effort wasted.  
- (Not Authorize, Not Invest) → informal, mediocre reliability.  
**Payoffs (ordinal):**  
- (Authorize, Invest): F = 3, S = 3 – best for both.  
- (Authorize, Not Invest): F = 0, S = 1 – farmer loses, staff avoids effort but risks blame.  
- (Not Authorize, Invest): F = 2, S = 0 – farmer benefits, staff loses.  
- (Not Authorize, Not Invest): F = 1, S = 2 – stable informal equilibrium.  

**Strategic Tension:** Asymmetric coordination (Assurance) game. Two pure‑strategy Nash equilibria: (Authorize, Invest) and (Not Authorize, Not Invest). The formal equilibrium Pareto‑dominates the informal one, but misaligned expectations can lock the system into the inferior informal outcome.  
**Temporal Structure:** Repeated annually; decisions made at the start of each irrigation cycle.  
**Relevant Rules:** Boundary rules define who is a farmer and who is staff; choice rules allow authorization and investment; control rules link joint actions to service outcomes.  

**Normal‑form game**  
Players: Farmer (row), Staff (col)  
Actions: A = Authorize, N = Not Authorize; I = Invest, NI = Not Invest  

|       | I     | NI    |
|-------|-------|-------|
| **A** | 3,3   | 0,1   |
| **N** | 2,0   | 1,2   |

---

### 5. Collusion Exchange Game  
**Title:** Informal Staff‑Farmer Trust Game  
**Location:** Local transformer area and sub‑station office  
**Players:** One farmer (F) and one sub‑station staff member (S) with an existing social tie  
**Roles:**  
- Farmer: potential initiator of informal cooperation  
- Staff: potential recipient who can reciprocate or reject  
**Actions:**  
- Farmer (first mover): **Offer Collusion** (propose informal exchange, e.g., side payment for unauthorised tolerance) or **Not Offer**.  
- Staff (second mover, after observing offer): if offered, **Accept** (reciprocate and provide informal favours) or **Reject** (refuse and potentially report).  
**Control Rules:**  
- If the farmer offers and the staff accepts, both gain from the informal exchange (cheaper access for farmer, side benefit for staff) while assuming a shared risk of detection.  
- If the farmer offers but the staff rejects, the farmer’s offer is wasted and may expose the farmer to risk; the staff maintains the formal status quo.  
- If the farmer does not offer, no collusion occurs and both receive the formal status‑quo payoff regardless of staff’s contingent choice.  
**Information:** The farmer knows the staff’s general reputation and past collusion density; the staff knows the farmer’s financial strain and capacity to reciprocate. Both are uncertain about detection probability.  
**Outcomes:**  
- (Offer, Accept) → mutual informal benefit, higher payoff but detection risk.  
- (Offer, Reject) → farmer loses, staff keeps status quo.  
- (Not Offer, Accept/Reject) → status quo formal interaction.  
**Payoffs (ordinal):**  
- (Offer, Accept): F = 3, S = 3 – best mutual outcome.  
- (Offer, Reject): F = 0, S = 2 – farmer bears cost/risk, staff safe.  
- (Not Offer, either): F = 2, S = 2 – formal status quo.  

**Strategic Tension:** Trust game (sequential). The farmer must decide whether to trust the staff; the staff, if trusted, has a material incentive to reciprocate (3 > 2), but the farmer risks a sucker’s payoff if trust is betrayed. The unique subgame‑perfect equilibrium is (Not Offer, Reject if offered), yielding (2,2), yet the Pareto‑superior (Offer, Accept) is attainable only if trust is established.  
**Temporal Structure:** Repeated annually; collusion‑tie formation occurs once per year.  
**Relevant Rules:** Informal norms and reciprocity expectations act as choice rules; detection risk is a control rule parameter.  

**Normal‑form representation (reduced strategies)**  
Players: Farmer (row), Staff (col)  
Farmer strategies: O = Offer, NO = Not Offer  
Staff strategies: A = Accept if offered, R = Reject if offered  

|       | A     | R     |
|-------|-------|-------|
| **O** | 3,3   | 0,2   |
| **NO**| 2,2   | 2,2   |

---

### 6. Social Learning Process  
**Title:** Observational Learning and Imitation of Technology Adoption  
**Location:** Local social network within a transformer service area  
**Players:** Individual farmers (learners) and their neighbours (exemplars)  
**Roles:**  
- Learner: farmer updating adoption propensity  
- Exemplar: neighbour whose visible outcome is observed  
**Actions:**  
- The learner **observes** neighbours’ capacitor adoption status and the resulting service quality (voltage stability, pump performance, repair delays).  
- Based on observation, the learner **imitates** successful adopters with a probability that increases with the number of visibly successful peers.  
- The learner may also become an **experimenter** with a small fixed probability, adopting independently of neighbourhood outcomes.  
**Control Rules:**  
- Imitation is triggered only when a transformer’s adoption count has jumped by a threshold within a single cycle, opening the wider imitation pool.  
- Adoption cost is paid at most once per farmer; failed early adoption can discourage later imitation.  
**Information:** Farmers perceive neighbours’ adoption and performance without error regarding the act of adoption, but may misattribute the causes of voltage improvements or failures (noisy causal inference).  
**Outcomes:**  
- Adoption probability updates for each farmer.  
- Diffusion patterns emerge: rapid spread if early coordinated adoption is successful, or lock‑in of non‑adoption if early attempts fail.  
**Payoffs:** Not applicable as a strategic game; the process alters future adoption states and indirectly affects payoffs in the DSM Coordination Game.  
**Strategic Tension:** Non‑strategic sequential process. No simultaneous interdependent choice; instead, farmers update behaviour based on observed history.  
**Temporal Structure:** Occurs annually after outcomes of the irrigation cycle are realised.  
**Relevant Rules:** Information rules allow observation of neighbours; choice rules define imitation probabilities; the threshold for opening the imitation pool acts as a control rule.  

---

### Strategic Core Analysis and Diversity Check  
- **DSM Coordination Game:** Assurance (Stag Hunt) – symmetric, coordination dilemma.  
- **Capacity Provision Game:** Prisoner’s Dilemma – symmetric, free‑rider dilemma.  
- **Groundwater Extraction Game:** Chicken (Hawk‑Dove) – symmetric, conflict over resource use with mutual disaster.  
- **Authorization Game:** Asymmetric coordination (Assurance) between farmer and staff – two equilibria, one Pareto‑dominant.  
- **Collusion Exchange Game:** Trust game – sequential, asymmetric, trust‑based dilemma.  
- **Social Learning Process:** Non‑strategic, observational updating.  

No two strategic situations share the same incentive structure. The farmer‑only games span three distinct social dilemmas (assurance, PD, chicken). The farmer‑staff games are differentiated: one is a simultaneous coordination game over formal compliance, the other a sequential trust game over informal exchange. This set captures the full range of governance interactions described in the ODD+D while maintaining strategic diversity.
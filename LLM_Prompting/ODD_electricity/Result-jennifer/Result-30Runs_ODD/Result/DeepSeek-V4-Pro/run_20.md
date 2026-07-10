# Run 20 — deepseek-ai/DeepSeek-V4-Pro

### Action Situation 1: DSM Adoption Coordination  
**Non‑strategic precursor: Social learning (see Action Situation 7) informs farmers’ expectations before this strategic choice.**

| IAD Element | Description |
|-------------|-------------|
| **1. Title** | DSM (Capacitor) Adoption Coordination |
| **2. Location** | Transformer service area – a group of farmers sharing the same distribution transformer. |
| **3. Players** | Two farmers from the same transformer group (the game is played pairwise among all eligible farmers). |
| **4. Roles** | Potential adopters of demand‑side management (DSM) equipment. |
| **5. Actions** | Each farmer chooses **Invest** (buy and install a capacitor/ISI‑marked pumpset) or **Not Invest**. |
| **6. Control Rules** | If **both** invest in the same cycle, the shared benefit (improved voltage quality, reduced motor burnout) materialises. If only one invests, the adopter pays the full cost but receives no reliability gain because the threshold number of adopters is not reached. Investment cost is paid at most once per farmer. |
| **7. Information** | Farmers observe past adoption rates on their transformer and the outcomes (voltage quality, burnout frequency) experienced by neighbours. They do not know the simultaneous choice of the other player, but they share the common knowledge that the benefit requires a minimum number of simultaneous investments. |
| **8. Outcomes** | Transformer‑level voltage quality either improves (both invest) or stays degraded (any other combination). Individual budgets change by the cost of investment if chosen. |
| **9. Payoffs** | See payoff matrix below. |
| **10. Strategic Tension** | **Strategic – Assurance game (Stag Hunt).** Both farmers prefer mutual investment (highest collective payoff) but fear being the only one to pay the cost without receiving the benefit. The safe option is mutual non‑investment, which yields a moderate status‑quo payoff. |
| **11. Temporal Structure** | Repeated annually; farmers are drawn into the adoption pool each year. |
| **12. Relevant Rules** | Choice rule: farmers may invest only if they are in the adoption pool (experimenters or imitators on a transformer where a threshold jump has been observed). Boundary rule: only farmers on the same transformer participate in a given round. |

**Normal‑form game (ordinal payoffs 0–3, 3 = most preferred)**  

| Farmer A / Farmer B | Invest | Not Invest |
|---------------------|--------|------------|
| **Invest**          | 3 , 3  | 0 , 1      |
| **Not Invest**      | 1 , 0  | 2 , 2      |

*Explanation*:  
- (Invest, Invest): both pay the cost, reliability improves → best outcome for both (3,3).  
- (Invest, Not Invest): investor bears cost with no benefit (0), non‑investor keeps status quo but may suffer slightly from continued poor quality (1).  
- (Not Invest, Invest): symmetric.  
- (Not Invest, Not Invest): no cost, no improvement, status quo (2,2).  

---

### Action Situation 2: Connection Authorization  
**Players: Disconnected farmer and substation staff. The farmer needs a new electricity connection; the staff controls whether service is provided and in what form.**

| IAD Element | Description |
|-------------|-------------|
| **1. Title** | Connection Authorization Game |
| **2. Location** | Transformer level, involving the local substation staff responsible for that transformer. |
| **3. Players** | One disconnected farmer, one substation staff member (the staff member assigned to the farmer’s transformer, possibly with an existing tie). |
| **4. Roles** | Farmer: connection seeker. Staff: service provider / gatekeeper. |
| **5. Actions** | Farmer chooses **Formal** (apply for a paid, authorised connection) or **Informal** (seek an informal connection without full fees). Staff chooses **Formal** (invest in providing a formal connection) or **Informal** (provide capacity through informal channels). |
| **6. Control Rules** | If both choose the same channel, a connection is established under that regime. If they choose different channels, no connection is made (the farmer remains disconnected and may lose any application fee). |
| **7. Information** | Both know the local density of collusion, the farmer’s financial strain, and the staff’s workload. They do not observe the other’s simultaneous choice. |
| **8. Outcomes** | A new connection is created (formal or informal) or the farmer stays disconnected. Transformer capacity may be augmented if staff invests. |
| **9. Payoffs** | See payoff matrix. |
| **10. Strategic Tension** | **Strategic – Battle of the Sexes.** Both players want to coordinate on the same connection type, but they have opposite preferences: the farmer prefers the cheaper informal route, while the staff prefers the formal route (legitimacy, official recognition). Failure to coordinate leaves both worse off. |
| **11. Temporal Structure** | Played once per farmer when seeking a new connection; may be repeated if the farmer reapplies in later years. |
| **12. Relevant Rules** | Boundary rule: only disconnected farmers with a tie to staff are eligible for informal capacity; untied farmers can only choose Formal. Choice rule: staff’s willingness to provide informal capacity depends on workload and detection risk. |

**Normal‑form game**  

| Farmer / Staff | Formal (staff) | Informal (staff) |
|----------------|----------------|------------------|
| **Formal**     | 2 , 3          | 0 , 0            |
| **Informal**   | 0 , 0          | 3 , 2            |

*Explanation*:  
- (Formal, Formal): farmer gets authorised connection, pays fee → moderate payoff (2); staff gains formal credit, fulfills duty → best for staff (3).  
- (Informal, Informal): farmer gets connection without full fee → best for farmer (3); staff receives informal payment/favour → good but less preferred than formal (2).  
- Mismatch: no connection, farmer loses fee or remains disconnected (0), staff wastes effort or faces complaint (0).  

---

### Action Situation 3: Collusion Tie Formation  
**Players: A farmer and a matched substation staff member decide whether to enter a collusive relationship.**

| IAD Element | Description |
|-------------|-------------|
| **1. Title** | Collusion Exchange Game |
| **2. Location** | Transformer level; the interaction is embedded in ongoing social networks. |
| **3. Players** | One farmer and one substation staff member (matched annually; existing ties persist). |
| **4. Roles** | Farmer: potential bribe‑giver / favour‑recipient. Staff: potential bribe‑taker / favour‑provider. |
| **5. Actions** | Farmer: **Offer collusion** or **Not offer**. Staff: **Accept collusion** or **Reject**. |
| **6. Control Rules** | A collusive tie forms **only if** the farmer offers **and** the staff accepts. If the farmer offers and the staff rejects, the staff may report the attempt (risk of penalty for farmer). If the farmer does not offer, no tie forms regardless of staff’s willingness. |
| **7. Information** | Each knows the other’s general reputation, the local risk of detection, and their own financial/corruption propensity. They do not know the other’s simultaneous choice. |
| **8. Outcomes** | A collusive tie is either created (enabling future informal exchanges) or not. If the farmer offers and is rejected, the farmer may suffer a penalty. |
| **9. Payoffs** | See payoff matrix. |
| **10. Strategic Tension** | **Strategic – Coordination game with asymmetric risk (similar to Stag Hunt but with unequal off‑diagonal payoffs).** Both prefer mutual collusion (highest joint payoff) but fear being exploited. Mutual non‑collusion is a safe fallback. The risk is asymmetric: the farmer loses more if offering alone, while the staff gains a small reward for rejecting. |
| **11. Temporal Structure** | Repeated annually; existing ties can be maintained or dissolved. |
| **12. Relevant Rules** | Boundary rule: farmer and staff are matched based on transformer assignment and existing ties. Choice rule: willingness depends on corruption level, financial strain, and detection risk. |

**Normal‑form game**  

| Farmer / Staff | Accept | Reject |
|----------------|--------|--------|
| **Offer**      | 3 , 3  | 0 , 1  |
| **Not offer**  | 1 , 0  | 1 , 1  |

*Explanation*:  
- (Offer, Accept): collusion formed → mutual benefit (3,3).  
- (Offer, Reject): farmer exposed, penalised (0); staff gains reward for honesty (1).  
- (Not offer, Accept): staff willing but no offer → staff frustrated (0); farmer safe (1).  
- (Not offer, Reject): status quo, no collusion → both safe (1,1).  

---

### Action Situation 4: Transformer Capacity Investment  
**Players: A tied farmer (either disconnected awaiting capacity or a connected free‑rider) and the substation staff member who can invest in shared transformer capacity.**

| IAD Element | Description |
|-------------|-------------|
| **1. Title** | Transformer Capacity Investment Game |
| **2. Location** | Transformer level; the capacity upgrade benefits all farmers on that transformer. |
| **3. Players** | One tied farmer and one substation staff member. |
| **4. Roles** | Farmer: potential beneficiary / cost‑sharer. Staff: investor / capacity provider. |
| **5. Actions** | Staff: **Invest** (allocate resources to upgrade transformer capacity) or **Not invest**. Farmer: **Cooperate** (contribute to the cost or accept formal regularisation) or **Free‑ride** (withhold contribution). |
| **6. Control Rules** | If the staff invests and the farmer cooperates, capacity is upgraded and reliability improves for all. If the staff invests but the farmer free‑rides, the staff bears the full cost while the farmer enjoys the benefit. If the staff does not invest, no upgrade occurs; cooperating farmer wastes any preparatory effort. |
| **7. Information** | Both know the staff’s workload and the farmer’s willingness to pay. They do not know the other’s simultaneous choice. |
| **8. Outcomes** | Transformer capacity either increases (improving voltage quality and reducing burnout risk) or stays the same. Individual payoffs reflect costs borne and benefits received. |
| **9. Payoffs** | See payoff matrix. |
| **10. Strategic Tension** | **Strategic – Asymmetric Prisoner’s Dilemma (public goods provision).** The farmer has a dominant strategy to free‑ride, because free‑riding yields a higher payoff regardless of the staff’s action. The staff, anticipating free‑riding, will not invest. The unique equilibrium (Not invest, Free‑ride) is Pareto‑inferior to mutual cooperation. |
| **11. Temporal Structure** | Played when a tied farmer needs capacity; may be repeated if the farmer remains in the pool. |
| **12. Relevant Rules** | Boundary rule: only tied farmers (disconnected with a tie, or connected free‑riders offered regularisation) participate. Choice rule: staff’s willingness to invest declines with workload; farmer’s willingness to cooperate is independent and generally low. |

**Normal‑form game**  

| Staff / Farmer | Cooperate | Free‑ride |
|----------------|-----------|-----------|
| **Invest**     | 2 , 2     | 0 , 3     |
| **Not invest** | 1 , 0     | 1 , 1     |

*Explanation*:  
- (Invest, Cooperate): capacity upgraded, both benefit → (2,2).  
- (Invest, Free‑ride): staff bears cost alone, farmer gets benefit without paying → staff worst (0), farmer best (3).  
- (Not invest, Cooperate): farmer wastes effort, staff saves effort → staff (1), farmer (0).  
- (Not invest, Free‑ride): no upgrade, status quo → (1,1).  

---

### Action Situation 5: Groundwater Extraction  
**Players: Two connected farmers sharing an aquifer. Extraction decisions affect the common groundwater resource and future pumping costs.**

| IAD Element | Description |
|-------------|-------------|
| **1. Title** | Groundwater Extraction Game |
| **2. Location** | Shared aquifer underlying the transformer service area. |
| **3. Players** | Two farmers from the same transformer group (paired annually). |
| **4. Roles** | Groundwater users. |
| **5. Actions** | Each farmer chooses **Restrain** (pump at a sustainable rate) or **Pump full** (extract at maximum capacity). |
| **6. Control Rules** | Aggregate extraction determines aquifer drawdown. If both restrain, the water table is maintained and pumping costs stay low. If both pump full, the aquifer depletes rapidly, increasing energy costs for all. If one restrains and the other pumps full, the pumper gains high immediate benefit while the restainer suffers the cost of depletion without the benefit. |
| **7. Information** | Farmers sense current groundwater depth and past extraction rates. They do not know the simultaneous choice of the other. |
| **8. Outcomes** | Aquifer level changes, affecting future pumping energy costs. Individual payoffs reflect crop yield and pumping expenses. |
| **9. Payoffs** | See payoff matrix. |
| **10. Strategic Tension** | **Strategic – Symmetric Prisoner’s Dilemma.** Pumping full is a dominant strategy for each farmer: it yields a higher individual payoff regardless of the other’s choice. Mutual restraint would give a better collective outcome, but the individual incentive to defect leads to the Pareto‑inferior equilibrium of mutual full pumping. |
| **11. Temporal Structure** | Repeated annually; the payoff matrix shifts as the aquifer depletes (restraint becomes more attractive when energy costs rise). |
| **12. Relevant Rules** | Choice rule: farmers are paired within their transformer group each year. The attractiveness of restraint increases with aquifer stress and can be influenced by a per‑unit extraction tax. |

**Normal‑form game (for a typical year with moderate aquifer stress)**  

| Farmer A / Farmer B | Restrain | Pump full |
|---------------------|----------|-----------|
| **Restrain**        | 2 , 2    | 0 , 3     |
| **Pump full**       | 3 , 0    | 1 , 1     |

*Explanation*:  
- (Restrain, Restrain): sustainable extraction, moderate costs → (2,2).  
- (Restrain, Pump full): restainer bears depletion cost, low yield (0); pumper gets high yield (3).  
- (Pump full, Restrain): symmetric.  
- (Pump full, Pump full): over‑extraction, high costs, lower net benefit → (1,1).  

---

### Action Situation 6: Electricity Use Enforcement  
**Players: A connected farmer and the substation staff. The farmer decides whether to comply with load limits; the staff decides whether to monitor and enforce.**

| IAD Element | Description |
|-------------|-------------|
| **1. Title** | Electricity Use Enforcement Game |
| **2. Location** | Transformer level, involving the substation staff responsible for that transformer. |
| **3. Players** | One connected farmer, one substation staff member. |
| **4. Roles** | Farmer: electricity user. Staff: enforcer / monitor. |
| **5. Actions** | Farmer: **Comply** (operate within authorised load) or **Violate** (overload, e.g., use inefficient pumps or exceed sanctioned capacity). Staff: **Monitor** (inspect and enforce) or **Not monitor** (neglect inspection). |
| **6. Control Rules** | If the farmer complies and the staff monitors, compliance is verified; the grid remains stable. If the farmer violates and the staff monitors, the violation is detected and the farmer is penalised. If the staff does not monitor, violations go undetected and cause grid stress (voltage drops, transformer burnout risk). |
| **7. Information** | Both know the general monitoring intensity and the typical penalties. They do not know the other’s simultaneous choice. |
| **8. Outcomes** | Grid voltage quality and transformer failure risk are affected. Farmer may pay a fine if caught. Staff may incur monitoring costs or face reputational damage if failures occur. |
| **9. Payoffs** | See payoff matrix. |
| **10. Strategic Tension** | **Strategic – Inspection game (asymmetric, mixed‑strategy equilibrium).** The farmer prefers to violate only if the staff does not monitor; the staff prefers to monitor only if the farmer violates. There is no pure‑strategy Nash equilibrium; both must randomise, leading to a stable mix of compliance and enforcement. |
| **11. Temporal Structure** | Played monthly as part of the enforcement checks. |
| **12. Relevant Rules** | Choice rule: staff enforcement effort is conditional on perceived oversight intensity and workload. Farmer’s decision depends on expected monitoring and penalty. |

**Normal‑form game**  

| Farmer / Staff | Monitor | Not monitor |
|----------------|---------|-------------|
| **Comply**     | 2 , 1   | 2 , 2       |
| **Violate**    | 0 , 3   | 3 , 0       |

*Explanation*:  
- (Comply, Monitor): farmer normal payoff, staff incurs monitoring cost → (2,1).  
- (Comply, Not monitor): farmer normal payoff, staff saves cost → (2,2).  
- (Violate, Monitor): farmer caught, penalised (0); staff gains fine revenue and deters violation (3).  
- (Violate, Not monitor): farmer gets high benefit from overloading, grid degrades (3); staff faces blame for failure (0).  

---

### Action Situation 7: Social Learning (Non‑strategic sequential process)  
**This is not a simultaneous game but a behavioural update mechanism that feeds into the DSM adoption situation.**

| IAD Element | Description |
|-------------|-------------|
| **1. Title** | Social Learning from Neighbours’ DSM Outcomes |
| **2. Location** | Transformer service area – farmers observe peers on the same transformer. |
| **3. Players** | Individual farmers (learners) and their neighbours (demonstrators). |
| **4. Roles** | Observer / imitator. |
| **5. Actions** | A farmer observes whether neighbours adopted capacitors and the resulting change in motor burnouts and voltage quality. Based on this observation, the farmer updates their probability of adopting in the next cycle. |
| **6. Control Rules** | Imitation is triggered only after a threshold number of simultaneous adoptions has been observed on the transformer. Once that threshold is crossed, each non‑adopter becomes independently eligible to imitate with a fixed yearly probability. A small number of “experimenters” are drawn each year regardless of neighbourhood outcomes. |
| **7. Information** | Farmers perceive neighbours’ adoption status and visible outcomes (burnouts, voltage) without error, but may misattribute causality. |
| **8. Outcomes** | Updated adoption probabilities; no direct payoff change in the learning step itself. |
| **9. Payoffs** | Not applicable (non‑strategic). |
| **10. Strategic Tension** | **Non‑strategic** – sequential updating based on observed success, no simultaneous interdependence. |
| **11. Temporal Structure** | Occurs annually before the DSM adoption decision. |
| **12. Relevant Rules** | Information rule: only neighbours on the same transformer are observed. Choice rule: imitation probability is fixed once the transformer‑level adoption threshold is met. |

---

### Strategic Core Analysis and Diversity Check

| Action Situation | Strategic Core | Symmetry | Distinct from others? |
|------------------|----------------|----------|-----------------------|
| 1. DSM Adoption Coordination | Assurance game (Stag Hunt) | Symmetric | Yes – only symmetric coordination with a safe non‑adoption equilibrium. |
| 2. Connection Authorization | Battle of the Sexes | Asymmetric | Yes – conflicting preferences over coordination target; no other game has this structure. |
| 3. Collusion Exchange | Coordination with asymmetric risk | Asymmetric | Yes – similar to Stag Hunt but with unequal off‑diagonal payoffs and different risk profiles. |
| 4. Transformer Capacity Investment | Asymmetric Prisoner’s Dilemma (public goods) | Asymmetric | Yes – one player has a dominant strategy to free‑ride; no other game has a strictly dominant strategy for one side. |
| 5. Groundwater Extraction | Symmetric Prisoner’s Dilemma | Symmetric | Yes – both players have a dominant strategy to defect; distinct from the asymmetric PD in situation 4. |
| 6. Electricity Use Enforcement | Inspection game | Asymmetric | Yes – mixed‑strategy equilibrium, no pure‑strategy Nash equilibrium; different from all others. |
| 7. Social Learning | Non‑strategic sequential process | – | Not a game; provides input to situation 1. |

All strategic games represent **different governance interactions** with unique incentive structures. No two games share the same strategic core, player‑role asymmetry, and payoff pattern simultaneously. The set covers coordination, cooperation, conflict, and enforcement dilemmas, fulfilling the requirement for strategic diversity.
# Run 2 — openai/gpt-oss-120b

## 1. DSM Coordination Game  (Capacitor / DSM adoption)

| **IAD Element** | **Description** |
|-----------------|-----------------|
| **Title** | DSM Coordination (Assurance) Game |
| **Location** | Transformer‑service area (village‑level cluster of farmers sharing the same transformer) |
| **Players** | Two *representative* farmers (the game is replicated pair‑wise for all farmers on the same transformer) |
| **Roles** | • Farmer A – electricity consumer, potential DSM adopter  <br>• Farmer B – electricity consumer, potential DSM adopter |
| **Actions** | **Invest** – pay the one‑off cost of a capacitor / DSM kit (only profitable if enough neighbours also invest). <br>**Wait** – postpone investment (no cost, but receives whatever voltage quality the transformer provides). |
| **Control Rules** | *If both farmers invest in the same month* → shared reduction of voltage drops → each receives the full benefit of the upgrade (no additional cost after the first payment). <br>*If only one invests* → the adopter bears the cost but does **not** obtain the voltage‑quality benefit because the transformer load is unchanged; the non‑investor enjoys the marginal improvement for free. <br>*If none invest* → status‑quo voltage quality persists. |
| **Information** | Farmers know their own past voltage experience and see whether neighbours have already installed capacitors (visible equipment). They **do not** know the neighbour’s decision for the current month – the game is simultaneous. Information is **partial** and sometimes noisy (voltage fluctuations may be mis‑attributed). |
| **Outcomes** | – Change in each farmer’s net income (cost of equipment vs. saved pump‑energy). <br>– Change in transformer load profile (slightly lower spikes). |
| **Payoffs** (ordinal 0 = worst → 3 = best) | <pre>
                Farmer B
                ┌───────────────┬───────────────┐
                │   Invest      │   Wait        │
    ┌───────────┼───────────────┼───────────────┤
    │  Invest   │ (3 , 3)       │ (0 , 2)       │
    │  Wait     │ (2 , 0)       │ (1 , 1)       │
    └───────────┴───────────────┴───────────────┘
</pre> |
| **Strategic Tension** | **Strategic** – a *coordination / assurance* game. Both farmers would like to adopt, but the benefit is realized only if the neighbour also adopts. The matrix is asymmetric in the mixed‑strategy cells (invest‑wait). |
| **Temporal Structure** | Repeated **annually** (once per year a new adoption‑pool is drawn; the same pair may meet again in later years). |
| **Relevant Rules** | • **Boundary rule** – only farmers attached to the same transformer are paired. <br>• **Choice rule** – each farmer can invest at most once (cost is sunk). <br>• **Control rule** – shared benefit is realised only when the *joint* adoption count on the transformer exceeds a threshold in the same cycle. |


### Strategic Core  
*Assurance (coordination) game*: two pure‑strategy Nash equilibria – (Invest, Invest) (Pareto‑optimal) and (Wait, Wait) (risk‑dominant). The mixed cells generate a classic “wait‑and‑see” dilemma.

---

## 2. Authorization Game  (Formal vs. informal electricity connection)

| **IAD Element** | **Description** |
|-----------------|-----------------|
| **Title** | Authorization Game |
| **Location** | Sub‑station office / field interaction at the farmer’s transformer |
| **Players** | Farmer (seeking a connection) – **F** <br>Sub‑station staff member – **S** |
| **Roles** | • Farmer F – electricity consumer, requester of a *formal* connection. <br>• Staff S – service provider / gate‑keeper with discretionary power to grant or reject a formal connection. |
| **Actions** | **Farmer**: *Pay‑Fee* (apply for a formal, authorised connection) or *Stay‑Illegal* (continue with an unauthorised line). <br>**Staff**: *Grant* (approve the formal connection) or *Reject* (maintain the status‑quo). |
| **Control Rules** | • If **Pay‑Fee** + **Grant** → farmer receives a legal, reliable supply; staff records a compliant connection (no illicit income). <br>• If **Pay‑Fee** + **Reject** → farmer loses the fee with no connection; staff avoids extra workload. <br>• If **Stay‑Illegal** + **Grant** → staff grants a legal line that the farmer declines; staff wastes effort, farmer keeps cheap electricity. <br>• If **Stay‑Illegal** + **Reject** → informal connection persists; staff may collect informal “tolerance” benefits, farmer keeps low‑cost electricity. |
| **Information** | Farmer knows the staff’s historical propensity to grant (observed from neighbours). Staff knows the farmer’s ability to pay the fee (observed from household wealth). Both have **partial** information; the exact decision of the other is simultaneous. |
| **Outcomes** | – Legal status of the farmer’s connection. <br>– Financial flows: fee paid to utility vs. informal tolerance payment. <br>– Staff workload (formal connection paperwork vs. informal monitoring). |
| **Payoffs** (ordinal) | <pre>
                Staff S
                ┌───────────────┬───────────────┐
                │   Grant       │   Reject      │
    ┌───────────┼───────────────┼───────────────┤
    │ Pay‑Fee   │ (3 , 3)       │ (0 , 1)       │
    │ Stay‑Il   │ (1 , 0)       │ (2 , 2)       │
    └───────────┴───────────────┴───────────────┘
</pre> |
| **Strategic Tension** | **Strategic** – an *asymmetric coordination/conflict* game. The farmer wants a formal link, the staff balances workload and informal gains. The (Pay‑Fee, Grant) cell is jointly best, but the staff may prefer to *Reject* to avoid paperwork; the farmer may prefer to stay illegal if the chance of grant is low. |
| **Temporal Structure** | One‑shot **annual** decision (players re‑match each year). |
| **Relevant Rules** | • **Boundary rule** – only the farmer’s assigned staff member (or the two staff at the transformer) can act. <br>• **Choice rule** – staff’s willingness to grant is moderated by current workload (parameter τ). <br>• **Control rule** – a formal connection changes the grid‑load calculation for the transformer. |


### Strategic Core  
*Asymmetric coordination/conflict*: two pure‑strategy Nash equilibria – (Pay‑Fee, Grant) (efficient, high‑payoff) and (Stay‑Illegal, Reject) (status‑quo, moderate‑payoff). The game captures the trade‑off between formal compliance and informal tolerance.

---

## 3. Collusion Exchange Game  (Informal bribe‑for‑favour)

| **IAD Element** | **Description** |
|-----------------|-----------------|
| **Title** | Collusion Exchange Game |
| **Location** | On‑site interaction at the transformer / field visits |
| **Players** | Farmer **F** (who may offer a bribe) <br>Sub‑station staff **S** (who may accept) |
| **Roles** | • Farmer F – electricity consumer, potential bribe‑giver. <br>• Staff S – discretionary official, potential bribe‑taker. |
| **Actions** | **Farmer**: *Bribe* (offer informal payment) or *Clean* (no bribe). <br>**Staff**: *Accept* (take the bribe and give a favourable service, e.g., reduced fees, delayed disconnection) or *Reject* (refuse the bribe, follow formal rules). |
| **Control Rules** | • If **Bribe + Accept** → farmer receives a discount / delayed enforcement; staff gains illicit income. <br>• If **Bribe + Reject** → farmer loses the offered money, staff incurs monitoring cost. <br>• If **Clean + Accept** → staff’s acceptance is wasted (no bribe received); farmer gets the standard service. <br>• If **Clean + Reject** → both parties obtain the baseline, rule‑based outcome. |
| **Information** | Farmer knows the staff member’s “corruption level” from past interactions (noisy). Staff knows the farmer’s current cash‑flow constraints (partial). Decisions are simultaneous. |
| **Outcomes** | – Monetary transfer (bribe) (if any). <br>– Change in service quality (e.g., lower fees, delayed shut‑off). <br>– Risk of detection (higher when both cooperate). |
| **Payoffs** (ordinal) | <pre>
                Staff S
                ┌───────────────┬───────────────┐
                │   Accept      │   Reject      │
    ┌───────────┼───────────────┼───────────────┤
    │ Bribe     │ (3 , 3)       │ (0 , 1)       │
    │ Clean     │ (2 , 0)       │ (2 , 2)       │
    └───────────┴───────────────┴───────────────┘
</pre> |
| **Strategic Tension** | **Strategic** – a *trust / coordination* game. Mutual cooperation yields the highest joint payoff, but the risk of unilateral bribe‑offer or acceptance creates a temptation to defect. |
| **Temporal Structure** | Repeated **annually** (the same farmer–staff pair may meet each year; past outcomes affect future willingness). |
| **Relevant Rules** | • **Boundary rule** – only farmers with an existing social tie to a staff member can attempt a bribe. <br>• **Choice rule** – staff willingness to accept declines with current workload (parameter δ). <br>• **Control rule** – detection probability is exogenous (stochastic monitoring intensity). |


### Strategic Core  
*Trust game*: (Bribe, Accept) is Pareto‑optimal, (Clean, Reject) is the safe equilibrium. The matrix is asymmetric because the farmer bears the cost of a failed bribe, while the staff suffers a monitoring cost when rejecting a bribe.

---

## 4. Enforcement Compliance Game  (Formal enforcement vs. lenient tolerance)

| **IAD Element** | **Description** |
|-----------------|-----------------|
| **Title** | Enforcement Compliance Game |
| **Location** | Sub‑station enforcement office – monitoring of connections on a transformer |
| **Players** | Sub‑station staff **S** (enforcer) <br>Farmer **F** (potential evader) |
| **Roles** | • Staff S – regulator / enforcer with discretionary power to inspect and penalise. <br>• Farmer F – electricity consumer who may either comply with the formal connection rules or evade them. |
| **Actions** | **Staff**: *Enforce* (conduct inspections, issue penalties) or *Lenient* (reduce inspection intensity, tolerate unauthorised use). <br>**Farmer**: *Comply* (pay the authorisation fee, use a legal connection) or *Evasion* (keep an unauthorised line). |
| **Control Rules** | • **Enforce + Comply** → farmer pays the fee, staff records compliance (no penalty). <br>• **Enforce + Evasion** → farmer is caught, incurs a fine; staff receives enforcement reward (higher reputation, possible bonus). <br>• **Lenient + Comply** → farmer pays fee but staff foregoes extra enforcement benefit. <br>• **Lenient + Evasion** → farmer enjoys cheap electricity; staff may obtain an informal “tolerance” payment (lower than a fine). |
| **Information** | Staff observes past evasion rates on the transformer (partial). Farmer observes the current inspection intensity (visible patrols) and the probability of being caught (noisy). Decisions are simultaneous. |
| **Outcomes** | – Financial flows (fees, fines, informal tolerance payments). <br>– Change in the share of authorised vs. unauthorised connections. <br>– Staff workload (inspection effort). |
| **Payoffs** (ordinal) | <pre>
                Staff S
                ┌───────────────┬───────────────┐
                │ Enforce       │ Lenient       │
    ┌───────────┼───────────────┼───────────────┤
    │ Comply    │ (2 , 3)       │ (2 , 1)       │
    │ Evasion   │ (0 , 3)       │ (3 , 2)       │
    └───────────┴───────────────┴───────────────┘
</pre> |
| **Strategic Tension** | **Strategic** – a *prisoner’s‑dilemma‑type* conflict. The jointly best outcome (Lenient + Evasion) is unstable because the staff can improve its payoff by enforcing, while the farmer can improve by complying when enforcement is expected. |
| **Temporal Structure** | Repeated **annual** (inspection regime is set each year; farmers decide each year whether to evade). |
| **Relevant Rules** | • **Boundary rule** – staff can only enforce on the set of farmers attached to his/her transformer. <br>• **Choice rule** – staff’s willingness to enforce is reduced by current workload (parameter γ). <br>• **Control rule** – enforcement generates a stochastic detection probability (exogenous monitoring intensity). |


### Strategic Core  
*Prisoner’s dilemma*: (Lenient, Evasion) gives the highest joint payoff (3,2) but is not a Nash equilibrium; the only Nash equilibrium is (Enforce, Evasion) (0,3) where the farmer is worst‑off and staff gets the enforcement reward.

---

## 5. Groundwater Extraction Game  (Common‑pool resource)

| **IAD Element** | **Description** |
|-----------------|-----------------|
| **Title** | Groundwater Extraction Game |
| **Location** | Village‑level groundwater basin (shared aquifer) |
| **Players** | Two neighbouring farmers **A** and **B** (representative of many; the game is replicated across all pairs on a transformer). |
| **Roles** | • Farmer A – water‑user, pump‑operator. <br>• Farmer B – water‑user, pump‑operator. |
| **Actions** | **Full** – pump at the maximum feasible rate (high short‑term yield, high energy cost). <br>**Restrict** – voluntarily limit extraction (lower short‑term yield, preserves aquifer). |
| **Control Rules** | • Aquifer drawdown each month equals the sum of the two farmers’ extraction levels. <br>• If total extraction exceeds the sustainable threshold, the aquifer level drops, raising future energy‑cost per unit water for **both** (reflected in the payoff ranking). <br>• If both restrict, the aquifer remains stable → long‑term moderate yields. |
| **Information** | Each farmer knows the *current* groundwater depth (observed at his own well) and the *historical* trend for the basin (partial). They do **not** know the neighbour’s exact extraction decision for the current month. |
| **Outcomes** | – Individual water volume extracted (and thus crop yield). <br>– Energy cost per cubic metre (higher when the aquifer is depleted). <br>– Updated aquifer level for the next year. |
| **Payoffs** (ordinal) | <pre>
                Farmer B
                ┌───────────────┬───────────────┐
                │   Full        │ Restrict      │
    ┌───────────┼───────────────┼───────────────┤
    │ Full      │ (0 , 0)       │ (3 , 1)       │
    │ Restrict  │ (1 , 3)       │ (3 , 3)       │
    └───────────┴───────────────┴───────────────┘
</pre> |
| **Strategic Tension** | **Strategic** – a *common‑pool resource* (tragedy‑of‑the‑commons) game. Mutual restriction yields the best joint outcome, but each farmer has an incentive to over‑extract when the other restricts. |
| **Temporal Structure** | Repeated **annual** (each irrigation season). The aquifer level provides a state variable that feeds back into later rounds. |
| **Relevant Rules** | • **Boundary rule** – all farmers whose wells draw from the same aquifer belong to the same CPR. <br>• **Choice rule** – extraction level is bounded by pump capacity and groundwater depth. <br>• **Control rule** – aquifer dynamics (drawdown, recharge) are modelled endogenously (exogenous recharge parameter ι). |


### Strategic Core  
*Common‑pool resource (prisoner’s dilemma)*: (Restrict, Restrict) is Pareto‑optimal (3,3); (Full, Full) is the Nash equilibrium (0,0) because each farmer’s dominant strategy is to pump fully given the other’s possible restriction.

---

## 6. Social‑Learning Process  (Observation → Imitation)

| **IAD Element** | **Description** |
|-----------------|-----------------|
| **Title** | Social‑Learning (Imitation) Process |
| **Location** | Village‑level social network; visible equipment at the transformer site |
| **Players** | All farmers (treated as a *population*; no strategic interaction) |
| **Roles** | • Observer – farmer watching neighbours’ outcomes. |
| **Actions** | **Observe** – gather information on whether neighbours have adopted capacitors/DSM and on their reported yields. <br>**Imitate** – with a fixed probability (τ) adopt the observed successful technology in the next cycle. |
| **Control Rules** | Observation is deterministic (farmers see visible equipment). Imitation occurs probabilistically; the probability increases once the number of adopters on a transformer exceeds a threshold (the “critical mass” rule). |
| **Information** | Perfect observation of neighbours’ *adoption status* (no error). Perceived performance (e.g., yield increase) is noisy because farmers may mis‑attribute causes. |
| **Outcomes** | – Diffusion of DSM technology across the transformer cluster. <br>– Change in the number of farmers in the *investment* pool for the DSM Coordination Game. |
| **Payoffs** | Not modelled as a payoff matrix; the process changes the *state* (adoption count) that later influences payoffs in the DSM Coordination Game. |
| **Strategic Tension** | **Non‑strategic** – a sequential learning process; no simultaneous decision‑making. |
| **Temporal Structure** | Continuous **monthly** observation; **annual** probabilistic imitation. |
| **Relevant Rules** | • **Boundary rule** – only farmers within the same transformer cluster are observable. <br>• **Choice rule** – imitation probability is a function of the current adoption share (parameter τ). <br>• **Control rule** – once the adoption count on a transformer jumps by the threshold δ in a single cycle, the whole cluster’s imitation pool opens. |


---

# Comparative Analysis of the Strategic Action Situations

| Situation | Players | Game Type (per list) | Core Dilemma | Distinctive Feature |
|-----------|---------|----------------------|--------------|----------------------|
| **1 DSM Coordination** | Farmer ↔ Farmer | **DSM Coordination Game** (Assurance) | Need *joint* adoption to reap benefits. | Benefit is *shared* only when *both* adopt in the **same** month – a pure coordination problem. |
| **2 Authorization** | Farmer ↔ Staff | **Authorization Game** (Asymmetric coordination/conflict) | Farmer wants formal connection; staff balances workload vs. informal gains. | Asymmetry: staff’s “grant” decision does **not** automatically benefit a farmer who stays illegal. |
| **3 Collusion Exchange** | Farmer ↔ Staff | **Collusion Exchange Game** (Trust/Coordination) | Mutual bribe‑exchange yields highest payoff but carries detection risk. | Explicit *bribe* as a strategic variable; payoff asymmetry because a failed bribe hurts farmer more than staff. |
| **4 Enforcement Compliance** | Staff ↔ Farmer | **Enforcement Compliance Game** (Prisoner’s‑Dilemma) | Staff can enforce or be lenient; farmer can comply or evade. | The jointly best outcome is *lenient + evasion* (both benefit), yet the equilibrium is *enforce + evasion* (staff wins, farmer loses). |
| **5 Groundwater Extraction** | Farmer ↔ Farmer | **Groundwater Extraction Game** (Common‑pool resource) | Over‑extraction harms both; restraint is collectively optimal. | Physical CPR (aquifer) links payoffs across time; the matrix is symmetric but the *environmental* feedback makes it distinct from the pure coordination of Situation 1. |
| **6 Social‑Learning** | Population of farmers | **Non‑strategic** (Sequential observation → imitation) | – | Learning process that feeds into Situation 1; no simultaneous move. |

### Why the Set Is Strategically Diverse

1. **Different player pairings** – three games involve farmer–staff pairs (2, 3, 4) but each captures a **different institutional mechanism** (authorization, informal bribe, formal enforcement).  
2. **Different game structures** – coordination (1), asymmetric coordination (2), trust (3), prisoner's dilemma (4), CPR (5). No two games share the same payoff topology.  
3. **Different sources of payoff** – financial (fees, fines, bribes), service quality (voltage stability), environmental (aquifer health), and reputational (staff workload).  

### Revision for Strategic Diversity

The original ODD+D description also mentioned a *Capacity‑Provision* sub‑model (staff investing transformer capacity for tied farmers). That interaction overlaps heavily with the **Authorization Game** (both involve staff deciding whether to allocate capacity and farmer deciding whether to request it). To avoid redundancy, the **Capacity‑Provision Game** was **replaced** by the **Enforcement Compliance Game** (Situation 4). The new game introduces a *prisoner’s‑dilemma* tension that was absent from the previous set, thereby guaranteeing that each strategic situation now reflects a **unique** governance dilemma.

---

# Full List of Distinct Action Situations (5 strategic + 1 non‑strategic)

1. **DSM Coordination (Assurance) Game** – farmer‑farmer coordination on capacitor adoption.  
2. **Authorization Game** – farmer‑staff decision on formal connection grant.  
3. **Collusion Exchange Game** – farmer‑staff bribe‑for‑favour interaction.  
4. **Enforcement Compliance Game** – staff‑farmer choice between inspection and leniency vs. compliance or evasion.  
5. **Groundwater Extraction Game** – farmer‑farmer CPR dilemma over water pumping.  
6. **Social‑Learning Process** – non‑strategic observation‑imitation sequence that drives diffusion of technology.

Each situation is fully specified above with IAD elements, ordinal payoff matrices (where strategic), and a brief analysis of its strategic core.
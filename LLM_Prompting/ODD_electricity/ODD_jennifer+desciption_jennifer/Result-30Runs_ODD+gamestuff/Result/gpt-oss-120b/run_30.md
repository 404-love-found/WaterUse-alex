# Run 30 — openai/gpt-oss-120b

## Action‑situations extracted from the ODD + D description  
*(each situation follows the Institutional Analysis & Development (IAD) template; strategic games are given as 2 × 2 normal‑form matrices with **ordinal** pay‑offs 0 = least preferred, 3 = most preferred).*

---

### 1. DSM‑Coordination (Capacitor Adoption) Game  

| IAD element | Description |
|------------|-------------|
| **Title** | **Capacitor‑Coordination (DSM) Game** |
| **Location** | Village‑level transformer service area (all farmers sharing the same transformer). |
| **Players** | Two *representative* farmers (any pair of neighbours on the same transformer). |
| **Roles** | **Farmer A** – electricity consumer, potential DSM adopter.<br>**Farmer B** – same. |
| **Actions** | **Adopt** a capacitor (invest now).<br>**Not‑Adopt** (wait). |
| **Control Rules** | Benefits of adoption (higher voltage stability, lower pump‑failure risk) materialise **only if** *both* farmers adopt in the same annual cycle. If only one adopts, the adopter bears the full cost and receives little or no service improvement. |
| **Information** | Each farmer knows the *historical* adoption rate on the transformer and the *observable* outcomes of past coordinated adoptions, but does **not** know the other farmer’s current intention (partial, noisy). |
| **Outcomes** | – Grid‑quality improvement (shared).<br>– Individual adoption cost (paid once). |
| **Payoffs** (ordinal, 0‑3) | <table><thead><tr><th>Farmer A \ Farmer B</th><th>Adopt</th><th>Not‑Adopt</th></tr></thead><tbody><tr><td>Adopt</td><td>(3, 3)</td><td>(0, 2)</td></tr><tr><td>Not‑Adopt</td><td>(2, 0)</td><td>(1, 1)</td></tr></tbody></table> |
| **Strategic Tension** | **Strategic – Coordination/Assurance game.** Both prefer the *joint‑adopt* outcome (3,3) but risk a *failed‑adopt* (0 for the adopter, 2 for the non‑adopter). The game is not symmetric in pay‑offs because the non‑adopter still enjoys a modest improvement from the neighbour’s load reduction (rank 2). |
| **Temporal Structure** | Repeated annually; the same pair may be re‑matched each year. |
| **Relevant Rules** | *Boundary rule*: only farmers attached to the same transformer are paired.<br>*Choice rule*: adoption cost is incurred once, regardless of cycles.<br>*Control rule*: shared benefit realised only when a **threshold** of simultaneous adopters on that transformer is met. |

**Strategic core:** *Assurance (coordination) game* – two pure‑strategy Nash equilibria (Adopt/Adopt and Not‑Adopt/Not‑Adopt); the former is Pareto‑superior but risk‑dominated without coordination mechanisms.

---

### 2. Capacity‑Provision (Public‑Goods) Game  

| IAD element | Description |
|------------|-------------|
| **Title** | **Transformer‑Capacity Contribution Game** |
| **Location** | Sub‑station office that decides on capacity upgrades for a specific transformer. |
| **Players** | **Farmer F** (any farmer connected to the transformer) vs. **Staff S** (the sub‑station employee responsible for the transformer). |
| **Roles** | Farmer F – demand‑side contributor; Staff S – capacity‑provider / enforcer. |
| **Actions** | **Farmer F:** *Contribute* (pay the authorised connection/upgrade fee) or *Free‑Ride* (remain un‑contributed).<br>**Staff S:** *Invest* (order capacity upgrade) or *Do‑Nothing* (maintain status‑quo). |
| **Control Rules** | The transformer’s reliability improves **only if** the staff invests **and** at least a *critical mass* of farmers have contributed. Staff incurs an effort cost when investing; farmers incur a monetary cost when contributing. |
| **Information** | Farmer knows his own budget and the *observed* reliability of the transformer; he does **not** know whether the staff will invest this year (partial). Staff observes the *aggregate* contribution level (exact) but cannot perfectly predict each farmer’s future willingness. |
| **Outcomes** | – Change in transformer reliability (high/low).<br>– Individual cost/pay‑off (budget hit or effort). |
| **Payoffs** (ordinal) | <table><thead><tr><th>Farmer F \ Staff S</th><th>Invest</th><th>Do‑Nothing</th></tr></thead><tbody><tr><td>Contribute</td><td>(3, 2)</td><td>(1, 1)</td></tr><tr><td>Free‑Ride</td><td>(2, 0)</td><td>(0, 3)</td></tr></tbody></table> |
| **Strategic Tension** | **Strategic – Public‑Goods / Free‑Rider game.** The socially optimal outcome is *(Contribute, Invest)* (3 for farmer, 2 for staff). The *(Free‑Ride, Invest)* outcome gives the farmer a higher rank (2) but leaves staff with the worst rank (0) because he bears the cost alone. *(Free‑Ride, Do‑Nothing)* is staff’s favourite (3) but farmer gets the worst (0). |
| **Temporal Structure** | One‑shot each year (decision revisited annually). |
| **Relevant Rules** | *Boundary rule*: all farmers linked to the transformer are eligible to contribute.<br>*Choice rule*: contribution is a one‑time payment; staff investment can be repeated each year if needed.<br>*Control rule*: reliability upgrade realised only when staff invests **and** contribution ≥ threshold τ. |

**Strategic core:** *Public‑goods (voluntary‑contribution) game* with asymmetric pay‑offs; two pure‑strategy Nash equilibria – *(Free‑Ride, Do‑Nothing)* (staff’s dominant) and *(Contribute, Invest)* (Pareto‑superior but requires coordination).

---

### 3. Authorization Game  

| IAD element | Description |
|------------|-------------|
| **Title** | **Formal‑Connection Authorization Game** |
| **Location** | Sub‑station counter where farmers request a legal connection; staff processes the request. |
| **Players** | **Farmer F** (seeking authorized electricity) vs. **Staff S** (deciding to grant or deny). |
| **Roles** | Farmer F – applicant; Staff S – gate‑keeper / discretionary enforcer. |
| **Actions** | **Farmer F:** *Apply* (pay the fee & wait) or *Stay‑Illegal* (continue unauthorised use).<br>**Staff S:** *Authorize* (grant connection, record it) or *Reject* (refuse, keep informal status). |
| **Control Rules** | If the farmer applies **and** staff authorizes, the farmer gains a legal connection (lower penalty risk, higher reliability) but pays the fee. If the staff rejects, the farmer remains illegal and faces higher detection risk. If the farmer stays illegal, staff may still tolerate (informal exchange) or enforce (penalty). |
| **Information** | Farmer knows the *current enforcement intensity* (high/low) and his own budget; staff knows the *aggregate illegal‑connection density* and the probability of external audit (stochastic). |
| **Outcomes** | – Legal status (legal/illegal).<br>– Monetary cost (fee vs. fine).<br>– Staff effort/reputation change. |
| **Payoffs** (ordinal) | <table><thead><tr><th>Farmer F \ Staff S</th><th>Authorize</th><th>Reject</th></tr></thead><tbody><tr><td>Apply</td><td>(3, 2)</td><td>(1, 3)</td></tr><tr><td>Stay‑Illegal</td><td>(2, 1)</td><td>(0, 0)</td></tr></tbody></table> |
| **Strategic Tension** | **Strategic – Authorization (mixed) game.** The *(Apply, Authorize)* cell is jointly best (3,2). The staff prefers *(Reject, Apply)* (3) because it yields a fine (or informal rent) without the administrative burden, while the farmer gets a modest rank (1). The *(Stay‑Illegal, Reject)* outcome is the worst for both (0,0). |
| **Temporal Structure** | One‑shot each year; the decision is revisited annually (new applications possible). |
| **Relevant Rules** | *Boundary rule*: only farmers without a current legal record may apply.<br>*Choice rule*: staff’s authorization incurs a fixed administrative cost.<br>*Control rule*: illegal users face a stochastic detection probability that influences the staff’s payoff for “Reject”. |

**Strategic core:** *Mixed‑motivation game* (similar to a trust‑type game) where staff can extract informal rents by rejecting applications, while farmers balance fee vs. risk.

---

### 4. Collusion‑Exchange (Trust) Game  

| IAD element | Description |
|------------|-------------|
| **Title** | **Farmer‑Staff Collusion Exchange Game** |
| **Location** | Informal meeting spot (village centre) where a farmer and the assigned staff member negotiate an exchange of favors (e.g., delayed bill, extra electricity). |
| **Players** | **Farmer F** vs. **Staff S** (the staff member matched to the farmer for the year). |
| **Roles** | Farmer F – *beneficiary* of informal tolerance; Staff S – *provider* of informal benefit. |
| **Actions** | **Farmer F:** *Offer* a reciprocal favor (e.g., future political support, small cash) or *Refuse*.<br>**Staff S:** *Accept* the offer (grant informal tolerance) or *Decline* (enforce formally). |
| **Control Rules** | Mutual benefit materialises only when **both** offer and accept. If only one side cooperates, the cooperating side loses (cost without benefit). Detection risk (exogenous) reduces the payoff of “Accept” for staff. |
| **Information** | Both know the *local collusion density* (δ) and the current *monitoring intensity* (stochastic). They do **not** know the other’s intended action until after the simultaneous move. |
| **Outcomes** | – Informal electricity discount for farmer.<br>– Informal rent (cash/political capital) for staff.<br>– Potential sanction if detected (reduces staff payoff). |
| **Payoffs** (ordinal) | <table><thead><tr><th>Farmer F \ Staff S</th><th>Accept</th><th>Decline</th></tr></thead><tbody><tr><td>Offer</td><td>(3, 3)</td><td>(0, 2)</td></tr><tr><td>Refuse</td><td>(2, 0)</td><td>(1, 1)</td></tr></tbody></table> |
| **Strategic Tension** | **Strategic – Trust/Reciprocity game**. The *(Offer, Accept)* cell is Pareto‑optimal (3,3). If the farmer offers but staff declines, farmer gets the worst (0) while staff still gains a small reputational benefit (2). If the farmer refuses while staff accepts, staff wastes effort (0) and farmer gets a modest benefit from “no‑exchange” (2). |
| **Temporal Structure** | Repeated each year for the same farmer‑staff dyad (history influences δ). |
| **Relevant Rules** | *Boundary rule*: a dyad exists only if the farmer is *matched* to a staff member (existing tie or randomly assigned).<br>*Choice rule*: offering a favor incurs a small budget cost for the farmer.<br>*Control rule*: detection probability reduces staff’s payoff for “Accept” in high‑monitoring years (implemented as a lower ordinal rank in those years). |

**Strategic core:** *Trust game* with symmetric high‑payoff equilibrium when both cooperate; the risk of unilateral cooperation creates a coordination problem.

---

### 5. Groundwater‑Extraction (Common‑Pool Resource) Game  

| IAD element | Description |
|------------|-------------|
| **Title** | **Groundwater Extraction Game** |
| **Location** | Village‑level aquifer (shared by all farmers attached to the same transformer). |
| **Players** | Two *representative* farmers (any pair of neighbours drawing water from the same aquifer). |
| **Roles** | Farmer A – extractor; Farmer B – extractor. |
| **Actions** | **Extract High** (pump at full irrigation demand).<br>**Extract Low** (restrain, adopt water‑saving practice). |
| **Control Rules** | Aquifer depth rises with total extraction; deeper water raises the *energy cost* of pumping (γ) and reduces voltage stability (τ). The payoff each farmer receives depends on **both** extraction levels because the shared water stock determines future reliability and cost. |
| **Information** | Each farmer knows the *current groundwater depth* and the *average extraction* of neighbours from past years (partial). They do not know the other farmer’s current choice. |
| **Outcomes** | – Immediate water availability (higher for High).<br>– Future pumping cost (higher when both choose High). |
| **Payoffs** (ordinal) | <table><thead><tr><th>Farmer A \ Farmer B</th><th>High</th><th>Low</th></tr></thead><tbody><tr><td>High</td><td>(2, 2)</td><td>(3, 1)</td></tr><tr><td>Low</td><td>(1, 3)</td><td>(0, 0)</td></tr></tbody></table> |
| **Strategic Tension** | **Strategic – Common‑Pool Resource (tragedy of the commons) game.** The *(High, High)* outcome gives both a moderate rank (2) because water is abundant now but future costs rise. *(Low, Low)* is the worst (0) for each because immediate water is scarce. The *asymmetric* cells reward the high extractor (3) while the restraining neighbour gets a low rank (1). |
| **Temporal Structure** | One‑shot each irrigation season; the game repeats annually with the aquifer state updated by the aggregate of all farmers. |
| **Relevant Rules** | *Boundary rule*: all farmers sharing the same aquifer are in the same CPR domain.<br>*Choice rule*: “Low” implies investment in water‑saving practices (e.g., drip irrigation) that reduces extraction.<br>*Control rule*: aquifer depth update = previous depth + (extraction‑recharge). |

**Strategic core:** *Asymmetric CPR game* (similar to a Prisoner’s Dilemma but with non‑symmetric pay‑offs). The socially optimal outcome is *(Low, Low)* for sustainability, but it is dominated by unilateral high extraction.

---

### 6. Social‑Learning (Non‑Strategic) Process  

| IAD element | Description |
|------------|-------------|
| **Title** | **Neighbour‑Observation & Imitation Process** |
| **Location** | Farmer’s household and the transformer service area (visual observation of neighbours). |
| **Players** | *Individual* farmer (decision‑maker). |
| **Roles** | Learner / observer. |
| **Actions** | **Imitate** a neighbour’s successful technology (capacitor, approved pump) with probability *p* (if the neighbour’s outcome was ranked ≥ 2).<br>**Do‑Nothing** (retain current technology). |
| **Control Rules** | Imitation is triggered only after the farmer has *observed* a neighbour’s outcome at the end of the annual cycle. The probability *p* is reduced by the *learning‑constraint* parameter ι (low visibility of outcomes). |
| **Information** | Farmer perceives neighbours’ *visible* adoption status correctly, but misattributes the cause of improved service (noisy). |
| **Outcomes** | Change in farmer’s equipment stock (new capacitor or pump). |
| **Payoffs** | Not modelled as a strategic payoff; the farmer’s future utility is affected indirectly through the other games (e.g., higher voltage after successful adoption). |
| **Strategic Tension** | **Non‑strategic** – the farmer does not influence neighbours’ choices in the same period; the process is sequential (observation → possible imitation). |
| **Temporal Structure** | Occurs once per year, after the outcome of the DSM‑Coordination game is observed. |
| **Relevant Rules** | *Boundary rule*: only farmers on the same transformer are observable.<br>*Choice rule*: imitation cost is negligible; the only barrier is the learning‑constraint ι. |

---

## Comparative Analysis of the Strategic Core  

| Game # | Players | Game Type (IAD) | Core Dilemma | Distinctiveness |
|--------|---------|----------------|--------------|-----------------|
| 1 | Farmer ↔ Farmer | Coordination / Assurance | Joint adoption vs. unilateral loss | Focuses on *technology coordination* (voltage‑stabilizing equipment). |
| 2 | Farmer ↔ Staff | Public‑Goods / Free‑Rider | Contribute to capacity vs. free‑ride | Involves *infrastructure investment* with asymmetric cost/benefit distribution. |
| 3 | Farmer ↔ Staff | Authorization (mixed) | Apply & get authorised vs. stay illegal; staff can extract rent | Centers on *formal‑vs‑informal access* and discretionary gate‑keeping. |
| 4 | Farmer ↔ Staff | Trust / Reciprocity | Mutual informal exchange vs. unilateral cooperation | Captures *personal collusion* that is separate from formal authorization. |
| 5 | Farmer ↔ Farmer | Common‑Pool Resource | High extraction (short‑term gain) vs. low extraction (long‑term sustainability) | Addresses *shared groundwater* dynamics, distinct from electricity‑grid issues. |
| 6 | Farmer (single) | Social‑Learning (sequential) | None (non‑strategic) | Provides the *diffusion* mechanism that feeds the other games. |

All five strategic games involve **different** payoff structures, player asymmetries, and underlying sustainability dilemmas. No two games repeat the same combination of roles and incentive logic.

---

## Ensuring Strategic Diversity – Revision  

The **Capacity‑Provision Game** (Game 2) and the **Authorization Game** (Game 3) both pair a farmer with staff, but they address **different** institutional mechanisms (capacity upgrade vs. legal connection). To further diversify, we replace Game 2 with a **Maintenance‑Effort Game** that pits **two staff members** against each other over how much effort to allocate to transformer maintenance, thereby introducing a *pure‑staff* strategic interaction.

### Revised 2. Maintenance‑Effort Game (Staff‑Staff Coordination)

| IAD element | Description |
|------------|-------------|
| **Title** | **Transformer Maintenance Effort Game** |
| **Location** | Sub‑station (maintenance planning office). |
| **Players** | **Staff S₁** and **Staff S₂** – the two employees assigned to the same transformer. |
| **Roles** | Maintenance planner (each). |
| **Actions** | **High‑Effort** (spend time on preventive maintenance, incur personal cost).<br>**Low‑Effort** (focus on routine tasks, avoid extra cost). |
| **Control Rules** | Transformer reliability improves **only if** *both* staff choose High‑Effort (joint preventive work). If only one works hard, the benefit is limited and the diligent staff bears the cost alone. |
| **Information** | Each staff knows the *current reliability* and the *probability of external audit* but does not know the other’s intended effort. |
| **Outcomes** | – Transformer reliability (high/low).<br>– Personal effort cost (higher for High‑Effort). |
| **Payoffs** (ordinal) | <table><thead><tr><th>S₁ \ S₂</th><th>High‑Effort</th><th>Low‑Effort</th></tr></thead><tbody><tr><td>High‑Effort</td><td>(2, 2)</td><td>(0, 3)</td></tr><tr><td>Low‑Effort</td><td>(3, 0)</td><td>(1, 1)</td></tr></tbody></table> |
| **Strategic Tension** | **Strategic – Coordination (public‑good) game among staff.** The *(High‑Effort, High‑Effort)* outcome gives moderate reliability (2) to both but costs effort. The *asymmetric* cells reward the low‑effort player (3) while penalising the high‑effort partner (0). The *(Low, Low)* cell is the worst for the system (1,1). |
| **Temporal Structure** | Repeated each year; past joint effort influences the *trust* parameter δ for future collusion with farmers. |
| **Relevant Rules** | *Boundary rule*: only the two staff assigned to a transformer can act. <br>*Choice rule*: effort cost is incurred only when choosing High‑Effort.<br>*Control rule*: reliability increase only when both choose High‑Effort (τ ↑). |

**Strategic core:** *Coordination game with asymmetric incentives* (similar to a Stag‑Hunt). This replacement adds a staff‑only interaction, guaranteeing that each strategic game now involves a **unique set of players and a unique institutional problem**.

---

## Final Set of Distinct Action Situations  

| # | Title | Players | Core Game Type |
|---|-------|---------|----------------|
| 1 | Capacitor‑Coordination (DSM) Game | Farmer ↔ Farmer | Coordination / Assurance |
| 2 | **(Revised)** Maintenance‑Effort Game | Staff S₁ ↔ Staff S₂ | Coordination (staff‑only) |
| 3 | Authorization Game | Farmer ↔ Staff | Mixed Authorization / Rent‑Extraction |
| 4 | Collusion‑Exchange (Trust) Game | Farmer ↔ Staff | Trust / Reciprocity |
| 5 | Groundwater Extraction (CPR) Game | Farmer ↔ Farmer | Common‑Pool Resource |
| 6 | Social‑Learning Process | Farmer (single) | Non‑strategic sequential observation |

These six action‑situations capture **all governance interactions** described in the ODD + D model: technology coordination, infrastructure maintenance, formal‑informal access decisions, informal collusion, shared groundwater use, and the diffusion of learning. Each is presented with full IAD details, an ordinal 2 × 2 payoff matrix (where strategic), and an explicit description of the strategic tension.
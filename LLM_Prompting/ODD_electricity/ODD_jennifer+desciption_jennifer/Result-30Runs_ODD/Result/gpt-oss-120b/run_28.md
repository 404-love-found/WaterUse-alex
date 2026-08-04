# Run 28 — openai/gpt-oss-120b

## Electricity‑Irrigation Governance – Action‑Situation Catalogue (IAD + D)

The following list extracts **every distinct governance interaction** that is described (or implied) in the ODD+D specification.  
Both **strategic games** (simultaneous choices with inter‑dependent ordinal payoffs) and **non‑strategic sequential processes** (observation, experimentation, imitation) are included.  
Each situation is presented with the full IAD template; strategic situations are followed by a 2 × 2 normal‑form game whose payoffs are **ordinal ranks 0 – 3** (3 = most preferred, 0 = least preferred).

---

### 1. DSM (Capacitor) Coordination Game – “Assurance Adoption”

| Element | Description |
|---|---|
| **Title** | DSM Coordination (Assurance) Game |
| **Location** | Transformer service area (village‑level) |
| **Players** | Two *farmers* that share the same transformer (any pair can be drawn; the game is repeated among many pairs) |
| **Roles** | Electricity consumer – “potential adopter” |
| **Actions** | **Invest** (buy and install a capacitor/DSM device)  or  **Not‑Invest** |
| **Control Rules** | If *both* farmers invest in the same month, the transformer voltage improves for **all** farmers on that transformer → shared benefit. If only one invests, the investor bears the full cost and receives no voltage improvement (the benefit is “non‑existent” because the threshold is not met). |
| **Information** | Each farmer knows: (i) its own cost of a capacitor, (ii) the historical success rate of past joint adoptions on the transformer, (iii) the current voltage quality (noisy). No knowledge of the partner’s current decision. |
| **Outcomes** | – Investor’s net budget (‑cost if successful, ‑cost + no benefit if failure)  <br>– Transformer voltage level (improved only when ≥ threshold adopters) |
| **Payoffs (ordinal)** | 3 = high‑quality voltage **and** cost recovered (both invest)  <br>2 = good voltage **without** own cost (free‑ride)  <br>1 = moderate voltage (partial benefit when ≥ threshold reached elsewhere)  <br>0 = low voltage **and** cost sunk (solo invest) |
| **Strategic Tension** | **Strategic – Assurance / Coordination Game**. The payoff structure creates a *risk‑dominant* equilibrium (both Not‑Invest) and a *payoff‑dominant* equilibrium (both Invest). The tension is the classic “I will adopt only if enough neighbours adopt”. |
| **Temporal Structure** | Repeated **annually** (once per year a new adoption pool is drawn). Within a year the decision is a one‑shot simultaneous move. |
| **Relevant Rules** | • Boundary rule – only farmers attached to the same transformer can affect each other. <br>• Choice rule – “Invest” costs a fixed budget amount; “Not‑Invest” costs nothing. <br>• Control rule – voltage improvement occurs only when the number of “Invest” decisions on the transformer ≥ threshold τ. |

#### Normal‑Form Representation  

|                | **Farmer B: Invest** | **Farmer B: Not‑Invest** |
|----------------|----------------------|--------------------------|
| **Farmer A: Invest** | (3, 3) – both get high voltage, share cost  | (0, 2) – A pays cost, no benefit; B free‑rides on existing grid |
| **Farmer A: Not‑Invest** | (2, 0) – B pays cost, A free‑rides | (1, 1) – no investment, voltage stays low, no costs |

*Interpretation*: The cell (3,3) is the **coordinated adoption** equilibrium; (1,1) is the **mutual‑defection** equilibrium; the asymmetric cells represent unilateral investment (high personal loss, possible free‑ride gain).

---

### 2. Authorization Game – “Formal Connection Decision”

| Element | Description |
|---|---|
| **Title** | Authorization (Formal Connection) Game |
| **Location** | Sub‑station office & field (interaction between farmer and the staff member responsible for the transformer) |
| **Players** | (i) *Farmer* seeking a legal electricity connection  (ii) *Sub‑station staff* who can authorize or deny |
| **Roles** | Farmer = “Applicant”; Staff = “Gate‑keeper / Service provider” |
| **Actions** | **Farmer**: **Apply** (pay the authorization fee) or **Stay‑Illegal** (remain unauthorised). <br>**Staff**: **Authorize** (grant legal connection, incur monitoring cost) or **Ignore** (leave the connection informal). |
| **Control Rules** | – If *Apply* & *Authorize*: farmer receives a legal connection, pays fee **F**, staff receives a compliance bonus **B** (but also bears monitoring cost **C**). <br>– If *Apply* & *Ignore*: farmer pays fee **F** but receives no service; staff saves monitoring cost but risks detection penalty **P**. <br>– If *Stay‑Illegal* & *Authorize*: staff grants a “soft” connection (informal favor) – farmer avoids fee, staff gains informal rent **R** but raises detection risk. <br>– If *Stay‑Illegal* & *Ignore*: status‑quo – no fee, no formal service, low detection risk. |
| **Information** | Farmer knows its own budget, the typical fee **F**, and the observed frequency of staff authorizations (empirical estimate). Staff knows its own corruption level and the stochastic monitoring intensity (exogenous). Both have incomplete knowledge of the partner’s exact payoff. |
| **Outcomes** | – Legal connection status (yes/no)  <br>– Budget changes for farmer (‑F or 0)  <br>– Staff’s monitoring cost, informal rent, and probability of sanction |
| **Payoffs (ordinal)** | 3 = Farmer: legal connection **and** fee affordable; Staff: authorized + bonus (high compliance). <br>2 = Farmer: informal connection (no fee, some service); Staff: informal rent **R** (moderate). <br>1 = Farmer: pays fee but gets no service (waste); Staff: monitoring cost **C** with no benefit. <br>0 = Both stay illegal – low service, high risk of future enforcement for staff, and low productivity for farmer. |
| **Strategic Tension** | **Strategic – Asymmetric Conflict / Authorization Game**. The farmer’s best response depends on expected staff behavior, and staff’s willingness to authorize hinges on the farmer’s willingness to pay and the detection risk. |
| **Temporal Structure** | One‑shot **annual** decision (made once per year). The outcome persists for the whole simulation year. |
| **Relevant Rules** | • Boundary rule – only the staff assigned to the farmer’s transformer can authorize. <br>• Position rule – staff holds discretionary power (can grant informal favors). <br>• Choice rule – “Apply” incurs a fee; “Authorize” incurs monitoring cost. <br>• Control rule – detection probability is exogenous; sanction **P** applies if illegal authorisation is discovered. |

#### Normal‑Form Representation  

|                | **Staff: Authorize** | **Staff: Ignore** |
|----------------|----------------------|-------------------|
| **Farmer: Apply** | (3, 2) – farmer gets legal service, staff gets compliance bonus (2) | (1, 1) – farmer pays fee, gets nothing; staff bears monitoring cost |
| **Farmer: Stay‑Illegal** | (2, 3) – farmer gets informal service, staff gains rent **R** (high for staff) | (0, 0) – status‑quo, low payoff for both |

*Explanation*: The (3,2) cell is the **formal‑contract** equilibrium; (2,3) is the **informal‑collusion** equilibrium; the mixed cells are dominated for at least one player.

---

### 3. Capacity‑Provision Game – “Transformer Upgrade Investment”

| Element | Description |
|---|---|
| **Title** | Capacity‑Provision (Transformer Upgrade) Game |
| **Location** | Transformer yard (physical upgrade) and the associated sub‑station office |
| **Players** | (i) *Farmer* (or a *group of farmers* represented by a single “representative” farmer)  (ii) *Sub‑station staff* responsible for capacity decisions |
| **Roles** | Farmer = “Investor / Beneficiary”; Staff = “Capacity allocator / Service maintainer” |
| **Actions** | **Farmer**: **Contribute** (pay a share of the upgrade cost **U**) or **Free‑Ride** (pay nothing). <br>**Staff**: **Upgrade** (install additional transformer capacity) or **Do‑Nothing**. |
| **Control Rules** | – If *Contribute* & *Upgrade*: capacity increases, voltage stability improves for all farmers on the transformer; contributor bears cost **U**. <br>– If *Free‑Ride* & *Upgrade*: capacity improves, free‑rider enjoys benefit without cost; staff still incurs upgrade cost **Cᵤ**. <br>– If *Upgrade* & *All Free‑Ride*: staff may refuse to upgrade because cost is not covered (but staff can still invest at own expense, reflecting discretionary power). <br>– If *Do‑Nothing*: no capacity change, status‑quo voltage (low). |
| **Information** | Farmer knows its own budget and the typical share **U**; it observes whether the transformer is overloaded (high load indicator). Staff knows total contributions pledged and the exogenous monitoring intensity. |
| **Outcomes** | – Transformer capacity (high/low)  <br>– Farmer’s budget (‑U if contributed)  <br>– Staff’s expenditure **Cᵤ** and possible performance bonus **Bᵤ** if upgrade succeeds. |
| **Payoffs (ordinal)** | 3 = Farmer contributes **and** upgrade occurs (high voltage, cost incurred but offset by productivity gain). <br>2 = Farmer free‑rides **and** upgrade occurs (high voltage, no cost). <br>1 = Farmer contributes **but** upgrade does not occur (cost sunk, no benefit). <br>0 = No upgrade, low voltage for all. |
| **Strategic Tension** | **Strategic – Public‑Goods / Free‑Rider Game** (asymmetric because staff decides to upgrade only if contributions cover cost). |
| **Temporal Structure** | Annual **simultaneous** move (decisions made once per year). The capacity outcome persists for the remainder of the year. |
| **Relevant Rules** | • Boundary rule – only farmers attached to the transformer can contribute. <br>• Choice rule – “Contribute” costs **U**; “Upgrade” costs **Cᵤ** to staff. <br>• Control rule – upgrade succeeds only if total pledged contributions ≥ required cost **K** (parameter). |

#### Normal‑Form Representation  

|                | **Staff: Upgrade** | **Staff: Do‑Nothing** |
|----------------|--------------------|-----------------------|
| **Farmer: Contribute** | (3, 2) – farmer gets benefit, staff receives partial cost recovery (2) | (1, 0) – farmer pays cost, no capacity improvement |
| **Farmer: Free‑Ride** | (2, 1) – farmer enjoys benefit, staff bears full upgrade cost (low payoff) | (0, 0) – status‑quo, no cost, no benefit |

*Interpretation*: (3,2) is the **cooperative** outcome; (2,1) is a **free‑rider** equilibrium; (1,0) and (0,0) are **failed‑investment** outcomes.

---

### 4. Trust (Collusion) Exchange Game – “Reciprocal Favor‑Trading”

| Element | Description |
|---|---|
| **Title** | Trust / Collusion Exchange Game |
| **Location** | Field interaction at the farmer’s pump site and the sub‑station office (informal meeting) |
| **Players** | *Farmer* and *Sub‑station staff* (the same pair that may have an existing social tie) |
| **Roles** | Farmer = “Favour‑seeker”; Staff = “Favour‑giver” |
| **Actions** | **Farmer**: **Offer** (provide a small cash or material gift) or **Withhold**. <br>**Staff**: **Reciprocate** (grant an informal service – e.g., delayed billing, extra kWh) or **Refuse**. |
| **Control Rules** | – If both **Offer** & **Reciprocate**: a *trust* bond is strengthened; future interactions enjoy lower detection risk and higher informal rents. <br>– If Farmer **Offers** but Staff **Refuses**: farmer loses the gift (cost) and trust deteriorates. <br>– If Farmer **Withholds** but Staff **Reciprocates**: staff’s informal rent is given without compensation → staff may reduce future cooperation. <br>– If both **Withhold**/**Refuse**: no exchange, baseline relationship. |
| **Information** | Both know the historical frequency of successful exchanges in their dyad (memory of past ties). They do **not** know the partner’s exact willingness in the current period (bounded rationality). |
| **Outcomes** | – Change in dyadic trust level (high/medium/low). <br>– Immediate material transfer (gift cost **g** for farmer, informal rent **r** for staff). |
| **Payoffs (ordinal)** | 3 = Both cooperate – farmer’s crop yields improve (informal electricity discount) and staff gains rent **r** (high). <br>2 = Farmer offers, staff refuses – farmer loses gift **g** (low), staff keeps status‑quo (medium). <br>1 = Staff reciprocates, farmer withholds – staff’s rent wasted (low), farmer keeps budget (medium). <br>0 = No exchange – no gain for either side (baseline). |
| **Strategic Tension** | **Strategic – Trust Game** (asymmetric, sequential‑like but modeled as simultaneous because offers and reciprocation are decided without knowledge of the other’s move). The dilemma is whether to risk a costly gift for a potentially valuable informal service. |
| **Temporal Structure** | Repeated **annual** (once per year) simultaneous move; trust level carries over to the next year (dynamic). |
| **Relevant Rules** | • Boundary rule – only farmer–staff pairs that have interacted before can exchange gifts (emergent network). <br>• Choice rule – “Offer” costs **g**; “Reciprocate” yields rent **r**. <br>• Control rule – trust level updates: ↑ if both cooperate, ↓ if unilateral move. |

#### Normal‑Form Representation  

|                | **Staff: Reciprocate** | **Staff: Refuse** |
|----------------|------------------------|-------------------|
| **Farmer: Offer** | (3, 3) – mutual trust, high payoff for both | (2, 1) – farmer loses gift, staff gets nothing |
| **Farmer: Withhold** | (1, 2) – staff gives rent for free, farmer saves gift | (0, 0) – status‑quo, no exchange |

*Explanation*: (3,3) is the **trust‑building** equilibrium; (0,0) is the **no‑trust** equilibrium; the asymmetric cells capture the risk of unilateral generosity.

---

### 5. Groundwater Extraction (Common‑Pool Resource) Game – “Pump‑Rate Dilemma”

| Element | Description |
|---|---|
| **Title** | Groundwater Extraction Game (CPR) |
| **Location** | Aquifer basin shared by all farmers attached to a transformer (district‑level) |
| **Players** | Two *farmers* (representative of any pair drawing from the same aquifer) |
| **Roles** | Farmer = “Extractor” |
| **Actions** | **Pump‑Full** (extract at maximum legal rate) or **Restrict** (pump at a reduced, sustainable rate). |
| **Control Rules** | – If **both** **Restrict**: aquifer drawdown is low, pumping cost stays low, yields are moderate but sustainable → long‑term payoff. <br>– If one **Pump‑Full** while the other **Restricts**: the full‑pumper gets high immediate yield, the restrictor suffers lower water availability (lower yield). <br>– If **both** **Pump‑Full**: aquifer drawdown spikes, electricity‑pumping cost rises sharply (energy penalty **e**), yields drop for both after the period (over‑extraction). |
| **Information** | Farmers observe current groundwater depth (noisy) and the last period’s extraction outcome (public). They do **not** know the partner’s current decision. |
| **Outcomes** | – Immediate water volume extracted (high/medium/low). <br>– Future pumping cost (energy price) that depends on total extraction. |
| **Payoffs (ordinal)** | 3 = Both **Restrict** – sustainable yields, low energy cost (best long‑run). <br>2 = Unilateral **Pump‑Full** – high immediate water, but future cost rise (moderate). <br>1 = Both **Pump‑Full** – short‑term high water but severe over‑extraction → higher future cost, lower net benefit (low). <br>0 = Both **Restrict** but severe drought (exogenous) – yields collapse despite restraint (worst). |
| **Strategic Tension** | **Strategic – Common‑Pool Resource (Prisoner’s Dilemma‑type) Game**. Each farmer prefers to pump full while hoping the other restricts, but mutual restraint dominates in the long run. |
| **Temporal Structure** | **Annual** simultaneous move; the aquifer stock is updated each month, feeding back into the next year’s payoff. |
| **Relevant Rules** | • Boundary rule – all farmers sharing the same aquifer are part of the same CPR. <br>• Choice rule – “Pump‑Full” incurs higher energy cost **e** if total extraction exceeds a threshold **θ**. <br>• Control rule – aquifer level updates each month based on extracted volumes; depletion raises the marginal cost of pumping. |

#### Normal‑Form Representation  

|                | **Farmer B: Restrict** | **Farmer B: Pump‑Full** |
|----------------|------------------------|--------------------------|
| **Farmer A: Restrict** | (3, 3) – sustainable outcome | (1, 2) – A suffers low water, B gets high short‑term |
| **Farmer A: Pump‑Full** | (2, 1) – A gets high short‑term, B suffers | (0, 0) – over‑extraction, both lose (worst) |

*Interpretation*: (3,3) is the **cooperative restraint** equilibrium; (0,0) is the **mutual over‑extraction** equilibrium; the off‑diagonal cells capture the temptation to defect.

---

### 6. Social‑Learning & Imitation Process – “Observation‑Driven Adoption”

| Element | Description |
|---|---|
| **Title** | Social‑Learning (Imitation) Process |
| **Location** | Village‑level (farmers observe neighbours) |
| **Players** | *Individual farmer* (decision‑making unit) – **non‑strategic** (no simultaneous opponent) |
| **Roles** | Learner / Observer |
| **Actions** | **Imitate** (adopt the technology that the majority of observed neighbours have successfully used) or **Remain‑Status‑Quo** |
| **Control Rules** | – If the observed adoption rate on the farmer’s transformer exceeds a **threshold ι**, the farmer becomes *eligible* to imitate with probability **pᵢ** (fixed yearly). <br>– If the farmer imitates, the adoption cost is incurred; the benefit is realized only if the transformer’s overall adoption count reaches the DSM threshold τ in the same cycle (as in Situation 1). |
| **Information** | Farmers perfectly observe neighbours’ *adoption status* (visible hardware), but they have noisy beliefs about the resulting voltage improvement (subjective). |
| **Outcomes** | – Change in farmer’s technology state (adopted / not). <br>– Contribution to the transformer‑level adoption count. |
| **Payoffs (ordinal)** | 3 = Successful imitation (adoption + voltage benefit). <br>2 = Imitation but no benefit (threshold not met). <br>1 = No imitation, but future chance remains. <br>0 = Never imitates (stays low‑quality). |
| **Strategic Tension** | **Non‑strategic** (sequential observation). The tension is *informational*: the farmer must decide whether the observed success is sufficient evidence to risk the adoption cost. |
| **Temporal Structure** | Occurs **once per year** after the adoption pool is drawn; it is a *one‑way* process (no opponent). |
| **Relevant Rules** | • Boundary rule – only farmers on the same transformer are observable. <br>• Choice rule – “Imitate” incurs a one‑time cost. <br>• Control rule – eligibility depends on the aggregate adoption count (τ) and learning threshold ι. |

---

## Comparative Analysis of the Strategic Core

| Situation | Game Type (per ODD+D) | Core Dilemma | Symmetry | Main Asymmetry |
|---|---|---|---|---|
| **1 – DSM Coordination** | Assurance / Coordination | Risk of unilateral investment | Symmetric (both farmers) | Payoff depends on *joint* threshold |
| **2 – Authorization** | Asymmetric Conflict (Authorization) | Farmer must pay fee vs staff’s monitoring cost | Asymmetric (different roles) | Staff holds discretionary power |
| **3 – Capacity‑Provision** | Public‑Goods / Free‑Rider | Staff upgrades only if contributions cover cost | Asymmetric (contributor vs allocator) | Staff’s decision contingent on aggregate contributions |
| **4 – Trust/Collusion** | Trust Game (Reciprocal exchange) | Gift cost vs informal rent | Asymmetric (gift giver vs rent receiver) | History‑dependent trust level |
| **5 – Groundwater Extraction** | CPR / Prisoner’s Dilemma | Over‑extraction vs restraint | Symmetric (both extractors) | Environmental feedback (energy cost) |
| **6 – Social‑Learning** | Non‑strategic (sequential) | Information uncertainty vs adoption cost | N/A | None – no opponent |

### Redundancy Check & Revision

*Potential overlap*: Situations 1 (DSM Coordination) and 3 (Capacity‑Provision) both involve **public‑goods** provision on a transformer. However, the **source of the public good** and the **decision‑maker** differ:

| Aspect | Situation 1 | Situation 3 |
|---|---|---|
| **Good** | Voltage quality (technology‑dependent) | Physical capacity (infrastructure) |
| **Decision makers** | *Only* farmers (investment) | *Both* farmer (contribution) **and** staff (upgrade) |
| **Strategic tension** | Assurance (need enough adopters) | Free‑rider / cost‑recovery (staff’s willingness) |

Because the underlying strategic mechanisms (assurance vs free‑rider) are distinct, we keep both.

*Potential overlap*: Situation 4 (Trust/Collusion) and Situation 2 (Authorization) both involve farmer–staff dyads. Yet the **payoff structure** is different: Authorization is a formal‑policy decision with a fee vs monitoring cost; Trust/Collusion is an informal exchange of gifts and rents. The dilemmas (authorization vs trust) are therefore separate.

**Result:** All five strategic situations are **strategically diverse**; no further replacement is required.

---

## Full Set of Distinct Action Situations (5 strategic + 1 non‑strategic)

1. **DSM Coordination (Assurance) Game** – farmer‑farmer joint investment.  
2. **Authorization Game** – farmer vs staff on formal connection.  
3. **Capacity‑Provision Game** – farmer contribution vs staff upgrade decision.  
4. **Trust/Collusion Exchange Game** – farmer‑staff reciprocal gifting.  
5. **Groundwater Extraction (CPR) Game** – farmer‑farmer pump‑rate dilemma.  
6. **Social‑Learning & Imitation Process** – non‑strategic observation/adoption.

Each situation satisfies the ODD+D description, uses only **ordinal payoffs (0‑3)**, and reflects a **different governance interaction** in the electricity‑irrigation system of Andhra Pradesh.
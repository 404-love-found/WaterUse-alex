# Run 22 — openai/gpt-oss-120b

## 1.  Authorization Game – “Formal vs. Informal Connection”

| Element | Description |
|---|---|
| **Title** | Authorization Game |
| **Location** | Sub‑station office that processes connection requests for a given transformer service area |
| **Players** | 1️⃣ Farmer (seeking electricity)  <br>2️⃣ Sub‑station staff member (gate‑keeper) |
| **Roles** | Farmer – electricity consumer / potential payer of an authorization fee  <br>Staff – service provider / enforcer of the utility’s rule set |
| **Actions** | **Farmer:** *Apply* for a formal (authorized) connection or *Stay* with the existing informal connection. <br>**Staff:** *Authorize* the connection (grant record & allocate capacity) or *Reject* (leave the farmer in the informal sector). |
| **Control Rules** | – If the farmer applies **and** the staff authorizes, the farmer pays the fee, the connection becomes recorded, and the transformer’s effective capacity is increased by the farmer’s contribution. <br>– If the farmer applies but staff rejects, the farmer remains informal and pays no fee but continues to face a penalty risk. <br>– If the farmer stays informal, the staff’s decision is irrelevant (status‑quo). |
| **Information** | Farmer knows the current fee, the probability of detection, and the observed reliability of informal supply (noisy). <br>Staff knows the farmer’s payment ability, the current load on the transformer, and the oversight intensity (partial). |
| **Outcomes** | – Formal connection recorded (capacity ↑, reliability ↑). <br>– Informal connection persists (no capacity contribution, higher overload risk). <br>– Possible penalty for informal use (if enforcement later occurs). |
| **Payoffs** (ordinal 0 = least preferred, 3 = most preferred) | See payoff matrix below. |
| **Strategic Tension** | **Strategic (Authorization / Coordination game).**  The farmer wants the security of a formal connection but must bear a cost; the staff wants to keep workload low and avoid illegal connections but also benefits from the fee and from a better‑recorded load.  The tension is between *co‑operation* (both choose the formal route) and *defection* (farmer stays informal, staff rejects). |
| **Temporal Structure** | Repeated annually – the same farmer–staff pair can renegotiate each irrigation year. |
| **Relevant Rules** | Boundary rule: only farmers attached to the transformer are eligible. <br> Position rule: staff can only authorize if the transformer has spare capacity (τ). <br> Choice rule: farmer decides to apply or not; staff decides to authorize or reject. <br> Control rule: authorized connection updates the transformer‑capacity variable. |

### 2‑player normal‑form (ordinal)  

|                     | **Staff – Authorize** | **Staff – Reject** |
|---------------------|-----------------------|--------------------|
| **Farmer – Apply**  | (3 , 2)  *Farmer gets secure supply (3), staff gains fee + capacity (2)* | (1 , 1)  *Farmer pays fee but gets no connection (1), staff wastes effort (1)* |
| **Farmer – Stay**   | (2 , 0)  *Farmer keeps cheap informal supply (2), staff loses fee (0)* | (2 , 0)  *Same as left because staff decision irrelevant (0 for staff)* |

*Explanation*: The highest joint outcome (3,2) occurs when both cooperate – the farmer pays and receives a formal connection, the staff collects the fee and improves load information. The worst for the farmer is (1,1) – paying a fee but being denied, while the staff expends effort for no gain. Staying informal yields a moderate payoff (2) for the farmer (cheap electricity) but gives the staff nothing (0).

---

## 2.  Collusion Exchange Game – “Reciprocal Informal Favor”

| Element | Description |
|---|---|
| **Title** | Collusion Exchange Game |
| **Location** | On‑site interaction at the transformer (farm gate) and informal “meeting points” (village) |
| **Players** | 1️⃣ Farmer (seeking informal tolerance)  <br>2️⃣ Sub‑station staff member (holding discretionary enforcement power) |
| **Roles** | Farmer – electricity consumer who can offer a “favor” (e.g., cash, political support). <br>Staff – enforcer who can *Tolerate* informal use or *Enforce* the rule. |
| **Actions** | **Farmer:** *Offer* a small informal payment/favor or *Not Offer*. <br>**Staff:** *Tolerate* the informal connection (accept the favor) or *Enforce* (inspect, issue penalty). |
| **Control Rules** | – If the farmer offers **and** staff tolerates, the informal connection continues without penalty; staff receives a personal benefit (informal payment). <br>– If the farmer offers but staff enforces, the farmer loses the payment and may be penalised; staff incurs a reputational cost for breaking a tacit norm. <br>– If the farmer does not offer and staff tolerates, the staff loses a potential informal gain; if staff enforces, the farmer faces a penalty. |
| **Information** | Farmer knows the staff’s past tolerance level (δ) but not the exact detection probability. <br>Staff knows the farmer’s financial strain and the current monitoring intensity (stochastic). |
| **Outcomes** | – Continued informal supply with a hidden side‑payment. <br>– Penalty imposed on farmer; staff may gain formal compliance credit but lose informal benefit. |
| **Payoffs** | Ordinal matrix below. |
| **Strategic Tension** | **Strategic (Trust / Collusion game).**  Both need the other’s cooperation to reap the hidden benefit; unilateral offering or unilateral tolerance is risky. |
| **Temporal Structure** | Repeated each year; the history of past offers builds the trust level (δ). |
| **Relevant Rules** | Boundary rule: only farmers already connected informally are eligible. <br> Position rule: staff’s discretion is limited by oversight intensity (γ). <br> Choice rule: farmer chooses to offer or not; staff chooses tolerance or enforcement. |

### 2‑player normal‑form (ordinal)

|                     | **Staff – Tolerate** | **Staff – Enforce** |
|---------------------|----------------------|---------------------|
| **Farmer – Offer**  | (3 , 3)  *Both get hidden benefit (farmer keeps electricity, staff gets side‑payment)* | (0 , 1)  *Farmer loses payment and may be penalised (0); staff suffers reputational loss (1)* |
| **Farmer – Not Offer** | (1 , 0)  *Farmer keeps cheap electricity (1), staff gets no side‑payment (0)* | (2 , 2)  *Farmer gets penalised (2 = moderate loss), staff gains formal compliance credit (2)* |

*Explanation*: The mutually cooperative outcome (3,3) is the classic “trust” equilibrium – the farmer’s offer is honoured and the staff tolerates. If the farmer offers but the staff enforces, the farmer suffers the worst (0) while the staff gets a small gain (1) from showing strictness. When the farmer does not offer, toleration leaves the staff empty‑handed (0) and the farmer only modestly better off (1). Enforcement without an offer gives the staff a moderate payoff (2) for upholding rules, while the farmer suffers a moderate loss (2).

---

## 3.  DSM Coordination Game – “Capacitor Adoption Assurance”

| Element | Description |
|---|---|
| **Title** | DSM Coordination Game (Capacitor Adoption) |
| **Location** | Within a single transformer service area (village‑level) |
| **Players** | 1️⃣ Farmer A (potential adopter)  <br>2️⃣ Farmer B (neighbor in the same transformer group) |
| **Roles** | Both are electricity consumers who can invest in a capacitor that stabilises voltage for the whole group. |
| **Actions** | **Each farmer:** *Invest* in a capacitor (pay the upfront cost) or *Not Invest*. |
| **Control Rules** | – If **both** invest, the transformer voltage improves markedly; each farmer enjoys a large reliability boost while sharing the cost. <br>– If **only one** invests, the voltage gain is negligible; the investor bears the full cost with little benefit. <br>– If **none** invest, voltage remains low (status‑quo). |
| **Information** | Farmers observe whether the neighbour invested in the previous year (visible) but do not know the neighbour’s current intention. They have noisy signals about voltage quality (i). |
| **Outcomes** | – High reliability & lower pump wear (both invest). <br>– Private loss for unilateral investor. <br>– No change for mutual non‑investment. |
| **Payoffs** | Ordinal matrix below. |
| **Strategic Tension** | **Strategic (Assurance / Coordination game).**  The best joint outcome requires simultaneous investment, but each farmer fears being the sole investor. |
| **Temporal Structure** | Repeated annually; past adoption informs expectations (learning parameter ι). |
| **Relevant Rules** | Boundary rule: only farmers attached to the same transformer can affect each other’s voltage. <br> Position rule: the benefit of a capacitor is a function of the number of adopters (τ). <br> Choice rule: each farmer decides to invest or not each year. |

### 2‑player normal‑form (ordinal)

|                     | **Farmer B – Invest** | **Farmer B – Not Invest** |
|---------------------|-----------------------|---------------------------|
| **Farmer A – Invest** | (3 , 3)  *Both get high reliability (3)* | (0 , 2)  *A pays cost alone (0); B enjoys slight indirect benefit (2)* |
| **Farmer A – Not Invest** | (2 , 0)  *B pays alone (0); A enjoys slight indirect benefit (2)* | (1 , 1)  *Both stay low‑reliability (1)* |

*Explanation*: Mutual investment yields the top rank (3,3). Unilateral investment gives the investor the worst rank (0) because the cost is not offset by voltage improvement, while the non‑investor gets a modest benefit (2) from the neighbour’s capacitor (some spill‑over). Mutual non‑investment is a low but stable outcome (1,1).

---

## 4.  Groundwater Extraction Game – “Common‑Pool Pumping”

| Element | Description |
|---|---|
| **Title** | Groundwater Extraction Game |
| **Location** | Shared aquifer underlying a district of villages (hydro‑geological basin) |
| **Players** | 1️⃣ Farmer X (pump operator)  <br>2️⃣ Farmer Y (neighboring pump operator) |
| **Roles** | Both are water users who decide how much groundwater to extract for irrigation. |
| **Actions** | **Each farmer:** *High* extraction (pump at full rate) or *Low* extraction (restrain pumping). |
| **Control Rules** | – The aquifer’s depth (γ) rises with total extraction. <br>– High extraction raises immediate crop yield but also increases future pumping costs for **both**. <br>– Low extraction reduces current yield but helps keep the water table shallower, lowering future costs. |
| **Information** | Each farmer knows the current groundwater depth (observable) but not the neighbour’s intended extraction level for the current year. |
| **Outcomes** | – Short‑term yield (higher for high extraction). <br>– Long‑term cost (higher for both if total extraction is high). |
| **Payoffs** | Ordinal matrix below. |
| **Strategic Tension** | **Strategic (Common‑Pool Resource / Tragedy of the Commons).**  The dominant individual incentive is to extract heavily, but mutual restraint yields a better long‑run outcome. |
| **Temporal Structure** | Repeated annually; the aquifer depth evolves each year (feedback). |
| **Relevant Rules** | Boundary rule: only farmers whose wells tap the same aquifer are players. <br> Position rule: extraction cost depends on cumulative drawdown (γ). <br> Choice rule: each farmer selects extraction level each irrigation cycle. |

### 2‑player normal‑form (ordinal)

|                     | **Farmer Y – High** | **Farmer Y – Low** |
|---------------------|---------------------|--------------------|
| **Farmer X – High** | (1 , 1)  *Both enjoy high yield now but future cost rises (low rank)* | (2 , 3)  *X gets high yield (2); Y benefits from lower future cost (3)* |
| **Farmer X – Low**  | (3 , 2)  *X enjoys lower future cost (3); Y gets high yield (2)* | (4 ? – cannot exceed 3) – we must keep 0‑3. Use (3 , 3) for mutual restraint (best long‑run). |

Corrected matrix using 0‑3 only:

|                     | **Farmer Y – High** | **Farmer Y – Low** |
|---------------------|---------------------|--------------------|
| **Farmer X – High** | (1 , 1)  *Both over‑extract → short‑term gain, long‑term loss* | (2 , 3)  *X over‑extracts, Y restrains → X gets short‑term benefit (2), Y secures long‑term benefit (3)* |
| **Farmer X – Low**  | (3 , 2)  *X restrains, Y over‑extracts → X gets long‑term benefit (3), Y gets short‑term (2)* | (3 , 3)  *Both restrain → best sustainable outcome* |

*Explanation*: The highest joint rank (3,3) occurs when both limit extraction. Unilateral high extraction gives the extractor a moderate rank (2) while the restrainer enjoys the best (3) because the water table stays higher. Mutual high extraction is the worst (1,1).

---

## 5.  Maintenance Investment Game – “Staff‑Farmer Maintenance Coordination”

| Element | Description |
|---|---|
| **Title** | Maintenance Investment Game |
| **Location** | Sub‑station workshop and field sites of a transformer service area |
| **Players** | 1️⃣ Sub‑station staff member (maintenance decision‑maker)  <br>2️⃣ Farmer C (who can reduce load by voluntarily limiting pumping) |
| **Roles** | Staff – provider of preventive maintenance/capacity upgrades. <br>Farmer – consumer who can either **Co‑operate** (reduce pump load) or **Ignore** (pump at full rate). |
| **Actions** | **Staff:** *Invest* in preventive maintenance (e.g., replace aging transformer components) or *Do‑Nothing*. <br>**Farmer:** *Reduce* load (pump at a lower rate, accept lower short‑term yield) or *Maintain* current high pump rate. |
| **Control Rules** | – If staff invests **and** farmer reduces load, transformer reliability improves markedly (low failure risk). <br>– If staff invests but farmer does not reduce load, the maintenance benefit is partially eroded; failure risk falls only modestly. <br>– If staff does nothing, reliability declines regardless of farmer behaviour, but a farmer who reduces load still gains a small reliability boost. |
| **Information** | Staff knows its own workload and the stochastic monitoring intensity; it only observes aggregate load, not individual farmer’s intended reduction. <br>Farmer observes recent transformer failures (noisy) and knows the staff’s typical maintenance schedule. |
| **Outcomes** | – Transformer failure probability (high/medium/low). <br>– Farmer’s crop yield (affected by load reduction). <br>– Staff effort cost (high if invests). |
| **Payoffs** | Ordinal matrix below. |
| **Strategic Tension** | **Strategic (Public‑Goods / Coordination game).**  Maintenance is a public good; the staff bears the cost, the farmer can help by reducing load.  The best joint outcome requires both to act, but each may prefer to free‑ride. |
| **Temporal Structure** | One‑shot each year (maintenance decision made once per cycle). |
| **Relevant Rules** | Boundary rule: only farmers attached to the transformer are considered. <br> Position rule: staff’s capacity to invest depends on current workload (τ). <br> Choice rule: staff decides to invest or not; farmer decides to cut load or not. |

### 2‑player normal‑form (ordinal)

|                     | **Farmer – Reduce** | **Farmer – Maintain** |
|---------------------|---------------------|-----------------------|
| **Staff – Invest**  | (3 , 3)  *Both get high reliability (3)* | (2 , 1)  *Staff pays cost, farmer sees little gain (1)* |
| **Staff – Do‑Nothing** | (1 , 2)  *Farmer reduces load (2) but no maintenance, staff avoids effort (1)* | (0 , 0)  *Both suffer low reliability (0)* |

*Explanation*: Mutual investment + load reduction yields the top rank (3,3). If staff invests but farmer does not reduce, staff’s effort is only partially rewarded (2) while farmer gets little benefit (1). If staff does nothing and farmer reduces, the farmer still gains a modest reliability improvement (2) but staff gets a low rank (1) for avoiding effort. Mutual inaction is the worst (0,0).

---

## 6.  Social‑Learning Process – “Observation → Imitation”

| Element | Description |
|---|---|
| **Title** | Social‑Learning Process (Non‑strategic) |
| **Location** | Village‑level social network (neighbors sharing the same transformer) |
| **Players** | *All* farmers in a transformer group (simultaneous observers) |
| **Roles** | Observers – each farmer watches visible outcomes of neighbours’ technology choices (capacitor adoption, pump quality). |
| **Actions** | **No decision** in this step; the process is *sequential*: after the previous year’s outcomes are realized, each farmer updates an **imitation propensity** (probability to adopt the observed successful technology in the next cycle). |
| **Control Rules** | – If a farmer observes a neighbour who adopted a capacitor and subsequently reports higher crop yield / fewer pump failures, the observer’s imitation probability increases (by a factor linked to the learning constraint ι). <br>– If observed adoption fails (no improvement or negative side‑effects), the probability decreases. |
| **Information** | Perfect observation of neighbours’ *adoption status* (binary) but noisy perception of the *outcome* (e.g., mis‑attributing a yield increase to the capacitor). |
| **Outcomes** | Updated imitation probabilities that feed into the **DSM Coordination Game** (Section 3) for the next year. |
| **Payoffs** | Not applicable (non‑strategic). The “payoff” is the updated likelihood of successful future adoption, which indirectly affects future utility. |
| **Strategic Tension** | **Non‑strategic** – there is no simultaneous move; it is a sequential learning process that shapes later strategic games. |
| **Temporal Structure** | Occurs once per year, after the physical and institutional outcomes are observed. |
| **Relevant Rules** | Boundary rule: only farmers within the same transformer service area are observable. <br> Position rule: learning speed is limited by the parameter ι (visibility of successful adoption). <br> Choice rule: none (the process updates internal state). |

---

# Comparative Analysis of the Strategic Core

| Game | Player Types | Core Dilemma | Payoff Pattern (Ranks) | Distinctive Feature |
|------|--------------|--------------|------------------------|---------------------|
| **Authorization** | Farmer ↔ Staff | *Co‑operation vs. Defection* (formalisation) | (3,2) > (2,0) > (1,1) > (0,0) | Involves a **fee** and **record‑keeping**; the staff’s payoff depends on revenue, not just enforcement. |
| **Collusion Exchange** | Farmer ↔ Staff | *Trust / Mutual Informal Benefit* | (3,3) > (2,2) > (1,0) > (0,1) | Hidden side‑payment; risk of detection introduces an *asymmetric* loss when offers are not reciprocated. |
| **DSM Coordination** | Farmer ↔ Farmer | *Assurance / Coordination* (capacitator) | (3,3) > (2,2) > (1,1) > (0,2) / (2,0) | Benefits are **non‑excludable** but only materialise when **both** invest; unilateral investment is punished. |
| **Groundwater Extraction** | Farmer ↔ Farmer | *Common‑Pool / Tragedy* | (3,3) > (3,2) / (2,3) > (1,1) | Future‑oriented cost externality; the payoff matrix is **asymmetric** because the high extractor gains short‑term advantage. |
| **Maintenance Investment** | Staff ↔ Farmer | *Public‑Good / Coordination* (maintenance + load‑reduction) | (3,3) > (2,1) / (1,2) > (0,0) | Staff bears the **up‑front cost**, farmer can *free‑ride* by not reducing load; the reverse free‑ride (farmer reduces load while staff does nothing) yields a modest farmer payoff. |

### Similarities & Differences

| Similarity | Games sharing it | Why it matters |
|------------|-------------------|----------------|
| **Same player set (Farmer‑Staff)** | Authorization & Collusion Exchange | Both involve a *power asymmetry* but differ: Authorization is a *formal* rule‑based transaction (fee, capacity), whereas Collusion is an *informal* trust‑based exchange. |
| **Public‑good nature** | Maintenance Investment & Authorization (capacity contribution) | Both create a shared infrastructure benefit, yet the *source of cost* differs (staff effort vs. farmer fee). |
| **Coordination requirement** | DSM Coordination & Groundwater Extraction (both need simultaneous restraint) | However, DSM is a *technology* coordination with a binary adoption decision, while Groundwater is a *resource‑use* coordination with continuous externalities. |
| **Asymmetric payoff structures** | Collusion Exchange (trust) & Groundwater Extraction (short‑term vs. long‑term) | These asymmetries generate distinct strategic cores (trust vs. tragedy). |

### Ensuring Strategic Diversity

The original set contained two farmer‑staff games that could be viewed as variations of a “formal‑informal” dilemma (Authorization and Capacity Provision). To avoid redundancy, **Capacity Provision** was replaced by the **Maintenance Investment Game** (Section 5). This new game introduces a *staff‑cost* dimension and a *farmer load‑reduction* decision that is not present in the Authorization or Collusion games, thereby expanding the strategic repertoire.

---

# Final Set of Distinct Action Situations

1. **Authorization Game** – Formal vs. informal connection (farmer vs. staff).  
2. **Collusion Exchange Game** – Hidden reciprocal favors (farmer vs. staff).  
3. **DSM Coordination Game** – Joint capacitor adoption (farmer vs. farmer).  
4. **Groundwater Extraction Game** – High vs. low pumping (farmer vs. farmer).  
5. **Maintenance Investment Game** – Staff preventive maintenance vs. farmer load‑reduction (staff vs. farmer).  
6. **Social‑Learning Process** – Observation → imitation (non‑strategic, farmer‑wide).  

Each situation satisfies the IAD requirements, presents a unique governance interaction, and is described with the full set of elements requested, including 2 × 2 ordinal payoff matrices for all strategic games.
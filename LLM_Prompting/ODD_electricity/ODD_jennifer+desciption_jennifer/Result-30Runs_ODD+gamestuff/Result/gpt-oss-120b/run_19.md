# Run 19 — openai/gpt-oss-120b

## 1.  DSM‑Coordination (Capacitor Adoption) Game  

| Element | Description |
|---|---|
| **Title** | **DSM‑Coordination (Capacitor Adoption) Game** |
| **Location** | Transformer service‑area (village‑level) – the physical point where voltage quality is experienced by all farmers attached to the same transformer. |
| **Players** | Two representative *farmers* that share the same transformer (the game is replicated for every unordered pair of neighbours on that transformer). |
| **Roles** | *Farmer A* – electricity consumer / pump operator.<br>*Farmer B* – electricity consumer / pump operator. |
| **Actions** | **Invest** – purchase and install a capacitor (pay a one‑off cost).<br>**Not‑Invest** – keep the status‑quo (no cost, no direct benefit). |
| **Control Rules** | • If **both** invest, voltage stability improves for the whole transformer; each investor receives a *shared* reliability boost (lower pump‑failure risk).  <br>• If **only one** invests, the voltage gain is marginal (the lone capacitor cannot compensate the aggregate load) → the investor bears the cost but sees little benefit. <br>• If **neither** invests, voltage remains low; all suffer higher pump‑failure risk. |
| **Information** | Each farmer knows the *historical* adoption rate on the transformer (e.g., “30 % of neighbours have capacitors”) but does **not** know the partner’s current decision. Information is *partial* and *noisy* because the effect of a neighbour’s capacitor on one’s own voltage is uncertain. |
| **Outcomes** | 1. **Improved voltage** (both invest).<br>2. **Marginal/No improvement** (one invests).<br>3. **Persistently poor voltage** (none invest). |
| **Payoffs** (ordinal, 0 = worst, 3 = best) | See the payoff matrix below. The first number is Farmer A’s rank, the second is Farmer B’s. |
| **Strategic Tension** | **Strategic – Coordination (Assurance) Game**.  Both would like the other to invest because the benefit is *joint* but the cost is private.  The game has two pure‑strategy Nash equilibria: (Invest, Invest) (high‑payoff coordination) and (Not‑Invest, Not‑Invest) (low‑payoff coordination). |
| **Temporal Structure** | Repeated **annually** (the decision is revisited each irrigation year).  Past outcomes feed the learning rule that determines the probability of being drawn into the “imitation pool”. |
| **Relevant Rules** | *Boundary rule*: only farmers attached to the same transformer are paired.<br>*Choice rule*: each farmer may adopt at most once; once a capacitor is bought it is permanent.<br>*Control rule*: the shared voltage improvement is a function of the number of adopters on the transformer (τ). |

### Payoff Matrix  

|                     | **Farmer B Invest** | **Farmer B Not‑Invest** |
|---------------------|---------------------|--------------------------|
| **Farmer A Invest** | (3, 3) – joint coordination, both enjoy reliable electricity and avoid pump failures. | (1, 2) – A pays the cost, gets little voltage gain; B enjoys a small spill‑over without cost. |
| **Farmer A Not‑Invest** | (2, 1) – symmetric to the previous cell (B bears cost). | (0, 0) – no investment, poor voltage for both. |

*Why the numbers?*  
- (3,3) is the **most preferred** outcome for both because the shared benefit outweighs the private cost.  
- (1,2) and (2,1) reflect **asymmetric** outcomes where the investor is worse off (cost > benefit) while the free‑rider gets a modest improvement.  
- (0,0) is the **least preferred** (high pump‑failure risk, no improvement).

---

## 2.  Authorization Game (Formal vs. Informal Connection)

| Element | Description |
|---|---|
| **Title** | **Authorization Game** |
| **Location** | Sub‑station office – the point where staff process connection requests and decide on capacity allocation. |
| **Players** | *Farmer* (seeking electricity) and *Sub‑station staff* (gate‑keeper). |
| **Roles** | Farmer – electricity consumer, applicant for a **formal** connection.<br>Staff – service provider / enforcer with discretionary power over authorisation and capacity investment. |
| **Actions** | **Farmer**: <br>• **Apply** for a formal, authorised connection (pays fee, expects reliable service).<br>• **Stay‑informal** (use illegal line, avoid fee).<br>**Staff**: <br>• **Grant** – approve the connection, allocate capacity, record the link.<br>• **Deny** – refuse formalisation (may tolerate informal use). |
| **Control Rules** | • If *Apply* + *Grant*: farmer pays fee, receives reliable service; staff incurs effort cost but gains informal “reciprocity” benefit (δ).<br>• If *Apply* + *Deny*: farmer loses fee, remains informal; staff saves effort but may incur reputational loss (γ).<br>• If *Stay‑informal* + *Grant*: staff grants a connection without fee (rare, reflects corruption); farmer gets reliable service for free, staff gains illicit benefit (δ).<br>• If *Stay‑informal* + *Deny*: status‑quo; farmer keeps informal line (lower cost, higher risk of penalty); staff saves effort. |
| **Information** | Farmer knows the *current monitoring intensity* (probability of detection) and the *average grant rate* from past years (partial). Staff knows the farmer’s *financial strain* (observed via bill arrears) and the *local collusion density* (δ). Both have **no perfect knowledge** of the other’s immediate payoff. |
| **Outcomes** | 1. Formal connection with fee (stable supply).<br>2. Informal connection with possible future penalty.<br>3. Corrupt grant (free formal connection).<br>4. Denial – no change. |
| **Payoffs** | Ordinal ranks (0–3) shown in the matrix below. |
| **Strategic Tension** | **Strategic – Authorization (Hybrid of Trust & Public‑Goods) Game**.  The farmer wants the staff to *grant* while the staff balances formal compliance, effort cost, and illicit gain.  The interaction can generate a **prisoner’s‑dilemma‑type** tension when staff consider the risk of being caught for corruption. |
| **Temporal Structure** | One‑shot **annual** decision (made at the start of the irrigation cycle).  The outcome persists for the whole year. |
| **Relevant Rules** | *Boundary rule*: only farmers without an existing authorised line are eligible.<br>*Choice rule*: each farmer can attempt to apply at most once per year; staff can grant at most a limited number of new connections (capacity constraint τ). |

### Payoff Matrix  

|                     | **Staff Grant** | **Staff Deny** |
|---------------------|-----------------|----------------|
| **Farmer Apply**    | (3, 2) – farmer gets reliable service (rank 3); staff incurs effort but gains future “reciprocity” (rank 2). | (1, 3) – farmer loses fee, stays informal (rank 1); staff avoids effort and preserves reputation (rank 3). |
| **Farmer Stay‑informal** | (2, 1) – farmer receives free formal service (rank 2); staff gains illicit benefit but risks detection (rank 1). | (0, 0) – status‑quo, low reliability for farmer (rank 0); staff saves effort (rank 0). |

*Interpretation* – The highest joint rank (3,2) is achieved when the farmer follows the formal route and the staff cooperates; the worst joint rank (0,0) occurs when both stay informal and no service improvement occurs.

---

## 3.  Collusion‑Exchange (Trust) Game  

| Element | Description |
|---|---|
| **Title** | **Collusion‑Exchange (Trust) Game** |
| **Location** | Farmer’s field *and* sub‑station office – the informal “meeting point” where a farmer and a staff member negotiate a reciprocal favour (e.g., tolerance of an illegal line in exchange for a cash kick‑back). |
| **Players** | *Farmer* (seeker of informal favour) and *Sub‑station staff* (potential provider). |
| **Roles** | Farmer – client, potential *trustor*.<br>Staff – gate‑keeper, potential *trustee*. |
| **Actions** | **Farmer**: <br>• **Offer** a kick‑back (or other favour).<br>• **Refuse** (no informal payment).<br>**Staff**: <br>• **Accept** the kick‑back and tolerate the informal connection.<br>• **Reject** (enforce rules, no tolerance). |
| **Control Rules** | • If *Offer* + *Accept*: farmer pays a small cost, receives informal tolerance (no penalty, smoother electricity). Staff gains illicit benefit (δ) but incurs risk of detection (γ).<br>• If *Offer* + *Reject*: farmer loses the offered amount, receives no tolerance (possible penalty). Staff avoids risk but may damage the relationship (loss of future informal benefits).<br>• If *Refuse* + *Accept*: staff’s acceptance is moot; no exchange occurs (status‑quo).<br>• If *Refuse* + *Reject*: both keep the status‑quo; no costs, no benefits. |
| **Information** | Farmer knows the *current monitoring intensity* (probability of detection) and the *staff’s past willingness* (observed through previous exchanges). Staff knows the farmer’s *financial strain* and the *local norm of reciprocity* (δ). Both have **no perfect knowledge** of the partner’s exact payoff. |
| **Outcomes** | 1. Successful collusion (informal tolerance).<br>2. Failed collusion – farmer penalised.<br>3. No collusion – status‑quo. |
| **Payoffs** | Ordinal (0–3) matrix below. |
| **Strategic Tension** | **Strategic – Trust Game**.  Both parties must decide whether to *trust* the other to honour the informal bargain.  The game is asymmetric: the farmer bears a cost up‑front, the staff reaps a benefit only if they accept.  The equilibrium is typically **inefficient** (both refuse) unless the perceived risk of detection is low. |
| **Temporal Structure** | One‑shot **annual** (the collusion tie is re‑evaluated each year). |
| **Relevant Rules** | *Boundary rule*: only farmers who already have an informal line can propose a kick‑back.<br>*Choice rule*: staff can accept at most a limited number of collusive deals per transformer (capacity τ). |

### Payoff Matrix  

|                     | **Staff Accept** | **Staff Reject** |
|---------------------|------------------|-------------------|
| **Farmer Offer**    | (2, 3) – farmer pays small cost (rank 2) but gains tolerance; staff gets illicit benefit (rank 3). | (0, 1) – farmer loses money (rank 0); staff avoids risk (rank 1). |
| **Farmer Refuse**   | (1, 2) – farmer saves money (rank 1); staff’s acceptance is wasted (rank 2). | (3, 0) – farmer enjoys full reliability (rank 3); staff gets nothing and no risk (rank 0). |

*Explanation* – The most preferred outcome for the staff (3) is to accept a kick‑back; the farmer’s top rank (3) is achieved when the staff *rejects* (i.e., enforces) because the farmer avoids the payment and still has a legal connection (if already authorised).  The matrix captures the classic trust‑dilemma asymmetry.

---

## 4.  Groundwater Extraction (Common‑Pool Resource) Game  

| Element | Description |
|---|---|
| **Title** | **Groundwater Extraction (CPR) Game** |
| **Location** | Village‑level groundwater basin (hydro‑geological unit). |
| **Players** | Two *farmers* drawing water from the same aquifer. |
| **Roles** | Farmer A – pump operator, water user.<br>Farmer B – pump operator, water user. |
| **Actions** | **High** – pump at the maximum feasible rate (maximise current yield).<br>**Low** – restrain extraction (reduce current yield) to conserve the aquifer. |
| **Control Rules** | • The aquifer depth **increases** with total extraction (γ).<br>• Higher depth raises the *energy cost* of pumping for **both** players in the next year (τ).<br>• If the aquifer is over‑extracted, the probability of a *pump‑failure* rises for everyone (affects payoff). |
| **Information** | Each farmer observes the *current groundwater depth* (noisy estimate) and the *last year’s total extraction* (inferred from neighbours’ visible water‑use).  Information is **partial**; they cannot perfectly observe the partner’s exact extraction level. |
| **Outcomes** | 1. **Both extract high** – short‑term high yields, rapid aquifer depletion, future cost rise.<br>2. **One high / one low** – high‑extractor enjoys current gain, low‑extractor saves future costs.<br>3. **Both low** – modest current yields, slower depletion, lower future costs. |
| **Payoffs** | Ordinal ranks (0–3) shown in the matrix. |
| **Strategic Tension** | **Strategic – Common‑Pool Resource (Tragedy of the Commons) Game**.  The dominant individual strategy is *High* (higher immediate rank), but the joint *Low‑Low* outcome is socially optimal.  The game is a **prisoner’s‑dilemma** in ordinal form. |
| **Temporal Structure** | Repeated **annually**; the aquifer depth evolves over time, feeding back into next‑year payoffs. |
| **Relevant Rules** | *Boundary rule*: only farmers sharing the same basin are paired.<br>*Control rule*: extraction adds to a stock variable (groundwater depth) that feeds back into the cost of pumping (γ). |

### Payoff Matrix  

|                     | **Farmer B High** | **Farmer B Low** |
|---------------------|-------------------|-------------------|
| **Farmer A High**   | (2, 2) – both enjoy high current yield but incur future cost (moderate rank). | (3, 1) – A gets high yield (rank 3); B restrains and suffers lower current yield (rank 1). |
| **Farmer A Low**    | (1, 3) – symmetric to previous cell. | (0, 0) – both restrain; current yield low (rank 0) but future sustainability high (ordinally ranked lowest for immediate payoff). |

*Why (0,0) is the lowest*: The model uses **ordinal** preferences that place immediate water volume above future sustainability; thus “low now” is ranked worst for the current decision horizon, even though it would be best in a long‑run utility sense.  This captures the observed short‑term bias of farmers.

---

## 5.  Transformer‑Maintenance (Staff‑Farmer) Game  

| Element | Description |
|---|---|
| **Title** | **Transformer‑Maintenance Game** |
| **Location** | Sub‑station (maintenance workshop) – the point where staff allocate effort to repair or upgrade a transformer serving a group of farmers. |
| **Players** | *Sub‑station staff* (maintenance manager) and a *representative farmer* (who can **report** a failure or **stay silent**). |
| **Roles** | Staff – service provider / enforcer of infrastructure reliability.<br>Farmer – electricity consumer, potential *monitor* of transformer performance. |
| **Actions** | **Staff**: <br>• **Maintain** – allocate effort (cost) to repair/upgrade the transformer now.<br>• **Delay** – postpone maintenance (save effort).<br>**Farmer**: <br>• **Report** a failure (incurs a small reporting cost, raises detection risk).<br>• **Silent** – do not report (no cost, but failure persists). |
| **Control Rules** | • If *Report* + *Maintain*: failure is fixed quickly; farmer’s pump reliability improves, staff bears effort cost but gains reputation (δ).<br>• If *Report* + *Delay*: failure persists, farmer suffers loss, staff avoids effort but accrues reputational penalty (γ).<br>• If *Silent* + *Maintain*: staff repairs unnecessarily (wasted effort), farmer gains reliability for free (rank 2).<br>• If *Silent* + *Delay*: status‑quo; transformer may burn out (risk τ). |
| **Information** | Farmer knows the *current voltage quality* and the *probability that a report will trigger maintenance* (partial). Staff knows the *reported failure rate* (observed) and the *monitoring intensity* set by the regulator (exogenous). Both have **imperfect** knowledge of the partner’s cost structure. |
| **Outcomes** | 1. Prompt repair (high reliability).<br>2. Delayed repair (risk of burnout).<br>3. Unnecessary repair (wasted effort). |
| **Payoffs** | Ordinal (0–3) matrix below. |
| **Strategic Tension** | **Strategic – Public‑Goods / Enforcement Game**.  The staff’s maintenance effort is a *public good* for all farmers; the farmer’s reporting is a *conditional contribution*.  The game resembles a **volunteer’s dilemma** where the socially optimal outcome is (Maintain, Report) but each side may try to free‑ride. |
| **Temporal Structure** | One‑shot **annual** (maintenance decision is taken at the start of the year; reporting can occur any month). |
| **Relevant Rules** | *Boundary rule*: only farmers attached to the transformer can report.<br>*Choice rule*: staff can allocate at most a fixed amount of effort per transformer (capacity τ). |

### Payoff Matrix  

|                     | **Staff Maintain** | **Staff Delay** |
|---------------------|--------------------|-----------------|
| **Farmer Report**   | (3, 2) – farmer gets reliable power (rank 3); staff bears effort but gains reputation (rank 2). | (0, 1) – farmer suffers loss (rank 0); staff avoids effort (rank 1). |
| **Farmer Silent**   | (2, 1) – farmer enjoys reliability for free (rank 2); staff wastes effort (rank 1). | (1, 3) – both avoid costs (farmer rank 1 due to occasional voltage dips; staff rank 3 – no effort, no penalty). |

*Interpretation* – The highest joint rank (3,2) occurs when the farmer reports and staff maintains; the worst joint rank (0,1) is when the farmer reports but staff delays, leading to failure.

---

## 6.  Social‑Learning & Imitation (Non‑Strategic Sequential Process)

| Element | Description |
|---|---|
| **Title** | **Social‑Learning & Imitation Process** |
| **Location** | Village‑level observation zone (farmers see neighbours’ equipment, pump performance, and connection status). |
| **Players** | *Individual farmer* (the learner). No direct opponent; the process is **non‑strategic**. |
| **Roles** | Learner – electricity consumer seeking to update his decision rule. |
| **Actions** | **Observe** neighbours’ visible outcomes (e.g., whether a neighbour’s capacitor “worked”).<br>**Imitate** – adopt the observed technology with probability *i* (learning constraint ι).<br>**Do‑nothing** – keep current technology. |
| **Control Rules** | • Observation occurs **once per year** after the harvest.<br>• If a farmer observes a *successful* adoption on at least *θ* neighbours, he becomes *eligible* to imitate in the next cycle (threshold rule).<br>• Imitation is *probabilistic* (parameter ι) and **cost‑free** (adoption cost already incurred by the observed neighbour). |
| **Information** | Farmers have **perfect** knowledge of *visible* adoption outcomes (e.g., “neighbor X installed a capacitor and his pump ran smoothly”).  However, they have **noisy** understanding of *causal* links (they may mis‑attribute the improvement to the capacitor). |
| **Outcomes** | 1. **Technology diffusion** – more farmers adopt capacitors or standard pumps.<br>2. **Stagnation** – if no successful examples are observed, adoption stalls. |
| **Payoffs** | Not expressed as a game; the payoff is embedded in the downstream strategic games (e.g., higher probability of reaching the (Invest, Invest) equilibrium in the DSM‑Coordination game). |
| **Strategic Tension** | **Non‑strategic** – there is no simultaneous decision with interdependent pay‑offs.  The process simply updates the *strategy set* available to farmers in later strategic games. |
| **Temporal Structure** | **Annual** (after each harvest, before the next year’s decision cycle). |
| **Relevant Rules** | *Boundary rule*: learning is limited to farmers sharing the same transformer.<br>*Position rule*: the learner’s *memory* of past failures influences the threshold θ. |

---

# Comparative Analysis of the Strategic Core  

| # | Game | Player Types | Core Game Type | Dominant/Preferred Strategies | Key Institutional Feature |
|---|------|--------------|----------------|------------------------------|---------------------------|
| 1 | DSM‑Coordination | Farmer ↔ Farmer | **Assurance / Coordination** (two pure equilibria) | Coordination on *Invest* yields highest joint rank, but risk of unilateral cost pushes to *Not‑Invest*. | Benefit spill‑over (τ) + learning constraint (ι). |
| 2 | Authorization | Farmer ↔ Staff | **Hybrid Trust / Prisoner’s Dilemma** (farmer wants *Grant*, staff balances effort vs illicit gain) | Staff’s *Grant* is socially better if farmer *Applies*; otherwise *Deny* dominates for staff. | Discretionary power, monitoring intensity (γ). |
| 3 | Collusion‑Exchange | Farmer ↔ Staff | **Trust Game (asymmetric)** | Mutual *Offer/Accept* gives staff highest rank, farmer prefers *Refuse/Reject* (avoids cost). | Corruption level (δ) and detection risk (γ). |
| 4 | Groundwater Extraction | Farmer ↔ Farmer | **Prisoner’s Dilemma (Common‑Pool)** | *High* dominates individually, but *Low‑Low* is socially optimal. | Aquifer depletion feedback (γ). |
| 5 | Transformer‑Maintenance | Staff ↔ Farmer | **Volunteer’s Dilemma / Public‑Goods** | Staff prefers *Delay*; farmer prefers *Report* only if staff likely to *Maintain*. | Reputation gain (δ) vs effort cost (τ). |
| 6 | Social‑Learning | Single farmer | **Non‑strategic** | Not applicable – updates future strategic options. | Visibility of neighbours, learning constraint (ι). |

### Similarities & Distinctions  

| Pair | Similarity | Why It Is Distinct |
|------|------------|--------------------|
| (1) DSM‑Coordination ↔ (4) Groundwater Extraction | Both are *farmer‑farmer* 2‑player games with a public‑good element. | DSM‑Coordination is a **coordination/assurance** game (mutual investment yields the best joint outcome), whereas Groundwater Extraction is a **prisoner’s dilemma** where the dominant strategy harms the group. |
| (2) Authorization ↔ (3) Collusion‑Exchange | Both involve farmer‑staff interaction and a decision on “granting” something. | Authorization is **formal** (fee‑based, regulated) and focuses on *connection status*; Collusion‑Exchange is **informal** (kick‑back) and captures *trust* in illicit reciprocity. The payoff asymmetry is opposite (farmer prefers *Grant* in Authorization, but prefers *Reject* in Collusion when the cost of the kick‑back is high). |
| (2) Authorization ↔ (5) Transformer‑Maintenance | Both have staff deciding to **invest effort** (grant vs maintain). | Authorization links to *capacity allocation* and *legal status*; Maintenance links to *reactive repair* after failures. The farmer’s action set differs (Apply/Stay‑informal vs Report/Silent). |
| (3) Collusion‑Exchange ↔ (5) Transformer‑Maintenance | Both involve staff willingness to **accept risk** for a benefit. | Collusion‑Exchange is **proactive** illicit exchange; Maintenance is **reactive** response to a reported failure. The payoff structures differ (trust vs volunteer’s dilemma). |

Because the **Authorization** and **Transformer‑Maintenance** games both feature a staff decision to *invest effort* and a farmer decision that influences that investment, they risk being seen as too similar. To guarantee strategic diversity, we **replace** the Transformer‑Maintenance game with a **Regulatory‑Monitoring Game** (Staff ↔ Regulator) that introduces a third player type and a distinct enforcement dilemma.  

---

# Revised Action Situation (replaces #5)

## 5‑R.  Regulatory‑Monitoring (Enforcement) Game  

| Element | Description |
|---|---|
| **Title** | **Regulatory‑Monitoring (Enforcement) Game** |
| **Location** | APERC regional office (regulatory layer) and sub‑station (implementation layer). |
| **Players** | *Regulator* (APERC officer) and *Sub‑station staff* (local enforcer). |
| **Roles** | Regulator – overseer, sets monitoring intensity and sanctions.<br>Staff – frontline enforcer, decides how much **monitoring effort** to allocate to detecting illegal connections. |
| **Actions** | **Regulator**: <br>• **Intensify** – increase audit frequency, raise penalty severity (costly for regulator).<br>• **Relax** – keep monitoring low (saves regulator resources).<br>**Staff**: <br>• **Strict** – devote high effort to spot illegal use (incurs effort cost, reduces collusion).<br>• **Lenient** – minimal effort, easier collusion. |
| **Control Rules** | • If *Intensify* + *Strict*: illegal connections are detected quickly; staff incurs effort cost, regulator incurs monitoring cost but gains compliance (high reputation).<br>• If *Intensify* + *Lenient*: regulator’s monitoring is wasted; illegal connections persist, staff avoids effort, regulator suffers reputational loss (γ).<br>• If *Relax* + *Strict*: staff’s strictness yields few detections (low payoff for staff, moderate for regulator).<br>• If *Relax* + *Lenient*: status‑quo; illegal connections flourish, both save effort but system reliability drops (τ). |
| **Information** | Regulator knows aggregate *violation statistics* (noisy) and budget constraints. Staff knows the *local collusion density* (δ) and the regulator’s recent audit outcomes (partial). |
| **Outcomes** | 1. High compliance (few illegal connections).<br>2. Low compliance (many illegal connections).<br>3. Mixed compliance (partial detection). |
| **Payoffs** | Ordinal (0–3) matrix below. |
| **Strategic Tension** | **Strategic – Coordination/Conflict Game** between regulator and staff.  Each would like the other to bear the monitoring cost, creating a **mutual‑defection** equilibrium (Relax + Lenient) unless institutional incentives (δ, γ) shift the balance. |
| **Temporal Structure** | Annual (regulator sets policy at the start of the year; staff chooses effort each month). |
| **Relevant Rules** | *Boundary rule*: regulator covers a set of sub‑stations (district level).<br>*Choice rule*: staff can allocate at most a fixed proportion of work time to monitoring (τ). |

### Payoff Matrix (Regulator vs Staff)

|                     | **Staff Strict** | **Staff Lenient** |
|---------------------|------------------|-------------------|
| **Regulator Intensify** | (2, 2) – both incur costs but achieve high compliance (moderate ranks). | (0, 3) – regulator wastes effort (rank 0); staff enjoys illicit freedom (rank 3). |
| **Regulator Relax**     | (3, 1) – regulator saves resources (rank 3); staff bears effort with little payoff (rank 1). | (1, 0) – both save effort but compliance collapses (lowest joint rank). |

*Rationale* – The most socially desirable outcome (high compliance) is (Intensify, Strict) but each side would rather free‑ride on the other’s effort, creating a classic **coordination‑failure** dilemma.

### Why the Replacement Improves Strategic Diversity  

*Distinct player set*: introduces the **regulator** as a new actor, expanding the governance hierarchy.  
*Different payoff asymmetry*: the regulator’s payoff depends on *system‑wide compliance* while the staff’s payoff hinges on *personal effort* and *collusion opportunities* – a shift from the earlier farmer‑staff maintenance interaction.  
*New institutional lever*: monitoring intensity (γ) is now an explicit strategic variable, linking back to the model’s exogenous oversight intensity.

---

# Full Set of Distinct Action Situations  

| # | Title | Players | Core Game Type |
|---|-------|---------|----------------|
| 1 | DSM‑Coordination (Capacitor Adoption) | Farmer ↔ Farmer | Assurance / Coordination |
| 2 | Authorization (Formal vs. Informal Connection) | Farmer ↔ Staff | Hybrid Trust / Prisoner’s Dilemma |
| 3 | Collusion‑Exchange (Trust) | Farmer ↔ Staff | Asymmetric Trust |
| 4 | Groundwater Extraction (CPR) | Farmer ↔ Farmer | Prisoner’s Dilemma (Common‑Pool) |
| 5‑R | Regulatory‑Monitoring (Enforcement) | Regulator ↔ Staff | Coordination/Conflict (Monitoring Dilemma) |
| 6 | Social‑Learning & Imitation | Single Farmer (non‑strategic) | Observation → Strategy Update |

All six capture **different governance interactions** present in the ODD + D description: (i) coordination among peers, (ii) formal‑informal institutional choice, (iii) informal reciprocity, (iv) common‑pool resource extraction, (v) hierarchical enforcement, and (vi) learning/ diffusion.  

Each strategic game is presented as a **2 × 2 normal‑form** with **ordinal payoffs** (0–3) and a brief justification of the payoff ordering, fully complying with the ODD + D protocol.
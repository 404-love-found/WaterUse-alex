# Run 1 — openai/gpt-oss-120b

## 1. Capacitor‑Coordination Game (Assurance / Coordination)

| Element | Description |
|--------|-------------|
| **Title** | Capacitor‑Coordination Game |
| **Location** | Transformer service area (village‑level) |
| **Players** | Two neighbouring farmers that share the same transformer |
| **Roles** | *Farmer A* – electricity consumer, *Farmer B* – electricity consumer |
| **Actions** | **Adopt** a capacitor (invest)  ↔  **Not‑Adopt** (keep current set‑up) |
| **Control Rules** | – If both adopt, the local voltage stabilises and the shared benefit (higher pump efficiency, lower losses) is realised for **both**.<br>– If only one adopts, the adopter bears the investment cost but the voltage improvement is too small to be noticeable; the non‑adopter experiences the same (or slightly worse) voltage as before. |
| **Information** | Each farmer observes the *current* voltage quality and whether the neighbour has a visible capacitor (visual cue). Information about the neighbour’s *future* decision is **partial / noisy** – they only know the neighbour’s past behaviour. |
| **Outcomes** | – Change in electricity‑quality rating (high / medium / low).<br>– Budget change for the adopter (investment cost). |
| **Payoffs** (ordinal, 0 = worst, 3 = best) | See payoff matrix below. |
| **Strategic Tension** | **Strategic** – a *coordination / assurance* game. Farmers would like to adopt **together**, but each fears being the sole adopter. |
| **Temporal Structure** | Repeated once every irrigation year (the decision is revisited annually). |
| **Relevant Rules** | • Boundary rule – only farmers attached to the same transformer are paired.<br>• Choice rule – each farmer can either invest in a capacitor or not.<br>• Control rule – the joint outcome (voltage stability) is a deterministic function of the two choices. |

### 2 × 2 payoff matrix (Farmer A rows, Farmer B columns)

|                | **B Adopt** | **B Not‑Adopt** |
|----------------|-------------|-----------------|
| **A Adopt**    | (3 , 3)     | (0 , 1)         |
| **A Not‑Adopt**| (1 , 0)     | (2 , 2)         |

*Why the numbers make sense*  

* (3,3) – both enjoy high reliability and no one bears a unilateral cost.  
* (0,1) – the adopter pays the cost but sees no benefit; the non‑adopter keeps the status‑quo (slightly better than a failed investment).  
* (2,2) – the “do‑nothing” outcome is the baseline (moderate reliability, no extra cost).  

---

## 2. Transformer‑Capacity Public‑Goods Game (Contribution vs Free‑Riding)

| Element | Description |
|--------|-------------|
| **Title** | Capacity‑Provision Public‑Goods Game |
| **Location** | Transformer‑level (group of all farmers connected to the same transformer) |
| **Players** | Two representative farmers (the game is symmetric and stands for the whole group) |
| **Roles** | *Contributor* – farmer who can pay for a capacity upgrade; *Potential Free‑Rider* – farmer who can choose not to pay |
| **Actions** | **Contribute** to the transformer upgrade (pay a share of the cost) ↔  **Free‑Ride** (pay nothing) |
| **Control Rules** | – If **both** contribute, the transformer capacity rises enough to keep voltage stable for the whole group.<br>– If **only one** contributes, the capacity increase is insufficient; both still benefit, but the contributor bears the full cost.<br>– If **none** contribute, the transformer stays overloaded → frequent brown‑outs. |
| **Information** | Each farmer knows the *current* transformer load and whether the neighbour contributed in the previous year (perfectly observed). Future contributions are uncertain. |
| **Outcomes** | – Change in effective transformer capacity (high / medium / low).<br>– Individual cash outflow for the contributor. |
| **Payoffs** | Ordinal ranks (0‑3) – see matrix. |
| **Strategic Tension** | **Strategic** – a *public‑goods* dilemma. The socially optimal outcome is both contributing, but each can gain by free‑riding. |
| **Temporal Structure** | Annual decision, repeated each irrigation year. |
| **Relevant Rules** | • Boundary rule – only farmers attached to the same transformer are in the same public‑goods pool.<br>• Choice rule – each farmer can either put money into the upgrade or not.<br>• Control rule – the aggregate contribution determines the capacity level. |

### 2 × 2 payoff matrix (Farmer A rows, Farmer B columns)

|                | **B Contribute** | **B Free‑Ride** |
|----------------|------------------|-----------------|
| **A Contribute**| (3 , 3)          | (1 , 2)         |
| **A Free‑Ride** | (2 , 1)          | (0 , 0)         |

*Interpretation*  

* (3,3) – both share a reliable transformer and each bears only a modest share of the cost.  
* (1,2) – the contributor pays the full cost (low rank) while the free‑rider enjoys the upgraded service (higher rank).  
* (0,0) – no upgrade, frequent outages, lowest rank for both.

---

## 3. Authorization Game (Formal Connection vs Informal Access)

| Element | Description |
|--------|-------------|
| **Title** | Authorization Game |
| **Location** | Sub‑station office (record‑keeping desk) and the farmer’s field (where the decision to apply is made) |
| **Players** | **Farmer** (seeker of a formal electricity connection) and **Sub‑station Staff** (gate‑keeper) |
| **Roles** | Farmer = *Applicant*; Staff = *Authorizer / Enforcer* |
| **Actions** | **Farmer:** *Apply* for a formal connection ↔ *Stay Informal* (use illegal line).<br>**Staff:** *Authorize* (process the application, invest in record‑keeping) ↔ *Enforce* (reject/penalise informal use). |
| **Control Rules** | – If the farmer applies **and** staff authorizes, the farmer receives a legal connection (reliable supply) and the staff incurs a small administrative cost.<br>– If the farmer applies but staff denies, the farmer wastes effort (application fee, time) while staff saves effort.<br>– If the farmer stays informal **and** staff tolerates, the farmer gets cheap electricity; staff gains an informal “kick‑back” (social norm benefit).<br>– If the farmer stays informal **and** staff enforces, the farmer is penalised (fine) and staff receives a compliance reward. |
| **Information** | Farmer knows the *current* enforcement intensity (observed fines) but not the staff’s exact willingness to authorize. Staff knows the farmer’s payment capacity and past informal behaviour, but not the farmer’s hidden willingness to apply again. |
| **Outcomes** | – Legal connection status (yes/no).<br>– Cash outflow for the farmer (application fee, fine, or informal payment).<br>– Effort cost for staff (processing vs enforcement). |
| **Payoffs** | Ordinal (0‑3) – see matrix. |
| **Strategic Tension** | **Strategic** – an *authorization* game with asymmetric power: the farmer wants the formal link, the staff balances effort, oversight risk and informal benefits. |
| **Temporal Structure** | One‑shot each year (the farmer decides once per irrigation cycle; staff decides simultaneously). |
| **Relevant Rules** | • Boundary rule – only the farmer‑staff pair linked to a given transformer can interact.<br>• Choice rule – farmer chooses “apply” or “stay informal”; staff chooses “authorize” or “enforce”.<br>• Control rule – the joint action determines legal status and cost flows. |

### 2 × 2 payoff matrix (Farmer rows, Staff columns)

|                | **Staff Authorize** | **Staff Enforce** |
|----------------|---------------------|-------------------|
| **Farmer Apply**   | (3 , 2)               | (1 , 3)           |
| **Farmer Stay Informal** | (2 , 2)               | (0 , 3)           |

*Explanation*  

* (3,2) – farmer gets reliable power (top rank); staff bears modest admin cost (second rank).  
* (1,3) – farmer wastes effort (low rank); staff avoids admin work and gains enforcement reward (top rank).  
* (2,2) – informal access is cheap for farmer (second rank) and staff gains informal benefit (second rank).  
* (0,3) – farmer is fined (worst); staff receives full compliance reward (best).

---

## 4. Collusion‑Exchange (Trust) Game between Farmer and Staff

| Element | Description |
|--------|-------------|
| **Title** | Collusion‑Exchange (Trust) Game |
| **Location** | Informal meeting point near the sub‑station (e.g., village tea‑shop) |
| **Players** | Farmer and the same sub‑station staff member with whom the farmer may have a personal tie |
| **Roles** | Farmer = *Briber*; Staff = *Reciprocator* |
| **Actions** | **Farmer:** *Give* a small informal “kick‑back” (cash or favour) ↔ *No‑Give*.<br>**Staff:** *Reciprocate* (grant tolerant service, e.g., overlook an illegal connection) ↔ *Defect* (strict enforcement). |
| **Control Rules** | – Mutual cooperation (Give + Recip) yields cheap electricity for the farmer and a personal benefit for the staff (both rank 3).<br>– If the farmer gives but staff defects, the farmer loses the kick‑back (rank 0) while staff pockets the payment (rank 3).<br>– If staff reciprocates but farmer does not give, staff gets nothing (rank 0) while the farmer enjoys tolerant service for free (rank 2).<br>– If both abstain, the status‑quo persists (low but non‑zero rank 1). |
| **Information** | Both parties see each other’s past behaviour (e.g., previous kick‑backs, past tolerance) but cannot observe the current intention before acting – **simultaneous, imperfect information**. |
| **Outcomes** | – Transfer of informal payment (yes/no).<br>– Change in enforcement intensity for the farmer’s connection. |
| **Payoffs** | Ordinal (0‑3) – see matrix. |
| **Strategic Tension** | **Strategic** – a *trust* game. The farmer must decide whether to risk a bribe; the staff must decide whether to honour the informal pact. |
| **Temporal Structure** | Repeated annually (the pair renegotiates each irrigation year). |
| **Relevant Rules** | • Boundary rule – only farmer–staff pairs with an existing social tie can play.<br>• Choice rule – each chooses “give / no‑give” and “recip / defect”.<br>• Control rule – the joint action determines the informal service level. |

### 2 × 2 payoff matrix (Farmer rows, Staff columns)

|                | **Staff Reciprocate** | **Staff Defect** |
|----------------|-----------------------|------------------|
| **Farmer Give**    | (3 , 3)                 | (0 , 3)          |
| **Farmer No‑Give** | (2 , 0)                 | (1 , 1)          |

*Rationale*  

* (3,3) – both obtain the expected benefit of a trusted exchange.  
* (0,3) – farmer loses the bribe without any service gain; staff keeps the payment.  
* (2,0) – staff honours the informal pact for free; farmer enjoys tolerant service.  
* (1,1) – no exchange, status‑quo (low but non‑zero ranks).

---

## 5. Groundwater‑Extraction Common‑Pool Resource (CPR) Game

| Element | Description |
|--------|-------------|
| **Title** | Groundwater‑Extraction CPR Game |
| **Location** | Shared aquifer basin underlying a cluster of farms (spatially defined by the transformer area) |
| **Players** | Two neighbouring farmers who pump from the same aquifer |
| **Roles** | Farmer = *Extractor* |
| **Actions** | **High Extraction** (pump at maximum irrigation demand) ↔ **Low Extraction** (conserve water, pump less) |
| **Control Rules** | – The aquifer’s water table falls when total extraction exceeds the natural recharge. <br>– If the water table is low, pumping costs rise (higher electricity use, more frequent transformer overload). <br>– The payoff for each farmer depends on both his own extraction level and the neighbour’s level. |
| **Information** | Each farmer observes the *current* groundwater depth (noisy estimate) and knows the neighbour’s *historical* extraction pattern, but not the exact current decision. |
| **Outcomes** | – Change in aquifer depth (depletion or recovery).<br>– Individual pumping cost (higher when depth is larger). |
| **Payoffs** | Ordinal (0‑3) – see matrix. |
| **Strategic Tension** | **Strategic** – a *common‑pool resource* dilemma. Mutual restraint yields sustainability, but each farmer has an incentive to over‑extract if the other restrains. |
| **Temporal Structure** | One‑shot each irrigation year, repeated (the water table evolves over time). |
| **Relevant Rules** | • Boundary rule – only farmers drawing from the same aquifer are linked.<br>• Choice rule – each selects High or Low extraction.<br>• Control rule – the sum of extractions determines the aquifer’s next‑year depth. |

### 2 × 2 payoff matrix (Farmer A rows, Farmer B columns)

|                | **B High** | **B Low** |
|----------------|------------|-----------|
| **A High**     | (0 , 0)    | (3 , 1)   |
| **A Low**      | (1 , 3)    | (3 , 3)   |

*Interpretation*  

* (0,0) – both over‑extract, aquifer collapses, high costs for both (worst).  
* (3,1) – A over‑extracts while B restrains; A enjoys high yield (best), B suffers reduced yield (low).  
* (3,3) – mutual restraint gives sustainable yields and low costs (best for both).  

---

## 6. Social‑Learning (Non‑Strategic) Process

| Element | Description |
|--------|-------------|
| **Title** | Social‑Learning / Imitation Process |
| **Location** | Village‑level observation network (farmers watch neighbours, staff observe farmer behaviour) |
| **Players** | Individual farmers (as observers) – no direct opponent |
| **Roles** | *Observer* (farmer) |
| **Actions** | **Imitate** a successful neighbour’s technology (e.g., adopt a capacitor) ↔ **Do‑Not‑Imitate** (keep current technology) |
| **Control Rules** | – Each year a farmer is placed in an *adoption pool* if (i) the farmer is a “experimenter” (random draw) or (ii) the transformer has already witnessed a *threshold* number of simultaneous adopters in the previous cycle.<br>– If the farmer imitates and the neighbour’s outcome was **successful** (high reliability, higher yield), the farmer’s adoption succeeds; otherwise the imitation fails and the farmer bears the cost without benefit. |
| **Information** | Farmers perfectly observe neighbours’ **visible** technology choices (capacitor presence, pump type) but only receive noisy feedback about the *effectiveness* of those choices (mis‑attribution of voltage improvement). |
| **Outcomes** | – Updated belief about the payoff of the technology.<br>– Possible adoption (or failed adoption) of the technology. |
| **Payoffs** | Not modelled as a strategic payoff matrix; the outcome feeds back into the farmer’s future decision set (higher probability of adopting in later years if previous imitation succeeded). |
| **Strategic Tension** | **Non‑strategic** – a sequential observation‑imitation process; no simultaneous move against another player. |
| **Temporal Structure** | Occurs **once per year** after the physical processes (grid loading, groundwater extraction) have generated observable outcomes. |
| **Relevant Rules** | • Boundary rule – only farmers sharing the same transformer can be observed.<br>• Choice rule – a farmer either imitates or does not imitate.<br>• Control rule – the probability of entering the imitation pool depends on the number of successful adopters in the previous cycle (threshold‑trigger). |

---

# Comparative Analysis of the Strategic Core

| Game | Type of Strategic Interaction | Core Dilemma | Symmetry | Key Asymmetry / Feature |
|------|------------------------------|--------------|----------|--------------------------|
| **1 Capacitor‑Coordination** | Assurance / Coordination (2‑player) | Need *joint* adoption to reap benefit | Symmetric payoffs | Benefit only materialises when **both** adopt; unilateral adoption is punished. |
| **2 Capacity‑Provision** | Public‑Goods (2‑player) | Free‑riding vs collective upgrade | Symmetric payoffs | Contribution is costly; non‑contributors still enjoy the upgraded grid. |
| **3 Authorization** | Asymmetric *Authorization* game | Farmer wants formal access; staff balances effort vs informal gain | Asymmetric (different action sets) | Power imbalance: staff can block the farmer; farmer can waste effort. |
| **4 Collusion‑Exchange** | Trust game (2‑player) | Mutual cooperation vs risk of betrayal | Asymmetric payoffs (different incentives) | Informal “kick‑back” creates a contingent reward; defection yields high payoff for the defector only. |
| **5 Groundwater‑Extraction** | CPR (2‑player) | Sustainable use vs individual over‑extraction | Symmetric payoffs | The resource is *shared*; over‑extraction harms both, but each can tempt to over‑extract. |
| **6 Social‑Learning** | Non‑strategic sequential | Observation → Imitation → Adoption | – | No simultaneous move; learning shapes future strategic games. |

### Distinctiveness Check

* **Capacitor‑Coordination** and **Capacity‑Provision** both involve *farmers* and *joint outcomes*, but they differ fundamentally: the former is an **assurance** game where the *technology* itself only works if enough adopt; the latter is a **public‑goods** game where the *infrastructure* is improved regardless of who pays, creating a classic free‑rider problem.  

* **Authorization** is the only game that directly pits a *farmer* against a *regulatory‑type* decision (staff) with *asymmetric* action sets (apply vs stay informal ↔ authorize vs enforce).  

* **Collusion‑Exchange** captures a *trust* dilemma that is distinct from the formal‑authorization game because the payoff to the staff comes from an *informal* benefit, not from compliance or enforcement.  

* **Groundwater‑Extraction** is the sole **common‑pool resource** game; the resource is natural (aquifer) rather than institutional.  

* **Social‑Learning** is the only *non‑strategic* sequential process, providing the feedback loop that updates preferences in the other games.

Thus each listed situation represents a **different governance interaction**.

---

# Ensuring Strategic Diversity – Revision

During the comparison we observed that **Games 1 and 2** both involve *joint farmer decisions* and could be perceived as overlapping “coordination” themes. To sharpen the diversity we replace **Game 2 (Capacity‑Provision Public‑Goods)** with a **“Capacity‑Negotiation (Bargaining) Game”** that explicitly models *asymmetric bargaining* between a **farmer** who wants a capacity upgrade and the **staff** who decides how much of the cost to bear.

### Revised Action Situation 2 – Capacity‑Negotiation (Bargaining) Game

| Element | Description |
|--------|-------------|
| **Title** | Capacity‑Negotiation (Bargaining) Game |
| **Location** | Sub‑station office (capacity‑planning meeting) |
| **Players** | Farmer (requester) and Sub‑station Staff (capacity provider) |
| **Roles** | Farmer = *Requester*; Staff = *Provider* |
| **Actions** | **Farmer:** *Offer* a contribution share (High ↔ Low).<br>**Staff:** *Accept* the offer (provide remaining capacity) ↔ *Reject* (no upgrade). |
| **Control Rules** | – If the farmer offers **High** (covers ≥ 70 % of upgrade cost) and staff accepts, the transformer is upgraded → high reliability for all.<br>– If the farmer offers **Low** (≤ 30 % contribution) and staff accepts, the upgrade is partial → moderate reliability.<br>– If staff rejects, no upgrade occurs regardless of the farmer’s offer. |
| **Information** | Farmer knows the *current* overload level and the *minimum* contribution required (public rule). Staff knows the farmer’s budget (observed from past payments) but not the exact amount the farmer is willing to offer. |
| **Outcomes** | – Updated transformer capacity (high / moderate / unchanged).<br>– Cash outflow for farmer (high or low contribution).<br>– Effort cost for staff (processing the upgrade). |
| **Payoffs** (ordinal 0‑3) | See new matrix. |
| **Strategic Tension** | **Strategic** – a *bargaining* game with asymmetric power: the farmer must decide how much to contribute; the staff decides whether the contribution is sufficient to justify the upgrade. |
| **Temporal Structure** | One‑shot each year (negotiation occurs before the monthly physical cycle). |
| **Relevant Rules** | • Boundary rule – only the farmer linked to the transformer can negotiate with the two staff assigned to that transformer.<br>• Choice rule – farmer selects contribution level; staff selects accept/reject.<br>• Control rule – the joint decision determines the upgrade level. |

#### Payoff matrix (Farmer rows, Staff columns)

|                | **Staff Accept** | **Staff Reject** |
|----------------|------------------|------------------|
| **Farmer High‑Offer** | (3 , 2)            | (1 , 1)          |
| **Farmer Low‑Offer**  | (2 , 3)            | (0 , 0)          |

*Why the numbers make sense*  

* (3,2) – Farmer gets a full upgrade (best rank) while staff bears a modest effort cost (second rank).  
* (2,3) – Farmer saves money (second rank) and staff secures a partial upgrade at low effort (top rank).  
* (1,1) – Farmer’s high offer is rejected; both get a low‑rank “missed opportunity”.  
* (0,0) – Low offer rejected; no upgrade, worst outcome for both.

**Result:** This bargaining game introduces a **different asymmetric interaction** (farmer‑staff negotiation) that does not duplicate the coordination or public‑goods logic of the capacitor game. The set now contains five truly distinct strategic games plus one non‑strategic learning process.

--- 

## Final Set of Action Situations (complete)

| # | Title | Strategic? | Game Type (if strategic) |
|---|-------|------------|--------------------------|
| 1 | Capacitor‑Coordination Game | Yes | Assurance / Coordination |
| 2 | Capacity‑Negotiation (Bargaining) Game | Yes | Asymmetric Bargaining |
| 3 | Authorization Game | Yes | Authorization (asymmetric) |
| 4 | Collusion‑Exchange (Trust) Game | Yes | Trust |
| 5 | Groundwater‑Extraction CPR Game | Yes | Common‑Pool Resource |
| 6 | Social‑Learning (Imitation) Process | No | Non‑strategic sequential |

Each of these six action situations captures a **distinct governance interaction** described in the ODD + D model of electricity‑irrigation governance in Andhra Pradesh. The payoff matrices use only ordinal ranks (0‑3) as required, and the accompanying IAD elements specify the full institutional context.
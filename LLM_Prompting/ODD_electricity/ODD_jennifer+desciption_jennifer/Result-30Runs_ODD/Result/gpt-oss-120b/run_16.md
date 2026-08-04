# Run 16 — openai/gpt-oss-120b

## Electricity‑Irrigation Governance – Action‑Situation Catalogue  
*(Extracted from the ODD + D description and expressed with the Institutional Analysis & Development (IAD) template)*  

Below are **all distinct governance interactions** that appear in the model.  
Strategic interactions are given as 2‑player normal‑form games (ordinal pay‑offs 0‑3).  
Non‑strategic processes are described as sequential “games” (no simultaneous move).  

---

### 1. Authorization Game  – Farmer ↔ Sub‑station Staff  

| IAD Element | Description |
|------------|-------------|
| **Title** | **Authorization Decision** |
| **Location** | Transformer service area (village‑level) – the point where a connection request is processed. |
| **Players** | • *Farmer* (any household seeking electricity)  <br>• *Sub‑station staff* (utility officer assigned to the transformer). |
| **Roles** | Farmer = *electricity consumer / connection‑seeker*; Staff = *service‑provider & gate‑keeper*. |
| **Actions** | **Farmer:** 1 → **Apply** for a formal (authorised) connection; 2 → **Stay informal** (no application). <br>**Staff:** 1 → **Authorize** (grant connection & invest required capacity); 2 → **Reject** (refuse). |
| **Control Rules** | – If **Apply & Authorize** → a legal connection is created, transformer load is updated, and the farmer receives a stable voltage. <br>– **Apply & Reject** → farmer bears application cost, receives no connection; staff avoids capacity cost. <br>– **Stay & Authorize** → staff prepares a connection that is never taken up (wasted effort). <br>– **Stay & Reject** → status‑quo informal connection persists; staff saves effort, farmer continues informal supply (subject to risk of penalties). |
| **Information** | Farmer knows his own budget, the typical processing time, and the *observed* rejection rate of staff (no perfect knowledge of staff’s willingness). <br>Staff knows the farmer’s payment ability and the current load on the transformer, but not the farmer’s exact willingness to pay for a formal link. |
| **Outcomes** | • Legal connection (yes/no)  <br>• Capital outlay by staff (yes/no)  <br>• Farmer’s electricity cost (lower if authorised)  <br>• Risk of illegal‑connection penalties (only when informal). |
| **Payoffs (ordinal)** | **Farmer** – 3 = secure, cheap electricity; 2 = informal but no extra cost; 1 = informal with staff‑initiated offer (minor benefit); 0 = application rejected (wasted effort). <br>**Staff** – 3 = legitimate revenue & compliance; 2 = no extra work (informal status quo); 1 = wasted authorisation effort; 0 = costly rejection of a willing applicant. |
| **Strategic Tension** | **Strategic (simultaneous)** – a *coordination/authorization* game. Both players prefer the (Apply, Authorize) outcome, but each fears the other’s opposite move (rejection or staying informal). |
| **Temporal Structure** | Decided **once per year** (the “annual strategic decision” step). |
| **Relevant Rules** | *Boundary rule*: only farmers attached to the transformer and the two staff members assigned to it participate. <br>*Position rule*: staff can only authorise if transformer capacity permits. <br>*Choice rule*: binary (Apply/Stay; Authorize/Reject). |
| **Normal‑Form Game** |  |  

|                     | **Staff – Authorize** | **Staff – Reject** |
|---------------------|----------------------|--------------------|
| **Farmer – Apply**  | (3, 3)               | (0, 2)             |
| **Farmer – Stay**   | (1, 1)               | (2, 2)             |

*Explanation*: (Farmer payoff, Staff payoff). The highest joint payoff (3,3) is achieved when both cooperate; the lowest for the farmer (0) occurs when he applies but is rejected, while the staff’s worst (0) occurs when he rejects a willing applicant.

---

### 2. Collusion‑Exchange (Trust) Game – Farmer ↔ Sub‑station Staff  

| IAD Element | Description |
|------------|-------------|
| **Title** | **Collusive Exchange / Trust Game** |
| **Location** | Same transformer service area; informal negotiations usually happen at the sub‑station office or in the field. |
| **Players** | Farmer, Sub‑station staff (same individuals as in Situation 1). |
| **Roles** | Farmer = *bribe‑giver*; Staff = *bribe‑receiver*. |
| **Actions** | **Farmer:** 1 → **Offer bribe** (propose an informal payment for better service); 2 → **No offer**. <br>**Staff:** 1 → **Accept** (provide preferential treatment, e.g., delayed disconnection, reduced tariff); 2 → **Reject**. |
| **Control Rules** | – Mutual acceptance → farmer receives lower electricity cost or delayed enforcement; staff receives illicit gain. <br>– Offer + Reject → farmer loses the bribe amount, staff avoids detection risk. <br>– No‑offer + Accept → staff waits for a bribe that never arrives (wasted opportunity). <br>– No‑offer + Reject → status‑quo informal relationship, no extra cost or gain. |
| **Information** | Farmer knows his own financial strain and the *perceived* willingness of the staff (based on past encounters). <br>Staff knows the farmer’s reputation (history of payments) but not the exact amount the farmer is ready to give. |
| **Outcomes** | • Informal payment transferred (yes/no). <br>• Adjustment of enforcement intensity (relaxed/normal). <br>• Risk of detection (higher when both collude). |
| **Payoffs (ordinal)** | **Farmer** – 3 = receives service discount after paying bribe; 2 = status‑quo informal supply; 1 = no discount but staff’s willingness to collude (potential future benefit); 0 = bribe lost, no discount. <br>**Staff** – 3 = receives illicit gain without detection; 2 = status‑quo informal revenue; 1 = wasted expectation of bribe; 0 = rejection of a willing bribe (lost illicit profit). |
| **Strategic Tension** | **Strategic (simultaneous)** – a *trust / collusion* game. Both parties gain most from mutual cooperation, but each can defect (reject/offer) to avoid risk. |
| **Temporal Structure** | Decided **once per year** (same decision window as Situation 1). |
| **Relevant Rules** | *Boundary*: only farmers with an existing informal tie to a staff member may consider offering a bribe. <br>*Position*: staff willingness is moderated by personal corruption level and local detection risk. |
| **Normal‑Form Game** |  |  

|                     | **Staff – Accept** | **Staff – Reject** |
|---------------------|-------------------|-------------------|
| **Farmer – Offer**  | (3, 3)            | (0, 2)            |
| **Farmer – No‑offer**| (2, 1)           | (2, 2)            |

*Explanation*: Mutual collusion (3,3) is the most preferred outcome for both. The worst for the farmer is offering a bribe that is rejected (0). The staff’s worst is accepting a bribe that never arrives (1).

---

### 3. DSM (Capacitor) Coordination Game – Farmer ↔ Farmer  

| IAD Element | Description |
|------------|-------------|
| **Title** | **Demand‑Side‑Management (DSM) Coordination / Capacitor Adoption** |
| **Location** | Within each transformer’s service area – the physical point where a capacitor would be installed on a farmer’s pump. |
| **Players** | Two *neighboring* farmers (representative pair; the game is repeated among all farmer pairs on the same transformer). |
| **Roles** | Both are *electricity consumers* who can invest in voltage‑stabilising equipment. |
| **Actions** | **Adopt** a capacitor (pay the upfront cost). <br>**Do not adopt** (remain with existing pump). |
| **Control Rules** | – If **both adopt**, the transformer voltage stabilises; each farmer enjoys higher pump efficiency and lower electricity bills (shared benefit). <br>– If **only one adopts**, the adopter bears the full cost but receives only a modest voltage improvement (because the other’s pump still draws down voltage). <br>– If **none adopt**, voltage remains poor; both suffer higher operating costs. |
| **Information** | Farmers observe whether neighbours have installed capacitors (visible hardware) and the *experienced* voltage quality on their own pump. Information about neighbours’ future intentions is *uncertain*. |
| **Outcomes** | • Capacitor installed (yes/no) for each farmer. <br>• Voltage quality level (high/medium/low). <br>• Annual electricity cost (reduced only if enough adopters). |
| **Payoffs (ordinal)** | **Adopter** – 3 = adopt **and** neighbour adopts (full benefit). <br>2 = free‑ride (neighbour adopts, you do not). <br>1 = both do not adopt (status‑quo). <br>0 = adopt alone (cost without benefit). |
| **Strategic Tension** | **Strategic (simultaneous)** – an *assurance/coordination* game. Mutual adoption yields the highest payoff, but a single adopter is penalised, creating a coordination problem. |
| **Temporal Structure** | **Repeated annually**: each year a new “adoption pool” is drawn; successful simultaneous adoption locks the investment for the farmer forever. |
| **Relevant Rules** | *Boundary*: only farmers attached to the same transformer can affect each other’s voltage. <br>*Choice*: binary (Adopt/Not). |
| **Normal‑Form Game** |  |  

|                     | **Neighbour – Adopt** | **Neighbour – Not** |
|---------------------|----------------------|---------------------|
| **Farmer – Adopt**  | (3, 3)               | (0, 2)              |
| **Farmer – Not**    | (2, 0)               | (1, 1)              |

*Explanation*: The joint‑adopt outcome (3,3) is the socially optimal coordination point. The “adopt‑alone” cell (0,2) reflects the adopter’s loss and the non‑adopter’s free‑ride gain.

---

### 4. Groundwater Extraction (Common‑Pool Resource) Game – Farmer ↔ Farmer  

| IAD Element | Description |
|------------|-------------|
| **Title** | **Groundwater Extraction Game** |
| **Location** | Aquifer basin underlying a transformer’s service area (the CPR). |
| **Players** | Two *neighboring* farmers drawing water from the same groundwater table. |
| **Roles** | Both are *water extractors* (irrigation pump operators). |
| **Actions** | **Restrict** extraction (pump at a sustainable rate). <br>**Extract fully** (pump at maximum possible rate). |
| **Control Rules** | – Extraction reduces the aquifer level; the cost of pumping (energy needed) rises with depletion. <br>– If **both restrict**, the aquifer stays near its recharge level → low energy cost for both. <br>– If **one extracts fully** while the other restricts, the extractor enjoys high short‑term water volume (high payoff) but pushes the aquifer toward stress, raising the partner’s future cost. <br>– If **both extract fully**, the aquifer drops sharply → high energy cost for both (lowest payoff). |
| **Information** | Farmers know the current water table depth (measured locally) and the *observed* extraction of neighbours (through pump run‑times). Future aquifer response is uncertain. |
| **Outcomes** | • Actual water extracted (cubic metres). <br>• Aquifer depth change (incremental). <br>• Energy cost per unit water (higher when depth increases). |
| **Payoffs (ordinal)** | **Extractor** – 3 = high water now *and* the other restricts (short‑term gain). <br>2 = both restrict (stable, sustainable yields). <br>1 = restrict while neighbour extracts fully (lower yield). <br>0 = both extract fully (high cost, low net benefit). |
| **Strategic Tension** | **Strategic (simultaneous)** – a *common‑pool resource* (tragedy‑of‑the‑commons) game. Mutual restraint is jointly optimal, yet each farmer has an incentive to over‑extract if the other restrains. |
| **Temporal Structure** | **Repeated each month** (the “groundwater extraction” step). The game’s payoff matrix shifts over time as the aquifer depth changes, but the ordinal ranking remains as above for each period. |
| **Relevant Rules** | *Boundary*: all farmers sharing the same aquifer belong to the same CPR. <br>*Position*: extraction level influences the physical state of the aquifer (control rule). |
| **Normal‑Form Game** |  |  

|                     | **Neighbour – Restrict** | **Neighbour – Extract** |
|---------------------|--------------------------|--------------------------|
| **Farmer – Restrict**| (2, 2)                  | (1, 3)                  |
| **Farmer – Extract** | (3, 1)                  | (0, 0)                  |

*Explanation*: (Restrict, Restrict) yields a moderate but sustainable payoff (2). (Extract, Restrict) gives the extractor the highest short‑term payoff (3) while the restrictor suffers (1). Mutual over‑extraction collapses payoffs to 0.

---

### 5. Regulatory Subsidy Coordination Game – Regulator ↔ Farmer  

*(Replaced the earlier “Capacity‑Provision” game to guarantee a distinct strategic pattern.)*  

| IAD Element | Description |
|------------|-------------|
| **Title** | **Subsidy‑for‑Capacitor Adoption Game** |
| **Location** | State‑level regulatory office (APERC) – policy‑setting arena; implementation occurs at the transformer level. |
| **Players** | **Regulator** (APERC) and a **Farmer** (representative of a group of farmers on a transformer). |
| **Roles** | Regulator = *policy‑maker / subsidy‑grantor*; Farmer = *technology adopter*. |
| **Actions** | **Regulator:** 1 → **Subsidize** (provide a per‑capactor grant, reducing farmer’s adoption cost). <br>2 → **Do not subsidize**. <br>**Farmer:** 1 → **Adopt** capacitor (pay net cost after any subsidy). <br>2 → **Do not adopt**. |
| **Control Rules** | – If **Subsidize & Adopt**, the farmer pays a reduced cost and the regulator expends budget; voltage improves for the whole transformer. <br>– **Subsidize & Not adopt** wastes public funds (regulator gets low payoff). <br>– **No subsidy & Adopt** forces the farmer to bear full cost (farmer’s payoff low). <br>– **No subsidy & Not adopt** leaves the status‑quo (moderate payoff for both). |
| **Information** | Regulator knows the aggregate budget constraint and the estimated social benefit of voltage improvement, but not the exact willingness‑to‑pay of each farmer. <br>Farmer knows his own budget, the announced subsidy level (if any), and the expected voltage gain (based on neighbours’ adoption). |
| **Outcomes** | • Capacitor installed (yes/no). <br>• Regulator’s budget consumption. <br>• Transformer voltage quality. |
| **Payoffs (ordinal)** | **Farmer** – 3 = adopt with subsidy (low net cost + voltage gain). <br>2 = do not adopt (status‑quo). <br>1 = adopt without subsidy (high net cost). <br>0 = subsidy offered but farmer does not adopt (wasted public money). <br>**Regulator** – 3 = subsidy + adoption (social benefit achieved). <br>2 = no subsidy + no adoption (budget saved, no benefit). <br>1 = subsidy + no adoption (budget waste). <br>0 = no subsidy + adoption (farmer bears cost, regulator misses opportunity to improve welfare). |
| **Strategic Tension** | **Strategic (simultaneous)** – an *public‑goods/subsidy* game. The regulator wants adoption but must decide whether to spend limited funds; the farmer wants the subsidy but may forego adoption if the grant is absent. |
| **Temporal Structure** | Decided **once per year** (the “institutional push toward DSM adoption” step). |
| **Relevant Rules** | *Boundary*: only farmers attached to the transformer are eligible for the subsidy. <br>*Position*: regulator’s willingness to subsidize is limited by a budget parameter. |
| **Normal‑Form Game** |  |  

|                     | **Regulator – Subsidize** | **Regulator – No Subsidy** |
|---------------------|---------------------------|---------------------------|
| **Farmer – Adopt**  | (3, 3)                    | (1, 0)                    |
| **Farmer – Not**    | (0, 1)                    | (2, 2)                    |

*Explanation*: The joint (Subsidize, Adopt) outcome is the Pareto‑optimal (3,3). If the regulator withholds the subsidy and the farmer still adopts, the farmer suffers (1) while the regulator gets nothing (0). If the regulator subsidizes but the farmer refuses, the regulator incurs a waste (1) and the farmer stays at status‑quo (0). The “no‑subsidy / no‑adopt” cell (2,2) reflects budget saving and the farmer’s unchanged situation.

---

### 6. Social‑Learning & Imitation Process – Farmer → Farmer (Non‑Strategic)  

| IAD Element | Description |
|------------|-------------|
| **Title** | **Capacitor Adoption Experimentation & Imitation** |
| **Location** | Transformer service area (the “adoption pool” is created at the transformer level each year). |
| **Players** | *All* farmers attached to the transformer (the process is population‑wide; no simultaneous move). |
| **Roles** | Farmers are *observers* and *potential imitators*. |
| **Actions** | 1. **Experimentation** – a stochastic draw selects a small set of “experimenters” who may adopt a capacitor regardless of neighbours’ current adoption count. <br>2. **Imitation** – if a transformer’s cumulative adopters exceed a threshold in a given cycle, every other farmer on that transformer becomes *eligible* to imitate with a fixed yearly probability. |
| **Control Rules** | – Experimenters pay the adoption cost immediately; if the adoption fails to reach the threshold, the cost is sunk with no shared benefit. <br>– Imitators only adopt when the *assurance* condition (enough neighbours already adopted) is satisfied; otherwise they wait. |
| **Information** | Farmers perfectly observe **who** has already installed a capacitor (visible hardware) but have *no* perfect knowledge of the future benefit magnitude; they only know the *observed* voltage improvement of neighbours. |
| **Outcomes** | • Number of new adopters per year. <br>• Update of the transformer’s voltage quality (if the threshold is crossed). |
| **Payoffs** | Not modelled as explicit utility; the process simply changes the state variables used in the strategic DSM Coordination Game (Situation 3). |
| **Strategic Tension** | **Non‑strategic** – a sequential process (experiment → possible imitation). No simultaneous move; the “game” is a *learning* routine. |
| **Temporal Structure** | **Annual**: at the start of each year the experiment pool is drawn; later in the year the imitation step may occur. |
| **Relevant Rules** | *Boundary*: only farmers attached to the transformer are in the pool. <br>*Position*: the imitation eligibility threshold (τ) is a model parameter. <br>*Choice*: adoption is forced for experimenters; imitators decide probabilistically. |

---

## Comparative Analysis of the Strategic Core  

| Situation | Players | Game Type (as‑named) | Ordinal Pay‑off Pattern | Key Dilemma |
|-----------|---------|----------------------|--------------------------|-------------|
| 1 Authorization | Farmer ↔ Staff | **Authorization / Coordination** | (3,3) > (2,2) > (1,1) > (0,2) / (0,2) | Both need each other’s move to obtain a legal connection; risk of unilateral rejection. |
| 2 Collusion‑Exchange | Farmer ↔ Staff | **Trust / Collusion** | (3,3) > (2,2) > (2,1) > (0,2) | Mutual illicit gain vs risk of wasted bribe or missed opportunity. |
| 3 DSM Coordination | Farmer ↔ Farmer | **Assurance / Coordination** | (3,3) > (2,0) = (0,2) > (1,1) | Adoption only valuable if enough neighbours also adopt; free‑riding temptation. |
| 4 Groundwater Extraction | Farmer ↔ Farmer | **Common‑Pool Resource** | (3,1) & (1,3) > (2,2) > (0,0) | Over‑extraction yields short‑term gain but collapses the pool; mutual restraint is jointly optimal. |
| 5 Regulatory Subsidy | Regulator ↔ Farmer | **Public‑Goods / Subsidy** | (3,3) > (2,2) > (1,0) > (0,1) | Regulator must decide whether to spend limited budget; farmer decides whether to adopt given the subsidy. |
| 6 Social‑Learning | – | **Non‑strategic sequential** | – | No simultaneous move; learning updates the state for Situation 3. |

### Distinctiveness Check  

| Pair of Situations | Overlap? | Reason for Distinctness |
|--------------------|----------|--------------------------|
| 1 vs 2 | **No** – different payoff ordering and underlying motive (legal connection vs illicit gain). |
| 1 vs 5 | **No** – player set differs (staff vs regulator) and the regulator’s decision is budget‑constrained, not discretionary authorisation. |
| 2 vs 5 | **No** – collusion is a *trust* game with no public‑budget dimension; subsidy game is a *public‑goods* provision. |
| 3 vs 4 | **No** – DSM coordination is a *technology‑adoption* assurance game; groundwater extraction is a *resource‑extraction* CPR game. |
| 3 vs 6 | **No** – Situation 3 is a strategic 2‑player game; Situation 6 is a population‑level learning routine (non‑strategic). |
| 4 vs 5 | **No** – different resource (water vs electricity) and different institutional actors. |

Thus every strategic interaction maps onto a **different governance problem** (authorization, collusion, technology coordination, CPR management, subsidy provision). The non‑strategic learning process supplies the *behavioral‑feedback* link between them.

---

## Revision for Strategic Diversity  

During the comparison it became clear that the original “Capacity‑Provision” game (farmer ↔ staff) duplicated the **authorization** pattern (both involved the same two actors and a similar “both cooperate → high payoff” structure). To guarantee a broader set of dilemmas, we **replaced** that game with the **Regulatory Subsidy Coordination Game** (Situation 5).  

*Why the replacement satisfies the ODD + D description*  

* **Players** now include the **regulator (APERC)**, an entity explicitly mentioned in the ODD (II.i a).  
* The decision **“state‑driven institutional push toward DSM adoption”** (process step 5) is precisely the annual subsidy‑announcement described in the model overview.  
* The payoff matrix respects the ordinal‑rank requirement (0‑3) and captures the asymmetric incentives (budget constraint for the regulator, cost‑benefit trade‑off for the farmer).  
* The game introduces a **public‑goods** dilemma that is *institutionally* distinct from the *authorization* and *collusion* dilemmas, thereby enriching the strategic core of the model.

---

### Final Set of Action Situations  

| # | Title | Type (Strategic / Non‑Strategic) |
|---|-------|---------------------------------|
| 1 | Authorization Decision | Strategic – Coordination / Authorization |
| 2 | Collusive Exchange (Trust) | Strategic – Trust / Collusion |
| 3 | DSM Coordination (Capacitor Adoption) | Strategic – Assurance / Coordination |
| 4 | Groundwater Extraction (CPR) | Strategic – Common‑Pool Resource |
| 5 | Regulatory Subsidy Coordination | Strategic – Public‑Goods / Subsidy |
| 6 | Social‑Learning & Imitation Process | Non‑Strategic – Sequential Learning |

Each of these six situations is **mutually exclusive** in terms of the decision problem it addresses, and together they reproduce the full governance dynamics described in the ODD + D protocol for the Andhra Pradesh electricity‑irrigation model.
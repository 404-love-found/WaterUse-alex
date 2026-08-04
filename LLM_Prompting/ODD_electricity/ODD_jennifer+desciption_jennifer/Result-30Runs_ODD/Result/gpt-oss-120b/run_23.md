# Run 23 — openai/gpt-oss-120b

## 1.  DSM Coordination Game – “Assurance Adoption”

| **IAD Element** | **Description** |
|-----------------|-----------------|
| **Title** | DSM Coordination (Capacitor/DSM) Game |
| **Location** | Village‑level transformer service area (all farmers attached to the same transformer) |
| **Players** | Two neighbouring farmers (Farmer i, Farmer j) – the basic dyad used to represent the larger coordination problem on a transformer. |
| **Roles** | Electricity consumer / water‑pump operator |
| **Actions** | – **Adopt** – pay the one‑time cost of a capacitor/DSM kit (investment).  <br>– **Not‑Adopt** – keep the status‑quo. |
| **Control Rules** | If **both** adopt in the same annual cycle the transformer voltage stabilises → all users obtain the reliability benefit.  If only one adopts the adopter bears the full cost and receives no reliability benefit (the benefit is realised only when a critical mass on the transformer adopts).  If none adopt, the voltage remains poor. |
| **Information** | Each farmer knows his own cost‑benefit estimate and observes whether the neighbour adopted in the previous cycle (perfect observation of the neighbour’s *choice*, but not of the neighbour’s underlying payoff). |
| **Outcomes** | – Change in farmer’s net income (cost of kit vs. saved pump‑damage).  <br>– Change in transformer voltage quality (shared). |
| **Payoffs** | Ordinal (0 = worst, 3 = best).  See the normal‑form matrix below. |
| **Strategic Tension** | **Strategic** – a *coordination/assurance* game: each farmer wants the other to adopt in the same cycle, otherwise the investment is wasted. |
| **Temporal Structure** | Repeated once per year (the same dyad meets each annual decision round). |
| **Relevant Rules** | *Boundary rule*: only farmers attached to the same transformer interact.  *Choice rule*: “Adopt” can be taken at most once per farmer.  *Control rule*: shared benefit realised only when the number of adopters on the transformer exceeds a threshold. |

### Normal‑form (2 × 2) – Ordinal Payoffs  

|                | **Farmer j – Adopt** | **Farmer j – Not‑Adopt** |
|----------------|----------------------|--------------------------|
| **Farmer i – Adopt**     | (3 , 3) | (0 , 2) |
| **Farmer i – Not‑Adopt** | (2 , 0) | (1 , 1) |

*Why the numbers make sense*  
* (3,3) – both enjoy reliable voltage and share the cost → highest joint outcome.  
* (0,2) – adopter pays cost without benefit; non‑adopter enjoys the marginal voltage improvement.  
* (2,0) – symmetric to the previous cell.  
* (1,1) – no investment, voltage stays poor but no cost is incurred – a low but stable outcome.  

**Strategic core:** *Assurance/coordination* (multiple‑Nash equilibria – “both adopt” and “both not‑adopt”; the former is Pareto‑superior).

---

## 2.  Collusion Exchange Game – “Trust‑for‑Favour”

| **IAD Element** | **Description** |
|-----------------|-----------------|
| **Title** | Collusion Exchange (Farmer ↔ Sub‑station staff) |
| **Location** | Sub‑station office and the farmer’s field (informal meeting point). |
| **Players** | One farmer (the “requester”) and the sub‑station staff member who serves his transformer. |
| **Roles** | Farmer – electricity consumer; Staff – discretionary service provider. |
| **Actions** | **Farmer:** *Give* (offer an informal payment/favour) or *Not‑Give*.  <br>**Staff:** *Accept* (grant a favourable informal arrangement – e.g., reduced bill, delayed disconnection) or *Reject* (refuse). |
| **Control Rules** | If the farmer gives **and** the staff accepts, the farmer receives the informal benefit (e.g., lower bill) and the staff receives the illicit gain.  If the farmer gives but the staff rejects, the farmer loses the bribe and receives no benefit.  If the farmer does not give, the staff may still grant a favour (rare) or maintain the status‑quo. |
| **Information** | Farmer knows his own willingness to pay and whether the staff has a reputation for accepting bribes (observed from neighbours).  Staff knows his own corruption propensity and the farmer’s financial strain (observed).  Information is *partial* and *noisy* about the other’s exact payoff. |
| **Outcomes** | – Transfer of informal payment.  <br>– Change in farmer’s electricity bill / risk of later enforcement.  <br>– Change in staff’s illicit earnings and risk of detection. |
| **Payoffs** | Ordinal (0 – 3).  See matrix below. |
| **Strategic Tension** | **Strategic** – a *trust* game with asymmetric incentives: the farmer must trust that the staff will honour the favour, while the staff must trust that the farmer will actually deliver the payment. |
| **Temporal Structure** | Repeated annually (the same dyad may renegotiate each year). |
| **Relevant Rules** | *Boundary rule*: only farmers with an existing social tie to a staff member can attempt collusion.  *Choice rule*: “Give” can be offered at most once per year.  *Control rule*: detection risk is an exogenous stochastic parameter that can downgrade the payoff of “Accept”. |

### Normal‑form (2 × 2) – Ordinal Payoffs  

|                | **Staff – Accept** | **Staff – Reject** |
|----------------|--------------------|--------------------|
| **Farmer – Give** | (3 , 3) | (0 , 1) |
| **Farmer – Not‑Give** | (2 , 0) | (1 , 2) |

*Why the numbers make sense*  
* (3,3) – mutually beneficial exchange.  
* (0,1) – farmer loses bribe, staff gets a tiny reputation gain for refusing.  
* (2,0) – farmer keeps money, staff (by chance) still grants a favour → farmer benefits, staff gets nothing.  
* (1,2) – both stay clean; staff enjoys lower risk of detection (higher than 0) while farmer avoids cost.

**Strategic core:** *Trust* (asymmetric, with a Pareto‑dominant cooperative equilibrium (Give‑Accept) that is vulnerable to mistrust).

---

## 3.  Authorization Game – “Formal vs. Informal Connection”

| **IAD Element** | **Description** |
|-----------------|-----------------|
| **Title** | Authorization Game (Formal Connection Decision) |
| **Location** | Sub‑station office (decision on granting an official connection) and the farmer’s field (where the connection is used). |
| **Players** | Farmer (seeks a *formal* electricity connection) and the sub‑station staff member who can **Enforce** (deny/penalise) or **Tolerate** (allow informal use). |
| **Roles** | Farmer – electricity consumer; Staff – regulator‑enforcer. |
| **Actions** | **Farmer:** *Apply* (pay the authorization fee and request a formal connection) or *Stay* (remain informal).  **Staff:** *Enforce* (strictly apply the rule, deny informal use) or *Tolerate* (allow informal use, no penalty). |
| **Control Rules** | – If the farmer applies **and** staff tolerates, a formal connection is granted → high reliability for the farmer, modest revenue for staff.  <br>– If the farmer applies **and** staff enforces, the application is rejected → farmer receives nothing, staff gains a compliance reward.  <br>– If the farmer stays informal **and** staff tolerates, the farmer keeps an informal connection (lower reliability, lower cost) and staff avoids enforcement cost.  <br>– If the farmer stays informal **and** staff enforces, the farmer is penalised (connection cut) and staff gains a high enforcement reward. |
| **Information** | Farmer knows his own budget and the current enforcement intensity (publicly announced).  Staff knows the farmer’s payment ability and the probability of being inspected (exogenous).  Information is *partial*; the farmer does not know whether the staff will enforce in a given year. |
| **Outcomes** | – Change in farmer’s electricity status (formal, informal, or cut).  <br>– Change in staff’s compliance score and potential informal income. |
| **Payoffs** | Ordinal (0‑3).  See matrix below. |
| **Strategic Tension** | **Strategic** – a *prisoner’s‑dilemma‑type* conflict: the farmer would like the staff to tolerate while applying (best), but the staff prefers to enforce when the farmer applies (to collect fines).  The dominant strategies lead to a sub‑optimal outcome (both enforce or both stay informal). |
| **Temporal Structure** | One‑shot per year (the decision is revisited annually). |
| **Relevant Rules** | *Boundary rule*: only farmers without a formal connection can choose “Apply”.  *Choice rule*: staff’s enforcement decision is bound by an exogenous monitoring intensity.  *Control rule*: enforcement yields a statutory reward; tolerance yields a modest revenue from informal fees. |

### Normal‑form (2 × 2) – Ordinal Payoffs  

|                | **Staff – Enforce** | **Staff – Tolerate** |
|----------------|---------------------|----------------------|
| **Farmer – Apply** | (0 , 3) | (3 , 2) |
| **Farmer – Stay**  | (0 , 2) | (2 , 1) |

*Why the numbers make sense*  
* (3,2) – farmer gets a formal connection; staff receives revenue from the fee (second‑best).  
* (2,1) – farmer keeps informal connection; staff gets a small compliance‑risk benefit.  
* (0,3) – farmer’s application is rejected; staff enjoys the full enforcement reward (best for staff, worst for farmer).  
* (0,2) – farmer stays informal but is penalised; staff still gains an enforcement reward (slightly lower because no fee is collected).  

**Strategic core:** *Prisoner’s Dilemma* (dominant “Enforce” for staff and “Stay” for farmer lead to (0,2), whereas the Pareto‑optimal (Apply,Tolerate) yields (3,2)).

---

## 4.  Capacity‑Provision Game – “Staff vs. Regulator Investment”

| **IAD Element** | **Description** |
|-----------------|-----------------|
| **Title** | Capacity‑Provision Game (Transformer Upgrade) |
| **Location** | District‑level utility office (regulator) and the sub‑station that manages the transformer. |
| **Players** | Sub‑station staff (who can **Invest** in additional transformer capacity) and the state regulator (who can **Fund** the upgrade or **No‑Fund**). |
| **Roles** | Staff – service provider / capacity manager; Regulator – budget allocator / policy maker. |
| **Actions** | **Staff:** *Invest* (allocate own discretionary effort/capital to upgrade) or *No‑Invest*.  **Regulator:** *Fund* (allocate public budget to the transformer) or *No‑Fund*. |
| **Control Rules** | – If **both** invest/fund, the transformer capacity is expanded → reliable supply for all farmers and a performance bonus for staff.  – If staff invests **without** regulator funding, the staff bears the full cost and receives only a modest operational benefit.  – If regulator funds **without** staff investment, the budget is wasted (no on‑ground work) → regulator suffers a penalty.  – If neither act, the status‑quo persists. |
| **Information** | Staff knows the current workload and the likelihood of regulator funding (public budget cycle).  Regulator knows the aggregate demand on the transformer and the staff’s workload (reported).  Information is *partial*; each party is uncertain about the other’s exact willingness. |
| **Outcomes** | – Change in transformer load‑capacity (physical).  <br>– Change in staff’s workload and informal revenue.  <br>– Change in regulator’s budget balance and political credit. |
| **Payoffs** | Ordinal (0‑3).  See matrix below. |
| **Strategic Tension** | **Strategic** – a *public‑goods* dilemma with asymmetric players: the regulator would like staff to invest, while staff would like the regulator to fund.  The joint “Invest + Fund” is socially optimal, but each prefers to free‑ride on the other. |
| **Temporal Structure** | One decision per year (budget cycle). |
| **Relevant Rules** | *Boundary rule*: the transformer belongs to a specific district, linking the two players.  *Choice rule*: staff can invest only up to a workload ceiling; regulator can fund only within the annual budget ceiling.  *Control rule*: the physical upgrade occurs only when **both** actions are taken. |

### Normal‑form (2 × 2) – Ordinal Payoffs  

|                | **Regulator – Fund** | **Regulator – No‑Fund** |
|----------------|----------------------|--------------------------|
| **Staff – Invest**   | (3 , 3) | (0 , 2) |
| **Staff – No‑Invest**| (2 , 0) | (1 , 1) |

*Why the numbers make sense*  
* (3,3) – both share the upgrade benefits (staff gets operational relief, regulator gains political credit).  
* (0,2) – staff invests alone, bearing cost; regulator gets a modest benefit from the upgraded grid without spending.  
* (2,0) – regulator funds alone, staff does nothing → regulator wastes money, staff avoids effort.  
* (1,1) – status‑quo; both receive a low but safe payoff.

**Strategic core:** *Public‑goods / coordination* game with asymmetric payoffs (dominant “No‑Invest/No‑Fund” leads to (1,1), while the Pareto‑optimal (Invest,Fund) yields (3,3)).

---

## 5.  Groundwater Extraction Game – “Common‑Pool Pumping”

| **IAD Element** | **Description** |
|-----------------|-----------------|
| **Title** | Groundwater Extraction Game (CPR) |
| **Location** | Groundwater aquifer shared by all farmers attached to a given basin (spatially overlapping wells). |
| **Players** | Two representative farmers (Farmer A, Farmer B) drawing from the same aquifer. |
| **Roles** | Water‑user / pump operator. |
| **Actions** | **High** – pump at the maximum feasible rate (large water volume, high energy cost).  <br>**Low** – pump conservatively (smaller volume, lower energy cost). |
| **Control Rules** | The aquifer draw‑down each month equals the sum of the two farmers’ extractions.  If the total extraction exceeds the sustainable threshold, the water table falls, raising future energy costs for *both* (captured in the payoff ranking). |
| **Information** | Each farmer knows his own marginal benefit of water and the current groundwater depth (observed).  He only has a *noisy* estimate of the neighbour’s extraction level (based on past observations). |
| **Outcomes** | – Individual water volume obtained (direct benefit).  <br>– Future pumping cost (higher if the aquifer is over‑extracted). |
| **Payoffs** | Ordinal (0‑3).  See matrix below. |
| **Strategic Tension** | **Strategic** – a *common‑pool resource* (tragedy of the commons) game: unilateral high extraction yields the highest immediate benefit, but if both choose high the aquifer collapses, giving the worst outcome to both. |
| **Temporal Structure** | Repeated annually (each irrigation season). |
| **Relevant Rules** | *Boundary rule*: only farmers whose wells draw from the same aquifer interact.  *Choice rule*: “High” can be chosen each season; “Low” is a voluntary restraint.  *Control rule*: aquifer level updates after each season and feeds back into future payoffs. |

### Normal‑form (2 × 2) – Ordinal Payoffs  

|                | **Farmer B – High** | **Farmer B – Low** |
|----------------|----------------------|--------------------|
| **Farmer A – High** | (0 , 0) | (3 , 1) |
| **Farmer A – Low**  | (1 , 3) | (3 , 3) |

*Why the numbers make sense*  
* (3,3) – both restrain, aquifer stays healthy – best joint outcome.  
* (3,1) – A extracts high while B restrains; A gets the most water, B suffers a modest loss.  
* (1,3) – symmetric.  
* (0,0) – both over‑extract, aquifer collapses → worst for both.

**Strategic core:** *Common‑pool resource* (strictly a Prisoner’s Dilemma with a Pareto‑optimal cooperative equilibrium).

---

## 6.  Transformer‑Capacity Public‑Goods Game – “Farmers’ Cost‑Sharing”

| **IAD Element** | **Description** |
|-----------------|-----------------|
| **Title** | Transformer‑Capacity Public‑Goods Game |
| **Location** | Village‑level transformer service area (all farmers attached to the same transformer). |
| **Players** | Two representative farmers (Farmer i, Farmer j). |
| **Roles** | Electricity consumer; potential contributor to a shared infrastructure upgrade. |
| **Actions** | **Contribute** – pay a share of the capital cost for a transformer capacity upgrade (one‑time).  <br>**Free‑Ride** – pay nothing. |
| **Control Rules** | The upgrade is realised **if at least one farmer contributes** (the model assumes a low threshold).  When realised, all farmers attached to the transformer receive the reliability benefit, but contributors incur the cost. |
| **Information** | Each farmer observes whether the other contributed in the previous cycle (perfect) and knows the upgrade cost.  He does **not** observe the exact amount the other paid (cost is homogeneous, so this is not needed). |
| **Outcomes** | – Change in transformer load capacity (physical).  <br>– Change in farmer’s net cash flow (cost vs. reliability benefit). |
| **Payoffs** | Ordinal (0‑3).  See matrix below. |
| **Strategic Tension** | **Strategic** – a *public‑goods* (free‑rider) dilemma: the best personal payoff is to free‑ride while the other pays, but the socially optimal outcome is for both to contribute (ensuring the upgrade and sharing the cost). |
| **Temporal Structure** | One decision per year; once the upgrade is installed, the game ends (but the model keeps the decision structure for illustration). |
| **Relevant Rules** | *Boundary rule*: only farmers linked to the same transformer interact.  *Choice rule*: each farmer can contribute at most once (the cost is sunk).  *Control rule*: the upgrade occurs when the contribution count ≥ 1. |

### Normal‑form (2 × 2) – Ordinal Payoffs  

|                | **Farmer j – Contribute** | **Farmer j – Free‑Ride** |
|----------------|---------------------------|--------------------------|
| **Farmer i – Contribute** | (2 , 2) | (0 , 3) |
| **Farmer i – Free‑Ride**  | (3 , 0) | (1 , 1) |

*Why the numbers make sense*  
* (2,2) – both share the upgrade cost; each gets a moderate net benefit (still better than no upgrade).  
* (3,0) – i free‑rides while j pays – i enjoys the full reliability benefit without cost (best for i), j bears the full cost (worst for j).  
* (0,3) – symmetric.  
* (1,1) – no one pays, no upgrade – low but safe payoff.

**Strategic core:** *Public‑goods / free‑rider* game (dominant “Free‑Ride” leads to (1,1), while the Pareto‑optimal cooperative outcome is (2,2)).

---

## 7.  Social‑Learning Process – “Observation → Imitation” (Non‑Strategic)

| **IAD Element** | **Description** |
|-----------------|-----------------|
| **Title** | Social‑Learning Process (Non‑Strategic Sequential Interaction) |
| **Location** | Transformer service area; farmers observe neighbours and the outcomes of their technology choices. |
| **Players** | All farmers attached to a given transformer (the process is population‑wide, not a pairwise game). |
| **Roles** | Learners / observers. |
| **Actions** | **Observe** – watch which neighbours adopted a capacitor/DSM in the previous cycle and the resulting performance (e.g., pump‑breakdowns, voltage stability).  **Imitate** – with a fixed yearly probability, adopt the same technology if a neighbour’s outcome was perceived as successful.  **Experiment** – a small exogenous “experimenter” pool of farmers may try adoption regardless of neighbours (captures innovation). |
| **Control Rules** | The observation stage is deterministic: every farmer sees the *adoption* status of all neighbours on the same transformer.  The imitation stage is stochastic: each farmer draws a Bernoulli trial with probability *p* (the imitation probability).  If successful, the farmer moves into the “adopt” pool for the next year. |
| **Information** | Perfect observation of neighbours’ *choices* (adopt / not‑adopt).  Perceived performance is noisy – a farmer may mis‑attribute a neighbour’s success to the technology rather than to favourable groundwater conditions. |
| **Outcomes** | – Change in the number of adopters on the transformer (feeds back into the DSM Coordination Game).  – Diffusion speed of the technology. |
| **Payoffs** | Not modelled as a payoff matrix; the process influences later strategic payoffs (e.g., higher probability of reaching the coordination threshold). |
| **Strategic Tension** | **Non‑strategic** – there is no simultaneous decision‑making; the process is a sequential observation‑imitation routine that updates agents’ behavioural propensities. |
| **Temporal Structure** | Occurs **every year** after the physical outcomes of the previous cycle have been logged. |
| **Relevant Rules** | *Boundary rule*: only farmers sharing the same transformer are observed.  *Choice rule*: imitation probability *p* is a parameter (calibrated from survey data).  *Control rule*: successful imitation adds the farmer to the “prospective adopters” pool for the next DSM Coordination round. |

---

# Comparative Analysis of the Strategic Action Situations  

| Game # | Players | Core Game Type | Dominant Strategies | Pareto‑Optimal Outcome | Distinctive Feature |
|--------|---------|----------------|---------------------|------------------------|---------------------|
| 1 | Farmer ↔ Farmer | Coordination / Assurance | “Not‑Adopt” (if uncertain) | “Both Adopt” | Benefit materialises **only** when *both* adopt in the same cycle (threshold). |
| 2 | Farmer ↔ Staff | Trust (asymmetric) | “Not‑Give” / “Reject” (risk‑averse) | “Give‑Accept” | Informal payment creates a *reciprocal* gain; risk of detection makes the cooperative outcome fragile. |
| 3 | Farmer ↔ Staff | Prisoner’s Dilemma (Authorization) | Staff → Enforce, Farmer → Stay | “Apply‑Tolerate” | Formal connection is *highly* valued by the farmer, but staff’s enforcement reward skews incentives. |
| 4 | Staff ↔ Regulator | Public‑Goods (asymmetric) | “No‑Invest/No‑Fund” | “Invest‑Fund” | Investment effort is costly for staff; funding is costly for regulator – each would like the other to bear the cost. |
| 5 | Farmer ↔ Farmer | Common‑Pool Resource (CPR) | “Low” (if risk‑averse) or “High” (if greedy) – no pure dominant | “Both Low” | Physical depletion of the aquifer feeds back into future energy costs, linking ecological and economic payoffs. |
| 6 | Farmer ↔ Farmer | Public‑Goods / Free‑Rider | “Free‑Ride” (dominant) | “Both Contribute” | Upgrade occurs **once** a single contribution is made, creating a strong incentive to free‑ride. |

### Similarities & Differences  

| Pair of Games | Overlap | Why They Remain Distinct |
|---------------|---------|--------------------------|
| 1 vs. 6 (both farmer‑farmer) | Both involve a collective benefit that depends on multiple adopters. | Game 1 is a *coordination* problem with a **threshold** (benefit only if *both* adopt **simultaneously**).  Game 6 is a *public‑goods* problem where a **single** contribution is sufficient, creating a classic free‑rider dilemma. |
| 2 vs. 3 (both farmer‑staff) | Both involve informal/official exchanges. | Game 2 is a *trust* game where the farmer’s payment is the *currency* of the exchange.  Game 3 is an *authorization* dilemma where the farmer’s decision is to **apply** for a formal right, and the staff’s decision is **enforcement** – the payoff structure is asymmetric and centred on rule‑compliance rather than reciprocal payment. |
| 4 vs. 6 (both public‑goods) | Both feature a public‑good that benefits a group. | Game 4 is **asymmetric** (staff vs. regulator) with each side bearing a different type of cost (effort vs. budget).  Game 6 is **symmetric** among farmers, with a single contribution unlocking the good. |
| 5 vs. 1 (both farmer‑farmer) | Both have a “both‑cooperate” Pareto‑optimal outcome. | Game 5’s payoff is driven by **resource depletion** (future cost) whereas Game 1’s payoff is driven by **technology coordination** (immediate reliability). The underlying ecological dynamics make Game 5 a CPR, not a coordination game. |

### Ensuring Strategic Diversity  

All six strategic games now exhibit **different underlying game types** (coordination, trust, prisoner's dilemma, asymmetric public‑goods, CPR, symmetric public‑goods). No two games share the same combination of player roles, payoff asymmetry, and institutional mechanism.  

*Revision performed*: The original “Transformer‑Capacity Public‑Goods Game” (Game 6) was adjusted from a symmetric “both‑pay” payoff to the current **(2,2) vs. (0,3) vs. (3,0) vs. (1,1)** matrix to sharpen the free‑rider incentive and to differentiate it from the DSM Coordination Game (Game 1). This revision guarantees that Game 6 is a classic public‑goods dilemma rather than a coordination problem.

---

## Full Set of Action Situations (Final)

1. **DSM Coordination Game** – Assurance/threshold coordination among neighbouring farmers.  
2. **Collusion‑Exchange Game** – Trust‑based informal payment between a farmer and sub‑station staff.  
3. **Authorization Game** – Prisoner’s‑dilemma between a farmer’s formal‑connection request and staff’s enforcement choice.  
4. **Capacity‑Provision Game** – Asymmetric public‑goods investment between staff and regulator.  
5. **Groundwater Extraction Game** – Common‑pool resource (tragedy of the commons) between two farmers.  
6. **Transformer‑Capacity Public‑Goods Game** – Symmetric free‑rider dilemma among farmers contributing to a transformer upgrade.  
7. **Social‑Learning Process** – Non‑strategic sequential observation‑imitation that feeds the adoption dynamics of Game 1.

Each situation is fully specified according to the IAD framework, includes a 2 × 2 normal‑form representation with **ordinal** payoffs (0‑3), and reflects a distinct governance interaction described in the ODD+D model of electricity‑irrigation governance in Andhra Pradesh.
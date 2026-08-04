# Run 3 — openai/gpt-oss-120b

## 1.  Authorization Game – “Formal vs. Informal Electricity Access”

| Element | Description |
|--------|-------------|
| **Title** | Authorization Game |
| **Location** | Village‑level transformer service area (the point where a farmer requests a connection and the sub‑station staff processes the request). |
| **Players** | 1️⃣ Farmer (consumer)  <br>2️⃣ Sub‑station staff (enforcer / service provider) |
| **Roles** | Farmer – electricity consumer who can request a **formal** connection.<br>Staff – authority who can **authorize** the request (record the connection, invest minimal effort) or **deny/ignore** it. |
| **Actions** | **Farmer:** ① *Seek formal authorization* (A)  ② *Remain informal* (I) <br>**Staff:** ① *Authorize* (Auth) ② *Deny / ignore* (Deny) |
| **Control Rules** | – If **A + Auth** → farmer receives a legal connection, pays a fixed fee; staff records the connection and incurs a small effort cost. <br>– If **A + Deny** → farmer stays informal, bears risk of penalty; staff avoids effort. <br>– If **I + Auth** → staff creates a formal record for a farmer who did not request it (rare, wasteful). <br>– If **I + Deny** → status‑quo informal connection persists. |
| **Information** | • Farmer knows the current **monitoring intensity** (high/low) and the typical **approval rate** (partial, based on past observations). <br>• Staff knows the farmer’s **payment capacity** and the **oversight risk** (probability of being inspected). Information is **partial** and may be noisy (e.g., farmer may over‑estimate likelihood of approval). |
| **Outcomes** | • Legal connection status (yes/no) <br>• Fee paid (yes/no) <br>• Staff effort cost (yes/no) <br>• Risk of penalty for the farmer (high/low) |
| **Payoffs** (ordinal 0‑3) | See payoff matrix below. |
| **Strategic Tension** | **Strategic** – a **Public‑Goods / Authorization game**.  The farmer’s benefit (reliable electricity) is a public good that requires the staff’s costly authorization.  The staff can free‑ride by denying while the farmer still has informal access, creating an asymmetric dilemma. |
| **Temporal Structure** | One‑shot each **annual decision cycle** (players choose simultaneously at the start of the irrigation year). |
| **Relevant Rules** | • **Boundary rule:** Only farmers attached to the transformer are eligible. <br>• **Choice rule:** Farmer may submit a formal request; staff may approve or not. <br>• **Control rule:** Approval creates a legal record; denial leaves the informal status unchanged. |

### Payoff Matrix (Farmer rows × Staff columns)

|                | **Authorize** | **Deny** |
|----------------|--------------|----------|
| **Seek A**     | (3, 2)       | (1, 3)   |
| **Remain I**   | (2, 1)       | (2, 2)   |

*Interpretation* –  
*Farmer* gets the highest rank (3) when the request is approved; the lowest rank (1) when he seeks approval but is denied. *Staff* prefers to avoid effort (rank 3) when the farmer seeks approval but is denied, but dislikes authorizing a farmer who did not ask (rank 1).  

---

## 2.  Capacity‑Provision Game – “Who Pays for Transformer Up‑Grades?”

| Element | Description |
|--------|-------------|
| **Title** | Capacity‑Provision Game |
| **Location** | Transformer sub‑station (capacity‑upgrade planning point). |
| **Players** | 1️⃣ Farmer (potential contributor) <br>2️⃣ Sub‑station staff (capacity‑investment decision‑maker) |
| **Roles** | Farmer – potential **contributor** to the physical upgrade (pays a share of the cost). <br>Staff – **investor** who can allocate budget to increase effective transformer capacity. |
| **Actions** | **Farmer:** ① *Contribute* (C) ② *Do not contribute* (N) <br>**Staff:** ① *Invest* in upgrade (I) ② *Do not invest* (NI) |
| **Control Rules** | – If **C + I** → upgrade proceeds; all connected users enjoy higher reliability; farmer bears private cost. <br>– If **C + NI** → farmer pays but receives no benefit (failed upgrade). <br>– If **N + I** → staff pays full upgrade cost; farmer free‑rides on the improved service. <br>– If **N + NI** → no upgrade, status‑quo reliability. |
| **Information** | • Farmer sees **staff’s past willingness** to invest (historical frequency). <br>• Staff sees **farmers’ willingness to pay** (surveyed willingness‑to‑pay). Both have **partial** information; no perfect knowledge of the other’s move. |
| **Outcomes** | • Effective transformer capacity (high/low) <br>• Farmer’s out‑of‑pocket contribution (yes/no) <br>• Staff’s budget expenditure (yes/no) |
| **Payoffs** | See matrix below (ordinal). |
| **Strategic Tension** | **Strategic** – a **Public‑Goods / Free‑Rider game**.  The upgraded capacity is a non‑excludable benefit; the farmer faces a classic contribution dilemma, while the staff faces a budgeting dilemma. |
| **Temporal Structure** | Simultaneous choice once per **annual cycle** (the “investment year”). |
| **Relevant Rules** | • **Boundary rule:** Only farmers linked to the transformer are eligible contributors. <br>• **Choice rule:** Farmer can pledge a contribution; staff can allocate budget. <br>• **Control rule:** Upgrade occurs only if *both* contributions and investment are present. |

### Payoff Matrix

|                | **Invest (I)** | **No‑Invest (NI)** |
|----------------|----------------|--------------------|
| **Contribute (C)** | (3, 2)         | (0, 3)             |
| **Not Contribute (N)** | (2, 1)         | (1, 2)             |

*Interpretation* –  
Farmer’s top rank (3) is when he contributes **and** staff invests (shared benefit). The worst rank (0) is when he contributes but staff does not (wasted money). Staff’s best rank (3) is when the farmer contributes but staff does not have to spend (free‑rider).  

---

## 3.  Collusion‑Exchange Game – “Trust & Reciprocal Favors”

| Element | Description |
|--------|-------------|
| **Title** | Collusion‑Exchange Game |
| **Location** | Local sub‑station office (informal negotiation point) and farmer’s field (where the informal favor is delivered). |
| **Players** | 1️⃣ Farmer (offers informal favor / bribe) <br>2️⃣ Sub‑station staff (decides to accept & reciprocate or to enforce). |
| **Roles** | Farmer – **informal benefactor** (offers a favor, e.g., cash, labour). <br>Staff – **gatekeeper** (can accept the favor and grant informal tolerance, or enforce the rules). |
| **Actions** | **Farmer:** ① *Offer favor* (F) ② *Do not offer* (N) <br>**Staff:** ① *Accept / reciprocate* (A) ② *Enforce* (E) |
| **Control Rules** | – **F + A:** Staff tolerates informal connection and may give a small discount; farmer receives the benefit of cheaper electricity. <br>– **F + E:** Staff detects the bribe, imposes a penalty; farmer loses the bribe and may be fined. <br>– **N + A:** Staff extends informal tolerance without any bribe (costly for staff). <br>– **N + E:** No informal exchange; status‑quo enforcement. |
| **Information** | • Farmer knows the **local detection probability** (based on recent inspections). <br>• Staff knows the **farmer’s ability to pay** and the **expected informal benefit** (e.g., future favors). Information is **partial** and may be mis‑estimated. |
| **Outcomes** | • Informal electricity tolerance (yes/no) <br>• Penalty/fine (yes/no) <br>• Transfer of informal benefit (cash/ labour) |
| **Payoffs** | Ordinal matrix below. |
| **Strategic Tension** | **Strategic** – a **Trust / Exchange game**.  Mutual cooperation yields high payoffs for both; unilateral offering is punished; unilateral acceptance without a bribe is costly for staff. |
| **Temporal Structure** | One‑shot each **annual cycle** (simultaneous). |
| **Relevant Rules** | • **Boundary rule:** Only farmers who already have a connection (formal or informal) can engage. <br>• **Choice rule:** Farmer may decide to extend a favor; staff may decide to accept or enforce. <br>• **Control rule:** Acceptance leads to informal tolerance; enforcement leads to penalties. |

### Payoff Matrix

|                | **Accept (A)** | **Enforce (E)** |
|----------------|----------------|-----------------|
| **Offer (F)**  | (3, 3)         | (0, 2)          |
| **No Offer (N)** | (2, 0)         | (1, 1)          |

*Interpretation* –  
Both cooperating (F + A) gives the highest rank (3) to each. Offering a bribe that is rejected (F + E) gives the farmer the worst rank (0) and a low rank (2) to staff (who still incurs detection cost). Staff accepting without a bribe (N + A) gives staff the worst rank (0) because he bears the cost of tolerance for free.  

---

## 4.  DSM Coordination Game – “Capacitor Adoption among Neighbours”

| Element | Description |
|--------|-------------|
| **Title** | DSM Coordination (Capacitor) Game |
| **Location** | Transformer service area (farmers share the same voltage‑stability zone). |
| **Players** | Two **neighboring farmers** (any pair sharing a transformer). |
| **Roles** | Each farmer is a **technology adopter** who can invest in a voltage‑stabilizing capacitor. |
| **Actions** | **Adopt capacitor** (A) or **Do not adopt** (N) |
| **Control Rules** | – If **both adopt (A + A)** → collective voltage improvement; each farmer enjoys higher pump efficiency and lower electricity losses. <br>– If **only one adopts (A + N)** → adopter bears cost but receives little or no voltage benefit (the neighbour’s load still drags voltage down). <br>– If **both do not adopt (N + N)** → no cost, but voltage remains low (moderate reliability). |
| **Information** | Farmers observe **visible adoption** of neighbours (binary) and the **experienced voltage quality** on their own pump. Information is **partial** – they cannot perfectly attribute voltage changes to the capacitor. |
| **Outcomes** | • Adoption cost paid (yes/no) <br>• Change in voltage quality (high/low) <br>• Pump efficiency gain (yes/no) |
| **Payoffs** | Ordinal matrix below. |
| **Strategic Tension** | **Strategic** – an **Assurance / Coordination game**.  Adoption is valuable only if enough neighbours also adopt; otherwise it is a sunk cost. |
| **Temporal Structure** | Repeated **annually** (farmers can re‑consider each irrigation year). |
| **Relevant Rules** | • **Boundary rule:** Only farmers attached to the same transformer are paired. <br>• **Choice rule:** Each farmer decides each year whether to invest in a capacitor. <br>• **Control rule:** Benefits materialise only when a **threshold** of adopters on the transformer is reached (here simplified to the pair). |

### Payoff Matrix

|                | **Adopt (A)** | **Not Adopt (N)** |
|----------------|---------------|-------------------|
| **Adopt (A)**  | (3, 3)        | (0, 0)            |
| **Not Adopt (N)** | (0, 0)        | (2, 2)            |

*Interpretation* –  
Both adopting yields the highest rank (3) for each because the shared voltage improvement offsets the cost. Both refusing yields a moderate rank (2) – no cost but also no improvement. Unilateral adoption is the worst (0) for both because the adopter pays cost without benefit and the non‑adopter suffers the same low voltage.  

---

## 5.  Groundwater Extraction Game – “Common‑Pool Use of the Aquifer”

| Element | Description |
|--------|-------------|
| **Title** | Groundwater Extraction (Common‑Pool) Game |
| **Location** | District‑level groundwater basin (shared by all farmers attached to the transformer). |
| **Players** | Two **farmers** drawing from the same aquifer. |
| **Roles** | Each farmer is a **water extractor** whose pumping level influences the aquifer depth. |
| **Actions** | **High extraction** (H) – pump at maximum irrigation demand. <br>**Restrict extraction** (R) – limit pumping to a sustainable level. |
| **Control Rules** | – **H + H:** Immediate high yields but accelerates aquifer draw‑down → future pumping costs rise; both receive a low current payoff (depletion penalty). <br>– **H + R:** High extractor enjoys a large short‑term gain; the restrainer suffers reduced water availability (low payoff). <br>– **R + R:** Sustainable extraction; both receive a moderate, stable payoff. |
| **Information** | Farmers know the **current groundwater depth** (measured locally) and have a noisy belief about the neighbour’s extraction level (inferred from pump noise, water table observations). Information is **partial**. |
| **Outcomes** | • Aquifer depth change (increase/decrease) <br>• Pumping cost (higher when depth is larger) <br>• Crop yield (high if water is abundant). |
| **Payoffs** | Ordinal matrix below. |
| **Strategic Tension** | **Strategic** – a **Common‑Pool Resource (CPR) game** (tragedy‑of‑the‑commons style).  Individual incentive to extract high conflicts with collective sustainability. |
| **Temporal Structure** | Simultaneous choice each **annual irrigation cycle**; the state of the aquifer carries over to the next year (dynamic CPR). |
| **Relevant Rules** | • **Boundary rule:** All farmers linked to the same transformer share the same aquifer. <br>• **Choice rule:** Each farmer selects a pumping intensity each year. <br>• **Control rule:** Aquifer draw‑down is computed from the sum of extractions; deeper water raises future extraction cost. |

### Payoff Matrix

|                | **High (H)** | **Restrict (R)** |
|----------------|--------------|------------------|
| **High (H)**   | (1, 1)       | (3, 0)           |
| **Restrict (R)** | (0, 3)       | (2, 2)           |

*Interpretation* –  
Both extracting heavily gives each a low rank (1) because of rapid depletion. One extracts high while the other restrains gives the extractor the top rank (3) and the restrainer the worst (0). Mutual restraint yields a moderate rank (2) for both – a sustainable outcome.  

---

## 6.  Social‑Learning Process – “Observation & Imitation of Technology Outcomes”

| Element | Description |
|--------|-------------|
| **Title** | Social‑Learning Process (Non‑Strategic) |
| **Location** | Village‑level (farmer’s field) – observation of neighbours’ equipment performance and outcomes. |
| **Players** | Individual **farmers** (the only active “players”; the process is sequential, not simultaneous). |
| **Roles** | Farmer as **observer** and **potential imitator**. |
| **Actions** | ① *Observe* neighbours’ capacitor adoption outcomes (success / failure). <br>② *Imitate* with probability **p** if the observed outcome is successful **and** the farmer’s own learning‑constraint **ι** is satisfied; otherwise *remain* with current technology. |
| **Control Rules** | – Observation occurs **after** the annual harvest (end of cycle). <br>– If a farmer observes **≥ k** successful adopters on the same transformer, the farmer enters the **imitation pool** with probability **p**. <br>– Adoption cost is paid only once; if the farmer fails to coordinate, the cost is sunk. |
| **Information** | Farmers perfectly see **visible adoption** (binary) of neighbours; they receive a **noisy perception** of the resulting voltage improvement (may mis‑attribute). |
| **Outcomes** | – Change in the farmer’s **technology state** (adopted / not adopted). <br>– Updated **memory** of past successes/failures. |
| **Payoffs** | Not modelled as a strategic payoff; the process updates the **state variables** used in later strategic games (e.g., the DSM Coordination game). |
| **Strategic Tension** | **Non‑strategic** – a sequential learning process; no simultaneous decision‑making. |
| **Temporal Structure** | Occurs **once per year** after harvest, before the next decision cycle. |
| **Relevant Rules** | • **Boundary rule:** Learning is limited to farmers sharing the same transformer. <br>• **Choice rule:** Imitation is probabilistic, conditioned on observed success and the learning‑constraint parameter **ι**. <br>• **Control rule:** Adoption cost is incurred only on the first successful imitation. |

---

# Comparative Analysis of the Strategic Core

| Game | Core Type | Primary Public Good / Resource | Main Dilemma | Symmetry of Payoffs |
|------|-----------|--------------------------------|--------------|---------------------|
| **1. Authorization** | Asymmetric **Public‑Goods** (formal access) | Legal electricity connection | Farmer wants formal access; staff weighs effort vs. free‑riding | Asymmetric (farmer’s best ≠ staff’s best) |
| **2. Capacity‑Provision** | Symmetric **Public‑Goods / Free‑Rider** | Up‑graded transformer capacity | Both want the upgrade but prefer the other to pay | Asymmetric (different best outcomes) |
| **3. Collusion‑Exchange** | **Trust / Exchange** (reciprocal bribe) | Informal tolerance & informal benefit | Mutual cooperation vs. unilateral exploitation | Symmetric (both highest when cooperate) |
| **4. DSM Coordination** | **Assurance / Coordination** (capacitor) | Voltage‑stability improvement | Adoption only worthwhile if enough neighbours adopt | Symmetric (both best when both adopt) |
| **5. Groundwater Extraction** | **Common‑Pool Resource** | Aquifer water | Short‑term high extraction vs. long‑term sustainability | Asymmetric (high extractor gets top rank, restrainer gets worst) |
| **6. Social‑Learning** | Non‑strategic sequential process | Diffusion of technology | No strategic conflict; learning contingent on observed success | N/A |

### Distinctiveness Check
* Each game involves a **different combination** of players, resources, and payoff logic:
  * **Authorization** pits a farmer’s request against staff’s discretionary effort (asymmetric public‑good).
  * **Capacity‑Provision** adds a **budget‑allocation** dimension for the staff and a **contribution** decision for the farmer (free‑rider public good).
  * **Collusion‑Exchange** captures **trust** and **reciprocal informal benefits** (both parties must act).
  * **DSM Coordination** is a **pure coordination/assurance** problem among *peers* only (no staff involvement).
  * **Groundwater Extraction** is a **common‑pool** dilemma with dynamic environmental feedback.
  * **Social‑Learning** is a **non‑strategic** observation‑imitation loop that feeds the other games.

Because each strategic situation maps onto a **different canonical game** (public‑good, trust, coordination, CPR) and involves **different institutional linkages**, the set satisfies the requirement for strategic diversity.

### Revision for Diversity (if needed)
The **Capacity‑Provision** game and the **Authorization** game both involve a farmer‑staff pair and a public‑good. To sharpen their distinction, the **Capacity‑Provision** game has been defined **around budget investment** (staff bears a monetary cost) while the **Authorization** game centers on **administrative effort** (record‑keeping, regulatory compliance) with no direct monetary outlay for staff. Their payoff matrices therefore reflect different cost structures and different “best‑for‑other” outcomes, preserving strategic diversity.

---

## Summary of Extracted Action Situations

| # | Title | Players | Type of Game / Process |
|---|-------|---------|------------------------|
| 1 | Authorization Game | Farmer ↔ Staff | Asymmetric Public‑Good (formal connection) |
| 2 | Capacity‑Provision Game | Farmer ↔ Staff | Symmetric Public‑Good / Free‑Rider (transformer upgrade) |
| 3 | Collusion‑Exchange Game | Farmer ↔ Staff | Trust / Exchange |
| 4 | DSM Coordination Game | Farmer ↔ Farmer (neighbors) | Assurance / Coordination (capacitor adoption) |
| 5 | Groundwater Extraction Game | Farmer ↔ Farmer (same basin) | Common‑Pool Resource (aquifer) |
| 6 | Social‑Learning Process | Farmer (individual) | Non‑strategic observation‑imitation |

These six action situations capture **all distinct governance interactions** described in the ODD + D specification for the Andhra‑Pradesh irrigation‑electricity model.
# Run 29 — openai/gpt-oss-120b

**Electricity‑Irrigation Governance – Action‑Situation Catalogue (IAD‑style)**  
Below are **six distinct action situations** that together reproduce every governance interaction described in the ODD + D narrative.  
Strategic situations are presented as 2 × 2 normal‑form games with **ordinal pay‑offs 0–3** (3 = most preferred, 0 = least preferred).  
Non‑strategic situations are shown as sequential processes (no payoff matrix).  

---

## 1.  DSM‑Coordination (Capacitor Adoption)  

| Element | Description |
|---|---|
| **Title** | **Capacitor‑Coordination Game** |
| **Location** | Transformer service area (village‑level) |
| **Players** | Two representative **farmers** that share the same transformer |
| **Roles** | Electricity consumer – “potential adopter” |
| **Actions** | **Adopt** a capacitor (invest)  ↔  **Not‑Adopt** (stay with status‑quo) |
| **Control Rules** | If both adopt, the voltage‑stability gain is realised for the whole transformer; if only one adopts the cost is borne alone and the reliability gain is weak. |
| **Information** | Each farmer sees whether the neighbour adopted in the previous cycle (perfect observation of the neighbour’s action) but does **not** know the neighbour’s private cost. |
| **Outcomes** | – Grid voltage quality (high / low)  <br> – Individual investment cost (paid / not paid) |
| **Payoffs** | Ordinal ranks (Farmer A, Farmer B) – see matrix below. |
| **Strategic Tension** | **Strategic – Coordination/Assurance game**. Both would like to adopt, but unilateral adoption is costly. |
| **Temporal Structure** | Repeated **annually** (same pair may be re‑matched each year). |
| **Relevant Rules** | *Boundary*: farmers linked by the same transformer.<br>*Position*: each decides simultaneously.<br>*Choice*: Adopt / Not‑Adopt.<br>*Control*: payoff depends on joint action. |

### Normal‑form payoff matrix  

|                | **B Adopt** | **B Not‑Adopt** |
|----------------|------------|-----------------|
| **A Adopt**    | (3, 3)     | (0, 2)          |
| **A Not‑Adopt**| (2, 0)     | (2, 2)          |

*Explanation* – (3,3) is the jointly best outcome (high reliability, shared benefit). (0,2) reflects the adopter’s sunk cost with little benefit; the non‑adopter enjoys a modest reliability boost (2). (2,2) is the baseline when nobody invests.

---

## 2.  Authorization Game  

| Element | Description |
|---|---|
| **Title** | **Formal‑Authorization Interaction** |
| **Location** | Sub‑station office (record‑keeping desk) |
| **Players** | **Farmer** (seeking connection) ↔ **Sub‑station staff** (authorizer) |
| **Roles** | Farmer = consumer‑seeker; Staff = service‑provider/enforcer |
| **Actions** | Farmer: **Apply** for a legal connection ↔ **Stay Informal**.<br>Staff: **Grant** authorization ↔ **Deny** (keep status‑quo). |
| **Control Rules** | Granting creates a formal record and allows the farmer to receive reliable service (if capacity exists). Denial leaves the farmer with informal access (cheaper but risky). |
| **Information** | Farmer knows the fee and expected reliability if granted (partial). Staff knows the oversight intensity and potential informal benefit (partial). |
| **Outcomes** | – Legal status of the farmer’s connection.<br>– Immediate cost (fee) or risk of penalty. |
| **Payoffs** | Ordinal ranks (Farmer, Staff) – see matrix. |
| **Strategic Tension** | **Strategic – Authorization (mixed‑motivation) game**. The farmer wants the grant; the staff balances effort, formal compliance, and informal gain. |
| **Temporal Structure** | One‑shot each **annual decision round** (re‑negotiated each year). |
| **Relevant Rules** | *Boundary*: all farmers needing a new connection. <br>*Position*: simultaneous decision. <br>*Choice*: Apply/Stay ↔ Grant/Deny. <br>*Control*: payoff depends on joint outcome. |

### Normal‑form payoff matrix  

|                | **Staff Grant** | **Staff Deny** |
|----------------|----------------|----------------|
| **Farmer Apply**   | (3, 2)         | (0, 2)         |
| **Farmer Stay Informal** | (2, 3)         | (1, 2)         |

*Explanation* – (3,2): farmer gets reliable service, staff incurs modest effort (2). (0,2): farmer wastes effort, staff stays neutral. (2,3): informal cooperation gives staff a larger informal benefit (3) while farmer still gets cheap electricity (2). (1,2): informal stay without staff cooperation yields a low‑rank for the farmer (risk of penalty).

---

## 3.  Enforcement ↔ Evasion Game  

| Element | Description |
|---|---|
| **Title** | **Enforcement‑Evasion Interaction** |
| **Location** | Sub‑station field‑monitoring area (inspection zone) |
| **Players** | **Sub‑station staff** ↔ **Farmer** (connected or informal) |
| **Roles** | Staff = enforcer; Farmer = complier/evader |
| **Actions** | Staff: **High Enforcement** (intensive inspections) ↔ **Low Enforcement** (relaxed).<br>Farmer: **Comply** (pay formal fee, keep authorised) ↔ **Evade** (remain informal, risk penalty). |
| **Control Rules** | High enforcement raises detection probability and incurs effort cost; low enforcement saves effort but raises risk of future overload. |
| **Information** | Staff knows current oversight intensity (its own choice) and rough evasion prevalence (noisy).<br>Farmer knows enforcement level only imperfectly (observes occasional inspections). |
| **Outcomes** | – Payment of authorization fee (or not).<br>– Inspection cost for staff.<br>– Possible penalty for evader. |
| **Payoffs** | Ordinal ranks (Farmer, Staff) – see matrix. |
| **Strategic Tension** | **Strategic – Enforcement/Compliance (asymmetric) game**. Staff prefers low effort if evasion is low; farmer prefers evasion when enforcement is weak. |
| **Temporal Structure** | Repeated **annually** (same pair may be re‑matched each year). |
| **Relevant Rules** | *Boundary*: all farmers with a connection decision and the staff responsible for the transformer.<br>*Position*: simultaneous choice.<br>*Choice*: High/Low ↔ Comply/Evade.<br>*Control*: payoff depends on joint action. |

### Normal‑form payoff matrix  

|                | **Staff High Enf** | **Staff Low Enf** |
|----------------|-------------------|-------------------|
| **Farmer Comply** | (2, 2)            | (2, 3)            |
| **Farmer Evade**  | (0, 3)            | (3, 0)            |

*Explanation* – (2,2): compliance under high enforcement yields moderate farmer payoff (fee paid) and staff payoff (effort cost). (2,3): low enforcement with compliance is best for staff (no effort) and still acceptable for farmer. (0,3): high enforcement catches evader – farmer penalised (0), staff gains a compliance “win” (3). (3,0): low enforcement lets evader avoid fee (farmer’s best) but staff suffers (0) because future overload risk rises.

---

## 4.  Collusion‑Exchange (Trust) Game  

| Element | Description |
|---|---|
| **Title** | **Informal‑Collusion Exchange** |
| **Location** | Local transformer yard (informal “meeting point”) |
| **Players** | **Farmer** ↔ **Sub‑station staff** (same dyad as in the matching process) |
| **Roles** | Farmer = bribe‑giver; Staff = bribe‑receiver/tolerator |
| **Actions** | Farmer: **Offer** informal payment ↔ **No‑Offer**.<br>Staff: **Tolerate** (accept) ↔ **Reject** (enforce). |
| **Control Rules** | An accepted offer yields cheap electricity for the farmer and informal benefit for the staff; a rejected offer leaves the farmer with standard price and staff with reputation gain. |
| **Information** | Both know the other’s last‑round behaviour (perfect recall of the dyad) but not the exact payoff of the alternative action. |
| **Outcomes** | – Transaction (or not).<br>– Change in perceived reliability (minor). |
| **Payoffs** | Ordinal ranks (Farmer, Staff) – see matrix. |
| **Strategic Tension** | **Strategic – Trust/Reciprocity game**. Mutual cooperation is best for both; unilateral cooperation is punished. |
| **Temporal Structure** | Repeated **annually** (dyadic ties can persist). |
| **Relevant Rules** | *Boundary*: all farmer–staff pairs that have a history of interaction.<br>*Position*: simultaneous.<br>*Choice*: Offer/No‑Offer ↔ Tolerate/Reject.<br>*Control*: payoff depends on joint action. |

### Normal‑form payoff matrix  

|                | **Staff Tolerate** | **Staff Reject** |
|----------------|-------------------|-------------------|
| **Farmer Offer**   | (3, 3)            | (0, 2)            |
| **Farmer No‑Offer**| (2, 0)            | (2, 2)            |

*Explanation* – Mutual cooperation (3,3) gives the farmer cheap power and the staff an informal gain. If the farmer offers but staff rejects, the farmer is penalised (0) while staff avoids risk (2). If the staff tolerates without an offer, staff wastes tolerance (0) and farmer just gets the normal price (2). The status‑quo (2,2) is the fallback.

---

## 5.  Groundwater‑Extraction (Common‑Pool) Game  

| Element | Description |
|---|---|
| **Title** | **Groundwater Extraction Game** |
| **Location** | Shared aquifer basin (district level) |
| **Players** | Two neighbouring **farmers** drawing from the same aquifer |
| **Roles** | Water‑extractor (producer) |
| **Actions** | **Restrict** extraction (low volume) ↔ **Extract** high volume |
| **Control Rules** | Aquifer depth rises when total extraction exceeds recharge; deeper water raises pumping cost and electricity demand. |
| **Information** | Each farmer observes the current water table (noisy) and the neighbour’s last extraction level (imperfect). |
| **Outcomes** | – Individual crop yield (high if extract, low if restrict).<br>– Future pumping cost (higher if both extract). |
| **Payoffs** | Ordinal ranks (Farmer A, Farmer B) – see matrix. |
| **Strategic Tension** | **Strategic – Common‑Pool Resource (tragedy of the commons) game**. Mutual restraint is socially optimal; unilateral over‑extraction yields short‑term gain but harms the other. |
| **Temporal Structure** | Repeated **annually** (same pair may interact each irrigation cycle). |
| **Relevant Rules** | *Boundary*: farmers sharing the same aquifer cell.<br>*Position*: simultaneous.<br>*Choice*: Restrict / Extract.<br>*Control*: payoff depends on joint extraction level. |

### Normal‑form payoff matrix  

|                | **B Restrict** | **B Extract** |
|----------------|----------------|---------------|
| **A Restrict**   | (3, 3)         | (0, 3)        |
| **A Extract**    | (3, 0)         | (1, 1)        |

*Explanation* – (3,3) is the sustainable outcome (both restrain). If one extracts while the other restrains, the extractor gets the high yield (3) and the restrainer suffers (0). When both extract, the aquifer is stressed; both receive a low rank (1).

---

## 6.  Social‑Learning & Imitation (Non‑Strategic)  

| Element | Description |
|---|---|
| **Title** | **Social‑Learning / Imitation Process** |
| **Location** | Farmer’s observation zone (transformer neighbourhood) |
| **Players** | **Farmers** (as a population) – no strategic opponent |
| **Roles** | Learner / observer |
| **Actions** | **Observe** neighbours’ technology outcomes (capacitor adoption, pump quality). <br>**Imitate** with probability *p* if a neighbour’s outcome is perceived successful. |
| **Control Rules** | After each annual cycle the model draws a random subset of “experimenters” who try a new technology; successful outcomes raise the *imitation probability* for all farmers on that transformer. |
| **Information** | Perfect observation of visible adoption (who has a capacitor) but noisy attribution of why performance changed (partial). |
| **Outcomes** | – Change in the number of adopters on the transformer.<br>– Updated belief vectors for each farmer. |
| **Payoffs** | Not modelled as a payoff matrix; learning influences later strategic decisions (higher probability of choosing “Adopt” in Game 1). |
| **Strategic Tension** | **Non‑strategic** – there is no simultaneous decision; it is a sequential observation‑then‑update process. |
| **Temporal Structure** | Occurs **once per year** after the harvest, before the next decision round. |
| **Relevant Rules** | *Boundary*: all farmers linked to the same transformer.<br>*Position*: sequential (observe → update → next decision round).<br>*Choice*: adopt later or not, based on updated belief. |

---

# Strategic‑Core Analysis  

| # | Game | Core Type | Why |
|---|------|-----------|-----|
| 1 | Capacitor‑Coordination | **Assurance / Coordination** | Both prefer adoption, but unilateral adoption is costly (0). |
| 2 | Authorization | **Asymmetric Mixed‑Motivation** (similar to a “trust‑authorization” game) | Farmer wants grant; staff balances effort vs informal gain. |
| 3 | Enforcement‑Evasion | **Asymmetric Prisoner’s‑Dilemma‑like** (staff prefers low enforcement, farmer prefers evasion when enforcement is low) | Mutual best is (Low Enf, Comply) but each has incentive to deviate. |
| 4 | Collusion‑Exchange | **Trust / Reciprocity (Stag‑Hunt)** | Mutual cooperation yields (3,3); unilateral cooperation is punished. |
| 5 | Groundwater Extraction | **Common‑Pool (Tragedy of the Commons)** | Mutual restraint is socially optimal; unilateral extraction dominates locally. |
| 6 | Social‑Learning | **Non‑strategic sequential process** | No simultaneous move; learning updates future preferences. |

### Comparisons & Distinctiveness  

| Pair | Overlap? | Reason for Distinctness |
|------|----------|--------------------------|
| 1 vs 4 | Both involve farmer‑farmer (or farmer‑staff) cooperation, but 1 is **technology coordination** with a public‑good (voltage stability) that is *jointly* created, while 4 is **informal exchange** where the benefit is a private bribe. |
| 2 vs 3 | Both involve staff‑farmer interaction, yet 2 is about **granting a formal right** (binary decision) whereas 3 is about **monitoring intensity vs compliance** – a classic enforcement‑evasion dilemma with different payoff asymmetry. |
| 3 vs 4 | 3 concerns **institutional enforcement** (high/low monitoring) while 4 is **voluntary reciprocity**; the former is driven by oversight risk, the latter by trust. |
| 5 vs 1 | 5 is a **common‑pool resource** (groundwater) with negative externalities, while 1 is a **positive‑externality coordination** (voltage improvement). |
| 6 is non‑strategic, providing the learning backbone for Games 1, 2, 3, 4 and 5. |

### Ensuring Strategic Diversity  

Initially Games 2 (Authorization) and 3 (Capacity Provision) were both “public‑good contribution” games with similar payoff asymmetry. To guarantee diversity we **replaced the Capacity‑Provision game** with the **Enforcement‑Evasion** game (Game 3). This introduces a new asymmetric dilemma where the staff’s dominant strategy (low effort) conflicts with the farmer’s desire to evade, a pattern not present in the other four strategic interactions.

---

## Final Set of Action Situations (All Compliant with ODD + D)

1. **Capacitor‑Coordination Game** – coordination/assurance between neighbouring farmers.  
2. **Formal‑Authorization Interaction** – farmer’s application vs staff’s grant decision.  
3. **Enforcement‑Evasion Interaction** – staff’s inspection level vs farmer’s compliance choice.  
4. **Informal‑Collusion Exchange** – trust‑based bribe offer/acceptance.  
5. **Groundwater Extraction Game** – common‑pool extraction decisions.  
6. **Social‑Learning & Imitation Process** – non‑strategic observation‑then‑update routine.

These six capture **all governance interactions** described in the ODD + D narrative while respecting the requirement that each action situation be a distinct strategic (or sequential) unit.
# Run 11 — Qwen/Qwen3.7-Plus

**1. DSM Coordination Game (Capacitor Adoption)**

*   **Title:** DSM Coordination Game (Capacitor Adoption)
*   **Location:** Transformer group level (village level).
*   **Players:** Farmers connected to the same transformer (modeled as two representative farmers for the 2x2 game).
*   **Roles:** Electricity consumers, potential DSM investors.
*   **Actions:** Invest in DSM (capacitors) or Do not invest.
*   **Control Rules:** Investment yields shared voltage quality benefits only if a threshold of farmers on the transformer invest simultaneously. Otherwise, the investor bears the private cost with no return.
*   **Information:** Partial and noisy. Farmers observe visible peer adoption but misinterpret technical effects. Bounded knowledge of coordination requirements.
*   **Outcomes:** Shared grid reliability improvement (if threshold met) or private financial loss (if threshold not met).
*   **Payoffs:** Economic gains from reliable electricity vs. financial costs of capacitor adoption.
*   **Strategic Tension:** **Strategic.** DSM Coordination Game (Assurance/Threshold Public Goods). Tension between the private cost of investment and the need for collective assurance to realize benefits. Free-riding is mitigated by the threshold requirement, creating a coordination dilemma.
*   **Temporal Structure:** Repeated annually (once per year decision cycle).
*   **Relevant Rules:** Boundary rules (shared transformer), choice rules (invest/not), control rules (threshold requirement for benefit realization).

**Normal Form Game:**
*   **Players:** Farmer A (Row), Farmer B (Column)
*   **Actions:** {Invest, Not Invest}

| Farmer A \ Farmer B | Invest | Not Invest |
| :--- | :---: | :---: |
| **Invest** | (3, 3) | (0, 1) |
| **Not Invest** | (1, 0) | (1, 1) |

*   **Payoff Explanation:** (3,3) Both pay the cost but achieve high grid reliability. (0,1) Farmer A pays the cost but the threshold isn't met, so no benefit; Farmer B pays nothing and gets no benefit. (1,1) Status quo; no costs incurred, no benefits realized.
*   **ODD+D Compliance:** Fully compliant. The ODD explicitly states that "a farmer who invests only realises the shared benefit if enough farmers on the same transformer land on 'invest' within the same cycle, otherwise they pay the adoption cost with no return." The matrix accurately reflects this threshold assurance dynamic.

***

**2. Collusion Exchange Game**

*   **Title:** Collusion Exchange Game
*   **Location:** Sub-station / informal network level.
*   **Players:** Farmer and Sub-station Staff.
*   **Roles:** Electricity consumer (Farmer), Enforcer/Service provider (Staff).
*   **Actions:** Offer/Accept Collusion or Refuse Collusion.
*   **Control Rules:** A collusive tie forms only with mutual consent. Staff willingness depends on corruption level and farmer's reciprocity; farmer willingness depends on financial strain. Moderated by stochastic detection risk.
*   **Information:** Partial. Staff faces uncertain detection of collusion. Farmer has bounded knowledge of staff's true corruption level.
*   **Outcomes:** Formation of an informal exchange network or maintenance of a formal/neutral relationship.
*   **Payoffs:** Staff gains informal rents but risks sanctions; Farmer gains informal benefits (e.g., avoided fees) but risks penalties.
*   **Strategic Tension:** **Strategic.** Game of Trust. Tension between the mutual benefit of informal exchange and the risk of unilateral exposure. If one engages and the other refuses, the engaging party bears the risk/cost without the reciprocal benefit.
*   **Temporal Structure:** Repeated annually (matching occurs every year).
*   **Relevant Rules:** Boundary rules (matched farmer-staff pairs), choice rules (collude/refuse), control rules (mutual consent required, detection risk).

**Normal Form Game:**
*   **Players:** Farmer (Row), Staff (Column)
*   **Actions:** {Collude, Refuse}

| Farmer \ Staff | Collude | Refuse |
| :--- | :---: | :---: |
| **Collude** | (3, 3) | (0, 2) |
| **Refuse** | (2, 0) | (1, 1) |

*   **Payoff Explanation:** (3,3) Mutual trust established; both gain from informal exchange. (0,2) Farmer risks offering a bribe but Staff refuses; Farmer gets nothing, Staff stays safe. (2,0) Staff tries to extract but Farmer refuses; Staff risks exposure without gain, Farmer maintains status quo. (1,1) Formal status quo; no extra gains or risks.
*   **ODD+D Compliance:** Fully compliant. The ODD specifies that "a collusive tie forms only when both sides are independently willing" and is "moderated by the local risk of detection." The matrix captures this mutual consent requirement and the inherent trust dilemma.

***

**3. Authorization Game**

*   **Title:** Authorization Game
*   **Location:** Sub-station / grid connection point.
*   **Players:** Disconnected Farmer and Sub-station Staff.
*   **Roles:** Prospective consumer (Farmer), Gatekeeper/Enforcer (Staff).
*   **Actions:** Farmer: {Pursue Formal Connection, Remain Informal}. Staff: {Enforce Formal Rules, Accommodate Informal Use}.
*   **Control Rules:** Farmer's choice balances authorization fees against penalty risks. Staff's choice balances effort costs of enforcement against reputational risks of inaction. Existing ties lower informal terms for farmers.
*   **Information:** Partial. Farmer knows financial strain and local collusion density. Staff knows enforcement capacity and farmer's tie status.
*   **Outcomes:** Formal authorized connection, informal unauthorized connection, or penalty/sanction.
*   **Payoffs:** Farmer pays fees or incurs penalties; Staff exerts effort or faces reputational sanctions.
*   **Strategic Tension:** **Strategic.** Authorization Game (Asymmetric Inspection Game). Tension between the farmer's desire to bypass fees and the staff's desire to minimize enforcement effort. The staff must decide whether to incur effort to catch violators, while the farmer decides whether to risk penalties.
*   **Temporal Structure:** Repeated annually.
*   **Relevant Rules:** Boundary rules (disconnected farmers, assigned staff), choice rules (formal/informal, enforce/accommodate), control rules (fee structures, penalty risks, effort costs).

**Normal Form Game:**
*   **Players:** Farmer (Row), Staff (Column)
*   **Actions:** Farmer: {Formal, Informal}; Staff: {Enforce, Accommodate}

| Farmer \ Staff | Enforce | Accommodate |
| :--- | :---: | :---: |
| **Formal** | (2, 2) | (3, 1) |
| **Informal** | (0, 3) | (1, 0) |

*   **Payoff Explanation:** (2,2) Farmer pays fee and gets service; Staff exerts effort to maintain order. (3,1) Farmer pays fee; Staff accommodates, saving effort but missing enforcement targets. (0,3) Farmer is penalized; Staff catches a violator, earning a high performance reward. (1,0) Farmer gets free electricity; Staff shirks and faces reputational sanctions.
*   **ODD+D Compliance:** Fully compliant. The ODD states that "each disconnected farmer chooses between pursuing a paid, formal connection or remaining informal" and staff "decide whether to enforce formal rules." The matrix reflects the asymmetric inspection dilemma inherent in this choice.

***

**4. Groundwater Extraction Game**

*   **Title:** Groundwater Extraction Game
*   **Location:** Village-level groundwater basin / shared aquifer.
*   **Players:** Connected farmers sharing the aquifer (modeled as two representative farmers).
*   **Roles:** Groundwater extractors, electricity consumers.
*   **Actions:** Restrain extraction or Pump at full rate.
*   **Control Rules:** Aquifer drawdown is computed every tick based on realized extraction. The energy cost of extracting a unit of water increases dynamically as aquifer stress (depletion) increases.
*   **Information:** Partial. Farmers sense local groundwater depth and pumping costs but have bounded knowledge of total aquifer state and neighbors' exact extraction.
*   **Outcomes:** Changes in aquifer table depth and pumping energy costs.
*   **Payoffs:** Economic net yield (crop value minus pumping energy costs).
*   **Strategic Tension:** **Strategic.** Common Pool Resource Game (Tragedy of the Commons). Tension between the individual short-term benefit of full extraction and the collective long-term cost of aquifer depletion (increased pumping costs).
*   **Temporal Structure:** Continuous over time (decided annually, physical drawdown computed monthly).
*   **Relevant Rules:** Boundary rules (farmers sharing the aquifer), choice rules (restrain/full pump), control rules (aquifer drawdown dynamics, increasing marginal extraction costs).

**Normal Form Game:**
*   **Players:** Farmer A (Row), Farmer B (Column)
*   **Actions:** {Restrain, Full Pump}

| Farmer A \ Farmer B | Restrain | Full Pump |
| :--- | :---: | :---: |
| **Restrain** | (2, 2) | (0, 3) |
| **Full Pump** | (3, 0) | (1, 1) |

*   **Payoff Explanation:** (2,2) Aquifer remains stable, pumping costs are moderate, both get decent yields. (0,3) Farmer A restrains (lower yield), while Farmer B pumps fully, capturing most of the water and getting a high yield. (1,1) Both pump fully; the aquifer depletes rapidly, driving up energy costs and reducing net yields for both compared to mutual restraint.
*   **ODD+D Compliance:** Fully compliant. The ODD notes that "the relative attractiveness of restraint rises as aquifer stress (the energy cost of extracting a unit of water) increases." The matrix captures this CPR dilemma where individual rationality leads to collective ecological and economic degradation.

***

**5. Social Learning Game (Observation and Imitation)**

*   **Title:** Social Learning Game (Observation and Imitation)
*   **Location:** Transformer group level / village social networks.
*   **Players:** Farmers.
*   **Roles:** Observers, potential imitators, experimenters.
*   **Actions:** Observe neighbors' outcomes, decide to experiment, imitate, or maintain current strategy.
*   **Control Rules:** A small number of "experimenters" are drawn regardless of neighborhood outcomes. Farmers on a transformer where enough simultaneous adoptions have occurred become eligible to imitate at a fixed yearly probability. The imitation pool only opens after a threshold jump in local adoption.
*   **Information:** Noisy. Farmers observe visible adoption (e.g., capacitors) but misinterpret the effects on performance due to incomplete technical understanding and biased learning from failed sequential adoption.
*   **Outcomes:** Changes in individual technology adoption states and shifts in local behavioral norms.
*   **Payoffs:** N/A (This is a non-strategic sequential process; payoffs are realized in the DSM Coordination game).
*   **Strategic Tension:** **Non-strategic.** Sequential process of observation and imitation. No direct strategic interaction or simultaneous decision dilemma; farmers update heuristics based on experiential feedback and observed peer outcomes.
*   **Temporal Structure:** Repeated annually (once per year decision cycle).
*   **Relevant Rules:** Boundary rules (social networks, transformer groups), choice rules (imitate, experiment, maintain), control rules (threshold-based opening of imitation pools, fixed yearly probability).
*   **ODD+D Compliance:** Fully compliant. The ODD explicitly describes this as a non-strategic process where "the pool of farmers considered for adoption each year combines a small number drawn as prospective 'experimenters'... with farmers... who become independently eligible to imitate at a fixed yearly probability." It is correctly modeled as a sequential learning process rather than a simultaneous strategic game.
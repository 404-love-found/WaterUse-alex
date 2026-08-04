# Run 26 — Qwen/Qwen3.7-Plus

Here are the distinct action situations extracted from the ODD+D description, structured according to the IAD framework. The final set includes five strategic games and one non-strategic sequential process, revised to ensure maximum strategic diversity.

### 1. DSM Coordination Game (Capacitor Adoption)
**Location:** Transformer group level (village-level service area).
**Players:** Two representative farmers sharing the same transformer.
**Roles:** Electricity consumers and potential technology adopters.
**Actions:** Invest in Capacitor, Do Not Invest.
**Control Rules:** Capacitors improve voltage stability, but benefits are strongly non-linear and require coordinated adoption. If both invest, voltage stabilizes and pump efficiency increases. If only one invests, the cost is borne but the local voltage improvement is negligible due to the neighbor's poor power factor.
**Information:** Partial and noisy. Farmers observe neighbors' visible adoption but may misattribute voltage drops to the wrong causes.
**Outcomes:** Changes in local voltage quality, pump efficiency, and individual budget.
**Payoffs:** Ordinal ranks reflecting crop reliability and equipment costs.
**Strategic Tension:** **Assurance Game (Coordination).** Mutual investment yields the best outcome, but unilateral investment is a "sucker's payoff." Farmers must trust that enough neighbors will also invest to make the technology effective.
**Temporal Structure:** Repeated annually (once per irrigation cycle).
**Relevant Rules:** Choice rules (invest or not), information rules (observe neighbors' visible adoption).

**Payoff Matrix:**
| Farmer A \ Farmer B | Invest (I) | Do Not Invest (N) |
| :--- | :---: | :---: |
| **Invest (I)** | 3, 3 | 0, 2 |
| **Do Not Invest (N)** | 2, 0 | 1, 1 |

### 2. Capacity Provision Game (Transformer Upgrade Contribution)
**Location:** Transformer group level.
**Players:** Two representative farmers sharing a transformer.
**Roles:** Electricity consumers and infrastructure contributors.
**Actions:** Contribute to Capacity, Free-ride (Do Not Contribute).
**Control Rules:** Upgrading transformer capacity requires financial contributions. The upgraded capacity improves reliability for all connected farmers. Contributors bear the full private cost, while non-contributors enjoy the reliability gains without paying.
**Information:** Partial. Farmers know the cost of contribution and observe who has contributed in the past.
**Outcomes:** Transformer capacity level, voltage stability, individual financial cost.
**Payoffs:** Ordinal ranks reflecting financial expenditure and grid reliability.
**Strategic Tension:** **Public Goods Game (Symmetric Prisoner’s Dilemma).** Free-riding is the dominant strategy, but mutual free-riding leads to transformer overload and burnouts, making everyone worse off.
**Temporal Structure:** Repeated annually.
**Relevant Rules:** Boundary rules (who is connected to the transformer), choice rules (contribute or not), payoff rules (costs and benefits).

**Payoff Matrix:**
| Farmer A \ Farmer B | Contribute (C) | Free-ride (F) |
| :--- | :---: | :---: |
| **Contribute (C)** | 2, 2 | 0, 3 |
| **Free-ride (F)** | 3, 0 | 1, 1 |

### 3. Authorization Game (Grid Connection and Capacity Investment)
**Location:** Sub-station and farmer field interface (Decentralized regime).
**Players:** Disconnected Farmer and Sub-station Staff.
**Roles:** Applicant for electricity connection / Service provider and allocator.
**Actions:** Farmer: Seek Formal Authorization, Bypass (Remain Informal). Staff: Invest in Capacity/Authorize, Withhold Investment.
**Control Rules:** Formal authorization requires the farmer to pay fees and the staff to invest effort. If the farmer seeks formal and staff invests, connection is granted. If the farmer seeks formal but staff withholds, the farmer pays fees but gets no connection. If the farmer bypasses and staff invests, the staff upgrades the grid but the farmer gets informal access. 
**Information:** Partial. Farmer knows staff's general reputation; staff knows farmer's financial capacity.
**Outcomes:** Connection status, grid capacity, financial costs, staff effort.
**Payoffs:** Ordinal ranks reflecting connection benefits, fees, and effort costs.
**Strategic Tension:** **Asymmetric Dominant Strategy Trap.** Both players have a dominant strategy that leads to a suboptimal equilibrium. The farmer prefers to bypass to avoid fees, and the staff prefers to withhold to avoid effort, resulting in a stagnant status quo.
**Temporal Structure:** Repeated annually.
**Relevant Rules:** Authority rules (staff has discretion over capacity), choice rules.

**Payoff Matrix:**
| Farmer \ Staff | Invest (I) | Withhold (W) |
| :--- | :---: | :---: |
| **Formal (F)** | 2, 2 | 0, 3 |
| **Bypass (B)** | 3, 0 | 1, 1 |

### 4. Collusion Exchange Game (Informal Tolerance and Favors)
**Location:** Sub-station and connected farmer field.
**Players:** Connected Farmer and Sub-station Staff.
**Roles:** Regulated consumer / Enforcer and informal broker.
**Actions:** Farmer: Offer Informal Exchange (bribe/favor), Comply Formally. Staff: Accept Informal Exchange (tolerate overload), Enforce Rules (penalize).
**Control Rules:** Informal exchange yields mutual benefit but carries detection risk. If one offers and the other enforces, the offering party is penalized. 
**Information:** Noisy. Both face uncertainty about oversight and detection risk.
**Outcomes:** Penalty avoidance, informal rents, grid stress, formal compliance.
**Payoffs:** Ordinal ranks reflecting informal rents, penalties, and effort.
**Strategic Tension:** **Stag Hunt (Trust/Coordination Game).** Mutual informal exchange is highly profitable but risky. Mutual formal compliance is safe but costly. Players must coordinate on the payoff-dominant informal equilibrium or fall back to the risk-dominant formal one.
**Temporal Structure:** Repeated continuously (monthly/annually).
**Relevant Rules:** Choice rules, information rules (uncertainty of detection).

**Payoff Matrix:**
| Farmer \ Staff | Accept (A) | Enforce (E) |
| :--- | :---: | :---: |
| **Offer (O)** | 3, 3 | 0, 2 |
| **Comply (C)** | 2, 0 | 1, 1 |

### 5. Groundwater Extraction Game (Aquifer Depletion)
**Location:** District-level groundwater basin (shared aquifer).
**Players:** Two heterogeneous farmers sharing an aquifer (Farmer A: Shallow-well; Farmer B: Deep-well).
**Roles:** Groundwater extractors.
**Actions:** Restrain Extraction, Extract Fully.
**Control Rules:** Individual extraction yields immediate crop benefits. Aggregate extraction lowers the water table. The shallow-well farmer is highly sensitive to depletion, while the deep-well farmer can sustain extraction longer but faces higher baseline pumping costs.
**Information:** Partial. Farmers observe groundwater depth and pumping costs but may not fully attribute long-term depletion to aggregate extraction.
**Outcomes:** Crop yield, pumping costs, aquifer depth, grid load.
**Payoffs:** Ordinal ranks reflecting crop revenue and pumping energy costs.
**Strategic Tension:** **Asymmetric Common Pool Resource Game.** Both have a dominant strategy to extract, but the negative externality of depletion falls disproportionately on the shallow-well farmer, creating an asymmetric tragedy of the commons.
**Temporal Structure:** Continuous over time (monthly/annual cycles).
**Relevant Rules:** Boundary rules (who has access to the aquifer), choice rules (pumping volume).

**Payoff Matrix:**
| Farmer A (Shallow) \ Farmer B (Deep) | Restrain (R) | Extract Fully (E) |
| :--- | :---: | :---: |
| **Restrain (R)** | 2, 2 | 0, 3 |
| **Extract Fully (E)** | 3, 1 | 1, 0 |

### 6. Social Learning Game (Observation and Imitation)
**Location:** Village-level social network.
**Players:** Observer Farmer and Model Neighbor.
**Roles:** Potential imitator and observed adopter.
**Actions:** Model: (Realized state determined by nature/past choices: Successful Adoption, Unsuccessful/No Adoption). Observer: Imitate, Do Not Imitate.
**Control Rules:** The observer sees the neighbor's outcome. If the neighbor succeeded, imitation is likely to succeed. If the neighbor failed, imitation is likely to fail.
**Information:** Noisy. The observer sees the visible outcome (e.g., pump working) but may misinterpret the cause (e.g., attributing success to a capacitor when it was actually due to low aggregate load that month).
**Outcomes:** Technology adoption diffusion, individual budget, equipment performance.
**Payoffs:** Ordinal ranks based on equipment performance and cost.
**Strategic Tension:** **Non-strategic sequential process.** There is no simultaneous strategic interaction. The observer is making a sequential decision under uncertainty, reacting to the model neighbor's already-realized outcome.
**Temporal Structure:** Sequential, repeated annually.
**Relevant Rules:** Information rules (observability of neighbors), choice rules (imitation threshold).

***

### Strategic Core Analysis, Comparison, and Revision

To ensure the model captures the full complexity of the electricity-irrigation governance system, the strategic cores of the five strategic action situations were analyzed and compared:

1. **DSM Coordination Game:** Functions as an **Assurance Game**. The core tension is coordination; players want to cooperate but only if they are assured others will do the same.
2. **Capacity Provision Game:** Functions as a **Symmetric Public Goods Game (Prisoner’s Dilemma)**. The core tension is free-riding; individual rationality leads to collective ruin.
3. **Authorization Game:** Initially conceptualized as a symmetric coordination game, this was **revised** into an **Asymmetric Dominant Strategy Trap**. In a decentralized regime, the power and information asymmetries between farmers and staff mean both players have a dominant strategy to defect (Bypass/Withhold), trapping them in a suboptimal equilibrium. This provides a distinct asymmetric tension compared to the symmetric dilemmas elsewhere.
4. **Collusion Exchange Game:** Functions as a **Stag Hunt (Trust Game)**. The core tension is risk vs. reward; players must trust each other to sustain a highly profitable but risky informal equilibrium, rather than settling for a safe but costly formal one.
5. **Groundwater Extraction Game:** Initially conceptualized as a symmetric Common Pool Resource game, this was **revised** into an **Asymmetric CPR Game**. By introducing heterogeneous agents (shallow-well vs. deep-well farmers), the negative externalities of over-extraction are distributed unevenly. This ensures the CPR tension is distinct from the symmetric free-rider tension in the Capacity Provision game.

**Conclusion on Diversity:** 
By revising the Authorization and Groundwater Extraction games, the final set of action situations avoids overlapping strategic cores. The model now features an Assurance Game, a Symmetric PD, an Asymmetric Dominant Strategy Trap, a Stag Hunt, and an Asymmetric CPR Game. This guarantees that the ODD+D protocol captures a wide spectrum of institutional dilemmas, from coordination failures and free-riding to asymmetric power dynamics and heterogeneous resource vulnerabilities. All games strictly comply with the ODD+D description, utilizing ordinal payoffs (0-3) and reflecting the decentralized, boundedly-rational context of Andhra Pradesh's irrigation governance.
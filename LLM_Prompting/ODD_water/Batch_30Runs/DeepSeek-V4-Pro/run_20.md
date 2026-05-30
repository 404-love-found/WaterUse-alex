# Run 20 — deepseek-ai/DeepSeek-V4-Pro

**Analysis of Distinct Action Situations in the Decentralised Version (DV)**  
*Only farmer decisions under DV are considered; centralised governance (CV) is excluded.*

---

### Action Situation 1: Water Appropriation along the River
**Tension:**  
Upstream farmers have priority access to river water. Their extraction directly reduces the water available for downstream farmers, creating an asymmetric commons dilemma. Upstream has a dominant strategy to irrigate heavily, forcing downstream to bear the costs of scarcity.

**2-Player Normal Form Payoff Matrix**  
Players: Upstream Farmer (U) vs Downstream Farmer (D)  
Actions: Irrigate High (H = 8 fields) or Low (L = 4 fields)  
Payoffs: Net agricultural return (revenue – costs), assuming inflow = 10, demand = 1 unit/field, revenue = 10/field fully irrigated, cost = 5/field. Water is withdrawn sequentially; U takes first.

| U \ D | High (8 fields) | Low (4 fields) |
|--------|-----------------|----------------|
| **High (8)** | (40, –20) | (40, 0) |
| **Low (4)**  | (20, 20) | (20, 20) |

*Payoffs are (U, D).*

**Justification:**  
In the model, water flows from upstream to downstream. U’s extraction is always satisfied first, so U’s payoff depends only on its own choice and the inflow. D receives the residual. If U plays High, D’s water is drastically reduced, making Low irrigation the only viable response (0 > –20). If U plays Low, D can safely play High or Low (20 either way). U’s dominant strategy is High (40 > 20). The Nash equilibrium (High, Low) gives U a large advantage while D barely breaks even. This spatial asymmetry drives over-extraction by upstream farmers and water stress for downstream farmers, a core tension in the model.

---

### Action Situation 2: Fish Stock Sustainability in the Lake
**Tension:**  
Downstream farmers have priority access to the fishing lake. Fish recruitment depends on a threshold volume of river inflow into the lake. Because downstream farmers fish first, they are guaranteed a catch even when the stock is depleted, giving them no incentive to conserve water for the fishery. This creates an asymmetric dilemma where the upstream farmer’s fish catch is entirely dependent on downstream’s willingness to limit irrigation—which downstream has no reason to do.

**2-Player Normal Form Payoff Matrix**  
Players: Upstream Farmer (U) vs Downstream Farmer (D)  
Actions: Irrigate High (H = 8 fields) or Low (L = 4 fields)  
Payoffs: Fish catch value only (agricultural returns set aside). Inflow = 14, threshold for fish recruitment = 4. Lake inflow = 14 – (U extraction + D extraction). If lake inflow ≥ 4, fish are abundant: both catch 10 fish (value = 20). If lake inflow < 4, fish are scarce: D catches 10 (20), U catches 0 (0) because D fishes first.

| U \ D | High (8 fields) | Low (4 fields) |
|--------|-----------------|----------------|
| **High (8)** | (0, 20) | (0, 20) |
| **Low (4)**  | (0, 20) | (20, 20) |

*Payoffs are (U, D).*

**Justification:**  
In the model, farmers access the lake in order of proximity, with downstream first. The fish population collapses unless total water extraction is low enough to maintain the May inflow threshold. D always catches the target because of first access, so D’s fish payoff is 20 regardless of the state. U only catches fish if both play Low, preserving the stock. D has no incentive to play Low (20 vs 20), so the equilibrium is any profile where D plays High—leading to U getting 0. This mirrors the real-world dynamic where those with priority access to a resource may not bear the costs of its depletion, while those later in the chain suffer the consequences.

---

### Combined Effect
The two action situations operate simultaneously in the model. The combined payoff matrix (summing agricultural and fish returns) reveals a social dilemma where mutual Low irrigation (L,L) yields the highest collective payoff, but the asymmetric incentives in water and fish access drive the system toward (High, Low) or (High, High), depleting both water and fish resources. This precisely captures the resilience challenges the model was designed to study.
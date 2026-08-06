# Run 26 — Qwen/Qwen3.7-Plus

# IAD Action Situation Analysis — Decentralised Version (DV)

---

## Thought Process

To extract the distinct action situations under the DV, I first mapped the strategic interactions available to farmers when no central authority allocates water. Three candidate tensions emerged from the model mechanics:

1. **Sequential water access along the river** → Upstream farmers withdraw first; downstream farmers receive the residual. This creates a positional power asymmetry.
2. **Lake inflow ecological threshold** → Fish larvae survival requires water inflow above a critical threshold. Cumulative irrigation extraction can push inflow below this tipping point, collapsing the fishery.
3. **Heuristic-based risk-taking** → Farmers below an income threshold expand fields recklessly. However, this is a behavioural rule, not a distinct *interaction* structure—it manifests through tension #1.

I therefore identified **two** genuinely distinct action situations, each with a unique game-theoretic structure. I parameterised payoffs using the model's constraints: max 10 fields, sequential extraction, and a lake inflow threshold.

---

## Action Situation 1: Upstream–Downstream Irrigation Competition

### Strategic Tension
**Positional Power Asymmetry in a Common-Pool Resource.**
Because water flows unidirectionally from upstream to downstream, the upstream farmer withdraws first and faces no uncertainty about water availability. The downstream farmer receives only the residual. The upstream farmer therefore has a **dominant strategy** to maximise irrigation, while the downstream farmer—anticipating this—must adapt by conserving. The tension is a structural distributional conflict: the downstream farmer is locked into a subordinate position by spatial geography, with no strategic recourse to influence the upstream farmer's extraction.

### 2-Player Normal Form Payoff Matrix

*Assumptions: Total river inflow = 15 water units. Max (10 fields) requires 10 units; Conservative (5 fields) requires 5 units. Upstream farmer (U) extracts first. Downstream farmer (D) irrigates with the residual. Yield = min(fields, water) with a stress penalty when water < fields.*

| | **Downstream: Max (10 fields)** | **Downstream: Conservative (5 fields)** |
|---|:---:|:---:|
| **Upstream: Max (10 fields)** | **(10, 3)** | **(10, 5)** |
| **Upstream: Conservative (5 fields)** | **(5, 10)** | **(5, 5)** |

*Payoffs shown as (Upstream yield, Downstream yield).*

**Derivation:**
- *(Max, Max):* U uses 10 → D gets 5. D has 10 fields but only 5 units → severe stress → D yield = 3. U yield = 10.
- *(Max, Con):* U uses 10 → D gets 5. D has 5 fields and 5 units → no stress → D yield = 5. U yield = 10.
- *(Con, Max):* U uses 5 → D gets 10. D has 10 fields and 10 units → no stress → D yield = 10. U yield = 5.
- *(Con, Con):* U uses 5 → D gets 10. D has 5 fields and 10 units → no stress → D yield = 5. U yield = 5.

**Nash Equilibrium:** **(Max, Conservative) = (10, 5)**
- U: Max strictly dominates Conservative (10 > 5 regardless of D's choice).
- D: Given U plays Max, Conservative is the best response (5 > 3).

### Justification
This matrix captures the core spatial asymmetry of the DV. The upstream farmer's payoff depends *only* on their own choice because they extract from the undiminished river inflow. The downstream farmer's payoff depends on *both* farmers' choices because D irrigates from the residual. U's dominant strategy to maximise extraction leaves D with a take-it-or-leave-it choice: adapt to scarcity (Conservative) or suffer severe water stress (Max). The equilibrium (10, 5) is highly inequitable—U captures twice D's yield—yet D cannot unilaterally improve their position. The alternative (Conservative, Max) = (5, 10) would favour D but is unreachable because U will never voluntarily conserve. This is not a classic Prisoner's Dilemma but a **Stackelberg-style positional advantage game**: the "dilemma" is D's structural entrapment.

---

## Action Situation 2: Irrigation–Fishery Ecological Threshold Dilemma

### Strategic Tension
**Coordination Failure at an Ecological Tipping Point.**
Both farmers' irrigation withdrawals reduce the water flow reaching the fishing lake. The fish population depends on a **non-linear ecological threshold**: larvae migration into the lake succeeds only if inflow exceeds a critical minimum. If cumulative extraction pushes lake inflow below this threshold, the fishery collapses entirely—eliminating fishing income for *all* farmers. The tension is a **Stag Hunt**: both farmers would prefer to jointly conserve water (maintaining the fishery), but each fears being the "sucker" who conserves while the other over-extracts. Under uncertainty, the risk-dominant equilibrium is mutual over-extraction and fishery collapse.

### 2-Player Normal Form Payoff Matrix

*Assumptions: Total river inflow = 18 water units. Lake ecological threshold = 6 units of inflow. Fishing income = 7 per farmer if fishery thrives, 0 if it collapses. Agricultural yield as in Situation 1. Water reaching lake = 18 − U's extraction − D's extraction.*

| | **Downstream: Max (10 fields)** | **Downstream: Conservative (5 fields)** |
|---|:---:|:---:|
| **Upstream: Max (10 fields)** | **(10, 6)** | **(10, 5)** |
| **Upstream: Conservative (5 fields)** | **(5, 10)** | **(12, 12)** |

*Payoffs shown as (Upstream total income, Downstream total income) = (agri yield + fishing income).*

**Derivation:**
- *(Max, Max):* U uses 10, D gets 8, D uses 8. Lake inflow = 0 < 6 → **fishery collapses**. D has 10 fields, 8 units → mild stress → agri yield = 6. Fishing = 0. U: 10+0 = 10. D: 6+0 = 6.
- *(Max, Con):* U uses 10, D gets 8, D uses 5. Lake inflow = 3 < 6 → **fishery collapses**. D: 5+0 = 5. U: 10+0 = 10.
- *(Con, Max):* U uses 5, D gets 13, D uses 10. Lake inflow = 3 < 6 → **fishery collapses**. D: 10+0 = 10. U: 5+0 = 5.
- *(Con, Con):* U uses 5, D gets 13, D uses 5. Lake inflow = 8 ≥ 6 → **fishery thrives**. D: 5+7 = 12. U: 5+7 = 12.

**Nash Equilibria:** **(Max, Max) = (10, 6)** and **(Conservative, Conservative) = (12, 12)**
- U: If D plays Max → U prefers Max (10 > 5). If D plays Conservative → U prefers Conservative (12 > 10).
- D: If U plays Max → D prefers Max (6 > 5). If U plays Conservative → D prefers Conservative (12 > 10).

**Risk-dominant equilibrium: (Max, Max)**
- U's maximin: Max guarantees min(10,10) = 10; Conservative guarantees min(5,12) = 5. → Max is safer.
- D's maximin: Max guarantees min(6,10) = 6; Conservative guarantees min(5,12) = 5. → Max is safer.

### Justification
This matrix captures the ecological threshold that distinguishes this situation from pure water competition. The fishery introduces a **lumpy public good**: it is either fully available (inflow ≥ 6) or completely collapsed (inflow < 6). This non-linearity transforms the game from a simple extraction competition into a **Stag Hunt coordination problem**. The Pareto-superior equilibrium (Conservative, Conservative) = (12, 12) requires both farmers to restrain extraction. However, the risk-dominant equilibrium is (Max, Max) = (10, 6): under uncertainty about the other farmer's behaviour, each farmer's safe strategy is to over-extract, because the loss from being the sole cooperator (5 for U, 5 for D) is worse than mutual defection (10 for U, 6 for D). Crucially, the spatial asymmetry persists here too—U's agri yield is always higher than D's in every cell because U extracts first and never faces water stress—but the *ecological threshold* adds a second layer of tension: even the upstream farmer ultimately suffers from fishery collapse (10 vs. 12), yet the fear of exploitation drives both toward the inferior equilibrium. This mirrors the model's finding that resilience depends on governance type, diversity of water use, and memory capacity—factors that shape whether farmers can coordinate on the cooperative equilibrium.
# Run 14 — openai/gpt-oss-120b

**IAD‑derived Action Situations for the Decentralised (DV) version**  
*Only farmer‑to‑farmer strategic tensions are extracted.  The spatial ordering (up‑stream ↔ down‑stream) and the ecological thresholds that can tip the fish population are explicitly built into each game.*

---

## 1.  Water‑Extraction Conflict (Up‑stream vs Down‑stream)

|                     | **Down‑stream L** (low extraction = 5 fields) | **Down‑stream H** (high extraction = 10 fields) |
|---------------------|----------------------------------------------|-----------------------------------------------|
| **Up‑stream L** (5 fields) | (4 , 5) | (3 , 2) |
| **Up‑stream H** (10 fields) | (6 , 1) | (2 , 0) |

*Payoffs = expected net monetary return (yield − irrigation cost) for the year.*

### Strategic tension  
- **“How much water should I take?”** – The upstream farmer enjoys priority in the flow; a high‑extraction choice guarantees a large yield for him but can starve the downstream neighbour.  
- The downstream farmer, lacking priority, can only secure water if the upstream farmer restrains his demand.

### Why it is a distinct DV situation  
- No national authority is involved (centralised allocation is ignored).  
- The game captures the **spatial asymmetry** (up‑stream priority) and the **resource‑scarcity** that emerges each irrigation season.

---

## 2.  Fishing‑Effort Competition (Down‑stream ↔ Up‑stream)

|                     | **Up‑stream C** (conserve = ½ × target catch) | **Up‑stream O** (over‑fish = full target) |
|---------------------|----------------------------------------------|-------------------------------------------|
| **Down‑stream C** (conserve) | (3 , 3) | (2 , 4) |
| **Down‑stream O** (over‑fish) | (5 , 1) | (2 , 1) |

*Payoffs = λ × fish‑catch value (λ is the scaling factor) minus any negligible handling cost.*

### Strategic tension  
- **“Should I take the whole allowed catch or leave some for the future?”** – The downstream farmer fishes first; if he over‑exploits, the upstream farmer receives almost nothing.  
- The upstream farmer can still over‑fish, but because he is second in line his extra effort yields only a modest gain and accelerates the depletion of the stock.

### Distinctiveness  
- This game isolates the **ecological threshold** of the fish population: repeated “O/O” outcomes push the stock toward the tipping point (very low future returns).  
- It is a pure **pairwise interaction**; the national authority does not intervene in fishing.

---

## 3.  Field‑Expansion Decision (Both Farmers)

|                     | **Down‑stream H** (hold = current number of fields)** | **Down‑stream E** (expand = +1 field) |
|---------------------|------------------------------------------------------|--------------------------------------|
| **Up‑stream H** (hold) | (4 , 4) | (3 , 6) |
| **Up‑stream E** (expand) | (7 , 2) | (5 , 0) |

*Payoffs = expected net return after the vegetation season (yield × water‑stress factor − irrigation cost).*

### Strategic tension  
- **“Should I risk adding another field?”** – Expanding raises potential income but also raises water demand.  
- Because water flows sequentially, an upstream expansion reduces the water that reaches the downstream farmer, while a downstream expansion does not affect the upstream farmer’s water receipt.

### Distinctiveness  
- The game captures **spatial asymmetry** (up‑stream expansion harms the neighbour, downstream expansion does not) and the **budget constraint** (expansion is only possible if the farmer’s budget permits).  
- It is a separate strategic dilemma from the pure extraction game because the decision is about *future* field capacity rather than the current season’s water draw.

---

## 4.  Ecological‑Threshold Maintenance (Collective Water‑Conservation)

|                     | **Down‑stream C** (conserve = ≤ threshold extraction) | **Down‑stream O** (over‑extract > threshold) |
|---------------------|------------------------------------------------------|---------------------------------------------|
| **Up‑stream C** (conserve) | (5 , 5) | (3 , 4) |
| **Up‑stream O** (over‑extract) | (4 , 3) | (1 , 1) |

*Payoffs = long‑term expected return (yield + fish income) where the fish‑recruitment term **Iₜ** (see the model) is **high** if total extraction stays below the larvae‑migration threshold, **low** otherwise.*

### Strategic tension  
- **“Do I keep my water extraction low enough to guarantee the larvae‑migration threshold?”** – If both conserve, the lake receives enough flow in May, larvae survive, and the fish stock stays productive (high payoff).  
- If either farmer over‑extracts enough to push the downstream flow below the threshold, the fish recruitment collapses, dragging both payoffs down dramatically.

### Distinctiveness  
- This game explicitly embeds the **ecological tipping point** (larvae‑migration threshold) that is not present in the pure extraction or fishing games.  
- It is a **pairwise collective‑action problem**: the outcome depends on the *sum* of both players’ actions, not on who moves first.

---

### How the matrices were built  

1. **Payoff magnitudes** are illustrative but respect the model’s logic:  
   - Up‑stream always has a water‑priority advantage, so his payoff is never lower than the downstream payoff when both choose the same extraction level.  
   - Over‑extraction or over‑fishing can raise short‑term returns but creates a risk of crossing the ecological threshold, reflected by the low (1) payoffs in the “both over‑extract” cells.  
   - The maximum number of irrigated fields is limited to **10**; the “expand” actions assume the farmer is still below that ceiling.

2. **Spatial asymmetry** is encoded by making the upstream farmer’s “high” choice more rewarding when the downstream farmer is restrained, while the downstream farmer’s “high” choice only yields a modest gain because he receives water after the upstream draw.

3. **Ecological thresholds** appear in Games 2 and 4: the “O/O” fishing cell and the “O/O” water‑conservation cell both generate dramatically lower future returns, mimicking the collapse of the fish population when water inflow falls below the larvae‑migration requirement.

These four action situations exhaust the **unique strategic tensions** that arise among farmers in the decentralised (DV) version of the water‑use model, respecting the required constraints.
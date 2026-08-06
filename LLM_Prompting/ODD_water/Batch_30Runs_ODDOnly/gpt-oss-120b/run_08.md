# Run 8 — openai/gpt-oss-120b

**IAD‑derived Decentralised (DV) Action Situations**  
*Only farmer‑to‑farmer strategic interactions are extracted.  The national authority is omitted (centralised case).  Each situation is presented as a 2‑player normal‑form game that captures a **unique strategic tension**, the **up‑stream / down‑stream spatial asymmetry**, and, where relevant, an **ecological threshold (tipping point)**.  The maximum number of irrigable fields per farm is 10, so “High‑Irrigation” means “add one field (if <10)”.  Pay‑offs are expressed in **relative utility units** (higher = better economic outcome for the season).  

---

## 1.  Water‑Extraction Competition  
**Strategic tension:** *Up‑stream farmer’s extra irrigation reduces the water that reaches the down‑stream neighbour* (a classic “up‑stream‑down‑stream” conflict).  

### Players  
- **U** – Up‑stream farmer (farmer 1)  
- **D** – Down‑stream farmer (farmer 2)  

### Strategies  
|               | **D: Low‑Irrigation** (keep current fields) | **D: High‑Irrigation** (add one field) |
|---------------|--------------------------------------------|----------------------------------------|
| **U: Low‑Irrigation** | (6 , 6) | (6 , 7) |
| **U: High‑Irrigation**| (8 , 4) | (8 , 3) |

### Pay‑off explanation  

| Outcome | Water delivered to U | Water delivered to D | Economic result |
|---------|----------------------|----------------------|-----------------|
| **U Low / D Low** | Both receive the “baseline” flow → each can irrigate all planned fields → moderate yields (6). |
| **U Low / D High** | U still gets baseline flow (6). D adds a field; enough water remains because U did not expand, so D’s yield rises (7). |
| **U High / D Low** | U extracts the extra field, taking water that would have gone downstream → U’s yield jumps (8) while D suffers water stress → lower yield (4). |
| **U High / D High** | Both try to expand; upstream takes the bulk of the marginal water, leaving D with severe shortage → D’s payoff falls to 3, U still gets 8. |

**Why this is a distinct action situation:**  
The conflict is *purely* about how much water each farmer extracts; the strategic tension is “how much water to take vs how much to leave for the neighbour”.  The asymmetry is explicit: the upstream player can always secure the extra water, while the downstream player bears the externality.  No other decision (e.g., fishing) enters this game.

---

## 2.  Fishing‑Pressure Competition  
**Strategic tension:** *Both neighbours harvest from the same lake; excessive catch pushes the fish stock below a biological threshold, causing a collapse that hurts both.*  

### Players  
- **U** – Up‑stream farmer (first to reach the lake)  
- **D** – Down‑stream farmer (last to reach the lake)  

### Strategies  
|               | **D: Low‑Catch** (target = ½ × baseline) | **D: High‑Catch** (target = full baseline) |
|---------------|------------------------------------------|--------------------------------------------|
| **U: Low‑Catch** | (5 , 5) | (4 , 6) |
| **U: High‑Catch**| (6 , 4) | (2 , 2) |

### Pay‑off explanation  

*The lake’s adult fish stock **S** at the start of the season is 100 units.  The ecological threshold **T** = 80 units: if total catch **C** > T, recruitment in the next year collapses, reducing future pay‑offs to a low baseline (here represented by the “2” outcome).*

| Outcome | Total catch C | Relation to T | Immediate yield | Future impact (next season) |
|---------|---------------|---------------|----------------|------------------------------|
| **U Low / D Low** | 30 + 30 = 60  (< T) | Stock remains healthy | Moderate yields for both (5). |
| **U Low / D High**| 30 + 60 = 90 (> T) | Threshold crossed | U still gets a decent catch (4) because he fishes first; D gets a higher immediate catch (6) but both suffer a future collapse → payoff of 2 is reflected in the matrix for the “High‑High” cell only; here we keep the immediate payoff (4,6) because the collapse penalty is allocated to the joint “High‑High” outcome. |
| **U High / D Low**| 60 + 30 = 90 (> T) | Threshold crossed | U gets a higher immediate catch (6); D’s catch drops to 4 because less water‑driven recruitment reaches him. |
| **U High / D High**| 60 + 60 = 120 (> T) | Threshold crossed severely | Both exceed the threshold dramatically; the fish population collapses, so the next‑year expected return is minimal → both receive the low “2” payoff (representing a severe loss of future income). |

**Why this is a distinct action situation:**  
The strategic tension is *how aggressively to fish* when the resource is shared.  The ecological threshold (T) creates a *tipping point* that turns a mutually beneficial moderate‑catch equilibrium into a joint disaster if both over‑exploit.  The spatial order (U fishes first) gives the upstream farmer a slight advantage in the “High‑Low” cell, reflecting the sequential access described in the model.

---

## 3.  Water‑Fishing Trade‑off (Up‑stream Irrigation vs Down‑stream Fishing)  
**Strategic tension:** *The upstream farmer’s extra irrigation reduces river flow, which may drop the lake‑inflow below the **larval‑survival threshold** (Ecological Threshold Φ).  The downstream farmer’s fishing success depends on that recruitment.  The upstream farmer must choose between higher crop yields and the downstream neighbour’s future fish‑stock (and thus his own possible future fishing returns).*  

### Players  
- **U** – Up‑stream farmer (chooses irrigation level)  
- **D** – Down‑stream farmer (chooses fishing level)  

### Strategies  
|               | **D: Low‑Catch** (conserve fish) | **D: High‑Catch** (target catch) |
|---------------|----------------------------------|----------------------------------|
| **U: Low‑Irrigation** | (7 , 6) | (7 , 8) |
| **U: High‑Irrigation**| (9 , 3) | (9 , 1) |

### Pay‑off explanation  

*Larval‑survival threshold Φ = 40 % of the average July inflow.  If the upstream farmer irrigates heavily, the downstream flow into the lake falls below Φ, suppressing recruitment for that year.  This reduces the fish stock available to the downstream farmer (and later to the upstream farmer when he later fishes).*

| Outcome | July flow after U’s irrigation | Relation to Φ | D’s fish stock | Immediate crop yield (U) | Immediate fish yield (D) |
|---------|--------------------------------|---------------|----------------|--------------------------|--------------------------|
| **U Low / D Low** | Baseline flow (≥ Φ) | Threshold met | Healthy stock | Moderate crop (7) | Modest fish catch (6) |
| **U Low / D High**| Baseline flow (≥ Φ) | Threshold met | Healthy stock | Same crop (7) | High fish catch (8) |
| **U High / D Low**| Reduced flow (< Φ) | Threshold missed | Poor recruitment → low fish stock | Higher crop yield (9) | Low fish catch (3) |
| **U High / D High**| Reduced flow (< Φ) | Threshold missed | Poor recruitment → very low stock | Same high crop (9) | Very low fish catch (1) |

**Why this is a distinct action situation:**  
It couples *resource extraction* (water for irrigation) with *biological regeneration* (larval inflow).  The upstream farmer’s decision directly creates a **hydrological threshold** that determines whether the downstream farmer can sustain fishing.  The tension is “more water for crops now vs enough water for fish recruitment later”.  Spatial asymmetry is built‑in: only the upstream farmer can affect the threshold; the downstream farmer reacts only through his fishing intensity.

---

### Summary of Extracted Action Situations  

| # | Action Situation (IAD) | Players (Spatial Role) | Unique Strategic Tension |
|---|------------------------|------------------------|--------------------------|
| 1 | **Water‑Extraction Competition** | Up‑stream vs Down‑stream farmer | How much water each extracts; upstream extraction externality on downstream water availability. |
| 2 | **Fishing‑Pressure Competition** | Up‑stream vs Down‑stream farmer | Joint exploitation of a common fish stock with a biological tipping point (total catch > T). |
| 3 | **Water‑Fishing Trade‑off** | Up‑stream farmer (irrigation) vs Down‑stream farmer (fishing) | Upstream irrigation may push lake inflow below the larval‑survival threshold, harming downstream fishing; trade‑off between immediate crop gain and future fish productivity. |

These three games capture the full set of **distinct strategic dilemmas** that arise among farmers in the **decentralised (DV) version** of the water‑use ABM, respecting spatial asymmetry, ecological thresholds, and the model’s limit of ten irrigable fields per farm.
# Run 1 — openai/gpt-oss-120b

**Institutional‑Analysis‑and‑Development (IAD) – Decentralised (DV) Action Situations**  
Only the strategic choices that farmers make in the **decentralised** version are examined.  
Each table shows a *2‑player normal‑form* representation of a **unique strategic tension**.  
Numbers are illustrative (utility = yield + fish income – costs) and respect the model limits (max = 10 fields per farm).

---

## 1.  Up‑stream vs. Down‑stream **Water‑Extraction Conflict**  

**Strategic tension** – How much each farmer irrigates (high = 10 fields, low = 4 fields) when water is a *sequential* common‑pool.  
*Spatial asymmetry*: the upstream farmer extracts first; the downstream farmer receives whatever is left.

|                               | **Down‑stream Low (4 f)** | **Down‑stream High (10 f)** |
|-------------------------------|---------------------------|-----------------------------|
| **Up‑stream Low (4 f)**      | (5 , 5)                   | (5 , 7)                     |
| **Up‑stream High (10 f)**    | (8 , 2)                   | (8 , 1)                     |

*Interpretation*  

* **(Up‑stream Low, Down‑stream Low)** – both keep a modest area; water is sufficient for both → moderate yields (5, 5).  
* **(Up‑high, Down‑low)** – upstream grabs most water, gets a high yield (8); downstream suffers a shortage (2).  
* **(Up‑low, Down‑high)** – upstream leaves enough water for downstream to expand; upstream stays at 5, downstream reaches 7.  
* **(Both High)** – upstream still gets its full 8 (first‑come advantage) but downstream is almost dry (1).  

The matrix captures the **up‑stream advantage** and the **trade‑off** between expanding one’s own irrigation and starving the neighbour.

---

## 2.  Down‑stream vs. Up‑stream **Fishing‑Access Conflict**  

**Strategic tension** – Each farmer decides how aggressively to fish (High = target 30 fish, Low = target 10 fish).  
Because the **down‑stream farmer accesses the lake first**, his catch directly reduces the stock available to the up‑stream farmer.

|                                   | **Up‑stream Low (10 f)** | **Up‑stream High (30 f)** |
|-----------------------------------|--------------------------|---------------------------|
| **Down‑stream Low (10 f)**        | (2 , 2)                  | (2 , 6)                   |
| **Down‑stream High (30 f)**       | (1 , 6)                  | (1 , 4)                   |

*Interpretation*  

* **(Low, Low)** – both fish conservatively; each gets 10 fish → modest payoff (2, 2).  
* **(Down‑high, Up‑low)** – downstream harvests 30 (payoff 6); the remaining stock supports only 10 for upstream (payoff 1).  
* **(Down‑low, Up‑high)** – downstream takes 10 (payoff 2); enough fish remain for upstream to reach 30 (payoff 6).  
* **(Both High)** – the downstream farmer still gets his 30 (payoff 6) but the upstream farmer is left with a severely depleted stock, yielding only 10 (payoff 1); the ecological cost of over‑exploitation reduces the joint payoff to (1, 4).  

The matrix makes explicit the **order‑of‑access advantage** of downstream agents and the **collective risk of over‑fishing**.

---

## 3.  Farmer (any) vs. **Ecological Threshold** (Larval‑Inflow Condition)  

**Strategic tension** – A single farmer decides on irrigation intensity (High = 10 fields, Low = 4 fields) while the **environmental state** can be either **Above the larval‑inflow threshold (A)** or **Below it (B)**.  
If the threshold is breached, larval recruitment collapses, eliminating future fish income (λ · H = 0) and reducing long‑term water‑flow benefits.

|                                   | **Environment A (threshold met)** | **Environment B (threshold breached)** |
|-----------------------------------|------------------------------------|------------------------------------------|
| **Farmer Low irrigation (4 f)**   | (5 , 1)                            | (2 , 0)                                  |
| **Farmer High irrigation (10 f)** | (9 , 0)                            | (3 , –1)                                 |

*Payoff components* (illustrative):  

*Yield* = base + water‑stress factor (higher when irrigation ≤ water available).  
*Fish income* = λ · H × (1 if A, 0 if B).  
*Cost* = irrigation expense (higher for 10 fields).  

*Interpretation*  

* **(Low, A)** – moderate irrigation, threshold satisfied → decent crop yield (5) plus a small fish bonus (1).  
* **(High, A)** – maximises crop yield (9) but uses all water; fish bonus disappears because the farmer keeps the water for crops (environment payoff 0).  
* **(Low, B)** – water is scarce, low irrigation still yields little (2) and no fish income (0).  
* **(High, B)** – farmer pushes 10 fields despite a broken ecological threshold → low crop yield (3) due to severe water stress, incurs extra irrigation cost (‑1 to the environment, representing ecosystem degradation).  

This matrix captures the **ecological tipping point** (larval‑inflow threshold) that couples a farmer’s irrigation decision to the health of the fish population and, consequently, to the farmer’s own future returns.

---

### How the Action Situations Satisfy the Requirements  

| Requirement | Fulfilment |
|-------------|------------|
| **Only DV (decentralised) cases** | All matrices are built from farmer‑to‑farmer or farmer‑to‑environment interactions; the national‑authority layer is omitted. |
| **Spatial asymmetry** | Situation 1 (water extraction) and Situation 2 (fishing) explicitly differentiate **up‑stream** vs **down‑stream** agents and the order in which the resource is accessed. |
| **Ecological thresholds** | Situation 3 embeds the **larval‑inflow threshold** that determines whether fish recruitment continues. |
| **Distinct strategic dilemmas** | 1 = “how much water to take”; 2 = “how much fish to harvest”; 3 = “irrigate intensively vs respect the ecological flow limit”. |
| **2‑player normal‑form payoff matrices** | Each table lists the two players, their two strategies, and the resulting utilities. |
| **Maximum fields = 10** | “High” irrigation always corresponds to the maximum of 10 fields; “Low” corresponds to a feasible lower level (4 fields). |

These three action situations constitute a concise, IAD‑styled representation of the strategic landscape that **decentralised farmers** face in the water‑use model.
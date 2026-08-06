# Run 30 — openai/gpt-oss-120b

**I.  Action‑situations (decentralised – DV) extracted with the IAD lens**  
Only farmer‑to‑farmer strategic interactions are considered (the national authority does not appear in the DV version).  
Each situation captures a *unique* strategic tension, respects the upstream‑down‑stream spatial asymmetry, and embeds the ecological thresholds that drive the system (water‑flow threshold for larval migration and fish‑stock collapse threshold).  
For every situation a 2‑player normal‑form matrix is supplied (players = an **Up‑stream farmer U** and a **Down‑stream farmer D**).  
Payoffs are expressed in *relative utility units* (higher = better outcome).  The numbers are illustrative – they capture the direction of incentives rather than precise calibrated values.

---

### 1.  Water‑Extraction Competition (Irrigation‑field expansion)

|                     | **D : Keep ( K )** | **D : Add field (A)** |
|---------------------|-------------------|-----------------------|
| **U : Keep (K)**    | (6 , 6)           | (8 , 4)               |
| **U : Add field (A)**| (4 , 8)           | (2 , 2)               |

**Strategic tension** – *“Do I expand my irrigated area knowing that my extra draw will reduce the water that reaches the downstream neighbour?”*  

*Why the payoffs look like this*  

* **Water balance**: total water that arrives each year is **W** (the realised inflow).  Each added field consumes a fixed volume **w_f**.  When **U + D** add a field, total demand may exceed **W**.  
* **Priority rule**: water is taken sequentially upstream → U is first to satisfy his demand; D receives whatever is left.  
* If both keep (K,K) the water surplus is modest; both obtain a comfortable yield (6,6).  
* If U adds while D keeps, U captures the extra water, raising his yield (8) while D suffers a shortfall (4).  
* If D adds while U keeps, the reverse occurs (4,8).  
* If both add, total demand > W; the system falls below the **larval‑migration threshold** (see Situation 2).  Both experience severe water stress → low payoffs (2,2).  

**Ecological link** – the (A,A) cell pushes the river flow below the critical volume needed for larvae to reach the lake, which later reduces fish‑stock pay‑offs (captured in Situation 2).

---

### 2.  Fishing‑Harvest Competition (Down‑stream priority)

|                     | **D : Conserving (C)** | **D : Aggressive (G)** |
|---------------------|------------------------|------------------------|
| **U : Conserving (C)**| (5 , 5)                | (3 , 7)                |
| **U : Aggressive (G)**| (7 , 3)                | (1 , 1)                |

**Strategic tension** – *“Should I harvest the maximum allowed catch knowing that my catch reduces the future fish stock for both of us, especially when the downstream farmer gets first access?”*  

*Why the payoffs look like this*  

* **Order of access**: downstream farmer D fishes first; if enough fish remain, U can also catch.  
* **Target catch** = T (fixed).  “Conserving” means catching **T‑1** (leaving one extra fish for the next year); “Aggressive” means catching the full **T**.  
* When both conserve, the fish‑stock stays above the **density‑dependent mortality threshold**, yielding moderate, stable returns (5,5).  
* If U is aggressive while D conserves, U captures the extra fish before D’s turn, boosting his payoff (7) but leaving D with less (3).  
* The reverse gives (3,7).  
* When both are aggressive, the total harvest pushes the adult‑fish abundance below the **population‑viability threshold**; the stock collapses and both receive only a token return (1,1).  

**Ecological link** – the (G,G) outcome can trigger the **larval‑migration threshold** in the water‑flow sub‑model (low flow → no larvae), reinforcing the coupling between Situations 1 and 2.

---

### 3.  Budget‑Risk Decision (Investment vs. Financial‑safety)

|                     | **D : Save (S)** | **D : Invest (I)** |
|---------------------|------------------|--------------------|
| **U : Save (S)**    | (6 , 6)          | (5 , 8)            |
| **U : Invest (I)**  | (8 , 5)          | (2 , 2)            |

**Strategic tension** – *“Do I use my current budget to add an extra field (risking water shortage) when my neighbour may be doing the same, possibly leaving us both unable to cover irrigation costs?”*  

*Why the payoffs look like this*  

* **Budget constraint**: each farmer starts the season with a budget **B**.  Adding a field costs **c_f**; the expected revenue from a successful field is **r_f** ( > c_f ).  
* If both **Save**, they keep a safe surplus (6,6).  
* If U **Invests** while D **Saves**, U enjoys the extra revenue (8) and D remains safe (5).  
* The mirror case gives (5,8).  
* If both **Invest**, the combined water demand (see Situation 1) often exceeds the realised inflow, producing water stress that erodes yields and may even cause a budget deficit; both end up with low pay‑offs (2,2).  

**Ecological link** – the (I,I) cell reproduces the same water‑shortage condition that triggers the **larval‑migration threshold** (Situation 1) and can also lower future fish catches (Situation 2) because of reduced water‑flow‑driven recruitment.

---

## Summary of Distinct Strategic Tensions

| # | Action‑situation (title) | Players | Core dilemma (strategic tension) |
|---|--------------------------|---------|-----------------------------------|
| 1 | **Water‑Extraction Competition** | Up‑stream U vs Down‑stream D | Expand irrigated area vs preserve downstream water (spatial asymmetry, water‑flow threshold). |
| 2 | **Fishing‑Harvest Competition** | Up‑stream U vs Down‑stream D | Aggressive catch vs conserving stock (downstream priority, fish‑population threshold). |
| 3 | **Budget‑Risk Decision** | Up‑stream U vs Down‑stream D | Invest in extra field (high return, high risk) vs keep financial safety (risk of collective water shortage). |

Each matrix captures the *pay‑off curvature* that makes the situation a genuine **action situation** in the IAD sense: a set of actors, a set of alternative strategies, a rule‑based outcome function, and a resulting pattern of incentives that can generate coordination problems, dilemmas, or commons‑tragedy dynamics.  The three matrices together cover the main decentralized strategic interactions described in the ODD + D specification while respecting the required constraints (no central authority, spatial asymmetry, ecological thresholds, and the 10‑field maximum).
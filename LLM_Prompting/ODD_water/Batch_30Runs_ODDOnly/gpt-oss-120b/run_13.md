# Run 13 — openai/gpt-oss-120b

**Decentralised (DV) Action‑Situations – IAD Framework**  
Only farmer‑to‑farmer strategic interactions are extracted (the national authority does not act in the DV version).  
Each table shows a **2‑player normal‑form game** (Up‑stream U vs Down‑stream D). Payoffs are illustrative (higher = better) and embed the three required features  

* **Spatial asymmetry** – U is always upstream of D.  
* **Ecological thresholds** – a water‑flow threshold **T** determines whether larvae reach the lake; if total extraction pushes the flow < T the fish stock collapses and fishing pay‑offs fall to zero.  
* **Maximum fields = 10** – “High demand” means asking for one extra field (still ≤ 10).  

---

### 1. Water‑Extraction Competition  

|                     | **D: Low demand** (keep current fields) | **D: High demand** (add +1 field) |
|---------------------|------------------------------------------|-----------------------------------|
| **U: Low demand**   | (4 , 4) – both get enough water, yields are moderate and no stress. | (3 , 5) – D extracts more, U still ok because flow is still ≥ T; D gains extra yield. |
| **U: High demand**  | (5 , 3) – U extracts extra field, D suffers reduced water (still ≥ T). | (2 , 2) – total extraction pushes flow **< T** → fish larvae lost, both suffer water stress and lower yields. |

**Justification**  
*Strategic tension*: each farmer decides whether to increase the number of irrigated fields.  
*Spatial asymmetry*: the upstream farmer’s extra extraction directly reduces the water that reaches the downstream farmer, so the downstream payoff is more sensitive to U’s “High”.  
*Ecological threshold*: when both choose “High” the combined drawdown drops the river flow below the larvae‑survival threshold **T**, cutting off the fish subsidy and lowering both pay‑offs (the “2,2” cell).  

---

### 2. Fishing‑Priority Game  

|                     | **D: Aggressive fish** (take full target) | **D: Conservative fish** (take half target) |
|---------------------|--------------------------------------------|---------------------------------------------|
| **U: Aggressive fish** | (3 , 2) – D fishes first, depletes stock; U gets little left. | (5 , 4) – D leaves enough fish; both harvest well (flow ≥ T). |
| **U: Conservative fish** | (4 , 5) – D gets most of the catch; U’s restraint leaves stock high. | (6 , 6) – Both fish lightly, stock stays robust, and because flow ≥ T the larvae influx is maintained. |

**Justification**  
*Strategic tension*: each farmer chooses how much to fish when the lake is accessed.  
*Spatial asymmetry*: the downstream farmer always fishes **first**, so his “Aggressive” choice can starve the upstream farmer.  
*Ecological threshold*: the payoff matrix assumes the river flow is still above **T** (otherwise all fishing pay‑offs would drop to zero). The “Aggressive‑Aggressive” cell (3,2) reflects the downstream advantage and the upstream loss.  

---

### 3. Joint Water‑Fish Threshold Coordination  

|                     | **D: Conserve water** (stay at current fields) | **D: Extract water** (add +1 field) |
|---------------------|------------------------------------------------|------------------------------------|
| **U: Conserve water** | (7 , 7) – total extraction stays well above **T**; both enjoy high yields **and** a healthy fish stock. | (5 , 6) – D extracts one extra field, flow still ≥ T, D gains extra crop profit, U loses a little water but remains above the threshold. |
| **U: Extract water**  | (6 , 5) – U extracts, D conserves; flow still ≥ T, U gains crop profit, D loses a bit of water. | (1 , 1) – Both extract; combined drawdown pushes flow **< T**, larvae stop arriving, fish catch collapses and water stress spikes – both suffer severe losses. |

**Justification**  
*Strategic tension*: a classic **coordination / tragedy‑of‑the‑commons** problem – each farmer can either “Conserve” or “Extract” an extra field.  
*Spatial asymmetry*: the upstream farmer’s extraction has a larger marginal impact on the downstream flow, so the payoff loss for D when U extracts is larger (5 vs 6).  
*Ecological threshold*: the only cell where the flow falls below **T** is the joint “Extract‑Extract” outcome, delivering the lowest pay‑offs (1,1) because the fish‑recruitment pulse is lost and water stress dramatically reduces crop yields.  

---

### Summary of Distinct Action‑Situations  

| # | Action‑Situation (IAD) | Players (spatial) | Core Strategic Dilemma |
|---|------------------------|-------------------|------------------------|
| 1 | **Water‑Extraction Competition** | Up‑stream U vs Down‑stream D | Whether to ask for an extra irrigation field; extra extraction harms downstream water availability and can breach the ecological flow threshold. |
| 2 | **Fishing‑Priority Game** | Down‑stream D (first fisher) vs Up‑stream U (second) | How aggressively to fish given the downstream priority; aggressive downstream fishing can starve upstream, while over‑fishing risks stock collapse if flow is already low. |
| 3 | **Joint Water‑Fish Threshold Coordination** | Up‑stream U vs Down‑stream D | Joint decision to conserve or extract water; coordinated conservation keeps flow ≥ T and sustains fish recruitment, while mutual extraction triggers a threshold breach and severe losses. |

These three matrices capture **all unique strategic tensions** that arise among farmers in the **decentralised (DV) version** of the water‑use model, respecting spatial asymmetry, the ecological water‑flow threshold, and the model’s field‑limit constraint.
# Run 7 — openai/gpt-oss-120b

**NOTE:**  
Only the **decentralised (DV)** version of the model is considered.  All matrices are written for a *pair* of neighbouring farmers – one **up‑stream (U)** and one **down‑stream (D)** – because the IAD framework defines an “action situation” as the set of participants, the shared resource, the rules and the strategic problem they face.  The three situations below capture every *qualitatively different* strategic tension that emerges from the description of the DV model while respecting the spatial asymmetry (U is always first in the water‑flow sequence, D is first in the fishing‑access sequence) and the ecological thresholds (water‑stress‑induced yield collapse and fish‑stock tipping point).  The maximum number of irrigable fields is 10; the binary choice “Expand (E)” means “add one field (if budget allows, up to 10)”, “Maintain (M)” means “keep the current number of fields”.

---

## 1.  Water‑Extraction Conflict (Up‑stream vs Down‑stream)

### Strategic tension  
**“Should I expand my irrigated area and risk depriving my neighbour of water, or should I hold back and preserve water for downstream use?”**  

*Why it is unique*: the decision directly couples the two agents through the **hydrological flow**; the upstream farmer’s extra extraction reduces the volume that reaches the downstream farmer, creating a classic “up‑stream over‑use vs downstream scarcity” dilemma.  The ecological threshold is the **water‑stress level** – if the total extracted volume exceeds the inflow, both farmers suffer a sharp yield loss (the denominator in the yield equation falls below the required water, driving yields toward zero).

### Normal‑form (binary) payoff matrix  

|                     | **Down‑stream: Maintain (M)** | **Down‑stream: Expand (E)** |
|---------------------|------------------------------|-----------------------------|
| **Up‑stream: Maintain (M)** | (6 , 6) – both receive enough water, yields near‑maximal | (5 , 7) – U keeps enough water, D adds one field and still receives enough |
| **Up‑stream: Expand (E)**   | (7 , 4) – U gains extra field, D suffers water shortage (yield drops) | (4 , 3) – both expand → total demand > inflow → severe water stress; all yields collapse (below ecological threshold) |

*Payoff interpretation* (arbitrary utility units, higher = better):  

* **(6,6)** – “co‑operative” outcome: each farmer keeps the current number of fields; water demand = 0.9 × inflow → yields ≈ 90 % of Ymax.  
* **(7,4)** – U “defects” by expanding; D’s water share falls below 70 % of demand → D’s yield falls sharply (below the water‑stress tipping point).  
* **(5,7)** – D expands while U does not; U still has enough water, D enjoys the extra field.  
* **(4,3)** – Mutual expansion pushes total demand > inflow; the **water‑stress threshold** is crossed, causing a collapse of yields for both (≈ 30 % of Ymax).

---

## 2.  Fishing‑Harvest Conflict (Down‑stream vs Up‑stream)

### Strategic tension  
**“Should I take the full target catch now (risking stock collapse) or conserve part of the fish stock for future seasons?”**  

*Why it is unique*: the **order of access** is reversed – the downstream farmer harvests first, then the upstream farmer.  The ecological threshold is the **fish‑stock tipping point**: if the total catch in a year exceeds the sustainable harvest (≈ 30 % of the adult stock), density‑dependent mortality spikes and the next year’s recruitment drops dramatically.  The tension is therefore about **short‑term gain vs long‑term stock viability**, with a direct externality on the neighbour.

### Normal‑form (binary) payoff matrix  

|                     | **Up‑stream: Conserve (C)** | **Up‑stream: Harvest (H)** |
|---------------------|-----------------------------|----------------------------|
| **Down‑stream: Conserve (C)** | (4 , 4) – low harvest for both, stock stays above threshold → future high returns | (5 , 2) – D conserves, U over‑harvests; stock drops, U gets a one‑time boost, D suffers later |
| **Down‑stream: Harvest (H)**  | (2 , 5) – D takes full target, U conserves; stock still above threshold because total catch ≤ sustainable level | (1 , 1) – Both harvest full target → total catch > sustainable level → stock collapses; both receive only a tiny immediate payoff |

*Payoff interpretation*:  

* **(4,4)** – Mutual restraint keeps the adult stock > Tₛₜₐ𝚋ᵢₗᵢ𝚝𝚢, guaranteeing a modest but reliable fish income (λ·H).  
* **(5,2)** – The upstream farmer “defects” by harvesting despite the downstream farmer’s restraint; the stock is pushed past the **density‑dependent mortality threshold** (σ), giving U a short‑term windfall but leaving D with a depleted future stock (low payoff).  
* **(2,5)** – The downstream farmer harvests, but the upstream farmer holds back; total catch stays below the ecological tipping point, so D receives the immediate benefit while the stock remains healthy for U.  
* **(1,1)** – Mutual over‑harvest triggers the **fish‑population collapse** (the term e^{‑σ∑Nᵢ} ≈ 0), so both obtain only a minimal subsistence catch.

---

## 3.  Field‑Expansion after Low Income (Farmer vs Neighbour)

### Strategic tension  
**“Having earned less than my income threshold last year, should I take a risky extra field (even if water may be scarce) or should I stay conservative and risk further income loss?”**  

*Why it is unique*: the decision rule is **conditional on the previous year’s income** and on **budget constraints**; the neighbour’s behaviour matters because water is a *common‑pool* – an upstream farmer’s risky expansion reduces the downstream farmer’s ability to meet his own water demand, potentially pushing the downstream farmer below his own income threshold in the next year.  This creates a **dynamic inter‑temporal coordination problem** that is distinct from the pure water‑extraction conflict (Situation 1) because the trigger is *income‑based* rather than *purely water‑stress*.

### Normal‑form (binary) payoff matrix  

|                     | **Neighbour: Conservative (C)** | **Neighbour: Risky (R)** |
|---------------------|--------------------------------|--------------------------|
| **Self: Conservative (C)** | (6 , 6) – both keep current fields; stable income above threshold | (5 , 7) – self stays safe, neighbour expands and may cause downstream water shortage for self next year |
| **Self: Risky (R)**        | (7 , 4) – self expands, neighbour stays conservative; self gains extra yield now, neighbour may suffer water stress later | (3 , 3) – both take the risk; total demand > inflow → immediate water stress for both and both fall below income threshold (risk of a cascade) |

*Payoff interpretation*:  

* **(6,6)** – Mutual conservatism yields stable, moderate returns; both remain above the **minimum‑income threshold**.  
* **(7,4)** – The “risky” farmer adds a field, enjoys a higher current yield (if water still sufficient), while the neighbour’s water share is reduced, pushing his income below the threshold.  
* **(5,7)** – The neighbour’s risky expansion harms the focal farmer (down‑stream effect), but the focal farmer’s conservative stance protects his own budget (he can still meet consumption).  
* **(3,3)** – Mutual risk leads to **water‑stress collapse** (the denominator in the yield equation falls below the critical 0.5 × V_D, causing yields to drop sharply). Both fall under the income threshold, triggering the “risk‑increase” rule in the next season – a classic **poverty trap**.

---

### How the matrices satisfy the required constraints  

| Constraint | Satisfaction |
|------------|---------------|
| **Only DV (decentralised) actions** | All matrices involve *farmers* making predictions, field‑expansion, irrigation and fishing decisions; the national authority never appears. |
| **Spatial asymmetry** | Situation 1 and 2 explicitly label *up‑stream* vs *down‑stream* players and embed the order of water withdrawal / lake access. Situation 3 pairs “self” with a neighbour, preserving the upstream‑downstream ordering. |
| **Ecological thresholds** | Situation 1: water‑stress threshold (total demand > inflow). Situation 2: fish‑stock tipping point (total catch > sustainable harvest). Situation 3: water‑stress threshold again, but triggered by income‑based risk behaviour. |
| **Maximum fields = 10** | The “Expand (E)” / “Risky (R)” actions are defined as “add **one** field, respecting the 10‑field cap”.  The payoff numbers assume the farmer is below the cap; if at 10, the “Expand” action is unavailable (not represented because the strategic tension disappears). |
| **Two‑player normal form** | Each matrix is a 2 × 2 game with clearly identified players and payoffs. |
| **Distinct strategic dilemmas** | 1) Pure water‑allocation conflict, 2) Fishing‑stock sustainability conflict, 3) Income‑driven risky expansion conflict – each stems from a different rule or ecological/process in the DV model. |

These three action situations capture all qualitatively different strategic tensions that arise among farmers in the decentralised version of the water‑use model, while honouring the spatial hierarchy, the ecological thresholds, and the institutional rules described in the ODD + D specification.
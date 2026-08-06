# Run 19 — openai/gpt-oss-120b

**IAD‑derived Action Situations for the Decentralised (DV) version**  
*(Only farmer‑to‑farmer interactions are considered; the national authority is omitted.  
Spatial asymmetry – upstream (U) vs. downstream (D) – and ecological thresholds are made explicit.  
The maximum number of irrigable fields per farm is 10, which bounds the “expansion” choices.)*  

---

## 1. Water‑Extraction Competition  
**Strategic tension:** *Up‑stream priority vs. downstream demand for a limited water flow.*  

|                     | **Down‑stream D: Hold (H)**<br/>(keep current fields) | **Down‑stream D: Expand (E)**<br/>(add +1 field) |
|---------------------|------------------------------------------------------|------------------------------------------------|
| **Up‑stream U: Hold (H)** | **(3 , 3)**  <br/>*Both keep enough water → high yields for both.* | **(2 , 4)**  <br/>*U leaves water, D extracts more; D gets a larger share, U still meets demand.* |
| **Up‑stream U: Expand (E)**| **(4 , 2)**  <br/>*U takes the first slice of water → high yield, D receives less.* | **(2 , 1)**  <br/>*Both push the limit; water stress hits; U’s priority gives a modest advantage, D suffers.* |

*Payoff scale:* 1 = severe water stress (very low yield), 2 = moderate, 3 = high, 4 = very high.  
The matrix captures the **spatial asymmetry** (U always receives water before D) and the **resource‑scarcity dilemma** that each farmer faces when deciding whether to expand irrigated fields (max 10).

---

## 2. Fishing‑Race (Access‑Priority)  
**Strategic tension:** *Down‑stream farmer’s first‑access right to the lake vs. upstream farmer’s later access.*  

|                     | **Down‑stream D: Low catch (L)**<br/>(target ≤ ½ max) | **Down‑stream D: High catch (H)**<br/>(target ≈ max) |
|---------------------|------------------------------------------------------|---------------------------------------------------|
| **Up‑stream U: Low catch (L)** | **(3 , 3)**  <br/>*Both harvest modestly → fish stock stays healthy, each keeps the intended share.* | **(2 , 4)**  <br/>*D grabs most of the available fish; enough remains for U to obtain a decent catch.* |
| **Up‑stream U: High catch (H)**| **(4 , 2)**  <br/>*U attempts a large haul after D has taken little; enough fish remain for U to succeed.* | **(1 , 5)**  <br/>*Both aim high; D harvests first, depleting the stock for U → U’s catch collapses, D enjoys a bumper.* |

*Payoff scale:* 1 = near‑zero catch, 2 = low, 3 = moderate, 4 = high, 5 = very high (the maximum possible catch).  
The asymmetry is built‑in: the downstream player always extracts before the upstream player, creating a **race‑to‑catch** dilemma.

---

## 3. Collective Water‑Use vs. Fish‑Recruitment Threshold  
**Strategic tension:** *Total water extraction by the two farms can push the river flow below the ecological threshold needed for larval immigration, endangering the fish population.*  

|                     | **Down‑stream D: Low extraction (L)**<br/>(≤ 5 fields) | **Down‑stream D: High extraction (H)**<br/>(≥ 6 fields) |
|---------------------|------------------------------------------------------|------------------------------------------------------|
| **Up‑stream U: Low extraction (L)** | **(4 , 4)**  <br/>*Total extraction stays below the threshold → fish recruitment succeeds; both enjoy high agricultural yields and fish income.* | **(3 , 2)**  <br/>*Combined extraction is just at the threshold; fish recruitment weakens → moderate fish income, still good crops.* |
| **Up‑stream U: High extraction (H)**| **(3 , 2)**  <br/>*Same as above – threshold crossed only by D’s high use; fish stock drops, U’s crops stay high.* | **(1 , 1)**  <br/>*Both pull heavily; flow falls far below the larval‑survival threshold → fish collapse (no fish income) and severe water stress reduces yields.* |

*Payoff scale:* 1 = very poor overall return (crop loss + no fish), 2 = poor, 3 = moderate, 4 = high (both crops and fish).  

The matrix makes explicit the **ecological tipping point**: when the sum of the two farmers’ extractions exceeds the flow needed for larvae survival, the fish population collapses, turning a purely economic game into a **social‑ecological** dilemma.

---

### How the matrices satisfy the constraints  

| Constraint | Fulfilment |
|------------|------------|
| **Only DV (decentralised) actions** | All matrices involve *farmer‑to‑farmer* decisions; the national authority is absent. |
| **Spatial asymmetry** | Situations 1 and 2 explicitly distinguish *up‑stream* (first‑mover on water) from *down‑stream* (first‑mover on fish). |
| **Ecological thresholds** | Situation 3 incorporates the water‑flow threshold required for fish larval immigration. |
| **Maximum fields = 10** | “Expand” actions are limited to +1 field (or to a total ≤ 10); the matrices are defined for the binary choice “Hold/Low” vs “Expand/High”. |
| **Unique strategic tensions** | – Competition for scarce water (S1). <br>– Race for fish harvest (S2). <br>– Joint impact on a biological threshold (S3). |

These three action situations capture the core strategic dilemmas that emerge in the decentralised water‑use model under the IAD framework.
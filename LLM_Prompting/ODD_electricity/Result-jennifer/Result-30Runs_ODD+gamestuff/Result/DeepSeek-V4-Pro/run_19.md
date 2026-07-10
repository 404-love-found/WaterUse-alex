# Run 19 — deepseek-ai/DeepSeek-V4-Pro

### 1. DSM Coordination Game (Capacitor Adoption)
- **Location:** Village-level transformer service area.
- **Players:** Two farmers from the same transformer group (representative of paired farmers in the adoption pool).
- **Roles:** Electricity consumers considering investment in voltage‑stabilizing equipment.
- **Actions:**  
  - Farmer A: Invest in capacitor (I) or Not invest (N).  
  - Farmer B: Invest (I) or Not invest (N).
- **Control Rules:**  
  - If both invest, the shared benefit (voltage stability, reduced burnouts) is realised and both enjoy improved reliability.  
  - If only one invests, the benefit is negligible – the investor pays the cost with no return, while the non‑investor free‑rides but gets no improvement.  
  - If neither invests, the status quo (low reliability, no investment cost) prevails.
- **Information:** Farmers observe neighbours’ past adoption and outcomes but cannot know the simultaneous choice of the other. Perceptions of benefits are noisy; farmers may misattribute voltage improvements.
- **Outcomes:** Voltage quality, transformer failure risk, pump efficiency, individual investment cost.
- **Payoffs (ordinal, 0–3):**  
  - Mutual investment (I,I): both get 3.  
  - Unilateral investment (I,N) or (N,I): investor gets 0, non‑investor gets 2.  
  - No investment (N,N): both get 2.
- **Strategic Tension:** **Assurance game (coordination).** Farmers want to coordinate on investment because mutual adoption yields the highest payoff, but each fears being the only one to pay, which gives the worst individual outcome. This is a **strategic** situation.
- **Temporal Structure:** Repeated annually, with social learning and experimentation.
- **Relevant Rules:** Choice rules based on bounded rationality and social learning; boundary rules define the transformer group as the relevant interaction set.

**Payoff Matrix (Farmer A, Farmer B):**

| A \ B | Invest (I) | Not invest (N) |
|-------|------------|----------------|
| **Invest (I)** | (3, 3) | (0, 2) |
| **Not invest (N)** | (2, 0) | (2, 2) |

**Compliance with ODD+D:** Matches the description: capacitor benefits are strongest when adoption is coordinated; unilateral investment is unattractive because the reliability improvement is weak or hard to attribute. The ordinal structure reflects the assurance dilemma observed in the field.

---

### 2. Authorization Game (Formal Connection Seeking)
- **Location:** Transformer area, involving a disconnected farmer and the substation staff responsible for that transformer.
- **Players:** Disconnected farmer (F) and Substation staff (S).
- **Roles:** Farmer as connection seeker; Staff as service provider/authorizer.
- **Actions:**  
  - Farmer: Seek formal connection (Seek) or Remain informal (Informal).  
  - Staff: Provide service (Provide) – invest effort/capacity to grant and support a formal connection – or Withhold (Withhold).
- **Control Rules:**  
  - If farmer seeks and staff provides, a formal connection is established: farmer pays the fee, gets reliable legal access; staff bears effort cost but gains compliance and avoids penalties.  
  - If farmer seeks and staff withholds, farmer pays the fee but receives no connection or poor service; staff saves effort but risks complaints.  
  - If farmer remains informal, formal service is irrelevant; farmer stays informal (no fee, but risk of enforcement), staff’s action affects only their own workload.
- **Information:** Farmer knows the formal fee and past staff behaviour; staff knows the farmer’s request and their own workload. Both have imperfect knowledge of the other’s current intention.
- **Outcomes:** Connection status, reliability of supply, fee payment, staff effort, compliance record.
- **Payoffs (ordinal, 0–3):**  
  - (Seek, Provide): Farmer 3, Staff 3 (best for both).  
  - (Seek, Withhold): Farmer 0, Staff 2 (farmer loses, staff saves effort but faces oversight risk).  
  - (Informal, Provide): Farmer 2, Staff 1 (farmer stays informal, staff wastes effort).  
  - (Informal, Withhold): Farmer 2, Staff 2 (status quo informal tolerance).
- **Strategic Tension:** **Coordination game with asymmetric risk (trust).** Both prefer the formal connection outcome, but the farmer will seek only if they trust the staff to provide; the staff may prefer to withhold if the farmer does not seek, creating two equilibria: (Seek, Provide) and (Informal, Withhold). This is a **strategic** situation.
- **Temporal Structure:** Repeated annually; a farmer may seek formalisation once, but the interaction recurs for different farmers.
- **Relevant Rules:** Boundary rules define who is a disconnected farmer; position rules assign staff as authorizer; choice rules allow seeking or remaining informal; control rules link joint actions to connection outcomes.

**Payoff Matrix (Farmer, Staff):**

| Farmer \ Staff | Provide | Withhold |
|----------------|---------|----------|
| **Seek**       | (3, 3)  | (0, 2)   |
| **Informal**   | (2, 1)  | (2, 2)   |

**Compliance with ODD+D:** Reflects the model’s description that disconnected farmers choose between pursuing a paid formal connection or remaining informal, and that staff decide whether to invest effort. The payoffs capture the asymmetry: the farmer risks a loss if staff withholds, while staff’s best outcome requires the farmer to seek.

---

### 3. Collusion Exchange Game (Informal Reciprocity)
- **Location:** Transformer area, between a farmer and a matched substation staff member.
- **Players:** Farmer (F) and Substation staff (S).
- **Roles:** Farmer as potential colluder; Staff as potential colluder/enforcer.
- **Actions:**  
  - Farmer: Offer collusion (Offer) – willingness to engage in informal exchange – or Not offer (Not).  
  - Staff: Honour collusion (Honour) – reciprocate and tolerate informal access – or Betray (Betray) – enforce rules/report.
- **Control Rules:**  
  - A collusive tie forms only if both choose Offer and Honour.  
  - If farmer offers and staff betrays, farmer faces penalty; staff gains enforcement credit.  
  - If farmer does not offer and staff honours, staff is exposed to risk without farmer participation.  
  - If neither offers/honours, formal compliance status quo prevails.
- **Information:** Farmer knows own financial strain and perceived staff trustworthiness; staff knows oversight risk and farmer’s capacity to reciprocate. Both have imperfect information about the other’s current willingness.
- **Outcomes:** Existence of collusive tie, informal access, penalty risk, staff reputation, enforcement effort.
- **Payoffs (ordinal, 0–3):**  
  - (Offer, Honour): Farmer 3, Staff 2 (mutual benefit, but staff’s payoff tempered by risk).  
  - (Offer, Betray): Farmer 0, Staff 3 (staff gains from enforcement, farmer punished).  
  - (Not, Honour): Farmer 2, Staff 1 (staff wastes effort, farmer safe).  
  - (Not, Betray): Farmer 2, Staff 2 (status quo).
- **Strategic Tension:** **Trust game (social dilemma).** The farmer must trust the staff to honour the collusion; however, the staff has a dominant incentive to betray when trust is offered, leading to the Pareto‑inferior equilibrium (Not, Betray). This is a **strategic** situation.
- **Temporal Structure:** Repeated annually; ties can persist or dissolve based on mutual choices.
- **Relevant Rules:** Boundary rules define the matched pair; choice rules allow offering or not; control rules make tie formation conditional on mutual agreement; the game captures the informal institution of collusion.

**Payoff Matrix (Farmer, Staff):**

| Farmer \ Staff | Honour | Betray |
|----------------|--------|--------|
| **Offer**      | (3, 2) | (0, 3) |
| **Not**        | (2, 1) | (2, 2) |

**Compliance with ODD+D:** Directly follows the description that a collusion tie forms only when both sides are independently willing, and that staff enforcement involves effort costs and potential sanctions. The trust dilemma reflects the risk that staff may enforce even when a farmer offers collusion, matching the model’s uncertainty about detection and staff’s discretionary power.

---

### 4. Capacity Provision Game (Staff Investment for Tied Farmers)
- **Location:** Transformer area, involving a substation staff member and a tied farmer (either a disconnected farmer awaiting informal capacity, or a connected free‑rider being offered regularisation).
- **Players:** Substation staff (S) and Tied farmer (F).
- **Roles:** Staff as capacity provider; Farmer as beneficiary/potential contributor.
- **Actions:**  
  - Staff: Invest in transformer capacity (Invest) or Not invest (Not).  
  - Farmer: Accept regularisation/contribute (Accept) or Reject (Reject) – refuse regularisation, remain free‑riding.
- **Control Rules:**  
  - If staff invests and farmer accepts, capacity is upgraded, reliability improves; farmer pays fees/formalises, staff bears cost.  
  - If staff invests and farmer rejects, farmer free‑rides on the improved capacity without paying; staff bears the full cost.  
  - If staff does not invest, capacity remains low; if farmer accepts, they pay but get no improvement; if both reject/not invest, the status quo low capacity persists.
- **Information:** Staff knows own workload and the farmer’s tie status; farmer knows the fee and past reliability. Both are aware of the free‑riding incentive.
- **Outcomes:** Transformer capacity, reliability, fee payment, staff effort, free‑riding.
- **Payoffs (ordinal, 0–3):**  
  - (Accept, Invest): Farmer 2, Staff 2 (both contribute, moderate net benefit).  
  - (Accept, Not): Farmer 0, Staff 3 (farmer pays but no improvement, staff gains fee without effort).  
  - (Reject, Invest): Farmer 3, Staff 0 (farmer free‑rides, staff loses).  
  - (Reject, Not): Farmer 1, Staff 1 (low capacity, no fees, mediocre outcome).
- **Strategic Tension:** **Public Goods Game (Prisoner’s Dilemma).** Mutual cooperation yields a better collective outcome, but each player has a private incentive to defect: the farmer prefers to reject and free‑ride if staff invests, and the staff prefers not to invest and collect the fee if the farmer accepts. The dominant strategies lead to the inferior (Reject, Not) equilibrium. This is a **strategic** situation.
- **Temporal Structure:** Repeated annually; capacity investments are discrete decisions.
- **Relevant Rules:** Boundary rules restrict the interaction to tied farmer–staff pairs; choice rules reflect the decision to invest or accept; control rules determine how joint actions affect capacity and fee collection.

**Payoff Matrix (Farmer, Staff):**

| Farmer \ Staff | Invest | Not |
|----------------|--------|-----|
| **Accept**     | (2, 2) | (0, 3) |
| **Reject**     | (3, 0) | (1, 1) |

**Compliance with ODD+D:** Matches the description that staff decide whether to invest transformer capacity on behalf of tied farmers, and that farmers’ willingness to accept regularisation is independent and comparatively low. The free‑rider incentive and uneven costs are captured by the payoff structure, reflecting the public goods dilemma inherent in shared infrastructure contribution.

---

### 5. Groundwater Extraction Game (Common Pool Resource)
- **Location:** Shared aquifer accessed by farmers connected to the same transformer area (or wider district basin).
- **Players:** Two representative farmers sharing the aquifer.
- **Roles:** Irrigators extracting groundwater.
- **Actions:**  
  - Each farmer: High extraction (High) or Restrain (Low).
- **Control Rules:**  
  - If both restrain, the aquifer is sustained, pumping costs remain low, and both obtain moderate yields.  
  - If both extract high, the aquifer depletes, future pumping costs rise, and both suffer in the long run despite high immediate yields.  
  - If one extracts high and the other restrains, the high extractor gains a large crop but imposes depletion costs on both; the restrainer suffers from depletion without the high yield.
- **Information:** Farmers sense groundwater depth and pumping costs; they observe neighbours’ extraction behaviour imperfectly. They know the general relationship between aggregate extraction and depletion.
- **Outcomes:** Groundwater level, pumping cost, crop yield, future water availability.
- **Payoffs (ordinal, 0–3):**  
  - (Low, Low): both 3 (sustainable, low cost).  
  - (Low, High) or (High, Low): high extractor 3, restrainer 0.  
  - (High, High): both 1 (depletion, high future costs).
- **Strategic Tension:** **Common Pool Resource Game (Prisoner’s Dilemma).** Each farmer has a dominant strategy to extract high, leading to mutual over‑extraction and depletion, even though mutual restraint would make everyone better off. This is a **strategic** situation.
- **Temporal Structure:** Repeated annually; aquifer dynamics create feedback that shifts the attractiveness of restraint over time.
- **Relevant Rules:** Choice rules allow high or low extraction; control rules link aggregate extraction to aquifer drawdown and pumping costs; the shared aquifer is the common pool.

**Payoff Matrix (Farmer 1, Farmer 2):**

| Farmer 1 \ Farmer 2 | Low   | High  |
|---------------------|-------|-------|
| **Low**             | (3,3) | (0,3) |
| **High**            | (3,0) | (1,1) |

**Compliance with ODD+D:** Reflects the description that farmers choose between pumping at full rate and restraining extraction, that individual high extraction is beneficial in the short run, but aggregate over‑extraction lowers the water table and raises pumping costs. The ordinal payoffs capture the classic CPR dilemma.

---

### 6. Social Learning and Imitation (Capacitor Adoption Diffusion)
- **Location:** Transformer group social network.
- **Players:** Individual farmer (observer) and neighbouring farmers (observed).
- **Roles:** Learner and demonstrators.
- **Actions:**  
  - The observing farmer perceives neighbours’ visible adoption and performance outcomes (voltage quality, pump efficiency).  
  - Based on observed success, the farmer updates their probability of adopting a capacitor in the next cycle.  
  - A small number of “experimenters” are drawn randomly each year regardless of neighbourhood outcomes.  
  - Once a transformer’s adoption count jumps by a threshold within a single cycle, the wider imitation pool opens, making other farmers independently eligible to imitate with a fixed annual probability.
- **Control Rules:**  
  - Observation is local and may be erroneous (misattribution of causes).  
  - Imitation probability depends on the number of successful coordinated adoptions observed.  
  - Experimentation injects stochastic variation.
- **Information:** Farmers sense neighbours’ adoption status and perceived outcomes; they do not have perfect technical knowledge, leading to possible misinterpretation of voltage improvements.
- **Outcomes:** Changes in individual adoption probability, diffusion patterns, eventual capacitor adoption rates.
- **Payoffs:** Not applicable as a strategic game; this is a non‑strategic sequential process of belief updating and behavioural change.
- **Strategic Tension:** **Non‑strategic.** No simultaneous interdependent choices; it is a learning and imitation process under uncertainty.
- **Temporal Structure:** Occurs annually, with memory of past outcomes.
- **Relevant Rules:** Choice rules for adoption are influenced by this learning process; information rules define what is observable; the process is part of the broader DSM coordination mechanism.

**Compliance with ODD+D:** Directly follows the model’s description of social learning: farmers observe neighbours’ capacitor outcomes, imitate successful peers, and are subject to experimentation. The process is explicitly non‑strategic and sequential.

---

### Analysis of Strategic Core and Diversity

- **DSM Coordination Game:** Assurance game – two symmetric farmers must coordinate to achieve a Pareto‑superior outcome; risk of unilateral investment.
- **Authorization Game:** Asymmetric coordination/trust – farmer and staff must align on formal connection; farmer risks loss if staff withholds.
- **Collusion Exchange Game:** Trust game (social dilemma) – farmer’s trust can be exploited by staff; dominant strategy for staff leads to inferior equilibrium.
- **Capacity Provision Game:** Public goods / Prisoner’s Dilemma – asymmetric players face free‑riding incentives; mutual defection is the unique Nash equilibrium.
- **Groundwater Extraction Game:** Common pool resource / Prisoner’s Dilemma – symmetric farmers over‑extract despite collective interest in restraint.
- **Social Learning:** Non‑strategic sequential process – no simultaneous interdependent payoffs.

The five strategic games cover **assurance**, **coordination with asymmetric risk**, **trust dilemma**, **public goods (asymmetric PD)**, and **common pool resource (symmetric PD)**. Although both the capacity provision and groundwater games are Prisoner’s Dilemmas, they are distinct in their domain (infrastructure contribution vs. resource extraction) and symmetry (asymmetric staff–farmer vs. symmetric farmer–farmer), satisfying the requirement for strategic diversity. No two games share identical player roles, payoff structures, and incentive logic simultaneously.
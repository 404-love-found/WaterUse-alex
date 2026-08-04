# Run 30 — deepseek-ai/DeepSeek-V4-Pro

### 1. Capacitor Adoption Assurance Game (AS1)
**Title:** Capacitor Adoption Assurance Game  
**Tension:** Two farmers sharing a transformer decide whether to install capacitors. Mutual adoption yields the best collective outcome, but unilateral adoption is costly and ineffective, creating a coordination problem where each farmer fears being the only adopter.  
**Matrix (Normal Form):**  
Players: Farmer 1 (row), Farmer 2 (col). Strategies: Adopt (A), Not Adopt (N). Payoffs (ordinal: 4=best, 1=worst):

| Farmer 1 \ Farmer 2 | Adopt | Not Adopt |
|----------------------|-------|-----------|
| Adopt                | 4,4   | 1,3       |
| Not Adopt            | 3,1   | 2,2       |

**Justification:** Explicitly described as AS1 in the ODD+D: “a capacitor-adoption assurance game between two neighbouring farmers… mutual investment yields shared improvement, while unilateral investment yields no added private benefit.”

---

### 2. Capacitor Adoption Sequential Social Learning (AS2)
**Title:** Capacitor Adoption Sequential Social Learning  
**Tension:** Adoption diffuses through a social learning process where a first farmer decides whether to adopt, and a second farmer observes the first’s outcome before deciding. Successful diffusion requires a coordinated trial; if the first adopter fails because the second does not follow, the first farmer is worse off, discouraging future adoption.  
**Sequential Representation (Game Tree):**  
```
Farmer 1
├── Not Adopt → (2,2)
└── Adopt → Farmer 2
    ├── Adopt → (4,4)
    └── Not Adopt → (1,3)
```
Payoffs: (Farmer 1, Farmer 2). Ordinal ranks: 4=best, 1=worst.  
**Justification:** Explicitly described as AS2: “a sequential social-learning process in capacitor adoption in which each farmer observes a peer’s outcome and imitates only if that outcome ranks higher.”

---

### 3. Transformer-Capacity Authorization Dilemma (AS3)
**Title:** Transformer-Capacity Authorization Dilemma  
**Tension:** Two farmers connected to the same transformer can invest in capacity upgrades that improve voltage quality for both, but the costs fall solely on the investor. This creates an asymmetric free‑rider incentive: each prefers the other to invest, leading to under‑provision of shared infrastructure.  
**Matrix (Normal Form):**  
Players: Farmer A (Authorizer, higher cost), Farmer B (Beneficiary, lower cost). Strategies: Invest (I), Not Invest (N). Payoffs (ordinal: 4=best, 1=worst):

| Farmer A \ Farmer B | Invest | Not Invest |
|---------------------|--------|------------|
| Invest              | 3,4    | 1,4        |
| Not Invest          | 4,1    | 2,2        |

*Asymmetry:* Farmer A’s payoff from mutual investment is lower due to higher cost; Farmer B’s payoff from unilateral investment is worse than Farmer A’s.  
**Justification:** Explicitly described as AS3: “an asymmetric transformer-capacity authorization dilemma between two farmers: one farmer’s authorization or investment benefits both… costs fall solely on the authorizer.”

---

### 4. Farmer–Staff Mutual Exchange Coordination (AS4)
**Title:** Farmer–Staff Mutual Exchange Coordination  
**Tension:** A farmer and a sub‑station staff member can both engage in informal exchange (e.g., tolerance of unauthorized use for reciprocal favours). Mutual exchange benefits both, but unilateral cooperation is costly—if one offers exchange and the other defects, the cooperator loses while the defector gains. This is a coordination problem requiring matched expectations.  
**Matrix (Normal Form):**  
Players: Farmer (row), Staff (col). Strategies: Exchange (E), Not Exchange (N). Payoffs (ordinal: 4=best, 1=worst):

| Farmer \ Staff | Exchange | Not Exchange |
|----------------|----------|--------------|
| Exchange       | 4,4      | 1,3          |
| Not Exchange   | 3,1      | 2,2          |

**Justification:** Explicitly described as AS4: “a mutual-exchange coordination game between a farmer and sub-station staff in which reciprocal benefit arises only when both engage… if either abstains while the other offers exchange, the offerer bears a loss.”

---

### 5. Authorization and Investment Asymmetric Coordination (AS5)
**Title:** Authorization and Investment Asymmetric Coordination  
**Tension:** A farmer decides whether to request a formal (legal) or informal (illegal) electricity connection; the staff decides whether to invest effort in capacity/maintenance or withhold it. Formal cooperation is collectively optimal, but individual incentives are misaligned: the farmer can gain by avoiding formal fees, while the staff can save effort by withholding investment.  
**Matrix (Normal Form):**  
Players: Farmer (row), Staff (col). Strategies: Farmer: Formal (F), Informal (I); Staff: Invest (I), Withhold (W). Payoffs (ordinal: 4=best, 1=worst):

| Farmer \ Staff | Invest | Withhold |
|----------------|--------|-----------|
| Formal (F)    | 3,3    | 1,4       |
| Informal (I)  | 4,1    | 2,2       |

**Justification:** Explicitly described as AS5: “an authorization-and-investment asymmetric coordination game… mutual formal cooperation is collectively optimal, but if the farmer makes a formal request and the staff withhold, the farmer incurs a loss while the staff save effort.”

---

### 6. Groundwater Extraction Prisoner’s Dilemma (AS6)
**Title:** Groundwater Extraction Prisoner’s Dilemma  
**Tension:** Two farmers drawing from the same aquifer decide whether to restrain extraction or over‑extract. Mutual restraint sustains the resource, but unilateral over‑extraction yields a short‑term private gain while imposing depletion costs on both. Individual rationality leads to mutual over‑extraction and a collectively worse outcome.  
**Matrix (Normal Form):**  
Players: Farmer 1 (row), Farmer 2 (col). Strategies: Restrain (R), Over‑extract (O). Payoffs (ordinal: 4=best, 1=worst):

| Farmer 1 \ Farmer 2 | Restrain | Over‑extract |
|----------------------|----------|--------------|
| Restrain             | 3,3      | 1,4          |
| Over‑extract         | 4,1      | 2,2          |

**Justification:** Explicitly described as AS6: “a groundwater-extraction prisoner’s dilemma between two farmers drawing from the same aquifer, where mutual restraint sustains yields but unilateral over‑extraction offers short‑term gain.”
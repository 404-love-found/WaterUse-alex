# Single test - deepseek-ai/DeepSeek-V4-Pro

### 1. Queue Order Compliance
**Tension:** Two users waiting for a charger must each decide whether to follow the posted queue order or jump ahead. Individual queue-jumping provides immediate benefit but erodes collective fairness and increases overall waiting time when others do the same.

**2‑Player Normal Form Payoff Matrix** (Player 1 \ Player 2)

| Player 1 \ Player 2 | Follow Queue | Jump Queue |
|----------------------|--------------|------------|
| Follow Queue         | (3,3)        | (1,4)      |
| Jump Queue           | (4,1)        | (2,2)      |

**Justification:** This is a social dilemma with a temptation to defect (jump) that, if mutual, leaves both worse off than if they had both followed the queue. It captures the core queue‑fairness tension.

---

### 2. Post‑Charging Move‑out (Charger Release)
**Tension:** After a charging session is complete, the current occupant decides whether to move promptly or overstay and block the bay. The next waiting user decides whether to wait silently or complain.

**2‑Player Normal Form Payoff Matrix** (Occupant \ Next User)

| Occupant \ Next User | Wait | Complain |
|----------------------|------|-----------|
| Move Promptly        | (3,3) | (2,2)    |
| Overstay             | (4,1) | (1,2)    |

**Justification:** The occupant gains by overstaying unless the next user complains, which may trigger penalties. This represents the tension over charger occupation and the decision to enforce move‑out norms.

---

### 3. Rule Enforcement
**Tension:** Parking staff decide how strictly to enforce queue and move‑out rules; users decide whether to comply or violate.

**2‑Player Normal Form Payoff Matrix** (Staff \ User)

| Staff \ User | Comply | Violate |
|--------------|--------|---------|
| Enforce      | (2,2)  | (3,1)   |
| Not Enforce  | (4,3)  | (1,4)   |

**Justification:** A classic inspection game. Staff prefer to save effort when users comply, but must enforce when violations occur to avoid complaints. Users prefer to violate only when enforcement is lax.

---

### 4. Informal Priority Request
**Tension:** A resident may ask staff for an informal favour (e.g., holding a bay); staff decide whether to grant it, balancing relationship‑building against undermining formal rules.

**2‑Player Normal Form Payoff Matrix** (Resident \ Staff)

| Resident \ Staff | Grant Favor | Deny Favor |
|------------------|-------------|-------------|
| Request Favor    | (4,2)       | (1,3)       |
| Use Formal Queue | (3,3)       | (3,4)       |

**Justification:** Captures the tension between informal governance through personal favours and adherence to the posted queue. Favours can increase individual convenience but weaken overall rule legitimacy.

---

### 5. Resident vs Non‑resident Priority Claim
**Tension:** When a charger becomes available, a resident and a non‑resident both want it. Each can assert priority or yield, influenced by the resident discount and perceived entitlement.

**2‑Player Normal Form Payoff Matrix** (Resident \ Non‑resident)

| Resident \ Non‑resident | Assert | Yield |
|------------------------|--------|-------|
| Assert                 | (1,1)  | (4,2) |
| Yield                  | (2,4)  | (3,3) |

**Justification:** A Hawk‑Dove (Chicken) game illustrating the conflict over charger access. Mutual assertion leads to conflict and delay; mutual yielding is fair but slow; asymmetric assertion gives the assertive player immediate access.

---

### 6. Violation Reporting
**Tension:** A user observes a rule violation (e.g., overstay, queue jump) and decides whether to report it. The violator decides whether to violate, knowing that reporting may lead to penalties.

**2‑Player Normal Form Payoff Matrix** (Violator \ Observer)

| Violator \ Observer | Report | Ignore |
|---------------------|--------|--------|
| Comply              | (2,2)  | (3,3)  |
| Violate             | (1,3)  | (4,1)  |

**Justification:** The observer’s willingness to report affects the violator’s calculus. Reporting can deter violations but costs effort; ignoring saves effort but allows unfairness to persist.

---

### 7. Capacity Expansion Contribution
**Tension:** Residents must decide whether to support (and pay for) additional chargers or oppose expansion, hoping others will bear the cost.

**2‑Player Normal Form Payoff Matrix** (Resident 1 \ Resident 2)

| Resident 1 \ Resident 2 | Support | Oppose |
|-------------------------|---------|--------|
| Support                 | (3,3)   | (2,4)  |
| Oppose                  | (4,2)   | (1,1)  |

**Justification:** A public‑goods dilemma. The collectively optimal outcome (both support) provides shared benefits, but each resident has an incentive to free‑ride. If both oppose, no expansion occurs and congestion worsens.

---

### 8. Maintenance Responsiveness
**Tension:** When a charger is faulty, staff decide how quickly to repair it; users decide whether to report the fault or wait silently.

**2‑Player Normal Form Payoff Matrix** (Staff \ User)

| Staff \ User | Report Fault | Not Report |
|---------------|--------------|-------------|
| Repair Quickly | (2,2)        | (3,3)       |
| Delay Repair   | (1,2)        | (4,1)       |

**Justification:** Staff prefer to delay repairs to save effort, but risk complaints and loss of trust. Users benefit from quick repairs but may not report faults if they expect staff inaction.

---

### 9. Off‑Peak Charging Coordination
**Tension:** Users decide whether to charge during peak or off‑peak hours. Shifting to off‑peak reduces congestion, but each user prefers to charge at peak while others shift away.

**2‑Player Normal Form Payoff Matrix** (User 1 \ User 2)

| User 1 \ User 2 | Off‑Peak | Peak |
|------------------|----------|------|
| Off‑Peak         | (3,3)    | (2,4)|
| Peak             | (4,2)    | (1,1)|

**Justification:** A coordination problem with a temptation to stay on peak while others move to off‑peak. If both stay on peak, congestion is worst; mutual off‑peak is better but requires collective behaviour change.
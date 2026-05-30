# Run 18 - deepseek-ai/DeepSeek-V4-Pro

**Queue Order Compliance**
- **Tension**: Users can comply with the posted queue order or skip ahead. Skipping gives individual time savings but undermines collective trust in the queue. If both skip, the queue collapses into disorder.
- **Matrix** (Player 1, Player 2):
  ```
              Comply    Skip
  Comply     (3,3)    (1,4)
  Skip       (4,1)    (2,2)
  ```
- **Justification**: The ODD highlights that “users compete for fair queue access” and that “if queue skipping … was tolerated, some users become more likely to attempt similar behaviour.” This prisoner’s dilemma captures the tension between individual gain and collective order.

**Post‑Charging Bay Release**
- **Tension**: After useful charging ends, a user may move promptly or overstay. Prompt moving frees the charger for the next user; overstaying gives personal convenience but blocks others. If many overstay, charger utilisation collapses.
- **Matrix** (Player 1, Player 2):
  ```
              Move    Overstay
  Move       (3,3)    (1,4)
  Overstay   (4,1)    (2,2)
  ```
- **Justification**: The ODD notes that “a vehicle that remains connected after useful charging may block the bay” and that “one user's … move‑out decision affect the next user's access.” This PD represents the dilemma of bay release.

**Rule Enforcement**
- **Tension**: Staff can enforce posted rules (costly effort) or not enforce. Users can comply or violate. Staff prefers low effort but faces complaints if violations occur; users prefer convenience but risk penalties. The strategic interdependence determines whether rules are credible.
- **Matrix** (Staff, User):
  ```
              Comply   Violate
  Enforce     (3,3)    (2,1)
  Not Enforce (4,2)    (1,4)
  ```
- **Justification**: The ODD states “Staff compare the cost of intervention with complaint risk … Users … compare … perceived enforcement.” This mixed‑motive game captures the credibility of enforcement.

**Violation Reporting**
- **Tension**: Users who observe a queue violation or overstay can report it (complain) or remain silent. Reporting is a public good that deters future violations, but it is individually costly. If no one reports, violations proliferate.
- **Matrix** (User A, User B):
  ```
              Report   Not Report
  Report      (2,2)    (1,3)
  Not Report  (3,1)    (1,1)
  ```
- **Justification**: The ODD includes “complaint procedures” and “complaint and legitimacy feedback.” This PD shows the tension between individual free‑riding and collective enforcement.

**Resident vs Non‑resident Charger Access**
- **Tension**: A resident and a non‑resident arrive simultaneously at the last available charger. The resident may feel entitled to priority due to the resident discount; the non‑resident expects equal treatment. Both can assert their claim or defer, creating a hawk‑dove conflict over a scarce resource.
- **Matrix** (Resident, Non‑resident):
  ```
              Assert   Defer
  Assert     (1,1)    (4,2)
  Defer      (2,3)    (3,3)
  ```
- **Justification**: The ODD notes “Residents know they receive a lower per‑kWh price and may expect stronger entitlement … Non‑residents … may expect equal queue treatment.” This asymmetric hawk‑dove game captures the clash of informal norms.

**Off‑Peak Charging Coordination**
- **Tension**: Users can shift charging to off‑peak hours (inconvenient but reduces congestion) or stay at peak hours. If both shift, congestion is low; if one shifts, the other enjoys low peak congestion without inconvenience. Mutual shifting is collectively better but individually tempting to stay.
- **Matrix** (User A, User B):
  ```
            Off    Peak
  Off     (3,3)   (1,4)
  Peak    (4,1)   (2,2)
  ```
- **Justification**: The ODD mentions “charge during off‑peak periods” and that users adapt based on past experience. This PD represents the coordination problem of shifting demand.

**Staff Favoritism**
- **Tension**: A resident can request informal priority from staff, and staff can grant or deny the favor. Granting favors builds personal relationships but undermines formal fairness. Denying favors maintains order but may disappoint residents.
- **Matrix** (Staff, Resident):
  ```
               Request   Not Request
  Grant        (3,4)      (2,2)
  Deny         (2,1)      (4,3)
  ```
- **Justification**: The ODD describes “informal requests,” “tolerance of informal requests,” and that “informal relationships can … undermine queue fairness.” This coordination game captures the tension between formal rules and informal ties.

**Maintenance Reporting**
- **Tension**: Users who encounter a faulty charger can report it or not. Reporting is a public good that restores capacity, but it costs individual effort. If both free‑ride, the fault persists and waiting times increase.
- **Matrix** (User A, User B):
  ```
              Report   Not Report
  Report      (2,2)    (1,3)
  Not Report  (3,1)    (1,1)
  ```
- **Justification**: The ODD notes “Maintenance and charger reliability: Faults reduce available charging capacity … Delayed repair increases waiting time.” This PD captures the public‑good dilemma of reporting faults.

**Capacity Expansion Lobbying**
- **Tension**: Users can lobby management to install additional chargers. Lobbying is costly but can lead to expansion, a public good that benefits all users. If no one lobbies, the facility remains congested.
- **Matrix** (User A, User B):
  ```
              Lobby   Not Lobby
  Lobby      (2,2)    (1,3)
  Not Lobby  (3,1)    (1,1)
  ```
- **Justification**: The ODD includes “Capacity planning: Management may evaluate whether to add chargers … based on demand, complaints.” This PD represents the collective action problem of lobbying for expansion.

**Reservation vs. Walk‑up**
- **Tension**: Users can reserve a slot in advance (guaranteeing access but requiring planning) or walk up spontaneously (flexible but risky). If both walk up, they compete and wait longer; if both reserve, the system is orderly; if one reserves and the other walks up, the reserver gets priority.
- **Matrix** (User A, User B):
  ```
              Reserve   Walk-up
  Reserve     (3,3)     (1,4)
  Walk-up     (4,1)     (2,2)
  ```
- **Justification**: The ODD describes “reservation rules” and that users “decide whether to reserve a slot, join the live queue, arrive without reservation.” This PD captures the tension between individual flexibility and collective order.
# Run 23 — Qwen/Qwen3.7-Plus

[
  {
    "Title": "Capacitor Adoption Assurance Game",
    "Tension": "Coordination/Assurance dilemma where mutual investment in voltage-stabilizing equipment yields shared reliability improvements, but unilateral investment is risky and yields no added private benefit if the neighbor does not adopt.",
    "Representation": "| | Adopt | Not Adopt |\n|---|---|---|\n| **Adopt** | 3, 3 | 1, 1 |\n| **Not Adopt** | 1, 1 | 2, 2 |",
    "Justification": "Reflects the assurance game structure where mutual cooperation is Pareto-dominant, but the risk of unilateral defection (wasted investment without voltage improvement) makes coordination essential among farmers sharing a transformer."
  },
  {
    "Title": "Sequential Social-Learning in Capacitor Adoption",
    "Tension": "Bounded rationality and path-dependent diffusion where a late-adopting farmer must decide whether to imitate an early-adopting neighbor based on observed, potentially misattributed, outcomes.",
    "Representation": "Farmer 1: [Adopt | Not Adopt]\n-> If Adopt: Nature [Success (p) | Fail (1-p)]\n   -> If Success: Farmer 2 [Imitate (3,3) | Not Imitate (2,2)]\n   -> If Fail: Farmer 2 [Imitate (1,1) | Not Imitate (2,2)]\n-> If Not Adopt: Farmer 2 [Imitate (1,1) | Not Imitate (2,2)]",
    "Justification": "Captures the sequential social learning process where diffusion only occurs after a successful coordinated trial is observed, and misattribution of failure can block efficient technology adoption."
  },
  {
    "Title": "Asymmetric Transformer-Capacity Authorization Dilemma",
    "Tension": "Free-rider dilemma in infrastructure investment where one farmer's authorization or capacity upgrade benefits all connected farmers, but the private costs fall solely on the contributor.",
    "Representation": "| | Contribute | Not Contribute |\n|---|---|---|\n| **Contribute** | 3, 3 | 1, 4 |\n| **Not Contribute** | 4, 1 | 2, 2 |",
    "Justification": "Models the asymmetric interdependence in transformer upgrades. Mutual contribution is optimal, but unilateral contribution creates a spillover benefit, incentivizing free-riding and leading to under-investment."
  },
  {
    "Title": "Mutual-Exchange Coordination Game",
    "Tension": "Coordination of informal exchange where reciprocal benefits between a farmer and sub-station staff only materialize if both engage; mismatched expectations result in losses for the cooperating party.",
    "Representation": "| | Accept Exchange | Abstain/Enforce |\n|---|---|---|\n| **Offer Exchange** | 3, 3 | 1, 2 |\n| **Abstain** | 2, 1 | 2, 2 |",
    "Justification": "Represents relational governance and collusion dynamics. Mutual informal exchange yields reciprocal gains, but unilateral offers risk penalties or wasted effort, making trust and matched expectations critical."
  },
  {
    "Title": "Authorization-and-Investment Asymmetric Coordination",
    "Tension": "Asymmetric coordination between formal legality and informal opportunism, where mutual formal cooperation is collectively optimal but burdens staff, while informal requests exploit staff investment.",
    "Representation": "| | Invest/Authorize | Withhold |\n|---|---|---|\n| **Formal Request** | 3, 2 | 1, 3 |\n| **Informal Request** | 4, 1 | 2, 3 |",
    "Justification": "Captures the strategic tension between formal compliance and informal opportunism. Farmers prefer informal access to avoid fees, while staff prefer to withhold effort, creating asymmetric incentives that can undermine formal grid planning."
  },
  {
    "Title": "Groundwater-Extraction Prisoner’s Dilemma",
    "Tension": "Common-pool resource extraction where individual over-extraction provides short-term irrigation benefits but accelerates aquifer depletion, increasing future pumping costs and grid stress for all.",
    "Representation": "| | Restrain | Over-extract |\n|---|---|---|\n| **Restrain** | 3, 3 | 1, 4 |\n| **Over-extract** | 4, 1 | 2, 2 |",
    "Justification": "Classic prisoner's dilemma applied to the shared aquifer. Individual rationality drives over-extraction, but mutual over-extraction leads to long-term degradation of both groundwater and electricity reliability."
  }
]
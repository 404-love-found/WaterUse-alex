# Run 19 — Qwen/Qwen3.7-Plus

[
  {
    "title": "Coordinated Capacitor Adoption",
    "tension": "Assurance/Coordination dilemma where unilateral investment in voltage stabilization yields no return due to threshold-dependent benefits and bounded rationality.",
    "representation": "Normal Form (Farmer 1 vs Farmer 2): Strategies [Invest, Not Invest]. Payoffs: (Invest, Invest)=(B-C, B-C); (Invest, Not)=(-C, 0); (Not, Invest)=(0, -C); (Not, Not)=(0, 0). Condition: B > C > 0.",
    "justification": "Reflects the mechanism where capacitor benefits require coordinated adoption on the same transformer. Unilateral adoption is unattractive because benefits spill over and may be misattributed, creating a threshold-dependent assurance game."
  },
  {
    "title": "Transformer Capacity Contribution",
    "tension": "Free-rider/Public Goods dilemma where capacity upgrades confer collective reliability benefits but impose uneven private costs on contributors.",
    "representation": "Normal Form (Farmer 1 vs Farmer 2): Strategies [Contribute, Free-ride]. Payoffs: (Contribute, Contribute)=(B-C, B-C); (Contribute, Free-ride)=(B-C, B); (Free-ride, Contribute)=(B, B-C); (Free-ride, Free-ride)=(0, 0). Condition: B > B-C > 0.",
    "justification": "Captures the asymmetric interdependence of transformer upgrades. When one farmer pays for authorization or capacity, all connected farmers benefit from improved voltage quality, making free-riding the dominant individual strategy despite collective suboptimality."
  },
  {
    "title": "Connection Authorization and Enforcement",
    "tension": "Coordination/Trust dilemma where mismatched expectations between farmer connection choices and staff enforcement lead to suboptimal outcomes or penalties.",
    "representation": "Normal Form (Farmer vs Staff): Farmer [Formal, Informal] x Staff [Enforce, Tolerate]. Payoffs: (Formal, Enforce)=(1, 1); (Formal, Tolerate)=(2, 0); (Informal, Enforce)=(-1, 2); (Informal, Tolerate)=(3, 3).",
    "justification": "Models the mutual dependence of formal compliance and informal reciprocity. Mutual informal exchange yields the highest payoff if undetected, but if the farmer chooses informal and the staff enforces, the farmer suffers a penalty, highlighting the risk of mismatched expectations."
  },
  {
    "title": "Groundwater Extraction",
    "tension": "Tragedy of the Commons/Prisoner's Dilemma where individual short-term pumping benefits are outweighed by long-term aquifer depletion and increased energy costs.",
    "representation": "Normal Form (Farmer 1 vs Farmer 2): Strategies [Restrain, Full Pump]. Payoffs: (Restrain, Restrain)=(R, R); (Restrain, Full)=(S, T); (Full, Restrain)=(T, S); (Full, Full)=(P, P). Condition: T > R > P > S.",
    "justification": "Represents the endogenous feedback of aquifer drawdown. Individual high extraction dominates in the short run, but mutual high extraction accelerates depletion, raising future pumping costs and worsening grid stress."
  },
  {
    "title": "Staff Maintenance and Oversight",
    "tension": "Inspection/Shirking dilemma where staff balance the effort costs of grid maintenance against the reputational risk and sanctions of inaction under regulatory monitoring.",
    "representation": "Normal Form (Staff vs Regulator): Staff [Maintain, Shirk] x Regulator [Monitor, Ignore]. Payoffs: (Maintain, Monitor)=(-C, -M); (Maintain, Ignore)=(-C, 0); (Shirk, Monitor)=(-S, R); (Shirk, Ignore)=(0, 0).",
    "justification": "Illustrates the staff's trade-off between saving effort and facing sanctions. Staff adapt their enforcement and maintenance effort conditionally based on the exogenous, stochastic monitoring intensity and oversight risk from the regulator."
  },
  {
    "title": "Sequential Collusion Tie Formation",
    "tension": "Sequential trust/reciprocity dilemma where informal exchanges only stabilize when both farmer willingness and staff willingness align without detection.",
    "representation": "Sequential Game Tree: 1. Farmer: [Offer Informal, Not Offer]. 2. If Not Offer -> (0, 0). 3. If Offer Informal -> Staff: [Accept/Reciprocate, Reject/Enforce]. 4. If Accept -> (Benefit, Benefit). 5. If Reject -> (-Loss, Enforcement_Gain).",
    "justification": "Captures the sequential formation of collusive ties. A tie forms only where offers agree, moderated by the farmer's financial strain, the staff's corruption level, and the local risk of detection, making it a sequential game of trust."
  }
]
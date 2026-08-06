from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import evaluate_tp_fp_fn_compare as evaluator


class WaterEvaluatorRegressionTests(unittest.TestCase):
    def extract(self, response: str) -> list[evaluator.ActionSituation]:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "run_01.md"
            path.write_text(response, encoding="utf-8")
            return evaluator.extract_action_situations(path)

    def test_two_heading_action_situations_are_extracted(self) -> None:
        response = """# Run 1 - test/model

## Action Situation 1: Upstream-Downstream Withdrawal Decisions
Tension: Farmers at different river positions choose low or high withdrawals.
Payoff Matrix: 2x2.

## Action Situation 2: Lake Fishing Harvest Coordination Game
Tension: Farmers choose sustainable or aggressive catches from a common-pool fish stock.
Payoff Matrix: 2x2.
"""
        situations = self.extract(response)

        self.assertEqual(2, len(situations))
        self.assertEqual("AS1", evaluator.classify_against_correct_set(situations[0]))
        self.assertEqual("AS2", evaluator.classify_against_correct_set(situations[1]))

    def test_markdown_action_situation_table_is_extracted(self) -> None:
        response = """# Run 1 - test/model

| # | Title | Strategic tension | Representation |
|---|-------|-------------------|----------------|
| 1 | Upstream-Downstream Withdrawal Decisions | Spatial water rivalry | Payoff matrix |
| 2 | Fish Extraction Common-Pool Resource Game | Sustainable catch vs overharvest | Payoff matrix |
"""
        situations = self.extract(response)

        self.assertEqual(2, len(situations))
        self.assertEqual("AS1", evaluator.classify_against_correct_set(situations[0]))
        self.assertEqual("AS2", evaluator.classify_against_correct_set(situations[1]))

    def test_json_action_situations_are_extracted(self) -> None:
        response = '''# Run 1 - test/model

{
  "action_situations": [
    {
      "title": "Upstream and Downstream Water Withdrawal",
      "tension": "Upstream and downstream farmers compete for irrigation water",
      "representation": "Payoff matrix"
    },
    {
      "title": "Fish Extraction Common-Pool Resource Game",
      "tension": "Farmers choose sustainable catch or overharvest the shared fish stock",
      "representation": "Payoff matrix"
    }
  ]
}
'''
        situations = self.extract(response)

        self.assertEqual(2, len(situations))
        self.assertEqual("AS1", evaluator.classify_against_correct_set(situations[0]))
        self.assertEqual("AS2", evaluator.classify_against_correct_set(situations[1]))

    def test_body_reference_to_authority_does_not_reject_decentralized_water_as(self) -> None:
        situation = evaluator.ActionSituation(
            title="Upstream-Downstream Withdrawal Decisions",
            block=(
                "In the decentralized case, upstream and downstream farmers forecast local flow and choose "
                "irrigation withdrawals rather than relying on the National Authority. Payoff matrix."
            ),
            line_no=1,
            has_payoff_evidence=True,
        )
        self.assertEqual("AS1", evaluator.classify_against_correct_set(situation))

    def test_explicitly_centralized_title_is_rejected(self) -> None:
        situation = evaluator.ActionSituation(
            title="Centralized National Authority Allocation Game",
            block="The authority allocates fields to representative farmers. Payoff matrix.",
            line_no=1,
            has_payoff_evidence=True,
        )
        self.assertIsNone(evaluator.classify_against_correct_set(situation))

    def test_fish_reproduction_threshold_is_not_fish_extraction(self) -> None:
        situation = evaluator.ActionSituation(
            title="Fish Reproduction Threshold Game",
            block="Farmers delay May irrigation so larvae can migrate when lake inflow crosses a threshold. Matrix.",
            line_no=1,
            has_payoff_evidence=True,
        )
        self.assertIsNone(evaluator.classify_against_correct_set(situation))

    def test_model_assigned_number_does_not_override_semantics(self) -> None:
        situation = evaluator.ActionSituation(
            title="AS1: Fish Extraction Common-Pool Resource Game",
            block="Farmers choose catch levels and can overharvest the shared fish stock. Matrix.",
            line_no=1,
            has_payoff_evidence=True,
        )
        self.assertEqual("AS2", evaluator.classify_against_correct_set(situation))

    def test_risk_taking_title_is_not_rescued_by_incidental_fish_and_water_text(self) -> None:
        situation = evaluator.ActionSituation(
            title="Bounded Rationality and Income Threshold Risk Dilemma",
            block=(
                "Upstream and downstream farmers choose safe or risky field expansion. "
                "The downstream budget includes fish catch, while both may experience water stress. Payoff matrix."
            ),
            line_no=1,
            has_payoff_evidence=True,
        )
        self.assertIsNone(evaluator.classify_against_correct_set(situation))

    def test_cross_resource_water_vs_fish_game_matches_neither_ground_truth_as(self) -> None:
        situation = evaluator.ActionSituation(
            title="Upstream Water Extraction vs Downstream Fish Harvest",
            block=(
                "The upstream farmer chooses irrigation extraction while the downstream farmer chooses fishing effort. "
                "Their choices affect lake inflow and catch. Payoff matrix."
            ),
            line_no=1,
            has_payoff_evidence=True,
        )
        self.assertIsNone(evaluator.classify_against_correct_set(situation))

    def test_ecological_flow_game_is_not_fish_extraction(self) -> None:
        situation = evaluator.ActionSituation(
            title="Ecological Threshold and Fishery Collapse Dilemma",
            block=(
                "Upstream and downstream farmers choose whether to maintain environmental flow or irrigate fields. "
                "Larval recruitment fails below the lake-inflow threshold. Payoff matrix."
            ),
            line_no=1,
            has_payoff_evidence=True,
        )
        self.assertIsNone(evaluator.classify_against_correct_set(situation))

    def test_generic_fishery_title_does_not_hide_cross_resource_actions(self) -> None:
        situation = evaluator.ActionSituation(
            title="Ecological Threshold and Fishery Collapse Dilemma",
            block="""Upstream farmers control lake inflow while downstream farmers set fishing effort.
| Upstream / Downstream | Sustainable Catch | Target Catch |
|---|---|---|
| Conserve Water | (3,4) | (3,1) |
| Extract Water | (4,0) | (4,0) |
""",
            line_no=1,
            has_payoff_evidence=True,
        )
        self.assertIsNone(evaluator.classify_against_correct_set(situation))

    def test_cross_resource_axes_with_implicit_water_extraction_are_rejected(self) -> None:
        situation = evaluator.ActionSituation(
            title="Ecological Threshold and Fishery Dilemma",
            block="""Upstream farmers' irrigation decisions control lake inflow. Downstream farmers choose fishing effort.
| Upstream / Downstream | Over-extract | Conserve |
|---|---|---|
| High Fishing Effort | (4,1) | (3,4) |
| Low Fishing Effort | (4,2) | (3,3) |
""",
            line_no=1,
            has_payoff_evidence=True,
        )
        self.assertIsNone(evaluator.classify_against_correct_set(situation))

    def test_fishery_collapse_title_with_two_farmer_harvest_choices_matches_as2(self) -> None:
        situation = evaluator.ActionSituation(
            title="Fishery Collapse Dilemma",
            block=(
                "Upstream and downstream farmers each choose a low or high catch. "
                "Aggressive harvest by both depletes the common fish stock. Payoff matrix."
            ),
            line_no=1,
            has_payoff_evidence=True,
        )
        self.assertEqual("AS2", evaluator.classify_against_correct_set(situation))

    def test_two_fishers_or_numbered_downstream_farmers_are_valid_resource_users(self) -> None:
        situations = (
            evaluator.ActionSituation(
                title="Fishery Threshold Dilemma",
                block="Fisher A and Fisher B choose sustainable harvest or overharvest of the shared stock. Matrix.",
                line_no=1,
                has_payoff_evidence=True,
            ),
            evaluator.ActionSituation(
                title="Spatial Priority Access Fishing Dilemma",
                block=(
                    "Downstream Farmer 1 and Downstream Farmer 2 choose low or high catch from the common pool. "
                    "Payoff matrix."
                ),
                line_no=1,
                has_payoff_evidence=True,
            ),
        )
        for situation in situations:
            with self.subTest(title=situation.title):
                self.assertEqual("AS2", evaluator.classify_against_correct_set(situation))

    def test_aggressive_fishing_is_not_mistaken_for_agricultural_action(self) -> None:
        situation = evaluator.ActionSituation(
            title="Fishing-Access Conflict (Downstream vs Upstream)",
            block="""Both farmers choose low catch or aggressive high catch.
| Downstream / Upstream | Low Catch | Aggressive Catch |
|---|---|---|
| Low Catch | (4,4) | (2,5) |
| Aggressive Catch | (5,2) | (1,1) |
""",
            line_no=1,
            has_payoff_evidence=True,
        )
        self.assertFalse(evaluator.is_cross_resource_water_fish_game(situation.block))
        self.assertEqual("AS2", evaluator.classify_against_correct_set(situation))

    def test_moderate_vs_maximum_catch_is_a_fish_extraction_choice(self) -> None:
        situation = evaluator.ActionSituation(
            title="Fishing-Priority Conflict",
            block=(
                "Upstream and downstream farmers choose moderate catch or maximum catch from the lake. "
                "Payoff matrix."
            ),
            line_no=1,
            has_payoff_evidence=True,
        )
        self.assertEqual("AS2", evaluator.classify_against_correct_set(situation))

    def test_farmer_vs_nature_field_expansion_is_not_as1(self) -> None:
        situation = evaluator.ActionSituation(
            title="Farmer vs Nature: Field Expansion under Uncertain Inflow",
            block="A farmer chooses expand or hold; nature supplies high or low water. Payoff matrix.",
            line_no=1,
            has_payoff_evidence=True,
        )
        self.assertIsNone(evaluator.classify_against_correct_set(situation))

    def test_internal_fields_and_game_tree_steps_are_not_as_starts(self) -> None:
        lines = (
            "**8. Outcomes:** Water delivered and crop yield.",
            "10. **Strategic Tension:** Upstream farmers can reduce downstream flow.",
            "1. **Farmer chooses: High or Low Withdrawal**",
            "## Step 2 - Downstream farmer responds",
            "### Normal-form payoff matrix (Upstream rows, Downstream columns)",
        )
        for line in lines:
            with self.subTest(line=line):
                self.assertFalse(evaluator.is_candidate_start(line))

    def test_wrong_irrigation_expansion_heading_still_starts_a_separate_as(self) -> None:
        self.assertTrue(
            evaluator.is_candidate_start("## 3. Risk-Taking vs Risk-Averse Irrigation under Uncertain Flow")
        )

    def test_payoff_matrix_table_is_not_an_as_table(self) -> None:
        lines = [
            "| Upstream / Downstream | Low | High |",
            "|-----------------------|-----|------|",
            "| Low | (3,3) | (1,4) |",
            "| High | (4,1) | (2,2) |",
        ]
        self.assertEqual([], evaluator.extract_table_action_situations(lines))

    def test_unicode_action_situation_headings_and_leading_tables_are_extracted(self) -> None:
        response = """# Run 1 - test/model

## 1. Action‑Situation : **Up‑stream vs. Down‑stream Water Competition**
| U / D | Low | High |
|---|---|---|
| Low | (3,3) | (2,4) |

## 2. Action‑Situation : **Down‑stream vs. Up‑stream Fishing Competition**
| D / U | Low catch | High catch |
|---|---|---|
| Low catch | (3,3) | (2,4) |
"""
        situations = self.extract(response)

        self.assertEqual(2, len(situations))
        self.assertEqual("Up-stream vs. Down-stream Water Competition", situations[0].title)
        self.assertEqual("Down-stream vs. Up-stream Fishing Competition", situations[1].title)
        self.assertTrue(all(situation.has_payoff_evidence for situation in situations))

    def test_lettered_action_situation_headings_are_extracted(self) -> None:
        response = """# Run 1 - test/model

## 1️⃣ Action Situation A - Competing Water Extraction
| U / D | Conserve | Extract |
|---|---|---|
| Conserve | (3,3) | (2,4) |

## 2️⃣ Action Situation B - Fishing-Pressure Competition
| U / D | Low catch | High catch |
|---|---|---|
| Low catch | (3,3) | (2,4) |
"""
        situations = self.extract(response)

        self.assertEqual(
            ["Competing Water Extraction", "Fishing-Pressure Competition"],
            [situation.title for situation in situations],
        )

    def test_document_heading_is_not_used_when_real_as_headings_exist(self) -> None:
        response = """# Run 1 - test/model

**IAD-derived Decentralised Action-Situations (DV only)**

## Action Situation 1: Water-Extraction Competition
Upstream and downstream farmers choose low or high irrigation withdrawals.
| U / D | Low | High |
|---|---|---|
| Low | (3,3) | (2,4) |
"""
        situations = self.extract(response)

        self.assertEqual(1, len(situations))
        self.assertEqual("Water-Extraction Competition", situations[0].title)

    def test_how_action_situations_satisfy_requirements_is_not_an_as(self) -> None:
        self.assertFalse(evaluator.is_candidate_start("## How the Action Situations Satisfy the Requirements"))

    def test_thought_process_candidates_are_not_counted_when_final_games_have_matrices(self) -> None:
        response = """# Run 1 - test/model

## Thought Process
1. **Sequential water access**: upstream farmers withdraw before downstream farmers.
2. **Fish larvae threshold**: irrigation can reduce lake inflow.

## Action Situation 1: Water-Extraction Competition
Upstream and downstream farmers choose low or high withdrawals.
| U / D | Low | High |
|---|---|---|
| Low | (3,3) | (2,4) |

## Action Situation 2: Fishing-Harvest Coordination
Both farmers choose low or high catch from the shared stock.
| U / D | Low | High |
|---|---|---|
| Low | (3,3) | (2,4) |
"""
        situations = self.extract(response)

        self.assertEqual(
            ["Water-Extraction Competition", "Fishing-Harvest Coordination"],
            [situation.title for situation in situations],
        )


if __name__ == "__main__":
    unittest.main()

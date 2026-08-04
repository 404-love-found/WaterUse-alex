from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import evaluate_tp_fp_fn as evaluator


class ElectricityEvaluatorRegressionTests(unittest.TestCase):
    def test_plain_title_lines_start_separate_action_situations(self) -> None:
        response = """# Run 1 — test/model

Title: Capacitor Adoption Coordination among Farmers on a Transformer
Tension: Neighbouring farmers decide whether to adopt capacitors.
Matrix:
| | Adopt | Wait |
|---|---|---|
| Adopt | (3,3) | (0,2) |
| Wait | (2,0) | (1,1) |

Title: Groundwater Extraction Dilemma
Tension: Farmers decide whether to restrain pumping from a shared aquifer.
Matrix:
| | Restrain | Pump |
|---|---|---|
| Restrain | (3,3) | (0,2) |
| Pump | (2,0) | (1,1) |
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "run_01.md"
            path.write_text(response, encoding="utf-8")
            situations = evaluator.extract_action_situations(path)

        self.assertEqual(2, len(situations))
        self.assertEqual("AS1", evaluator.classify_against_correct_set(situations[0]))
        self.assertEqual("AS6", evaluator.classify_against_correct_set(situations[1]))

    def test_contextual_bold_titles_start_separate_action_situations(self) -> None:
        response = """# Run 1 — test/model

**Capacitor Adoption Coordination**
**Tension:** Farmers coordinate adoption.
**Matrix:**
| | Adopt | Wait |
|---|---|---|
| Adopt | (3,3) | (0,2) |
| Wait | (2,0) | (1,1) |

**Groundwater Extraction Restraint**
**Tension:** Farmers share an aquifer.
**Matrix:**
| | Restrain | Pump |
|---|---|---|
| Restrain | (3,3) | (0,2) |
| Pump | (2,0) | (1,1) |
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "run_01.md"
            path.write_text(response, encoding="utf-8")
            situations = evaluator.extract_action_situations(path)

        self.assertEqual(2, len(situations))
        self.assertEqual("AS1", evaluator.classify_against_correct_set(situations[0]))
        self.assertEqual("AS6", evaluator.classify_against_correct_set(situations[1]))

    def test_plain_action_situation_labels_start_separate_blocks(self) -> None:
        response = """# Run 1 — test/model

Action Situation 1: Capacitor Adoption Coordination
Tension: Farmers coordinate adoption.
Matrix:
| | Adopt | Wait |
|---|---|---|
| Adopt | (3,3) | (0,2) |
| Wait | (2,0) | (1,1) |

Action Situation 2: Groundwater Extraction
Tension: Farmers share an aquifer.
Matrix:
| | Restrain | Pump |
|---|---|---|
| Restrain | (3,3) | (0,2) |
| Pump | (2,0) | (1,1) |
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "run_01.md"
            path.write_text(response, encoding="utf-8")
            situations = evaluator.extract_action_situations(path)

        self.assertEqual(2, len(situations))
        self.assertEqual("AS1", evaluator.classify_against_correct_set(situations[0]))
        self.assertEqual("AS6", evaluator.classify_against_correct_set(situations[1]))

    def test_action_situation_table_rows_are_extracted_separately(self) -> None:
        response = """# Run 1 - test/model

| # | Title (AS) | Strategic tension | Representation |
|---|------------|-------------------|----------------|
| 1 | **Capacitor Adoption Assurance Game** | Neighbours coordinate adoption. | Payoff matrix |
| 2 | **Groundwater Extraction Dilemma** | Farmers share an aquifer. | Payoff matrix |
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "run_01.md"
            path.write_text(response, encoding="utf-8")
            situations = evaluator.extract_action_situations(path)

        self.assertEqual(2, len(situations))
        self.assertEqual("AS1", evaluator.classify_against_correct_set(situations[0]))
        self.assertEqual("AS6", evaluator.classify_against_correct_set(situations[1]))

    def test_detailed_headings_take_priority_over_summary_table(self) -> None:
        response = """# Run 1 - test/model

## Action Situation 1: Capacitor Adoption Assurance Game
Tension: Neighbours coordinate adoption.
Matrix: 2x2 payoff matrix.

## Action Situation 2: Groundwater Extraction Dilemma
Tension: Farmers share an aquifer.
Matrix: 2x2 payoff matrix.

| # | Title | Strategic tension |
|---|-------|-------------------|
| 1 | Capacitor Adoption Assurance Game | Coordination |
| 2 | Groundwater Extraction Dilemma | Common pool resource |
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "run_01.md"
            path.write_text(response, encoding="utf-8")
            situations = evaluator.extract_action_situations(path)

        self.assertEqual(2, len(situations))

    def test_payoff_matrix_table_is_not_an_action_situation_table(self) -> None:
        lines = [
            "| Farmer A / Farmer B | Adopt | Wait |",
            "|---------------------|-------|------|",
            "| Adopt | (3,3) | (0,2) |",
            "| Wait | (2,0) | (1,1) |",
        ]
        self.assertEqual([], evaluator.extract_table_action_situations(lines))

    def test_json_array_objects_are_extracted_as_action_situations(self) -> None:
        response = '''# Run 1 - test/model

[
  {
    "Title": "Capacitor Adoption Assurance Game",
    "Tension": "Neighbours coordinate adoption.",
    "Representation": "Payoff matrix"
  },
  {
    "title": "Groundwater Extraction Dilemma",
    "tension": "Farmers share an aquifer.",
    "representation": "Payoff matrix"
  }
]
'''
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "run_01.md"
            path.write_text(response, encoding="utf-8")
            situations = evaluator.extract_action_situations(path)

        self.assertEqual(2, len(situations))
        self.assertEqual("AS1", evaluator.classify_against_correct_set(situations[0]))
        self.assertEqual("AS6", evaluator.classify_against_correct_set(situations[1]))

    def test_wrapped_json_action_situations_are_extracted(self) -> None:
        response = '''# Run 1 - test/model

{
  "action_situations": [
    {"action_situation_title": "Sequential Social Learning", "representation": "Sequence"},
    {"action_situation_title": "Groundwater Extraction", "representation": "Payoff matrix"}
  ]
}
'''
        situations = evaluator.extract_json_action_situations(response)

        self.assertEqual(2, len(situations))
        self.assertEqual("AS2", evaluator.classify_against_correct_set(situations[0]))
        self.assertEqual("AS6", evaluator.classify_against_correct_set(situations[1]))

    def test_capacitor_title_takes_priority_over_transformer_context(self) -> None:
        situation = evaluator.ActionSituation(
            title="Capacitor Adoption Coordination among Farmers on a Transformer",
            block="Matrix: neighbouring farmers choose Adopt or Wait.",
            line_no=1,
            has_representation_evidence=True,
        )
        self.assertEqual("AS1", evaluator.classify_against_correct_set(situation))

    def test_title_and_body_still_identify_staff_authorization(self) -> None:
        situation = evaluator.ActionSituation(
            title="Staff Capacity Investment and Farmer Regularisation (Sequential)",
            block="Sub-station staff invest first; the farmer accepts or rejects formal connection authorization.",
            line_no=1,
            has_representation_evidence=True,
        )
        self.assertEqual("AS5", evaluator.classify_against_correct_set(situation))

    def test_sequential_transformer_capacity_title_is_not_social_learning(self) -> None:
        situation = evaluator.ActionSituation(
            title="Transformer Capacity Contribution (Sequential)",
            block="Two farmers choose whether to contribute or free-ride.",
            line_no=1,
            has_representation_evidence=True,
        )
        self.assertEqual("AS3", evaluator.classify_against_correct_set(situation))

    def test_authorized_connections_between_farmers_match_as3(self) -> None:
        situation = evaluator.ActionSituation(
            title="Farmer-Farmer Coordination on Authorized Connections",
            block="Both farmers authorize so transformer capacity improves.",
            line_no=1,
            has_representation_evidence=True,
        )
        self.assertEqual("AS3", evaluator.classify_against_correct_set(situation))

    def test_pump_quality_choice_is_not_transformer_capacity_as3(self) -> None:
        situation = evaluator.ActionSituation(
            title="Pump-Set Quality Choice",
            block=(
                "Low-quality pumps increase transformer load and transformer failure risk. "
                "Mutual adoption of standard pumps improves voltage stability."
            ),
            line_no=1,
            has_representation_evidence=True,
        )
        self.assertIsNone(evaluator.classify_against_correct_set(situation))

    def test_informal_farmer_network_is_not_transformer_capacity_as3(self) -> None:
        situation = evaluator.ActionSituation(
            title="Farmer-Farmer Coordination on Informal Connections",
            block="Farmers sharing a transformer decide whether to join an informal network and free-ride.",
            line_no=1,
            has_representation_evidence=True,
        )
        self.assertIsNone(evaluator.classify_against_correct_set(situation))

    def test_numbered_structured_fields_are_not_action_situation_starts(self) -> None:
        fields = (
            "**8. Outcomes:** Formal authorized connection and staff effort.",
            "10. **Strategic Tension:** Staff and farmer coordinate.",
            "**12. Relevant Rules:** Boundary and choice rules for the transformer.",
        )
        for field in fields:
            with self.subTest(field=field):
                self.assertFalse(evaluator.is_candidate_start(field))

    def test_numbered_title_field_remains_an_action_situation_start(self) -> None:
        self.assertTrue(evaluator.is_candidate_start("1. **Title:** Authorization Game"))

    def test_game_tree_moves_are_not_action_situation_starts(self) -> None:
        moves = (
            "1. **Staff chooses: Invest Effort or Shirk**",
            "## Stage 1 - Staff decides whether to authorize",
            "**Node A - Staff decision**",
            "### Step 2 (Staff): Choose Enforce or Tolerate",
            "**Focal Farmer observes Peer's choice, then chooses: Imitate or Wait**",
            "1. **Farmer 1 chooses: Authorize or Not Authorize**",
            "**[Peer's Realized Outcome] -> Success or Failure**",
        )
        for move in moves:
            with self.subTest(move=move):
                self.assertFalse(evaluator.is_candidate_start(move))

    def test_normal_form_payoff_matrix_is_not_an_action_situation_start(self) -> None:
        self.assertFalse(
            evaluator.is_candidate_start("### Normal-form payoff matrix (Farmer rows, Staff columns)")
        )

    def test_nonbreaking_hyphen_mutual_exchange_matches_as4(self) -> None:
        situation = evaluator.ActionSituation(
            title="Mutual‑exchange coordination between farmer and sub-station staff",
            block="Farmer and staff exchange reciprocal informal benefits. Matrix.",
            line_no=1,
            has_representation_evidence=True,
        )
        self.assertEqual("AS4", evaluator.classify_against_correct_set(situation))

    def test_staff_maintenance_tradeoff_is_not_as5(self) -> None:
        situation = evaluator.ActionSituation(
            title="Staff workload-maintenance trade-off",
            block="Sub-station staff choose maintenance effort. Payoff matrix.",
            line_no=1,
            has_representation_evidence=True,
        )
        self.assertIsNone(evaluator.classify_against_correct_set(situation))

    def test_transformer_investment_and_regularisation_matches_as5(self) -> None:
        situation = evaluator.ActionSituation(
            title="Transformer Capacity Investment and Regularisation",
            block="A farmer requests formalisation and sub-station staff decide whether to invest. Matrix.",
            line_no=1,
            has_representation_evidence=True,
        )
        self.assertEqual("AS5", evaluator.classify_against_correct_set(situation))

    def test_explicit_labels_do_not_override_semantic_review(self) -> None:
        as4 = evaluator.ActionSituation("AS‑4: Mutual-exchange coordination", "Matrix", 1, True)
        as5 = evaluator.ActionSituation(
            "Action Situation 5: Authorization-and-investment coordination",
            "Farmer and sub-station staff choose whether to formalize a connection. Matrix.",
            1,
            True,
        )
        mislabeled = evaluator.ActionSituation("AS1: Groundwater Extraction", "Shared aquifer matrix", 1, True)
        bare_label = evaluator.ActionSituation("AS-4", "Matrix", 1, True)
        self.assertEqual("AS4", evaluator.classify_against_correct_set(as4))
        self.assertEqual("AS5", evaluator.classify_against_correct_set(as5))
        self.assertEqual("AS6", evaluator.classify_against_correct_set(mislabeled))
        self.assertIsNone(evaluator.classify_against_correct_set(bare_label))


if __name__ == "__main__":
    unittest.main()

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


if __name__ == "__main__":
    unittest.main()

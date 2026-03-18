import json


class ActionSituationEvaluator:
    def __init__(self):

        self.ground_truth = {
            "AS1": {"name": "DSM Adoption Coordination", "type": "Assurance / Stag Hunt", "actors": ["F1", "F2"]},
            "AS3": {"name": "Infrastructure Capacity Provision", "type": "Asymmetric Prisoner's Dilemma",
                    "actors": ["F1", "F2"]},
            "AS4": {"name": "Mutual Exchange and Collusion", "type": "Coordination Game", "actors": ["F", "U"]},
            "AS5": {"name": "Authorization and Capacity Investment", "type": "Unique Nash Asymmetric",
                    "actors": ["F2", "U"]},
            "AS6": {"name": "Groundwater Extraction", "type": "Dynamic CPR / PD", "actors": ["F1", "F2"]}

        }

    def evaluate(self, llm_generated_games):

        tp_list = []
        fp_list = []
        fn_list = []


        matched_gt_keys = set()


        for gen_game in llm_generated_games:
            match_found = False
            for gt_key, gt_val in self.ground_truth.items():
                if gt_key in matched_gt_keys:
                    continue


                if self._semantic_match(gen_game, gt_val):
                    tp_list.append({gen_game['name']: gt_key})
                    matched_gt_keys.add(gt_key)
                    match_found = True
                    break

            if not match_found:
                fp_list.append(gen_game)


        for gt_key, gt_val in self.ground_truth.items():
            if gt_key not in matched_gt_keys:
                fn_list.append(gt_key)


        TP = len(tp_list)
        FP = len(fp_list)
        FN = len(fn_list)

        precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0.0


        return {
            "Metrics": {
                "TP": TP,
                "FP": FP,
                "FN": FN,
                "Precision": round(precision, 4),
                "Recall": round(recall, 4)
            },
            "Details": {
                "Correctly_Identified (TP)": tp_list,
                "Incorrect_or_Extra (FP)": fp_list,
                "Missed_Games (FN)": fn_list
            }
        }

    def _semantic_match(self, generated_game, ground_truth_game):

        gen_text = str(generated_game).lower()

        name_keywords = ground_truth_game['name'].lower().split()
        type_keyword = ground_truth_game['type'].split('/')[0].strip().lower()


        if any(word in gen_text for word in name_keywords) or (type_keyword in gen_text):
            return True
        return False



if __name__ == "__main__":
    evaluator = ActionSituationEvaluator()


    llm_output_simulation = [
        {"name": "Farmers DSM Coordination Game", "type": "Stag Hunt"},
        {"name": "Transformer Capacity Provision", "type": "Prisoner's Dilemma"},
        {"name": "Social Learning Sequential Adoption", "type": "Learning game"},
        {"name": "Groundwater Extraction Race", "type": "CPR Dilemma"}

    ]

    print(" LLM ...")
    results = evaluator.evaluate(llm_output_simulation)

    print("\nJSON:")
    print(json.dumps(results, indent=4, ensure_ascii=False))
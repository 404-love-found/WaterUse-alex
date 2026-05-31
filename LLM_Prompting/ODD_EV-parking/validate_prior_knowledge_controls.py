"""
Prior-knowledge / leakage-control validation for the EV-parking case.

This script does not prove that a provider's training corpus excludes the case.
Instead, it tests whether models can reproduce the hidden EV-parking AS set
before they are given the ODD/game material.

Control conditions:
  1. blind_prior: only the case file name/domain is mentioned.
  2. domain_baseline: generic apartment EV charging domain, no case details.
  3. weak_case_description: the short user concept, no ODD/game/scenario text.
  4. odd_only: the real ODD text is provided.
  5. odd_game: the real ODD + game_stuff text is provided.
  6. scenario_positive_control: scenario.txt is intentionally provided to
     verify the scorer can detect exact AS recovery.

Outputs are written to PriorKnowledgeControlRuns/. The scenario file is never
used in prompts except the explicit positive-control condition.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import time
from dataclasses import dataclass
from pathlib import Path

from together import Together

import evaluate_tp_fp_fn_compare as evaluator


CURRENT_DIR = Path(__file__).resolve().parent
TXT_DIR = CURRENT_DIR / "Txts"
ODD_PATH = TXT_DIR / "odd.txt"
GAME_PATH = TXT_DIR / "game_stuff.txt"
SCENARIO_PATH = TXT_DIR / "scenarios.txt"
OUTPUT_ROOT = CURRENT_DIR / "PriorKnowledgeControlRuns"

TEMPERATURE = 0.6
MAX_RETRIES = 5
RETRY_WAIT_SECONDS = 30

MODEL_CONFIGS = {
    "DeepSeek-V4-Pro": {
        "model_id": "deepseek-ai/DeepSeek-V4-Pro",
        "timeout": 600.0,
        "max_tokens": 16000,
    },
    "Llama-3.3-70B": {
        "model_id": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        "timeout": 600.0,
        "max_tokens": 16000,
    },
    "Qwen2.5-7B": {
        "model_id": "Qwen/Qwen2.5-7B-Instruct-Turbo",
        "timeout": 600.0,
        "max_tokens": 16000,
    },
}

CONDITION_ORDER = (
    "blind_prior",
    "domain_baseline",
    "weak_case_description",
    "odd_only",
    "odd_game",
    "scenario_positive_control",
)


@dataclass(frozen=True)
class Condition:
    name: str
    description: str
    includes_odd: bool = False
    includes_game: bool = False
    includes_scenario: bool = False
    leakage_control: bool = False


CONDITIONS = {
    "blind_prior": Condition(
        name="blind_prior",
        description="No ODD/game/scenario context; tests whether the exact case is already known.",
        leakage_control=True,
    ),
    "domain_baseline": Condition(
        name="domain_baseline",
        description="Generic apartment EV charging context; tests domain-level inference.",
        leakage_control=True,
    ),
    "weak_case_description": Condition(
        name="weak_case_description",
        description="Short user concept only; tests what can be inferred without ODD/game/scenario.",
        leakage_control=True,
    ),
    "odd_only": Condition(
        name="odd_only",
        description="Real ODD text only; expected to recover more ASs than weak controls.",
        includes_odd=True,
    ),
    "odd_game": Condition(
        name="odd_game",
        description="Real ODD + game_stuff text; expected to recover the most ASs.",
        includes_odd=True,
        includes_game=True,
    ),
    "scenario_positive_control": Condition(
        name="scenario_positive_control",
        description="scenario.txt intentionally included; positive control for scorer sensitivity.",
        includes_scenario=True,
    ),
}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalize_for_exact_match(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def looks_truncated(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return True
    if stripped.count("```") % 2:
        return True
    return stripped[-1] not in ".!?)`]}>:;\"”'"


def extract_response_text(response) -> str | None:
    choice = response.choices[0]
    message = choice.message
    content = message.content or ""
    reasoning = getattr(message, "reasoning", None) or ""
    finish_reason = getattr(choice, "finish_reason", None)

    if reasoning and (not content or finish_reason == "length" or looks_truncated(content)):
        return reasoning
    return content or reasoning or None


def build_output_instruction() -> str:
    return """
Output candidate action situations in this exact structure:

### Action Situation N: <title>
**Tension:** <short explanation>
**Matrix:**
| Player A / Player B | Option 1 | Option 2 |
|---|---|---|
| Option 1 | (x, x) | (x, x) |
| Option 2 | (x, x) | (x, x) |
**Justification:** <why this is an action situation>

If you do not know the exact unpublished case, do not claim exact knowledge.
You may provide general hypotheses, but label them as inferred.
"""


def build_prompt(condition: Condition, odd_text: str, game_text: str, scenario_text: str) -> str:
    instruction = build_output_instruction()

    if condition.name == "blind_prior":
        return f"""
This is a prior-knowledge control test.

The unpublished case is named ODD_EV-parking and concerns action-situation
extraction for an EV-parking case. No ODD, game scenario, or gold AS list is
provided here.

Task:
If you already know the exact unpublished case, list the exact action
situations. If you do not know it exactly, state that the titles are inferred
from general domain knowledge.

{instruction}
"""

    if condition.name == "domain_baseline":
        return f"""
This is a domain-baseline control test.

Consider a generic apartment parking garage with shared EV chargers and limited
charging bays. Drivers may wait, charge, and leave. No case-specific ODD,
game_stuff, scenario file, or gold AS list is provided.

Extract plausible action situations using the IAD framework. These should be
general hypotheses, not claims about an exact unpublished case.

{instruction}
"""

    if condition.name == "weak_case_description":
        return f"""
This is a weak-context control test.

The only case description is:
An apartment parking garage has shared EV chargers. Residents receive a
discounted per-kWh charging price, non-residents pay the regular per-kWh price,
all users are billed by electricity consumed, and the research focus is fair
queueing for scarce shared chargers.

No ODD text, game_stuff text, scenario file, or gold AS list is provided.
Extract plausible action situations using the IAD framework.

{instruction}
"""

    if condition.name == "odd_only":
        return f"""
Given the following ODD+D description of an apartment EV parking shared-charging
model:

{odd_text}

Extract all distinct action situations described in the model using the IAD
framework. Do not use any scenario/gold-answer file.

{instruction}
"""

    if condition.name == "odd_game":
        return f"""
Given the following ODD+D description of an apartment EV parking shared-charging
model:

{odd_text}

Case scenario and model-logic context:

{game_text}

Extract all distinct action situations described in the model using the IAD
framework. Do not use any scenario/gold-answer file.

{instruction}
"""

    if condition.name == "scenario_positive_control":
        return f"""
This is a positive-control test. The hidden evaluation scenario is intentionally
provided below to confirm that the scorer can detect exact recovery.

{scenario_text}

Extract the action situations listed in the provided scenario using the IAD
framework.

{instruction}
"""

    raise ValueError(f"Unsupported condition: {condition.name}")


def call_model(client: Together, model_id: str, prompt: str, max_tokens: int) -> str | None:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.chat.completions.create(
                model=model_id,
                messages=[{"role": "user", "content": prompt}],
                temperature=TEMPERATURE,
                max_tokens=max_tokens,
            )
            return extract_response_text(response)
        except Exception as exc:
            error_msg = str(exc).lower()
            retryable = any(
                token in error_msg
                for token in ("503", "service_unavailable", "timeout", "429", "rate", "throttled")
            )
            if retryable and attempt < MAX_RETRIES:
                print(f"      retry {attempt}/{MAX_RETRIES}, waiting {RETRY_WAIT_SECONDS}s... ({exc})")
                time.sleep(RETRY_WAIT_SECONDS)
                continue
            print(f"      error: {exc}")
            return None
    return None


def exact_title_hits(text: str) -> list[str]:
    normalized_text = normalize_for_exact_match(text)
    hits: list[str] = []
    for gt_as in evaluator.GROUND_TRUTH.values():
        normalized_title = normalize_for_exact_match(gt_as.title)
        if normalized_title and normalized_title in normalized_text:
            hits.append(gt_as.key)
    return hits


def leakage_risk(condition_name: str, tp: int, exact_hits: int) -> str:
    if condition_name not in {"blind_prior", "domain_baseline", "weak_case_description"}:
        return "N/A"
    if exact_hits >= 2:
        return "HIGH"
    if exact_hits == 1:
        return "MEDIUM"
    if condition_name in {"blind_prior", "domain_baseline"} and tp >= 4:
        return "MEDIUM"
    return "LOW"


def write_manifest(
    output_root: Path,
    prompts: dict[str, str],
    odd_text: str,
    game_text: str,
    scenario_text: str,
    runs: int,
    models: list[str],
) -> None:
    manifest = {
        "purpose": "EV-parking prior-knowledge / leakage-control validation",
        "runs_per_condition_model": runs,
        "models": models,
        "input_hashes": {
            "odd.txt": sha256_text(odd_text),
            "game_stuff.txt": sha256_text(game_text),
            "scenarios.txt": sha256_text(scenario_text),
        },
        "conditions": {
            name: {
                "description": CONDITIONS[name].description,
                "includes_odd": CONDITIONS[name].includes_odd,
                "includes_game": CONDITIONS[name].includes_game,
                "includes_scenario": CONDITIONS[name].includes_scenario,
                "leakage_control": CONDITIONS[name].leakage_control,
                "prompt_sha256": sha256_text(prompt),
            }
            for name, prompt in prompts.items()
        },
        "interpretation": {
            "exact_title_hits": "Strongest black-box signal of possible prior knowledge.",
            "semantic_tp_without_context": "Can be ordinary domain inference; not proof of training-data exposure.",
            "positive_control": "Scenario is intentionally included only in scenario_positive_control.",
        },
    }
    output_root.mkdir(parents=True, exist_ok=True)
    (output_root / "prompt_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def run_generation(args, prompts: dict[str, str], selected_models: list[str]) -> None:
    api_key = os.environ.get("TOGETHER_API_KEY")
    if not api_key:
        raise RuntimeError("Set TOGETHER_API_KEY, or use --score-only to score existing outputs.")

    for condition_name in args.conditions:
        prompt = prompts[condition_name]
        for model_name in selected_models:
            cfg = MODEL_CONFIGS[model_name]
            model_id = cfg["model_id"]
            client = Together(api_key=api_key, timeout=cfg["timeout"])
            model_dir = args.output_root / condition_name / model_name
            model_dir.mkdir(parents=True, exist_ok=True)

            print(f"\n{condition_name} | {model_name} | {args.runs} runs")
            for run_no in range(1, args.runs + 1):
                target = model_dir / f"run_{run_no:02d}.md"
                if target.exists() and not args.force:
                    print(f"  run_{run_no:02d} skipped existing")
                    continue

                print(f"  run_{run_no:02d} ...", end="", flush=True)
                content = None
                for attempt in range(1, 4):
                    content = call_model(client, model_id, prompt, cfg["max_tokens"])
                    if content and not looks_truncated(content):
                        break
                    if attempt < 3:
                        print(f" suspicious attempt {attempt}, retrying ...", end="", flush=True)
                        time.sleep(5)

                if not content:
                    print(" failed")
                    continue

                target.write_text(f"# Run {run_no} - {model_id}\n\n{content}", encoding="utf-8")
                status = "ok" if not looks_truncated(content) else "still-suspicious"
                print(f" saved {len(content)} chars ({status})")


def score_outputs(output_root: Path, conditions: list[str], selected_models: list[str]) -> tuple[Path, Path]:
    summary_csv = output_root / "prior_knowledge_control_summary.csv"
    report_txt = output_root / "prior_knowledge_control_report.txt"
    output_root.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, str | int | float]] = []

    for condition_name in conditions:
        for model_name in selected_models:
            model_dir = output_root / condition_name / model_name
            for filepath in sorted(model_dir.glob("run_*.md")):
                result = evaluator.evaluate_run(filepath)
                text = filepath.read_text(encoding="utf-8", errors="replace")
                exact_hits = exact_title_hits(text)
                rows.append(
                    {
                        "Condition": condition_name,
                        "Model": model_name,
                        "Run": filepath.name,
                        "Generated_AS": result.total_as,
                        "TP": result.tp,
                        "FN": result.fn,
                        "FP": result.fp,
                        "Precision": f"{result.precision:.4f}",
                        "Recall": f"{result.recall:.4f}",
                        "Exact_Title_Hits": len(exact_hits),
                        "Exact_Title_AS": ";".join(exact_hits),
                        "Leakage_Risk": leakage_risk(condition_name, result.tp, len(exact_hits)),
                    }
                )

    with summary_csv.open("w", newline="", encoding="utf-8") as csvf:
        fieldnames = [
            "Condition",
            "Model",
            "Run",
            "Generated_AS",
            "TP",
            "FN",
            "FP",
            "Precision",
            "Recall",
            "Exact_Title_Hits",
            "Exact_Title_AS",
            "Leakage_Risk",
        ]
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    aggregates: dict[tuple[str, str], dict[str, float | int]] = {}
    for row in rows:
        key = (str(row["Condition"]), str(row["Model"]))
        bucket = aggregates.setdefault(
            key,
            {
                "runs": 0,
                "tp": 0,
                "fn": 0,
                "fp": 0,
                "exact": 0,
                "max_exact": 0,
                "high": 0,
                "medium": 0,
            },
        )
        bucket["runs"] += 1
        bucket["tp"] += int(row["TP"])
        bucket["fn"] += int(row["FN"])
        bucket["fp"] += int(row["FP"])
        exact_count = int(row["Exact_Title_Hits"])
        bucket["exact"] += exact_count
        bucket["max_exact"] = max(int(bucket["max_exact"]), exact_count)
        bucket["high"] += 1 if row["Leakage_Risk"] == "HIGH" else 0
        bucket["medium"] += 1 if row["Leakage_Risk"] == "MEDIUM" else 0

    with report_txt.open("w", encoding="utf-8") as out:
        out.write("=" * 88 + "\n")
        out.write("EV-PARKING PRIOR-KNOWLEDGE / LEAKAGE-CONTROL REPORT\n")
        out.write("=" * 88 + "\n\n")
        out.write("Interpretation:\n")
        out.write("  This script cannot prove absence from a provider training corpus.\n")
        out.write("  It tests whether models reproduce the hidden AS set before ODD/game/scenario text is given.\n")
        out.write("  Exact title hits in blind/domain/weak controls are the strongest warning signal.\n")
        out.write("  Semantic TP in weak controls may be ordinary inference, not proof of leakage.\n\n")
        out.write("Gold AS titles from Txts/scenarios.txt:\n")
        for gt_as in evaluator.GROUND_TRUTH.values():
            out.write(f"  {gt_as.label}\n")
        out.write("\n")

        out.write(
            f"{'Condition':<26} {'Model':<18} {'Runs':>4} {'TP':>4} {'FN':>4} {'FP':>4} "
            f"{'Prec':>7} {'Recall':>7} {'Exact':>6} {'MaxEx':>5} {'Hi':>3} {'Med':>4}\n"
        )
        out.write("-" * 96 + "\n")
        for condition_name in conditions:
            for model_name in selected_models:
                bucket = aggregates.get((condition_name, model_name))
                if not bucket:
                    continue
                tp = int(bucket["tp"])
                fn = int(bucket["fn"])
                fp = int(bucket["fp"])
                precision = tp / (tp + fp) if (tp + fp) else 0.0
                recall = tp / (tp + fn) if (tp + fn) else 0.0
                out.write(
                    f"{condition_name:<26} {model_name:<18} {int(bucket['runs']):>4} "
                    f"{tp:>4} {fn:>4} {fp:>4} {precision:>7.4f} {recall:>7.4f} "
                    f"{int(bucket['exact']):>6} {int(bucket['max_exact']):>5} "
                    f"{int(bucket['high']):>3} {int(bucket['medium']):>4}\n"
                )

        out.write("\nDecision guide:\n")
        out.write("  PASS: blind/domain/weak controls have zero exact title hits and low leakage risk.\n")
        out.write("  REVIEW: any weak control has exact title hits or repeated medium/high risk.\n")
        out.write("  FAIL-SUSPECT: blind_prior or domain_baseline repeatedly reproduces multiple exact AS titles.\n")
        out.write("  Positive control should recover many ASs when scenario text is intentionally provided.\n")

    return summary_csv, report_txt


def parse_csv_arg(value: str, allowed: set[str], label: str) -> list[str]:
    items = [item.strip() for item in value.split(",") if item.strip()]
    invalid = [item for item in items if item not in allowed]
    if invalid:
        raise ValueError(f"Unknown {label}: {invalid}. Allowed: {sorted(allowed)}")
    return items


def main() -> None:
    parser = argparse.ArgumentParser(description="Run EV-parking prior-knowledge leakage controls.")
    parser.add_argument("--runs", type=int, default=3, help="Runs per condition/model. Default: 3.")
    parser.add_argument(
        "--models",
        default=",".join(MODEL_CONFIGS),
        help="Comma-separated model keys. Default: all models.",
    )
    parser.add_argument(
        "--conditions",
        default=",".join(CONDITION_ORDER),
        help="Comma-separated condition names. Default: all conditions.",
    )
    parser.add_argument("--output-root", type=Path, default=OUTPUT_ROOT)
    parser.add_argument("--force", action="store_true", help="Overwrite existing generated outputs.")
    parser.add_argument("--score-only", action="store_true", help="Only score existing outputs; no API calls.")
    parser.add_argument("--dry-run", action="store_true", help="Write prompt manifest only; no API calls.")
    args = parser.parse_args()

    if args.runs < 1:
        raise ValueError("--runs must be >= 1")

    selected_models = parse_csv_arg(args.models, set(MODEL_CONFIGS), "models")
    args.conditions = parse_csv_arg(args.conditions, set(CONDITIONS), "conditions")
    args.output_root = args.output_root.resolve()

    odd_text = ODD_PATH.read_text(encoding="utf-8")
    game_text = GAME_PATH.read_text(encoding="utf-8")
    scenario_text = SCENARIO_PATH.read_text(encoding="utf-8")

    prompts = {
        condition_name: build_prompt(CONDITIONS[condition_name], odd_text, game_text, scenario_text)
        for condition_name in args.conditions
    }
    write_manifest(args.output_root, prompts, odd_text, game_text, scenario_text, args.runs, selected_models)

    if args.dry_run:
        print(f"Dry run complete. Manifest: {args.output_root / 'prompt_manifest.json'}")
        return

    if not args.score_only:
        run_generation(args, prompts, selected_models)

    summary_csv, report_txt = score_outputs(args.output_root, args.conditions, selected_models)
    print("\nValidation outputs:")
    print(f"  Summary CSV: {summary_csv}")
    print(f"  Report:      {report_txt}")
    print(f"  Manifest:    {args.output_root / 'prompt_manifest.json'}")


if __name__ == "__main__":
    main()

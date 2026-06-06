#!/usr/bin/env python3
"""Build table-only evaluation reports from local evaluation CSVs."""

from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "analysis_reports" / "model_evaluation_comparison_2026-06-06"
TABLE_DIR = OUT_DIR / "tables"

TODAY = date(2026, 6, 6)
RUN_COUNT_EXPECTED = 30

CASE_FILES = [
    {
        "case": "EV-parking",
        "condition": "ODD+game",
        "csv": ROOT / "ODD_EV-parking" / "Batch_30Runs" / "EVParking_evaluation_summary_ODD+game_stuff.csv",
    },
    {
        "case": "EV-parking",
        "condition": "ODD-only",
        "csv": ROOT / "ODD_EV-parking" / "Batch_30Runs_ODDOnly" / "EVParking_evaluation_summary_ODD-only.csv",
    },
    {
        "case": "Water-use",
        "condition": "ODD+game",
        "csv": ROOT / "ODD_water" / "Batch_30Runs" / "Water_evaluation_summary_ODD+game_stuff.csv",
    },
    {
        "case": "Water-use",
        "condition": "ODD-only",
        "csv": ROOT / "ODD_water" / "Batch_30Runs_ODDOnly" / "Water_evaluation_summary_ODD-only.csv",
    },
    {
        "case": "Electricity",
        "condition": "ODD+game",
        "csv": ROOT / "ODD_electricity" / "Batch_30Runs" / "Electricity_evaluation_summary_ODD+game_stuff.csv",
    },
    {
        "case": "Electricity",
        "condition": "ODD-only",
        "csv": ROOT / "ODD_electricity" / "Batch_30Runs_ODDOnly" / "Electricity_evaluation_summary_ODD-only.csv",
    },
]

AS_LEVEL_FILES = [
    {
        "case": "EV-parking",
        "condition": "ODD+game",
        "csv": ROOT / "ODD_EV-parking" / "Batch_30Runs" / "EVParking_evaluation_as_level_ODD+game_stuff.csv",
    },
    {
        "case": "EV-parking",
        "condition": "ODD-only",
        "csv": ROOT / "ODD_EV-parking" / "Batch_30Runs_ODDOnly" / "EVParking_evaluation_as_level_ODD-only.csv",
    },
    {
        "case": "Water-use",
        "condition": "ODD+game",
        "csv": ROOT / "ODD_water" / "Batch_30Runs" / "Water_evaluation_as_level_ODD+game_stuff.csv",
    },
    {
        "case": "Water-use",
        "condition": "ODD-only",
        "csv": ROOT / "ODD_water" / "Batch_30Runs_ODDOnly" / "Water_evaluation_as_level_ODD-only.csv",
    },
    {
        "case": "Electricity",
        "condition": "ODD+game",
        "csv": ROOT / "ODD_electricity" / "Batch_30Runs" / "Electricity_evaluation_as_level_ODD+game_stuff.csv",
    },
    {
        "case": "Electricity",
        "condition": "ODD-only",
        "csv": ROOT / "ODD_electricity" / "Batch_30Runs_ODDOnly" / "Electricity_evaluation_as_level_ODD-only.csv",
    },
]


def safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def run_num(run_name: str) -> int:
    return int(Path(run_name).stem.split("_")[1])


def fmt(value: object, digits: int = 4) -> str:
    if isinstance(value, float):
        if pd.isna(value):
            return ""
        return f"{value:.{digits}f}"
    return str(value)


def load_runs() -> pd.DataFrame:
    frames = []
    for spec in CASE_FILES:
        df = pd.read_csv(spec["csv"])
        df["Case"] = spec["case"]
        df["Condition"] = spec["condition"]
        df["Source"] = str(spec["csv"].relative_to(ROOT))
        df["Run_Number"] = df["Run"].map(run_num)
        df["Precision"] = df["Precision"].astype(float)
        df["Recall"] = df["Recall"].astype(float)
        frames.append(df)
    return pd.concat(frames, ignore_index=True)


def load_as_level() -> pd.DataFrame:
    frames = []
    for spec in AS_LEVEL_FILES:
        df = pd.read_csv(spec["csv"])
        df["Case"] = spec["case"]
        df["Condition"] = spec["condition"]
        df["Source"] = str(spec["csv"].relative_to(ROOT))
        frames.append(df)
    return pd.concat(frames, ignore_index=True)


def build_completeness(runs: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (case, condition, model), part in runs.groupby(["Case", "Condition", "Model"], sort=True):
        actual = sorted(part["Run_Number"].astype(int).tolist())
        missing = [i for i in range(1, RUN_COUNT_EXPECTED + 1) if i not in actual]
        duplicate_count = len(actual) - len(set(actual))
        rows.append(
            {
                "Case": case,
                "Condition": condition,
                "Model": model,
                "Run_Count": len(actual),
                "Expected_Runs": RUN_COUNT_EXPECTED,
                "Missing_Runs": ",".join(f"{i:02d}" for i in missing),
                "Duplicate_Run_Count": duplicate_count,
                "Status": "Complete" if len(actual) == RUN_COUNT_EXPECTED and not missing and duplicate_count == 0 else "Incomplete",
            }
        )
    return pd.DataFrame(rows).sort_values(["Case", "Condition", "Model"])


def build_metrics(runs: pd.DataFrame) -> pd.DataFrame:
    grouped = runs.groupby(["Case", "Condition", "Model"], as_index=False).agg(
        Runs=("Run", "count"),
        TP=("TP", "sum"),
        FN=("FN", "sum"),
        FP=("FP", "sum"),
        Mean_Precision=("Precision", "mean"),
        Mean_Recall=("Recall", "mean"),
    )
    grouped["Precision"] = grouped.apply(lambda r: safe_div(r["TP"], r["TP"] + r["FP"]), axis=1)
    grouped["Recall"] = grouped.apply(lambda r: safe_div(r["TP"], r["TP"] + r["FN"]), axis=1)
    return grouped.sort_values(["Case", "Model", "Condition"])


def build_effects(metrics: pd.DataFrame) -> pd.DataFrame:
    wide = metrics.pivot_table(
        index=["Case", "Model"],
        columns="Condition",
        values=["TP", "FN", "FP", "Precision", "Recall"],
        aggfunc="first",
    )
    rows = []
    for idx, values in wide.iterrows():
        case, model = idx
        if ("TP", "ODD+game") not in values or pd.isna(values[("TP", "ODD+game")]) or pd.isna(values[("TP", "ODD-only")]):
            continue
        rows.append(
            {
                "Case": case,
                "Model": model,
                "Delta_TP": values[("TP", "ODD+game")] - values[("TP", "ODD-only")],
                "Delta_FN": values[("FN", "ODD+game")] - values[("FN", "ODD-only")],
                "Delta_FP": values[("FP", "ODD+game")] - values[("FP", "ODD-only")],
                "Delta_Precision": values[("Precision", "ODD+game")] - values[("Precision", "ODD-only")],
                "Delta_Recall": values[("Recall", "ODD+game")] - values[("Recall", "ODD-only")],
            }
        )
    return pd.DataFrame(rows).sort_values(["Case", "Model"])


def build_aggregate(runs: pd.DataFrame, common_only: bool = False) -> pd.DataFrame:
    source = runs.copy()
    label = "available case coverage"
    if common_only:
        common_models = set.intersection(*[set(source.loc[source["Case"] == case, "Model"].unique()) for case in sorted(source["Case"].unique())])
        source = source[source["Model"].isin(common_models)].copy()
        label = "three-case common models"
    grouped = source.groupby(["Model", "Condition"], as_index=False).agg(
        Cases=("Case", lambda x: ",".join(sorted(set(x)))),
        Case_Count=("Case", lambda x: len(set(x))),
        Runs=("Run", "count"),
        TP=("TP", "sum"),
        FN=("FN", "sum"),
        FP=("FP", "sum"),
    )
    grouped["Precision"] = grouped.apply(lambda r: safe_div(r["TP"], r["TP"] + r["FP"]), axis=1)
    grouped["Recall"] = grouped.apply(lambda r: safe_div(r["TP"], r["TP"] + r["FN"]), axis=1)
    grouped["Aggregation"] = label
    return grouped.sort_values(["Model", "Condition"])


def write_csvs(tables: dict[str, pd.DataFrame]) -> None:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    for name, df in tables.items():
        df.to_csv(TABLE_DIR / f"{name}.csv", index=False, quoting=csv.QUOTE_MINIMAL)


def markdown_table(df: pd.DataFrame, columns: list[str]) -> str:
    view = df.loc[:, columns].copy()
    for col in view.columns:
        if view[col].dtype.kind == "f":
            view[col] = view[col].map(lambda x: fmt(x, 4))
    header = "| " + " | ".join(columns) + " |"
    sep = "| " + " | ".join(["---"] * len(columns)) + " |"
    rows = ["| " + " | ".join(str(row[col]) for col in columns) + " |" for _, row in view.iterrows()]
    return "\n".join([header, sep] + rows)


def render_markdown(tables: dict[str, pd.DataFrame]) -> Path:
    completeness = tables["run_completeness"]
    metrics = tables["overall_metrics_by_case_model_condition"].copy()
    effects = tables["prompt_effect_by_case_model"].copy()
    aggregate = tables["aggregate_metrics_available_cases"].copy()

    metric_view = metrics.assign(
        Precision=metrics["Precision"].map(lambda x: fmt(x, 4)),
        Recall=metrics["Recall"].map(lambda x: fmt(x, 4)),
    )
    effects_view = effects.assign(
        Delta_Precision=effects["Delta_Precision"].map(lambda x: f"{x:+.4f}"),
        Delta_Recall=effects["Delta_Recall"].map(lambda x: f"{x:+.4f}"),
    )
    aggregate_view = aggregate.assign(
        Precision=aggregate["Precision"].map(lambda x: fmt(x, 4)),
        Recall=aggregate["Recall"].map(lambda x: fmt(x, 4)),
    )

    md = f"""# ODD AS Extraction Evaluation Tables

Date: {TODAY.isoformat()}

## Run Completeness

{markdown_table(completeness, ["Case", "Condition", "Model", "Run_Count", "Expected_Runs", "Missing_Runs", "Duplicate_Run_Count", "Status"])}

## Overall Evaluation Results

{markdown_table(metric_view, ["Case", "Condition", "Model", "Runs", "TP", "FN", "FP", "Precision", "Recall"])}

## ODD+game Minus ODD-only

{markdown_table(effects_view, ["Case", "Model", "Delta_TP", "Delta_FN", "Delta_FP", "Delta_Precision", "Delta_Recall"])}

## Aggregate Evaluation Results

{markdown_table(aggregate_view, ["Model", "Condition", "Case_Count", "Runs", "TP", "FN", "FP", "Precision", "Recall", "Cases"])}
"""
    path = OUT_DIR / "ODD_AS_Extraction_Evaluation_Comparison_Report_2026-06-06.md"
    path.write_text(md, encoding="utf-8")
    return path


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    runs = load_runs()
    as_level = load_as_level()
    completeness = build_completeness(runs)
    metrics = build_metrics(runs)
    effects = build_effects(metrics)
    aggregate = build_aggregate(runs, common_only=False)
    aggregate_common = build_aggregate(runs, common_only=True)
    tables = {
        "run_level_metrics": runs,
        "as_level_metrics": as_level,
        "run_completeness": completeness,
        "overall_metrics_by_case_model_condition": metrics,
        "prompt_effect_by_case_model": effects,
        "aggregate_metrics_available_cases": aggregate,
        "aggregate_metrics_three_case_common_models": aggregate_common,
    }
    write_csvs(tables)
    markdown_path = render_markdown(tables)
    print(f"Report directory: {OUT_DIR}")
    print(f"Markdown report: {markdown_path}")
    print("Tables:")
    for name in tables:
        print(f"  {TABLE_DIR / (name + '.csv')}")


if __name__ == "__main__":
    main()

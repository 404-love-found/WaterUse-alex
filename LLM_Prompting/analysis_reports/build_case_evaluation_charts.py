#!/usr/bin/env python3
"""Build case-level evaluation comparison charts from TP/FN/FP/Precision/Recall."""

from __future__ import annotations

import os
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
import seaborn as sns
from matplotlib.patches import Patch


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "analysis_reports" / "model_evaluation_comparison_2026-06-06"
TABLE_DIR = OUT_DIR / "tables"
CHART_DIR = OUT_DIR / "charts"

TOKENS = {
    "surface": "#FCFCFD",
    "panel": "#FFFFFF",
    "ink": "#1F2430",
    "muted": "#6F768A",
    "grid": "#E6E8F0",
    "axis": "#D7DBE7",
}

COLOR_FAMILIES = {
    "blue": {"base": "#A3BEFA", "dark": "#2E4780"},
    "gold": {"base": "#FFE15B", "dark": "#736422"},
    "orange": {"base": "#F0986E", "dark": "#804126"},
    "olive": {"base": "#A3D576", "dark": "#386411"},
    "pink": {"base": "#F390CA", "dark": "#8A3A6F"},
}

CASE_ORDER = ["EV-parking", "Water-use", "Electricity"]
CONDITION_ORDER = ["ODD+game", "ODD-only"]
MODEL_ORDER = ["DeepSeek-R1", "DeepSeek-V4-Pro", "Llama-3.3-70B", "Qwen2.5-7B"]


def use_chart_theme() -> None:
    sns.set_theme(
        style="whitegrid",
        rc={
            "figure.facecolor": TOKENS["surface"],
            "figure.edgecolor": "none",
            "savefig.facecolor": TOKENS["surface"],
            "savefig.edgecolor": "none",
            "axes.facecolor": TOKENS["panel"],
            "axes.edgecolor": TOKENS["axis"],
            "axes.labelcolor": TOKENS["ink"],
            "axes.grid": True,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "grid.color": TOKENS["grid"],
            "grid.linewidth": 0.8,
            "font.family": "sans-serif",
            "font.sans-serif": ["Aptos", "Inter", "Segoe UI", "DejaVu Sans", "Arial", "sans-serif"],
            "font.monospace": ["SF Mono", "Menlo", "Consolas", "DejaVu Sans Mono", "monospace"],
            "patch.linewidth": 1.0,
        },
    )


def add_chart_header(fig, ax, title: str, subtitle: str) -> None:
    """Add a report-style title/subtitle and reserve plot space."""
    ax.set_title("")
    fig.subplots_adjust(top=0.88)
    left = ax.get_position().x0
    fig.text(left, 0.985, title, ha="left", va="top", fontsize=13, fontweight="semibold", color=TOKENS["ink"])
    fig.text(left, 0.94, subtitle, ha="left", va="top", fontsize=9, color=TOKENS["muted"])
    sns.despine(ax=ax)


def sorted_models(models: pd.Series) -> list[str]:
    present = set(models.dropna())
    return [model for model in MODEL_ORDER if model in present] + sorted(present - set(MODEL_ORDER))


def plot_precision_recall(metrics: pd.DataFrame) -> Path:
    use_chart_theme()
    long = metrics.melt(
        id_vars=["Case", "Condition", "Model", "Runs"],
        value_vars=["Precision", "Recall"],
        var_name="Metric",
        value_name="Value",
    )
    long["Metric"] = pd.Categorical(long["Metric"], ["Precision", "Recall"], ordered=True)
    long["Case"] = pd.Categorical(long["Case"], CASE_ORDER, ordered=True)
    long["Condition"] = pd.Categorical(long["Condition"], CONDITION_ORDER, ordered=True)
    long["Model"] = pd.Categorical(long["Model"], MODEL_ORDER, ordered=True)
    palette = {"ODD+game": COLOR_FAMILIES["blue"]["base"], "ODD-only": COLOR_FAMILIES["gold"]["base"]}

    fig, axes = plt.subplots(3, 2, figsize=(12, 11), sharex=True)
    for r, case in enumerate(CASE_ORDER):
        for c, metric in enumerate(["Precision", "Recall"]):
            ax = axes[r, c]
            part = long[(long["Case"] == case) & (long["Metric"] == metric)].copy()
            order = sorted_models(part["Model"])
            sns.barplot(
                data=part,
                x="Value",
                y="Model",
                hue="Condition",
                order=order,
                hue_order=CONDITION_ORDER,
                palette=palette,
                ax=ax,
                edgecolor=TOKENS["ink"],
                linewidth=0.7,
            )
            ax.set_xlim(0, 1.05)
            ax.xaxis.set_major_formatter(mticker.PercentFormatter(1.0))
            ax.set_xlabel(metric)
            ax.set_ylabel("")
            ax.set_title(f"{case} | {metric}", loc="left", fontsize=10, color=TOKENS["ink"], fontweight="semibold")
            if ax.get_legend():
                ax.get_legend().remove()
            for container in ax.containers:
                ax.bar_label(container, labels=[f"{bar.get_width() * 100:.1f}%" if bar.get_width() else "" for bar in container], padding=2, fontsize=6.8)
    add_chart_header(
        fig,
        axes[0, 0],
        "Precision and recall by case, model, and prompt condition",
        "Each panel compares ODD+game with ODD-only for the same case and model.",
    )
    fig.legend(
        handles=[
            Patch(facecolor=palette["ODD+game"], edgecolor=TOKENS["ink"], label="ODD+game"),
            Patch(facecolor=palette["ODD-only"], edgecolor=TOKENS["ink"], label="ODD-only"),
        ],
        loc="upper left",
        bbox_to_anchor=(0.08, 0.905),
        frameon=False,
        ncol=2,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.82), h_pad=1.8, w_pad=1.5)
    path = CHART_DIR / "precision_recall_by_case_model_condition.png"
    fig.savefig(path, dpi=220, bbox_inches="tight")
    plt.close(fig)
    return path


def plot_case_counts(metrics: pd.DataFrame, case: str) -> Path:
    use_chart_theme()
    part = metrics[metrics["Case"] == case].copy()
    long = part.melt(
        id_vars=["Case", "Condition", "Model", "Runs"],
        value_vars=["TP", "FN", "FP"],
        var_name="Metric",
        value_name="Count",
    )
    long["Condition"] = pd.Categorical(long["Condition"], CONDITION_ORDER, ordered=True)
    long["Model"] = pd.Categorical(long["Model"], sorted_models(long["Model"]), ordered=True)
    palette = {"ODD+game": COLOR_FAMILIES["blue"]["base"], "ODD-only": COLOR_FAMILIES["gold"]["base"]}

    fig, axes = plt.subplots(1, 3, figsize=(12, 4.8), sharey=True)
    for ax, metric in zip(axes, ["TP", "FN", "FP"]):
        metric_part = long[long["Metric"] == metric].copy()
        sns.barplot(
            data=metric_part,
            x="Count",
            y="Model",
            hue="Condition",
            hue_order=CONDITION_ORDER,
            palette=palette,
            ax=ax,
            edgecolor=TOKENS["ink"],
            linewidth=0.7,
        )
        ax.set_title(metric, loc="left", fontsize=10, color=TOKENS["ink"], fontweight="semibold")
        ax.set_xlabel("Count across 30 runs")
        ax.set_ylabel("")
        if metric != "TP":
            ax.get_legend().remove()
        else:
            ax.legend(loc="lower left", bbox_to_anchor=(0, 1.02), frameon=False, ncol=2, borderaxespad=0)
        for container in ax.containers:
            ax.bar_label(container, labels=[f"{bar.get_width():.0f}" if bar.get_width() else "" for bar in container], padding=2, fontsize=7)
    add_chart_header(
        fig,
        axes[0],
        f"{case} TP, FN, and FP by model and prompt condition",
        "Counts are summed over the 30-run batch; compare count levels within this case rather than across cases.",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.88), w_pad=1.5)
    slug = case.lower().replace("-", "_")
    path = CHART_DIR / f"{slug}_tp_fn_fp_by_model_condition.png"
    fig.savefig(path, dpi=220, bbox_inches="tight")
    plt.close(fig)
    return path


def plot_prompt_deltas(effects: pd.DataFrame) -> Path:
    use_chart_theme()
    long = effects.melt(
        id_vars=["Case", "Model"],
        value_vars=["Delta_Precision", "Delta_Recall"],
        var_name="Metric",
        value_name="Delta",
    )
    long["Metric"] = long["Metric"].map({"Delta_Precision": "Precision delta", "Delta_Recall": "Recall delta"})
    long["Label"] = long["Case"] + " | " + long["Model"]
    long["Case"] = pd.Categorical(long["Case"], CASE_ORDER, ordered=True)
    metric_order = ["Precision delta", "Recall delta"]

    fig, axes = plt.subplots(1, 2, figsize=(12, 7.5), sharey=True)
    for ax, metric in zip(axes, metric_order):
        part = long[long["Metric"] == metric].copy()
        part = part.sort_values(["Case", "Delta"], ascending=[True, True])
        colors = [COLOR_FAMILIES["olive"]["base"] if value >= 0 else COLOR_FAMILIES["orange"]["base"] for value in part["Delta"]]
        edges = [COLOR_FAMILIES["olive"]["dark"] if value >= 0 else COLOR_FAMILIES["orange"]["dark"] for value in part["Delta"]]
        bars = ax.barh(part["Label"], part["Delta"], color=colors, edgecolor=edges, linewidth=0.8)
        ax.axvline(0, color=TOKENS["ink"], linewidth=1.0)
        ax.set_title(metric, loc="left", fontsize=10, color=TOKENS["ink"], fontweight="semibold")
        ax.set_xlabel("ODD+game minus ODD-only")
        ax.xaxis.set_major_formatter(mticker.PercentFormatter(1.0))
        span = max(abs(part["Delta"].min()), abs(part["Delta"].max()), 0.05)
        ax.set_xlim(-span * 1.28, span * 1.28)
        for bar, value in zip(bars, part["Delta"]):
            ha = "left" if value >= 0 else "right"
            offset = span * 0.025 if value >= 0 else -span * 0.025
            ax.text(value + offset, bar.get_y() + bar.get_height() / 2, f"{value * 100:+.1f} pp", va="center", ha=ha, fontsize=7.2, color=TOKENS["ink"])
    add_chart_header(
        fig,
        axes[0],
        "Prompt-condition effect by case and model",
        "Signed deltas show ODD+game minus ODD-only; positive values favor ODD+game.",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.88), w_pad=2)
    path = CHART_DIR / "prompt_condition_delta_precision_recall_by_case_model.png"
    fig.savefig(path, dpi=220, bbox_inches="tight")
    plt.close(fig)
    return path


def main() -> None:
    os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    metrics = pd.read_csv(TABLE_DIR / "overall_metrics_by_case_model_condition.csv")
    effects = pd.read_csv(TABLE_DIR / "prompt_effect_by_case_model.csv")

    paths = [plot_precision_recall(metrics)]
    for case in CASE_ORDER:
        paths.append(plot_case_counts(metrics, case))
    paths.append(plot_prompt_deltas(effects))
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()

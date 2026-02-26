"""Visualization charts for evaluation results."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def _ensure_dir(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def latency_boxplot(
    data: dict[str, list[float]],
    output_path: Path,
    title: str = "Query Latency by System",
) -> Path:
    """Boxplot of latency distributions per system."""
    output_path = _ensure_dir(output_path)
    fig, ax = plt.subplots(figsize=(8, 5))

    labels = list(data.keys())
    values = [data[k] for k in labels]
    ax.boxplot(values, labels=labels, patch_artist=True)
    ax.set_ylabel("Latency (ms)")
    ax.set_title(title)
    sns.despine()
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    return output_path


def f1_vs_corpus_size(
    results: dict[str, list[tuple[int, float]]],
    output_path: Path,
    title: str = "F1 Score vs Corpus Size",
) -> Path:
    """Line chart of F1 score as a function of corpus size, per system.

    ``results`` maps system name to list of ``(corpus_size, f1)`` tuples.
    """
    output_path = _ensure_dir(output_path)
    fig, ax = plt.subplots(figsize=(8, 5))

    for system_name, points in results.items():
        points_sorted = sorted(points, key=lambda t: t[0])
        sizes = [p[0] for p in points_sorted]
        f1s = [p[1] for p in points_sorted]
        ax.plot(sizes, f1s, marker="o", label=system_name)

    ax.set_xlabel("Corpus Size (pages)")
    ax.set_ylabel("F1 Score")
    ax.set_title(title)
    ax.legend()
    sns.despine()
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    return output_path


def cost_quality_pareto(
    points: list[tuple[str, float, float]],
    output_path: Path,
    title: str = "Cost vs Quality Pareto Front",
) -> Path:
    """Scatter plot of cost (USD) vs quality (composite score).

    ``points`` is a list of ``(label, cost_usd, quality_score)`` tuples.
    """
    output_path = _ensure_dir(output_path)
    fig, ax = plt.subplots(figsize=(8, 5))

    labels = [p[0] for p in points]
    costs = [p[1] for p in points]
    qualities = [p[2] for p in points]

    ax.scatter(costs, qualities, s=80, zorder=3)
    for lbl, x, y in zip(labels, costs, qualities):
        ax.annotate(lbl, (x, y), textcoords="offset points", xytext=(5, 5), fontsize=8)

    ax.set_xlabel("Cost per Query (USD)")
    ax.set_ylabel("Composite Quality Score (0-10)")
    ax.set_title(title)
    sns.despine()
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    return output_path


def score_heatmap(
    scores: dict[tuple[str, str], float],
    output_path: Path,
    title: str = "Scores by System x Category",
) -> Path:
    """Heatmap of scores, rows = systems, columns = question categories.

    ``scores`` maps ``(system, category)`` to a score value.
    """
    output_path = _ensure_dir(output_path)

    systems = sorted({s for s, _ in scores})
    categories = sorted({c for _, c in scores})

    matrix = np.zeros((len(systems), len(categories)))
    for i, sys in enumerate(systems):
        for j, cat in enumerate(categories):
            matrix[i, j] = scores.get((sys, cat), 0.0)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(
        matrix,
        xticklabels=categories,
        yticklabels=systems,
        annot=True,
        fmt=".2f",
        cmap="YlOrRd",
        ax=ax,
    )
    ax.set_title(title)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
    return output_path


def radar_chart(
    system_metrics: dict[str, dict[str, float]],
    output_path: Path,
    title: str = "System Comparison Radar",
) -> Path:
    """Radar chart comparing multiple systems across metrics.

    ``system_metrics`` maps system name to a dict of metric_name -> value (0-1 scale).
    """
    output_path = _ensure_dir(output_path)

    metrics = sorted(next(iter(system_metrics.values())).keys())
    n_metrics = len(metrics)
    angles = np.linspace(0, 2 * np.pi, n_metrics, endpoint=False).tolist()
    angles += angles[:1]  # close the polygon

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

    for system_name, vals in system_metrics.items():
        values = [vals[m] for m in metrics]
        values += values[:1]
        ax.plot(angles, values, linewidth=2, label=system_name)
        ax.fill(angles, values, alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(metrics, size=9)
    ax.set_ylim(0, 1)
    ax.set_title(title, y=1.08)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return output_path

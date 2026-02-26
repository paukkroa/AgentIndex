"""Statistical analysis for evaluation experiments."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import stats


@dataclass
class TestResult:
    """Result of a statistical hypothesis test."""

    test_name: str
    statistic: float
    p_value: float
    effect_size: float | None = None
    ci_lower: float | None = None
    ci_upper: float | None = None
    significant: bool = False

    def to_dict(self) -> dict[str, float | str | bool | None]:
        return {
            "test_name": self.test_name,
            "statistic": self.statistic,
            "p_value": self.p_value,
            "effect_size": self.effect_size,
            "ci_lower": self.ci_lower,
            "ci_upper": self.ci_upper,
            "significant": self.significant,
        }


def cohens_d(group1: np.ndarray, group2: np.ndarray) -> float:
    """Compute Cohen's d effect size for two independent samples."""
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    if pooled_std == 0:
        return 0.0
    return float((np.mean(group1) - np.mean(group2)) / pooled_std)


def bootstrap_ci(
    data: np.ndarray, statistic_fn=np.mean, n_bootstrap: int = 10000, alpha: float = 0.05
) -> tuple[float, float]:
    """Compute bootstrap confidence interval for a statistic."""
    rng = np.random.default_rng(42)
    n = len(data)
    bootstrap_stats = np.array(
        [statistic_fn(rng.choice(data, size=n, replace=True)) for _ in range(n_bootstrap)]
    )
    lower = float(np.percentile(bootstrap_stats, 100 * alpha / 2))
    upper = float(np.percentile(bootstrap_stats, 100 * (1 - alpha / 2)))
    return lower, upper


def bonferroni_correction(p_values: list[float]) -> list[float]:
    """Apply Bonferroni correction for multiple comparisons."""
    m = len(p_values)
    return [min(p * m, 1.0) for p in p_values]


def paired_t_test(
    group1: np.ndarray, group2: np.ndarray, alpha: float = 0.05
) -> TestResult:
    """Paired t-test for two related samples."""
    stat, p = stats.ttest_rel(group1, group2)
    d = cohens_d(group1, group2)
    ci = bootstrap_ci(group1 - group2)
    return TestResult(
        test_name="paired_t_test",
        statistic=float(stat),
        p_value=float(p),
        effect_size=d,
        ci_lower=ci[0],
        ci_upper=ci[1],
        significant=float(p) < alpha,
    )


def wilcoxon_signed_rank(
    group1: np.ndarray, group2: np.ndarray, alpha: float = 0.05
) -> TestResult:
    """Wilcoxon signed-rank test (non-parametric paired test)."""
    diff = group1 - group2
    # Remove zeros (ties) for Wilcoxon
    diff_nonzero = diff[diff != 0]
    if len(diff_nonzero) == 0:
        return TestResult(
            test_name="wilcoxon_signed_rank",
            statistic=0.0,
            p_value=1.0,
            significant=False,
        )
    stat, p = stats.wilcoxon(diff_nonzero)
    d = cohens_d(group1, group2)
    return TestResult(
        test_name="wilcoxon_signed_rank",
        statistic=float(stat),
        p_value=float(p),
        effect_size=d,
        significant=float(p) < alpha,
    )


def mann_whitney_u(
    group1: np.ndarray, group2: np.ndarray, alpha: float = 0.05
) -> TestResult:
    """Mann-Whitney U test (non-parametric independent samples test)."""
    stat, p = stats.mannwhitneyu(group1, group2, alternative="two-sided")
    d = cohens_d(group1, group2)
    return TestResult(
        test_name="mann_whitney_u",
        statistic=float(stat),
        p_value=float(p),
        effect_size=d,
        significant=float(p) < alpha,
    )


def two_way_anova(
    data: dict[tuple[str, str], np.ndarray],
) -> dict[str, TestResult]:
    """Simplified two-way ANOVA using independent F-tests for each factor.

    ``data`` keys are ``(system, category)`` tuples mapping to score arrays.
    Returns test results for the system factor, category factor, and interaction.
    """
    # Gather by factor
    systems: dict[str, list[float]] = {}
    categories: dict[str, list[float]] = {}
    for (sys, cat), values in data.items():
        systems.setdefault(sys, []).extend(values.tolist())
        categories.setdefault(cat, []).extend(values.tolist())

    # One-way ANOVA by system
    sys_groups = [np.array(v) for v in systems.values()]
    if len(sys_groups) >= 2:
        f_sys, p_sys = stats.f_oneway(*sys_groups)
    else:
        f_sys, p_sys = 0.0, 1.0

    # One-way ANOVA by category
    cat_groups = [np.array(v) for v in categories.values()]
    if len(cat_groups) >= 2:
        f_cat, p_cat = stats.f_oneway(*cat_groups)
    else:
        f_cat, p_cat = 0.0, 1.0

    return {
        "system_factor": TestResult(
            test_name="anova_system",
            statistic=float(f_sys),
            p_value=float(p_sys),
            significant=float(p_sys) < 0.05,
        ),
        "category_factor": TestResult(
            test_name="anova_category",
            statistic=float(f_cat),
            p_value=float(p_cat),
            significant=float(p_cat) < 0.05,
        ),
    }


def run_comparative_analysis(
    scores_a: np.ndarray,
    scores_b: np.ndarray,
    label_a: str = "System A",
    label_b: str = "System B",
) -> dict[str, TestResult]:
    """Run the full suite of comparative statistical tests."""
    results: dict[str, TestResult] = {}

    if len(scores_a) == len(scores_b):
        results["paired_t"] = paired_t_test(scores_a, scores_b)
        results["wilcoxon"] = wilcoxon_signed_rank(scores_a, scores_b)

    results["mann_whitney"] = mann_whitney_u(scores_a, scores_b)

    # Apply Bonferroni correction
    p_vals = [r.p_value for r in results.values()]
    corrected = bonferroni_correction(p_vals)
    for (key, result), p_corr in zip(results.items(), corrected):
        result.p_value = p_corr
        result.significant = p_corr < 0.05

    return results

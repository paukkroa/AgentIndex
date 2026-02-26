---
id: 0.0.19.3
title: "statistics— Mathematical statistics functions¶"
nav_summary: "The `statistics` module in Python (introduced in **Python 3"
ref: https://docs.python.org/3/library/statistics.html
ref_type: url
---

# statistics— Mathematical statistics functions¶

The `statistics` module in Python (introduced in **Python 3.4**) provides lightweight, built-in functions for calculating fundamental mathematical statistics on numeric datasets, targeting users who require basic statistical operations akin to graphing calculators or scientific tools. It supports **`int`**, **`float`**, **`Decimal`**, and **`Fraction`** types, but not mixed-type collections or unsupported numeric types. Key features include **central tendency measures** (arithmetic mean via `mean()` and `fmean()`, geometric/harmonic means, and median variants like `median()`, `median_low()`, and `median_high()`), **distribution estimation** (kernel density estimation via `kde()` and random sampling via `kde_random()`), and **mode calculations** (`mode()` and `multimode()`). Notably, functions relying on sorting or counting (e.g., median, mode) may yield **undefined or erroneous results** when encountering `NaN` values, requiring explicit preprocessing (e.g., filtering via `filterfalse(isnan, data)`). This module is **not a replacement** for advanced libraries like NumPy or SciPy but serves as a convenient, no-installation-required solution for

[Link to original](https://docs.python.org/3/library/statistics.html)

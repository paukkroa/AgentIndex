---
id: 0.0.19.0.1
title: "cmath— Mathematical functions for complex numbers¶"
nav_summary: "`cmath` module: Complex math functions (polar, trig, log, sqrt)."
ref: https://docs.python.org/3/library/cmath.html
ref_type: url
---

# cmath— Mathematical functions for complex numbers¶

The `cmath` module in Python provides a comprehensive set of mathematical functions tailored for complex numbers, extending beyond basic arithmetic to include polar conversions, power/logarithmic operations, trigonometric/hyperbolic functions, and classification utilities. It supports inputs as integers, floats, or complex numbers, as well as objects with `__complex__()` or `__float__()` methods for type conversion. Key features include **polar coordinate conversions** (`phase`, `polar`, `rect`), **exponential/logarithmic functions** (`exp`, `log`, `log10`, `sqrt`), **trigonometric/hyperbolic functions** (`sin`, `cos`, `tan`, `sinh`, `cosh`, `tanh`, and their inverses), and **branch-cut handling** aligned with Kahan’s standards (e.g., distinguishing branch cuts via sign of zero). For example, `cmath.sqrt(-2-0j)` returns a negative imaginary result due to its position relative to the branch cut. Classification functions like `isfinite(z)` validate numerical properties.

---

[Link to original](https://docs.python.org/3/library/cmath.html)

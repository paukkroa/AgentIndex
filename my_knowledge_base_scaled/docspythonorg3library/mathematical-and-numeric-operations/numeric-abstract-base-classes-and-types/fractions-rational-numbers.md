---
id: 0.0.19.1.2
title: "fractions— Rational numbers¶"
nav_summary: "Python’s `fractions` module for"
ref: https://docs.python.org/3/library/fractions.html
ref_type: url
---

# fractions— Rational numbers¶

The `fractions` module in Python provides precise arithmetic support for **rational numbers** (fractions) by implementing the `Fraction` class, which avoids floating-point inaccuracies inherent in standard numeric types. A `Fraction` can be constructed from **numerator/denominator pairs**, a **single rational number** (e.g., `float`, `Decimal`), or a **string** (e.g., `"3/7"` or `"1.414"`). Key features include:
- **Automatic simplification** (e.g., `Fraction(16, -10)` simplifies to `-8/5`).
- **String parsing** with flexible formats (e.g., `"7e-6"` → `7/1000000`).
- **Floating-point handling** with caveats (e.g., `Fraction(1.1)` uses `as_integer_ratio()` due to binary precision limits).
- **Methods** like `limit_denominator(n)` to approximate fractions with bounded denominators.
- Inheritance from `numbers.Rational`, enabling compatibility with Python’s numeric type hierarchy.

[Link to original](https://docs.python.org/3/library/fractions.html)

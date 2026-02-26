---
id: 0.0.19.1.1
title: "decimal— Decimal fixed-point and floating-point arithmetic¶"
nav_summary: "The `decimal` module in Python provides **high-precision decimal arithmetic** (fixed-point and floating-point) with exact representation and rounding"
ref: https://docs.python.org/3/library/decimal.html
ref_type: url
---

# decimal— Decimal fixed-point and floating-point arithmetic¶

The `decimal` module in Python provides **high-precision decimal arithmetic** (fixed-point and floating-point) with exact representation and rounding control, addressing limitations of binary floating-point (`float`). Key features include:
- **Exact decimal representation** (e.g., `0.1 + 0.2 = 0.3` instead of binary floating-point inaccuracies).
- **Significant digit preservation** (e.g., `1.30 + 1.20 = 2.50` with trailing zeros).
- **User-configurable precision** (default: 28 digits, adjustable via `getcontext().prec`).
- **Standard-compliant rounding** (IEEE 854/ANSI/IEC 80002) with customizable rules (e.g., `ROUND_HALF_UP`, `ROUND_CEILING`).
- **Context-based arithmetic** (precision, rounding, overflow/underflow handling).
- **Immutable decimal objects** with sign, coefficient, exponent, and special values (`Infinity`, `NaN`, `-0/+0`).
- **Signal handling** for inexact operations (e.g., rounding, overflow) via exceptions

[Link to original](https://docs.python.org/3/library/decimal.html)

---
id: 0.0.19.1.0
title: "numbers— Numeric abstract base classes¶"
nav_summary: "`numbers` module: numeric ABC hierarchy (Complex, Real, Rational"
ref: https://docs.python.org/3/library/numbers.html
ref_type: url
---

# numbers— Numeric abstract base classes¶

The `numbers` module in Python defines a hierarchical system of **abstract base classes (ABCs)**—rooted in `numbers.Number`—to standardize numeric type behavior across built-in and custom numeric types. This **numeric tower** enforces progressive abstraction: `numbers.Complex` supports core operations like arithmetic (`+`, `-`, `*`, `/`, `**`), comparisons (`==`, `!=`), and complex-specific methods (`real`, `imag`, `conjugate`), while `numbers.Real` extends it with real-number operations (e.g., `floor`, `ceil`, `round`, `divmod`). `numbers.Rational` further refines this by adding `numerator`/`denominator` properties for fractional representation, ensuring lowest-term integers. These ABCs enable type checking (e.g., `isinstance(x, numbers.Number)`) and enforce consistent numeric behavior without direct instantiation. The module aligns with **PEP 3141** and serves as a foundation for custom numeric types (e.g., `Decimal`, `Fraction`) by defining abstract methods and default implementations.

---

[Link to original](https://docs.python.org/3/library/numbers.html)

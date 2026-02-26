---
id: 0.0.0.3.2
title: "operator— Standard operators as functions¶"
nav_summary: "`operator` module: Functions for Python operators as callable alternatives."
ref: https://docs.python.org/3/library/operator.html
ref_type: url
---

# operator— Standard operators as functions¶

The `operator` module provides a collection of **efficient, function-based alternatives** to Python’s built-in operators, mapping intrinsic syntax (e.g., `x + y`) to explicit function calls (e.g., `operator.add(x, y)`). Functions are categorized into **comparison** (e.g., `lt`, `eq`, `gt`), **logical** (e.g., `not_`, `truth`, `is_`), **mathematical**, and **sequence operations**. Comparison functions mirror rich comparison operators (`<`, `==`, `>=`, etc.), while logical functions include truth testing (`truth`), identity checks (`is_`), and boolean negation (`not_`). Both underscore-prefixed (e.g., `__eq__`) and underscore-free variants exist, with the latter preferred for clarity. These functions are optimized for performance and interoperability with higher-order functions (e.g., `map`, `filter`), enabling cleaner functional programming patterns.

---

[Link to original](https://docs.python.org/3/library/operator.html)

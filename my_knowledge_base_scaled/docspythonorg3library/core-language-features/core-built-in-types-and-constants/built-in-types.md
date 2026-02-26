---
id: 0.0.0.0.0
title: "Built-in Types¶"
nav_summary: "Core Python types: numerics, sequences, mappings, classes, exceptions."
ref: https://docs.python.org/3/library/stdtypes.html
ref_type: url
---

# Built-in Types¶

The **Built-in Types** documentation in Python outlines the core data types integrated into the interpreter, categorized into numerics (e.g., integers, floats), sequences (e.g., strings, lists), mappings (e.g., dictionaries), classes, instances, and exceptions. Key features include mutable collection types (e.g., lists, sets) where in-place operations return `None`, while immutable types (e.g., tuples) preserve identity. All objects support fundamental operations like equality checks (`==`), truth value testing (via `__bool__()` or `__len__()`), and string conversion (via `repr()` or `str()`). Truth testing defaults to `False` for `None`, `False`, zero values, or empty containers. Boolean operations (`and`, `or`, `not`) short-circuit for efficiency, with `not` having lower precedence than comparisons. Comparisons can be chained (e.g., `x < y <= z`) and evaluate operands lazily for performance.

---

[Link to original](https://docs.python.org/3/library/stdtypes.html)

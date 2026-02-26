---
id: 0.0.0.2
title: "enum— Support for enumerations¶"
nav_summary: "The `enum` module in Python (introduced in **Python 3"
ref: https://docs.python.org/3/library/enum.html
ref_type: url
---

# enum— Support for enumerations¶

The `enum` module in Python (introduced in **Python 3.4**) provides robust support for **enumerations**, enabling the creation of symbolic names bound to unique values. Enumerations are **immutable**, **iterable**, and support **callable syntax** (e.g., `Color(1)`) and **indexing** (e.g., `Color.RED`). They can be defined using **class syntax** (e.g., `class Color(Enum): RED = 1`) or **functional syntax** (e.g., `Enum('Color', [('RED', 1)])`). While syntactically resembling classes, enums are **not standard Python classes** and offer specialized behavior like **automatic iteration**, **value-based access**, and **type safety**.

Key features include:
- **Base Classes**: `Enum` (generic), `IntEnum` (subclass of `int`), `StrEnum` (subclass of `str`), `Flag` (bitwise-compatible), and `IntFlag` (bitwise-compatible `int`).
- **Specialized Enums**: `ReprEnum` (preserves mixed-in type representation), `EnumCheck` (validation flags

[Link to original](https://docs.python.org/3/library/enum.html)

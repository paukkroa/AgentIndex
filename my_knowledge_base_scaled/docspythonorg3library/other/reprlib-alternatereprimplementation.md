---
id: 0.0.24.3
title: "reprlib— Alternaterepr()implementation¶"
nav_summary: "`reprlib: Truncate object reprs with configurable size limits`"
ref: https://docs.python.org/3/library/reprlib.html
ref_type: url
---

# reprlib— Alternaterepr()implementation¶

The `reprlib` module offers an alternative implementation of Python’s built-in `repr()` function, designed to generate compact string representations of objects while enforcing configurable size limits to prevent excessively long output. It provides a `Repr` class with customizable depth and type-specific constraints (e.g., `maxlist`, `maxdict`, `maxstring`) to truncate nested structures like lists, dictionaries, or strings. The module includes a pre-configured instance `aRepr` and a `repr()` function that applies these limits. Additionally, it features the `@recursive_repr` decorator to handle recursive `__repr__()` calls by substituting a placeholder (e.g., `'...'`) when cycles are detected, avoiding infinite recursion. Key attributes like `fillvalue` and `indent` allow further customization of output formatting. This module is particularly useful in debugging tools (e.g., the Python debugger) or scenarios requiring controlled string representations.

---

[Link to original](https://docs.python.org/3/library/reprlib.html)

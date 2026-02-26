---
id: 0.0.1.4
title: "Built-in Constants¶"
nav_summary: "`Python’s immutable built-in constants: False, True, None, NotImplemented, Ellipsis`"
ref: https://docs.python.org/3/library/constants.html
ref_type: url
---

# Built-in Constants¶

The **Built-in Constants** in Python are immutable, predefined objects embedded in the interpreter’s namespace, including `False`, `True`, `None`, `NotImplemented`, and `Ellipsis`. These constants serve foundational roles: `False`/`True` represent boolean values (immutable and reassignable via syntax error), `None` denotes absence of a value (type `NoneType`), and `NotImplemented` signals unsupported binary operations (type `NotImplementedType`). `Ellipsis` (type `EllipsisType`) is used for omitted data (e.g., slicing). Key behaviors include:
- **`NotImplemented`**: Triggers fallback operations in binary methods (e.g., `__eq__`), raising exceptions if unresolved; deprecated boolean evaluation (now raises `TypeError` in Python ≥3.14).
- **Immutability**: Assignments to these constants raise `SyntaxError` (except `Ellipsis` via literal `...`).
- **Type Safety**: Each constant is a singleton of its respective type (`bool`, `NoneType`, etc.).

---

[Link to original](https://docs.python.org/3/library/constants.html)

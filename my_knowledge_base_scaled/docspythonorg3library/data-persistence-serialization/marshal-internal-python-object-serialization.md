---
id: 0.0.4.4
title: "marshal— Internal Python object serialization¶"
nav_summary: "`marshal` – Binary Python serialization for `.pyc` files (limited types, no version guarantees)."
ref: https://docs.python.org/3/library/marshal.html
ref_type: url
---

# marshal— Internal Python object serialization¶

The `marshal` module provides Python’s internal binary serialization for reading/writing Python objects in a machine-independent format, primarily designed for `.pyc` file handling (storing compiled bytecode). Unlike `pickle`, it lacks version compatibility guarantees, as the format may change between Python versions (e.g., code objects are incompatible across versions). Supported types include numeric values (`int`, `float`, `complex`), strings/bytes, containers (`tuple`, `list`, `set`, `frozenset`, `slice`), and singletons (`None`, `Ellipsis`). File/bytes operations are supported, but recursive structures require version 3+ (added in 3.4). **Security warning:** Untrusted data must never be unmarshaled due to potential malicious payloads.

---

[Link to original](https://docs.python.org/3/library/marshal.html)

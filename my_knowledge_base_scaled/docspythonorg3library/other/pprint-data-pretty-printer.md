---
id: 0.0.24.2
title: "pprint— Data pretty printer¶"
nav_summary: "The `pprint` module in Python’s standard library provides a **formatted, human-readable representation** of arbitrary Python data structures (e"
ref: https://docs.python.org/3/library/pprint.html
ref_type: url
---

# pprint— Data pretty printer¶

The `pprint` module in Python’s standard library provides a **formatted, human-readable representation** of arbitrary Python data structures (e.g., lists, dicts, dataclasses) for debugging or logging. It intelligently **wraps output to fit within a specified width** (default: 80 chars), breaking long structures across lines while preserving readability. Key features include:
- **Customizable formatting** via parameters like `indent` (spacing), `width` (line length), `depth` (nesting limit), and `compact` (collapsing sequences).
- **Dictionary sorting** (`sort_dicts`) to enforce key ordering or preserve insertion order.
- **Thousands separators** (`underscore_numbers`) for numeric readability.
- **Compatibility** with modern types like `types.SimpleNamespace` (since 3.9) and `dataclasses.dataclass` (since 3.10).
- **Interactive use**: Replace `print()` with `pprint.pp` for cleaner inspection in REPLs.
- **Limitations**: Non-literal objects (e.g., files, sockets) may not reconstruct correctly when reloaded.

---

[Link to original](https://docs.python.org/3/library/pprint.html)

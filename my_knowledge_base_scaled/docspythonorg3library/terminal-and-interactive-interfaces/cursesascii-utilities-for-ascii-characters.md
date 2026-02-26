---
id: 0.0.21.2
title: "curses.ascii— Utilities for ASCII characters¶"
nav_summary: "ASCII constants & membership utilities for terminal/character handling."
ref: https://docs.python.org/3/library/curses.ascii.html
ref_type: url
---

# curses.ascii— Utilities for ASCII characters¶

The `curses.ascii` module provides a standardized set of named constants for ASCII control characters, enabling programmatic access to their integer values (0–31, 127) via descriptive names like `curses.ascii.LF` (Line Feed) or `curses.ascii.BEL` (Bell). It also includes utility functions to classify characters into predefined ASCII categories (e.g., whitespace, printable, or control codes) via membership tests. These constants and functions are essential for terminal handling, data parsing, and low-level communication protocols, offering a clean abstraction over raw ASCII byte values. The module supports legacy terminal operations and character set manipulations (e.g., `SO`/`SI` for alternate character sets) while maintaining compatibility with the broader `curses` library for terminal display management.

---

[Link to original](https://docs.python.org/3/library/curses.ascii.html)

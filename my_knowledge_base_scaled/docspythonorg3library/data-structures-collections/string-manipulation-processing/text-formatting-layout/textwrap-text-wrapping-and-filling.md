---
id: 0.0.1.0.3.1
title: "textwrap— Text wrapping and filling¶"
nav_summary: "The `textwrap` module in Python provides utilities for formatting text by wrapping, filling, or shortening strings to fit specified constraints"
ref: https://docs.python.org/3/library/textwrap.html
ref_type: url
---

# textwrap— Text wrapping and filling¶

The `textwrap` module in Python provides utilities for formatting text by wrapping, filling, or shortening strings to fit specified constraints. It offers two primary approaches: **convenience functions** (`wrap`, `fill`, `shorten`) for one-off tasks and the **`TextWrapper` class** for reusable, configurable text processing. Key features include:
- **`wrap()`**: Splits text into lines of a specified `width`, returning a list of lines with optional indentation, tab handling, and sentence/word breaking rules (e.g., `break_long_words`, `break_on_hyphens`).
- **`fill()`**: Joins wrapped lines into a single string (equivalent to `"\n".join(wrap(...))`), preserving all `wrap()` parameters.
- **`shorten()`**: Collapses whitespace and truncates text to fit `width`, appending a placeholder (e.g., `" [...]"`) if truncation occurs. Whitespace is normalized before processing.
- **`TextWrapper` class**: A configurable object with attributes like `initial_indent`, `subsequent_indent`, `expand_tabs`, and `tabsize` to customize behavior. Supports methods like `wrap()`, `fill()`,

[Link to original](https://docs.python.org/3/library/textwrap.html)

---
id: 0.0.1.1.1
title: "rlcompleter— Completion function for GNU readline¶"
nav_summary: "`rlcompleter: Python readline autocompletion module`"
ref: https://docs.python.org/3/library/rlcompleter.html
ref_type: url
---

# rlcompleter— Completion function for GNU readline¶

The `rlcompleter` module provides a completion function tailored for GNU `readline`, enabling intelligent tab-based autocompletion in Python’s interactive shell. When imported on Unix systems with `readline` support, it automatically registers a `Completer` instance, setting its `complete()` method as the default readline completer. This method supports completing Python identifiers, keywords, and module attributes (e.g., `readline.`, `os.`) by leveraging `dir()` and safe attribute access. On platforms without `readline`, the `Completer` class remains usable for custom completion logic. The module integrates seamlessly with Python’s interactive mode (unless run with `-S`), offering dynamic suggestions for `__main__`, `builtins`, and dotted paths (e.g., `numpy.array`).

---

[Link to original](https://docs.python.org/3/library/rlcompleter.html)

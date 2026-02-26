---
id: 0.0.14.2.0
title: "doctest— Test interactive Python examples¶"
nav_summary: "`doctest` module tests embedded Python examples in docstrings."
ref: https://docs.python.org/3/library/doctest.html
ref_type: url
---

# doctest— Test interactive Python examples¶

The `doctest` module in Python automates the testing of interactive Python examples embedded in docstrings or source files. It parses text blocks resembling Python REPL sessions (prefixed with `>>>`) to validate that the documented behavior matches actual execution. Key use cases include verifying module docstrings, regression testing, and creating executable documentation ("literate testing"). The module executes examples, compares outputs (including error traces), and reports discrepancies. By default, running a script with `doctest.testmod()` silently confirms success; verbose mode (`-v`) details each test. Features include colorized output (default in Python 3.13+) and integration with standard test suites. Example modules embed doctests in docstrings, where `>>>`-prefixed snippets demonstrate function behavior, including edge cases and errors.

---

[Link to original](https://docs.python.org/3/library/doctest.html)

---
id: 0.0.14.1
title: "pydoc— Documentation generator and online help system¶"
nav_summary: "`pydoc`: CLI/HTTP doc generator for Python modules, classes, and functions."
ref: https://docs.python.org/3/library/pydoc.html
ref_type: url
---

# pydoc— Documentation generator and online help system¶

The `pydoc` module is a built-in Python tool for generating and serving documentation from Python modules, classes, functions, and methods. It extracts docstrings (`__doc__` attributes) or falls back to source comments if unavailable, enabling interactive help via the `help()` function or command-line execution (`python -m pydoc`). Output can be displayed as text (with pagination via `MANPAGER`/`PAGER`), saved as HTML (`-w` flag), or searched by keyword (`-k` flag). It also supports a local HTTP server (`-p <port>`) to browse documentation via a web browser, with optional hostname specification (`-n <hostname>`). Modules are dynamically imported, so module-level code may execute; use `if __name__ == '__main__':` guards to avoid unintended execution.

---

[Link to original](https://docs.python.org/3/library/pydoc.html)

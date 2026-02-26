---
id: 0.0.15.4
title: "pdb— The Python Debugger¶"
nav_summary: "`pdb: Python debugger with breakpoints, stepping, and post-mortem support.`"
ref: https://docs.python.org/3/library/pdb.html
ref_type: url
---

# pdb— The Python Debugger¶

The `pdb` module provides an **interactive source-level debugger** for Python, enabling developers to inspect variables, set breakpoints, step through code, and evaluate expressions dynamically. Key features include **conditional breakpoints**, **single-stepping (step, next, continue)**, **stack frame inspection**, **source code listing**, and **post-mortem debugging** (automatic activation on crashes). The debugger is extensible via the [`bdb`](bdb.html) framework and [`cmd`](cmd.html) module, supporting custom command-line interfaces. Usage is simplified via `breakpoint()` (built-in since Python 3.7) or `pdb.set_trace()`, with tab-completion for commands (since Python 3.3). It also supports **command-line invocation** (`python -m pdb`) for debugging scripts, modules, or processes by PID, with optional automatic restart after debugging sessions. Integrates with [`faulthandler`](faulthandler.html) for traceback dumps and [`traceback`](traceback.html) for stack trace management.

---

[Link to original](https://docs.python.org/3/library/pdb.html)

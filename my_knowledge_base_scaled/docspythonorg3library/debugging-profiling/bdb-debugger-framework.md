---
id: 0.0.15.2
title: "bdb— Debugger framework¶"
nav_summary: "Core Python debugger framework for breakpoints & execution control."
ref: https://docs.python.org/3/library/bdb.html
ref_type: url
---

# bdb— Debugger framework¶

The `bdb` module in Python’s standard library provides a foundational debugger framework for setting breakpoints, managing execution flow, and debugging code. It defines the **`BdbQuit`** exception for debugger termination and two core classes: **`Breakpoint`** and **`Bdb`**. The **`Breakpoint`** class enables temporary, conditional, or disabled breakpoints, indexed by number (`bpbynumber`) or file-line pairs (`bplist`). Breakpoints support attributes like `file`, `line`, `temporary`, and `hits`, along with methods for deletion (`deleteMe`), enabling/disabling (`enable`/`disable`), and formatting/printing breakpoint details (`bpformat`/`bpprint`). Breakpoints can be tied to specific functions (`funcname`) or conditional logic (`cond`), with hit counts tracked for debugging precision. This module serves as a low-level building block for higher-level debugging tools.

---

[Link to original](https://docs.python.org/3/library/bdb.html)

---
id: 0.0.20.5
title: "cmd— Support for line-oriented command interpreters¶"
nav_summary: "`cmd` module: Build CLI interpreters with command parsing & history support."
ref: https://docs.python.org/3/library/cmd.html
ref_type: url
---

# cmd— Support for line-oriented command interpreters¶

The `cmd` module in Python provides a framework for creating **line-oriented command interpreters**, ideal for test harnesses, administrative tools, or prototypes requiring a simple CLI. The core class, `cmd.Cmd`, serves as a superclass for custom interpreters, encapsulating methods for parsing and executing commands. Key features include **automatic command completion** (via `readline` integration, defaulting to `Tab`/`^I` for `editline` backends) and **interactive input handling** with history navigation (e.g., `Ctrl+P`, `Ctrl+N`). The `cmdloop()` method drives the interpreter loop, prompting for input, parsing commands, and dispatching them to user-defined action methods. Customization is supported via attributes like `intro` (banner text) and `stdin/stdout` redirection, though `use_rawinput` must be `False` for custom input streams. Backward compatibility notes highlight changes in `3.13` (e.g., `editline` handling of `Tab`). This module is lightweight but powerful for rapid CLI development.

---

[Link to original](https://docs.python.org/3/library/cmd.html)

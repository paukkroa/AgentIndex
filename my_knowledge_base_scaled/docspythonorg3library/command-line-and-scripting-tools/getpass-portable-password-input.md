---
id: 0.0.20.4
title: "getpass— Portable password input¶"
nav_summary: "`getpass` module: secure password input & username retrieval."
ref: https://docs.python.org/3/library/getpass.html
ref_type: url
---

# getpass— Portable password input¶

The `getpass` module in Python provides **secure password input handling** with cross-platform compatibility, offering two core functions: `getpass()` and `getuser()`. The `getpass.getpass()` function securely prompts users for a password without echoing input by default, with optional customization via `prompt` and `echo_char` (e.g., `'*'` for asterisks). It dynamically adapts to terminal capabilities, falling back to `sys.stdin` if secure input isn’t available, raising a `GetPassWarning`. On Unix, it uses **noncanonical terminal mode** for input masking, though this disables line-editing shortcuts. The `getpass.getuser()` function retrieves the system username by checking environment variables (`LOGNAME`, `USER`, etc.) or the password database (`pwd` module), preferred over `os.getlogin()`. Introduced in Python 3.13/3.14, it supports **WASI-exclusive availability** and integrates with standard library command-line utilities.

---

[Link to original](https://docs.python.org/3/library/getpass.html)

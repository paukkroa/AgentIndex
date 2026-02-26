---
id: 0.0.15.1
title: "Audit events table¶"
nav_summary: "The **Audit Events Table** in CPython (introduced in **Python 3"
ref: https://docs.python.org/3/library/audit_events.html
ref_type: url
---

# Audit events table¶

The **Audit Events Table** in CPython (introduced in **Python 3.8+** via [PEP 578](https://peps.python.org/pep-0578/)) documents all runtime events triggered by `sys.audit()` or `PySys_Audit()` calls across the interpreter, standard library, and core modules. These events enable fine-grained monitoring of critical operations like thread creation (`_thread.start_new_thread`), code compilation (`compile`), interpreter state management (`PyInterpreterState_New/Clear`), and low-level system interactions (e.g., `ctypes` operations like `dlopen`, `dlsym`, or memory buffers). The table lists **100+ events** (e.g., `builtins.id`, `sys.run_file`, `cpython.run_command`) with their arguments and references, though it is **CPython-specific**—other implementations may vary. Developers can register audit hooks via `sys.addaudithook()` or `PySys_AddAuditHook()` to log or analyze these events for debugging, security, or profiling. Key use cases include tracking module execution (`run_module`), interactive hooks (`run_interactivehook`), or system-level hooks (

[Link to original](https://docs.python.org/3/library/audit_events.html)

---
id: 0.0.8.0.2
title: "errno— Standard errno system symbols¶"
nav_summary: "`errno` module: maps system error codes to Python exceptions."
ref: https://docs.python.org/3/library/errno.html
ref_type: url
---

# errno— Standard errno system symbols¶

The `errno` module in Python provides standardized system error symbols derived from the Linux kernel’s `errno.h`, mapping integer error codes to descriptive names (e.g., `errno.EPERM` for "Operation not permitted"). It includes a dictionary (`errno.errorcode`) for reverse-lookup of numeric codes to their symbolic names (e.g., `errno.errorcode[errno.EPERM]` returns `'EPERM'`). Not all error codes are platform-specific; undefined symbols can be checked via `errno.errorcode.keys()`. Many errors correspond to Python exceptions (e.g., `EPERM` → `PermissionError`, `ENOENT` → `FileNotFoundError`), enabling consistent error handling. Use `os.strerror()` to convert numeric codes to human-readable messages.

---

[Link to original](https://docs.python.org/3/library/errno.html)

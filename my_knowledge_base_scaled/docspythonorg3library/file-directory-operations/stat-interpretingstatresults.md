---
id: 0.0.3.4
title: "stat— Interpretingstat()results¶"
nav_summary: "`stat` module interprets `os.stat()` file metadata via type-checking macros."
ref: https://docs.python.org/3/library/stat.html
ref_type: url
---

# stat— Interpretingstat()results¶

The `stat` module in Python provides constants and functions to interpret the results of `os.stat()`, `os.fstat()`, and `os.lstat()` calls, enabling detailed file metadata analysis. It includes type-checking macros like `S_ISDIR()`, `S_ISREG()`, `S_ISLNK()`, etc., to determine if a file is a directory, regular file, symbolic link, or other special file types (e.g., sockets, devices). Additional functions like `S_IMODE()` extract permission bits (e.g., read/write/execute) and `S_IFMT()` isolates the file type identifier. Optimized for performance, these macros avoid redundant `stat()` calls when testing multiple attributes of the same file. Useful for advanced filesystem operations, such as recursive directory traversal (e.g., `walktree()` example), where low-level file type checks are required. Introduced in Python 3.4, it supports newer file types like doors, ports, and whiteouts.

---

[Link to original](https://docs.python.org/3/library/stat.html)

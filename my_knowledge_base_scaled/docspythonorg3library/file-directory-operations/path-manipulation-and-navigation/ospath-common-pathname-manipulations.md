---
id: 0.0.3.0.2
title: "os.path— Common pathname manipulations¶"
nav_summary: "The `os"
ref: https://docs.python.org/3/library/os.path.html
ref_type: url
---

# os.path— Common pathname manipulations¶

The `os.path` module provides essential functions for manipulating filesystem paths in Python, offering cross-platform compatibility for common operations like path normalization, joining, splitting, and checking file/directory attributes. It supports string, bytes, or `os.PathLike` objects as input/output, ensuring flexibility. Key features include:
- **Path Resolution:** `abspath()` converts relative paths to absolute paths, while `normpath()` standardizes separators and removes redundant components (e.g., `./` or `../`).
- **Path Construction:** `join()` combines path components intelligently (e.g., `/home/user` + `file.txt` → `/home/user/file.txt`).
- **Path Decomposition:** `split()` and `basename()` isolate directory and filename components, respectively (e.g., `/home/user/file.txt` → `('home/user', 'file.txt')`).
- **File/Directory Checks:** Functions like `exists()`, `isdir()`, and `isfile()` verify filesystem entities without raising exceptions for invalid characters (since Python 3.8).
- **Shell-like Expansions:** `expanduser()` and `expandvars()` enable user home directory (`~`) and environment variable substitutions (e.g.,

[Link to original](https://docs.python.org/3/library/os.path.html)

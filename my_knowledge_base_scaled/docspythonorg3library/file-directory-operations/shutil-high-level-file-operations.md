---
id: 0.0.3.5
title: "shutil— High-level file operations¶"
nav_summary: "`shutil` module: High-level file/directory operations (copy, move, delete)."
ref: https://docs.python.org/3/library/shutil.html
ref_type: url
---

# shutil— High-level file operations¶

The `shutil` module in Python provides high-level utilities for file and directory operations, simplifying tasks like copying, moving, renaming, and deleting files/directories while preserving metadata where possible. Key functions include:
- **`copyfileobj()`**: Copies raw file contents between file-like objects (e.g., streams) with optional chunked buffering. Note: Destination stream may not be flushed automatically; explicit `flush()`/`close()` is required for reliable writes.
- **`copyfile()`**: Copies file contents (excluding metadata) from *src* to *dst* efficiently. Fails if *dst* is unwritable or if *src* and *dst* reference the same file (raises `SameFileError`). Symbolic links are followed by default unless `follow_symlinks=False`.
- **Limitations**: Metadata (e.g., ownership, ACLs, resource forks) is not preserved across platforms (POSIX, Windows, macOS). For metadata-aware operations, use `os` module functions or platform-specific tools.

[Link to original](https://docs.python.org/3/library/shutil.html)

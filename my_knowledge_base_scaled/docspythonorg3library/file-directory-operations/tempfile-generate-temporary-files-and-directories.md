---
id: 0.0.3.2
title: "tempfile— Generate temporary files and directories¶"
nav_summary: "`tempfile` module: secure temp files/dirs, auto-cleanup"
ref: https://docs.python.org/3/library/tempfile.html
ref_type: url
---

# tempfile— Generate temporary files and directories¶

The `tempfile` module provides secure, platform-independent tools for generating temporary files and directories in Python. It offers high-level abstractions like `TemporaryFile`, `NamedTemporaryFile`, `TemporaryDirectory`, and `SpooledTemporaryFile`, which automatically handle cleanup via context managers or garbage collection. Lower-level functions (`mkstemp()` and `mkdtemp()`) allow manual control over temporary resources. All names include cryptographically secure random strings to prevent collisions. Key features include:
- **Automatic cleanup** (via context managers or garbage collection).
- **Secure naming** (randomized strings for uniqueness).
- **Cross-platform support** (Unix, Windows, etc.), with Unix-specific optimizations like immediate directory entry removal.
- **Customizable parameters** (location, prefix/suffix, mode, buffering, encoding).
- **File-like objects** with POSIX compatibility and underlying file access via the `file` attribute.
- **Spooled files** for large data handling (via `SpooledTemporaryFile`).
- **Backward compatibility** with keyword arguments recommended for clarity.

[Link to original](https://docs.python.org/3/library/tempfile.html)

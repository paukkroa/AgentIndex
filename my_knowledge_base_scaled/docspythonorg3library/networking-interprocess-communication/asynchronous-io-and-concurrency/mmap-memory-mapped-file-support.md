---
id: 0.0.10.1.2
title: "mmap— Memory-mapped file support¶"
nav_summary: "`mmap` module: memory-mapped file I/O (bytearray-like, cross-platform)."
ref: https://docs.python.org/3/library/mmap.html
ref_type: url
---

# mmap— Memory-mapped file support¶

The `mmap` module in Python provides **memory-mapped file support**, enabling efficient access to files as if they were in-memory byte arrays. Memory-mapped files behave like a hybrid of `bytearray` and file objects, allowing direct byte manipulation (e.g., `obj[index] = 97` or slice assignment) and file operations like `seek()` and `read()`. Created via the `mmap.mmap()` constructor, these objects require a file descriptor (obtained via `fileno()` or `os.open()`) and optionally specify access modes (`ACCESS_READ`, `ACCESS_WRITE`, `ACCESS_COPY`, or `ACCESS_DEFAULT`). On Unix/Windows, mappings can be read-only, write-through, or copy-on-write, with modifications persisting to the file only for `ACCESS_WRITE`. Anonymous mappings (e.g., for shared memory) use `fileno=-1`. Flushing buffered files before mapping ensures consistency. Introduced in Python 3.7, `ACCESS_DEFAULT` defers to the `prot` parameter.

---

[Link to original](https://docs.python.org/3/library/mmap.html)

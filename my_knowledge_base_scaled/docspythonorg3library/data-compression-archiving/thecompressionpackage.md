---
id: 0.0.5.2
title: "Thecompressionpackage¶"
nav_summary: "`compression` package: Standardized Python 3.14 compression modules."
ref: https://docs.python.org/3/library/compression.html
ref_type: url
---

# Thecompressionpackage¶

The `compression` package (introduced in **Python 3.14**) provides a standardized interface to multiple compression algorithms, consolidating historically separate modules (`bz2`, `gzip`, `lzma`, `zlib`) under a unified namespace for improved maintainability. It re-exports these modules while preserving backward compatibility with their original names. The package includes **low-level wrappers** for algorithms like **Zstandard (zstd)**, **bzip2**, **gzip**, **LZMA**, and **zlib**, enabling efficient compression/decompression via Python’s standard library. The design encourages migration to the `compression` namespace where feasible, ensuring a cleaner, future-proof architecture.

---

[Link to original](https://docs.python.org/3/library/compression.html)

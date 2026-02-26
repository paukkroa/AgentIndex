---
id: 0.0.5.4
title: "gzip— Support forgzipfiles¶"
nav_summary: "The **`gzip`** module in Python provides a high-level interface for compressing and decompressing files in the **gzip** format, mirroring functionalit"
ref: https://docs.python.org/3/library/gzip.html
ref_type: url
---

# gzip— Support forgzipfiles¶

The **`gzip`** module in Python provides a high-level interface for compressing and decompressing files in the **gzip** format, mirroring functionality akin to the GNU `gzip`/`gunzip` utilities. Built upon the **`zlib`** module for low-level compression/decompression, it offers two primary constructs: the **`GzipFile`** class and convenience functions (`open()`, `compress()`, `decompress()`). The **`GzipFile`** class abstracts file operations, automatically handling compression/decompression while presenting a standard **file object** interface. The **`open()`** function supports both binary (`'rb'`, `'wb'`, etc.) and text modes (`'rt'`, `'wt'`, etc.), with optional parameters like `compresslevel` (0–9), `encoding`, `errors`, and `newline` for text handling. It also accepts file objects or path-like objects (since Python 3.6). Errors like **`BadGzipFile`** (inheriting from **`OSError`**) are raised for corrupted files, alongside **`EOFError`** and **`zlib.error`**. This module is

[Link to original](https://docs.python.org/3/library/gzip.html)

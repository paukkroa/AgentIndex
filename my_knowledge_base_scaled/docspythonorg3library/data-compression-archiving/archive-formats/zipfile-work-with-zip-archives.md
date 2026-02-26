---
id: 0.0.5.1.0
title: "zipfile— Work with ZIP archives¶"
nav_summary: "Python’s ZIP archive handling module: read/write, ZIP64, decryption."
ref: https://docs.python.org/3/library/zipfile.html
ref_type: url
---

# zipfile— Work with ZIP archives¶

The `zipfile` module in Python’s standard library enables reading, writing, appending, and listing ZIP archives, adhering to the [PKZIP format specification](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT). It supports ZIP64 extensions for files exceeding 4 GiB but lacks multipart ZIP handling. The module provides **`ZipFile`** (core class for ZIP operations), **`ZipInfo`** (metadata for archive entries), and **`Path`** (pathlib-like traversal, added in Python 3.8). Decryption is supported for encrypted files but is slow due to Python-level implementation. Optional compression modules like `zlib`, `bz2`, or `lzma` are required for handling compressed archives. Key exceptions include `BadZipFile` (invalid archives), `LargeZipFile` (ZIP64 unsupported), and deprecated `BadZipfile`. The module also includes `PyZipFile` for creating Python-specific archives.

---

[Link to original](https://docs.python.org/3/library/zipfile.html)

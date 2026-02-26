---
id: 0.0.5.3
title: "Data Compression and Archiving¶"
nav_summary: "Python compression/archiving: zlib, gzip, bzip2, LZMA, zstd, ZIP, tar"
ref: https://docs.python.org/3/library/archiving.html
ref_type: url
---

# Data Compression and Archiving¶

This chapter of the Python Standard Library documentation covers **data compression and archiving** modules, including support for **zlib, gzip, bzip2, LZMA, and Zstandard (zstd)** compression algorithms, as well as **ZIP and tar archive formats**. The **`compression` package** provides high-performance Zstandard compression, while individual modules like `zlib`, `gzip`, `bzip2`, and `lzma` offer specialized compression/decompression capabilities for files and in-memory data. The **`zipfile`** module enables creation, reading, and extraction of ZIP archives, including support for path objects, command-line interfaces, and handling decompression pitfalls (e.g., filesystem limitations). The **`tarfile`** module supports reading/writing tar archives, with features like custom extraction filters, TarInfo objects, and compatibility with older Python versions. Additional details include incremental/decompression methods, command-line tools, and examples for practical implementation.

---

[Link to original](https://docs.python.org/3/library/archiving.html)

---
id: 0.0.5.1.1
title: "tarfile— Read and write tar archive files¶"
nav_summary: "The `tarfile` module in Python’s standard library enables reading and writing **tar archives** (including compressed formats like **gzip, bz2, lzma, a"
ref: https://docs.python.org/3/library/tarfile.html
ref_type: url
---

# tarfile— Read and write tar archive files¶

The `tarfile` module in Python’s standard library enables reading and writing **tar archives** (including compressed formats like **gzip, bz2, lzma, and Zstandard**) while supporting **POSIX.1-1988 (ustar), GNU tar (with longname/longlink/sparse extensions), and POSIX.1-2001 (pax) formats**. It handles diverse file types (directories, hardlinks, symlinks, FIFOs, devices) and preserves metadata like timestamps, permissions, and ownership. Key features include:
- **Compression support**: Optional modules (`gzip`, `bz2`, `lzma`, `zstd`) enable handling compressed archives.
- **Security enhancements**: Version 3.12+ introduces **extraction filters** (e.g., `data_filter` for safer defaults) to mitigate risks like path traversal.
- **API**: The `tarfile.open()` function returns a `TarFile` object for operations like extraction, creation, or listing archive contents.
- **Backward compatibility**: Defaults shifted in 3.14 to safer extraction policies (e.g., blocking absolute paths).

---
**NA

[Link to original](https://docs.python.org/3/library/tarfile.html)

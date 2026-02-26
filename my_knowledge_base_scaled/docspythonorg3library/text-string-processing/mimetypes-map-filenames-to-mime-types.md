---
id: 0.0.2.0
title: "mimetypes— Map filenames to MIME types¶"
nav_summary: "`mimetypes` module maps filenames/URLs to MIME types."
ref: https://docs.python.org/3/library/mimetypes.html
ref_type: url
---

# mimetypes— Map filenames to MIME types¶

The `mimetypes` module in Python’s standard library maps filenames or URLs to their corresponding MIME types (e.g., `text/plain`, `image/jpeg`) and vice versa, leveraging file extensions and OS/IANA-registered databases. It provides two primary functions: `guess_type(url, strict=True)` and `guess_file_type(path, strict=True)`, which infer MIME types from file paths or URLs (now supporting path-like objects). The `strict` parameter filters results to IANA-registered types (default: `True`) or includes non-standard types. For reverse lookups, `guess_all_extensions(type, strict=True)` returns possible file extensions for a given MIME type. The module relies on an internal database and OS-level file associations, with `init()` initializing it. Note: Passing raw file paths to `guess_type()` is deprecated in favor of `guess_file_type()` (introduced in Python 3.13).

---

[Link to original](https://docs.python.org/3/library/mimetypes.html)

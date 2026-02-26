---
id: 0.0.3.6
title: "linecache— Random access to text lines¶"
nav_summary: "Efficient random-access text line retrieval via caching."
ref: https://docs.python.org/3/library/linecache.html
ref_type: url
---

# linecache— Random access to text lines¶

The `linecache` module in Python provides efficient random access to text lines in source files, leveraging an internal cache to optimize repeated reads from the same file. It is primarily used by the `traceback` module to fetch source code lines for formatted tracebacks. The module relies on `tokenize.open()` for file handling, automatically detecting encoding (defaulting to UTF-8) via `tokenize.detect_encoding()`. Key functions include:
- **`getline(filename, lineno, module_globals=None)`**: Retrieves a specific line from a file, handling frozen modules, PEP 302 loaders, and relative paths via `sys.path`. Returns an empty string on errors.
- **`clearcache()`**: Clears the internal cache to free memory.
- **`checkcache(filename=None)`**: Validates cached file entries against disk changes.
- **`lazycache(filename, module_globals)`** (Python 3.5+): Defer I/O until a line is requested, storing minimal module details for later access.

[Link to original](https://docs.python.org/3/library/linecache.html)

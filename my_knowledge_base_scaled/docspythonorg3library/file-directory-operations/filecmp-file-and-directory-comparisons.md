---
id: 0.0.3.1
title: "filecmp— File and Directory Comparisons¶"
nav_summary: "`filecmp` module: compare files/dirs via metadata or content."
ref: https://docs.python.org/3/library/filecmp.html
ref_type: url
---

# filecmp— File and Directory Comparisons¶

The `filecmp` module in Python provides robust tools for comparing files and directories with configurable trade-offs between speed and accuracy. It offers core functions like `cmp()`, which compares two files either by shallow metadata checks (file type, size, and modification time) or by content comparison, leveraging an internal cache for efficiency. The `cmpfiles()` function extends this to compare multiple files across two directories based on a list of common filenames, returning categorized lists of matches, mismatches, and errors. The `clear_cache()` function allows manual cache invalidation, critical for scenarios where file modifications occur too rapidly for the filesystem’s timestamp resolution. The `dircmp` class enables hierarchical directory comparisons, supporting optional ignore/hide lists (e.g., `.git`, `node_modules`) and shallow comparisons by default. Introduced in Python 3.13, the `shallow` parameter in `dircmp` enhances flexibility. This module prioritizes portability and performance by avoiding external tools, making it ideal for automated scripts or system checks.

---

[Link to original](https://docs.python.org/3/library/filecmp.html)

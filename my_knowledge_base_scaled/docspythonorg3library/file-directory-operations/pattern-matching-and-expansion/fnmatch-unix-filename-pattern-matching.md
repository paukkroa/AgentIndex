---
id: 0.0.3.3.1
title: "fnmatch— Unix filename pattern matching¶"
nav_summary: "Unix shell-style filename pattern matching with `*`, `?`, `[seq]` wildcards."
ref: https://docs.python.org/3/library/fnmatch.html
ref_type: url
---

# fnmatch— Unix filename pattern matching¶

The `fnmatch` module in Python implements Unix shell-style filename pattern matching, distinct from regular expressions (handled by the `re` module). It supports wildcards like `*` (matches any sequence), `?` (matches a single character), and character sets (`[abc]`, `[!abc]` for negation). Special characters must be escaped with brackets for literal matches (e.g., `'[?]'` matches the literal `?`). The module does not treat `/` or leading `.` as special. Functions include:
- **`fnmatch(name, pat)`**: Case-insensitive pattern matching (normalized via `os.path.normcase`).
- **`fnmatchcase(name, pat)`**: Case-sensitive matching.
- **`filter(names, pat)`**: Efficiently filters iterables of filenames against a pattern.
- **`filterfalse(names, pat)`**: Returns non-matching filenames.
Internally, compiled patterns are cached using `functools.lru_cache` for performance. Patterns and filenames must be consistent in type (`str` or `bytes`).

---

[Link to original](https://docs.python.org/3/library/fnmatch.html)

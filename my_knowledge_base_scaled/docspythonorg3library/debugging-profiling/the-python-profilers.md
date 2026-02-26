---
id: 0.0.15.5
title: "The Python Profilers¶"
nav_summary: "Python Profilers: `cProfile`/`profile` for performance analysis"
ref: https://docs.python.org/3/library/profile.html
ref_type: url
---

# The Python Profilers¶

The **Python Profilers** (`cProfile` and `profile`) provide deterministic profiling to analyze Python program execution by measuring function call frequency, duration, and cumulative time. **`cProfile`**, a C-extension-based profiler, is optimized for low overhead and long-running programs, while **`profile`**, a pure Python module, offers flexibility for customization but introduces higher overhead. Both generate statistics via the `pstats` module, which formats reports for analysis. Key distinctions include `cProfile`'s efficiency for production use and `profile`'s suitability for development or extension. Profilers track call counts, execution time, and primitive operations (e.g., built-in methods) but are **not** designed for benchmarking (use `timeit` instead). Output includes hierarchical call statistics, enabling performance bottlenecks to be identified.

---

[Link to original](https://docs.python.org/3/library/profile.html)

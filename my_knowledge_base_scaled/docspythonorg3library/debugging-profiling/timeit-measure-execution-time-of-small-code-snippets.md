---
id: 0.0.15.6
title: "timeit— Measure execution time of small code snippets¶"
nav_summary: "The `timeit` module in Python provides a robust and optimized way to measure the execution time of small code snippets, mitigating common pitfalls in"
ref: https://docs.python.org/3/library/timeit.html
ref_type: url
---

# timeit— Measure execution time of small code snippets¶

The `timeit` module in Python provides a robust and optimized way to measure the execution time of small code snippets, mitigating common pitfalls in benchmarking (e.g., system noise, overhead, or warm-up effects). It offers both a **command-line interface** (`python -m timeit`) and a **programmatic interface** via `timeit.timeit()`, `timeit.repeat()`, and the `Timer` class. Key features include:
- **Automatic repetition tuning** (CLI) or configurable repetitions (`number`, `repeat` parameters) to ensure statistically meaningful results.
- **Setup code** to pre-execute dependencies (e.g., imports, variable declarations) before timing the target statement.
- **Customizable timers** (default: `time.perf_counter()` for high-resolution wall-clock time) or `time.perf_counter_ns()` for nanosecond precision.
- **Global namespace support** (since Python 3.5) to execute code in a predefined environment.
- **Advanced timing** via the `Timer` class, enabling repeated measurements and statistical analysis (e.g., `repeat()` for multiple runs).
- **Example-driven usage**: Demonstrates performance comparisons (e.g., list

[Link to original](https://docs.python.org/3/library/timeit.html)

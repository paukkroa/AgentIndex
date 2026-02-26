---
id: 0.0.0.3.1
title: "functools— Higher-order functions and operations on callable objects¶"
nav_summary: "`functools: memoization, caching, thread-safe decorators`"
ref: https://docs.python.org/3/library/functools.html
ref_type: url
---

# functools— Higher-order functions and operations on callable objects¶

The `functools` module provides higher-order functions and utilities for manipulating callable objects in Python. It includes **`@cache`**, a lightweight unbounded memoization decorator (since Python 3.9) that caches function results in a thread-safe dictionary, improving performance for recursive or repeated computations. It also offers **`@cached_property`**, which transforms instance methods into cached attributes, optimizing expensive computations (e.g., statistical calculations) while allowing subsequent writes to override cached values. Both decorators avoid redundant calculations but differ in scope: `@cache` applies to standalone functions, while `@cached_property` targets instance attributes. Thread safety is noted for `@cache`, though `@cached_property` lacks explicit thread-safety guarantees, potentially causing race conditions in concurrent environments.

---

[Link to original](https://docs.python.org/3/library/functools.html)

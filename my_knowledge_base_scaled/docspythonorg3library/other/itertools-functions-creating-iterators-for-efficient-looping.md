---
id: 0.0.24.4
title: "itertools— Functions creating iterators for efficient looping¶"
nav_summary: "`itertools`: Efficient iterator tools for looping & transformations."
ref: https://docs.python.org/3/library/itertools.html
ref_type: url
---

# itertools— Functions creating iterators for efficient looping¶

The `itertools` module provides a collection of **memory-efficient iterator-building functions** inspired by functional programming languages like APL, Haskell, and SML. It offers an **"iterator algebra"**—a set of tools for constructing specialized iterators in pure Python without sacrificing performance. Key features include **infinite iterators** like `count()`, `cycle()`, and `repeat()` for generating sequences indefinitely or until a limit, and **terminating iterators** such as `accumulate()`, `chain()`, and `groupby()` for processing sequences with transformations, filtering, or grouping. Functions like `islice()`, `dropwhile()`, and `takewhile()` enable slicing, conditional iteration, and lazy evaluation, while `starmap()` and `pairwise()` facilitate advanced operations like unpacked function calls and adjacent-element pairing. The module emphasizes **lazy evaluation**, **low memory usage**, and **composability**, making it ideal for large-scale data processing and functional-style programming.

---

[Link to original](https://docs.python.org/3/library/itertools.html)

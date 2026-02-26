---
id: 0.0.1.3.2
title: "bisect— Array bisection algorithm¶"
nav_summary: "The `bisect` module implements an efficient **array bisection algorithm** to maintain sorted order in lists without full re-sorting after insertions"
ref: https://docs.python.org/3/library/bisect.html
ref_type: url
---

# bisect— Array bisection algorithm¶

The `bisect` module implements an efficient **array bisection algorithm** to maintain sorted order in lists without full re-sorting after insertions. It leverages **binary search (bisection)** to locate insertion points for new elements, optimizing performance for large datasets with expensive comparisons. Key functions include:
- **`bisect_left(a, x)`**: Finds the leftmost insertion point to preserve sorted order, ensuring duplicates are inserted before existing entries.
- **`bisect_right(a, x)`**: Finds the rightmost insertion point, placing duplicates after existing entries.
- **`bisect(a, x)`**: Alias for `bisect_right`.
- **`insort_left(a, x)`**: Inserts `x` into `a` at the correct position to maintain sorted order (uses `bisect_left` internally).
All functions support optional `lo`, `hi` bounds and a **`key` parameter** (added in Python 3.10) for custom comparison logic. The module avoids calling `__eq__` and relies solely on `__lt__` for comparisons. **Thread-unsafe**: Concurrent access or mutations to the list during operations yield undefined behavior.

---
**NAVIGATION

[Link to original](https://docs.python.org/3/library/bisect.html)

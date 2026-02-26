---
id: 0.0.1.3.1
title: "heapq— Heap queue algorithm¶"
nav_summary: "`heapq"
ref: https://docs.python.org/3/library/heapq.html
ref_type: url
---

# heapq— Heap queue algorithm¶

The `heapq` module implements a **min-heap** priority queue algorithm using zero-based indexing, where each parent node’s value is ≤ its children’s values (`heap[k] ≤ heap[2*k+1]` and `heap[k] ≤ heap[2*k+2]`). The smallest element is always at `heap[0]`. Key functions include:
- **`heapify()`**: Converts a list into a min-heap in-place in **O(n)** time.
- **`heappush()`**: Inserts an item while maintaining heap order.
- **`heappop()`**: Removes and returns the smallest item (raises `IndexError` if empty).
- **`heappushpop()`**: Efficiently pushes an item and pops the smallest in one step.
- **`heapreplace()`**: Pops the smallest item and pushes a new one atomically.
Max-heaps (reverse invariant) are supported via `_max` suffixed functions (e.g., `heapify_max()`). The module leverages Python’s `<` operator for comparisons, enabling seamless integration with lists (e.g., `heap.sort()` maintains heap order).

---

[Link to original](https://docs.python.org/3/library/heapq.html)

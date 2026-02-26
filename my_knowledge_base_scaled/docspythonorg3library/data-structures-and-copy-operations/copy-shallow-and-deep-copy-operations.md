---
id: 0.0.18.0
title: "copy— Shallow and deep copy operations¶"
nav_summary: "`copy` module: Shallow/deep copy functions for mutable objects."
ref: https://docs.python.org/3/library/copy.html
ref_type: url
---

# copy— Shallow and deep copy operations¶

The **`copy`** module in Python provides mechanisms for creating **shallow and deep copies** of objects to avoid unintended side effects when modifying mutable structures (e.g., lists, dictionaries, or custom class instances). A **shallow copy** duplicates the top-level object but retains references to nested objects, while a **deep copy** recursively duplicates all nested objects, ensuring complete independence. Key functions include:
- `copy.copy(obj)`: Creates a **shallow copy** (fast but shares nested references).
- `copy.deepcopy(obj[, memo])`: Performs a **deep copy** using a `memo` dictionary to handle cycles and optimize performance. Custom classes can override copying via `__copy__()` (shallow) or `__deepcopy__()` (deep) methods. The module integrates with `pickle` and `copyreg` for advanced control. Note: Immutable types (e.g., integers, strings) and certain objects (e.g., modules, sockets) are not copied.

---

[Link to original](https://docs.python.org/3/library/copy.html)

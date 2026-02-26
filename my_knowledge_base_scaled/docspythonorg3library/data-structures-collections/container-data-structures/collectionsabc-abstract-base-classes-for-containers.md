---
id: 0.0.1.3.0
title: "collections.abc— Abstract Base Classes for Containers¶"
nav_summary: "The `collections"
ref: https://docs.python.org/3/library/collections.abc.html
ref_type: url
---

# collections.abc— Abstract Base Classes for Containers¶

The `collections.abc` module in Python (introduced in **3.3**, previously part of `collections`) provides **abstract base classes (ABCs)** for defining and verifying container interfaces. These ABCs enable runtime checks using `issubclass()` or `isinstance()` to test if a class adheres to specific protocols (e.g., hashable, iterable, or mapping). Three key approaches exist:
1. **Direct inheritance**: Classes explicitly inherit from ABCs (e.g., `Sequence`) and implement required abstract methods (e.g., `__getitem__`, `__len__`), while optionally overriding mixin methods.
2. **Virtual subclass registration**: Existing classes (without inheritance) can be registered as ABC subclasses if they fully implement the interface, including all abstract and mixin methods (e.g., `Sequence.register(D)`).
3. **Automatic recognition**: Simple interfaces (e.g., `Iterable`) are inferred from method presence (e.g., `__iter__`, `__next__`), though complex interfaces require explicit registration.

The module supports core container protocols like `Iterable`, `Iterator`, `Container`, `Mapping`, `MutableMapping`, `Set`, `MutableSet`, and `Sequence`, ensuring type safety

[Link to original](https://docs.python.org/3/library/collections.abc.html)

---
id: 0.0.1.2
title: "collections— Container datatypes¶"
nav_summary: "Optimized container datatypes: `deque`, `ChainMap`, `Counter`, `OrderedDict`, etc."
ref: https://docs.python.org/3/library/collections.html
ref_type: url
---

# collections— Container datatypes¶

The `collections` module in Python provides optimized container datatypes as alternatives to built-in types like `dict`, `list`, `set`, and `tuple`. It includes specialized classes such as **`namedtuple()`** (immutable tuple subclasses with named fields), **`deque`** (efficient double-ended queue for O(1) appends/pops at both ends), **`ChainMap`** (a dict-like class merging multiple mappings into a single view for fast lookups and updates on the first mapping), **`Counter`** (a dictionary subclass for counting hashable objects), **`OrderedDict`** (a dictionary preserving insertion order), **`defaultdict`** (auto-populates missing keys via a factory function), and wrapper classes (**`UserDict`**, **`UserList`**, **`UserString`**) for easier customization of built-in containers. These tools enhance performance, readability, and functionality for specific use cases like templating, nested scopes, or ordered data handling.

---

[Link to original](https://docs.python.org/3/library/collections.html)

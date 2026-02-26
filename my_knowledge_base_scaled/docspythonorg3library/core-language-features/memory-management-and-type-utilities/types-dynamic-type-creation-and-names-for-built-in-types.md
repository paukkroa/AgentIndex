---
id: 0.0.0.1.1
title: "types— Dynamic type creation and names for built-in types¶"
nav_summary: "The `types` module in Python provides utilities for **dynamic class creation** and access to **built-in type names** not exposed as builtins (e"
ref: https://docs.python.org/3/library/types.html
ref_type: url
---

# types— Dynamic type creation and names for built-in types¶

The `types` module in Python provides utilities for **dynamic class creation** and access to **built-in type names** not exposed as builtins (e.g., `int`, `str`). Key features include:

1. **Dynamic Type Creation**:
   - `types.new_class()` dynamically constructs a class using a provided metaclass, name, bases, and keyword arguments. The `exec_body` callback populates the class namespace.
   - `types.prepare_class()` precomputes the metaclass and class namespace, returning a tuple `(metaclass, namespace, kwds)` for further customization.
   - `types.resolve_bases()` resolves inheritance hierarchies dynamically via `PEP 560`, handling non-type base classes with `__mro_entries__()` methods.
   - `types.get_original_bases()` retrieves the original base classes of a class, bypassing inheritance resolution.

2. **Built-in Type Access**:
   Exposes names for interpreter-internal types (e.g., `types.FrameType`, `types.CodeType`) not directly available as builtins.

3. **Utility Functions**:
   - Supports advanced metaclass workflows (e.g., `__prepare__` via `PE

[Link to original](https://docs.python.org/3/library/types.html)

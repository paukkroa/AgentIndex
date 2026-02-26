---
id: 0.0.0.1.0
title: "weakref— Weak references¶"
nav_summary: "`weakref` module: manage weak references for memory-efficient object tracking."
ref: https://docs.python.org/3/library/weakref.html
ref_type: url
---

# weakref— Weak references¶

The `weakref` module enables Python developers to create **weak references** to objects, allowing garbage collection to reclaim memory when no strong references remain. A weak reference (*referent*) does not prevent an object’s destruction, enabling efficient memory management for large objects in caches or mappings (e.g., `WeakKeyDictionary`, `WeakValueDictionary`, or `WeakSet`). These containers use callbacks to clean up entries when objects are garbage-collected. The `finalize` function simplifies registering cleanup tasks for objects. While most use cases rely on built-in weak containers, the module also provides low-level tools for custom weak reference implementations. Not all objects support weak references (e.g., C-extension objects or file objects).

---

[Link to original](https://docs.python.org/3/library/weakref.html)

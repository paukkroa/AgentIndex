---
id: 0.0.4.3
title: "shelve— Python object persistence¶"
nav_summary: "Persistent dictionary for Python objects via `pickle`."
ref: https://docs.python.org/3/library/shelve.html
ref_type: url
---

# shelve— Python object persistence¶

The `shelve` module in Python provides a persistent, dictionary-like object for storing arbitrary Python objects (serialized via `pickle`) with string keys. Unlike traditional key-value databases like `dbm`, `shelve` supports complex objects (e.g., class instances, nested structures) while maintaining simplicity. The `shelve.open()` function initializes a database file, allowing read/write operations with optional parameters like `flag` (file mode), `protocol` (pickle serialization version), and `writeback` (caching mutable objects in memory for automatic updates). Key limitations include manual closure (via `close()` or context managers) and security risks due to `pickle`'s arbitrary code execution. Methods mirror dictionary operations, with added `sync()` for flushing cached changes and `close()` for finalizing writes.

---

[Link to original](https://docs.python.org/3/library/shelve.html)

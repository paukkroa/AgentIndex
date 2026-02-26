---
id: 0.0.4.5
title: "dbm— Interfaces to Unix “databases”¶"
nav_summary: "Python’s Unix-style key-value database interface (SQLite/GNU/NDBM/dumb)."
ref: https://docs.python.org/3/library/dbm.html
ref_type: url
---

# dbm— Interfaces to Unix “databases”¶

The `dbm` module in Python provides a generic interface to Unix-style "databases" (key-value stores) via multiple backends, including `dbm.sqlite3` (SQLite-based), `dbm.gnu` (GNU DBM), `dbm.ndbm` (New DBM), and a fallback `dbm.dumb` implementation for portability. It raises a unified `dbm.error` exception for all supported modules. Key functions include `dbm.whichdb()`, which auto-detects the database format from a filename (returning `None`, `''`, or the module name), and `dbm.open()`, which opens a database with configurable flags (`'r'`, `'w'`, `'c'`, or `'n'`) and Unix-style permissions (default: `0o666`). The returned database object mimics mutable mappings, enabling CRUD operations (create, read, update, delete) and iteration. Introduced in Python 3.11, it supports path-like objects for cross-platform compatibility.

---

[Link to original](https://docs.python.org/3/library/dbm.html)

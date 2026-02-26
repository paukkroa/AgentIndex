---
id: 0.0.4.0
title: "Data Persistence¶"
nav_summary: "Python disk storage modules: pickle, shelve, DBM, SQLite"
ref: https://docs.python.org/3/library/persistence.html
ref_type: url
---

# Data Persistence¶

The **Data Persistence** chapter of the Python Standard Library documents modules for storing Python objects and data structures in persistent formats on disk. It covers **`pickle`**, a general-purpose serialization module that converts Python objects into byte streams (and vice versa) while supporting custom serialization logic for complex objects via **dispatch tables** and **reduction protocols**. It also includes **`marshal`**, a faster but less flexible alternative for internal use. For structured key-value storage, the **DBM-related modules** (`dbm`, `dbm.ndbm`, `dbm.gnu`, `dbm.dumb`, and `dbm.sqlite3`) provide hash-based file formats, while **`shelve`** offers a dictionary-like interface for persistent object storage. Additionally, **`sqlite3`** provides a full DB-API 2.0 interface for SQLite databases, enabling relational data persistence with SQL queries, transactions, and type conversions. Key considerations include security (e.g., unpickling arbitrary code), performance trade-offs, and platform-specific restrictions.

---

[Link to original](https://docs.python.org/3/library/persistence.html)

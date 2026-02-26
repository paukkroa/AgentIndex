---
id: 0.0.6.2
title: "configparser— Configuration file parser¶"
nav_summary: "The `configparser` module in Python provides the `ConfigParser` class, enabling parsing and writing of **INI-style configuration files** with a hierar"
ref: https://docs.python.org/3/library/configparser.html
ref_type: url
---

# configparser— Configuration file parser¶

The `configparser` module in Python provides the `ConfigParser` class, enabling parsing and writing of **INI-style configuration files** with a hierarchical structure of **sections** (key-value pairs grouped under named headers, e.g., `[DEFAULT]`, `[forge.example]`). It mimics dictionary-like behavior for accessing and modifying configurations, though with additional features like **section inheritance** (where missing keys fall back to `DEFAULT` or parent sections) and **file I/O support** (reading/writing `.ini` files). Key features include:
- **Section-based organization**: Sections act as nested dictionaries, allowing modular configuration.
- **Default section**: The `DEFAULT` section serves as a fallback for unspecified keys.
- **File operations**: Methods like `read()`, `write()`, and `read_file()` handle file I/O seamlessly.
- **Mapping protocol**: Supports dictionary-like access (e.g., `config['section']['key']`) with optional overrides via `add_section()`, `set()`, and `get()`.
- **No advanced INI features**: Unlike Windows Registry INI files, it does not support value-type prefixes (e.g., `int`, `bool`).
- **Compatibility**: Works with Python’s standard

[Link to original](https://docs.python.org/3/library/configparser.html)

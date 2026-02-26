---
id: 0.0.6.3
title: "tomllib— Parse TOML files¶"
nav_summary: "Parse TOML 1.0.0 files into Python dicts."
ref: https://docs.python.org/3/library/tomllib.html
ref_type: url
---

# tomllib— Parse TOML files¶

The `tomllib` module (introduced in Python 3.11) provides a secure, standard library interface for parsing TOML 1.0.0 files into Python dictionaries, converting TOML types (e.g., booleans, integers, floats, dates) via a predefined schema. It supports two primary functions: `tomllib.load()` for parsing file objects and `tomllib.loads()` for parsing string content. Both functions accept an optional `parse_float` callback to customize float parsing (e.g., using `decimal.Decimal`). Errors are raised as `TOMLDecodeError`, a subclass of `ValueError`, with detailed positional and contextual metadata (e.g., line/column numbers, raw document snippet). The module lacks write support but integrates with third-party libraries like `tomli-w` or `tomlkit` for editing TOML files. Security note: `tomllib` is designed to be safe against arbitrary TOML injection attacks.

---

[Link to original](https://docs.python.org/3/library/tomllib.html)

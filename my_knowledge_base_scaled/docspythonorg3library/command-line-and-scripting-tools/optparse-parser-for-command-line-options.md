---
id: 0.0.20.3
title: "optparse— Parser for command line options¶"
nav_summary: "The `optparse` module is a **declarative command-line argument parser** in Python’s standard library (since Python 2"
ref: https://docs.python.org/3/library/optparse.html
ref_type: url
---

# optparse— Parser for command line options¶

The `optparse` module is a **declarative command-line argument parser** in Python’s standard library (since Python 2.3), designed as a **modern alternative to the procedural `getopt` module**. It provides **flexible, object-oriented syntax** for defining and parsing command-line options, including **short (`-x`) and long (`--option`) flags**, **optional/required arguments**, **type conversion**, and **help generation**. Key features include:
- **Declarative API**: Uses classes (`OptionParser`, `OptionGroup`) to define options declaratively rather than procedural logic.
- **Interleaved Option Handling**: Supports **mixed positional/optional arguments** (e.g., `cmd -v file.txt --mode=2`).
- **Incremental Parsing**: Allows **partial parsing** of arguments (useful for interactive or multi-stage CLI tools).
- **Custom Value Handling**: Supports **complex argument parsing** (e.g., options with values starting with `-`, delegated subprocess args).
- **Backward Compatibility**: Retains `getopt`-like functionality while offering **higher-level abstractions** (e.g., automatic help messages, type validation).
- **

[Link to original](https://docs.python.org/3/library/optparse.html)

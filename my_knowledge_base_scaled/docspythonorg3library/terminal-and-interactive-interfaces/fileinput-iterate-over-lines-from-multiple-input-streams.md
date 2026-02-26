---
id: 0.0.21.0
title: "fileinput— Iterate over lines from multiple input streams¶"
nav_summary: "The `fileinput` module in Python provides a streamlined way to iterate over lines from multiple input sources (files or `sys"
ref: https://docs.python.org/3/library/fileinput.html
ref_type: url
---

# fileinput— Iterate over lines from multiple input streams¶

The `fileinput` module in Python provides a streamlined way to iterate over lines from multiple input sources (files or `sys.stdin`) using a unified interface. It simplifies handling multiple files by abstracting file operations into a single iterable object, leveraging `sys.argv[1:]` for default file selection or falling back to `sys.stdin` if no arguments are provided. Key features include:
- **Flexible Input Handling**: Supports explicit file lists, `sys.argv`, or `sys.stdin` (including via `-` placeholder), with automatic fallback to text mode.
- **Error Handling**: Raises `OSError` (or `IOError` in Python < 3.3) for I/O failures during file operations.
- **Customizable File Opening**: Allows overriding default behavior via `openhook` (e.g., for compressed files) or specifying `mode`, `encoding`, or `errors` parameters.
- **In-Place Editing**: Supports in-place file modifications with `inplace=True` and configurable backup handling.
- **Context Manager Support**: Works seamlessly with `with` statements for resource cleanup.
- **Edge-Case Handling**: Empty files are skipped, and newlines are

[Link to original](https://docs.python.org/3/library/fileinput.html)

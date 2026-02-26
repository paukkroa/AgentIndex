---
id: 0.0.6.4
title: "netrc— netrc file processing¶"
nav_summary: "Parse/"
ref: https://docs.python.org/3/library/netrc.html
ref_type: url
---

# netrc— netrc file processing¶

The `netrc` module in Python’s standard library parses and processes `.netrc` files, a Unix-standard format used by FTP clients to store authentication credentials (login, account, password) for remote hosts. The core `netrc.netrc` class reads and validates `.netrc` files, defaulting to `~/.netrc` if none is specified. Key features include:
- **Security checks** (POSIX systems only): Rejects insecure files (non-owner access or permissions) and raises `NetrcParseError` for syntax issues, with detailed diagnostics (filename, line number, error message).
- **Flexible parsing**: Supports UTF-8 encoding by default, allowing arbitrary characters (whitespace, non-ASCII) in tokens/values. Missing tokens default to empty strings, and anonymous logins bypass security checks.
- **Host-based lookup**: The `authenticators(host)` method returns a 3-tuple `(login, account, password)` for a given host, falling back to the ‘default’ entry if no match exists. Errors (e.g., missing files) raise `FileNotFoundError` or `NetrcParseError`.

[Link to original](https://docs.python.org/3/library/netrc.html)

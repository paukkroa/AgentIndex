---
id: 0.0.8.0.1
title: "platform—  Access to underlying platform’s identifying data¶"
nav_summary: "The `platform` module in Python provides cross-platform access to system-specific identifying data, enabling applications to dynamically adapt to unde"
ref: https://docs.python.org/3/library/platform.html
ref_type: url
---

# platform—  Access to underlying platform’s identifying data¶

The `platform` module in Python provides cross-platform access to system-specific identifying data, enabling applications to dynamically adapt to underlying hardware and OS configurations. Key features include:
- **`architecture()`**: Queries executable bitness (e.g., 32/64-bit) and linkage format via the system’s `file` command, defaulting to `sys.maxsize` for reliable 64-bit detection on macOS.
- **`machine()`**: Returns the CPU architecture (e.g., `'AMD64'`), with platform-specific naming conventions.
- **`node()`**: Retrieves the host’s network name (unqualified), falling back to an empty string if unavailable.
- **`platform()`**: Generates a human-readable string identifying the OS, with optional aliases (e.g., SunOS → Solaris) and terse mode for minimal info. macOS versions now integrate `mac_ver()` for accuracy.
- **`processor()`**: Displays the CPU model (e.g., `'amdk6'`), though many systems omit this data.
- **`system_alias()`**: Used internally to standardize platform names (e.g., SunOS → Solaris).

The module leverages system commands and OS-specific

[Link to original](https://docs.python.org/3/library/platform.html)

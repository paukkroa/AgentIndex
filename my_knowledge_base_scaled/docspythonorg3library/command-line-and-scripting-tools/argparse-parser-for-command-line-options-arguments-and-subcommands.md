---
id: 0.0.20.2
title: "argparse— Parser for command-line options, arguments and subcommands¶"
nav_summary: "`argparse`: Python’s CLI parser for options, arguments, and subcommands."
ref: https://docs.python.org/3/library/argparse.html
ref_type: url
---

# argparse— Parser for command-line options, arguments and subcommands¶

The `argparse` module, introduced in Python 3.2, is a robust standard library tool for constructing user-friendly command-line interfaces by parsing options, arguments, and subcommands from `sys.argv`. It automates help/usage message generation and error handling for invalid inputs. Core functionality revolves around the `ArgumentParser` class, which configures global settings (e.g., `prog`, `description`) and defines argument specifications via `add_argument()`, supporting positional arguments, value-accepting options (`-c --count`), and boolean flags (`-v --verbose`). Parsing results are stored in an `argparse.Namespace` object, enabling structured access to user-provided inputs. Advanced features include customizable help formatting, conflict resolution, and support for subcommands, though it lacks fine-grained control for niche use cases (e.g., disabling interspersed options). For migration from `optparse`, dedicated documentation is available.

---

[Link to original](https://docs.python.org/3/library/argparse.html)

---
id: 0.0.1.1.0
title: "readline— GNU readline interface¶"
nav_summary: "GNU Readline: History, Completion, Keybindings (Unix)"
ref: https://docs.python.org/3/library/readline.html
ref_type: url
---

# readline— GNU readline interface¶

The `readline` module provides Python integration with the **GNU Readline** library, enabling advanced command-line editing features like **history navigation, tab completion, and customizable keybindings** for both the Python interpreter and `input()` function. It supports **identifier completion** via the `rlcompleter` module and allows configuration through a `.inputrc` (or `.editrc` for macOS) file, where users define keybindings (e.g., Emacs/Vi modes) and completion triggers. The module detects the underlying library (GNU `readline` or `editline`/`libedit`) at runtime via `readline.backend` and handles history file storage, though format compatibility may vary across libraries. Optional on Unix systems, it lacks support on mobile platforms (Android/iOS) or WebAssembly. Functions like `readline.parse_and_bind()` and `readline.read_init_file()` enable dynamic configuration, while auditing events track file operations.

---

[Link to original](https://docs.python.org/3/library/readline.html)

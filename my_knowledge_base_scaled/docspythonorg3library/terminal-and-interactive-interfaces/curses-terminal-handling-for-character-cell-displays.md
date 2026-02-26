---
id: 0.0.21.1
title: "curses— Terminal handling for character-cell displays¶"
nav_summary: "The `curses` module provides a Python interface to the **ncurses** library, enabling portable terminal handling for character-cell displays across Uni"
ref: https://docs.python.org/3/library/curses.html
ref_type: url
---

# curses— Terminal handling for character-cell displays¶

The `curses` module provides a Python interface to the **ncurses** library, enabling portable terminal handling for character-cell displays across Unix, Windows, and DOS systems. It abstracts low-level terminal control, offering functions for cursor manipulation, window management, color support, and input/output handling. Key features include:
- **Cross-platform compatibility** with Unix, Windows, and DOS (not supported on Android, iOS, or WASI).
- **Terminal abstraction** for advanced features like color pairs (`init_pair`), cursor positioning (`move`), and attribute manipulation (e.g., bold, underline).
- **Window management** with nested windows, scrolling, and input/output redirection.
- **Color support** via `assume_default_colors()` (introduced in Python 3.14) for dynamic foreground/background transparency and default color assignments.
- **Input handling** with Emacs-like editing via `curses.textpad` and panel stacking for layered UI elements.
- **Error handling** via `curses.error` exceptions for library failures.
- **Unicode/byte string flexibility**: Characters can be integers, Unicode strings, or byte strings, while strings support Unicode or byte formats.

The module is optional and may

[Link to original](https://docs.python.org/3/library/curses.html)

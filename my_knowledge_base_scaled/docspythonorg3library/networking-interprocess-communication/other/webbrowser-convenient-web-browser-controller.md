---
id: 0.0.10.5.3
title: "webbrowser— Convenient web-browser controller¶"
nav_summary: "The `webbrowser` module in Python provides a high-level interface for launching web browsers to display documents"
ref: https://docs.python.org/3/library/webbrowser.html
ref_type: url
---

# webbrowser— Convenient web-browser controller¶

The `webbrowser` module in Python provides a high-level interface for launching web browsers to display documents. It automatically selects the most appropriate browser based on the platform and environment, prioritizing graphical browsers under X11 on Unix systems. If no graphical browser is available, it falls back to text-mode browsers, blocking the calling process until the user exits. On non-Unix platforms or when remote browsers are accessible on Unix, the process does not block, allowing the browser to run independently.

Key features include:
- **Browser Selection:** Uses the `BROWSER` environment variable to override default browser preferences, enabling custom browser lists or command-line arguments (e.g., `%s` for URL substitution). On macOS, this variable can reorder platform defaults.
- **Platform-Specific Behavior:** On iOS, the module ignores custom settings and always opens URLs in the user’s default browser in a new tab, requiring the `ctypes` module for functionality.
- **Command-Line Interface:** The `webbrowser` script supports optional flags like `-n` (new window) or `-t` (new tab) for programmatic URL opening.
- **Error Handling:** Raises `webbrowser.Error` exceptions for browser

[Link to original](https://docs.python.org/3/library/webbrowser.html)

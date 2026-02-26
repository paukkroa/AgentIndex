---
id: 0.0.13.0.1.0
title: "Tkinter Dialogs¶"
nav_summary: "Tkinter Dialogs: Input & File Selection Dialogs"
ref: https://docs.python.org/3/library/dialog.html
ref_type: url
---

# Tkinter Dialogs¶

The **Tkinter Dialogs** documentation outlines two primary modules for creating interactive user dialogs in Python’s Tkinter GUI framework: `tkinter.simpledialog` and `tkinter.filedialog`. The `tkinter.simpledialog` module provides **modal input dialogs** (`askfloat`, `askinteger`, `askstring`) for retrieving numeric or string values from users, along with a base `Dialog` class for custom dialog development. Key methods include `body()` (for UI construction) and `buttonbox()` (for button layouts). Meanwhile, `tkinter.filedialog` offers **native file selection dialogs** (Open/Save) with customizable options like `filetypes`, `initialdir`, and `multiple` selections. Factory functions (`askopenfile`, `askopenfilename`, `asksaveasfile`) generate modal dialogs, returning file objects or paths. Both modules leverage Tkinter’s widget hierarchy to ensure cross-platform compatibility and intuitive user interactions.

---

[Link to original](https://docs.python.org/3/library/dialog.html)

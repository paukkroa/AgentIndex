---
id: 0.0.13.0.0
title: "tkinter.ttk— Tk themed widgets¶"
nav_summary: "`tkinter.ttk: Themed Tk widgets (18 types, `Style` class for styling)`"
ref: https://docs.python.org/3/library/tkinter.ttk.html
ref_type: url
---

# tkinter.ttk— Tk themed widgets¶

The `tkinter.ttk` module introduces **Tk themed widgets**, an enhanced widget set from Tk 8.5 that improves cross-platform UI consistency with features like **anti-aliased fonts (X11)** and **window transparency** (requires a compositing WM). It separates widget **behavior** from **appearance** for modular styling. Key widgets include **18 total** (12 legacy replacements like `Button`, `Label`, `Entry` and 6 new ones like `Combobox`, `Notebook`, `Progressbar`, `Treeview`). Styling is managed via the `ttk.Style` class, replacing traditional options like `fg`/`bg` with themed styles (e.g., `style.configure("TLabel", foreground="black")`). Inherits from `ttk.Widget`, which defines standard options like `class`, `takefocus`, and `cursor`.

---

[Link to original](https://docs.python.org/3/library/tkinter.ttk.html)

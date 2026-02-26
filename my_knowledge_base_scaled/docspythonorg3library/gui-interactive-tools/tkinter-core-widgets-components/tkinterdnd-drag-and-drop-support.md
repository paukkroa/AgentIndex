---
id: 0.0.13.0.4
title: "tkinter.dnd— Drag and drop support¶"
nav_summary: "`tkinter.dnd` – Experimental drag-and-drop for Tkinter widgets."
ref: https://docs.python.org/3/library/tkinter.dnd.html
ref_type: url
---

# tkinter.dnd— Drag and drop support¶

The `tkinter.dnd` module provides **experimental drag-and-drop functionality** for Tkinter applications, enabling intra-application transfers between widgets or windows. It relies on event bindings (e.g., `ButtonPress`) to initiate drags via `dnd_start(source, event)`, triggering a sequence of callbacks: `dnd_enter`, `dnd_leave`, `dnd_commit` (for target validation), and `dnd_end`. The `DndHandler` class manages motion/release events, allowing dynamic target detection via a top-down widget hierarchy check for `dnd_accept` callables. Note: This module is deprecated in favor of native Tk DND support.

---

[Link to original](https://docs.python.org/3/library/tkinter.dnd.html)

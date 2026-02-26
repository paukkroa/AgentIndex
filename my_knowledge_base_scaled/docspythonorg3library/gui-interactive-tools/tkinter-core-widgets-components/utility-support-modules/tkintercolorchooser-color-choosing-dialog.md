---
id: 0.0.13.0.3.0
title: "tkinter.colorchooser— Color choosing dialog¶"
nav_summary: "`tkinter.colorchooser`: Native color picker dialog for Tkinter."
ref: https://docs.python.org/3/library/tkinter.colorchooser.html
ref_type: url
---

# tkinter.colorchooser— Color choosing dialog¶

The `tkinter.colorchooser` module provides a native color picker dialog via the `Chooser` class (inheriting from `tkinter.commondialog.Dialog`), enabling modal color selection in Tkinter applications. The primary function, `askcolor(color=None, **options)`, launches a cross-platform color dialog, returning the selected RGB tuple (e.g., `(R, G, B)`) or `None` if canceled. The dialog supports pre-selection via the `initialcolor` parameter (e.g., `#RRGGBB` or `(R, G, B)`) and customization through optional keyword arguments like `title` or `parent`. It integrates seamlessly with Tkinter’s GUI framework, leveraging native OS color picker dialogs for consistency and user familiarity.

---

[Link to original](https://docs.python.org/3/library/tkinter.colorchooser.html)

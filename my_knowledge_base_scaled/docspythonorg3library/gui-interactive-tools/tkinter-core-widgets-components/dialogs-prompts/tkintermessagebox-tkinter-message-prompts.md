---
id: 0.0.13.0.1.1
title: "tkinter.messagebox— Tkinter message prompts¶"
nav_summary: "`tkinter.messagebox: Modal dialogs with icons/buttons for user prompts`"
ref: https://docs.python.org/3/library/tkinter.messagebox.html
ref_type: url
---

# tkinter.messagebox— Tkinter message prompts¶

The `tkinter.messagebox` module in Python’s Tkinter library provides a standardized way to display modal dialogs (message boxes) for user notifications, confirmations, or alerts. It offers a base `Message` class for customizable message windows with configurable options like **icon styles** (`INFO`, `ERROR`, `WARNING`, `QUESTION`), **button types** (`OK`, `YES/NO`, `RETRY/CANCEL`), and **layout elements** (e.g., `message`, `detail`, `title`). The module also includes convenience functions like `showinfo()`, `showwarning()`, `showerror()`, `askquestion()`, `askokcancel()`, `askyesno()`, and `askretrycancel()` for predefined use cases. These functions return user selections as symbolic values (`True`, `False`, `None`, or button constants) and support platform-specific behaviors (e.g., macOS title restrictions). The dialogs are modal, blocking further interaction until dismissed, and can be parented to specific windows for context-aware placement.

---

[Link to original](https://docs.python.org/3/library/tkinter.messagebox.html)

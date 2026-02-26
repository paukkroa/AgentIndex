---
id: 0.0.13.0.3.1
title: "tkinter.font— Tkinter font wrapper¶"
nav_summary: "`tkinter.font` – Font management for Tkinter"
ref: https://docs.python.org/3/library/tkinter.font.html
ref_type: url
---

# tkinter.font— Tkinter font wrapper¶

The `tkinter.font` module provides a **`Font` class** for managing and manipulating fonts in Tkinter applications. It enables the creation of named font objects with configurable attributes such as **family (e.g., "Arial"), size (points/pixels), weight (NORMAL/BOLD), slant (ROMAN/ITALIC), underlining, and strikeout**. Fonts can be defined via a tuple (family, size, options) or keyword arguments (e.g., `family="Courier", size=12, weight="bold"`). Key methods include:
- **`actual()`** – Retrieves the final rendered font attributes.
- **`cget()`** – Fetches specific font properties.
- **`config()`** – Modifies font attributes dynamically.
- **`measure()`** – Calculates text width/height in pixels.
- **`metrics()`** – Returns font metrics like ascent, descent, and line spacing.
Additionally, `families()` lists available font families on the system. This module bridges Tk’s native font system with Python, allowing precise control over typography in GUI applications.

---

[Link to original](https://docs.python.org/3/library/tkinter.font.html)

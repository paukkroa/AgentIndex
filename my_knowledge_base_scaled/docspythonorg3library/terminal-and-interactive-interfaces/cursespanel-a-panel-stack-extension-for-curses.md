---
id: 0.0.21.3
title: "curses.panel— A panel stack extension for curses¶"
nav_summary: "`curses.panel: Stackable windows with depth management for layered curses displays.`"
ref: https://docs.python.org/3/library/curses.panel.html
ref_type: url
---

# curses.panel— A panel stack extension for curses¶

The `curses.panel` module extends the core `curses` library by introducing **panel objects**, which are windows with **stacking depth** for layered display management. Panels enable dynamic control over visibility, positioning, and hierarchy (e.g., bringing a panel to the top/bottom of the stack). Key functions include `new_panel()` (creates a panel tied to a window), `top_panel()`/`bottom_panel()` (retrieve top/bottom panels), and `update_panels()` (refreshes the virtual screen after stack changes). Panel methods like `hide()`/`show()`, `move()`, and `replace()` allow runtime manipulation of visibility, position, and associated windows. The `userptr()` mechanism enables attaching arbitrary Python objects to panels for custom data storage. Unlike raw `curses` windows, panels automatically handle depth-based rendering, ensuring only visible portions of overlapping windows are displayed.

---

[Link to original](https://docs.python.org/3/library/curses.panel.html)

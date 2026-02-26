### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](cmd.html "cmd — Support for line-oriented command interpreters") |
* [previous](curses.ascii.html "curses.ascii — Utilities for ASCII characters") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Command-line interface libraries](cmdlinelibs.html) »
* `curses.panel` — A panel stack extension for curses
* |
* Theme
  Auto
  Light
  Dark
   |

# `curses.panel` — A panel stack extension for curses[¶](#module-curses.panel "Link to this heading")

---

Panels are windows with the added feature of depth, so they can be stacked on
top of each other, and only the visible portions of each window will be
displayed. Panels can be added, moved up or down in the stack, and removed.

## Functions[¶](#functions "Link to this heading")

The module `curses.panel` defines the following functions:

curses.panel.bottom\_panel()[¶](#curses.panel.bottom_panel "Link to this definition")
:   Returns the bottom panel in the panel stack.

curses.panel.new\_panel(*win*)[¶](#curses.panel.new_panel "Link to this definition")
:   Returns a panel object, associating it with the given window *win*. Be aware
    that you need to keep the returned panel object referenced explicitly. If you
    don’t, the panel object is garbage collected and removed from the panel stack.

curses.panel.top\_panel()[¶](#curses.panel.top_panel "Link to this definition")
:   Returns the top panel in the panel stack.

curses.panel.update\_panels()[¶](#curses.panel.update_panels "Link to this definition")
:   Updates the virtual screen after changes in the panel stack. This does not call
    [`curses.doupdate()`](curses.html#curses.doupdate "curses.doupdate"), so you’ll have to do this yourself.

## Panel Objects[¶](#panel-objects "Link to this heading")

Panel objects, as returned by [`new_panel()`](#curses.panel.new_panel "curses.panel.new_panel") above, are windows with a
stacking order. There’s always a window associated with a panel which determines
the content, while the panel methods are responsible for the window’s depth in
the panel stack.

Panel objects have the following methods:

Panel.above()[¶](#curses.panel.Panel.above "Link to this definition")
:   Returns the panel above the current panel.

Panel.below()[¶](#curses.panel.Panel.below "Link to this definition")
:   Returns the panel below the current panel.

Panel.bottom()[¶](#curses.panel.Panel.bottom "Link to this definition")
:   Push the panel to the bottom of the stack.

Panel.hidden()[¶](#curses.panel.Panel.hidden "Link to this definition")
:   Returns `True` if the panel is hidden (not visible), `False` otherwise.

Panel.hide()[¶](#curses.panel.Panel.hide "Link to this definition")
:   Hide the panel. This does not delete the object, it just makes the window on
    screen invisible.

Panel.move(*y*, *x*)[¶](#curses.panel.Panel.move "Link to this definition")
:   Move the panel to the screen coordinates `(y, x)`.

Panel.replace(*win*)[¶](#curses.panel.Panel.replace "Link to this definition")
:   Change the window associated with the panel to the window *win*.

Panel.set\_userptr(*obj*)[¶](#curses.panel.Panel.set_userptr "Link to this definition")
:   Set the panel’s user pointer to *obj*. This is used to associate an arbitrary
    piece of data with the panel, and can be any Python object.

Panel.show()[¶](#curses.panel.Panel.show "Link to this definition")
:   Display the panel (which might have been hidden).

Panel.top()[¶](#curses.panel.Panel.top "Link to this definition")
:   Push panel to the top of the stack.

Panel.userptr()[¶](#curses.panel.Panel.userptr "Link to this definition")
:   Returns the user pointer for the panel. This might be any Python object.

Panel.window()[¶](#curses.panel.Panel.window "Link to this definition")
:   Returns the window object associated with the panel.

### [Table of Contents](../contents.html)

* [`curses.panel` — A panel stack extension for curses](#)
  + [Functions](#functions)
  + [Panel Objects](#panel-objects)

#### Previous topic

[`curses.ascii` — Utilities for ASCII characters](curses.ascii.html "previous chapter")

#### Next topic

[`cmd` — Support for line-oriented command interpreters](cmd.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/curses.panel.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](cmd.html "cmd — Support for line-oriented command interpreters") |
* [previous](curses.ascii.html "curses.ascii — Utilities for ASCII characters") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Command-line interface libraries](cmdlinelibs.html) »
* `curses.panel` — A panel stack extension for curses
* |
* Theme
  Auto
  Light
  Dark
   |

© [Copyright](../copyright.html) 2001 Python Software Foundation.
  
This page is licensed under the Python Software Foundation License Version 2.
  
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
  
See [History and License](/license.html) for more information.  
  
The Python Software Foundation is a non-profit corporation.
[Please donate.](https://www.python.org/psf/donations/)
  
  
Last updated on Feb 22, 2026 (06:32 UTC).
[Found a bug](/bugs.html)?
  
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.
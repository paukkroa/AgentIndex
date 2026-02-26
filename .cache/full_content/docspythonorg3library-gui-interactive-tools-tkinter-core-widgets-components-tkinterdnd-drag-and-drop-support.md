### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tkinter.ttk.html "tkinter.ttk — Tk themed widgets") |
* [previous](tkinter.scrolledtext.html "tkinter.scrolledtext — Scrolled Text Widget") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Graphical user interfaces with Tk](tk.html) »
* `tkinter.dnd` — Drag and drop support
* |
* Theme
  Auto
  Light
  Dark
   |

# `tkinter.dnd` — Drag and drop support[¶](#module-tkinter.dnd "Link to this heading")

**Source code:** [Lib/tkinter/dnd.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/dnd.py)

---

Note

This is experimental and due to be deprecated when it is replaced
with the Tk DND.

The `tkinter.dnd` module provides drag-and-drop support for objects within
a single application, within the same window or between windows. To enable an
object to be dragged, you must create an event binding for it that starts the
drag-and-drop process. Typically, you bind a ButtonPress event to a callback
function that you write (see [Bindings and Events](tkinter.html#bindings-and-events)). The function should
call [`dnd_start()`](#tkinter.dnd.dnd_start "tkinter.dnd.dnd_start"), where ‘source’ is the object to be dragged, and ‘event’
is the event that invoked the call (the argument to your callback function).

Selection of a target object occurs as follows:

1. Top-down search of area under mouse for target widget

> * Target widget should have a callable *dnd\_accept* attribute
> * If *dnd\_accept* is not present or returns `None`, search moves to parent widget
> * If no target widget is found, then the target object is `None`

2. Call to *<old\_target>.dnd\_leave(source, event)*
3. Call to *<new\_target>.dnd\_enter(source, event)*
4. Call to *<target>.dnd\_commit(source, event)* to notify of drop
5. Call to *<source>.dnd\_end(target, event)* to signal end of drag-and-drop

*class* tkinter.dnd.DndHandler(*source*, *event*)[¶](#tkinter.dnd.DndHandler "Link to this definition")
:   The *DndHandler* class handles drag-and-drop events tracking Motion and
    ButtonRelease events on the root of the event widget.

    cancel(*event=None*)[¶](#tkinter.dnd.DndHandler.cancel "Link to this definition")
    :   Cancel the drag-and-drop process.

    finish(*event*, *commit=0*)[¶](#tkinter.dnd.DndHandler.finish "Link to this definition")
    :   Execute end of drag-and-drop functions.

    on\_motion(*event*)[¶](#tkinter.dnd.DndHandler.on_motion "Link to this definition")
    :   Inspect area below mouse for target objects while drag is performed.

    on\_release(*event*)[¶](#tkinter.dnd.DndHandler.on_release "Link to this definition")
    :   Signal end of drag when the release pattern is triggered.

tkinter.dnd.dnd\_start(*source*, *event*)[¶](#tkinter.dnd.dnd_start "Link to this definition")
:   Factory function for drag-and-drop process.

See also

[Bindings and Events](tkinter.html#bindings-and-events)

#### Previous topic

[`tkinter.scrolledtext` — Scrolled Text Widget](tkinter.scrolledtext.html "previous chapter")

#### Next topic

[`tkinter.ttk` — Tk themed widgets](tkinter.ttk.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/tkinter.dnd.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tkinter.ttk.html "tkinter.ttk — Tk themed widgets") |
* [previous](tkinter.scrolledtext.html "tkinter.scrolledtext — Scrolled Text Widget") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Graphical user interfaces with Tk](tk.html) »
* `tkinter.dnd` — Drag and drop support
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
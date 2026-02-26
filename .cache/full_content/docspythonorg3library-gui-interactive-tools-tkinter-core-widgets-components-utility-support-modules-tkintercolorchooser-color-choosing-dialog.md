### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tkinter.font.html "tkinter.font — Tkinter font wrapper") |
* [previous](tkinter.html "tkinter — Python interface to Tcl/Tk") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Graphical user interfaces with Tk](tk.html) »
* `tkinter.colorchooser` — Color choosing dialog
* |
* Theme
  Auto
  Light
  Dark
   |

# `tkinter.colorchooser` — Color choosing dialog[¶](#module-tkinter.colorchooser "Link to this heading")

**Source code:** [Lib/tkinter/colorchooser.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/colorchooser.py)

---

The `tkinter.colorchooser` module provides the [`Chooser`](#tkinter.colorchooser.Chooser "tkinter.colorchooser.Chooser") class
as an interface to the native color picker dialog. `Chooser` implements
a modal color choosing dialog window. The `Chooser` class inherits from
the [`Dialog`](dialog.html#tkinter.commondialog.Dialog "tkinter.commondialog.Dialog") class.

*class* tkinter.colorchooser.Chooser(*master=None*, *\*\*options*)[¶](#tkinter.colorchooser.Chooser "Link to this definition")

tkinter.colorchooser.askcolor(*color=None*, *\*\*options*)[¶](#tkinter.colorchooser.askcolor "Link to this definition")
:   Create a color choosing dialog. A call to this method will show the window,
    wait for the user to make a selection, and return the selected color (or
    `None`) to the caller.

See also

Module [`tkinter.commondialog`](dialog.html#module-tkinter.commondialog "tkinter.commondialog: Tkinter base class for dialogs")
:   Tkinter standard dialog module

#### Previous topic

[`tkinter` — Python interface to Tcl/Tk](tkinter.html "previous chapter")

#### Next topic

[`tkinter.font` — Tkinter font wrapper](tkinter.font.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/tkinter.colorchooser.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tkinter.font.html "tkinter.font — Tkinter font wrapper") |
* [previous](tkinter.html "tkinter — Python interface to Tcl/Tk") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Graphical user interfaces with Tk](tk.html) »
* `tkinter.colorchooser` — Color choosing dialog
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
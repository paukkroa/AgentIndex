### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tkinter.dnd.html "tkinter.dnd — Drag and drop support") |
* [previous](tkinter.messagebox.html "tkinter.messagebox — Tkinter message prompts") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Graphical user interfaces with Tk](tk.html) »
* `tkinter.scrolledtext` — Scrolled Text Widget
* |
* Theme
  Auto
  Light
  Dark
   |

# `tkinter.scrolledtext` — Scrolled Text Widget[¶](#module-tkinter.scrolledtext "Link to this heading")

**Source code:** [Lib/tkinter/scrolledtext.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/scrolledtext.py)

---

The `tkinter.scrolledtext` module provides a class of the same name which
implements a basic text widget which has a vertical scroll bar configured to do
the “right thing.” Using the [`ScrolledText`](#tkinter.scrolledtext.ScrolledText "tkinter.scrolledtext.ScrolledText") class is a lot easier than
setting up a text widget and scroll bar directly.

The text widget and scrollbar are packed together in a `Frame`, and the
methods of the `Grid` and `Pack` geometry managers are acquired
from the `Frame` object. This allows the [`ScrolledText`](#tkinter.scrolledtext.ScrolledText "tkinter.scrolledtext.ScrolledText") widget to
be used directly to achieve most normal geometry management behavior.

Should more specific control be necessary, the following attributes are
available:

*class* tkinter.scrolledtext.ScrolledText(*master=None*, *\*\*kw*)[¶](#tkinter.scrolledtext.ScrolledText "Link to this definition")
:   frame[¶](#tkinter.scrolledtext.ScrolledText.frame "Link to this definition")
    :   The frame which surrounds the text and scroll bar widgets.

    vbar[¶](#tkinter.scrolledtext.ScrolledText.vbar "Link to this definition")
    :   The scroll bar widget.

#### Previous topic

[`tkinter.messagebox` — Tkinter message prompts](tkinter.messagebox.html "previous chapter")

#### Next topic

[`tkinter.dnd` — Drag and drop support](tkinter.dnd.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/tkinter.scrolledtext.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tkinter.dnd.html "tkinter.dnd — Drag and drop support") |
* [previous](tkinter.messagebox.html "tkinter.messagebox — Tkinter message prompts") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Graphical user interfaces with Tk](tk.html) »
* `tkinter.scrolledtext` — Scrolled Text Widget
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
### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tkinter.scrolledtext.html "tkinter.scrolledtext — Scrolled Text Widget") |
* [previous](dialog.html "Tkinter Dialogs") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Graphical user interfaces with Tk](tk.html) »
* `tkinter.messagebox` — Tkinter message prompts
* |
* Theme
  Auto
  Light
  Dark
   |

# `tkinter.messagebox` — Tkinter message prompts[¶](#module-tkinter.messagebox "Link to this heading")

**Source code:** [Lib/tkinter/messagebox.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/messagebox.py)

---

The `tkinter.messagebox` module provides a template base class as well as
a variety of convenience methods for commonly used configurations. The message
boxes are modal and will return a subset of (`True`, `False`, `None`,
[`OK`](#tkinter.messagebox.OK "tkinter.messagebox.OK"), [`CANCEL`](#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL"), [`YES`](#tkinter.messagebox.YES "tkinter.messagebox.YES"), [`NO`](#tkinter.messagebox.NO "tkinter.messagebox.NO")) based on
the user’s selection. Common message box styles and layouts include but are not
limited to:

![../_images/tk_msg.png](../_images/tk_msg.png)

*class* tkinter.messagebox.Message(*master=None*, *\*\*options*)[¶](#tkinter.messagebox.Message "Link to this definition")
:   Create a message window with an application-specified message, an icon
    and a set of buttons.
    Each of the buttons in the message window is identified by a unique symbolic name (see the *type* options).

    The following options are supported:

    > *command*
    > :   Specifies the function to invoke when the user closes the dialog.
    >     The name of the button clicked by the user to close the dialog is
    >     passed as argument.
    >     This is only available on macOS.
    >
    > *default*
    > :   Gives the [symbolic name](#messagebox-buttons) of the default button
    >     for this message window ([`OK`](#tkinter.messagebox.OK "tkinter.messagebox.OK"), [`CANCEL`](#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL"), and so on).
    >     If this option is not specified, the first button in the dialog will
    >     be made the default.
    >
    > *detail*
    > :   Specifies an auxiliary message to the main message given by the
    >     *message* option.
    >     The message detail will be presented beneath the main message and,
    >     where supported by the OS, in a less emphasized font than the main
    >     message.
    >
    > *icon*
    > :   Specifies an [icon](#messagebox-icons) to display.
    >     If this option is not specified, then the [`INFO`](#tkinter.messagebox.INFO "tkinter.messagebox.INFO") icon will be
    >     displayed.
    >
    > *message*
    > :   Specifies the message to display in this message box.
    >     The default value is an empty string.
    >
    > *parent*
    > :   Makes the specified window the logical parent of the message box.
    >     The message box is displayed on top of its parent window.
    >
    > *title*
    > :   Specifies a string to display as the title of the message box.
    >     This option is ignored on macOS, where platform guidelines forbid
    >     the use of a title on this kind of dialog.
    >
    > *type*
    > :   Arranges for a [predefined set of buttons](#messagebox-types)
    >     to be displayed.

    show(*\*\*options*)[¶](#tkinter.messagebox.Message.show "Link to this definition")
    :   Display a message window and wait for the user to select one of the buttons. Then return the symbolic name of the selected button.
        Keyword arguments can override options specified in the constructor.

**Information message box**

tkinter.messagebox.showinfo(*title=None*, *message=None*, *\*\*options*)[¶](#tkinter.messagebox.showinfo "Link to this definition")
:   Creates and displays an information message box with the specified title
    and message.

**Warning message boxes**

tkinter.messagebox.showwarning(*title=None*, *message=None*, *\*\*options*)[¶](#tkinter.messagebox.showwarning "Link to this definition")
:   Creates and displays a warning message box with the specified title
    and message.

tkinter.messagebox.showerror(*title=None*, *message=None*, *\*\*options*)[¶](#tkinter.messagebox.showerror "Link to this definition")
:   Creates and displays an error message box with the specified title
    and message.

**Question message boxes**

tkinter.messagebox.askquestion(*title=None*, *message=None*, *\**, *type=YESNO*, *\*\*options*)[¶](#tkinter.messagebox.askquestion "Link to this definition")
:   Ask a question. By default shows buttons [`YES`](#tkinter.messagebox.YES "tkinter.messagebox.YES") and [`NO`](#tkinter.messagebox.NO "tkinter.messagebox.NO").
    Returns the symbolic name of the selected button.

tkinter.messagebox.askokcancel(*title=None*, *message=None*, *\*\*options*)[¶](#tkinter.messagebox.askokcancel "Link to this definition")
:   Ask if operation should proceed. Shows buttons [`OK`](#tkinter.messagebox.OK "tkinter.messagebox.OK") and [`CANCEL`](#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL").
    Returns `True` if the answer is ok and `False` otherwise.

tkinter.messagebox.askretrycancel(*title=None*, *message=None*, *\*\*options*)[¶](#tkinter.messagebox.askretrycancel "Link to this definition")
:   Ask if operation should be retried. Shows buttons [`RETRY`](#tkinter.messagebox.RETRY "tkinter.messagebox.RETRY") and [`CANCEL`](#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL").
    Return `True` if the answer is yes and `False` otherwise.

tkinter.messagebox.askyesno(*title=None*, *message=None*, *\*\*options*)[¶](#tkinter.messagebox.askyesno "Link to this definition")
:   Ask a question. Shows buttons [`YES`](#tkinter.messagebox.YES "tkinter.messagebox.YES") and [`NO`](#tkinter.messagebox.NO "tkinter.messagebox.NO").
    Returns `True` if the answer is yes and `False` otherwise.

tkinter.messagebox.askyesnocancel(*title=None*, *message=None*, *\*\*options*)[¶](#tkinter.messagebox.askyesnocancel "Link to this definition")
:   Ask a question. Shows buttons [`YES`](#tkinter.messagebox.YES "tkinter.messagebox.YES"), [`NO`](#tkinter.messagebox.NO "tkinter.messagebox.NO") and [`CANCEL`](#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL").
    Return `True` if the answer is yes, `None` if cancelled, and `False`
    otherwise.

Symbolic names of buttons:

tkinter.messagebox.ABORT *= 'abort'*[¶](#tkinter.messagebox.ABORT "Link to this definition")

tkinter.messagebox.RETRY *= 'retry'*[¶](#tkinter.messagebox.RETRY "Link to this definition")

tkinter.messagebox.IGNORE *= 'ignore'*[¶](#tkinter.messagebox.IGNORE "Link to this definition")

tkinter.messagebox.OK *= 'ok'*[¶](#tkinter.messagebox.OK "Link to this definition")

tkinter.messagebox.CANCEL *= 'cancel'*[¶](#tkinter.messagebox.CANCEL "Link to this definition")

tkinter.messagebox.YES *= 'yes'*[¶](#tkinter.messagebox.YES "Link to this definition")

tkinter.messagebox.NO *= 'no'*[¶](#tkinter.messagebox.NO "Link to this definition")

Predefined sets of buttons:

tkinter.messagebox.ABORTRETRYIGNORE *= 'abortretryignore'*[¶](#tkinter.messagebox.ABORTRETRYIGNORE "Link to this definition")
:   Displays three buttons whose symbolic names are [`ABORT`](#tkinter.messagebox.ABORT "tkinter.messagebox.ABORT"),
    [`RETRY`](#tkinter.messagebox.RETRY "tkinter.messagebox.RETRY") and [`IGNORE`](#tkinter.messagebox.IGNORE "tkinter.messagebox.IGNORE").

tkinter.messagebox.OK *= 'ok'*
:   Displays one button whose symbolic name is [`OK`](#tkinter.messagebox.OK "tkinter.messagebox.OK").

tkinter.messagebox.OKCANCEL *= 'okcancel'*[¶](#tkinter.messagebox.OKCANCEL "Link to this definition")
:   Displays two buttons whose symbolic names are [`OK`](#tkinter.messagebox.OK "tkinter.messagebox.OK") and
    [`CANCEL`](#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL").

tkinter.messagebox.RETRYCANCEL *= 'retrycancel'*[¶](#tkinter.messagebox.RETRYCANCEL "Link to this definition")
:   Displays two buttons whose symbolic names are [`RETRY`](#tkinter.messagebox.RETRY "tkinter.messagebox.RETRY") and
    [`CANCEL`](#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL").

tkinter.messagebox.YESNO *= 'yesno'*[¶](#tkinter.messagebox.YESNO "Link to this definition")
:   Displays two buttons whose symbolic names are [`YES`](#tkinter.messagebox.YES "tkinter.messagebox.YES") and
    [`NO`](#tkinter.messagebox.NO "tkinter.messagebox.NO").

tkinter.messagebox.YESNOCANCEL *= 'yesnocancel'*[¶](#tkinter.messagebox.YESNOCANCEL "Link to this definition")
:   Displays three buttons whose symbolic names are [`YES`](#tkinter.messagebox.YES "tkinter.messagebox.YES"),
    [`NO`](#tkinter.messagebox.NO "tkinter.messagebox.NO") and [`CANCEL`](#tkinter.messagebox.CANCEL "tkinter.messagebox.CANCEL").

Icon images:

tkinter.messagebox.ERROR *= 'error'*[¶](#tkinter.messagebox.ERROR "Link to this definition")

tkinter.messagebox.INFO *= 'info'*[¶](#tkinter.messagebox.INFO "Link to this definition")

tkinter.messagebox.QUESTION *= 'question'*[¶](#tkinter.messagebox.QUESTION "Link to this definition")

tkinter.messagebox.WARNING *= 'warning'*[¶](#tkinter.messagebox.WARNING "Link to this definition")

#### Previous topic

[Tkinter Dialogs](dialog.html "previous chapter")

#### Next topic

[`tkinter.scrolledtext` — Scrolled Text Widget](tkinter.scrolledtext.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/tkinter.messagebox.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tkinter.scrolledtext.html "tkinter.scrolledtext — Scrolled Text Widget") |
* [previous](dialog.html "Tkinter Dialogs") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Graphical user interfaces with Tk](tk.html) »
* `tkinter.messagebox` — Tkinter message prompts
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
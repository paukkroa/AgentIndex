### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tkinter.html "tkinter — Python interface to Tcl/Tk") |
* [previous](locale.html "locale — Internationalization services") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Graphical user interfaces with Tk
* |
* Theme
  Auto
  Light
  Dark
   |

# Graphical user interfaces with Tk[¶](#graphical-user-interfaces-with-tk "Link to this heading")

Tk/Tcl has long been an integral part of Python. It provides a robust and
platform independent windowing toolkit, that is available to Python programmers
using the [`tkinter`](tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces") package, and its extension, the [`tkinter.ttk`](tkinter.ttk.html#module-tkinter.ttk "tkinter.ttk: Tk themed widget set") module.

The [`tkinter`](tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces") package is a thin object-oriented layer on top of Tcl/Tk. To
use [`tkinter`](tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces"), you don’t need to write Tcl code, but you will need to
consult the Tk documentation, and occasionally the Tcl documentation.
[`tkinter`](tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces") is a set of wrappers that implement the Tk widgets as Python
classes.

[`tkinter`](tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")’s chief virtues are that it is fast, and that it usually comes
bundled with Python. Although its standard documentation is weak, good
material is available, which includes: references, tutorials, a book and
others. [`tkinter`](tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces") is also famous for having an outdated look and feel,
which has been vastly improved in Tk 8.5. Nevertheless, there are many other
GUI libraries that you could be interested in. The Python wiki lists several
alternative [GUI frameworks and tools](https://wiki.python.org/moin/GuiProgramming).

* [`tkinter` — Python interface to Tcl/Tk](tkinter.html)
  + [Architecture](tkinter.html#architecture)
  + [Tkinter Modules](tkinter.html#tkinter-modules)
  + [Tkinter Life Preserver](tkinter.html#tkinter-life-preserver)
    - [A Hello World Program](tkinter.html#a-hello-world-program)
    - [Important Tk Concepts](tkinter.html#important-tk-concepts)
    - [Understanding How Tkinter Wraps Tcl/Tk](tkinter.html#understanding-how-tkinter-wraps-tcl-tk)
    - [How do I…? What option does…?](tkinter.html#how-do-i-what-option-does)
    - [Navigating the Tcl/Tk Reference Manual](tkinter.html#navigating-the-tcl-tk-reference-manual)
  + [Threading model](tkinter.html#threading-model)
  + [Handy Reference](tkinter.html#handy-reference)
    - [Setting Options](tkinter.html#setting-options)
    - [The Packer](tkinter.html#the-packer)
    - [Packer Options](tkinter.html#packer-options)
    - [Coupling Widget Variables](tkinter.html#coupling-widget-variables)
    - [The Window Manager](tkinter.html#the-window-manager)
    - [Tk Option Data Types](tkinter.html#tk-option-data-types)
    - [Bindings and Events](tkinter.html#bindings-and-events)
    - [The index Parameter](tkinter.html#the-index-parameter)
    - [Images](tkinter.html#images)
  + [File Handlers](tkinter.html#file-handlers)
* [`tkinter.colorchooser` — Color choosing dialog](tkinter.colorchooser.html)
* [`tkinter.font` — Tkinter font wrapper](tkinter.font.html)
* [Tkinter Dialogs](dialog.html)
  + [`tkinter.simpledialog` — Standard Tkinter input dialogs](dialog.html#module-tkinter.simpledialog)
  + [`tkinter.filedialog` — File selection dialogs](dialog.html#module-tkinter.filedialog)
    - [Native Load/Save Dialogs](dialog.html#native-load-save-dialogs)
  + [`tkinter.commondialog` — Dialog window templates](dialog.html#module-tkinter.commondialog)
* [`tkinter.messagebox` — Tkinter message prompts](tkinter.messagebox.html)
* [`tkinter.scrolledtext` — Scrolled Text Widget](tkinter.scrolledtext.html)
* [`tkinter.dnd` — Drag and drop support](tkinter.dnd.html)
* [`tkinter.ttk` — Tk themed widgets](tkinter.ttk.html)
  + [Using Ttk](tkinter.ttk.html#using-ttk)
  + [Ttk Widgets](tkinter.ttk.html#ttk-widgets)
  + [Widget](tkinter.ttk.html#widget)
    - [Standard Options](tkinter.ttk.html#standard-options)
    - [Scrollable Widget Options](tkinter.ttk.html#scrollable-widget-options)
    - [Label Options](tkinter.ttk.html#label-options)
    - [Compatibility Options](tkinter.ttk.html#compatibility-options)
    - [Widget States](tkinter.ttk.html#widget-states)
    - [ttk.Widget](tkinter.ttk.html#ttk-widget)
  + [Combobox](tkinter.ttk.html#combobox)
    - [Options](tkinter.ttk.html#options)
    - [Virtual events](tkinter.ttk.html#virtual-events)
    - [ttk.Combobox](tkinter.ttk.html#ttk-combobox)
  + [Spinbox](tkinter.ttk.html#spinbox)
    - [Options](tkinter.ttk.html#id1)
    - [Virtual events](tkinter.ttk.html#id2)
    - [ttk.Spinbox](tkinter.ttk.html#ttk-spinbox)
  + [Notebook](tkinter.ttk.html#notebook)
    - [Options](tkinter.ttk.html#id3)
    - [Tab Options](tkinter.ttk.html#tab-options)
    - [Tab Identifiers](tkinter.ttk.html#tab-identifiers)
    - [Virtual Events](tkinter.ttk.html#id4)
    - [ttk.Notebook](tkinter.ttk.html#ttk-notebook)
  + [Progressbar](tkinter.ttk.html#progressbar)
    - [Options](tkinter.ttk.html#id5)
    - [ttk.Progressbar](tkinter.ttk.html#ttk-progressbar)
  + [Separator](tkinter.ttk.html#separator)
    - [Options](tkinter.ttk.html#id6)
  + [Sizegrip](tkinter.ttk.html#sizegrip)
    - [Platform-specific notes](tkinter.ttk.html#platform-specific-notes)
    - [Bugs](tkinter.ttk.html#bugs)
  + [Treeview](tkinter.ttk.html#treeview)
    - [Options](tkinter.ttk.html#id7)
    - [Item Options](tkinter.ttk.html#item-options)
    - [Tag Options](tkinter.ttk.html#tag-options)
    - [Column Identifiers](tkinter.ttk.html#column-identifiers)
    - [Virtual Events](tkinter.ttk.html#id8)
    - [ttk.Treeview](tkinter.ttk.html#ttk-treeview)
  + [Ttk Styling](tkinter.ttk.html#ttk-styling)
    - [Layouts](tkinter.ttk.html#layouts)
* [IDLE — Python editor and shell](idle.html)
  + [Menus](idle.html#menus)
    - [File menu (Shell and Editor)](idle.html#file-menu-shell-and-editor)
    - [Edit menu (Shell and Editor)](idle.html#edit-menu-shell-and-editor)
    - [Format menu (Editor window only)](idle.html#format-menu-editor-window-only)
    - [Run menu (Editor window only)](idle.html#run-menu-editor-window-only)
    - [Shell menu (Shell window only)](idle.html#shell-menu-shell-window-only)
    - [Debug menu (Shell window only)](idle.html#debug-menu-shell-window-only)
    - [Options menu (Shell and Editor)](idle.html#options-menu-shell-and-editor)
    - [Window menu (Shell and Editor)](idle.html#window-menu-shell-and-editor)
    - [Help menu (Shell and Editor)](idle.html#help-menu-shell-and-editor)
    - [Context menus](idle.html#context-menus)
  + [Editing and Navigation](idle.html#editing-and-navigation)
    - [Editor windows](idle.html#editor-windows)
    - [Key bindings](idle.html#key-bindings)
    - [Automatic indentation](idle.html#automatic-indentation)
    - [Search and Replace](idle.html#search-and-replace)
    - [Completions](idle.html#completions)
    - [Calltips](idle.html#calltips)
    - [Format block](idle.html#format-block)
    - [Code Context](idle.html#code-context)
    - [Shell window](idle.html#shell-window)
    - [Text colors](idle.html#text-colors)
  + [Startup and Code Execution](idle.html#startup-and-code-execution)
    - [Command-line usage](idle.html#command-line-usage)
    - [Startup failure](idle.html#startup-failure)
    - [Running user code](idle.html#running-user-code)
    - [User output in Shell](idle.html#user-output-in-shell)
    - [Developing tkinter applications](idle.html#developing-tkinter-applications)
    - [Running without a subprocess](idle.html#running-without-a-subprocess)
  + [Help and Preferences](idle.html#help-and-preferences)
    - [Help sources](idle.html#help-sources)
    - [Setting preferences](idle.html#setting-preferences)
    - [IDLE on macOS](idle.html#idle-on-macos)
    - [Extensions](idle.html#extensions)
  + [idlelib — implementation of IDLE application](idle.html#module-idlelib)
* [`turtle` — Turtle graphics](turtle.html)
  + [Introduction](turtle.html#introduction)
  + [Get started](turtle.html#get-started)
  + [Tutorial](turtle.html#tutorial)
    - [Starting a turtle environment](turtle.html#starting-a-turtle-environment)
    - [Basic drawing](turtle.html#basic-drawing)
      * [Pen control](turtle.html#pen-control)
      * [The turtle’s position](turtle.html#the-turtle-s-position)
    - [Making algorithmic patterns](turtle.html#making-algorithmic-patterns)
  + [How to…](turtle.html#how-to)
    - [Get started as quickly as possible](turtle.html#get-started-as-quickly-as-possible)
    - [Automatically begin and end filling](turtle.html#automatically-begin-and-end-filling)
    - [Use the `turtle` module namespace](turtle.html#use-the-turtle-module-namespace)
    - [Use turtle graphics in a script](turtle.html#use-turtle-graphics-in-a-script)
    - [Use object-oriented turtle graphics](turtle.html#use-object-oriented-turtle-graphics)
  + [Turtle graphics reference](turtle.html#turtle-graphics-reference)
    - [Turtle methods](turtle.html#turtle-methods)
    - [Methods of TurtleScreen/Screen](turtle.html#methods-of-turtlescreen-screen)
  + [Methods of RawTurtle/Turtle and corresponding functions](turtle.html#methods-of-rawturtle-turtle-and-corresponding-functions)
    - [Turtle motion](turtle.html#turtle-motion)
    - [Tell Turtle’s state](turtle.html#tell-turtle-s-state)
    - [Settings for measurement](turtle.html#settings-for-measurement)
    - [Pen control](turtle.html#id1)
      * [Drawing state](turtle.html#drawing-state)
      * [Color control](turtle.html#color-control)
      * [Filling](turtle.html#filling)
      * [More drawing control](turtle.html#more-drawing-control)
    - [Turtle state](turtle.html#turtle-state)
      * [Visibility](turtle.html#visibility)
      * [Appearance](turtle.html#appearance)
    - [Using events](turtle.html#using-events)
    - [Special Turtle methods](turtle.html#special-turtle-methods)
    - [Compound shapes](turtle.html#compound-shapes)
  + [Methods of TurtleScreen/Screen and corresponding functions](turtle.html#methods-of-turtlescreen-screen-and-corresponding-functions)
    - [Window control](turtle.html#window-control)
    - [Animation control](turtle.html#animation-control)
    - [Using screen events](turtle.html#using-screen-events)
    - [Input methods](turtle.html#input-methods)
    - [Settings and special methods](turtle.html#settings-and-special-methods)
    - [Methods specific to Screen, not inherited from TurtleScreen](turtle.html#methods-specific-to-screen-not-inherited-from-turtlescreen)
  + [Public classes](turtle.html#public-classes)
  + [Explanation](turtle.html#explanation)
  + [Help and configuration](turtle.html#help-and-configuration)
    - [How to use help](turtle.html#how-to-use-help)
    - [Translation of docstrings into different languages](turtle.html#translation-of-docstrings-into-different-languages)
    - [How to configure Screen and Turtles](turtle.html#how-to-configure-screen-and-turtles)
  + [`turtledemo` — Demo scripts](turtle.html#module-turtledemo)
  + [Changes since Python 2.6](turtle.html#changes-since-python-2-6)
  + [Changes since Python 3.0](turtle.html#changes-since-python-3-0)

#### Previous topic

[`locale` — Internationalization services](locale.html "previous chapter")

#### Next topic

[`tkinter` — Python interface to Tcl/Tk](tkinter.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/tk.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tkinter.html "tkinter — Python interface to Tcl/Tk") |
* [previous](locale.html "locale — Internationalization services") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Graphical user interfaces with Tk
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
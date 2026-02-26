### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tkinter.messagebox.html "tkinter.messagebox — Tkinter message prompts") |
* [previous](tkinter.font.html "tkinter.font — Tkinter font wrapper") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Graphical user interfaces with Tk](tk.html) »
* Tkinter Dialogs
* |
* Theme
  Auto
  Light
  Dark
   |

# Tkinter Dialogs[¶](#tkinter-dialogs "Link to this heading")

## `tkinter.simpledialog` — Standard Tkinter input dialogs[¶](#module-tkinter.simpledialog "Link to this heading")

**Source code:** [Lib/tkinter/simpledialog.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/simpledialog.py)

---

The `tkinter.simpledialog` module contains convenience classes and
functions for creating simple modal dialogs to get a value from the user.

tkinter.simpledialog.askfloat(*title*, *prompt*, *\*\*kw*)[¶](#tkinter.simpledialog.askfloat "Link to this definition")

tkinter.simpledialog.askinteger(*title*, *prompt*, *\*\*kw*)[¶](#tkinter.simpledialog.askinteger "Link to this definition")

tkinter.simpledialog.askstring(*title*, *prompt*, *\*\*kw*)[¶](#tkinter.simpledialog.askstring "Link to this definition")
:   The above three functions provide dialogs that prompt the user to enter a value
    of the desired type.

*class* tkinter.simpledialog.Dialog(*parent*, *title=None*)[¶](#tkinter.simpledialog.Dialog "Link to this definition")
:   The base class for custom dialogs.

    body(*master*)[¶](#tkinter.simpledialog.Dialog.body "Link to this definition")
    :   Override to construct the dialog’s interface and return the widget that
        should have initial focus.

    buttonbox()[¶](#tkinter.simpledialog.Dialog.buttonbox "Link to this definition")
    :   Default behaviour adds OK and Cancel buttons. Override for custom button
        layouts.

## `tkinter.filedialog` — File selection dialogs[¶](#module-tkinter.filedialog "Link to this heading")

**Source code:** [Lib/tkinter/filedialog.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/filedialog.py)

---

The `tkinter.filedialog` module provides classes and factory functions for
creating file/directory selection windows.

### Native Load/Save Dialogs[¶](#native-load-save-dialogs "Link to this heading")

The following classes and functions provide file dialog windows that combine a
native look-and-feel with configuration options to customize behaviour.
The following keyword arguments are applicable to the classes and functions
listed below:

> *parent* - the window to place the dialog on top of
>
> *title* - the title of the window
>
> *initialdir* - the directory that the dialog starts in
>
> *initialfile* - the file selected upon opening of the dialog
>
> *filetypes* - a sequence of (label, pattern) tuples, ‘\*’ wildcard is allowed
>
> *defaultextension* - default extension to append to file (save dialogs)
>
> *multiple* - when true, selection of multiple items is allowed

**Static factory functions**

The below functions when called create a modal, native look-and-feel dialog,
wait for the user’s selection, then return the selected value(s) or `None` to the
caller.

tkinter.filedialog.askopenfile(*mode='r'*, *\*\*options*)[¶](#tkinter.filedialog.askopenfile "Link to this definition")

tkinter.filedialog.askopenfiles(*mode='r'*, *\*\*options*)[¶](#tkinter.filedialog.askopenfiles "Link to this definition")
:   The above two functions create an [`Open`](#tkinter.filedialog.Open "tkinter.filedialog.Open") dialog and return the opened
    file object(s) in read-only mode.

tkinter.filedialog.asksaveasfile(*mode='w'*, *\*\*options*)[¶](#tkinter.filedialog.asksaveasfile "Link to this definition")
:   Create a [`SaveAs`](#tkinter.filedialog.SaveAs "tkinter.filedialog.SaveAs") dialog and return a file object opened in write-only mode.

tkinter.filedialog.askopenfilename(*\*\*options*)[¶](#tkinter.filedialog.askopenfilename "Link to this definition")

tkinter.filedialog.askopenfilenames(*\*\*options*)[¶](#tkinter.filedialog.askopenfilenames "Link to this definition")
:   The above two functions create an [`Open`](#tkinter.filedialog.Open "tkinter.filedialog.Open") dialog and return the
    selected filename(s) that correspond to existing file(s).

tkinter.filedialog.asksaveasfilename(*\*\*options*)[¶](#tkinter.filedialog.asksaveasfilename "Link to this definition")
:   Create a [`SaveAs`](#tkinter.filedialog.SaveAs "tkinter.filedialog.SaveAs") dialog and return the selected filename.

tkinter.filedialog.askdirectory(*\*\*options*)[¶](#tkinter.filedialog.askdirectory "Link to this definition")
:   Prompt user to select a directory.

    Additional keyword option:

    *mustexist* - determines if selection must be an existing directory.

*class* tkinter.filedialog.Open(*master=None*, *\*\*options*)[¶](#tkinter.filedialog.Open "Link to this definition")

*class* tkinter.filedialog.SaveAs(*master=None*, *\*\*options*)[¶](#tkinter.filedialog.SaveAs "Link to this definition")
:   The above two classes provide native dialog windows for saving and loading
    files.

**Convenience classes**

The below classes are used for creating file/directory windows from scratch.
These do not emulate the native look-and-feel of the platform.

*class* tkinter.filedialog.Directory(*master=None*, *\*\*options*)[¶](#tkinter.filedialog.Directory "Link to this definition")
:   Create a dialog prompting the user to select a directory.

Note

The *FileDialog* class should be subclassed for custom event
handling and behaviour.

*class* tkinter.filedialog.FileDialog(*master*, *title=None*)[¶](#tkinter.filedialog.FileDialog "Link to this definition")
:   Create a basic file selection dialog.

    cancel\_command(*event=None*)[¶](#tkinter.filedialog.FileDialog.cancel_command "Link to this definition")
    :   Trigger the termination of the dialog window.

    dirs\_double\_event(*event*)[¶](#tkinter.filedialog.FileDialog.dirs_double_event "Link to this definition")
    :   Event handler for double-click event on directory.

    dirs\_select\_event(*event*)[¶](#tkinter.filedialog.FileDialog.dirs_select_event "Link to this definition")
    :   Event handler for click event on directory.

    files\_double\_event(*event*)[¶](#tkinter.filedialog.FileDialog.files_double_event "Link to this definition")
    :   Event handler for double-click event on file.

    files\_select\_event(*event*)[¶](#tkinter.filedialog.FileDialog.files_select_event "Link to this definition")
    :   Event handler for single-click event on file.

    filter\_command(*event=None*)[¶](#tkinter.filedialog.FileDialog.filter_command "Link to this definition")
    :   Filter the files by directory.

    get\_filter()[¶](#tkinter.filedialog.FileDialog.get_filter "Link to this definition")
    :   Retrieve the file filter currently in use.

    get\_selection()[¶](#tkinter.filedialog.FileDialog.get_selection "Link to this definition")
    :   Retrieve the currently selected item.

    go(*dir\_or\_file=os.curdir*, *pattern='\*'*, *default=''*, *key=None*)[¶](#tkinter.filedialog.FileDialog.go "Link to this definition")
    :   Render dialog and start event loop.

    ok\_event(*event*)[¶](#tkinter.filedialog.FileDialog.ok_event "Link to this definition")
    :   Exit dialog returning current selection.

    quit(*how=None*)[¶](#tkinter.filedialog.FileDialog.quit "Link to this definition")
    :   Exit dialog returning filename, if any.

    set\_filter(*dir*, *pat*)[¶](#tkinter.filedialog.FileDialog.set_filter "Link to this definition")
    :   Set the file filter.

    set\_selection(*file*)[¶](#tkinter.filedialog.FileDialog.set_selection "Link to this definition")
    :   Update the current file selection to *file*.

*class* tkinter.filedialog.LoadFileDialog(*master*, *title=None*)[¶](#tkinter.filedialog.LoadFileDialog "Link to this definition")
:   A subclass of FileDialog that creates a dialog window for selecting an
    existing file.

    ok\_command()[¶](#tkinter.filedialog.LoadFileDialog.ok_command "Link to this definition")
    :   Test that a file is provided and that the selection indicates an
        already existing file.

*class* tkinter.filedialog.SaveFileDialog(*master*, *title=None*)[¶](#tkinter.filedialog.SaveFileDialog "Link to this definition")
:   A subclass of FileDialog that creates a dialog window for selecting a
    destination file.

    ok\_command()[¶](#tkinter.filedialog.SaveFileDialog.ok_command "Link to this definition")
    :   Test whether or not the selection points to a valid file that is not a
        directory. Confirmation is required if an already existing file is
        selected.

## `tkinter.commondialog` — Dialog window templates[¶](#module-tkinter.commondialog "Link to this heading")

**Source code:** [Lib/tkinter/commondialog.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/commondialog.py)

---

The `tkinter.commondialog` module provides the [`Dialog`](#tkinter.commondialog.Dialog "tkinter.commondialog.Dialog") class that
is the base class for dialogs defined in other supporting modules.

*class* tkinter.commondialog.Dialog(*master=None*, *\*\*options*)[¶](#tkinter.commondialog.Dialog "Link to this definition")
:   show(*\*\*options*)[¶](#tkinter.commondialog.Dialog.show "Link to this definition")
    :   Render the Dialog window.

See also

Modules [`tkinter.messagebox`](tkinter.messagebox.html#module-tkinter.messagebox "tkinter.messagebox: Various types of alert dialogs"), [Reading and Writing Files](../tutorial/inputoutput.html#tut-files)

### [Table of Contents](../contents.html)

* [Tkinter Dialogs](#)
  + [`tkinter.simpledialog` — Standard Tkinter input dialogs](#module-tkinter.simpledialog)
  + [`tkinter.filedialog` — File selection dialogs](#module-tkinter.filedialog)
    - [Native Load/Save Dialogs](#native-load-save-dialogs)
  + [`tkinter.commondialog` — Dialog window templates](#module-tkinter.commondialog)

#### Previous topic

[`tkinter.font` — Tkinter font wrapper](tkinter.font.html "previous chapter")

#### Next topic

[`tkinter.messagebox` — Tkinter message prompts](tkinter.messagebox.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/dialog.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tkinter.messagebox.html "tkinter.messagebox — Tkinter message prompts") |
* [previous](tkinter.font.html "tkinter.font — Tkinter font wrapper") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Graphical user interfaces with Tk](tk.html) »
* Tkinter Dialogs
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
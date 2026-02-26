### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](dialog.html "Tkinter Dialogs") |
* [previous](tkinter.colorchooser.html "tkinter.colorchooser — Color choosing dialog") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Graphical user interfaces with Tk](tk.html) »
* `tkinter.font` — Tkinter font wrapper
* |
* Theme
  Auto
  Light
  Dark
   |

# `tkinter.font` — Tkinter font wrapper[¶](#module-tkinter.font "Link to this heading")

**Source code:** [Lib/tkinter/font.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/font.py)

---

The `tkinter.font` module provides the [`Font`](#tkinter.font.Font "tkinter.font.Font") class for creating
and using named fonts.

The different font weights and slants are:

tkinter.font.NORMAL[¶](#tkinter.font.NORMAL "Link to this definition")

tkinter.font.BOLD[¶](#tkinter.font.BOLD "Link to this definition")

tkinter.font.ITALIC[¶](#tkinter.font.ITALIC "Link to this definition")

tkinter.font.ROMAN[¶](#tkinter.font.ROMAN "Link to this definition")

*class* tkinter.font.Font(*root=None*, *font=None*, *name=None*, *exists=False*, *\*\*options*)[¶](#tkinter.font.Font "Link to this definition")
:   The [`Font`](#tkinter.font.Font "tkinter.font.Font") class represents a named font. *Font* instances are given
    unique names and can be specified by their family, size, and style
    configuration. Named fonts are Tk’s method of creating and identifying
    fonts as a single object, rather than specifying a font by its attributes
    with each occurrence.

    > arguments:
    >
    > > *font* - font specifier tuple (family, size, options)
    > >
    > > *name* - unique font name
    > >
    > > *exists* - self points to existing named font if true
    >
    > additional keyword options (ignored if *font* is specified):
    >
    > > *family* - font family i.e. Courier, Times
    > >
    > > *size* - font size
    > >
    > > If *size* is positive it is interpreted as size in points.
    > >
    > > If *size* is a negative number its absolute value is treated
    > >
    > > as size in pixels.
    > >
    > > *weight* - font emphasis (NORMAL, BOLD)
    > >
    > > *slant* - ROMAN, ITALIC
    > >
    > > *underline* - font underlining (0 - none, 1 - underline)
    > >
    > > *overstrike* - font strikeout (0 - none, 1 - strikeout)

    actual(*option=None*, *displayof=None*)[¶](#tkinter.font.Font.actual "Link to this definition")
    :   Return the attributes of the font.

    cget(*option*)[¶](#tkinter.font.Font.cget "Link to this definition")
    :   Retrieve an attribute of the font.

    config(*\*\*options*)[¶](#tkinter.font.Font.config "Link to this definition")
    :   Modify attributes of the font.

    copy()[¶](#tkinter.font.Font.copy "Link to this definition")
    :   Return new instance of the current font.

    measure(*text*, *displayof=None*)[¶](#tkinter.font.Font.measure "Link to this definition")
    :   Return amount of space the text would occupy on the specified display
        when formatted in the current font. If no display is specified then the
        main application window is assumed.

    metrics(*\*options*, *\*\*kw*)[¶](#tkinter.font.Font.metrics "Link to this definition")
    :   Return font-specific data.
        Options include:

        *ascent* - distance between baseline and highest point that a
        :   character of the font can occupy

        *descent* - distance between baseline and lowest point that a
        :   character of the font can occupy

        *linespace* - minimum vertical separation necessary between any two
        :   characters of the font that ensures no vertical overlap between lines.

        *fixed* - 1 if font is fixed-width else 0

tkinter.font.families(*root=None*, *displayof=None*)[¶](#tkinter.font.families "Link to this definition")
:   Return the different font families.

tkinter.font.names(*root=None*)[¶](#tkinter.font.names "Link to this definition")
:   Return the names of defined fonts.

tkinter.font.nametofont(*name*, *root=None*)[¶](#tkinter.font.nametofont "Link to this definition")
:   Return a [`Font`](#tkinter.font.Font "tkinter.font.Font") representation of a tk named font.

    Changed in version 3.10: The *root* parameter was added.

#### Previous topic

[`tkinter.colorchooser` — Color choosing dialog](tkinter.colorchooser.html "previous chapter")

#### Next topic

[Tkinter Dialogs](dialog.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/tkinter.font.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](dialog.html "Tkinter Dialogs") |
* [previous](tkinter.colorchooser.html "tkinter.colorchooser — Color choosing dialog") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Graphical user interfaces with Tk](tk.html) »
* `tkinter.font` — Tkinter font wrapper
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
### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](netrc.html "netrc — netrc file processing") |
* [previous](configparser.html "configparser — Configuration file parser") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [File Formats](fileformats.html) »
* `tomllib` — Parse TOML files
* |
* Theme
  Auto
  Light
  Dark
   |

# `tomllib` — Parse TOML files[¶](#module-tomllib "Link to this heading")

Added in version 3.11.

**Source code:** [Lib/tomllib](https://github.com/python/cpython/tree/3.14/Lib/tomllib)

---

This module provides an interface for parsing TOML 1.0.0 (Tom’s Obvious Minimal
Language, [https://toml.io](https://toml.io/en/)). This module does not
support writing TOML.

See also

The [Tomli-W package](https://pypi.org/project/tomli-w/)
is a TOML writer that can be used in conjunction with this module,
providing a write API familiar to users of the standard library
[`marshal`](marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).") and [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") modules.

See also

The [TOML Kit package](https://pypi.org/project/tomlkit/)
is a style-preserving TOML library with both read and write capability.
It is a recommended replacement for this module for editing already
existing TOML files.

This module defines the following functions:

tomllib.load(*fp*, */*, *\**, *parse\_float=float*)[¶](#tomllib.load "Link to this definition")
:   Read a TOML file. The first argument should be a readable and binary file object.
    Return a [`dict`](stdtypes.html#dict "dict"). Convert TOML types to Python using this
    [conversion table](#toml-to-py-table).

    *parse\_float* will be called with the string of every TOML
    float to be decoded. By default, this is equivalent to `float(num_str)`.
    This can be used to use another datatype or parser for TOML floats
    (e.g. [`decimal.Decimal`](decimal.html#decimal.Decimal "decimal.Decimal")). The callable must not return a
    [`dict`](stdtypes.html#dict "dict") or a [`list`](stdtypes.html#list "list"), else a [`ValueError`](exceptions.html#ValueError "ValueError") is raised.

    A [`TOMLDecodeError`](#tomllib.TOMLDecodeError "tomllib.TOMLDecodeError") will be raised on an invalid TOML document.

tomllib.loads(*s*, */*, *\**, *parse\_float=float*)[¶](#tomllib.loads "Link to this definition")
:   Load TOML from a [`str`](stdtypes.html#str "str") object. Return a [`dict`](stdtypes.html#dict "dict"). Convert TOML
    types to Python using this [conversion table](#toml-to-py-table). The
    *parse\_float* argument has the same meaning as in [`load()`](#tomllib.load "tomllib.load").

    A [`TOMLDecodeError`](#tomllib.TOMLDecodeError "tomllib.TOMLDecodeError") will be raised on an invalid TOML document.

The following exceptions are available:

*exception* tomllib.TOMLDecodeError(*msg*, *doc*, *pos*)[¶](#tomllib.TOMLDecodeError "Link to this definition")
:   Subclass of [`ValueError`](exceptions.html#ValueError "ValueError") with the following additional attributes:

    msg[¶](#tomllib.TOMLDecodeError.msg "Link to this definition")
    :   The unformatted error message.

    doc[¶](#tomllib.TOMLDecodeError.doc "Link to this definition")
    :   The TOML document being parsed.

    pos[¶](#tomllib.TOMLDecodeError.pos "Link to this definition")
    :   The index of *doc* where parsing failed.

    lineno[¶](#tomllib.TOMLDecodeError.lineno "Link to this definition")
    :   The line corresponding to *pos*.

    colno[¶](#tomllib.TOMLDecodeError.colno "Link to this definition")
    :   The column corresponding to *pos*.

    Changed in version 3.14: Added the *msg*, *doc* and *pos* parameters.
    Added the [`msg`](#tomllib.TOMLDecodeError.msg "tomllib.TOMLDecodeError.msg"), [`doc`](#tomllib.TOMLDecodeError.doc "tomllib.TOMLDecodeError.doc"), [`pos`](#tomllib.TOMLDecodeError.pos "tomllib.TOMLDecodeError.pos"), [`lineno`](#tomllib.TOMLDecodeError.lineno "tomllib.TOMLDecodeError.lineno") and [`colno`](#tomllib.TOMLDecodeError.colno "tomllib.TOMLDecodeError.colno") attributes.

    Deprecated since version 3.14: Passing free-form positional arguments is deprecated.

## Examples[¶](#examples "Link to this heading")

Parsing a TOML file:

```
import tomllib

with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)
```

Parsing a TOML string:

```
import tomllib

toml_str = """
python-version = "3.11.0"
python-implementation = "CPython"
"""

data = tomllib.loads(toml_str)
```

## Conversion Table[¶](#conversion-table "Link to this heading")

| TOML | Python |
| --- | --- |
| TOML document | dict |
| string | str |
| integer | int |
| float | float (configurable with *parse\_float*) |
| boolean | bool |
| offset date-time | datetime.datetime (`tzinfo` attribute set to an instance of `datetime.timezone`) |
| local date-time | datetime.datetime (`tzinfo` attribute set to `None`) |
| local date | datetime.date |
| local time | datetime.time |
| array | list |
| table | dict |
| inline table | dict |
| array of tables | list of dicts |

### [Table of Contents](../contents.html)

* [`tomllib` — Parse TOML files](#)
  + [Examples](#examples)
  + [Conversion Table](#conversion-table)

#### Previous topic

[`configparser` — Configuration file parser](configparser.html "previous chapter")

#### Next topic

[`netrc` — netrc file processing](netrc.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/tomllib.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](netrc.html "netrc — netrc file processing") |
* [previous](configparser.html "configparser — Configuration file parser") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [File Formats](fileformats.html) »
* `tomllib` — Parse TOML files
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
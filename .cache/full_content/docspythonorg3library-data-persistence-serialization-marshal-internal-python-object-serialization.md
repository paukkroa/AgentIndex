### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](dbm.html "dbm — Interfaces to Unix “databases”") |
* [previous](shelve.html "shelve — Python object persistence") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Persistence](persistence.html) »
* `marshal` — Internal Python object serialization
* |
* Theme
  Auto
  Light
  Dark
   |

# `marshal` — Internal Python object serialization[¶](#module-marshal "Link to this heading")

---

This module contains functions that can read and write Python values in a binary
format. The format is specific to Python, but independent of machine
architecture issues (e.g., you can write a Python value to a file on a PC,
transport the file to a Mac, and read it back there). Details of the format are
undocumented on purpose; it may change between Python versions (although it
rarely does). [[1]](#id2)

This is not a general “persistence” module. For general persistence and
transfer of Python objects through RPC calls, see the modules [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") and
[`shelve`](shelve.html#module-shelve "shelve: Python object persistence."). The `marshal` module exists mainly to support reading and
writing the “pseudo-compiled” code for Python modules of `.pyc` files.
Therefore, the Python maintainers reserve the right to modify the marshal format
in backward incompatible ways should the need arise.
The format of code objects is not compatible between Python versions,
even if the version of the format is the same.
De-serializing a code object in the incorrect Python version has undefined behavior.
If you’re serializing and
de-serializing Python objects, use the [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") module instead – the
performance is comparable, version independence is guaranteed, and pickle
supports a substantially wider range of objects than marshal.

Warning

The `marshal` module is not intended to be secure against erroneous or
maliciously constructed data. Never unmarshal data received from an
untrusted or unauthenticated source.

There are functions that read/write files as well as functions operating on
bytes-like objects.

Not all Python object types are supported; in general, only objects whose value
is independent from a particular invocation of Python can be written and read by
this module. The following types are supported:

* Numeric types: [`int`](functions.html#int "int"), [`bool`](functions.html#bool "bool"), [`float`](functions.html#float "float"), [`complex`](functions.html#complex "complex").
* Strings ([`str`](stdtypes.html#str "str")) and [`bytes`](stdtypes.html#bytes "bytes").
  [Bytes-like objects](../glossary.html#term-bytes-like-object) like [`bytearray`](stdtypes.html#bytearray "bytearray") are
  marshalled as `bytes`.
* Containers: [`tuple`](stdtypes.html#tuple "tuple"), [`list`](stdtypes.html#list "list"), [`set`](stdtypes.html#set "set"), [`frozenset`](stdtypes.html#frozenset "frozenset"),
  and (since [`version`](#marshal.version "marshal.version") 5), [`slice`](functions.html#slice "slice").
  It should be understood that these are supported only if the values contained
  therein are themselves supported.
  Recursive containers are supported since [`version`](#marshal.version "marshal.version") 3.
* The singletons [`None`](constants.html#None "None"), [`Ellipsis`](constants.html#Ellipsis "Ellipsis") and [`StopIteration`](exceptions.html#StopIteration "StopIteration").
* [`code`](code.html#module-code "code: Facilities to implement read-eval-print loops.") objects, if *allow\_code* is true. See note above about
  version dependence.

Changed in version 3.4:

* Added format version 3, which supports marshalling recursive lists, sets
  and dictionaries.
* Added format version 4, which supports efficient representations
  of short strings.

Changed in version 3.14: Added format version 5, which allows marshalling slices.

The module defines these functions:

marshal.dump(*value*, *file*, *version=version*, */*, *\**, *allow\_code=True*)[¶](#marshal.dump "Link to this definition")
:   Write the value on the open file. The value must be a supported type. The
    file must be a writeable [binary file](../glossary.html#term-binary-file).

    If the value has (or contains an object that has) an unsupported type, a
    [`ValueError`](exceptions.html#ValueError "ValueError") exception is raised — but garbage data will also be written
    to the file. The object will not be properly read back by [`load()`](#marshal.load "marshal.load").
    [Code objects](../reference/datamodel.html#code-objects) are only supported if *allow\_code* is true.

    The *version* argument indicates the data format that `dump` should use
    (see below).

    Raises an [auditing event](sys.html#auditing) `marshal.dumps` with arguments `value`, `version`.

    Changed in version 3.13: Added the *allow\_code* parameter.

marshal.load(*file*, */*, *\**, *allow\_code=True*)[¶](#marshal.load "Link to this definition")
:   Read one value from the open file and return it. If no valid value is read
    (e.g. because the data has a different Python version’s incompatible marshal
    format), raise [`EOFError`](exceptions.html#EOFError "EOFError"), [`ValueError`](exceptions.html#ValueError "ValueError") or [`TypeError`](exceptions.html#TypeError "TypeError").
    [Code objects](../reference/datamodel.html#code-objects) are only supported if *allow\_code* is true.
    The file must be a readable [binary file](../glossary.html#term-binary-file).

    Raises an [auditing event](sys.html#auditing) `marshal.load` with no arguments.

    Note

    If an object containing an unsupported type was marshalled with [`dump()`](#marshal.dump "marshal.dump"),
    [`load()`](#marshal.load "marshal.load") will substitute `None` for the unmarshallable type.

    Changed in version 3.10: This call used to raise a `code.__new__` audit event for each code object. Now
    it raises a single `marshal.load` event for the entire load operation.

    Changed in version 3.13: Added the *allow\_code* parameter.

marshal.dumps(*value*, *version=version*, */*, *\**, *allow\_code=True*)[¶](#marshal.dumps "Link to this definition")
:   Return the bytes object that would be written to a file by `dump(value, file)`. The
    value must be a supported type. Raise a [`ValueError`](exceptions.html#ValueError "ValueError") exception if value
    has (or contains an object that has) an unsupported type.
    [Code objects](../reference/datamodel.html#code-objects) are only supported if *allow\_code* is true.

    The *version* argument indicates the data format that `dumps` should use
    (see below).

    Raises an [auditing event](sys.html#auditing) `marshal.dumps` with arguments `value`, `version`.

    Changed in version 3.13: Added the *allow\_code* parameter.

marshal.loads(*bytes*, */*, *\**, *allow\_code=True*)[¶](#marshal.loads "Link to this definition")
:   Convert the [bytes-like object](../glossary.html#term-bytes-like-object) to a value. If no valid value is found, raise
    [`EOFError`](exceptions.html#EOFError "EOFError"), [`ValueError`](exceptions.html#ValueError "ValueError") or [`TypeError`](exceptions.html#TypeError "TypeError").
    [Code objects](../reference/datamodel.html#code-objects) are only supported if *allow\_code* is true.
    Extra bytes in the input are ignored.

    Raises an [auditing event](sys.html#auditing) `marshal.loads` with argument `bytes`.

    Changed in version 3.10: This call used to raise a `code.__new__` audit event for each code object. Now
    it raises a single `marshal.loads` event for the entire load operation.

    Changed in version 3.13: Added the *allow\_code* parameter.

In addition, the following constants are defined:

marshal.version[¶](#marshal.version "Link to this definition")
:   Indicates the format that the module uses.
    Version 0 is the historical first version; subsequent versions
    add new features.
    Generally, a new version becomes the default when it is introduced.

    | Version | Available since | New features |
    | --- | --- | --- |
    | 1 | Python 2.4 | Sharing interned strings |
    | 2 | Python 2.5 | Binary representation of floats |
    | 3 | Python 3.4 | Support for object instancing and recursion |
    | 4 | Python 3.4 | Efficient representation of short strings |
    | 5 | Python 3.14 | Support for [`slice`](functions.html#slice "slice") objects |

Footnotes

[[1](#id1)]

The name of this module stems from a bit of terminology used by the designers of
Modula-3 (amongst others), who use the term “marshalling” for shipping of data
around in a self-contained form. Strictly speaking, “to marshal” means to
convert some data from internal to external form (in an RPC buffer for instance)
and “unmarshalling” for the reverse process.

#### Previous topic

[`shelve` — Python object persistence](shelve.html "previous chapter")

#### Next topic

[`dbm` — Interfaces to Unix “databases”](dbm.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/marshal.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](dbm.html "dbm — Interfaces to Unix “databases”") |
* [previous](shelve.html "shelve — Python object persistence") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Persistence](persistence.html) »
* `marshal` — Internal Python object serialization
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
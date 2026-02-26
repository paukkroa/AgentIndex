### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](pickle.html "pickle — Python object serialization") |
* [previous](shutil.html "shutil — High-level file operations") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Data Persistence
* |
* Theme
  Auto
  Light
  Dark
   |

# Data Persistence[¶](#data-persistence "Link to this heading")

The modules described in this chapter support storing Python data in a
persistent form on disk. The [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") and [`marshal`](marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).") modules can turn
many Python data types into a stream of bytes and then recreate the objects from
the bytes. The various DBM-related modules support a family of hash-based file
formats that store a mapping of strings to other strings.

The list of modules described in this chapter is:

* [`pickle` — Python object serialization](pickle.html)
  + [Relationship to other Python modules](pickle.html#relationship-to-other-python-modules)
    - [Comparison with `marshal`](pickle.html#comparison-with-marshal)
    - [Comparison with `json`](pickle.html#comparison-with-json)
  + [Data stream format](pickle.html#data-stream-format)
  + [Module Interface](pickle.html#module-interface)
  + [What can be pickled and unpickled?](pickle.html#what-can-be-pickled-and-unpickled)
  + [Pickling Class Instances](pickle.html#pickling-class-instances)
    - [Persistence of External Objects](pickle.html#persistence-of-external-objects)
    - [Dispatch Tables](pickle.html#dispatch-tables)
    - [Handling Stateful Objects](pickle.html#handling-stateful-objects)
  + [Custom Reduction for Types, Functions, and Other Objects](pickle.html#custom-reduction-for-types-functions-and-other-objects)
  + [Out-of-band Buffers](pickle.html#out-of-band-buffers)
    - [Provider API](pickle.html#provider-api)
    - [Consumer API](pickle.html#consumer-api)
    - [Example](pickle.html#example)
  + [Restricting Globals](pickle.html#restricting-globals)
  + [Performance](pickle.html#performance)
  + [Examples](pickle.html#examples)
  + [Command-line interface](pickle.html#command-line-interface)
* [`copyreg` — Register `pickle` support functions](copyreg.html)
  + [Example](copyreg.html#example)
* [`shelve` — Python object persistence](shelve.html)
  + [Restrictions](shelve.html#restrictions)
  + [Example](shelve.html#example)
* [`marshal` — Internal Python object serialization](marshal.html)
* [`dbm` — Interfaces to Unix “databases”](dbm.html)
  + [`dbm.sqlite3` — SQLite backend for dbm](dbm.html#module-dbm.sqlite3)
  + [`dbm.gnu` — GNU database manager](dbm.html#module-dbm.gnu)
  + [`dbm.ndbm` — New Database Manager](dbm.html#module-dbm.ndbm)
  + [`dbm.dumb` — Portable DBM implementation](dbm.html#module-dbm.dumb)
* [`sqlite3` — DB-API 2.0 interface for SQLite databases](sqlite3.html)
  + [Tutorial](sqlite3.html#tutorial)
  + [Reference](sqlite3.html#reference)
    - [Module functions](sqlite3.html#module-functions)
    - [Module constants](sqlite3.html#module-constants)
    - [Connection objects](sqlite3.html#connection-objects)
    - [Cursor objects](sqlite3.html#cursor-objects)
    - [Row objects](sqlite3.html#row-objects)
    - [Blob objects](sqlite3.html#blob-objects)
    - [PrepareProtocol objects](sqlite3.html#prepareprotocol-objects)
    - [Exceptions](sqlite3.html#exceptions)
    - [SQLite and Python types](sqlite3.html#sqlite-and-python-types)
    - [Default adapters and converters (deprecated)](sqlite3.html#default-adapters-and-converters-deprecated)
    - [Command-line interface](sqlite3.html#command-line-interface)
  + [How-to guides](sqlite3.html#how-to-guides)
    - [How to use placeholders to bind values in SQL queries](sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)
    - [How to adapt custom Python types to SQLite values](sqlite3.html#how-to-adapt-custom-python-types-to-sqlite-values)
      * [How to write adaptable objects](sqlite3.html#how-to-write-adaptable-objects)
      * [How to register adapter callables](sqlite3.html#how-to-register-adapter-callables)
    - [How to convert SQLite values to custom Python types](sqlite3.html#how-to-convert-sqlite-values-to-custom-python-types)
    - [Adapter and converter recipes](sqlite3.html#adapter-and-converter-recipes)
    - [How to use connection shortcut methods](sqlite3.html#how-to-use-connection-shortcut-methods)
    - [How to use the connection context manager](sqlite3.html#how-to-use-the-connection-context-manager)
    - [How to work with SQLite URIs](sqlite3.html#how-to-work-with-sqlite-uris)
    - [How to create and use row factories](sqlite3.html#how-to-create-and-use-row-factories)
    - [How to handle non-UTF-8 text encodings](sqlite3.html#how-to-handle-non-utf-8-text-encodings)
  + [Explanation](sqlite3.html#explanation)
    - [Transaction control](sqlite3.html#transaction-control)
      * [Transaction control via the `autocommit` attribute](sqlite3.html#transaction-control-via-the-autocommit-attribute)
      * [Transaction control via the `isolation_level` attribute](sqlite3.html#transaction-control-via-the-isolation-level-attribute)

#### Previous topic

[`shutil` — High-level file operations](shutil.html "previous chapter")

#### Next topic

[`pickle` — Python object serialization](pickle.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/persistence.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](pickle.html "pickle — Python object serialization") |
* [previous](shutil.html "shutil — High-level file operations") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Data Persistence
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
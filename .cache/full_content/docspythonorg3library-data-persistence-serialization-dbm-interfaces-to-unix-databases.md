### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](sqlite3.html "sqlite3 — DB-API 2.0 interface for SQLite databases") |
* [previous](marshal.html "marshal — Internal Python object serialization") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Persistence](persistence.html) »
* `dbm` — Interfaces to Unix “databases”
* |
* Theme
  Auto
  Light
  Dark
   |

# `dbm` — Interfaces to Unix “databases”[¶](#module-dbm "Link to this heading")

**Source code:** [Lib/dbm/\_\_init\_\_.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/__init__.py)

---

`dbm` is a generic interface to variants of the DBM database:

* [`dbm.sqlite3`](#module-dbm.sqlite3 "dbm.sqlite3: SQLite backend for dbm")
* [`dbm.gnu`](#module-dbm.gnu "dbm.gnu: GNU database manager")
* [`dbm.ndbm`](#module-dbm.ndbm "dbm.ndbm: The New Database Manager")

If none of these modules are installed, the
slow-but-simple implementation in module [`dbm.dumb`](#module-dbm.dumb "dbm.dumb: Portable implementation of the simple DBM interface.") will be used. There
is a [third party interface](https://www.jcea.es/programacion/pybsddb.htm) to
the Oracle Berkeley DB.

*exception* dbm.error[¶](#dbm.error "Link to this definition")
:   A tuple containing the exceptions that can be raised by each of the supported
    modules, with a unique exception also named [`dbm.error`](#dbm.error "dbm.error") as the first
    item — the latter is used when [`dbm.error`](#dbm.error "dbm.error") is raised.

dbm.whichdb(*filename*)[¶](#dbm.whichdb "Link to this definition")
:   This function attempts to guess which of the several simple database modules
    available — [`dbm.sqlite3`](#module-dbm.sqlite3 "dbm.sqlite3: SQLite backend for dbm"), [`dbm.gnu`](#module-dbm.gnu "dbm.gnu: GNU database manager"), [`dbm.ndbm`](#module-dbm.ndbm "dbm.ndbm: The New Database Manager"),
    or [`dbm.dumb`](#module-dbm.dumb "dbm.dumb: Portable implementation of the simple DBM interface.") — should be used to open a given file.

    Return one of the following values:

    * `None` if the file can’t be opened because it’s unreadable or doesn’t exist
    * the empty string (`''`) if the file’s format can’t be guessed
    * a string containing the required module name, such as `'dbm.ndbm'` or `'dbm.gnu'`

    Changed in version 3.11: *filename* accepts a [path-like object](../glossary.html#term-path-like-object).

dbm.open(*file*, *flag='r'*, *mode=0o666*)[¶](#dbm.open "Link to this definition")
:   Open a database and return the corresponding database object.

    Parameters:
    :   * **file** ([path-like object](../glossary.html#term-path-like-object)) –

          The database file to open.

          If the database file already exists, the [`whichdb()`](#dbm.whichdb "dbm.whichdb") function is used to
          determine its type and the appropriate module is used; if it does not exist,
          the first submodule listed above that can be imported is used.
        * **flag** ([*str*](stdtypes.html#str "str")) –
          + `'r'` (default): Open existing database for reading only.
          + `'w'`: Open existing database for reading and writing.
          + `'c'`: Open database for reading and writing, creating it if it doesn’t exist.
          + `'n'`: Always create a new, empty database, open for reading and writing.
        * **mode** ([*int*](functions.html#int "int")) – The Unix file access mode of the file (default: octal `0o666`),
          used only when the database has to be created.

    Changed in version 3.11: *file* accepts a [path-like object](../glossary.html#term-path-like-object).

The object returned by [`open()`](#dbm.open "dbm.open") supports the basic
functionality of mutable [mappings](../glossary.html#term-mapping);
keys and their corresponding values can be stored, retrieved, and
deleted, and iteration, the [`in`](../reference/expressions.html#in) operator and methods `keys()`,
`get()`, `setdefault()` and `clear()` are available.
The `keys()` method returns a list instead of a view object.
The `setdefault()` method requires two arguments.

Key and values are always stored as [`bytes`](stdtypes.html#bytes "bytes"). This means that when
strings are used they are implicitly converted to the default encoding before
being stored.

These objects also support being used in a [`with`](../reference/compound_stmts.html#with) statement, which
will automatically close them when done.

Changed in version 3.2: `get()` and `setdefault()` methods are now available for all
`dbm` backends.

Changed in version 3.4: Added native support for the context management protocol to the objects
returned by [`open()`](#dbm.open "dbm.open").

Changed in version 3.8: Deleting a key from a read-only database raises a database module specific exception
instead of [`KeyError`](exceptions.html#KeyError "KeyError").

Changed in version 3.13: `clear()` methods are now available for all `dbm` backends.

The following example records some hostnames and a corresponding title, and
then prints out the contents of the database:

```
import dbm

# Open database, creating it if necessary.
with dbm.open('cache', 'c') as db:

    # Record some values
    db[b'hello'] = b'there'
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'

    # Note that the keys are considered bytes now.
    assert db[b'www.python.org'] == b'Python Website'
    # Notice how the value is now in bytes.
    assert db['www.cnn.com'] == b'Cable News Network'

    # Often-used methods of the dict interface work too.
    print(db.get('python.org', b'not present'))

    # Storing a non-string key or value will raise an exception (most
    # likely a TypeError).
    db['www.yahoo.com'] = 4

# db is automatically closed when leaving the with statement.
```

See also

Module [`shelve`](shelve.html#module-shelve "shelve: Python object persistence.")
:   Persistence module which stores non-string data.

The individual submodules are described in the following sections.

## `dbm.sqlite3` — SQLite backend for dbm[¶](#module-dbm.sqlite3 "Link to this heading")

Added in version 3.13.

**Source code:** [Lib/dbm/sqlite3.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/sqlite3.py)

---

This module uses the standard library [`sqlite3`](sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.") module to provide an
SQLite backend for the `dbm` module.
The files created by `dbm.sqlite3` can thus be opened by [`sqlite3`](sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x."),
or any other SQLite browser, including the SQLite CLI.

[Availability](intro.html#availability): not WASI.

This module does not work or is not available on WebAssembly. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

dbm.sqlite3.open(*filename*, */*, *flag='r'*, *mode=0o666*)[¶](#dbm.sqlite3.open "Link to this definition")
:   Open an SQLite database.

    Parameters:
    :   * **filename** ([path-like object](../glossary.html#term-path-like-object)) – The path to the database to be opened.
        * **flag** ([*str*](stdtypes.html#str "str")) –
          + `'r'` (default): Open existing database for reading only.
          + `'w'`: Open existing database for reading and writing.
          + `'c'`: Open database for reading and writing, creating it if it doesn’t exist.
          + `'n'`: Always create a new, empty database, open for reading and writing.
        * **mode** – The Unix file access mode of the file (default: octal `0o666`),
          used only when the database has to be created.

    The returned database object behaves similar to a mutable [mapping](../glossary.html#term-mapping),
    but the `keys()` method returns a list, and
    the `setdefault()` method requires two arguments.
    It also supports a “closing” context manager via the [`with`](../reference/compound_stmts.html#with) keyword.

    The following method is also provided:

    sqlite3.close()[¶](#dbm.sqlite3.sqlite3.close "Link to this definition")
    :   Close the SQLite database.

## `dbm.gnu` — GNU database manager[¶](#module-dbm.gnu "Link to this heading")

**Source code:** [Lib/dbm/gnu.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/gnu.py)

---

The `dbm.gnu` module provides an interface to the GDBM
library, similar to the [`dbm.ndbm`](#module-dbm.ndbm "dbm.ndbm: The New Database Manager") module, but with additional
functionality like crash tolerance.

Note

The file formats created by `dbm.gnu` and [`dbm.ndbm`](#module-dbm.ndbm "dbm.ndbm: The New Database Manager") are incompatible
and can not be used interchangeably.

[Availability](intro.html#availability): not Android, not iOS, not WASI.

This module is not supported on [mobile platforms](intro.html#mobile-availability)
or [WebAssembly platforms](intro.html#wasm-availability).

[Availability](intro.html#availability): Unix.

*exception* dbm.gnu.error[¶](#dbm.gnu.error "Link to this definition")
:   Raised on `dbm.gnu`-specific errors, such as I/O errors. [`KeyError`](exceptions.html#KeyError "KeyError") is
    raised for general mapping errors like specifying an incorrect key.

dbm.gnu.open\_flags[¶](#dbm.gnu.open_flags "Link to this definition")
:   A string of characters the *flag* parameter of [`open()`](#dbm.gnu.open "dbm.gnu.open") supports.

dbm.gnu.open(*filename*, *flag='r'*, *mode=0o666*, */*)[¶](#dbm.gnu.open "Link to this definition")
:   Open a GDBM database and return a `gdbm` object.

    Parameters:
    :   * **filename** ([path-like object](../glossary.html#term-path-like-object)) – The database file to open.
        * **flag** ([*str*](stdtypes.html#str "str")) –
          + `'r'` (default): Open existing database for reading only.
          + `'w'`: Open existing database for reading and writing.
          + `'c'`: Open database for reading and writing, creating it if it doesn’t exist.
          + `'n'`: Always create a new, empty database, open for reading and writing.

          The following additional characters may be appended
          to control how the database is opened:

          + `'f'`: Open the database in fast mode.
            Writes to the database will not be synchronized.
          + `'s'`: Synchronized mode.
            Changes to the database will be written immediately to the file.
          + `'u'`: Do not lock database.

          Not all flags are valid for all versions of GDBM.
          See the [`open_flags`](#dbm.gnu.open_flags "dbm.gnu.open_flags") member for a list of supported flag characters.
        * **mode** ([*int*](functions.html#int "int")) – The Unix file access mode of the file (default: octal `0o666`),
          used only when the database has to be created.

    Raises:
    :   [**error**](#dbm.gnu.error "dbm.gnu.error") – If an invalid *flag* argument is passed.

    Changed in version 3.11: *filename* accepts a [path-like object](../glossary.html#term-path-like-object).

    `gdbm` objects behave similar to mutable [mappings](../glossary.html#term-mapping),
    but methods `items()`, `values()`, `pop()`, `popitem()`,
    and `update()` are not supported,
    the `keys()` method returns a list, and
    the `setdefault()` method requires two arguments.
    It also supports a “closing” context manager via the [`with`](../reference/compound_stmts.html#with) keyword.

    Changed in version 3.2: Added the `get()` and `setdefault()` methods.

    Changed in version 3.13: Added the `clear()` method.

    The following methods are also provided:

    gdbm.close()[¶](#dbm.gnu.gdbm.close "Link to this definition")
    :   Close the GDBM database.

    gdbm.firstkey()[¶](#dbm.gnu.gdbm.firstkey "Link to this definition")
    :   It’s possible to loop over every key in the database using this method and the
        [`nextkey()`](#dbm.gnu.gdbm.nextkey "dbm.gnu.gdbm.nextkey") method. The traversal is ordered by GDBM’s internal
        hash values, and won’t be sorted by the key values. This method returns
        the starting key.

    gdbm.nextkey(*key*)[¶](#dbm.gnu.gdbm.nextkey "Link to this definition")
    :   Returns the key that follows *key* in the traversal. The following code prints
        every key in the database `db`, without having to create a list in memory that
        contains them all:

        ```
        k = db.firstkey()
        while k is not None:
            print(k)
            k = db.nextkey(k)
        ```

    gdbm.reorganize()[¶](#dbm.gnu.gdbm.reorganize "Link to this definition")
    :   If you have carried out a lot of deletions and would like to shrink the space
        used by the GDBM file, this routine will reorganize the database. `gdbm`
        objects will not shorten the length of a database file except by using this
        reorganization; otherwise, deleted file space will be kept and reused as new
        (key, value) pairs are added.

    gdbm.sync()[¶](#dbm.gnu.gdbm.sync "Link to this definition")
    :   When the database has been opened in fast mode, this method forces any
        unwritten data to be written to the disk.

## `dbm.ndbm` — New Database Manager[¶](#module-dbm.ndbm "Link to this heading")

**Source code:** [Lib/dbm/ndbm.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/ndbm.py)

---

The `dbm.ndbm` module provides an interface to the
NDBM library.
This module can be used with the “classic” NDBM interface or the
GDBM compatibility interface.

Note

The file formats created by [`dbm.gnu`](#module-dbm.gnu "dbm.gnu: GNU database manager") and `dbm.ndbm` are incompatible
and can not be used interchangeably.

Warning

The NDBM library shipped as part of macOS has an undocumented limitation on the
size of values, which can result in corrupted database files
when storing values larger than this limit. Reading such corrupted files can
result in a hard crash (segmentation fault).

[Availability](intro.html#availability): not Android, not iOS, not WASI.

This module is not supported on [mobile platforms](intro.html#mobile-availability)
or [WebAssembly platforms](intro.html#wasm-availability).

[Availability](intro.html#availability): Unix.

*exception* dbm.ndbm.error[¶](#dbm.ndbm.error "Link to this definition")
:   Raised on `dbm.ndbm`-specific errors, such as I/O errors. [`KeyError`](exceptions.html#KeyError "KeyError") is raised
    for general mapping errors like specifying an incorrect key.

dbm.ndbm.library[¶](#dbm.ndbm.library "Link to this definition")
:   Name of the NDBM implementation library used.

dbm.ndbm.open(*filename*, *flag='r'*, *mode=0o666*, */*)[¶](#dbm.ndbm.open "Link to this definition")
:   Open an NDBM database and return an `ndbm` object.

    Parameters:
    :   * **filename** ([path-like object](../glossary.html#term-path-like-object)) – The basename of the database file
          (without the `.dir` or `.pag` extensions).
        * **flag** ([*str*](stdtypes.html#str "str")) –
          + `'r'` (default): Open existing database for reading only.
          + `'w'`: Open existing database for reading and writing.
          + `'c'`: Open database for reading and writing, creating it if it doesn’t exist.
          + `'n'`: Always create a new, empty database, open for reading and writing.
        * **mode** ([*int*](functions.html#int "int")) – The Unix file access mode of the file (default: octal `0o666`),
          used only when the database has to be created.

    Changed in version 3.11: Accepts [path-like object](../glossary.html#term-path-like-object) for filename.

    `ndbm` objects behave similar to mutable [mappings](../glossary.html#term-mapping),
    but methods `items()`, `values()`, `pop()`, `popitem()`,
    and `update()` are not supported,
    the `keys()` method returns a list, and
    the `setdefault()` method requires two arguments.
    It also supports a “closing” context manager via the [`with`](../reference/compound_stmts.html#with) keyword.

    Changed in version 3.2: Added the `get()` and `setdefault()` methods.

    Changed in version 3.13: Added the `clear()` method.

    The following method is also provided:

    ndbm.close()[¶](#dbm.ndbm.ndbm.close "Link to this definition")
    :   Close the NDBM database.

## `dbm.dumb` — Portable DBM implementation[¶](#module-dbm.dumb "Link to this heading")

**Source code:** [Lib/dbm/dumb.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/dumb.py)

Note

The `dbm.dumb` module is intended as a last resort fallback for the
`dbm` module when a more robust module is not available. The `dbm.dumb`
module is not written for speed and is not nearly as heavily used as the other
database modules.

---

The `dbm.dumb` module provides a persistent [`dict`](stdtypes.html#dict "dict")-like
interface which is written entirely in Python.
Unlike other `dbm` backends, such as [`dbm.gnu`](#module-dbm.gnu "dbm.gnu: GNU database manager"), no
external library is required.

The `dbm.dumb` module defines the following:

*exception* dbm.dumb.error[¶](#dbm.dumb.error "Link to this definition")
:   Raised on `dbm.dumb`-specific errors, such as I/O errors. [`KeyError`](exceptions.html#KeyError "KeyError") is
    raised for general mapping errors like specifying an incorrect key.

dbm.dumb.open(*filename*, *flag='c'*, *mode=0o666*)[¶](#dbm.dumb.open "Link to this definition")
:   Open a `dbm.dumb` database.

    Parameters:
    :   * **filename** –

          The basename of the database file (without extensions).
          A new database creates the following files:

          + `filename.dat`
          + `filename.dir`
        * **flag** ([*str*](stdtypes.html#str "str")) –
          + `'r'`: Open existing database for reading only.
          + `'w'`: Open existing database for reading and writing.
          + `'c'` (default): Open database for reading and writing, creating it if it doesn’t exist.
          + `'n'`: Always create a new, empty database, open for reading and writing.
        * **mode** ([*int*](functions.html#int "int")) – The Unix file access mode of the file (default: octal `0o666`),
          used only when the database has to be created.

    Warning

    It is possible to crash the Python interpreter when loading a database
    with a sufficiently large/complex entry due to stack depth limitations in
    Python’s AST compiler.

    Changed in version 3.5: [`open()`](#dbm.dumb.open "dbm.dumb.open") always creates a new database when *flag* is `'n'`.

    Changed in version 3.8: A database opened read-only if *flag* is `'r'`.
    A database is not created if it does not exist if *flag* is `'r'` or `'w'`.

    Changed in version 3.11: *filename* accepts a [path-like object](../glossary.html#term-path-like-object).

    The returned database object behaves similar to a mutable [mapping](../glossary.html#term-mapping),
    but the `keys()` and `items()` methods return lists, and
    the `setdefault()` method requires two arguments.
    It also supports a “closing” context manager via the [`with`](../reference/compound_stmts.html#with) keyword.

    The following methods are also provided:

    dumbdbm.close()[¶](#dbm.dumb.dumbdbm.close "Link to this definition")
    :   Close the database.

    dumbdbm.sync()[¶](#dbm.dumb.dumbdbm.sync "Link to this definition")
    :   Synchronize the on-disk directory and data files. This method is called
        by the [`shelve.Shelf.sync()`](shelve.html#shelve.Shelf.sync "shelve.Shelf.sync") method.

### [Table of Contents](../contents.html)

* [`dbm` — Interfaces to Unix “databases”](#)
  + [`dbm.sqlite3` — SQLite backend for dbm](#module-dbm.sqlite3)
  + [`dbm.gnu` — GNU database manager](#module-dbm.gnu)
  + [`dbm.ndbm` — New Database Manager](#module-dbm.ndbm)
  + [`dbm.dumb` — Portable DBM implementation](#module-dbm.dumb)

#### Previous topic

[`marshal` — Internal Python object serialization](marshal.html "previous chapter")

#### Next topic

[`sqlite3` — DB-API 2.0 interface for SQLite databases](sqlite3.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/dbm.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](sqlite3.html "sqlite3 — DB-API 2.0 interface for SQLite databases") |
* [previous](marshal.html "marshal — Internal Python object serialization") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Persistence](persistence.html) »
* `dbm` — Interfaces to Unix “databases”
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
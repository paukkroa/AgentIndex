### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](marshal.html "marshal — Internal Python object serialization") |
* [previous](copyreg.html "copyreg — Register pickle support functions") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Persistence](persistence.html) »
* `shelve` — Python object persistence
* |
* Theme
  Auto
  Light
  Dark
   |

# `shelve` — Python object persistence[¶](#module-shelve "Link to this heading")

**Source code:** [Lib/shelve.py](https://github.com/python/cpython/tree/3.14/Lib/shelve.py)

---

A “shelf” is a persistent, dictionary-like object. The difference with “dbm”
databases is that the values (not the keys!) in a shelf can be essentially
arbitrary Python objects — anything that the [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") module can handle.
This includes most class instances, recursive data types, and objects containing
lots of shared sub-objects. The keys are ordinary strings.

shelve.open(*filename*, *flag='c'*, *protocol=None*, *writeback=False*)[¶](#shelve.open "Link to this definition")
:   Open a persistent dictionary. The filename specified is the base filename for
    the underlying database. As a side-effect, an extension may be added to the
    filename and more than one file may be created. By default, the underlying
    database file is opened for reading and writing. The optional *flag* parameter
    has the same interpretation as the *flag* parameter of [`dbm.open()`](dbm.html#dbm.open "dbm.open").

    By default, pickles created with [`pickle.DEFAULT_PROTOCOL`](pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") are used
    to serialize values. The version of the pickle protocol can be specified
    with the *protocol* parameter.

    Because of Python semantics, a shelf cannot know when a mutable
    persistent-dictionary entry is modified. By default modified objects are
    written *only* when assigned to the shelf (see [Example](#shelve-example)). If the
    optional *writeback* parameter is set to `True`, all entries accessed are also
    cached in memory, and written back on [`sync()`](#shelve.Shelf.sync "shelve.Shelf.sync") and
    [`close()`](#shelve.Shelf.close "shelve.Shelf.close"); this can make it handier to mutate mutable entries in
    the persistent dictionary, but, if many entries are accessed, it can consume
    vast amounts of memory for the cache, and it can make the close operation
    very slow since all accessed entries are written back (there is no way to
    determine which accessed entries are mutable, nor which ones were actually
    mutated).

    Changed in version 3.10: [`pickle.DEFAULT_PROTOCOL`](pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") is now used as the default pickle
    protocol.

    Changed in version 3.11: Accepts [path-like object](../glossary.html#term-path-like-object) for filename.

    Note

    Do not rely on the shelf being closed automatically; always call
    [`close()`](#shelve.Shelf.close "shelve.Shelf.close") explicitly when you don’t need it any more, or
    use [`shelve.open()`](#shelve.open "shelve.open") as a context manager:

    ```
    with shelve.open('spam') as db:
        db['eggs'] = 'eggs'
    ```

Warning

Because the `shelve` module is backed by [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back."), it is insecure
to load a shelf from an untrusted source. Like with pickle, loading a shelf
can execute arbitrary code.

Shelf objects support most of the methods and operations supported by dictionaries
(except copying, constructors and operators `|` and `|=`). This eases the
transition from dictionary based scripts to those requiring persistent storage.

Two additional methods are supported:

Shelf.sync()[¶](#shelve.Shelf.sync "Link to this definition")
:   Write back all entries in the cache if the shelf was opened with *writeback*
    set to [`True`](constants.html#True "True"). Also empty the cache and synchronize the persistent
    dictionary on disk, if feasible. This is called automatically when the shelf
    is closed with [`close()`](#shelve.Shelf.close "shelve.Shelf.close").

Shelf.close()[¶](#shelve.Shelf.close "Link to this definition")
:   Synchronize and close the persistent *dict* object. Operations on a closed
    shelf will fail with a [`ValueError`](exceptions.html#ValueError "ValueError").

See also

[Persistent dictionary recipe](https://code.activestate.com/recipes/576642-persistent-dict-with-multiple-standard-file-format/)
with widely supported storage formats and having the speed of native
dictionaries.

## Restrictions[¶](#restrictions "Link to this heading")

* The choice of which database package will be used (such as [`dbm.ndbm`](dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager") or
  [`dbm.gnu`](dbm.html#module-dbm.gnu "dbm.gnu: GNU database manager")) depends on which interface is available. Therefore it is not
  safe to open the database directly using [`dbm`](dbm.html#module-dbm "dbm: Interfaces to various Unix \"database\" formats."). The database is also
  (unfortunately) subject to the limitations of [`dbm`](dbm.html#module-dbm "dbm: Interfaces to various Unix \"database\" formats."), if it is used —
  this means that (the pickled representation of) the objects stored in the
  database should be fairly small, and in rare cases key collisions may cause
  the database to refuse updates.
* The `shelve` module does not support *concurrent* read/write access to
  shelved objects. (Multiple simultaneous read accesses are safe.) When a
  program has a shelf open for writing, no other program should have it open for
  reading or writing. Unix file locking can be used to solve this, but this
  differs across Unix versions and requires knowledge about the database
  implementation used.
* On macOS [`dbm.ndbm`](dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager") can silently corrupt the database file on updates,
  which can cause hard crashes when trying to read from the database.

*class* shelve.Shelf(*dict*, *protocol=None*, *writeback=False*, *keyencoding='utf-8'*)[¶](#shelve.Shelf "Link to this definition")
:   A subclass of [`collections.abc.MutableMapping`](collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping") which stores pickled
    values in the *dict* object.

    By default, pickles created with [`pickle.DEFAULT_PROTOCOL`](pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") are used
    to serialize values. The version of the pickle protocol can be specified
    with the *protocol* parameter. See the [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") documentation for a
    discussion of the pickle protocols.

    If the *writeback* parameter is `True`, the object will hold a cache of all
    entries accessed and write them back to the *dict* at sync and close times.
    This allows natural operations on mutable entries, but can consume much more
    memory and make sync and close take a long time.

    The *keyencoding* parameter is the encoding used to encode keys before they
    are used with the underlying dict.

    A [`Shelf`](#shelve.Shelf "shelve.Shelf") object can also be used as a context manager, in which
    case it will be automatically closed when the [`with`](../reference/compound_stmts.html#with) block ends.

    Changed in version 3.2: Added the *keyencoding* parameter; previously, keys were always encoded in
    UTF-8.

    Changed in version 3.4: Added context manager support.

    Changed in version 3.10: [`pickle.DEFAULT_PROTOCOL`](pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") is now used as the default pickle
    protocol.

*class* shelve.BsdDbShelf(*dict*, *protocol=None*, *writeback=False*, *keyencoding='utf-8'*)[¶](#shelve.BsdDbShelf "Link to this definition")
:   A subclass of [`Shelf`](#shelve.Shelf "shelve.Shelf") which exposes `first()`, `next()`,
    `previous()`, `last()` and `set_location()` methods.
    These are available
    in the third-party `bsddb` module from [pybsddb](https://www.jcea.es/programacion/pybsddb.htm) but not in other database
    modules. The *dict* object passed to the constructor must support those
    methods. This is generally accomplished by calling one of
    `bsddb.hashopen()`, `bsddb.btopen()` or `bsddb.rnopen()`. The
    optional *protocol*, *writeback*, and *keyencoding* parameters have the same
    interpretation as for the [`Shelf`](#shelve.Shelf "shelve.Shelf") class.

*class* shelve.DbfilenameShelf(*filename*, *flag='c'*, *protocol=None*, *writeback=False*)[¶](#shelve.DbfilenameShelf "Link to this definition")
:   A subclass of [`Shelf`](#shelve.Shelf "shelve.Shelf") which accepts a *filename* instead of a dict-like
    object. The underlying file will be opened using [`dbm.open()`](dbm.html#dbm.open "dbm.open"). By
    default, the file will be created and opened for both read and write. The
    optional *flag* parameter has the same interpretation as for the [`open()`](#shelve.open "shelve.open")
    function. The optional *protocol* and *writeback* parameters have the same
    interpretation as for the [`Shelf`](#shelve.Shelf "shelve.Shelf") class.

## Example[¶](#example "Link to this heading")

To summarize the interface (`key` is a string, `data` is an arbitrary
object):

```
import shelve

d = shelve.open(filename)  # open -- file may get suffix added by low-level
                           # library

d[key] = data              # store data at key (overwrites old data if
                           # using an existing key)
data = d[key]              # retrieve a COPY of data at key (raise KeyError
                           # if no such key)
del d[key]                 # delete data stored at key (raises KeyError
                           # if no such key)

flag = key in d            # true if the key exists
klist = list(d.keys())     # a list of all existing keys (slow!)

# as d was opened WITHOUT writeback=True, beware:
d['xx'] = [0, 1, 2]        # this works as expected, but...
d['xx'].append(3)          # *this doesn't!* -- d['xx'] is STILL [0, 1, 2]!

# having opened d without writeback=True, you need to code carefully:
temp = d['xx']             # extracts the copy
temp.append(5)             # mutates the copy
d['xx'] = temp             # stores the copy right back, to persist it

# or, d=shelve.open(filename,writeback=True) would let you just code
# d['xx'].append(5) and have it work as expected, BUT it would also
# consume more memory and make the d.close() operation slower.

d.close()                  # close it
```

See also

Module [`dbm`](dbm.html#module-dbm "dbm: Interfaces to various Unix \"database\" formats.")
:   Generic interface to `dbm`-style databases.

Module [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
:   Object serialization used by `shelve`.

### [Table of Contents](../contents.html)

* [`shelve` — Python object persistence](#)
  + [Restrictions](#restrictions)
  + [Example](#example)

#### Previous topic

[`copyreg` — Register `pickle` support functions](copyreg.html "previous chapter")

#### Next topic

[`marshal` — Internal Python object serialization](marshal.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/shelve.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](marshal.html "marshal — Internal Python object serialization") |
* [previous](copyreg.html "copyreg — Register pickle support functions") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Persistence](persistence.html) »
* `shelve` — Python object persistence
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
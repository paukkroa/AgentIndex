### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](shelve.html "shelve — Python object persistence") |
* [previous](pickle.html "pickle — Python object serialization") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Persistence](persistence.html) »
* `copyreg` — Register `pickle` support functions
* |
* Theme
  Auto
  Light
  Dark
   |

# `copyreg` — Register `pickle` support functions[¶](#module-copyreg "Link to this heading")

**Source code:** [Lib/copyreg.py](https://github.com/python/cpython/tree/3.14/Lib/copyreg.py)

---

The `copyreg` module offers a way to define functions used while pickling
specific objects. The [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") and [`copy`](copy.html#module-copy "copy: Shallow and deep copy operations.") modules use those functions
when pickling/copying those objects. The module provides configuration
information about object constructors which are not classes.
Such constructors may be factory functions or class instances.

copyreg.constructor(*object*)[¶](#copyreg.constructor "Link to this definition")
:   Declares *object* to be a valid constructor. If *object* is not callable (and
    hence not valid as a constructor), raises [`TypeError`](exceptions.html#TypeError "TypeError").

copyreg.pickle(*type*, *function*, *constructor\_ob=None*)[¶](#copyreg.pickle "Link to this definition")
:   Declares that *function* should be used as a “reduction” function for objects
    of type *type*. *function* must return either a string or a tuple
    containing between two and six elements. See the [`dispatch_table`](pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table")
    for more details on the interface of *function*.

    The *constructor\_ob* parameter is a legacy feature and is now ignored, but if
    passed it must be a callable.

    Note that the [`dispatch_table`](pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table") attribute of a pickler
    object or subclass of [`pickle.Pickler`](pickle.html#pickle.Pickler "pickle.Pickler") can also be used for
    declaring reduction functions.

## Example[¶](#example "Link to this heading")

The example below would like to show how to register a pickle function and how
it will be used:

```
>>> import copyreg, copy, pickle
>>> class C:
...     def __init__(self, a):
...         self.a = a
...
>>> def pickle_c(c):
...     print("pickling a C instance...")
...     return C, (c.a,)
...
>>> copyreg.pickle(C, pickle_c)
>>> c = C(1)
>>> d = copy.copy(c)
pickling a C instance...
>>> p = pickle.dumps(c)
pickling a C instance...
```

### [Table of Contents](../contents.html)

* [`copyreg` — Register `pickle` support functions](#)
  + [Example](#example)

#### Previous topic

[`pickle` — Python object serialization](pickle.html "previous chapter")

#### Next topic

[`shelve` — Python object persistence](shelve.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/copyreg.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](shelve.html "shelve — Python object persistence") |
* [previous](pickle.html "pickle — Python object serialization") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Persistence](persistence.html) »
* `copyreg` — Register `pickle` support functions
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
### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](pprint.html "pprint — Data pretty printer") |
* [previous](types.html "types — Dynamic type creation and names for built-in types") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Types](datatypes.html) »
* `copy` — Shallow and deep copy operations
* |
* Theme
  Auto
  Light
  Dark
   |

# `copy` — Shallow and deep copy operations[¶](#module-copy "Link to this heading")

**Source code:** [Lib/copy.py](https://github.com/python/cpython/tree/3.14/Lib/copy.py)

---

Assignment statements in Python do not copy objects, they create bindings
between a target and an object. For collections that are mutable or contain
mutable items, a copy is sometimes needed so one can change one copy without
changing the other. This module provides generic shallow and deep copy
operations (explained below).

Interface summary:

copy.copy(*obj*)[¶](#copy.copy "Link to this definition")
:   Return a shallow copy of *obj*.

copy.deepcopy(*obj*[, *memo*])[¶](#copy.deepcopy "Link to this definition")
:   Return a deep copy of *obj*.

copy.replace(*obj*, */*, *\*\*changes*)[¶](#copy.replace "Link to this definition")
:   Creates a new object of the same type as *obj*, replacing fields with values
    from *changes*.

    Added in version 3.13.

*exception* copy.Error[¶](#copy.Error "Link to this definition")
:   Raised for module specific errors.

The difference between shallow and deep copying is only relevant for compound
objects (objects that contain other objects, like lists or class instances):

* A *shallow copy* constructs a new compound object and then (to the extent
  possible) inserts *references* into it to the objects found in the original.
* A *deep copy* constructs a new compound object and then, recursively, inserts
  *copies* into it of the objects found in the original.

Two problems often exist with deep copy operations that don’t exist with shallow
copy operations:

* Recursive objects (compound objects that, directly or indirectly, contain a
  reference to themselves) may cause a recursive loop.
* Because deep copy copies everything it may copy too much, such as data
  which is intended to be shared between copies.

The [`deepcopy()`](#copy.deepcopy "copy.deepcopy") function avoids these problems by:

* keeping a `memo` dictionary of objects already copied during the current
  copying pass; and
* letting user-defined classes override the copying operation or the set of
  components copied.

This module does not copy types like module, method, stack trace, stack frame,
file, socket, window, or any similar types. It does “copy” functions and
classes (shallow and deeply), by returning the original object unchanged; this
is compatible with the way these are treated by the [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") module.

Shallow copies of dictionaries can be made using [`dict.copy()`](stdtypes.html#dict.copy "dict.copy"), and
of lists by assigning a slice of the entire list, for example,
`copied_list = original_list[:]`.

Classes can use the same interfaces to control copying that they use to control
pickling. See the description of module [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") for information on these
methods. In fact, the `copy` module uses the registered
pickle functions from the [`copyreg`](copyreg.html#module-copyreg "copyreg: Register pickle support functions.") module.

In order for a class to define its own copy implementation, it can define
special methods [`__copy__()`](#object.__copy__ "object.__copy__") and [`__deepcopy__()`](#object.__deepcopy__ "object.__deepcopy__").

object.\_\_copy\_\_(*self*)[¶](#object.__copy__ "Link to this definition")
:   Called to implement the shallow copy operation;
    no additional arguments are passed.

object.\_\_deepcopy\_\_(*self*, *memo*)[¶](#object.__deepcopy__ "Link to this definition")
:   Called to implement the deep copy operation; it is passed one
    argument, the *memo* dictionary. If the `__deepcopy__` implementation needs
    to make a deep copy of a component, it should call the [`deepcopy()`](#copy.deepcopy "copy.deepcopy") function
    with the component as first argument and the *memo* dictionary as second argument.
    The *memo* dictionary should be treated as an opaque object.

Function `copy.replace()` is more limited
than [`copy()`](#copy.copy "copy.copy") and [`deepcopy()`](#copy.deepcopy "copy.deepcopy"),
and only supports named tuples created by [`namedtuple()`](collections.html#collections.namedtuple "collections.namedtuple"),
[`dataclasses`](dataclasses.html#module-dataclasses "dataclasses: Generate special methods on user-defined classes."), and other classes which define method [`__replace__()`](#object.__replace__ "object.__replace__").

object.\_\_replace\_\_(*self*, */*, *\*\*changes*)[¶](#object.__replace__ "Link to this definition")
:   This method should create a new object of the same type,
    replacing fields with values from *changes*.

    Added in version 3.13.

See also

Module [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
:   Discussion of the special methods used to support object state retrieval and
    restoration.

#### Previous topic

[`types` — Dynamic type creation and names for built-in types](types.html "previous chapter")

#### Next topic

[`pprint` — Data pretty printer](pprint.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/copy.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](pprint.html "pprint — Data pretty printer") |
* [previous](types.html "types — Dynamic type creation and names for built-in types") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Types](datatypes.html) »
* `copy` — Shallow and deep copy operations
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
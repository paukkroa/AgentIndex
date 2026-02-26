### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](enum.html "enum — Support for enumerations") |
* [previous](pprint.html "pprint — Data pretty printer") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Types](datatypes.html) »
* `reprlib` — Alternate `repr()` implementation
* |
* Theme
  Auto
  Light
  Dark
   |

# `reprlib` — Alternate [`repr()`](functions.html#repr "repr") implementation[¶](#module-reprlib "Link to this heading")

**Source code:** [Lib/reprlib.py](https://github.com/python/cpython/tree/3.14/Lib/reprlib.py)

---

The `reprlib` module provides a means for producing object representations
with limits on the size of the resulting strings. This is used in the Python
debugger and may be useful in other contexts as well.

This module provides a class, an instance, and a function:

*class* reprlib.Repr(*\**, *maxlevel=6*, *maxtuple=6*, *maxlist=6*, *maxarray=5*, *maxdict=4*, *maxset=6*, *maxfrozenset=6*, *maxdeque=6*, *maxstring=30*, *maxlong=40*, *maxother=30*, *fillvalue='...'*, *indent=None*)[¶](#reprlib.Repr "Link to this definition")
:   Class which provides formatting services useful in implementing functions
    similar to the built-in [`repr()`](functions.html#repr "repr"); size limits for different object types
    are added to avoid the generation of representations which are excessively long.

    The keyword arguments of the constructor can be used as a shortcut to set the
    attributes of the [`Repr`](#reprlib.Repr "reprlib.Repr") instance. Which means that the following
    initialization:

    ```
    aRepr = reprlib.Repr(maxlevel=3)
    ```

    Is equivalent to:

    ```
    aRepr = reprlib.Repr()
    aRepr.maxlevel = 3
    ```

    See section [Repr Objects](#id1) for more information about [`Repr`](#reprlib.Repr "reprlib.Repr")
    attributes.

    Changed in version 3.12: Allow attributes to be set via keyword arguments.

reprlib.aRepr[¶](#reprlib.aRepr "Link to this definition")
:   This is an instance of [`Repr`](#reprlib.Repr "reprlib.Repr") which is used to provide the
    [`repr()`](#reprlib.repr "reprlib.repr") function described below. Changing the attributes of this
    object will affect the size limits used by [`repr()`](#reprlib.repr "reprlib.repr") and the Python
    debugger.

reprlib.repr(*obj*)[¶](#reprlib.repr "Link to this definition")
:   This is the [`repr()`](#reprlib.Repr.repr "reprlib.Repr.repr") method of `aRepr`. It returns a string
    similar to that returned by the built-in function of the same name, but with
    limits on most sizes.

In addition to size-limiting tools, the module also provides a decorator for
detecting recursive calls to [`__repr__()`](../reference/datamodel.html#object.__repr__ "object.__repr__") and substituting a
placeholder string instead.

@reprlib.recursive\_repr(*fillvalue='...'*)[¶](#reprlib.recursive_repr "Link to this definition")
:   Decorator for [`__repr__()`](../reference/datamodel.html#object.__repr__ "object.__repr__") methods to detect recursive calls within the
    same thread. If a recursive call is made, the *fillvalue* is returned,
    otherwise, the usual `__repr__()` call is made. For example:

    ```
    >>> from reprlib import recursive_repr
    >>> class MyList(list):
    ...     @recursive_repr()
    ...     def __repr__(self):
    ...         return '<' + '|'.join(map(repr, self)) + '>'
    ...
    >>> m = MyList('abc')
    >>> m.append(m)
    >>> m.append('x')
    >>> print(m)
    <'a'|'b'|'c'|...|'x'>
    ```

    Added in version 3.2.

## Repr Objects[¶](#repr-objects "Link to this heading")

[`Repr`](#reprlib.Repr "reprlib.Repr") instances provide several attributes which can be used to provide
size limits for the representations of different object types, and methods
which format specific object types.

Repr.fillvalue[¶](#reprlib.Repr.fillvalue "Link to this definition")
:   This string is displayed for recursive references. It defaults to
    `...`.

    Added in version 3.11.

Repr.maxlevel[¶](#reprlib.Repr.maxlevel "Link to this definition")
:   Depth limit on the creation of recursive representations. The default is `6`.

Repr.maxdict[¶](#reprlib.Repr.maxdict "Link to this definition")

Repr.maxlist[¶](#reprlib.Repr.maxlist "Link to this definition")

Repr.maxtuple[¶](#reprlib.Repr.maxtuple "Link to this definition")

Repr.maxset[¶](#reprlib.Repr.maxset "Link to this definition")

Repr.maxfrozenset[¶](#reprlib.Repr.maxfrozenset "Link to this definition")

Repr.maxdeque[¶](#reprlib.Repr.maxdeque "Link to this definition")

Repr.maxarray[¶](#reprlib.Repr.maxarray "Link to this definition")
:   Limits on the number of entries represented for the named object type. The
    default is `4` for [`maxdict`](#reprlib.Repr.maxdict "reprlib.Repr.maxdict"), `5` for [`maxarray`](#reprlib.Repr.maxarray "reprlib.Repr.maxarray"), and `6` for
    the others.

Repr.maxlong[¶](#reprlib.Repr.maxlong "Link to this definition")
:   Maximum number of characters in the representation for an integer. Digits
    are dropped from the middle. The default is `40`.

Repr.maxstring[¶](#reprlib.Repr.maxstring "Link to this definition")
:   Limit on the number of characters in the representation of the string. Note
    that the “normal” representation of the string is used as the character source:
    if escape sequences are needed in the representation, these may be mangled when
    the representation is shortened. The default is `30`.

Repr.maxother[¶](#reprlib.Repr.maxother "Link to this definition")
:   This limit is used to control the size of object types for which no specific
    formatting method is available on the [`Repr`](#reprlib.Repr "reprlib.Repr") object. It is applied in a
    similar manner as [`maxstring`](#reprlib.Repr.maxstring "reprlib.Repr.maxstring"). The default is `20`.

Repr.indent[¶](#reprlib.Repr.indent "Link to this definition")
:   If this attribute is set to `None` (the default), the output is formatted
    with no line breaks or indentation, like the standard [`repr()`](functions.html#repr "repr").
    For example:

    ```
    >>> example = [
    ...     1, 'spam', {'a': 2, 'b': 'spam eggs', 'c': {3: 4.5, 6: []}}, 'ham']
    >>> import reprlib
    >>> aRepr = reprlib.Repr()
    >>> print(aRepr.repr(example))
    [1, 'spam', {'a': 2, 'b': 'spam eggs', 'c': {3: 4.5, 6: []}}, 'ham']
    ```

    If [`indent`](#reprlib.Repr.indent "reprlib.Repr.indent") is set to a string, each recursion level
    is placed on its own line, indented by that string:

    ```
    >>> aRepr.indent = '-->'
    >>> print(aRepr.repr(example))
    [
    -->1,
    -->'spam',
    -->{
    -->-->'a': 2,
    -->-->'b': 'spam eggs',
    -->-->'c': {
    -->-->-->3: 4.5,
    -->-->-->6: [],
    -->-->},
    -->},
    -->'ham',
    ]
    ```

    Setting [`indent`](#reprlib.Repr.indent "reprlib.Repr.indent") to a positive integer value behaves as if it
    was set to a string with that number of spaces:

    ```
    >>> aRepr.indent = 4
    >>> print(aRepr.repr(example))
    [
        1,
        'spam',
        {
            'a': 2,
            'b': 'spam eggs',
            'c': {
                3: 4.5,
                6: [],
            },
        },
        'ham',
    ]
    ```

    Added in version 3.12.

Repr.repr(*obj*)[¶](#reprlib.Repr.repr "Link to this definition")
:   The equivalent to the built-in [`repr()`](functions.html#repr "repr") that uses the formatting imposed by
    the instance.

Repr.repr1(*obj*, *level*)[¶](#reprlib.Repr.repr1 "Link to this definition")
:   Recursive implementation used by [`repr()`](#reprlib.Repr.repr "reprlib.Repr.repr"). This uses the type of *obj* to
    determine which formatting method to call, passing it *obj* and *level*. The
    type-specific methods should call [`repr1()`](#reprlib.Repr.repr1 "reprlib.Repr.repr1") to perform recursive formatting,
    with `level - 1` for the value of *level* in the recursive call.

Repr.repr\_TYPE(*obj*, *level*)
:   Formatting methods for specific types are implemented as methods with a name
    based on the type name. In the method name, **TYPE** is replaced by
    `'_'.join(type(obj).__name__.split())`. Dispatch to these methods is
    handled by [`repr1()`](#reprlib.Repr.repr1 "reprlib.Repr.repr1"). Type-specific methods which need to recursively
    format a value should call `self.repr1(subobj, level - 1)`.

## Subclassing Repr Objects[¶](#subclassing-repr-objects "Link to this heading")

The use of dynamic dispatching by [`Repr.repr1()`](#reprlib.Repr.repr1 "reprlib.Repr.repr1") allows subclasses of
[`Repr`](#reprlib.Repr "reprlib.Repr") to add support for additional built-in object types or to modify
the handling of types already supported. This example shows how special support
for file objects could be added:

```
import reprlib
import sys

class MyRepr(reprlib.Repr):

    def repr_TextIOWrapper(self, obj, level):
        if obj.name in {'<stdin>', '<stdout>', '<stderr>'}:
            return obj.name
        return repr(obj)

aRepr = MyRepr()
print(aRepr.repr(sys.stdin))         # prints '<stdin>'
```

```
<stdin>
```

### [Table of Contents](../contents.html)

* [`reprlib` — Alternate `repr()` implementation](#)
  + [Repr Objects](#repr-objects)
  + [Subclassing Repr Objects](#subclassing-repr-objects)

#### Previous topic

[`pprint` — Data pretty printer](pprint.html "previous chapter")

#### Next topic

[`enum` — Support for enumerations](enum.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/reprlib.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](enum.html "enum — Support for enumerations") |
* [previous](pprint.html "pprint — Data pretty printer") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Types](datatypes.html) »
* `reprlib` — Alternate `repr()` implementation
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
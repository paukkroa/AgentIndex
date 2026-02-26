### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](filesys.html "File and Directory Access") |
* [previous](functools.html "functools — Higher-order functions and operations on callable objects") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Functional Programming Modules](functional.html) »
* `operator` — Standard operators as functions
* |
* Theme
  Auto
  Light
  Dark
   |

# `operator` — Standard operators as functions[¶](#module-operator "Link to this heading")

**Source code:** [Lib/operator.py](https://github.com/python/cpython/tree/3.14/Lib/operator.py)

---

The `operator` module exports a set of efficient functions corresponding to
the intrinsic operators of Python. For example, `operator.add(x, y)` is
equivalent to the expression `x+y`. Many function names are those used for
special methods, without the double underscores. For backward compatibility,
many of these have a variant with the double underscores kept. The variants
without the double underscores are preferred for clarity.

The functions fall into categories that perform object comparisons, logical
operations, mathematical operations and sequence operations.

The object comparison functions are useful for all objects, and are named after
the rich comparison operators they support:

operator.lt(*a*, *b*)[¶](#operator.lt "Link to this definition")

operator.le(*a*, *b*)[¶](#operator.le "Link to this definition")

operator.eq(*a*, *b*)[¶](#operator.eq "Link to this definition")

operator.ne(*a*, *b*)[¶](#operator.ne "Link to this definition")

operator.ge(*a*, *b*)[¶](#operator.ge "Link to this definition")

operator.gt(*a*, *b*)[¶](#operator.gt "Link to this definition")

operator.\_\_lt\_\_(*a*, *b*)[¶](#operator.__lt__ "Link to this definition")

operator.\_\_le\_\_(*a*, *b*)[¶](#operator.__le__ "Link to this definition")

operator.\_\_eq\_\_(*a*, *b*)[¶](#operator.__eq__ "Link to this definition")

operator.\_\_ne\_\_(*a*, *b*)[¶](#operator.__ne__ "Link to this definition")

operator.\_\_ge\_\_(*a*, *b*)[¶](#operator.__ge__ "Link to this definition")

operator.\_\_gt\_\_(*a*, *b*)[¶](#operator.__gt__ "Link to this definition")
:   Perform “rich comparisons” between *a* and *b*. Specifically, `lt(a, b)` is
    equivalent to `a < b`, `le(a, b)` is equivalent to `a <= b`, `eq(a,
    b)` is equivalent to `a == b`, `ne(a, b)` is equivalent to `a != b`,
    `gt(a, b)` is equivalent to `a > b` and `ge(a, b)` is equivalent to `a
    >= b`. Note that these functions can return any value, which may
    or may not be interpretable as a Boolean value. See
    [Comparisons](../reference/expressions.html#comparisons) for more information about rich comparisons.

The logical operations are also generally applicable to all objects, and support
truth tests, identity tests, and boolean operations:

operator.not\_(*obj*)[¶](#operator.not_ "Link to this definition")

operator.\_\_not\_\_(*obj*)[¶](#operator.__not__ "Link to this definition")
:   Return the outcome of [`not`](../reference/expressions.html#not) *obj*. (Note that there is no
    `__not__()` method for object instances; only the interpreter core defines
    this operation. The result is affected by the [`__bool__()`](../reference/datamodel.html#object.__bool__ "object.__bool__") and
    [`__len__()`](../reference/datamodel.html#object.__len__ "object.__len__") methods.)

operator.truth(*obj*)[¶](#operator.truth "Link to this definition")
:   Return [`True`](constants.html#True "True") if *obj* is true, and [`False`](constants.html#False "False") otherwise. This is
    equivalent to using the [`bool`](functions.html#bool "bool") constructor.

operator.is\_(*a*, *b*)[¶](#operator.is_ "Link to this definition")
:   Return `a is b`. Tests object identity.

operator.is\_not(*a*, *b*)[¶](#operator.is_not "Link to this definition")
:   Return `a is not b`. Tests object identity.

operator.is\_none(*a*)[¶](#operator.is_none "Link to this definition")
:   Return `a is None`. Tests object identity.

    Added in version 3.14.

operator.is\_not\_none(*a*)[¶](#operator.is_not_none "Link to this definition")
:   Return `a is not None`. Tests object identity.

    Added in version 3.14.

The mathematical and bitwise operations are the most numerous:

operator.abs(*obj*)[¶](#operator.abs "Link to this definition")

operator.\_\_abs\_\_(*obj*)[¶](#operator.__abs__ "Link to this definition")
:   Return the absolute value of *obj*.

operator.add(*a*, *b*)[¶](#operator.add "Link to this definition")

operator.\_\_add\_\_(*a*, *b*)[¶](#operator.__add__ "Link to this definition")
:   Return `a + b`, for *a* and *b* numbers.

operator.and\_(*a*, *b*)[¶](#operator.and_ "Link to this definition")

operator.\_\_and\_\_(*a*, *b*)[¶](#operator.__and__ "Link to this definition")
:   Return the bitwise and of *a* and *b*.

operator.floordiv(*a*, *b*)[¶](#operator.floordiv "Link to this definition")

operator.\_\_floordiv\_\_(*a*, *b*)[¶](#operator.__floordiv__ "Link to this definition")
:   Return `a // b`.

operator.index(*a*)[¶](#operator.index "Link to this definition")

operator.\_\_index\_\_(*a*)[¶](#operator.__index__ "Link to this definition")
:   Return *a* converted to an integer. Equivalent to `a.__index__()`.

    Changed in version 3.10: The result always has exact type [`int`](functions.html#int "int"). Previously, the result
    could have been an instance of a subclass of `int`.

operator.inv(*obj*)[¶](#operator.inv "Link to this definition")

operator.invert(*obj*)[¶](#operator.invert "Link to this definition")

operator.\_\_inv\_\_(*obj*)[¶](#operator.__inv__ "Link to this definition")

operator.\_\_invert\_\_(*obj*)[¶](#operator.__invert__ "Link to this definition")
:   Return the bitwise inverse of the number *obj*. This is equivalent to `~obj`.

operator.lshift(*a*, *b*)[¶](#operator.lshift "Link to this definition")

operator.\_\_lshift\_\_(*a*, *b*)[¶](#operator.__lshift__ "Link to this definition")
:   Return *a* shifted left by *b*.

operator.mod(*a*, *b*)[¶](#operator.mod "Link to this definition")

operator.\_\_mod\_\_(*a*, *b*)[¶](#operator.__mod__ "Link to this definition")
:   Return `a % b`.

operator.mul(*a*, *b*)[¶](#operator.mul "Link to this definition")

operator.\_\_mul\_\_(*a*, *b*)[¶](#operator.__mul__ "Link to this definition")
:   Return `a * b`, for *a* and *b* numbers.

operator.matmul(*a*, *b*)[¶](#operator.matmul "Link to this definition")

operator.\_\_matmul\_\_(*a*, *b*)[¶](#operator.__matmul__ "Link to this definition")
:   Return `a @ b`.

    Added in version 3.5.

operator.neg(*obj*)[¶](#operator.neg "Link to this definition")

operator.\_\_neg\_\_(*obj*)[¶](#operator.__neg__ "Link to this definition")
:   Return *obj* negated (`-obj`).

operator.or\_(*a*, *b*)[¶](#operator.or_ "Link to this definition")

operator.\_\_or\_\_(*a*, *b*)[¶](#operator.__or__ "Link to this definition")
:   Return the bitwise or of *a* and *b*.

operator.pos(*obj*)[¶](#operator.pos "Link to this definition")

operator.\_\_pos\_\_(*obj*)[¶](#operator.__pos__ "Link to this definition")
:   Return *obj* positive (`+obj`).

operator.pow(*a*, *b*)[¶](#operator.pow "Link to this definition")

operator.\_\_pow\_\_(*a*, *b*)[¶](#operator.__pow__ "Link to this definition")
:   Return `a ** b`, for *a* and *b* numbers.

operator.rshift(*a*, *b*)[¶](#operator.rshift "Link to this definition")

operator.\_\_rshift\_\_(*a*, *b*)[¶](#operator.__rshift__ "Link to this definition")
:   Return *a* shifted right by *b*.

operator.sub(*a*, *b*)[¶](#operator.sub "Link to this definition")

operator.\_\_sub\_\_(*a*, *b*)[¶](#operator.__sub__ "Link to this definition")
:   Return `a - b`.

operator.truediv(*a*, *b*)[¶](#operator.truediv "Link to this definition")

operator.\_\_truediv\_\_(*a*, *b*)[¶](#operator.__truediv__ "Link to this definition")
:   Return `a / b` where 2/3 is .66 rather than 0. This is also known as
    “true” division.

operator.xor(*a*, *b*)[¶](#operator.xor "Link to this definition")

operator.\_\_xor\_\_(*a*, *b*)[¶](#operator.__xor__ "Link to this definition")
:   Return the bitwise exclusive or of *a* and *b*.

Operations which work with sequences (some of them with mappings too) include:

operator.concat(*a*, *b*)[¶](#operator.concat "Link to this definition")

operator.\_\_concat\_\_(*a*, *b*)[¶](#operator.__concat__ "Link to this definition")
:   Return `a + b` for *a* and *b* sequences.

operator.contains(*a*, *b*)[¶](#operator.contains "Link to this definition")

operator.\_\_contains\_\_(*a*, *b*)[¶](#operator.__contains__ "Link to this definition")
:   Return the outcome of the test `b in a`. Note the reversed operands.

operator.countOf(*a*, *b*)[¶](#operator.countOf "Link to this definition")
:   Return the number of occurrences of *b* in *a*.

operator.delitem(*a*, *b*)[¶](#operator.delitem "Link to this definition")

operator.\_\_delitem\_\_(*a*, *b*)[¶](#operator.__delitem__ "Link to this definition")
:   Remove the value of *a* at index *b*.

operator.getitem(*a*, *b*)[¶](#operator.getitem "Link to this definition")

operator.\_\_getitem\_\_(*a*, *b*)[¶](#operator.__getitem__ "Link to this definition")
:   Return the value of *a* at index *b*.

operator.indexOf(*a*, *b*)[¶](#operator.indexOf "Link to this definition")
:   Return the index of the first of occurrence of *b* in *a*.

operator.setitem(*a*, *b*, *c*)[¶](#operator.setitem "Link to this definition")

operator.\_\_setitem\_\_(*a*, *b*, *c*)[¶](#operator.__setitem__ "Link to this definition")
:   Set the value of *a* at index *b* to *c*.

operator.length\_hint(*obj*, *default=0*)[¶](#operator.length_hint "Link to this definition")
:   Return an estimated length for the object *obj*. First try to return its
    actual length, then an estimate using [`object.__length_hint__()`](../reference/datamodel.html#object.__length_hint__ "object.__length_hint__"), and
    finally return the default value.

    Added in version 3.4.

The following operation works with callables:

operator.call(*obj*, */*, *\*args*, *\*\*kwargs*)[¶](#operator.call "Link to this definition")

operator.\_\_call\_\_(*obj*, */*, *\*args*, *\*\*kwargs*)[¶](#operator.__call__ "Link to this definition")
:   Return `obj(*args, **kwargs)`.

    Added in version 3.11.

The `operator` module also defines tools for generalized attribute and item
lookups. These are useful for making fast field extractors as arguments for
[`map()`](functions.html#map "map"), [`sorted()`](functions.html#sorted "sorted"), [`itertools.groupby()`](itertools.html#itertools.groupby "itertools.groupby"), or other functions that
expect a function argument.

operator.attrgetter(*attr*)[¶](#operator.attrgetter "Link to this definition")

operator.attrgetter(*\*attrs*)
:   Return a callable object that fetches *attr* from its operand.
    If more than one attribute is requested, returns a tuple of attributes.
    The attribute names can also contain dots. For example:

    * After `f = attrgetter('name')`, the call `f(b)` returns `b.name`.
    * After `f = attrgetter('name', 'date')`, the call `f(b)` returns
      `(b.name, b.date)`.
    * After `f = attrgetter('name.first', 'name.last')`, the call `f(b)`
      returns `(b.name.first, b.name.last)`.

    Equivalent to:

    ```
    def attrgetter(*items):
        if any(not isinstance(item, str) for item in items):
            raise TypeError('attribute name must be a string')
        if len(items) == 1:
            attr = items[0]
            def g(obj):
                return resolve_attr(obj, attr)
        else:
            def g(obj):
                return tuple(resolve_attr(obj, attr) for attr in items)
        return g

    def resolve_attr(obj, attr):
        for name in attr.split("."):
            obj = getattr(obj, name)
        return obj
    ```

operator.itemgetter(*item*)[¶](#operator.itemgetter "Link to this definition")

operator.itemgetter(*\*items*)
:   Return a callable object that fetches *item* from its operand using the
    operand’s [`__getitem__()`](../reference/datamodel.html#object.__getitem__ "object.__getitem__") method. If multiple items are specified,
    returns a tuple of lookup values. For example:

    * After `f = itemgetter(2)`, the call `f(r)` returns `r[2]`.
    * After `g = itemgetter(2, 5, 3)`, the call `g(r)` returns
      `(r[2], r[5], r[3])`.

    Equivalent to:

    ```
    def itemgetter(*items):
        if len(items) == 1:
            item = items[0]
            def g(obj):
                return obj[item]
        else:
            def g(obj):
                return tuple(obj[item] for item in items)
        return g
    ```

    The items can be any type accepted by the operand’s [`__getitem__()`](../reference/datamodel.html#object.__getitem__ "object.__getitem__")
    method. Dictionaries accept any [hashable](../glossary.html#term-hashable) value. Lists, tuples, and
    strings accept an index or a slice:

    ```
    >>> itemgetter(1)('ABCDEFG')
    'B'
    >>> itemgetter(1, 3, 5)('ABCDEFG')
    ('B', 'D', 'F')
    >>> itemgetter(slice(2, None))('ABCDEFG')
    'CDEFG'
    >>> soldier = dict(rank='captain', name='dotterbart')
    >>> itemgetter('rank')(soldier)
    'captain'
    ```

    Example of using [`itemgetter()`](#operator.itemgetter "operator.itemgetter") to retrieve specific fields from a
    tuple record:

    ```
    >>> inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
    >>> getcount = itemgetter(1)
    >>> list(map(getcount, inventory))
    [3, 2, 5, 1]
    >>> sorted(inventory, key=getcount)
    [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]
    ```

operator.methodcaller(*name*, */*, *\*args*, *\*\*kwargs*)[¶](#operator.methodcaller "Link to this definition")
:   Return a callable object that calls the method *name* on its operand. If
    additional arguments and/or keyword arguments are given, they will be given
    to the method as well. For example:

    * After `f = methodcaller('name')`, the call `f(b)` returns `b.name()`.
    * After `f = methodcaller('name', 'foo', bar=1)`, the call `f(b)`
      returns `b.name('foo', bar=1)`.

    Equivalent to:

    ```
    def methodcaller(name, /, *args, **kwargs):
        def caller(obj):
            return getattr(obj, name)(*args, **kwargs)
        return caller
    ```

## Mapping Operators to Functions[¶](#mapping-operators-to-functions "Link to this heading")

This table shows how abstract operations correspond to operator symbols in the
Python syntax and the functions in the `operator` module.

| Operation | Syntax | Function |
| --- | --- | --- |
| Addition | `a + b` | `add(a, b)` |
| Concatenation | `seq1 + seq2` | `concat(seq1, seq2)` |
| Containment Test | `obj in seq` | `contains(seq, obj)` |
| Division | `a / b` | `truediv(a, b)` |
| Division | `a // b` | `floordiv(a, b)` |
| Bitwise And | `a & b` | `and_(a, b)` |
| Bitwise Exclusive Or | `a ^ b` | `xor(a, b)` |
| Bitwise Inversion | `~ a` | `invert(a)` |
| Bitwise Or | `a | b` | `or_(a, b)` |
| Exponentiation | `a ** b` | `pow(a, b)` |
| Identity | `a is b` | `is_(a, b)` |
| Identity | `a is not b` | `is_not(a, b)` |
| Identity | `a is None` | `is_none(a)` |
| Identity | `a is not None` | `is_not_none(a)` |
| Indexed Assignment | `obj[k] = v` | `setitem(obj, k, v)` |
| Indexed Deletion | `del obj[k]` | `delitem(obj, k)` |
| Indexing | `obj[k]` | `getitem(obj, k)` |
| Left Shift | `a << b` | `lshift(a, b)` |
| Modulo | `a % b` | `mod(a, b)` |
| Multiplication | `a * b` | `mul(a, b)` |
| Matrix Multiplication | `a @ b` | `matmul(a, b)` |
| Negation (Arithmetic) | `- a` | `neg(a)` |
| Negation (Logical) | `not a` | `not_(a)` |
| Positive | `+ a` | `pos(a)` |
| Right Shift | `a >> b` | `rshift(a, b)` |
| Slice Assignment | `seq[i:j] = values` | `setitem(seq, slice(i, j), values)` |
| Slice Deletion | `del seq[i:j]` | `delitem(seq, slice(i, j))` |
| Slicing | `seq[i:j]` | `getitem(seq, slice(i, j))` |
| String Formatting | `s % obj` | `mod(s, obj)` |
| Subtraction | `a - b` | `sub(a, b)` |
| Truth Test | `obj` | `truth(obj)` |
| Ordering | `a < b` | `lt(a, b)` |
| Ordering | `a <= b` | `le(a, b)` |
| Equality | `a == b` | `eq(a, b)` |
| Difference | `a != b` | `ne(a, b)` |
| Ordering | `a >= b` | `ge(a, b)` |
| Ordering | `a > b` | `gt(a, b)` |

## In-place Operators[¶](#in-place-operators "Link to this heading")

Many operations have an “in-place” version. Listed below are functions
providing a more primitive access to in-place operators than the usual syntax
does; for example, the [statement](../glossary.html#term-statement) `x += y` is equivalent to
`x = operator.iadd(x, y)`. Another way to put it is to say that
`z = operator.iadd(x, y)` is equivalent to the compound statement
`z = x; z += y`.

In those examples, note that when an in-place method is called, the computation
and assignment are performed in two separate steps. The in-place functions
listed below only do the first step, calling the in-place method. The second
step, assignment, is not handled.

For immutable targets such as strings, numbers, and tuples, the updated
value is computed, but not assigned back to the input variable:

```
>>> a = 'hello'
>>> iadd(a, ' world')
'hello world'
>>> a
'hello'
```

For mutable targets such as lists and dictionaries, the in-place method
will perform the update, so no subsequent assignment is necessary:

```
>>> s = ['h', 'e', 'l', 'l', 'o']
>>> iadd(s, [' ', 'w', 'o', 'r', 'l', 'd'])
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> s
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
```

operator.iadd(*a*, *b*)[¶](#operator.iadd "Link to this definition")

operator.\_\_iadd\_\_(*a*, *b*)[¶](#operator.__iadd__ "Link to this definition")
:   `a = iadd(a, b)` is equivalent to `a += b`.

operator.iand(*a*, *b*)[¶](#operator.iand "Link to this definition")

operator.\_\_iand\_\_(*a*, *b*)[¶](#operator.__iand__ "Link to this definition")
:   `a = iand(a, b)` is equivalent to `a &= b`.

operator.iconcat(*a*, *b*)[¶](#operator.iconcat "Link to this definition")

operator.\_\_iconcat\_\_(*a*, *b*)[¶](#operator.__iconcat__ "Link to this definition")
:   `a = iconcat(a, b)` is equivalent to `a += b` for *a* and *b* sequences.

operator.ifloordiv(*a*, *b*)[¶](#operator.ifloordiv "Link to this definition")

operator.\_\_ifloordiv\_\_(*a*, *b*)[¶](#operator.__ifloordiv__ "Link to this definition")
:   `a = ifloordiv(a, b)` is equivalent to `a //= b`.

operator.ilshift(*a*, *b*)[¶](#operator.ilshift "Link to this definition")

operator.\_\_ilshift\_\_(*a*, *b*)[¶](#operator.__ilshift__ "Link to this definition")
:   `a = ilshift(a, b)` is equivalent to `a <<= b`.

operator.imod(*a*, *b*)[¶](#operator.imod "Link to this definition")

operator.\_\_imod\_\_(*a*, *b*)[¶](#operator.__imod__ "Link to this definition")
:   `a = imod(a, b)` is equivalent to `a %= b`.

operator.imul(*a*, *b*)[¶](#operator.imul "Link to this definition")

operator.\_\_imul\_\_(*a*, *b*)[¶](#operator.__imul__ "Link to this definition")
:   `a = imul(a, b)` is equivalent to `a *= b`.

operator.imatmul(*a*, *b*)[¶](#operator.imatmul "Link to this definition")

operator.\_\_imatmul\_\_(*a*, *b*)[¶](#operator.__imatmul__ "Link to this definition")
:   `a = imatmul(a, b)` is equivalent to `a @= b`.

    Added in version 3.5.

operator.ior(*a*, *b*)[¶](#operator.ior "Link to this definition")

operator.\_\_ior\_\_(*a*, *b*)[¶](#operator.__ior__ "Link to this definition")
:   `a = ior(a, b)` is equivalent to `a |= b`.

operator.ipow(*a*, *b*)[¶](#operator.ipow "Link to this definition")

operator.\_\_ipow\_\_(*a*, *b*)[¶](#operator.__ipow__ "Link to this definition")
:   `a = ipow(a, b)` is equivalent to `a **= b`.

operator.irshift(*a*, *b*)[¶](#operator.irshift "Link to this definition")

operator.\_\_irshift\_\_(*a*, *b*)[¶](#operator.__irshift__ "Link to this definition")
:   `a = irshift(a, b)` is equivalent to `a >>= b`.

operator.isub(*a*, *b*)[¶](#operator.isub "Link to this definition")

operator.\_\_isub\_\_(*a*, *b*)[¶](#operator.__isub__ "Link to this definition")
:   `a = isub(a, b)` is equivalent to `a -= b`.

operator.itruediv(*a*, *b*)[¶](#operator.itruediv "Link to this definition")

operator.\_\_itruediv\_\_(*a*, *b*)[¶](#operator.__itruediv__ "Link to this definition")
:   `a = itruediv(a, b)` is equivalent to `a /= b`.

operator.ixor(*a*, *b*)[¶](#operator.ixor "Link to this definition")

operator.\_\_ixor\_\_(*a*, *b*)[¶](#operator.__ixor__ "Link to this definition")
:   `a = ixor(a, b)` is equivalent to `a ^= b`.

### [Table of Contents](../contents.html)

* [`operator` — Standard operators as functions](#)
  + [Mapping Operators to Functions](#mapping-operators-to-functions)
  + [In-place Operators](#in-place-operators)

#### Previous topic

[`functools` — Higher-order functions and operations on callable objects](functools.html "previous chapter")

#### Next topic

[File and Directory Access](filesys.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/operator.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](filesys.html "File and Directory Access") |
* [previous](functools.html "functools — Higher-order functions and operations on callable objects") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Functional Programming Modules](functional.html) »
* `operator` — Standard operators as functions
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
### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](stdtypes.html "Built-in Types") |
* [previous](functions.html "Built-in Functions") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Built-in Constants
* |
* Theme
  Auto
  Light
  Dark
   |

# Built-in Constants[¶](#built-in-constants "Link to this heading")

A small number of constants live in the built-in namespace. They are:

False[¶](#False "Link to this definition")
:   The false value of the [`bool`](functions.html#bool "bool") type. Assignments to `False`
    are illegal and raise a [`SyntaxError`](exceptions.html#SyntaxError "SyntaxError").

True[¶](#True "Link to this definition")
:   The true value of the [`bool`](functions.html#bool "bool") type. Assignments to `True`
    are illegal and raise a [`SyntaxError`](exceptions.html#SyntaxError "SyntaxError").

None[¶](#None "Link to this definition")
:   An object frequently used to represent the absence of a value, as when
    default arguments are not passed to a function. Assignments to `None`
    are illegal and raise a [`SyntaxError`](exceptions.html#SyntaxError "SyntaxError").
    `None` is the sole instance of the [`NoneType`](types.html#types.NoneType "types.NoneType") type.

NotImplemented[¶](#NotImplemented "Link to this definition")
:   A special value which should be returned by the binary special methods
    (e.g. [`__eq__()`](../reference/datamodel.html#object.__eq__ "object.__eq__"), [`__lt__()`](../reference/datamodel.html#object.__lt__ "object.__lt__"), [`__add__()`](../reference/datamodel.html#object.__add__ "object.__add__"), [`__rsub__()`](../reference/datamodel.html#object.__rsub__ "object.__rsub__"),
    etc.) to indicate that the operation is not implemented with respect to
    the other type; may be returned by the in-place binary special methods
    (e.g. [`__imul__()`](../reference/datamodel.html#object.__imul__ "object.__imul__"), [`__iand__()`](../reference/datamodel.html#object.__iand__ "object.__iand__"), etc.) for the same purpose.
    It should not be evaluated in a boolean context.
    `NotImplemented` is the sole instance of the [`types.NotImplementedType`](types.html#types.NotImplementedType "types.NotImplementedType") type.

    Note

    When a binary (or in-place) method returns `NotImplemented` the
    interpreter will try the reflected operation on the other type (or some
    other fallback, depending on the operator). If all attempts return
    `NotImplemented`, the interpreter will raise an appropriate exception.
    Incorrectly returning `NotImplemented` will result in a misleading
    error message or the `NotImplemented` value being returned to Python code.

    See [Implementing the arithmetic operations](numbers.html#implementing-the-arithmetic-operations) for examples.

    Caution

    `NotImplemented` and `NotImplementedError` are not
    interchangeable. This constant should only be used as described
    above; see [`NotImplementedError`](exceptions.html#NotImplementedError "NotImplementedError") for details on correct usage
    of the exception.

    Changed in version 3.9: Evaluating `NotImplemented` in a boolean context was deprecated.

    Changed in version 3.14: Evaluating `NotImplemented` in a boolean context now raises a [`TypeError`](exceptions.html#TypeError "TypeError").
    It previously evaluated to [`True`](#True "True") and emitted a [`DeprecationWarning`](exceptions.html#DeprecationWarning "DeprecationWarning")
    since Python 3.9.

Ellipsis[¶](#Ellipsis "Link to this definition")
:   The same as the ellipsis literal “`...`”, an object frequently used to
    indicate that something is omitted. Assignment to `Ellipsis` is possible, but
    assignment to `...` raises a [`SyntaxError`](exceptions.html#SyntaxError "SyntaxError").
    `Ellipsis` is the sole instance of the [`types.EllipsisType`](types.html#types.EllipsisType "types.EllipsisType") type.

\_\_debug\_\_[¶](#debug__ "Link to this definition")
:   This constant is true if Python was not started with an [`-O`](../using/cmdline.html#cmdoption-O) option.
    See also the [`assert`](../reference/simple_stmts.html#assert) statement.

Note

The names [`None`](#None "None"), [`False`](#False "False"), [`True`](#True "True") and [`__debug__`](#debug__ "__debug__")
cannot be reassigned (assignments to them, even as an attribute name, raise
[`SyntaxError`](exceptions.html#SyntaxError "SyntaxError")), so they can be considered “true” constants.

## Constants added by the [`site`](site.html#module-site "site: Module responsible for site-specific configuration.") module[¶](#constants-added-by-the-site-module "Link to this heading")

The [`site`](site.html#module-site "site: Module responsible for site-specific configuration.") module (which is imported automatically during startup, except
if the [`-S`](../using/cmdline.html#cmdoption-S) command-line option is given) adds several constants to the
built-in namespace. They are useful for the interactive interpreter shell and
should not be used in programs.

quit(*code=None*)[¶](#quit "Link to this definition")

exit(*code=None*)[¶](#exit "Link to this definition")
:   Objects that when printed, print a message like “Use quit() or Ctrl-D
    (i.e. EOF) to exit”, and when accessed directly in the interactive
    interpreter or called as functions, raise [`SystemExit`](exceptions.html#SystemExit "SystemExit") with the
    specified exit code.

help
:   Object that when printed, prints the message “Type help() for interactive
    help, or help(object) for help about object.”, and when accessed directly
    in the interactive interpreter, invokes the built-in help system
    (see [`help()`](functions.html#help "help")).

copyright[¶](#copyright "Link to this definition")

credits[¶](#credits "Link to this definition")
:   Objects that when printed or called, print the text of copyright or
    credits, respectively.

license[¶](#license "Link to this definition")
:   Object that when printed, prints the message “Type license() to see the
    full license text”, and when called, displays the full license text in a
    pager-like fashion (one screen at a time).

### [Table of Contents](../contents.html)

* [Built-in Constants](#)
  + [Constants added by the `site` module](#constants-added-by-the-site-module)

#### Previous topic

[Built-in Functions](functions.html "previous chapter")

#### Next topic

[Built-in Types](stdtypes.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/constants.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](stdtypes.html "Built-in Types") |
* [previous](functions.html "Built-in Functions") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Built-in Constants
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
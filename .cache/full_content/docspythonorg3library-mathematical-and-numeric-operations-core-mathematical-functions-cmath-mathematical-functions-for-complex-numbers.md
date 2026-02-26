### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](decimal.html "decimal — Decimal fixed-point and floating-point arithmetic") |
* [previous](math.html "math — Mathematical functions") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Numeric and Mathematical Modules](numeric.html) »
* `cmath` — Mathematical functions for complex numbers
* |
* Theme
  Auto
  Light
  Dark
   |

# `cmath` — Mathematical functions for complex numbers[¶](#module-cmath "Link to this heading")

---

This module provides access to mathematical functions for complex numbers. The
functions in this module accept integers, floating-point numbers or complex
numbers as arguments. They will also accept any Python object that has either a
[`__complex__()`](../reference/datamodel.html#object.__complex__ "object.__complex__") or a [`__float__()`](../reference/datamodel.html#object.__float__ "object.__float__") method: these methods are used to
convert the object to a complex or floating-point number, respectively, and
the function is then applied to the result of the conversion.

Note

For functions involving branch cuts, we have the problem of deciding how to
define those functions on the cut itself. Following Kahan’s “Branch cuts for
complex elementary functions” paper, as well as Annex G of C99 and later C
standards, we use the sign of zero to distinguish one side of the branch cut
from the other: for a branch cut along (a portion of) the real axis we look
at the sign of the imaginary part, while for a branch cut along the
imaginary axis we look at the sign of the real part.

For example, the [`cmath.sqrt()`](#cmath.sqrt "cmath.sqrt") function has a branch cut along the
negative real axis. An argument of `-2-0j` is treated as
though it lies *below* the branch cut, and so gives a result on the negative
imaginary axis:

```
>>> cmath.sqrt(-2-0j)
-1.4142135623730951j
```

But an argument of `-2+0j` is treated as though it lies above
the branch cut:

```
>>> cmath.sqrt(-2+0j)
1.4142135623730951j
```

|  |  |
| --- | --- |
| **Conversions to and from polar coordinates** | |
| [`phase(z)`](#cmath.phase "cmath.phase") | Return the phase of *z* |
| [`polar(z)`](#cmath.polar "cmath.polar") | Return the representation of *z* in polar coordinates |
| [`rect(r, phi)`](#cmath.rect "cmath.rect") | Return the complex number *z* with polar coordinates *r* and *phi* |
| **Power and logarithmic functions** | |
| [`exp(z)`](#cmath.exp "cmath.exp") | Return *e* raised to the power *z* |
| [`log(z[, base])`](#cmath.log "cmath.log") | Return the logarithm of *z* to the given *base* (*e* by default) |
| [`log10(z)`](#cmath.log10 "cmath.log10") | Return the base-10 logarithm of *z* |
| [`sqrt(z)`](#cmath.sqrt "cmath.sqrt") | Return the square root of *z* |
| **Trigonometric functions** | |
| [`acos(z)`](#cmath.acos "cmath.acos") | Return the arc cosine of *z* |
| [`asin(z)`](#cmath.asin "cmath.asin") | Return the arc sine of *z* |
| [`atan(z)`](#cmath.atan "cmath.atan") | Return the arc tangent of *z* |
| [`cos(z)`](#cmath.cos "cmath.cos") | Return the cosine of *z* |
| [`sin(z)`](#cmath.sin "cmath.sin") | Return the sine of *z* |
| [`tan(z)`](#cmath.tan "cmath.tan") | Return the tangent of *z* |
| **Hyperbolic functions** | |
| [`acosh(z)`](#cmath.acosh "cmath.acosh") | Return the inverse hyperbolic cosine of *z* |
| [`asinh(z)`](#cmath.asinh "cmath.asinh") | Return the inverse hyperbolic sine of *z* |
| [`atanh(z)`](#cmath.atanh "cmath.atanh") | Return the inverse hyperbolic tangent of *z* |
| [`cosh(z)`](#cmath.cosh "cmath.cosh") | Return the hyperbolic cosine of *z* |
| [`sinh(z)`](#cmath.sinh "cmath.sinh") | Return the hyperbolic sine of *z* |
| [`tanh(z)`](#cmath.tanh "cmath.tanh") | Return the hyperbolic tangent of *z* |
| **Classification functions** | |
| [`isfinite(z)`](#cmath.isfinite "cmath.isfinite") | Check if all components of *z* are finite |
| [`isinf(z)`](#cmath.isinf "cmath.isinf") | Check if any component of *z* is infinite |
| [`isnan(z)`](#cmath.isnan "cmath.isnan") | Check if any component of *z* is a NaN |
| [`isclose(a, b, *, rel_tol, abs_tol)`](#cmath.isclose "cmath.isclose") | Check if the values *a* and *b* are close to each other |
| **Constants** | |
| [`pi`](#cmath.pi "cmath.pi") | *π* = 3.141592… |
| [`e`](#cmath.e "cmath.e") | *e* = 2.718281… |
| [`tau`](#cmath.tau "cmath.tau") | *τ* = 2*π* = 6.283185… |
| [`inf`](#cmath.inf "cmath.inf") | Positive infinity |
| [`infj`](#cmath.infj "cmath.infj") | Pure imaginary infinity |
| [`nan`](#cmath.nan "cmath.nan") | “Not a number” (NaN) |
| [`nanj`](#cmath.nanj "cmath.nanj") | Pure imaginary NaN |

## Conversions to and from polar coordinates[¶](#conversions-to-and-from-polar-coordinates "Link to this heading")

A Python complex number `z` is stored internally using *rectangular*
or *Cartesian* coordinates. It is completely determined by its *real
part* `z.real` and its *imaginary part* `z.imag`.

*Polar coordinates* give an alternative way to represent a complex
number. In polar coordinates, a complex number *z* is defined by the
modulus *r* and the phase angle *phi*. The modulus *r* is the distance
from *z* to the origin, while the phase *phi* is the counterclockwise
angle, measured in radians, from the positive x-axis to the line
segment that joins the origin to *z*.

The following functions can be used to convert from the native
rectangular coordinates to polar coordinates and back.

cmath.phase(*z*)[¶](#cmath.phase "Link to this definition")
:   Return the phase of *z* (also known as the *argument* of *z*), as a float.
    `phase(z)` is equivalent to `math.atan2(z.imag, z.real)`. The result
    lies in the range [-*π*, *π*], and the branch cut for this operation lies
    along the negative real axis. The sign of the result is the same as the
    sign of `z.imag`, even when `z.imag` is zero:

    ```
    >>> phase(-1+0j)
    3.141592653589793
    >>> phase(-1-0j)
    -3.141592653589793
    ```

Note

The modulus (absolute value) of a complex number *z* can be
computed using the built-in [`abs()`](functions.html#abs "abs") function. There is no
separate `cmath` module function for this operation.

cmath.polar(*z*)[¶](#cmath.polar "Link to this definition")
:   Return the representation of *z* in polar coordinates. Returns a
    pair `(r, phi)` where *r* is the modulus of *z* and *phi* is the
    phase of *z*. `polar(z)` is equivalent to `(abs(z),
    phase(z))`.

cmath.rect(*r*, *phi*)[¶](#cmath.rect "Link to this definition")
:   Return the complex number *z* with polar coordinates *r* and *phi*.
    Equivalent to `complex(r * math.cos(phi), r * math.sin(phi))`.

## Power and logarithmic functions[¶](#power-and-logarithmic-functions "Link to this heading")

cmath.exp(*z*)[¶](#cmath.exp "Link to this definition")
:   Return *e* raised to the power *z*, where *e* is the base of natural
    logarithms.

cmath.log(*z*[, *base*])[¶](#cmath.log "Link to this definition")
:   Return the logarithm of *z* to the given *base*. If the *base* is not
    specified, returns the natural logarithm of *z*. There is one branch cut,
    from 0 along the negative real axis to -∞.

cmath.log10(*z*)[¶](#cmath.log10 "Link to this definition")
:   Return the base-10 logarithm of *z*. This has the same branch cut as
    [`log()`](#cmath.log "cmath.log").

cmath.sqrt(*z*)[¶](#cmath.sqrt "Link to this definition")
:   Return the square root of *z*. This has the same branch cut as [`log()`](#cmath.log "cmath.log").

## Trigonometric functions[¶](#trigonometric-functions "Link to this heading")

cmath.acos(*z*)[¶](#cmath.acos "Link to this definition")
:   Return the arc cosine of *z*. There are two branch cuts: One extends right
    from 1 along the real axis to ∞. The other extends left from -1 along the
    real axis to -∞.

cmath.asin(*z*)[¶](#cmath.asin "Link to this definition")
:   Return the arc sine of *z*. This has the same branch cuts as [`acos()`](#cmath.acos "cmath.acos").

cmath.atan(*z*)[¶](#cmath.atan "Link to this definition")
:   Return the arc tangent of *z*. There are two branch cuts: One extends from
    `1j` along the imaginary axis to `∞j`. The other extends from `-1j`
    along the imaginary axis to `-∞j`.

cmath.cos(*z*)[¶](#cmath.cos "Link to this definition")
:   Return the cosine of *z*.

cmath.sin(*z*)[¶](#cmath.sin "Link to this definition")
:   Return the sine of *z*.

cmath.tan(*z*)[¶](#cmath.tan "Link to this definition")
:   Return the tangent of *z*.

## Hyperbolic functions[¶](#hyperbolic-functions "Link to this heading")

cmath.acosh(*z*)[¶](#cmath.acosh "Link to this definition")
:   Return the inverse hyperbolic cosine of *z*. There is one branch cut,
    extending left from 1 along the real axis to -∞.

cmath.asinh(*z*)[¶](#cmath.asinh "Link to this definition")
:   Return the inverse hyperbolic sine of *z*. There are two branch cuts:
    One extends from `1j` along the imaginary axis to `∞j`. The other
    extends from `-1j` along the imaginary axis to `-∞j`.

cmath.atanh(*z*)[¶](#cmath.atanh "Link to this definition")
:   Return the inverse hyperbolic tangent of *z*. There are two branch cuts: One
    extends from `1` along the real axis to `∞`. The other extends from
    `-1` along the real axis to `-∞`.

cmath.cosh(*z*)[¶](#cmath.cosh "Link to this definition")
:   Return the hyperbolic cosine of *z*.

cmath.sinh(*z*)[¶](#cmath.sinh "Link to this definition")
:   Return the hyperbolic sine of *z*.

cmath.tanh(*z*)[¶](#cmath.tanh "Link to this definition")
:   Return the hyperbolic tangent of *z*.

## Classification functions[¶](#classification-functions "Link to this heading")

cmath.isfinite(*z*)[¶](#cmath.isfinite "Link to this definition")
:   Return `True` if both the real and imaginary parts of *z* are finite, and
    `False` otherwise.

    Added in version 3.2.

cmath.isinf(*z*)[¶](#cmath.isinf "Link to this definition")
:   Return `True` if either the real or the imaginary part of *z* is an
    infinity, and `False` otherwise.

cmath.isnan(*z*)[¶](#cmath.isnan "Link to this definition")
:   Return `True` if either the real or the imaginary part of *z* is a NaN,
    and `False` otherwise.

cmath.isclose(*a*, *b*, *\**, *rel\_tol=1e-09*, *abs\_tol=0.0*)[¶](#cmath.isclose "Link to this definition")
:   Return `True` if the values *a* and *b* are close to each other and
    `False` otherwise.

    Whether or not two values are considered close is determined according to
    given absolute and relative tolerances. If no errors occur, the result will
    be: `abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)`.

    *rel\_tol* is the relative tolerance – it is the maximum allowed difference
    between *a* and *b*, relative to the larger absolute value of *a* or *b*.
    For example, to set a tolerance of 5%, pass `rel_tol=0.05`. The default
    tolerance is `1e-09`, which assures that the two values are the same
    within about 9 decimal digits. *rel\_tol* must be nonnegative and less
    than `1.0`.

    *abs\_tol* is the absolute tolerance; it defaults to `0.0` and it must be
    nonnegative. When comparing `x` to `0.0`, `isclose(x, 0)` is computed
    as `abs(x) <= rel_tol  * abs(x)`, which is `False` for any `x` and
    rel\_tol less than `1.0`. So add an appropriate positive abs\_tol argument
    to the call.

    The IEEE 754 special values of `NaN`, `inf`, and `-inf` will be
    handled according to IEEE rules. Specifically, `NaN` is not considered
    close to any other value, including `NaN`. `inf` and `-inf` are only
    considered close to themselves.

    Added in version 3.5.

    See also

    [**PEP 485**](https://peps.python.org/pep-0485/) – A function for testing approximate equality

## Constants[¶](#constants "Link to this heading")

cmath.pi[¶](#cmath.pi "Link to this definition")
:   The mathematical constant *π*, as a float.

cmath.e[¶](#cmath.e "Link to this definition")
:   The mathematical constant *e*, as a float.

cmath.tau[¶](#cmath.tau "Link to this definition")
:   The mathematical constant *τ*, as a float.

    Added in version 3.6.

cmath.inf[¶](#cmath.inf "Link to this definition")
:   Floating-point positive infinity. Equivalent to `float('inf')`.

    Added in version 3.6.

cmath.infj[¶](#cmath.infj "Link to this definition")
:   Complex number with zero real part and positive infinity imaginary
    part. Equivalent to `complex(0.0, float('inf'))`.

    Added in version 3.6.

cmath.nan[¶](#cmath.nan "Link to this definition")
:   A floating-point “not a number” (NaN) value. Equivalent to
    `float('nan')`. See also [`math.nan`](math.html#math.nan "math.nan").

    Added in version 3.6.

cmath.nanj[¶](#cmath.nanj "Link to this definition")
:   Complex number with zero real part and NaN imaginary part. Equivalent to
    `complex(0.0, float('nan'))`.

    Added in version 3.6.

Note that the selection of functions is similar, but not identical, to that in
module [`math`](math.html#module-math "math: Mathematical functions (sin() etc.)."). The reason for having two modules is that some users aren’t
interested in complex numbers, and perhaps don’t even know what they are. They
would rather have `math.sqrt(-1)` raise an exception than return a complex
number. Also note that the functions defined in `cmath` always return a
complex number, even if the answer can be expressed as a real number (in which
case the complex number has an imaginary part of zero).

A note on branch cuts: They are curves along which the given function fails to
be continuous. They are a necessary feature of many complex functions. It is
assumed that if you need to compute with complex functions, you will understand
about branch cuts. Consult almost any (not too elementary) book on complex
variables for enlightenment. For information of the proper choice of branch
cuts for numerical purposes, a good reference should be the following:

See also

Kahan, W: Branch cuts for complex elementary functions; or, Much ado about
nothing’s sign bit. In Iserles, A., and Powell, M. (eds.), The state of the art
in numerical analysis. Clarendon Press (1987) pp165–211.

### [Table of Contents](../contents.html)

* [`cmath` — Mathematical functions for complex numbers](#)
  + [Conversions to and from polar coordinates](#conversions-to-and-from-polar-coordinates)
  + [Power and logarithmic functions](#power-and-logarithmic-functions)
  + [Trigonometric functions](#trigonometric-functions)
  + [Hyperbolic functions](#hyperbolic-functions)
  + [Classification functions](#classification-functions)
  + [Constants](#constants)

#### Previous topic

[`math` — Mathematical functions](math.html "previous chapter")

#### Next topic

[`decimal` — Decimal fixed-point and floating-point arithmetic](decimal.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/cmath.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](decimal.html "decimal — Decimal fixed-point and floating-point arithmetic") |
* [previous](math.html "math — Mathematical functions") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Numeric and Mathematical Modules](numeric.html) »
* `cmath` — Mathematical functions for complex numbers
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
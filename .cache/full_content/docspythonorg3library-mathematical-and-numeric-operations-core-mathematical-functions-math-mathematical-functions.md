### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](cmath.html "cmath — Mathematical functions for complex numbers") |
* [previous](numbers.html "numbers — Numeric abstract base classes") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Numeric and Mathematical Modules](numeric.html) »
* `math` — Mathematical functions
* |
* Theme
  Auto
  Light
  Dark
   |

# `math` — Mathematical functions[¶](#module-math "Link to this heading")

---

This module provides access to common mathematical functions and constants,
including those defined by the C standard.

These functions cannot be used with complex numbers; use the functions of the
same name from the [`cmath`](cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.") module if you require support for complex
numbers. The distinction between functions which support complex numbers and
those which don’t is made since most users do not want to learn quite as much
mathematics as required to understand complex numbers. Receiving an exception
instead of a complex result allows earlier detection of the unexpected complex
number used as a parameter, so that the programmer can determine how and why it
was generated in the first place.

The following functions are provided by this module. Except when explicitly
noted otherwise, all return values are floats.

|  |  |
| --- | --- |
| **Number-theoretic functions** | |
| [`comb(n, k)`](#math.comb "math.comb") | Number of ways to choose *k* items from *n* items without repetition and without order |
| [`factorial(n)`](#math.factorial "math.factorial") | *n* factorial |
| [`gcd(*integers)`](#math.gcd "math.gcd") | Greatest common divisor of the integer arguments |
| [`isqrt(n)`](#math.isqrt "math.isqrt") | Integer square root of a nonnegative integer *n* |
| [`lcm(*integers)`](#math.lcm "math.lcm") | Least common multiple of the integer arguments |
| [`perm(n, k)`](#math.perm "math.perm") | Number of ways to choose *k* items from *n* items without repetition and with order |
| **Floating point arithmetic** | |
| [`ceil(x)`](#math.ceil "math.ceil") | Ceiling of *x*, the smallest integer greater than or equal to *x* |
| [`fabs(x)`](#math.fabs "math.fabs") | Absolute value of *x* |
| [`floor(x)`](#math.floor "math.floor") | Floor of *x*, the largest integer less than or equal to *x* |
| [`fma(x, y, z)`](#math.fma "math.fma") | Fused multiply-add operation: `(x * y) + z` |
| [`fmod(x, y)`](#math.fmod "math.fmod") | Remainder of division `x / y` |
| [`modf(x)`](#math.modf "math.modf") | Fractional and integer parts of *x* |
| [`remainder(x, y)`](#math.remainder "math.remainder") | Remainder of *x* with respect to *y* |
| [`trunc(x)`](#math.trunc "math.trunc") | Integer part of *x* |
| **Floating point manipulation functions** | |
| [`copysign(x, y)`](#math.copysign "math.copysign") | Magnitude (absolute value) of *x* with the sign of *y* |
| [`frexp(x)`](#math.frexp "math.frexp") | Mantissa and exponent of *x* |
| [`isclose(a, b, rel_tol, abs_tol)`](#math.isclose "math.isclose") | Check if the values *a* and *b* are close to each other |
| [`isfinite(x)`](#math.isfinite "math.isfinite") | Check if *x* is neither an infinity nor a NaN |
| [`isinf(x)`](#math.isinf "math.isinf") | Check if *x* is a positive or negative infinity |
| [`isnan(x)`](#math.isnan "math.isnan") | Check if *x* is a NaN (not a number) |
| [`ldexp(x, i)`](#math.ldexp "math.ldexp") | `x * (2**i)`, inverse of function [`frexp()`](#math.frexp "math.frexp") |
| [`nextafter(x, y, steps)`](#math.nextafter "math.nextafter") | Floating-point value *steps* steps after *x* towards *y* |
| [`ulp(x)`](#math.ulp "math.ulp") | Value of the least significant bit of *x* |
| **Power, exponential and logarithmic functions** | |
| [`cbrt(x)`](#math.cbrt "math.cbrt") | Cube root of *x* |
| [`exp(x)`](#math.exp "math.exp") | *e* raised to the power *x* |
| [`exp2(x)`](#math.exp2 "math.exp2") | *2* raised to the power *x* |
| [`expm1(x)`](#math.expm1 "math.expm1") | *e* raised to the power *x*, minus 1 |
| [`log(x, base)`](#math.log "math.log") | Logarithm of *x* to the given base (*e* by default) |
| [`log1p(x)`](#math.log1p "math.log1p") | Natural logarithm of *1+x* (base *e*) |
| [`log2(x)`](#math.log2 "math.log2") | Base-2 logarithm of *x* |
| [`log10(x)`](#math.log10 "math.log10") | Base-10 logarithm of *x* |
| [`pow(x, y)`](#math.pow "math.pow") | *x* raised to the power *y* |
| [`sqrt(x)`](#math.sqrt "math.sqrt") | Square root of *x* |
| **Summation and product functions** | |
| [`dist(p, q)`](#math.dist "math.dist") | Euclidean distance between two points *p* and *q* given as an iterable of coordinates |
| [`fsum(iterable)`](#math.fsum "math.fsum") | Sum of values in the input *iterable* |
| [`hypot(*coordinates)`](#math.hypot "math.hypot") | Euclidean norm of an iterable of coordinates |
| [`prod(iterable, start)`](#math.prod "math.prod") | Product of elements in the input *iterable* with a *start* value |
| [`sumprod(p, q)`](#math.sumprod "math.sumprod") | Sum of products from two iterables *p* and *q* |
| **Angular conversion** | |
| [`degrees(x)`](#math.degrees "math.degrees") | Convert angle *x* from radians to degrees |
| [`radians(x)`](#math.radians "math.radians") | Convert angle *x* from degrees to radians |
| **Trigonometric functions** | |
| [`acos(x)`](#math.acos "math.acos") | Arc cosine of *x* |
| [`asin(x)`](#math.asin "math.asin") | Arc sine of *x* |
| [`atan(x)`](#math.atan "math.atan") | Arc tangent of *x* |
| [`atan2(y, x)`](#math.atan2 "math.atan2") | `atan(y / x)` |
| [`cos(x)`](#math.cos "math.cos") | Cosine of *x* |
| [`sin(x)`](#math.sin "math.sin") | Sine of *x* |
| [`tan(x)`](#math.tan "math.tan") | Tangent of *x* |
| **Hyperbolic functions** | |
| [`acosh(x)`](#math.acosh "math.acosh") | Inverse hyperbolic cosine of *x* |
| [`asinh(x)`](#math.asinh "math.asinh") | Inverse hyperbolic sine of *x* |
| [`atanh(x)`](#math.atanh "math.atanh") | Inverse hyperbolic tangent of *x* |
| [`cosh(x)`](#math.cosh "math.cosh") | Hyperbolic cosine of *x* |
| [`sinh(x)`](#math.sinh "math.sinh") | Hyperbolic sine of *x* |
| [`tanh(x)`](#math.tanh "math.tanh") | Hyperbolic tangent of *x* |
| **Special functions** | |
| [`erf(x)`](#math.erf "math.erf") | [Error function](https://en.wikipedia.org/wiki/Error_function) at *x* |
| [`erfc(x)`](#math.erfc "math.erfc") | [Complementary error function](https://en.wikipedia.org/wiki/Error_function) at *x* |
| [`gamma(x)`](#math.gamma "math.gamma") | [Gamma function](https://en.wikipedia.org/wiki/Gamma_function) at *x* |
| [`lgamma(x)`](#math.lgamma "math.lgamma") | Natural logarithm of the absolute value of the [Gamma function](https://en.wikipedia.org/wiki/Gamma_function) at *x* |
| **Constants** | |
| [`pi`](#math.pi "math.pi") | *π* = 3.141592… |
| [`e`](#math.e "math.e") | *e* = 2.718281… |
| [`tau`](#math.tau "math.tau") | *τ* = 2*π* = 6.283185… |
| [`inf`](#math.inf "math.inf") | Positive infinity |
| [`nan`](#math.nan "math.nan") | “Not a number” (NaN) |

## Number-theoretic functions[¶](#number-theoretic-functions "Link to this heading")

math.comb(*n*, *k*)[¶](#math.comb "Link to this definition")
:   Return the number of ways to choose *k* items from *n* items without repetition
    and without order.

    Evaluates to `n! / (k! * (n - k)!)` when `k <= n` and evaluates
    to zero when `k > n`.

    Also called the binomial coefficient because it is equivalent
    to the coefficient of k-th term in polynomial expansion of
    `(1 + x)ⁿ`.

    Raises [`TypeError`](exceptions.html#TypeError "TypeError") if either of the arguments are not integers.
    Raises [`ValueError`](exceptions.html#ValueError "ValueError") if either of the arguments are negative.

    Added in version 3.8.

math.factorial(*n*)[¶](#math.factorial "Link to this definition")
:   Return factorial of the nonnegative integer *n*.

    Changed in version 3.10: Floats with integral values (like `5.0`) are no longer accepted.

math.gcd(*\*integers*)[¶](#math.gcd "Link to this definition")
:   Return the greatest common divisor of the specified integer arguments.
    If any of the arguments is nonzero, then the returned value is the largest
    positive integer that is a divisor of all arguments. If all arguments
    are zero, then the returned value is `0`. `gcd()` without arguments
    returns `0`.

    Added in version 3.5.

    Changed in version 3.9: Added support for an arbitrary number of arguments. Formerly, only two
    arguments were supported.

math.isqrt(*n*)[¶](#math.isqrt "Link to this definition")
:   Return the integer square root of the nonnegative integer *n*. This is the
    floor of the exact square root of *n*, or equivalently the greatest integer
    *a* such that *a*² ≤ *n*.

    For some applications, it may be more convenient to have the least integer
    *a* such that *n* ≤ *a*², or in other words the ceiling of
    the exact square root of *n*. For positive *n*, this can be computed using
    `a = 1 + isqrt(n - 1)`.

    Added in version 3.8.

math.lcm(*\*integers*)[¶](#math.lcm "Link to this definition")
:   Return the least common multiple of the specified integer arguments.
    If all arguments are nonzero, then the returned value is the smallest
    positive integer that is a multiple of all arguments. If any of the arguments
    is zero, then the returned value is `0`. `lcm()` without arguments
    returns `1`.

    Added in version 3.9.

math.perm(*n*, *k=None*)[¶](#math.perm "Link to this definition")
:   Return the number of ways to choose *k* items from *n* items
    without repetition and with order.

    Evaluates to `n! / (n - k)!` when `k <= n` and evaluates
    to zero when `k > n`.

    If *k* is not specified or is `None`, then *k* defaults to *n*
    and the function returns `n!`.

    Raises [`TypeError`](exceptions.html#TypeError "TypeError") if either of the arguments are not integers.
    Raises [`ValueError`](exceptions.html#ValueError "ValueError") if either of the arguments are negative.

    Added in version 3.8.

## Floating point arithmetic[¶](#floating-point-arithmetic "Link to this heading")

math.ceil(*x*)[¶](#math.ceil "Link to this definition")
:   Return the ceiling of *x*, the smallest integer greater than or equal to *x*.
    If *x* is not a float, delegates to [`x.__ceil__`](../reference/datamodel.html#object.__ceil__ "object.__ceil__"),
    which should return an [`Integral`](numbers.html#numbers.Integral "numbers.Integral") value.

math.fabs(*x*)[¶](#math.fabs "Link to this definition")
:   Return the absolute value of *x*.

math.floor(*x*)[¶](#math.floor "Link to this definition")
:   Return the floor of *x*, the largest integer less than or equal to *x*. If
    *x* is not a float, delegates to [`x.__floor__`](../reference/datamodel.html#object.__floor__ "object.__floor__"), which
    should return an [`Integral`](numbers.html#numbers.Integral "numbers.Integral") value.

math.fma(*x*, *y*, *z*)[¶](#math.fma "Link to this definition")
:   Fused multiply-add operation. Return `(x * y) + z`, computed as though with
    infinite precision and range followed by a single round to the `float`
    format. This operation often provides better accuracy than the direct
    expression `(x * y) + z`.

    This function follows the specification of the fusedMultiplyAdd operation
    described in the IEEE 754 standard. The standard leaves one case
    implementation-defined, namely the result of `fma(0, inf, nan)`
    and `fma(inf, 0, nan)`. In these cases, `math.fma` returns a NaN,
    and does not raise any exception.

    Added in version 3.13.

math.fmod(*x*, *y*)[¶](#math.fmod "Link to this definition")
:   Return the floating-point remainder of `x / y`,
    as defined by the platform C library function `fmod(x, y)`. Note that the
    Python expression `x % y` may not return the same result. The intent of the C
    standard is that `fmod(x, y)` be exactly (mathematically; to infinite
    precision) equal to `x - n*y` for some integer *n* such that the result has
    the same sign as *x* and magnitude less than `abs(y)`. Python’s `x % y`
    returns a result with the sign of *y* instead, and may not be exactly computable
    for float arguments. For example, `fmod(-1e-100, 1e100)` is `-1e-100`, but
    the result of Python’s `-1e-100 % 1e100` is `1e100-1e-100`, which cannot be
    represented exactly as a float, and rounds to the surprising `1e100`. For
    this reason, function [`fmod()`](#math.fmod "math.fmod") is generally preferred when working with
    floats, while Python’s `x % y` is preferred when working with integers.

math.modf(*x*)[¶](#math.modf "Link to this definition")
:   Return the fractional and integer parts of *x*. Both results carry the sign
    of *x* and are floats.

    Note that [`modf()`](#math.modf "math.modf") has a different call/return pattern
    than its C equivalents: it takes a single argument and return a pair of
    values, rather than returning its second return value through an ‘output
    parameter’ (there is no such thing in Python).

math.remainder(*x*, *y*)[¶](#math.remainder "Link to this definition")
:   Return the IEEE 754-style remainder of *x* with respect to *y*. For
    finite *x* and finite nonzero *y*, this is the difference `x - n*y`,
    where `n` is the closest integer to the exact value of the quotient `x /
    y`. If `x / y` is exactly halfway between two consecutive integers, the
    nearest *even* integer is used for `n`. The remainder `r = remainder(x,
    y)` thus always satisfies `abs(r) <= 0.5 * abs(y)`.

    Special cases follow IEEE 754: in particular, `remainder(x, math.inf)` is
    *x* for any finite *x*, and `remainder(x, 0)` and
    `remainder(math.inf, x)` raise [`ValueError`](exceptions.html#ValueError "ValueError") for any non-NaN *x*.
    If the result of the remainder operation is zero, that zero will have
    the same sign as *x*.

    On platforms using IEEE 754 binary floating point, the result of this
    operation is always exactly representable: no rounding error is introduced.

    Added in version 3.7.

math.trunc(*x*)[¶](#math.trunc "Link to this definition")
:   Return *x* with the fractional part
    removed, leaving the integer part. This rounds toward 0: `trunc()` is
    equivalent to [`floor()`](#math.floor "math.floor") for positive *x*, and equivalent to [`ceil()`](#math.ceil "math.ceil")
    for negative *x*. If *x* is not a float, delegates to [`x.__trunc__`](../reference/datamodel.html#object.__trunc__ "object.__trunc__"), which should return an [`Integral`](numbers.html#numbers.Integral "numbers.Integral") value.

For the [`ceil()`](#math.ceil "math.ceil"), [`floor()`](#math.floor "math.floor"), and [`modf()`](#math.modf "math.modf") functions, note that *all*
floating-point numbers of sufficiently large magnitude are exact integers.
Python floats typically carry no more than 53 bits of precision (the same as the
platform C double type), in which case any float *x* with `abs(x) >= 2**52`
necessarily has no fractional bits.

## Floating point manipulation functions[¶](#floating-point-manipulation-functions "Link to this heading")

math.copysign(*x*, *y*)[¶](#math.copysign "Link to this definition")
:   Return a float with the magnitude (absolute value) of *x* but the sign of
    *y*. On platforms that support signed zeros, `copysign(1.0, -0.0)`
    returns *-1.0*.

math.frexp(*x*)[¶](#math.frexp "Link to this definition")
:   Return the mantissa and exponent of *x* as the pair `(m, e)`. *m* is a float
    and *e* is an integer such that `x == m * 2**e` exactly. If *x* is zero,
    returns `(0.0, 0)`, otherwise `0.5 <= abs(m) < 1`. This is used to “pick
    apart” the internal representation of a float in a portable way.

    Note that [`frexp()`](#math.frexp "math.frexp") has a different call/return pattern
    than its C equivalents: it takes a single argument and return a pair of
    values, rather than returning its second return value through an ‘output
    parameter’ (there is no such thing in Python).

math.isclose(*a*, *b*, *\**, *rel\_tol=1e-09*, *abs\_tol=0.0*)[¶](#math.isclose "Link to this definition")
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
    as `abs(x) <= rel_tol  * abs(x)`, which is `False` for any nonzero `x` and
    *rel\_tol* less than `1.0`. So add an appropriate positive *abs\_tol* argument
    to the call.

    The IEEE 754 special values of `NaN`, `inf`, and `-inf` will be
    handled according to IEEE rules. Specifically, `NaN` is not considered
    close to any other value, including `NaN`. `inf` and `-inf` are only
    considered close to themselves.

    Added in version 3.5.

    See also

    [**PEP 485**](https://peps.python.org/pep-0485/) – A function for testing approximate equality

math.isfinite(*x*)[¶](#math.isfinite "Link to this definition")
:   Return `True` if *x* is neither an infinity nor a NaN, and
    `False` otherwise. (Note that `0.0` *is* considered finite.)

    Added in version 3.2.

math.isinf(*x*)[¶](#math.isinf "Link to this definition")
:   Return `True` if *x* is a positive or negative infinity, and
    `False` otherwise.

math.isnan(*x*)[¶](#math.isnan "Link to this definition")
:   Return `True` if *x* is a NaN (not a number), and `False` otherwise.

math.ldexp(*x*, *i*)[¶](#math.ldexp "Link to this definition")
:   Return `x * (2**i)`. This is essentially the inverse of function
    [`frexp()`](#math.frexp "math.frexp").

math.nextafter(*x*, *y*, *steps=1*)[¶](#math.nextafter "Link to this definition")
:   Return the floating-point value *steps* steps after *x* towards *y*.

    If *x* is equal to *y*, return *y*, unless *steps* is zero.

    Examples:

    * `math.nextafter(x, math.inf)` goes up: towards positive infinity.
    * `math.nextafter(x, -math.inf)` goes down: towards minus infinity.
    * `math.nextafter(x, 0.0)` goes towards zero.
    * `math.nextafter(x, math.copysign(math.inf, x))` goes away from zero.

    See also [`math.ulp()`](#math.ulp "math.ulp").

    Added in version 3.9.

    Changed in version 3.12: Added the *steps* argument.

math.ulp(*x*)[¶](#math.ulp "Link to this definition")
:   Return the value of the least significant bit of the float *x*:

    * If *x* is a NaN (not a number), return *x*.
    * If *x* is negative, return `ulp(-x)`.
    * If *x* is a positive infinity, return *x*.
    * If *x* is equal to zero, return the smallest positive
      *denormalized* representable float (smaller than the minimum positive
      *normalized* float, [`sys.float_info.min`](sys.html#sys.float_info "sys.float_info")).
    * If *x* is equal to the largest positive representable float,
      return the value of the least significant bit of *x*, such that the first
      float smaller than *x* is `x - ulp(x)`.
    * Otherwise (*x* is a positive finite number), return the value of the least
      significant bit of *x*, such that the first float bigger than *x*
      is `x + ulp(x)`.

    ULP stands for “Unit in the Last Place”.

    See also [`math.nextafter()`](#math.nextafter "math.nextafter") and [`sys.float_info.epsilon`](sys.html#sys.float_info "sys.float_info").

    Added in version 3.9.

## Power, exponential and logarithmic functions[¶](#power-exponential-and-logarithmic-functions "Link to this heading")

math.cbrt(*x*)[¶](#math.cbrt "Link to this definition")
:   Return the cube root of *x*.

    Added in version 3.11.

math.exp(*x*)[¶](#math.exp "Link to this definition")
:   Return *e* raised to the power *x*, where *e* = 2.718281… is the base
    of natural logarithms. This is usually more accurate than `math.e ** x`
    or `pow(math.e, x)`.

math.exp2(*x*)[¶](#math.exp2 "Link to this definition")
:   Return *2* raised to the power *x*.

    Added in version 3.11.

math.expm1(*x*)[¶](#math.expm1 "Link to this definition")
:   Return *e* raised to the power *x*, minus 1. Here *e* is the base of natural
    logarithms. For small floats *x*, the subtraction in `exp(x) - 1`
    can result in a [significant loss of precision](https://en.wikipedia.org/wiki/Loss_of_significance); the [`expm1()`](#math.expm1 "math.expm1")
    function provides a way to compute this quantity to full precision:

    ```
    >>> from math import exp, expm1
    >>> exp(1e-5) - 1  # gives result accurate to 11 places
    1.0000050000069649e-05
    >>> expm1(1e-5)    # result accurate to full precision
    1.0000050000166668e-05
    ```

    Added in version 3.2.

math.log(*x*[, *base*])[¶](#math.log "Link to this definition")
:   With one argument, return the natural logarithm of *x* (to base *e*).

    With two arguments, return the logarithm of *x* to the given *base*,
    calculated as `log(x)/log(base)`.

math.log1p(*x*)[¶](#math.log1p "Link to this definition")
:   Return the natural logarithm of *1+x* (base *e*). The
    result is calculated in a way which is accurate for *x* near zero.

math.log2(*x*)[¶](#math.log2 "Link to this definition")
:   Return the base-2 logarithm of *x*. This is usually more accurate than
    `log(x, 2)`.

    Added in version 3.3.

    See also

    [`int.bit_length()`](stdtypes.html#int.bit_length "int.bit_length") returns the number of bits necessary to represent
    an integer in binary, excluding the sign and leading zeros.

math.log10(*x*)[¶](#math.log10 "Link to this definition")
:   Return the base-10 logarithm of *x*. This is usually more accurate
    than `log(x, 10)`.

math.pow(*x*, *y*)[¶](#math.pow "Link to this definition")
:   Return *x* raised to the power *y*. Exceptional cases follow
    the IEEE 754 standard as far as possible. In particular,
    `pow(1.0, x)` and `pow(x, 0.0)` always return `1.0`, even
    when *x* is a zero or a NaN. If both *x* and *y* are finite,
    *x* is negative, and *y* is not an integer then `pow(x, y)`
    is undefined, and raises [`ValueError`](exceptions.html#ValueError "ValueError").

    Unlike the built-in `**` operator, [`math.pow()`](#math.pow "math.pow") converts both
    its arguments to type [`float`](functions.html#float "float"). Use `**` or the built-in
    [`pow()`](functions.html#pow "pow") function for computing exact integer powers.

    Changed in version 3.11: The special cases `pow(0.0, -inf)` and `pow(-0.0, -inf)` were
    changed to return `inf` instead of raising [`ValueError`](exceptions.html#ValueError "ValueError"),
    for consistency with IEEE 754.

math.sqrt(*x*)[¶](#math.sqrt "Link to this definition")
:   Return the square root of *x*.

## Summation and product functions[¶](#summation-and-product-functions "Link to this heading")

math.dist(*p*, *q*)[¶](#math.dist "Link to this definition")
:   Return the Euclidean distance between two points *p* and *q*, each
    given as a sequence (or iterable) of coordinates. The two points
    must have the same dimension.

    Roughly equivalent to:

    ```
    sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
    ```

    Added in version 3.8.

math.fsum(*iterable*)[¶](#math.fsum "Link to this definition")
:   Return an accurate floating-point sum of values in the iterable. Avoids
    loss of precision by tracking multiple intermediate partial sums.

    The algorithm’s accuracy depends on IEEE-754 arithmetic guarantees and the
    typical case where the rounding mode is half-even. On some non-Windows
    builds, the underlying C library uses extended precision addition and may
    occasionally double-round an intermediate sum causing it to be off in its
    least significant bit.

    For further discussion and two alternative approaches, see the [ASPN cookbook
    recipes for accurate floating-point summation](https://code.activestate.com/recipes/393090-binary-floating-point-summation-accurate-to-full-p/).

math.hypot(*\*coordinates*)[¶](#math.hypot "Link to this definition")
:   Return the Euclidean norm, `sqrt(sum(x**2 for x in coordinates))`.
    This is the length of the vector from the origin to the point
    given by the coordinates.

    For a two dimensional point `(x, y)`, this is equivalent to computing
    the hypotenuse of a right triangle using the Pythagorean theorem,
    `sqrt(x*x + y*y)`.

    Changed in version 3.8: Added support for n-dimensional points. Formerly, only the two
    dimensional case was supported.

    Changed in version 3.10: Improved the algorithm’s accuracy so that the maximum error is
    under 1 ulp (unit in the last place). More typically, the result
    is almost always correctly rounded to within 1/2 ulp.

math.prod(*iterable*, *\**, *start=1*)[¶](#math.prod "Link to this definition")
:   Calculate the product of all the elements in the input *iterable*.
    The default *start* value for the product is `1`.

    When the iterable is empty, return the start value. This function is
    intended specifically for use with numeric values and may reject
    non-numeric types.

    Added in version 3.8.

math.sumprod(*p*, *q*)[¶](#math.sumprod "Link to this definition")
:   Return the sum of products of values from two iterables *p* and *q*.

    Raises [`ValueError`](exceptions.html#ValueError "ValueError") if the inputs do not have the same length.

    Roughly equivalent to:

    ```
    sum(map(operator.mul, p, q, strict=True))
    ```

    For float and mixed int/float inputs, the intermediate products
    and sums are computed with extended precision.

    Added in version 3.12.

## Angular conversion[¶](#angular-conversion "Link to this heading")

math.degrees(*x*)[¶](#math.degrees "Link to this definition")
:   Convert angle *x* from radians to degrees.

math.radians(*x*)[¶](#math.radians "Link to this definition")
:   Convert angle *x* from degrees to radians.

## Trigonometric functions[¶](#trigonometric-functions "Link to this heading")

math.acos(*x*)[¶](#math.acos "Link to this definition")
:   Return the arc cosine of *x*, in radians. The result is between `0` and
    `pi`.

math.asin(*x*)[¶](#math.asin "Link to this definition")
:   Return the arc sine of *x*, in radians. The result is between `-pi/2` and
    `pi/2`.

math.atan(*x*)[¶](#math.atan "Link to this definition")
:   Return the arc tangent of *x*, in radians. The result is between `-pi/2` and
    `pi/2`.

math.atan2(*y*, *x*)[¶](#math.atan2 "Link to this definition")
:   Return `atan(y / x)`, in radians. The result is between `-pi` and `pi`.
    The vector in the plane from the origin to point `(x, y)` makes this angle
    with the positive X axis. The point of [`atan2()`](#math.atan2 "math.atan2") is that the signs of both
    inputs are known to it, so it can compute the correct quadrant for the angle.
    For example, `atan(1)` and `atan2(1, 1)` are both `pi/4`, but `atan2(-1,
    -1)` is `-3*pi/4`.

math.cos(*x*)[¶](#math.cos "Link to this definition")
:   Return the cosine of *x* radians.

math.sin(*x*)[¶](#math.sin "Link to this definition")
:   Return the sine of *x* radians.

math.tan(*x*)[¶](#math.tan "Link to this definition")
:   Return the tangent of *x* radians.

## Hyperbolic functions[¶](#hyperbolic-functions "Link to this heading")

[Hyperbolic functions](https://en.wikipedia.org/wiki/Hyperbolic_functions)
are analogs of trigonometric functions that are based on hyperbolas
instead of circles.

math.acosh(*x*)[¶](#math.acosh "Link to this definition")
:   Return the inverse hyperbolic cosine of *x*.

math.asinh(*x*)[¶](#math.asinh "Link to this definition")
:   Return the inverse hyperbolic sine of *x*.

math.atanh(*x*)[¶](#math.atanh "Link to this definition")
:   Return the inverse hyperbolic tangent of *x*.

math.cosh(*x*)[¶](#math.cosh "Link to this definition")
:   Return the hyperbolic cosine of *x*.

math.sinh(*x*)[¶](#math.sinh "Link to this definition")
:   Return the hyperbolic sine of *x*.

math.tanh(*x*)[¶](#math.tanh "Link to this definition")
:   Return the hyperbolic tangent of *x*.

## Special functions[¶](#special-functions "Link to this heading")

math.erf(*x*)[¶](#math.erf "Link to this definition")
:   Return the [error function](https://en.wikipedia.org/wiki/Error_function) at
    *x*.

    The [`erf()`](#math.erf "math.erf") function can be used to compute traditional statistical
    functions such as the [cumulative standard normal distribution](https://en.wikipedia.org/wiki/Cumulative_distribution_function):

    ```
    def phi(x):
        'Cumulative distribution function for the standard normal distribution'
        return (1.0 + erf(x / sqrt(2.0))) / 2.0
    ```

    Added in version 3.2.

math.erfc(*x*)[¶](#math.erfc "Link to this definition")
:   Return the complementary error function at *x*. The [complementary error
    function](https://en.wikipedia.org/wiki/Error_function) is defined as
    `1.0 - erf(x)`. It is used for large values of *x* where a subtraction
    from one would cause a [loss of significance](https://en.wikipedia.org/wiki/Loss_of_significance).

    Added in version 3.2.

math.gamma(*x*)[¶](#math.gamma "Link to this definition")
:   Return the [Gamma function](https://en.wikipedia.org/wiki/Gamma_function) at
    *x*.

    Added in version 3.2.

math.lgamma(*x*)[¶](#math.lgamma "Link to this definition")
:   Return the natural logarithm of the absolute value of the Gamma
    function at *x*.

    Added in version 3.2.

## Constants[¶](#constants "Link to this heading")

math.pi[¶](#math.pi "Link to this definition")
:   The mathematical constant *π* = 3.141592…, to available precision.

math.e[¶](#math.e "Link to this definition")
:   The mathematical constant *e* = 2.718281…, to available precision.

math.tau[¶](#math.tau "Link to this definition")
:   The mathematical constant *τ* = 6.283185…, to available precision.
    Tau is a circle constant equal to 2*π*, the ratio of a circle’s circumference to
    its radius. To learn more about Tau, check out Vi Hart’s video [Pi is (still)
    Wrong](https://vimeo.com/147792667), and start celebrating
    [Tau day](https://tauday.com/) by eating twice as much pie!

    Added in version 3.6.

math.inf[¶](#math.inf "Link to this definition")
:   A floating-point positive infinity. (For negative infinity, use
    `-math.inf`.) Equivalent to the output of `float('inf')`.

    Added in version 3.5.

math.nan[¶](#math.nan "Link to this definition")
:   A floating-point “not a number” (NaN) value. Equivalent to the output of
    `float('nan')`. Due to the requirements of the [IEEE-754 standard](https://en.wikipedia.org/wiki/IEEE_754), `math.nan` and `float('nan')` are
    not considered to equal to any other numeric value, including themselves. To check
    whether a number is a NaN, use the [`isnan()`](#math.isnan "math.isnan") function to test
    for NaNs instead of `is` or `==`.
    Example:

    ```
    >>> import math
    >>> math.nan == math.nan
    False
    >>> float('nan') == float('nan')
    False
    >>> math.isnan(math.nan)
    True
    >>> math.isnan(float('nan'))
    True
    ```

    Added in version 3.5.

    Changed in version 3.11: It is now always available.

**CPython implementation detail:** The `math` module consists mostly of thin wrappers around the platform C
math library functions. Behavior in exceptional cases follows Annex F of
the C99 standard where appropriate. The current implementation will raise
[`ValueError`](exceptions.html#ValueError "ValueError") for invalid operations like `sqrt(-1.0)` or `log(0.0)`
(where C99 Annex F recommends signaling invalid operation or divide-by-zero),
and [`OverflowError`](exceptions.html#OverflowError "OverflowError") for results that overflow (for example,
`exp(1000.0)`). A NaN will not be returned from any of the functions
above unless one or more of the input arguments was a NaN; in that case,
most functions will return a NaN, but (again following C99 Annex F) there
are some exceptions to this rule, for example `pow(float('nan'), 0.0)` or
`hypot(float('nan'), float('inf'))`.

Note that Python makes no effort to distinguish signaling NaNs from
quiet NaNs, and behavior for signaling NaNs remains unspecified.
Typical behavior is to treat all NaNs as though they were quiet.

See also

Module [`cmath`](cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.")
:   Complex number versions of many of these functions.

### [Table of Contents](../contents.html)

* [`math` — Mathematical functions](#)
  + [Number-theoretic functions](#number-theoretic-functions)
  + [Floating point arithmetic](#floating-point-arithmetic)
  + [Floating point manipulation functions](#floating-point-manipulation-functions)
  + [Power, exponential and logarithmic functions](#power-exponential-and-logarithmic-functions)
  + [Summation and product functions](#summation-and-product-functions)
  + [Angular conversion](#angular-conversion)
  + [Trigonometric functions](#trigonometric-functions)
  + [Hyperbolic functions](#hyperbolic-functions)
  + [Special functions](#special-functions)
  + [Constants](#constants)

#### Previous topic

[`numbers` — Numeric abstract base classes](numbers.html "previous chapter")

#### Next topic

[`cmath` — Mathematical functions for complex numbers](cmath.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/math.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](cmath.html "cmath — Mathematical functions for complex numbers") |
* [previous](numbers.html "numbers — Numeric abstract base classes") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Numeric and Mathematical Modules](numeric.html) »
* `math` — Mathematical functions
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
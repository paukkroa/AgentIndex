### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](numbers.html "numbers — Numeric abstract base classes") |
* [previous](graphlib.html "graphlib — Functionality to operate with graph-like structures") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Numeric and Mathematical Modules
* |
* Theme
  Auto
  Light
  Dark
   |

# Numeric and Mathematical Modules[¶](#numeric-and-mathematical-modules "Link to this heading")

The modules described in this chapter provide numeric and math-related functions
and data types. The [`numbers`](numbers.html#module-numbers "numbers: Numeric abstract base classes (Complex, Real, Integral, etc.).") module defines an abstract hierarchy of
numeric types. The [`math`](math.html#module-math "math: Mathematical functions (sin() etc.).") and [`cmath`](cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.") modules contain various
mathematical functions for floating-point and complex numbers. The [`decimal`](decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
module supports exact representations of decimal numbers, using arbitrary precision
arithmetic.

The following modules are documented in this chapter:

* [`numbers` — Numeric abstract base classes](numbers.html)
  + [The numeric tower](numbers.html#the-numeric-tower)
  + [Notes for type implementers](numbers.html#notes-for-type-implementers)
    - [Adding More Numeric ABCs](numbers.html#adding-more-numeric-abcs)
    - [Implementing the arithmetic operations](numbers.html#implementing-the-arithmetic-operations)
* [`math` — Mathematical functions](math.html)
  + [Number-theoretic functions](math.html#number-theoretic-functions)
  + [Floating point arithmetic](math.html#floating-point-arithmetic)
  + [Floating point manipulation functions](math.html#floating-point-manipulation-functions)
  + [Power, exponential and logarithmic functions](math.html#power-exponential-and-logarithmic-functions)
  + [Summation and product functions](math.html#summation-and-product-functions)
  + [Angular conversion](math.html#angular-conversion)
  + [Trigonometric functions](math.html#trigonometric-functions)
  + [Hyperbolic functions](math.html#hyperbolic-functions)
  + [Special functions](math.html#special-functions)
  + [Constants](math.html#constants)
* [`cmath` — Mathematical functions for complex numbers](cmath.html)
  + [Conversions to and from polar coordinates](cmath.html#conversions-to-and-from-polar-coordinates)
  + [Power and logarithmic functions](cmath.html#power-and-logarithmic-functions)
  + [Trigonometric functions](cmath.html#trigonometric-functions)
  + [Hyperbolic functions](cmath.html#hyperbolic-functions)
  + [Classification functions](cmath.html#classification-functions)
  + [Constants](cmath.html#constants)
* [`decimal` — Decimal fixed-point and floating-point arithmetic](decimal.html)
  + [Quick-start tutorial](decimal.html#quick-start-tutorial)
  + [Decimal objects](decimal.html#decimal-objects)
    - [Logical operands](decimal.html#logical-operands)
  + [Context objects](decimal.html#context-objects)
  + [Constants](decimal.html#constants)
  + [Rounding modes](decimal.html#rounding-modes)
  + [Signals](decimal.html#signals)
  + [Floating-point notes](decimal.html#floating-point-notes)
    - [Mitigating round-off error with increased precision](decimal.html#mitigating-round-off-error-with-increased-precision)
    - [Special values](decimal.html#special-values)
  + [Working with threads](decimal.html#working-with-threads)
  + [Recipes](decimal.html#recipes)
  + [Decimal FAQ](decimal.html#decimal-faq)
* [`fractions` — Rational numbers](fractions.html)
* [`random` — Generate pseudo-random numbers](random.html)
  + [Bookkeeping functions](random.html#bookkeeping-functions)
  + [Functions for bytes](random.html#functions-for-bytes)
  + [Functions for integers](random.html#functions-for-integers)
  + [Functions for sequences](random.html#functions-for-sequences)
  + [Discrete distributions](random.html#discrete-distributions)
  + [Real-valued distributions](random.html#real-valued-distributions)
  + [Alternative Generator](random.html#alternative-generator)
  + [Notes on Reproducibility](random.html#notes-on-reproducibility)
  + [Examples](random.html#examples)
  + [Recipes](random.html#recipes)
  + [Command-line usage](random.html#command-line-usage)
  + [Command-line example](random.html#command-line-example)
* [`statistics` — Mathematical statistics functions](statistics.html)
  + [Averages and measures of central location](statistics.html#averages-and-measures-of-central-location)
  + [Measures of spread](statistics.html#measures-of-spread)
  + [Statistics for relations between two inputs](statistics.html#statistics-for-relations-between-two-inputs)
  + [Function details](statistics.html#function-details)
  + [Exceptions](statistics.html#exceptions)
  + [`NormalDist` objects](statistics.html#normaldist-objects)
  + [Examples and Recipes](statistics.html#examples-and-recipes)
    - [Classic probability problems](statistics.html#classic-probability-problems)
    - [Monte Carlo inputs for simulations](statistics.html#monte-carlo-inputs-for-simulations)
    - [Approximating binomial distributions](statistics.html#approximating-binomial-distributions)
    - [Naive bayesian classifier](statistics.html#naive-bayesian-classifier)

#### Previous topic

[`graphlib` — Functionality to operate with graph-like structures](graphlib.html "previous chapter")

#### Next topic

[`numbers` — Numeric abstract base classes](numbers.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/numeric.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](numbers.html "numbers — Numeric abstract base classes") |
* [previous](graphlib.html "graphlib — Functionality to operate with graph-like structures") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Numeric and Mathematical Modules
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
### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](re.html "re — Regular expression operations") |
* [previous](string.html "string — Common string operations") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Text Processing Services](text.html) »
* `string.templatelib` — Support for template string literals
* |
* Theme
  Auto
  Light
  Dark
   |

# `string.templatelib` — Support for template string literals[¶](#module-string.templatelib "Link to this heading")

**Source code:** [Lib/string/templatelib.py](https://github.com/python/cpython/tree/3.14/Lib/string/templatelib.py)

---

See also

* [Format strings](../reference/lexical_analysis.html#f-strings)
* [Template string literal (t-string) syntax](../reference/lexical_analysis.html#t-strings)
* [**PEP 750**](https://peps.python.org/pep-0750/)

## Template strings[¶](#template-strings "Link to this heading")

Added in version 3.14.

Template strings are a mechanism for custom string processing.
They have the full flexibility of Python’s [f-strings](../reference/lexical_analysis.html#f-strings),
but return a [`Template`](#string.templatelib.Template "string.templatelib.Template") instance that gives access
to the static and interpolated (in curly brackets) parts of a string
*before* they are combined.

To write a t-string, use a `'t'` prefix instead of an `'f'`, like so:

```
>>> pi = 3.14
>>> t't-strings are new in Python {pi!s}!'
Template(
   strings=('t-strings are new in Python ', '!'),
   interpolations=(Interpolation(3.14, 'pi', 's', ''),)
)
```

## Types[¶](#types "Link to this heading")

*class* string.templatelib.Template[¶](#string.templatelib.Template "Link to this definition")
:   The `Template` class describes the contents of a template string.
    It is immutable, meaning that attributes of a template cannot be reassigned.

    The most common way to create a `Template` instance is to use the
    [template string literal syntax](../reference/lexical_analysis.html#t-strings).
    This syntax is identical to that of [f-strings](../reference/lexical_analysis.html#f-strings),
    except that it uses a `t` prefix in place of an `f`:

    ```
    >>> cheese = 'Red Leicester'
    >>> template = t"We're fresh out of {cheese}, sir."
    >>> type(template)
    <class 'string.templatelib.Template'>
    ```

    Templates are stored as sequences of literal [`strings`](#string.templatelib.Template.strings "string.templatelib.Template.strings")
    and dynamic [`interpolations`](#string.templatelib.Template.interpolations "string.templatelib.Template.interpolations").
    A [`values`](#string.templatelib.Template.values "string.templatelib.Template.values") attribute holds the values of the interpolations:

    ```
    >>> cheese = 'Camembert'
    >>> template = t'Ah! We do have {cheese}.'
    >>> template.strings
    ('Ah! We do have ', '.')
    >>> template.interpolations
    (Interpolation('Camembert', ...),)
    >>> template.values
    ('Camembert',)
    ```

    The `strings` tuple has one more element than `interpolations`
    and `values`; the interpolations “belong” between the strings.
    This may be easier to understand when tuples are aligned

    ```
    template.strings:  ('Ah! We do have ',              '.')
    template.values:   (                   'Camembert',    )
    ```

    Attributes

    strings*: [tuple](stdtypes.html#tuple "tuple")[[str](stdtypes.html#str "str"), ...]*[¶](#string.templatelib.Template.strings "Link to this definition")
    :   A [`tuple`](stdtypes.html#tuple "tuple") of the static strings in the template.

        ```
        >>> cheese = 'Camembert'
        >>> template = t'Ah! We do have {cheese}.'
        >>> template.strings
        ('Ah! We do have ', '.')
        ```

        Empty strings *are* included in the tuple:

        ```
        >>> response = 'We do have '
        >>> cheese = 'Camembert'
        >>> template = t'Ah! {response}{cheese}.'
        >>> template.strings
        ('Ah! ', '', '.')
        ```

        The `strings` tuple is never empty, and always contains one more
        string than the `interpolations` and `values` tuples:

        ```
        >>> t''.strings
        ('',)
        >>> t''.values
        ()
        >>> t'{'cheese'}'.strings
        ('', '')
        >>> t'{'cheese'}'.values
        ('cheese',)
        ```

    interpolations*: [tuple](stdtypes.html#tuple "tuple")[[Interpolation](#string.templatelib.Interpolation "string.templatelib.Interpolation"), ...]*[¶](#string.templatelib.Template.interpolations "Link to this definition")
    :   A [`tuple`](stdtypes.html#tuple "tuple") of the interpolations in the template.

        ```
        >>> cheese = 'Camembert'
        >>> template = t'Ah! We do have {cheese}.'
        >>> template.interpolations
        (Interpolation('Camembert', 'cheese', None, ''),)
        ```

        The `interpolations` tuple may be empty and always contains one fewer
        values than the `strings` tuple:

        ```
        >>> t'Red Leicester'.interpolations
        ()
        ```

    values*: [tuple](stdtypes.html#tuple "tuple")[[object](functions.html#object "object"), ...]*[¶](#string.templatelib.Template.values "Link to this definition")
    :   A tuple of all interpolated values in the template.

        ```
        >>> cheese = 'Camembert'
        >>> template = t'Ah! We do have {cheese}.'
        >>> template.values
        ('Camembert',)
        ```

        The `values` tuple always has the same length as the
        `interpolations` tuple. It is always equivalent to
        `tuple(i.value for i in template.interpolations)`.

    Methods

    \_\_new\_\_(*\*args: [str](stdtypes.html#str "str") | [Interpolation](#string.templatelib.Interpolation "string.templatelib.Interpolation")*)[¶](#string.templatelib.Template.__new__ "Link to this definition")
    :   While literal syntax is the most common way to create a `Template`,
        it is also possible to create them directly using the constructor:

        ```
        >>> from string.templatelib import Interpolation, Template
        >>> cheese = 'Camembert'
        >>> template = Template(
        ...     'Ah! We do have ', Interpolation(cheese, 'cheese'), '.'
        ... )
        >>> list(template)
        ['Ah! We do have ', Interpolation('Camembert', 'cheese', None, ''), '.']
        ```

        If multiple strings are passed consecutively, they will be concatenated
        into a single value in the [`strings`](#string.templatelib.Template.strings "string.templatelib.Template.strings") attribute. For example,
        the following code creates a [`Template`](#string.templatelib.Template "string.templatelib.Template") with a single final string:

        ```
        >>> from string.templatelib import Template
        >>> template = Template('Ah! We do have ', 'Camembert', '.')
        >>> template.strings
        ('Ah! We do have Camembert.',)
        ```

        If multiple interpolations are passed consecutively, they will be treated
        as separate interpolations and an empty string will be inserted between them.
        For example, the following code creates a template with empty placeholders
        in the [`strings`](#string.templatelib.Template.strings "string.templatelib.Template.strings") attribute:

        ```
        >>> from string.templatelib import Interpolation, Template
        >>> template = Template(
        ...     Interpolation('Camembert', 'cheese'),
        ...     Interpolation('.', 'punctuation'),
        ... )
        >>> template.strings
        ('', '', '')
        ```

    iter(template)
    :   Iterate over the template, yielding each non-empty string and
        [`Interpolation`](#string.templatelib.Interpolation "string.templatelib.Interpolation") in the correct order:

        ```
        >>> cheese = 'Camembert'
        >>> list(t'Ah! We do have {cheese}.')
        ['Ah! We do have ', Interpolation('Camembert', 'cheese', None, ''), '.']
        ```

        Caution

        Empty strings are **not** included in the iteration:

        ```
        >>> response = 'We do have '
        >>> cheese = 'Camembert'
        >>> list(t'Ah! {response}{cheese}.')
        ['Ah! ',
         Interpolation('We do have ', 'response', None, ''),
         Interpolation('Camembert', 'cheese', None, ''),
         '.']
        ```

    template + other

    template += other
    :   Concatenate this template with another, returning a new
        `Template` instance:

        ```
        >>> cheese = 'Camembert'
        >>> list(t'Ah! ' + t'We do have {cheese}.')
        ['Ah! We do have ', Interpolation('Camembert', 'cheese', None, ''), '.']
        ```

        Concatenating a `Template` and a `str` is **not** supported.
        This is because it is unclear whether the string should be treated as
        a static string or an interpolation.
        If you want to concatenate a `Template` with a string,
        you should either wrap the string directly in a `Template`
        (to treat it as a static string)
        or use an `Interpolation` (to treat it as dynamic):

        ```
        >>> from string.templatelib import Interpolation, Template
        >>> template = t'Ah! '
        >>> # Treat 'We do have ' as a static string
        >>> template += Template('We do have ')
        >>> # Treat cheese as an interpolation
        >>> cheese = 'Camembert'
        >>> template += Template(Interpolation(cheese, 'cheese'))
        >>> list(template)
        ['Ah! We do have ', Interpolation('Camembert', 'cheese', None, '')]
        ```

*class* string.templatelib.Interpolation[¶](#string.templatelib.Interpolation "Link to this definition")
:   The `Interpolation` type represents an expression inside a template string.
    It is immutable, meaning that attributes of an interpolation cannot be reassigned.

    Interpolations support pattern matching, allowing you to match against
    their attributes with the [match statement](../reference/compound_stmts.html#match):

    ```
    >>> from string.templatelib import Interpolation
    >>> interpolation = t'{1. + 2.:.2f}'.interpolations[0]
    >>> interpolation
    Interpolation(3.0, '1. + 2.', None, '.2f')
    >>> match interpolation:
    ...     case Interpolation(value, expression, conversion, format_spec):
    ...         print(value, expression, conversion, format_spec, sep=' | ')
    ...
    3.0 | 1. + 2. | None | .2f
    ```

    Attributes

    value*: [object](functions.html#object "object")*[¶](#string.templatelib.Interpolation.value "Link to this definition")
    :   The evaluated value of the interpolation.

        ```
        >>> t'{1 + 2}'.interpolations[0].value
        3
        ```

    expression*: [str](stdtypes.html#str "str")*[¶](#string.templatelib.Interpolation.expression "Link to this definition")
    :   For interpolations created by t-string literals, `expression`
        is the expression text found inside the curly brackets (`{` & `}`),
        including any whitespace, excluding the curly brackets themselves,
        and ending before the first `!`, `:`, or `=` if any is present.
        For manually created interpolations, `expression` is the arbitrary
        string provided when constructing the interpolation instance.

        We recommend using valid Python expressions or the empty string for the
        `expression` field of manually created `Interpolation`
        instances, although this is not enforced at runtime.

        ```
        >>> t'{1 + 2}'.interpolations[0].expression
        '1 + 2'
        ```

    conversion*: [Literal](typing.html#typing.Literal "typing.Literal")['a', 'r', 's'] | [None](constants.html#None "None")*[¶](#string.templatelib.Interpolation.conversion "Link to this definition")
    :   The conversion to apply to the value, or `None`.

        The `conversion` is the optional conversion to apply
        to the value:

        ```
        >>> t'{1 + 2!a}'.interpolations[0].conversion
        'a'
        ```

        Note

        Unlike f-strings, where conversions are applied automatically,
        the expected behavior with t-strings is that code that *processes* the
        `Template` will decide how to interpret and whether to apply
        the `conversion`.
        For convenience, the [`convert()`](#string.templatelib.convert "string.templatelib.convert") function can be used to mimic
        f-string conversion semantics.

    format\_spec*: [str](stdtypes.html#str "str")*[¶](#string.templatelib.Interpolation.format_spec "Link to this definition")
    :   The format specification to apply to the value.

        The `format_spec` is an optional, arbitrary string
        used as the format specification to present the value:

        ```
        >>> t'{1 + 2:.2f}'.interpolations[0].format_spec
        '.2f'
        ```

        Note

        Unlike f-strings, where format specifications are applied automatically
        via the [`format()`](functions.html#format "format") protocol, the expected behavior with
        t-strings is that code that *processes* the interpolation will
        decide how to interpret and whether to apply the format specification.
        As a result, `format_spec` values in interpolations
        can be arbitrary strings,
        including those that do not conform to the [`format()`](functions.html#format "format") protocol.

    Methods

    \_\_new\_\_(*value: [object](functions.html#object "object")*, *expression: [str](stdtypes.html#str "str")*, *conversion: [Literal](typing.html#typing.Literal "typing.Literal")['a', 'r', 's'] | [None](constants.html#None "None") = None*, *format\_spec: [str](stdtypes.html#str "str") = ''*)[¶](#string.templatelib.Interpolation.__new__ "Link to this definition")
    :   Create a new `Interpolation` object from component parts.

        Parameters:
        :   * **value** – The evaluated, in-scope result of the interpolation.
            * **expression** – The text of a valid Python expression,
              or an empty string.
            * **conversion** – The [conversion](string.html#formatstrings) to be used,
              one of `None`, `'a'`, `'r'`, or `'s'`.
            * **format\_spec** – An optional, arbitrary string used as the
              [format specification](string.html#formatspec) to present the value.

## Helper functions[¶](#helper-functions "Link to this heading")

string.templatelib.convert(*obj*, */*, *conversion*)[¶](#string.templatelib.convert "Link to this definition")
:   Applies formatted string literal [conversion](string.html#formatstrings-conversion)
    semantics to the given object *obj*.
    This is frequently useful for custom template string processing logic.

    Three conversion flags are currently supported:

    * `'s'` which calls [`str()`](stdtypes.html#str "str") on the value (like `!s`),
    * `'r'` which calls [`repr()`](functions.html#repr "repr") (like `!r`), and
    * `'a'` which calls [`ascii()`](functions.html#ascii "ascii") (like `!a`).

    If the conversion flag is `None`, *obj* is returned unchanged.

### [Table of Contents](../contents.html)

* [`string.templatelib` — Support for template string literals](#)
  + [Template strings](#template-strings)
  + [Types](#types)
  + [Helper functions](#helper-functions)

#### Previous topic

[`string` — Common string operations](string.html "previous chapter")

#### Next topic

[`re` — Regular expression operations](re.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/string.templatelib.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](re.html "re — Regular expression operations") |
* [previous](string.html "string — Common string operations") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Text Processing Services](text.html) »
* `string.templatelib` — Support for template string literals
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
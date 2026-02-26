### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](stringprep.html "stringprep — Internet String Preparation") |
* [previous](textwrap.html "textwrap — Text wrapping and filling") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Text Processing Services](text.html) »
* `unicodedata` — Unicode Database
* |
* Theme
  Auto
  Light
  Dark
   |

# `unicodedata` — Unicode Database[¶](#module-unicodedata "Link to this heading")

---

This module provides access to the Unicode Character Database (UCD) which
defines character properties for all Unicode characters. The data contained in
this database is compiled from the [UCD version 16.0.0](https://www.unicode.org/Public/16.0.0/ucd).

The module uses the same names and symbols as defined by Unicode
Standard Annex #44, [“Unicode Character Database”](https://www.unicode.org/reports/tr44/). It defines the
following functions:

See also

The [Unicode HOWTO](../howto/unicode.html#unicode-howto) for more information about Unicode and how to use
this module.

unicodedata.lookup(*name*)[¶](#unicodedata.lookup "Link to this definition")
:   Look up character by name. If a character with the given name is found, return
    the corresponding character. If not found, [`KeyError`](exceptions.html#KeyError "KeyError") is raised.
    For example:

    ```
    >>> unicodedata.lookup('LEFT CURLY BRACKET')
    '{'
    ```

    The characters returned by this function are the same as those produced by
    `\N` escape sequence in string literals. For example:

    ```
    >>> unicodedata.lookup('MIDDLE DOT') == '\N{MIDDLE DOT}'
    True
    ```

    Changed in version 3.3: Support for name aliases [[1]](#id3) and named sequences [[2]](#id4) has been added.

unicodedata.name(*chr*, *default=None*, */*)[¶](#unicodedata.name "Link to this definition")
:   Returns the name assigned to the character *chr* as a string. If no
    name is defined, *default* is returned, or, if not given, [`ValueError`](exceptions.html#ValueError "ValueError") is
    raised. For example:

    ```
    >>> unicodedata.name('½')
    'VULGAR FRACTION ONE HALF'
    >>> unicodedata.name('\uFFFF', 'fallback')
    'fallback'
    ```

unicodedata.decimal(*chr*, *default=None*, */*)[¶](#unicodedata.decimal "Link to this definition")
:   Returns the decimal value assigned to the character *chr* as integer.
    If no such value is defined, *default* is returned, or, if not given,
    [`ValueError`](exceptions.html#ValueError "ValueError") is raised. For example:

    ```
    >>> unicodedata.decimal('\N{ARABIC-INDIC DIGIT NINE}')
    9
    >>> unicodedata.decimal('\N{SUPERSCRIPT NINE}', -1)
    -1
    ```

unicodedata.digit(*chr*, *default=None*, */*)[¶](#unicodedata.digit "Link to this definition")
:   Returns the digit value assigned to the character *chr* as integer.
    If no such value is defined, *default* is returned, or, if not given,
    [`ValueError`](exceptions.html#ValueError "ValueError") is raised:

    ```
    >>> unicodedata.digit('\N{SUPERSCRIPT NINE}')
    9
    ```

unicodedata.numeric(*chr*, *default=None*, */*)[¶](#unicodedata.numeric "Link to this definition")
:   Returns the numeric value assigned to the character *chr* as float.
    If no such value is defined, *default* is returned, or, if not given,
    [`ValueError`](exceptions.html#ValueError "ValueError") is raised:

    ```
    >>> unicodedata.numeric('½')
    0.5
    ```

unicodedata.category(*chr*)[¶](#unicodedata.category "Link to this definition")
:   Returns the general category assigned to the character *chr* as
    string. General category names consist of two letters.
    See the [General Category Values section of the Unicode Character
    Database documentation](https://www.unicode.org/reports/tr44/tr44-34.html#General_Category_Values)
    for a list of category codes. For example:

    ```
    >>> unicodedata.category('A')  # 'L'etter, 'u'ppercase
    'Lu'
    ```

unicodedata.bidirectional(*chr*)[¶](#unicodedata.bidirectional "Link to this definition")
:   Returns the bidirectional class assigned to the character *chr* as
    string. If no such value is defined, an empty string is returned.
    See the [Bidirectional Class Values section of the Unicode Character
    Database](https://www.unicode.org/reports/tr44/tr44-34.html#Bidi_Class_Values)
    documentation for a list of bidirectional codes. For example:

    ```
    >>> unicodedata.bidirectional('\N{ARABIC-INDIC DIGIT SEVEN}') # 'A'rabic, 'N'umber
    'AN'
    ```

unicodedata.combining(*chr*)[¶](#unicodedata.combining "Link to this definition")
:   Returns the canonical combining class assigned to the character *chr*
    as integer. Returns `0` if no combining class is defined.
    See the [Canonical Combining Class Values section of the Unicode Character
    Database](https://www.unicode.org/reports/tr44/tr44-34.html#Canonical_Combining_Class_Values)
    for more information.

unicodedata.east\_asian\_width(*chr*)[¶](#unicodedata.east_asian_width "Link to this definition")
:   Returns the east asian width assigned to the character *chr* as
    string. For a list of widths and or more information, see the
    [Unicode Standard Annex #11](https://www.unicode.org/reports/tr11/tr11-43.html).

unicodedata.mirrored(*chr*)[¶](#unicodedata.mirrored "Link to this definition")
:   Returns the mirrored property assigned to the character *chr* as
    integer. Returns `1` if the character has been identified as a “mirrored”
    character in bidirectional text, `0` otherwise. For example:

    ```
    >>> unicodedata.mirrored('>')
    1
    ```

unicodedata.decomposition(*chr*)[¶](#unicodedata.decomposition "Link to this definition")
:   Returns the character decomposition mapping assigned to the character
    *chr* as string. An empty string is returned in case no such mapping is
    defined. For example:

    ```
    >>> unicodedata.decomposition('Ã')
    '0041 0303'
    ```

unicodedata.normalize(*form*, *unistr*)[¶](#unicodedata.normalize "Link to this definition")
:   Return the normal form *form* for the Unicode string *unistr*. Valid values for
    *form* are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.

    The Unicode standard defines various normalization forms of a Unicode string,
    based on the definition of canonical equivalence and compatibility equivalence.
    In Unicode, several characters can be expressed in various way. For example, the
    character U+00C7 (LATIN CAPITAL LETTER C WITH CEDILLA) can also be expressed as
    the sequence U+0043 (LATIN CAPITAL LETTER C) U+0327 (COMBINING CEDILLA).

    For each character, there are two normal forms: normal form C and normal form D.
    Normal form D (NFD) is also known as canonical decomposition, and translates
    each character into its decomposed form. Normal form C (NFC) first applies a
    canonical decomposition, then composes pre-combined characters again.

    In addition to these two forms, there are two additional normal forms based on
    compatibility equivalence. In Unicode, certain characters are supported which
    normally would be unified with other characters. For example, U+2160 (ROMAN
    NUMERAL ONE) is really the same thing as U+0049 (LATIN CAPITAL LETTER I).
    However, it is supported in Unicode for compatibility with existing character
    sets (for example, gb2312).

    The normal form KD (NFKD) will apply the compatibility decomposition, that is,
    replace all compatibility characters with their equivalents. The normal form KC
    (NFKC) first applies the compatibility decomposition, followed by the canonical
    composition.

    Even if two unicode strings are normalized and look the same to
    a human reader, if one has combining characters and the other
    doesn’t, they may not compare equal.

unicodedata.is\_normalized(*form*, *unistr*)[¶](#unicodedata.is_normalized "Link to this definition")
:   Return whether the Unicode string *unistr* is in the normal form *form*. Valid
    values for *form* are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.

    Added in version 3.8.

In addition, the module exposes the following constant:

unicodedata.unidata\_version[¶](#unicodedata.unidata_version "Link to this definition")
:   The version of the Unicode database used in this module.

unicodedata.ucd\_3\_2\_0[¶](#unicodedata.ucd_3_2_0 "Link to this definition")
:   This is an object that has the same methods as the entire module, but uses the
    Unicode database version 3.2 instead, for applications that require this
    specific version of the Unicode database (such as IDNA).

Footnotes

[[1](#id1)]

<https://www.unicode.org/Public/16.0.0/ucd/NameAliases.txt>


[[2](#id2)]

<https://www.unicode.org/Public/16.0.0/ucd/NamedSequences.txt>

#### Previous topic

[`textwrap` — Text wrapping and filling](textwrap.html "previous chapter")

#### Next topic

[`stringprep` — Internet String Preparation](stringprep.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/unicodedata.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](stringprep.html "stringprep — Internet String Preparation") |
* [previous](textwrap.html "textwrap — Text wrapping and filling") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Text Processing Services](text.html) »
* `unicodedata` — Unicode Database
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
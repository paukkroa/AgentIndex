### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](xml.html "XML Processing Modules") |
* [previous](html.parser.html "html.parser — Simple HTML and XHTML parser") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* `html.entities` — Definitions of HTML general entities
* |
* Theme
  Auto
  Light
  Dark
   |

# `html.entities` — Definitions of HTML general entities[¶](#module-html.entities "Link to this heading")

**Source code:** [Lib/html/entities.py](https://github.com/python/cpython/tree/3.14/Lib/html/entities.py)

---

This module defines four dictionaries, [`html5`](#html.entities.html5 "html.entities.html5"),
[`name2codepoint`](#html.entities.name2codepoint "html.entities.name2codepoint"), [`codepoint2name`](#html.entities.codepoint2name "html.entities.codepoint2name"), and [`entitydefs`](#html.entities.entitydefs "html.entities.entitydefs").

html.entities.html5[¶](#html.entities.html5 "Link to this definition")
:   A dictionary that maps HTML5 named character references [[1]](#id2) to the
    equivalent Unicode character(s), e.g. `html5['gt;'] == '>'`.
    Note that the trailing semicolon is included in the name (e.g. `'gt;'`),
    however some of the names are accepted by the standard even without the
    semicolon: in this case the name is present with and without the `';'`.
    See also [`html.unescape()`](html.html#html.unescape "html.unescape").

    Added in version 3.3.

html.entities.entitydefs[¶](#html.entities.entitydefs "Link to this definition")
:   A dictionary mapping XHTML 1.0 entity definitions to their replacement text in
    ISO Latin-1.

html.entities.name2codepoint[¶](#html.entities.name2codepoint "Link to this definition")
:   A dictionary that maps HTML4 entity names to the Unicode code points.

html.entities.codepoint2name[¶](#html.entities.codepoint2name "Link to this definition")
:   A dictionary that maps Unicode code points to HTML4 entity names.

Footnotes

[[1](#id1)]

See <https://html.spec.whatwg.org/multipage/named-characters.html#named-character-references>

#### Previous topic

[`html.parser` — Simple HTML and XHTML parser](html.parser.html "previous chapter")

#### Next topic

[XML Processing Modules](xml.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/html.entities.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](xml.html "XML Processing Modules") |
* [previous](html.parser.html "html.parser — Simple HTML and XHTML parser") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* `html.entities` — Definitions of HTML general entities
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
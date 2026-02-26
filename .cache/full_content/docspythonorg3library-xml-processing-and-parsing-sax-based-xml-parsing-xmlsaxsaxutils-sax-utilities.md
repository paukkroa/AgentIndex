### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](xml.sax.reader.html "xml.sax.xmlreader — Interface for XML parsers") |
* [previous](xml.sax.handler.html "xml.sax.handler — Base classes for SAX handlers") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* `xml.sax.saxutils` — SAX Utilities
* |
* Theme
  Auto
  Light
  Dark
   |

# `xml.sax.saxutils` — SAX Utilities[¶](#module-xml.sax.saxutils "Link to this heading")

**Source code:** [Lib/xml/sax/saxutils.py](https://github.com/python/cpython/tree/3.14/Lib/xml/sax/saxutils.py)

---

The module `xml.sax.saxutils` contains a number of classes and functions
that are commonly useful when creating SAX applications, either in direct use,
or as base classes.

xml.sax.saxutils.escape(*data*, *entities={}*)[¶](#xml.sax.saxutils.escape "Link to this definition")
:   Escape `'&'`, `'<'`, and `'>'` in a string of data.

    You can escape other strings of data by passing a dictionary as the optional
    *entities* parameter. The keys and values must all be strings; each key will be
    replaced with its corresponding value. The characters `'&'`, `'<'` and
    `'>'` are always escaped, even if *entities* is provided.

    Note

    This function should only be used to escape characters that
    can’t be used directly in XML. Do not use this function as a general
    string translation function.

xml.sax.saxutils.unescape(*data*, *entities={}*)[¶](#xml.sax.saxutils.unescape "Link to this definition")
:   Unescape `'&amp;'`, `'&lt;'`, and `'&gt;'` in a string of data.

    You can unescape other strings of data by passing a dictionary as the optional
    *entities* parameter. The keys and values must all be strings; each key will be
    replaced with its corresponding value. `'&amp;'`, `'&lt;'`, and `'&gt;'`
    are always unescaped, even if *entities* is provided.

xml.sax.saxutils.quoteattr(*data*, *entities={}*)[¶](#xml.sax.saxutils.quoteattr "Link to this definition")
:   Similar to [`escape()`](#xml.sax.saxutils.escape "xml.sax.saxutils.escape"), but also prepares *data* to be used as an
    attribute value. The return value is a quoted version of *data* with any
    additional required replacements. [`quoteattr()`](#xml.sax.saxutils.quoteattr "xml.sax.saxutils.quoteattr") will select a quote
    character based on the content of *data*, attempting to avoid encoding any
    quote characters in the string. If both single- and double-quote characters
    are already in *data*, the double-quote characters will be encoded and *data*
    will be wrapped in double-quotes. The resulting string can be used directly
    as an attribute value:

    ```
    >>> print("<element attr=%s>" % quoteattr("ab ' cd \" ef"))
    <element attr="ab ' cd &quot; ef">
    ```

    This function is useful when generating attribute values for HTML or any SGML
    using the reference concrete syntax.

*class* xml.sax.saxutils.XMLGenerator(*out=None*, *encoding='iso-8859-1'*, *short\_empty\_elements=False*)[¶](#xml.sax.saxutils.XMLGenerator "Link to this definition")
:   This class implements the [`ContentHandler`](xml.sax.handler.html#xml.sax.handler.ContentHandler "xml.sax.handler.ContentHandler") interface
    by writing SAX
    events back into an XML document. In other words, using an [`XMLGenerator`](#xml.sax.saxutils.XMLGenerator "xml.sax.saxutils.XMLGenerator")
    as the content handler will reproduce the original document being parsed. *out*
    should be a file-like object which will default to *sys.stdout*. *encoding* is
    the encoding of the output stream which defaults to `'iso-8859-1'`.
    *short\_empty\_elements* controls the formatting of elements that contain no
    content: if `False` (the default) they are emitted as a pair of start/end
    tags, if set to `True` they are emitted as a single self-closed tag.

    Changed in version 3.2: Added the *short\_empty\_elements* parameter.

*class* xml.sax.saxutils.XMLFilterBase(*base*)[¶](#xml.sax.saxutils.XMLFilterBase "Link to this definition")
:   This class is designed to sit between an
    [`XMLReader`](xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") and the client
    application’s event handlers. By default, it does nothing but pass requests up
    to the reader and events on to the handlers unmodified, but subclasses can
    override specific methods to modify the event stream or the configuration
    requests as they pass through.

xml.sax.saxutils.prepare\_input\_source(*source*, *base=''*)[¶](#xml.sax.saxutils.prepare_input_source "Link to this definition")
:   This function takes an input source and an optional base URL and returns a
    fully resolved [`InputSource`](xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource") object ready for
    reading. The input source can be given as a string, a file-like object, or
    an [`InputSource`](xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource") object; parsers will use this
    function to implement the polymorphic *source* argument to their
    [`parse()`](xml.sax.reader.html#xml.sax.xmlreader.XMLReader.parse "xml.sax.xmlreader.XMLReader.parse") method.

#### Previous topic

[`xml.sax.handler` — Base classes for SAX handlers](xml.sax.handler.html "previous chapter")

#### Next topic

[`xml.sax.xmlreader` — Interface for XML parsers](xml.sax.reader.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/xml.sax.utils.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](xml.sax.reader.html "xml.sax.xmlreader — Interface for XML parsers") |
* [previous](xml.sax.handler.html "xml.sax.handler — Base classes for SAX handlers") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* `xml.sax.saxutils` — SAX Utilities
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
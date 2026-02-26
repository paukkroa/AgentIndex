### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](xml.etree.elementtree.html "xml.etree.ElementTree — The ElementTree XML API") |
* [previous](html.entities.html "html.entities — Definitions of HTML general entities") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* XML Processing Modules
* |
* Theme
  Auto
  Light
  Dark
   |

# XML Processing Modules[¶](#module-xml "Link to this heading")

**Source code:** [Lib/xml/](https://github.com/python/cpython/tree/3.14/Lib/xml/)

---

Python’s interfaces for processing XML are grouped in the `xml` package.

Note

If you need to parse untrusted or unauthenticated data, see
[XML security](#xml-security).

It is important to note that modules in the `xml` package require that
there be at least one SAX-compliant XML parser available. The Expat parser is
included with Python, so the [`xml.parsers.expat`](pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.") module will always be
available.

The documentation for the [`xml.dom`](xml.dom.html#module-xml.dom "xml.dom: Document Object Model API for Python.") and [`xml.sax`](xml.sax.html#module-xml.sax "xml.sax: Package containing SAX2 base classes and convenience functions.") packages are the
definition of the Python bindings for the DOM and SAX interfaces.

The XML handling submodules are:

* [`xml.etree.ElementTree`](xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API."): the ElementTree API, a simple and lightweight
  XML processor

* [`xml.dom`](xml.dom.html#module-xml.dom "xml.dom: Document Object Model API for Python."): the DOM API definition
* [`xml.dom.minidom`](xml.dom.minidom.html#module-xml.dom.minidom "xml.dom.minidom: Minimal Document Object Model (DOM) implementation."): a minimal DOM implementation
* [`xml.dom.pulldom`](xml.dom.pulldom.html#module-xml.dom.pulldom "xml.dom.pulldom: Support for building partial DOM trees from SAX events."): support for building partial DOM trees

* [`xml.sax`](xml.sax.html#module-xml.sax "xml.sax: Package containing SAX2 base classes and convenience functions."): SAX2 base classes and convenience functions
* [`xml.parsers.expat`](pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser."): the Expat parser binding

## XML security[¶](#xml-vulnerabilities "Link to this heading")

An attacker can abuse XML features to carry out denial of service attacks,
access local files, generate network connections to other machines, or
circumvent firewalls when attacker-controlled XML is being parsed,
in Python or elsewhere.

The built-in XML parsers of Python rely on the library [libexpat](https://github.com/libexpat/libexpat), commonly
called Expat, for parsing XML.

By default, Expat itself does not access local files or create network
connections.

Expat versions lower than 2.7.2 may be vulnerable to the “billion laughs”,
“quadratic blowup” and “large tokens” vulnerabilities, or to disproportional
use of dynamic memory.
Python bundles a copy of Expat, and whether Python uses the bundled or a
system-wide Expat, depends on how the Python interpreter
[`has been configured`](../using/configure.html#cmdoption-with-system-expat) in your environment.
Python may be vulnerable if it uses such older versions of Expat.
Check `pyexpat.EXPAT_VERSION`.

[`xmlrpc`](xmlrpc.html#module-xmlrpc "xmlrpc: Server and client modules implementing XML-RPC.") is **vulnerable** to the “decompression bomb” attack.

billion laughs / exponential entity expansion
:   The [Billion Laughs](https://en.wikipedia.org/wiki/Billion_laughs) attack – also known as exponential entity expansion –
    uses multiple levels of nested entities. Each entity refers to another entity
    several times, and the final entity definition contains a small string.
    The exponential expansion results in several gigabytes of text and
    consumes lots of memory and CPU time.

quadratic blowup entity expansion
:   A quadratic blowup attack is similar to a [Billion Laughs](https://en.wikipedia.org/wiki/Billion_laughs) attack; it abuses
    entity expansion, too. Instead of nested entities it repeats one large entity
    with a couple of thousand chars over and over again. The attack isn’t as
    efficient as the exponential case but it avoids triggering parser countermeasures
    that forbid deeply nested entities.

decompression bomb
:   Decompression bombs (aka [ZIP bomb](https://en.wikipedia.org/wiki/Zip_bomb)) apply to all XML libraries
    that can parse compressed XML streams such as gzipped HTTP streams or
    LZMA-compressed
    files. For an attacker it can reduce the amount of transmitted data by three
    magnitudes or more.

large tokens
:   Expat needs to re-parse unfinished tokens; without the protection
    introduced in Expat 2.6.0, this can lead to quadratic runtime that can
    be used to cause denial of service in the application parsing XML.
    The issue is known as [**CVE 2023-52425**](https://www.cve.org/CVERecord?id=CVE-2023-52425).

### [Table of Contents](../contents.html)

* [XML Processing Modules](#)
  + [XML security](#xml-vulnerabilities)

#### Previous topic

[`html.entities` — Definitions of HTML general entities](html.entities.html "previous chapter")

#### Next topic

[`xml.etree.ElementTree` — The ElementTree XML API](xml.etree.elementtree.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/xml.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](xml.etree.elementtree.html "xml.etree.ElementTree — The ElementTree XML API") |
* [previous](html.entities.html "html.entities — Definitions of HTML general entities") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* XML Processing Modules
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
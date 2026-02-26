### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](xml.sax.handler.html "xml.sax.handler — Base classes for SAX handlers") |
* [previous](xml.dom.pulldom.html "xml.dom.pulldom — Support for building partial DOM trees") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* `xml.sax` — Support for SAX2 parsers
* |
* Theme
  Auto
  Light
  Dark
   |

# `xml.sax` — Support for SAX2 parsers[¶](#module-xml.sax "Link to this heading")

**Source code:** [Lib/xml/sax/\_\_init\_\_.py](https://github.com/python/cpython/tree/3.14/Lib/xml/sax/__init__.py)

---

The `xml.sax` package provides a number of modules which implement the
Simple API for XML (SAX) interface for Python. The package itself provides the
SAX exceptions and the convenience functions which will be most used by users of
the SAX API.

Note

If you need to parse untrusted or unauthenticated data, see
[XML security](xml.html#xml-security).

Changed in version 3.7.1: The SAX parser no longer processes general external entities by default
to increase security. Before, the parser created network connections
to fetch remote files or loaded local files from the file
system for DTD and entities. The feature can be enabled again with method
[`setFeature()`](xml.sax.reader.html#xml.sax.xmlreader.XMLReader.setFeature "xml.sax.xmlreader.XMLReader.setFeature") on the parser object
and argument [`feature_external_ges`](xml.sax.handler.html#xml.sax.handler.feature_external_ges "xml.sax.handler.feature_external_ges").

The convenience functions are:

xml.sax.make\_parser(*parser\_list=[]*)[¶](#xml.sax.make_parser "Link to this definition")
:   Create and return a SAX [`XMLReader`](xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") object. The
    first parser found will
    be used. If *parser\_list* is provided, it must be an iterable of strings which
    name modules that have a function named `create_parser()`. Modules listed
    in *parser\_list* will be used before modules in the default list of parsers.

    Changed in version 3.8: The *parser\_list* argument can be any iterable, not just a list.

xml.sax.parse(*filename\_or\_stream*, *handler*, *error\_handler=handler.ErrorHandler()*)[¶](#xml.sax.parse "Link to this definition")
:   Create a SAX parser and use it to parse a document. The document, passed in as
    *filename\_or\_stream*, can be a filename or a file object. The *handler*
    parameter needs to be a SAX [`ContentHandler`](xml.sax.handler.html#xml.sax.handler.ContentHandler "xml.sax.handler.ContentHandler") instance. If
    *error\_handler* is given, it must be a SAX [`ErrorHandler`](xml.sax.handler.html#xml.sax.handler.ErrorHandler "xml.sax.handler.ErrorHandler")
    instance; if
    omitted, [`SAXParseException`](#xml.sax.SAXParseException "xml.sax.SAXParseException") will be raised on all errors. There is no
    return value; all work must be done by the *handler* passed in.

xml.sax.parseString(*string*, *handler*, *error\_handler=handler.ErrorHandler()*)[¶](#xml.sax.parseString "Link to this definition")
:   Similar to [`parse()`](#xml.sax.parse "xml.sax.parse"), but parses from a buffer *string* received as a
    parameter. *string* must be a [`str`](stdtypes.html#str "str") instance or a
    [bytes-like object](../glossary.html#term-bytes-like-object).

    Changed in version 3.5: Added support of [`str`](stdtypes.html#str "str") instances.

A typical SAX application uses three kinds of objects: readers, handlers and
input sources. “Reader” in this context is another term for parser, i.e. some
piece of code that reads the bytes or characters from the input source, and
produces a sequence of events. The events then get distributed to the handler
objects, i.e. the reader invokes a method on the handler. A SAX application
must therefore obtain a reader object, create or open the input sources, create
the handlers, and connect these objects all together. As the final step of
preparation, the reader is called to parse the input. During parsing, methods on
the handler objects are called based on structural and syntactic events from the
input data.

For these objects, only the interfaces are relevant; they are normally not
instantiated by the application itself. Since Python does not have an explicit
notion of interface, they are formally introduced as classes, but applications
may use implementations which do not inherit from the provided classes. The
[`InputSource`](xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource"), [`Locator`](xml.sax.reader.html#xml.sax.xmlreader.Locator "xml.sax.xmlreader.Locator"),
`Attributes`, `AttributesNS`,
and [`XMLReader`](xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") interfaces are defined in the
module [`xml.sax.xmlreader`](xml.sax.reader.html#module-xml.sax.xmlreader "xml.sax.xmlreader: Interface which SAX-compliant XML parsers must implement."). The handler interfaces are defined in
[`xml.sax.handler`](xml.sax.handler.html#module-xml.sax.handler "xml.sax.handler: Base classes for SAX event handlers."). For convenience,
[`InputSource`](xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource") (which is often
instantiated directly) and the handler classes are also available from
`xml.sax`. These interfaces are described below.

In addition to these classes, `xml.sax` provides the following exception
classes.

*exception* xml.sax.SAXException(*msg*, *exception=None*)[¶](#xml.sax.SAXException "Link to this definition")
:   Encapsulate an XML error or warning. This class can contain basic error or
    warning information from either the XML parser or the application: it can be
    subclassed to provide additional functionality or to add localization. Note
    that although the handlers defined in the
    [`ErrorHandler`](xml.sax.handler.html#xml.sax.handler.ErrorHandler "xml.sax.handler.ErrorHandler") interface
    receive instances of this exception, it is not required to actually raise the
    exception — it is also useful as a container for information.

    When instantiated, *msg* should be a human-readable description of the error.
    The optional *exception* parameter, if given, should be `None` or an exception
    that was caught by the parsing code and is being passed along as information.

    This is the base class for the other SAX exception classes.

*exception* xml.sax.SAXParseException(*msg*, *exception*, *locator*)[¶](#xml.sax.SAXParseException "Link to this definition")
:   Subclass of [`SAXException`](#xml.sax.SAXException "xml.sax.SAXException") raised on parse errors. Instances of this
    class are passed to the methods of the SAX
    [`ErrorHandler`](xml.sax.handler.html#xml.sax.handler.ErrorHandler "xml.sax.handler.ErrorHandler") interface to provide information
    about the parse error. This class supports the SAX
    [`Locator`](xml.sax.reader.html#xml.sax.xmlreader.Locator "xml.sax.xmlreader.Locator") interface as well as the
    [`SAXException`](#xml.sax.SAXException "xml.sax.SAXException") interface.

*exception* xml.sax.SAXNotRecognizedException(*msg*, *exception=None*)[¶](#xml.sax.SAXNotRecognizedException "Link to this definition")
:   Subclass of [`SAXException`](#xml.sax.SAXException "xml.sax.SAXException") raised when a SAX
    [`XMLReader`](xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") is
    confronted with an unrecognized feature or property. SAX applications and
    extensions may use this class for similar purposes.

*exception* xml.sax.SAXNotSupportedException(*msg*, *exception=None*)[¶](#xml.sax.SAXNotSupportedException "Link to this definition")
:   Subclass of [`SAXException`](#xml.sax.SAXException "xml.sax.SAXException") raised when a SAX
    [`XMLReader`](xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") is asked to
    enable a feature that is not supported, or to set a property to a value that the
    implementation does not support. SAX applications and extensions may use this
    class for similar purposes.

See also

[SAX: The Simple API for XML](http://www.saxproject.org/)
:   This site is the focal point for the definition of the SAX API. It provides a
    Java implementation and online documentation. Links to implementations and
    historical information are also available.

Module [`xml.sax.handler`](xml.sax.handler.html#module-xml.sax.handler "xml.sax.handler: Base classes for SAX event handlers.")
:   Definitions of the interfaces for application-provided objects.

Module [`xml.sax.saxutils`](xml.sax.utils.html#module-xml.sax.saxutils "xml.sax.saxutils: Convenience functions and classes for use with SAX.")
:   Convenience functions for use in SAX applications.

Module [`xml.sax.xmlreader`](xml.sax.reader.html#module-xml.sax.xmlreader "xml.sax.xmlreader: Interface which SAX-compliant XML parsers must implement.")
:   Definitions of the interfaces for parser-provided objects.

## SAXException Objects[¶](#saxexception-objects "Link to this heading")

The [`SAXException`](#xml.sax.SAXException "xml.sax.SAXException") exception class supports the following methods:

SAXException.getMessage()[¶](#xml.sax.SAXException.getMessage "Link to this definition")
:   Return a human-readable message describing the error condition.

SAXException.getException()[¶](#xml.sax.SAXException.getException "Link to this definition")
:   Return an encapsulated exception object, or `None`.

### [Table of Contents](../contents.html)

* [`xml.sax` — Support for SAX2 parsers](#)
  + [SAXException Objects](#saxexception-objects)

#### Previous topic

[`xml.dom.pulldom` — Support for building partial DOM trees](xml.dom.pulldom.html "previous chapter")

#### Next topic

[`xml.sax.handler` — Base classes for SAX handlers](xml.sax.handler.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/xml.sax.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](xml.sax.handler.html "xml.sax.handler — Base classes for SAX handlers") |
* [previous](xml.dom.pulldom.html "xml.dom.pulldom — Support for building partial DOM trees") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* `xml.sax` — Support for SAX2 parsers
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
### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](pyexpat.html "xml.parsers.expat — Fast XML parsing using Expat") |
* [previous](xml.sax.utils.html "xml.sax.saxutils — SAX Utilities") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* `xml.sax.xmlreader` — Interface for XML parsers
* |
* Theme
  Auto
  Light
  Dark
   |

# `xml.sax.xmlreader` — Interface for XML parsers[¶](#module-xml.sax.xmlreader "Link to this heading")

**Source code:** [Lib/xml/sax/xmlreader.py](https://github.com/python/cpython/tree/3.14/Lib/xml/sax/xmlreader.py)

---

SAX parsers implement the [`XMLReader`](#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") interface. They are implemented in
a Python module, which must provide a function `create_parser()`. This
function is invoked by [`xml.sax.make_parser()`](xml.sax.html#xml.sax.make_parser "xml.sax.make_parser") with no arguments to create
a new parser object.

*class* xml.sax.xmlreader.XMLReader[¶](#xml.sax.xmlreader.XMLReader "Link to this definition")
:   Base class which can be inherited by SAX parsers.

*class* xml.sax.xmlreader.IncrementalParser[¶](#xml.sax.xmlreader.IncrementalParser "Link to this definition")
:   In some cases, it is desirable not to parse an input source at once, but to feed
    chunks of the document as they get available. Note that the reader will normally
    not read the entire file, but read it in chunks as well; still `parse()`
    won’t return until the entire document is processed. So these interfaces should
    be used if the blocking behaviour of `parse()` is not desirable.

    When the parser is instantiated it is ready to begin accepting data from the
    feed method immediately. After parsing has been finished with a call to close
    the reset method must be called to make the parser ready to accept new data,
    either from feed or using the parse method.

    Note that these methods must *not* be called during parsing, that is, after
    parse has been called and before it returns.

    By default, the class also implements the parse method of the XMLReader
    interface using the feed, close and reset methods of the IncrementalParser
    interface as a convenience to SAX 2.0 driver writers.

*class* xml.sax.xmlreader.Locator[¶](#xml.sax.xmlreader.Locator "Link to this definition")
:   Interface for associating a SAX event with a document location. A locator object
    will return valid results only during calls to DocumentHandler methods; at any
    other time, the results are unpredictable. If information is not available,
    methods may return `None`.

*class* xml.sax.xmlreader.InputSource(*system\_id=None*)[¶](#xml.sax.xmlreader.InputSource "Link to this definition")
:   Encapsulation of the information needed by the [`XMLReader`](#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") to read
    entities.

    This class may include information about the public identifier, system
    identifier, byte stream (possibly with character encoding information) and/or
    the character stream of an entity.

    Applications will create objects of this class for use in the
    [`XMLReader.parse()`](#xml.sax.xmlreader.XMLReader.parse "xml.sax.xmlreader.XMLReader.parse") method and for returning from
    EntityResolver.resolveEntity.

    An [`InputSource`](#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource") belongs to the application, the [`XMLReader`](#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") is
    not allowed to modify [`InputSource`](#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource") objects passed to it from the
    application, although it may make copies and modify those.

*class* xml.sax.xmlreader.AttributesImpl(*attrs*)[¶](#xml.sax.xmlreader.AttributesImpl "Link to this definition")
:   This is an implementation of the `Attributes` interface (see section
    [The Attributes Interface](#attributes-objects)). This is a dictionary-like object which
    represents the element attributes in a `startElement()` call. In addition
    to the most useful dictionary operations, it supports a number of other
    methods as described by the interface. Objects of this class should be
    instantiated by readers; *attrs* must be a dictionary-like object containing
    a mapping from attribute names to attribute values.

*class* xml.sax.xmlreader.AttributesNSImpl(*attrs*, *qnames*)[¶](#xml.sax.xmlreader.AttributesNSImpl "Link to this definition")
:   Namespace-aware variant of [`AttributesImpl`](#xml.sax.xmlreader.AttributesImpl "xml.sax.xmlreader.AttributesImpl"), which will be passed to
    `startElementNS()`. It is derived from [`AttributesImpl`](#xml.sax.xmlreader.AttributesImpl "xml.sax.xmlreader.AttributesImpl"), but
    understands attribute names as two-tuples of *namespaceURI* and
    *localname*. In addition, it provides a number of methods expecting qualified
    names as they appear in the original document. This class implements the
    `AttributesNS` interface (see section [The AttributesNS Interface](#attributes-ns-objects)).

## XMLReader Objects[¶](#xmlreader-objects "Link to this heading")

The [`XMLReader`](#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") interface supports the following methods:

XMLReader.parse(*source*)[¶](#xml.sax.xmlreader.XMLReader.parse "Link to this definition")
:   Process an input source, producing SAX events. The *source* object can be a
    system identifier (a string identifying the input source – typically a file
    name or a URL), a [`pathlib.Path`](pathlib.html#pathlib.Path "pathlib.Path") or [path-like](../glossary.html#term-path-like-object)
    object, or an [`InputSource`](#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource") object. When
    [`parse()`](#xml.sax.xmlreader.XMLReader.parse "xml.sax.xmlreader.XMLReader.parse") returns, the input is completely processed, and the parser object
    can be discarded or reset.

    Changed in version 3.5: Added support of character streams.

    Changed in version 3.8: Added support of path-like objects.

XMLReader.getContentHandler()[¶](#xml.sax.xmlreader.XMLReader.getContentHandler "Link to this definition")
:   Return the current [`ContentHandler`](xml.sax.handler.html#xml.sax.handler.ContentHandler "xml.sax.handler.ContentHandler").

XMLReader.setContentHandler(*handler*)[¶](#xml.sax.xmlreader.XMLReader.setContentHandler "Link to this definition")
:   Set the current [`ContentHandler`](xml.sax.handler.html#xml.sax.handler.ContentHandler "xml.sax.handler.ContentHandler"). If no
    [`ContentHandler`](xml.sax.handler.html#xml.sax.handler.ContentHandler "xml.sax.handler.ContentHandler") is set, content events will be
    discarded.

XMLReader.getDTDHandler()[¶](#xml.sax.xmlreader.XMLReader.getDTDHandler "Link to this definition")
:   Return the current [`DTDHandler`](xml.sax.handler.html#xml.sax.handler.DTDHandler "xml.sax.handler.DTDHandler").

XMLReader.setDTDHandler(*handler*)[¶](#xml.sax.xmlreader.XMLReader.setDTDHandler "Link to this definition")
:   Set the current [`DTDHandler`](xml.sax.handler.html#xml.sax.handler.DTDHandler "xml.sax.handler.DTDHandler"). If no
    [`DTDHandler`](xml.sax.handler.html#xml.sax.handler.DTDHandler "xml.sax.handler.DTDHandler") is set, DTD
    events will be discarded.

XMLReader.getEntityResolver()[¶](#xml.sax.xmlreader.XMLReader.getEntityResolver "Link to this definition")
:   Return the current [`EntityResolver`](xml.sax.handler.html#xml.sax.handler.EntityResolver "xml.sax.handler.EntityResolver").

XMLReader.setEntityResolver(*handler*)[¶](#xml.sax.xmlreader.XMLReader.setEntityResolver "Link to this definition")
:   Set the current [`EntityResolver`](xml.sax.handler.html#xml.sax.handler.EntityResolver "xml.sax.handler.EntityResolver"). If no
    [`EntityResolver`](xml.sax.handler.html#xml.sax.handler.EntityResolver "xml.sax.handler.EntityResolver") is set,
    attempts to resolve an external entity will result in opening the system
    identifier for the entity, and fail if it is not available.

XMLReader.getErrorHandler()[¶](#xml.sax.xmlreader.XMLReader.getErrorHandler "Link to this definition")
:   Return the current [`ErrorHandler`](xml.sax.handler.html#xml.sax.handler.ErrorHandler "xml.sax.handler.ErrorHandler").

XMLReader.setErrorHandler(*handler*)[¶](#xml.sax.xmlreader.XMLReader.setErrorHandler "Link to this definition")
:   Set the current error handler. If no [`ErrorHandler`](xml.sax.handler.html#xml.sax.handler.ErrorHandler "xml.sax.handler.ErrorHandler")
    is set, errors will be raised as exceptions, and warnings will be printed.

XMLReader.setLocale(*locale*)[¶](#xml.sax.xmlreader.XMLReader.setLocale "Link to this definition")
:   Allow an application to set the locale for errors and warnings.

    SAX parsers are not required to provide localization for errors and warnings; if
    they cannot support the requested locale, however, they must raise a SAX
    exception. Applications may request a locale change in the middle of a parse.

XMLReader.getFeature(*featurename*)[¶](#xml.sax.xmlreader.XMLReader.getFeature "Link to this definition")
:   Return the current setting for feature *featurename*. If the feature is not
    recognized, `SAXNotRecognizedException` is raised. The well-known
    featurenames are listed in the module [`xml.sax.handler`](xml.sax.handler.html#module-xml.sax.handler "xml.sax.handler: Base classes for SAX event handlers.").

XMLReader.setFeature(*featurename*, *value*)[¶](#xml.sax.xmlreader.XMLReader.setFeature "Link to this definition")
:   Set the *featurename* to *value*. If the feature is not recognized,
    `SAXNotRecognizedException` is raised. If the feature or its setting is not
    supported by the parser, *SAXNotSupportedException* is raised.

XMLReader.getProperty(*propertyname*)[¶](#xml.sax.xmlreader.XMLReader.getProperty "Link to this definition")
:   Return the current setting for property *propertyname*. If the property is not
    recognized, a `SAXNotRecognizedException` is raised. The well-known
    propertynames are listed in the module [`xml.sax.handler`](xml.sax.handler.html#module-xml.sax.handler "xml.sax.handler: Base classes for SAX event handlers.").

XMLReader.setProperty(*propertyname*, *value*)[¶](#xml.sax.xmlreader.XMLReader.setProperty "Link to this definition")
:   Set the *propertyname* to *value*. If the property is not recognized,
    `SAXNotRecognizedException` is raised. If the property or its setting is
    not supported by the parser, *SAXNotSupportedException* is raised.

## IncrementalParser Objects[¶](#incrementalparser-objects "Link to this heading")

Instances of [`IncrementalParser`](#xml.sax.xmlreader.IncrementalParser "xml.sax.xmlreader.IncrementalParser") offer the following additional methods:

IncrementalParser.feed(*data*)[¶](#xml.sax.xmlreader.IncrementalParser.feed "Link to this definition")
:   Process a chunk of *data*.

IncrementalParser.close()[¶](#xml.sax.xmlreader.IncrementalParser.close "Link to this definition")
:   Assume the end of the document. That will check well-formedness conditions that
    can be checked only at the end, invoke handlers, and may clean up resources
    allocated during parsing.

IncrementalParser.reset()[¶](#xml.sax.xmlreader.IncrementalParser.reset "Link to this definition")
:   This method is called after close has been called to reset the parser so that it
    is ready to parse new documents. The results of calling parse or feed after
    close without calling reset are undefined.

## Locator Objects[¶](#locator-objects "Link to this heading")

Instances of [`Locator`](#xml.sax.xmlreader.Locator "xml.sax.xmlreader.Locator") provide these methods:

Locator.getColumnNumber()[¶](#xml.sax.xmlreader.Locator.getColumnNumber "Link to this definition")
:   Return the column number where the current event begins.

Locator.getLineNumber()[¶](#xml.sax.xmlreader.Locator.getLineNumber "Link to this definition")
:   Return the line number where the current event begins.

Locator.getPublicId()[¶](#xml.sax.xmlreader.Locator.getPublicId "Link to this definition")
:   Return the public identifier for the current event.

Locator.getSystemId()[¶](#xml.sax.xmlreader.Locator.getSystemId "Link to this definition")
:   Return the system identifier for the current event.

## InputSource Objects[¶](#inputsource-objects "Link to this heading")

InputSource.setPublicId(*id*)[¶](#xml.sax.xmlreader.InputSource.setPublicId "Link to this definition")
:   Sets the public identifier of this [`InputSource`](#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource").

InputSource.getPublicId()[¶](#xml.sax.xmlreader.InputSource.getPublicId "Link to this definition")
:   Returns the public identifier of this [`InputSource`](#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource").

InputSource.setSystemId(*id*)[¶](#xml.sax.xmlreader.InputSource.setSystemId "Link to this definition")
:   Sets the system identifier of this [`InputSource`](#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource").

InputSource.getSystemId()[¶](#xml.sax.xmlreader.InputSource.getSystemId "Link to this definition")
:   Returns the system identifier of this [`InputSource`](#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource").

InputSource.setEncoding(*encoding*)[¶](#xml.sax.xmlreader.InputSource.setEncoding "Link to this definition")
:   Sets the character encoding of this [`InputSource`](#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource").

    The encoding must be a string acceptable for an XML encoding declaration (see
    section 4.3.3 of the XML recommendation).

    The encoding attribute of the [`InputSource`](#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource") is ignored if the
    [`InputSource`](#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource") also contains a character stream.

InputSource.getEncoding()[¶](#xml.sax.xmlreader.InputSource.getEncoding "Link to this definition")
:   Get the character encoding of this InputSource.

InputSource.setByteStream(*bytefile*)[¶](#xml.sax.xmlreader.InputSource.setByteStream "Link to this definition")
:   Set the byte stream (a [binary file](../glossary.html#term-binary-file)) for this input source.

    The SAX parser will ignore this if there is also a character stream specified,
    but it will use a byte stream in preference to opening a URI connection itself.

    If the application knows the character encoding of the byte stream, it should
    set it with the setEncoding method.

InputSource.getByteStream()[¶](#xml.sax.xmlreader.InputSource.getByteStream "Link to this definition")
:   Get the byte stream for this input source.

    The getEncoding method will return the character encoding for this byte stream,
    or `None` if unknown.

InputSource.setCharacterStream(*charfile*)[¶](#xml.sax.xmlreader.InputSource.setCharacterStream "Link to this definition")
:   Set the character stream (a [text file](../glossary.html#term-text-file)) for this input source.

    If there is a character stream specified, the SAX parser will ignore any byte
    stream and will not attempt to open a URI connection to the system identifier.

InputSource.getCharacterStream()[¶](#xml.sax.xmlreader.InputSource.getCharacterStream "Link to this definition")
:   Get the character stream for this input source.

## The `Attributes` Interface[¶](#the-attributes-interface "Link to this heading")

`Attributes` objects implement a portion of the [mapping protocol](../glossary.html#term-mapping), including the methods `copy()`,
`get()`, [`__contains__()`](../reference/datamodel.html#object.__contains__ "object.__contains__"),
`items()`, `keys()`,
and `values()`. The following methods
are also provided:

Attributes.getLength()[¶](#xml.sax.xmlreader.Attributes.getLength "Link to this definition")
:   Return the number of attributes.

Attributes.getNames()[¶](#xml.sax.xmlreader.Attributes.getNames "Link to this definition")
:   Return the names of the attributes.

Attributes.getType(*name*)[¶](#xml.sax.xmlreader.Attributes.getType "Link to this definition")
:   Returns the type of the attribute *name*, which is normally `'CDATA'`.

Attributes.getValue(*name*)[¶](#xml.sax.xmlreader.Attributes.getValue "Link to this definition")
:   Return the value of attribute *name*.

## The `AttributesNS` Interface[¶](#the-attributesns-interface "Link to this heading")

This interface is a subtype of the `Attributes` interface (see section
[The Attributes Interface](#attributes-objects)). All methods supported by that interface are also
available on `AttributesNS` objects.

The following methods are also available:

AttributesNS.getValueByQName(*name*)[¶](#xml.sax.xmlreader.AttributesNS.getValueByQName "Link to this definition")
:   Return the value for a qualified name.

AttributesNS.getNameByQName(*name*)[¶](#xml.sax.xmlreader.AttributesNS.getNameByQName "Link to this definition")
:   Return the `(namespace, localname)` pair for a qualified *name*.

AttributesNS.getQNameByName(*name*)[¶](#xml.sax.xmlreader.AttributesNS.getQNameByName "Link to this definition")
:   Return the qualified name for a `(namespace, localname)` pair.

AttributesNS.getQNames()[¶](#xml.sax.xmlreader.AttributesNS.getQNames "Link to this definition")
:   Return the qualified names of all attributes.

### [Table of Contents](../contents.html)

* [`xml.sax.xmlreader` — Interface for XML parsers](#)
  + [XMLReader Objects](#xmlreader-objects)
  + [IncrementalParser Objects](#incrementalparser-objects)
  + [Locator Objects](#locator-objects)
  + [InputSource Objects](#inputsource-objects)
  + [The `Attributes` Interface](#the-attributes-interface)
  + [The `AttributesNS` Interface](#the-attributesns-interface)

#### Previous topic

[`xml.sax.saxutils` — SAX Utilities](xml.sax.utils.html "previous chapter")

#### Next topic

[`xml.parsers.expat` — Fast XML parsing using Expat](pyexpat.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/xml.sax.reader.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](pyexpat.html "xml.parsers.expat — Fast XML parsing using Expat") |
* [previous](xml.sax.utils.html "xml.sax.saxutils — SAX Utilities") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* `xml.sax.xmlreader` — Interface for XML parsers
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
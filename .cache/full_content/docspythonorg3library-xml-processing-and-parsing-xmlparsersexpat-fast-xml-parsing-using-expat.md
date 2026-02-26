### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](internet.html "Internet Protocols and Support") |
* [previous](xml.sax.reader.html "xml.sax.xmlreader — Interface for XML parsers") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* `xml.parsers.expat` — Fast XML parsing using Expat
* |
* Theme
  Auto
  Light
  Dark
   |

# `xml.parsers.expat` — Fast XML parsing using Expat[¶](#module-xml.parsers.expat "Link to this heading")

---

Note

If you need to parse untrusted or unauthenticated data, see
[XML security](xml.html#xml-security).

The `xml.parsers.expat` module is a Python interface to the Expat
non-validating XML parser. The module provides a single extension type,
`xmlparser`, that represents the current state of an XML parser. After
an `xmlparser` object has been created, various attributes of the object
can be set to handler functions. When an XML document is then fed to the
parser, the handler functions are called for the character data and markup in
the XML document.

This module uses the `pyexpat` module to provide access to the Expat
parser. Direct use of the `pyexpat` module is deprecated.

This module provides one exception and one type object:

*exception* xml.parsers.expat.ExpatError[¶](#xml.parsers.expat.ExpatError "Link to this definition")
:   The exception raised when Expat reports an error. See section
    [ExpatError Exceptions](#expaterror-objects) for more information on interpreting Expat errors.

*exception* xml.parsers.expat.error[¶](#xml.parsers.expat.error "Link to this definition")
:   Alias for [`ExpatError`](#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError").

xml.parsers.expat.XMLParserType[¶](#xml.parsers.expat.XMLParserType "Link to this definition")
:   The type of the return values from the [`ParserCreate()`](#xml.parsers.expat.ParserCreate "xml.parsers.expat.ParserCreate") function.

The `xml.parsers.expat` module contains two functions:

xml.parsers.expat.ErrorString(*errno*)[¶](#xml.parsers.expat.ErrorString "Link to this definition")
:   Returns an explanatory string for a given error number *errno*.

xml.parsers.expat.ParserCreate(*encoding=None*, *namespace\_separator=None*)[¶](#xml.parsers.expat.ParserCreate "Link to this definition")
:   Creates and returns a new `xmlparser` object. *encoding*, if specified,
    must be a string naming the encoding used by the XML data. Expat doesn’t
    support as many encodings as Python does, and its repertoire of encodings can’t
    be extended; it supports UTF-8, UTF-16, ISO-8859-1 (Latin1), and ASCII. If
    *encoding* [[1]](#id3) is given it will override the implicit or explicit encoding of the
    document.

    Parsers created through `ParserCreate()` are called “root” parsers,
    in the sense that they do not have any parent parser attached. Non-root
    parsers are created by [`parser.ExternalEntityParserCreate`](#xml.parsers.expat.xmlparser.ExternalEntityParserCreate "xml.parsers.expat.xmlparser.ExternalEntityParserCreate").

    Expat can optionally do XML namespace processing for you, enabled by providing a
    value for *namespace\_separator*. The value must be a one-character string; a
    [`ValueError`](exceptions.html#ValueError "ValueError") will be raised if the string has an illegal length (`None`
    is considered the same as omission). When namespace processing is enabled,
    element type names and attribute names that belong to a namespace will be
    expanded. The element name passed to the element handlers
    `StartElementHandler` and `EndElementHandler` will be the
    concatenation of the namespace URI, the namespace separator character, and the
    local part of the name. If the namespace separator is a zero byte (`chr(0)`)
    then the namespace URI and the local part will be concatenated without any
    separator.

    For example, if *namespace\_separator* is set to a space character (`' '`) and
    the following document is parsed:

    ```
    <?xml version="1.0"?>
    <root xmlns    = "http://default-namespace.org/"
          xmlns:py = "http://www.python.org/ns/">
      <py:elem1 />
      <elem2 xmlns="" />
    </root>
    ```

    `StartElementHandler` will receive the following strings for each
    element:

    ```
    http://default-namespace.org/ root
    http://www.python.org/ns/ elem1
    elem2
    ```

    Due to limitations in the `Expat` library used by `pyexpat`,
    the `xmlparser` instance returned can only be used to parse a single
    XML document. Call `ParserCreate` for each document to provide unique
    parser instances.

See also

[The Expat XML Parser](http://www.libexpat.org/)
:   Home page of the Expat project.

## XMLParser Objects[¶](#xmlparser-objects "Link to this heading")

`xmlparser` objects have the following methods:

xmlparser.Parse(*data*[, *isfinal*])[¶](#xml.parsers.expat.xmlparser.Parse "Link to this definition")
:   Parses the contents of the string *data*, calling the appropriate handler
    functions to process the parsed data. *isfinal* must be true on the final call
    to this method; it allows the parsing of a single file in fragments,
    not the submission of multiple files.
    *data* can be the empty string at any time.

xmlparser.ParseFile(*file*)[¶](#xml.parsers.expat.xmlparser.ParseFile "Link to this definition")
:   Parse XML data reading from the object *file*. *file* only needs to provide
    the `read(nbytes)` method, returning the empty string when there’s no more
    data.

xmlparser.SetBase(*base*)[¶](#xml.parsers.expat.xmlparser.SetBase "Link to this definition")
:   Sets the base to be used for resolving relative URIs in system identifiers in
    declarations. Resolving relative identifiers is left to the application: this
    value will be passed through as the *base* argument to the
    [`ExternalEntityRefHandler()`](#xml.parsers.expat.xmlparser.ExternalEntityRefHandler "xml.parsers.expat.xmlparser.ExternalEntityRefHandler"), [`NotationDeclHandler()`](#xml.parsers.expat.xmlparser.NotationDeclHandler "xml.parsers.expat.xmlparser.NotationDeclHandler"), and
    [`UnparsedEntityDeclHandler()`](#xml.parsers.expat.xmlparser.UnparsedEntityDeclHandler "xml.parsers.expat.xmlparser.UnparsedEntityDeclHandler") functions.

xmlparser.GetBase()[¶](#xml.parsers.expat.xmlparser.GetBase "Link to this definition")
:   Returns a string containing the base set by a previous call to [`SetBase()`](#xml.parsers.expat.xmlparser.SetBase "xml.parsers.expat.xmlparser.SetBase"),
    or `None` if [`SetBase()`](#xml.parsers.expat.xmlparser.SetBase "xml.parsers.expat.xmlparser.SetBase") hasn’t been called.

xmlparser.GetInputContext()[¶](#xml.parsers.expat.xmlparser.GetInputContext "Link to this definition")
:   Returns the input data that generated the current event as a string. The data is
    in the encoding of the entity which contains the text. When called while an
    event handler is not active, the return value is `None`.

xmlparser.ExternalEntityParserCreate(*context*[, *encoding*])[¶](#xml.parsers.expat.xmlparser.ExternalEntityParserCreate "Link to this definition")
:   Create a “child” parser which can be used to parse an external parsed entity
    referred to by content parsed by the parent parser. The *context* parameter
    should be the string passed to the [`ExternalEntityRefHandler()`](#xml.parsers.expat.xmlparser.ExternalEntityRefHandler "xml.parsers.expat.xmlparser.ExternalEntityRefHandler") handler
    function, described below. The child parser is created with the
    [`ordered_attributes`](#xml.parsers.expat.xmlparser.ordered_attributes "xml.parsers.expat.xmlparser.ordered_attributes") and [`specified_attributes`](#xml.parsers.expat.xmlparser.specified_attributes "xml.parsers.expat.xmlparser.specified_attributes") set to the values of
    this parser.

xmlparser.SetParamEntityParsing(*flag*)[¶](#xml.parsers.expat.xmlparser.SetParamEntityParsing "Link to this definition")
:   Control parsing of parameter entities (including the external DTD subset).
    Possible *flag* values are `XML_PARAM_ENTITY_PARSING_NEVER`,
    `XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE` and
    `XML_PARAM_ENTITY_PARSING_ALWAYS`. Return true if setting the flag
    was successful.

xmlparser.UseForeignDTD([*flag*])[¶](#xml.parsers.expat.xmlparser.UseForeignDTD "Link to this definition")
:   Calling this with a true value for *flag* (the default) will cause Expat to call
    the [`ExternalEntityRefHandler`](#xml.parsers.expat.xmlparser.ExternalEntityRefHandler "xml.parsers.expat.xmlparser.ExternalEntityRefHandler") with [`None`](constants.html#None "None") for all arguments to
    allow an alternate DTD to be loaded. If the document does not contain a
    document type declaration, the [`ExternalEntityRefHandler`](#xml.parsers.expat.xmlparser.ExternalEntityRefHandler "xml.parsers.expat.xmlparser.ExternalEntityRefHandler") will still be
    called, but the [`StartDoctypeDeclHandler`](#xml.parsers.expat.xmlparser.StartDoctypeDeclHandler "xml.parsers.expat.xmlparser.StartDoctypeDeclHandler") and
    [`EndDoctypeDeclHandler`](#xml.parsers.expat.xmlparser.EndDoctypeDeclHandler "xml.parsers.expat.xmlparser.EndDoctypeDeclHandler") will not be called.

    Passing a false value for *flag* will cancel a previous call that passed a true
    value, but otherwise has no effect.

    This method can only be called before the [`Parse()`](#xml.parsers.expat.xmlparser.Parse "xml.parsers.expat.xmlparser.Parse") or [`ParseFile()`](#xml.parsers.expat.xmlparser.ParseFile "xml.parsers.expat.xmlparser.ParseFile")
    methods are called; calling it after either of those have been called causes
    [`ExpatError`](#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError") to be raised with the [`code`](code.html#module-code "code: Facilities to implement read-eval-print loops.") attribute set to
    `errors.codes[errors.XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING]`.

xmlparser.SetReparseDeferralEnabled(*enabled*)[¶](#xml.parsers.expat.xmlparser.SetReparseDeferralEnabled "Link to this definition")
:   Warning

    Calling `SetReparseDeferralEnabled(False)` has security implications,
    as detailed below; please make sure to understand these consequences
    prior to using the `SetReparseDeferralEnabled` method.

    Expat 2.6.0 introduced a security mechanism called “reparse deferral”
    where instead of causing denial of service through quadratic runtime
    from reparsing large tokens, reparsing of unfinished tokens is now delayed
    by default until a sufficient amount of input is reached.
    Due to this delay, registered handlers may — depending of the sizing of
    input chunks pushed to Expat — no longer be called right after pushing new
    input to the parser. Where immediate feedback and taking over responsibility
    of protecting against denial of service from large tokens are both wanted,
    calling `SetReparseDeferralEnabled(False)` disables reparse deferral
    for the current Expat parser instance, temporarily or altogether.
    Calling `SetReparseDeferralEnabled(True)` allows re-enabling reparse
    deferral.

    Note that [`SetReparseDeferralEnabled()`](#xml.parsers.expat.xmlparser.SetReparseDeferralEnabled "xml.parsers.expat.xmlparser.SetReparseDeferralEnabled") has been backported to some
    prior releases of CPython as a security fix. Check for availability of
    [`SetReparseDeferralEnabled()`](#xml.parsers.expat.xmlparser.SetReparseDeferralEnabled "xml.parsers.expat.xmlparser.SetReparseDeferralEnabled") using [`hasattr()`](functions.html#hasattr "hasattr") if used in code
    running across a variety of Python versions.

    Added in version 3.13.

xmlparser.GetReparseDeferralEnabled()[¶](#xml.parsers.expat.xmlparser.GetReparseDeferralEnabled "Link to this definition")
:   Returns whether reparse deferral is currently enabled for the given
    Expat parser instance.

    Added in version 3.13.

`xmlparser` objects have the following methods to mitigate some
common XML vulnerabilities.

xmlparser.SetAllocTrackerActivationThreshold(*threshold*, */*)[¶](#xml.parsers.expat.xmlparser.SetAllocTrackerActivationThreshold "Link to this definition")
:   Sets the number of allocated bytes of dynamic memory needed to activate
    protection against disproportionate use of RAM.

    By default, parser objects have an allocation activation threshold of 64 MiB,
    or equivalently 67,108,864 bytes.

    An [`ExpatError`](#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError") is raised if this method is called on a
    [non-root](#xmlparser-non-root) parser.
    The corresponding [`lineno`](#xml.parsers.expat.ExpatError.lineno "xml.parsers.expat.ExpatError.lineno") and [`offset`](#xml.parsers.expat.ExpatError.offset "xml.parsers.expat.ExpatError.offset")
    should not be used as they may have no special meaning.

    Added in version 3.14.1.

xmlparser.SetAllocTrackerMaximumAmplification(*max\_factor*, */*)[¶](#xml.parsers.expat.xmlparser.SetAllocTrackerMaximumAmplification "Link to this definition")
:   Sets the maximum amplification factor between direct input and bytes
    of dynamic memory allocated.

    The amplification factor is calculated as `allocated / direct`
    while parsing, where `direct` is the number of bytes read from
    the primary document in parsing and `allocated` is the number
    of bytes of dynamic memory allocated in the parser hierarchy.

    The *max\_factor* value must be a non-NaN [`float`](functions.html#float "float") value greater than
    or equal to 1.0. Amplification factors greater than 100.0 can be observed
    near the start of parsing even with benign files in practice. In particular,
    the activation threshold should be carefully chosen to avoid false positives.

    By default, parser objects have a maximum amplification factor of 100.0.

    An [`ExpatError`](#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError") is raised if this method is called on a
    [non-root](#xmlparser-non-root) parser or if *max\_factor* is outside the valid range.
    The corresponding [`lineno`](#xml.parsers.expat.ExpatError.lineno "xml.parsers.expat.ExpatError.lineno") and [`offset`](#xml.parsers.expat.ExpatError.offset "xml.parsers.expat.ExpatError.offset")
    should not be used as they may have no special meaning.

    Note

    The maximum amplification factor is only considered if the threshold
    that can be adjusted by [`SetAllocTrackerActivationThreshold()`](#xml.parsers.expat.xmlparser.SetAllocTrackerActivationThreshold "xml.parsers.expat.xmlparser.SetAllocTrackerActivationThreshold")
    is exceeded.

    Added in version 3.14.1.

`xmlparser` objects have the following attributes:

xmlparser.buffer\_size[¶](#xml.parsers.expat.xmlparser.buffer_size "Link to this definition")
:   The size of the buffer used when [`buffer_text`](#xml.parsers.expat.xmlparser.buffer_text "xml.parsers.expat.xmlparser.buffer_text") is true.
    A new buffer size can be set by assigning a new integer value
    to this attribute.
    When the size is changed, the buffer will be flushed.

xmlparser.buffer\_text[¶](#xml.parsers.expat.xmlparser.buffer_text "Link to this definition")
:   Setting this to true causes the `xmlparser` object to buffer textual
    content returned by Expat to avoid multiple calls to the
    [`CharacterDataHandler()`](#xml.parsers.expat.xmlparser.CharacterDataHandler "xml.parsers.expat.xmlparser.CharacterDataHandler") callback whenever possible. This can improve
    performance substantially since Expat normally breaks character data into chunks
    at every line ending. This attribute is false by default, and may be changed at
    any time. Note that when it is false, data that does not contain newlines
    may be chunked too.

xmlparser.buffer\_used[¶](#xml.parsers.expat.xmlparser.buffer_used "Link to this definition")
:   If [`buffer_text`](#xml.parsers.expat.xmlparser.buffer_text "xml.parsers.expat.xmlparser.buffer_text") is enabled, the number of bytes stored in the buffer.
    These bytes represent UTF-8 encoded text. This attribute has no meaningful
    interpretation when [`buffer_text`](#xml.parsers.expat.xmlparser.buffer_text "xml.parsers.expat.xmlparser.buffer_text") is false.

xmlparser.ordered\_attributes[¶](#xml.parsers.expat.xmlparser.ordered_attributes "Link to this definition")
:   Setting this attribute to a non-zero integer causes the attributes to be
    reported as a list rather than a dictionary. The attributes are presented in
    the order found in the document text. For each attribute, two list entries are
    presented: the attribute name and the attribute value. (Older versions of this
    module also used this format.) By default, this attribute is false; it may be
    changed at any time.

xmlparser.specified\_attributes[¶](#xml.parsers.expat.xmlparser.specified_attributes "Link to this definition")
:   If set to a non-zero integer, the parser will report only those attributes which
    were specified in the document instance and not those which were derived from
    attribute declarations. Applications which set this need to be especially
    careful to use what additional information is available from the declarations as
    needed to comply with the standards for the behavior of XML processors. By
    default, this attribute is false; it may be changed at any time.

The following attributes contain values relating to the most recent error
encountered by an `xmlparser` object, and will only have correct values
once a call to `Parse()` or `ParseFile()` has raised an
[`xml.parsers.expat.ExpatError`](#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError") exception.

xmlparser.ErrorByteIndex[¶](#xml.parsers.expat.xmlparser.ErrorByteIndex "Link to this definition")
:   Byte index at which an error occurred.

xmlparser.ErrorCode[¶](#xml.parsers.expat.xmlparser.ErrorCode "Link to this definition")
:   Numeric code specifying the problem. This value can be passed to the
    [`ErrorString()`](#xml.parsers.expat.ErrorString "xml.parsers.expat.ErrorString") function, or compared to one of the constants defined in the
    `errors` object.

xmlparser.ErrorColumnNumber[¶](#xml.parsers.expat.xmlparser.ErrorColumnNumber "Link to this definition")
:   Column number at which an error occurred.

xmlparser.ErrorLineNumber[¶](#xml.parsers.expat.xmlparser.ErrorLineNumber "Link to this definition")
:   Line number at which an error occurred.

The following attributes contain values relating to the current parse location
in an `xmlparser` object. During a callback reporting a parse event they
indicate the location of the first of the sequence of characters that generated
the event. When called outside of a callback, the position indicated will be
just past the last parse event (regardless of whether there was an associated
callback).

xmlparser.CurrentByteIndex[¶](#xml.parsers.expat.xmlparser.CurrentByteIndex "Link to this definition")
:   Current byte index in the parser input.

xmlparser.CurrentColumnNumber[¶](#xml.parsers.expat.xmlparser.CurrentColumnNumber "Link to this definition")
:   Current column number in the parser input.

xmlparser.CurrentLineNumber[¶](#xml.parsers.expat.xmlparser.CurrentLineNumber "Link to this definition")
:   Current line number in the parser input.

Here is the list of handlers that can be set. To set a handler on an
`xmlparser` object *o*, use `o.handlername = func`. *handlername* must
be taken from the following list, and *func* must be a callable object accepting
the correct number of arguments. The arguments are all strings, unless
otherwise stated.

xmlparser.XmlDeclHandler(*version*, *encoding*, *standalone*)[¶](#xml.parsers.expat.xmlparser.XmlDeclHandler "Link to this definition")
:   Called when the XML declaration is parsed. The XML declaration is the
    (optional) declaration of the applicable version of the XML recommendation, the
    encoding of the document text, and an optional “standalone” declaration.
    *version* and *encoding* will be strings, and *standalone* will be `1` if the
    document is declared standalone, `0` if it is declared not to be standalone,
    or `-1` if the standalone clause was omitted. This is only available with
    Expat version 1.95.0 or newer.

xmlparser.StartDoctypeDeclHandler(*doctypeName*, *systemId*, *publicId*, *has\_internal\_subset*)[¶](#xml.parsers.expat.xmlparser.StartDoctypeDeclHandler "Link to this definition")
:   Called when Expat begins parsing the document type declaration (`<!DOCTYPE
    ...`). The *doctypeName* is provided exactly as presented. The *systemId* and
    *publicId* parameters give the system and public identifiers if specified, or
    `None` if omitted. *has\_internal\_subset* will be true if the document
    contains an internal document declaration subset. This requires Expat version
    1.2 or newer.

xmlparser.EndDoctypeDeclHandler()[¶](#xml.parsers.expat.xmlparser.EndDoctypeDeclHandler "Link to this definition")
:   Called when Expat is done parsing the document type declaration. This requires
    Expat version 1.2 or newer.

xmlparser.ElementDeclHandler(*name*, *model*)[¶](#xml.parsers.expat.xmlparser.ElementDeclHandler "Link to this definition")
:   Called once for each element type declaration. *name* is the name of the
    element type, and *model* is a representation of the content model.

xmlparser.AttlistDeclHandler(*elname*, *attname*, *type*, *default*, *required*)[¶](#xml.parsers.expat.xmlparser.AttlistDeclHandler "Link to this definition")
:   Called for each declared attribute for an element type. If an attribute list
    declaration declares three attributes, this handler is called three times, once
    for each attribute. *elname* is the name of the element to which the
    declaration applies and *attname* is the name of the attribute declared. The
    attribute type is a string passed as *type*; the possible values are
    `'CDATA'`, `'ID'`, `'IDREF'`, … *default* gives the default value for
    the attribute used when the attribute is not specified by the document instance,
    or `None` if there is no default value (`#IMPLIED` values). If the
    attribute is required to be given in the document instance, *required* will be
    true. This requires Expat version 1.95.0 or newer.

xmlparser.StartElementHandler(*name*, *attributes*)[¶](#xml.parsers.expat.xmlparser.StartElementHandler "Link to this definition")
:   Called for the start of every element. *name* is a string containing the
    element name, and *attributes* is the element attributes. If
    [`ordered_attributes`](#xml.parsers.expat.xmlparser.ordered_attributes "xml.parsers.expat.xmlparser.ordered_attributes") is true, this is a list (see
    [`ordered_attributes`](#xml.parsers.expat.xmlparser.ordered_attributes "xml.parsers.expat.xmlparser.ordered_attributes") for a full description). Otherwise it’s a
    dictionary mapping names to values.

xmlparser.EndElementHandler(*name*)[¶](#xml.parsers.expat.xmlparser.EndElementHandler "Link to this definition")
:   Called for the end of every element.

xmlparser.ProcessingInstructionHandler(*target*, *data*)[¶](#xml.parsers.expat.xmlparser.ProcessingInstructionHandler "Link to this definition")
:   Called for every processing instruction.

xmlparser.CharacterDataHandler(*data*)[¶](#xml.parsers.expat.xmlparser.CharacterDataHandler "Link to this definition")
:   Called for character data. This will be called for normal character data, CDATA
    marked content, and ignorable whitespace. Applications which must distinguish
    these cases can use the [`StartCdataSectionHandler`](#xml.parsers.expat.xmlparser.StartCdataSectionHandler "xml.parsers.expat.xmlparser.StartCdataSectionHandler"),
    [`EndCdataSectionHandler`](#xml.parsers.expat.xmlparser.EndCdataSectionHandler "xml.parsers.expat.xmlparser.EndCdataSectionHandler"), and [`ElementDeclHandler`](#xml.parsers.expat.xmlparser.ElementDeclHandler "xml.parsers.expat.xmlparser.ElementDeclHandler") callbacks to
    collect the required information. Note that the character data may be
    chunked even if it is short and so you may receive more than one call to
    [`CharacterDataHandler()`](#xml.parsers.expat.xmlparser.CharacterDataHandler "xml.parsers.expat.xmlparser.CharacterDataHandler"). Set the [`buffer_text`](#xml.parsers.expat.xmlparser.buffer_text "xml.parsers.expat.xmlparser.buffer_text") instance attribute
    to `True` to avoid that.

xmlparser.UnparsedEntityDeclHandler(*entityName*, *base*, *systemId*, *publicId*, *notationName*)[¶](#xml.parsers.expat.xmlparser.UnparsedEntityDeclHandler "Link to this definition")
:   Called for unparsed (NDATA) entity declarations. This is only present for
    version 1.2 of the Expat library; for more recent versions, use
    [`EntityDeclHandler`](#xml.parsers.expat.xmlparser.EntityDeclHandler "xml.parsers.expat.xmlparser.EntityDeclHandler") instead. (The underlying function in the Expat
    library has been declared obsolete.)

xmlparser.EntityDeclHandler(*entityName*, *is\_parameter\_entity*, *value*, *base*, *systemId*, *publicId*, *notationName*)[¶](#xml.parsers.expat.xmlparser.EntityDeclHandler "Link to this definition")
:   Called for all entity declarations. For parameter and internal entities,
    *value* will be a string giving the declared contents of the entity; this will
    be `None` for external entities. The *notationName* parameter will be
    `None` for parsed entities, and the name of the notation for unparsed
    entities. *is\_parameter\_entity* will be true if the entity is a parameter entity
    or false for general entities (most applications only need to be concerned with
    general entities). This is only available starting with version 1.95.0 of the
    Expat library.

xmlparser.NotationDeclHandler(*notationName*, *base*, *systemId*, *publicId*)[¶](#xml.parsers.expat.xmlparser.NotationDeclHandler "Link to this definition")
:   Called for notation declarations. *notationName*, *base*, and *systemId*, and
    *publicId* are strings if given. If the public identifier is omitted,
    *publicId* will be `None`.

xmlparser.StartNamespaceDeclHandler(*prefix*, *uri*)[¶](#xml.parsers.expat.xmlparser.StartNamespaceDeclHandler "Link to this definition")
:   Called when an element contains a namespace declaration. Namespace declarations
    are processed before the [`StartElementHandler`](#xml.parsers.expat.xmlparser.StartElementHandler "xml.parsers.expat.xmlparser.StartElementHandler") is called for the element
    on which declarations are placed.

xmlparser.EndNamespaceDeclHandler(*prefix*)[¶](#xml.parsers.expat.xmlparser.EndNamespaceDeclHandler "Link to this definition")
:   Called when the closing tag is reached for an element that contained a
    namespace declaration. This is called once for each namespace declaration on
    the element in the reverse of the order for which the
    [`StartNamespaceDeclHandler`](#xml.parsers.expat.xmlparser.StartNamespaceDeclHandler "xml.parsers.expat.xmlparser.StartNamespaceDeclHandler") was called to indicate the start of each
    namespace declaration’s scope. Calls to this handler are made after the
    corresponding [`EndElementHandler`](#xml.parsers.expat.xmlparser.EndElementHandler "xml.parsers.expat.xmlparser.EndElementHandler") for the end of the element.

xmlparser.CommentHandler(*data*)[¶](#xml.parsers.expat.xmlparser.CommentHandler "Link to this definition")
:   Called for comments. *data* is the text of the comment, excluding the leading
    `'<!-``-'` and trailing `'-``->'`.

xmlparser.StartCdataSectionHandler()[¶](#xml.parsers.expat.xmlparser.StartCdataSectionHandler "Link to this definition")
:   Called at the start of a CDATA section. This and [`EndCdataSectionHandler`](#xml.parsers.expat.xmlparser.EndCdataSectionHandler "xml.parsers.expat.xmlparser.EndCdataSectionHandler")
    are needed to be able to identify the syntactical start and end for CDATA
    sections.

xmlparser.EndCdataSectionHandler()[¶](#xml.parsers.expat.xmlparser.EndCdataSectionHandler "Link to this definition")
:   Called at the end of a CDATA section.

xmlparser.DefaultHandler(*data*)[¶](#xml.parsers.expat.xmlparser.DefaultHandler "Link to this definition")
:   Called for any characters in the XML document for which no applicable handler
    has been specified. This means characters that are part of a construct which
    could be reported, but for which no handler has been supplied.

xmlparser.DefaultHandlerExpand(*data*)[¶](#xml.parsers.expat.xmlparser.DefaultHandlerExpand "Link to this definition")
:   This is the same as the [`DefaultHandler()`](#xml.parsers.expat.xmlparser.DefaultHandler "xml.parsers.expat.xmlparser.DefaultHandler"), but doesn’t inhibit expansion
    of internal entities. The entity reference will not be passed to the default
    handler.

xmlparser.NotStandaloneHandler()[¶](#xml.parsers.expat.xmlparser.NotStandaloneHandler "Link to this definition")
:   Called if the XML document hasn’t been declared as being a standalone document.
    This happens when there is an external subset or a reference to a parameter
    entity, but the XML declaration does not set standalone to `yes` in an XML
    declaration. If this handler returns `0`, then the parser will raise an
    `XML_ERROR_NOT_STANDALONE` error. If this handler is not set, no
    exception is raised by the parser for this condition.

xmlparser.ExternalEntityRefHandler(*context*, *base*, *systemId*, *publicId*)[¶](#xml.parsers.expat.xmlparser.ExternalEntityRefHandler "Link to this definition")
:   Warning

    Implementing a handler that accesses local files and/or the network
    may create a vulnerability to
    [external entity attacks](https://en.wikipedia.org/wiki/XML_external_entity_attack)
    if `xmlparser` is used with user-provided XML content.
    Please reflect on your [threat model](https://en.wikipedia.org/wiki/Threat_model)
    before implementing this handler.

    Called for references to external entities. *base* is the current base, as set
    by a previous call to [`SetBase()`](#xml.parsers.expat.xmlparser.SetBase "xml.parsers.expat.xmlparser.SetBase"). The public and system identifiers,
    *systemId* and *publicId*, are strings if given; if the public identifier is not
    given, *publicId* will be `None`. The *context* value is opaque and should
    only be used as described below.

    For external entities to be parsed, this handler must be implemented. It is
    responsible for creating the sub-parser using
    `ExternalEntityParserCreate(context)`, initializing it with the appropriate
    callbacks, and parsing the entity. This handler should return an integer; if it
    returns `0`, the parser will raise an
    `XML_ERROR_EXTERNAL_ENTITY_HANDLING` error, otherwise parsing will
    continue.

    If this handler is not provided, external entities are reported by the
    [`DefaultHandler`](#xml.parsers.expat.xmlparser.DefaultHandler "xml.parsers.expat.xmlparser.DefaultHandler") callback, if provided.

## ExpatError Exceptions[¶](#expaterror-exceptions "Link to this heading")

[`ExpatError`](#xml.parsers.expat.ExpatError "xml.parsers.expat.ExpatError") exceptions have a number of interesting attributes:

ExpatError.code[¶](#xml.parsers.expat.ExpatError.code "Link to this definition")
:   Expat’s internal error number for the specific error. The
    [`errors.messages`](#xml.parsers.expat.errors.messages "xml.parsers.expat.errors.messages") dictionary maps
    these error numbers to Expat’s error messages. For example:

    ```
    from xml.parsers.expat import ParserCreate, ExpatError, errors

    p = ParserCreate()
    try:
        p.Parse(some_xml_document)
    except ExpatError as err:
        print("Error:", errors.messages[err.code])
    ```

    The [`errors`](#module-xml.parsers.expat.errors "xml.parsers.expat.errors") module also provides error message
    constants and a dictionary [`codes`](#xml.parsers.expat.errors.codes "xml.parsers.expat.errors.codes") mapping
    these messages back to the error codes, see below.

ExpatError.lineno[¶](#xml.parsers.expat.ExpatError.lineno "Link to this definition")
:   Line number on which the error was detected. The first line is numbered `1`.

ExpatError.offset[¶](#xml.parsers.expat.ExpatError.offset "Link to this definition")
:   Character offset into the line where the error occurred. The first column is
    numbered `0`.

## Example[¶](#example "Link to this heading")

The following program defines three handlers that just print out their
arguments.

```
import xml.parsers.expat

# 3 handler functions
def start_element(name, attrs):
    print('Start element:', name, attrs)
def end_element(name):
    print('End element:', name)
def char_data(data):
    print('Character data:', repr(data))

p = xml.parsers.expat.ParserCreate()

p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data

p.Parse("""<?xml version="1.0"?>
<parent id="top"><child1 name="paul">Text goes here</child1>
<child2 name="fred">More text</child2>
</parent>""", 1)
```

The output from this program is:

```
Start element: parent {'id': 'top'}
Start element: child1 {'name': 'paul'}
Character data: 'Text goes here'
End element: child1
Character data: '\n'
Start element: child2 {'name': 'fred'}
Character data: 'More text'
End element: child2
Character data: '\n'
End element: parent
```

## Content Model Descriptions[¶](#module-xml.parsers.expat.model "Link to this heading")

Content models are described using nested tuples. Each tuple contains four
values: the type, the quantifier, the name, and a tuple of children. Children
are simply additional content model descriptions.

The values of the first two fields are constants defined in the
`xml.parsers.expat.model` module. These constants can be collected in two
groups: the model type group and the quantifier group.

The constants in the model type group are:

xml.parsers.expat.model.XML\_CTYPE\_ANY
:   The element named by the model name was declared to have a content model of
    `ANY`.

xml.parsers.expat.model.XML\_CTYPE\_CHOICE
:   The named element allows a choice from a number of options; this is used for
    content models such as `(A | B | C)`.

xml.parsers.expat.model.XML\_CTYPE\_EMPTY
:   Elements which are declared to be `EMPTY` have this model type.

xml.parsers.expat.model.XML\_CTYPE\_MIXED

xml.parsers.expat.model.XML\_CTYPE\_NAME

xml.parsers.expat.model.XML\_CTYPE\_SEQ
:   Models which represent a series of models which follow one after the other are
    indicated with this model type. This is used for models such as `(A, B, C)`.

The constants in the quantifier group are:

xml.parsers.expat.model.XML\_CQUANT\_NONE
:   No modifier is given, so it can appear exactly once, as for `A`.

xml.parsers.expat.model.XML\_CQUANT\_OPT
:   The model is optional: it can appear once or not at all, as for `A?`.

xml.parsers.expat.model.XML\_CQUANT\_PLUS
:   The model must occur one or more times (like `A+`).

xml.parsers.expat.model.XML\_CQUANT\_REP
:   The model must occur zero or more times, as for `A*`.

## Expat error constants[¶](#module-xml.parsers.expat.errors "Link to this heading")

The following constants are provided in the `xml.parsers.expat.errors`
module. These constants are useful in interpreting some of the attributes of
the `ExpatError` exception objects raised when an error has occurred.
Since for backwards compatibility reasons, the constants’ value is the error
*message* and not the numeric error *code*, you do this by comparing its
[`code`](code.html#module-code "code: Facilities to implement read-eval-print loops.") attribute with
`errors.codes[errors.XML_ERROR_CONSTANT_NAME]`.

The `errors` module has the following attributes:

xml.parsers.expat.errors.codes[¶](#xml.parsers.expat.errors.codes "Link to this definition")
:   A dictionary mapping string descriptions to their error codes.

    Added in version 3.2.

xml.parsers.expat.errors.messages[¶](#xml.parsers.expat.errors.messages "Link to this definition")
:   A dictionary mapping numeric error codes to their string descriptions.

    Added in version 3.2.

xml.parsers.expat.errors.XML\_ERROR\_ASYNC\_ENTITY[¶](#xml.parsers.expat.errors.XML_ERROR_ASYNC_ENTITY "Link to this definition")

xml.parsers.expat.errors.XML\_ERROR\_ATTRIBUTE\_EXTERNAL\_ENTITY\_REF[¶](#xml.parsers.expat.errors.XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF "Link to this definition")
:   An entity reference in an attribute value referred to an external entity instead
    of an internal entity.

xml.parsers.expat.errors.XML\_ERROR\_BAD\_CHAR\_REF[¶](#xml.parsers.expat.errors.XML_ERROR_BAD_CHAR_REF "Link to this definition")
:   A character reference referred to a character which is illegal in XML (for
    example, character `0`, or ‘`&#0;`’).

xml.parsers.expat.errors.XML\_ERROR\_BINARY\_ENTITY\_REF[¶](#xml.parsers.expat.errors.XML_ERROR_BINARY_ENTITY_REF "Link to this definition")
:   An entity reference referred to an entity which was declared with a notation, so
    cannot be parsed.

xml.parsers.expat.errors.XML\_ERROR\_DUPLICATE\_ATTRIBUTE[¶](#xml.parsers.expat.errors.XML_ERROR_DUPLICATE_ATTRIBUTE "Link to this definition")
:   An attribute was used more than once in a start tag.

xml.parsers.expat.errors.XML\_ERROR\_INCORRECT\_ENCODING[¶](#xml.parsers.expat.errors.XML_ERROR_INCORRECT_ENCODING "Link to this definition")

xml.parsers.expat.errors.XML\_ERROR\_INVALID\_TOKEN[¶](#xml.parsers.expat.errors.XML_ERROR_INVALID_TOKEN "Link to this definition")
:   Raised when an input byte could not properly be assigned to a character; for
    example, a NUL byte (value `0`) in a UTF-8 input stream.

xml.parsers.expat.errors.XML\_ERROR\_JUNK\_AFTER\_DOC\_ELEMENT[¶](#xml.parsers.expat.errors.XML_ERROR_JUNK_AFTER_DOC_ELEMENT "Link to this definition")
:   Something other than whitespace occurred after the document element.

xml.parsers.expat.errors.XML\_ERROR\_MISPLACED\_XML\_PI[¶](#xml.parsers.expat.errors.XML_ERROR_MISPLACED_XML_PI "Link to this definition")
:   An XML declaration was found somewhere other than the start of the input data.

xml.parsers.expat.errors.XML\_ERROR\_NO\_ELEMENTS[¶](#xml.parsers.expat.errors.XML_ERROR_NO_ELEMENTS "Link to this definition")
:   The document contains no elements (XML requires all documents to contain exactly
    one top-level element)..

xml.parsers.expat.errors.XML\_ERROR\_NO\_MEMORY[¶](#xml.parsers.expat.errors.XML_ERROR_NO_MEMORY "Link to this definition")
:   Expat was not able to allocate memory internally.

xml.parsers.expat.errors.XML\_ERROR\_PARAM\_ENTITY\_REF[¶](#xml.parsers.expat.errors.XML_ERROR_PARAM_ENTITY_REF "Link to this definition")
:   A parameter entity reference was found where it was not allowed.

xml.parsers.expat.errors.XML\_ERROR\_PARTIAL\_CHAR[¶](#xml.parsers.expat.errors.XML_ERROR_PARTIAL_CHAR "Link to this definition")
:   An incomplete character was found in the input.

xml.parsers.expat.errors.XML\_ERROR\_RECURSIVE\_ENTITY\_REF[¶](#xml.parsers.expat.errors.XML_ERROR_RECURSIVE_ENTITY_REF "Link to this definition")
:   An entity reference contained another reference to the same entity; possibly via
    a different name, and possibly indirectly.

xml.parsers.expat.errors.XML\_ERROR\_SYNTAX[¶](#xml.parsers.expat.errors.XML_ERROR_SYNTAX "Link to this definition")
:   Some unspecified syntax error was encountered.

xml.parsers.expat.errors.XML\_ERROR\_TAG\_MISMATCH[¶](#xml.parsers.expat.errors.XML_ERROR_TAG_MISMATCH "Link to this definition")
:   An end tag did not match the innermost open start tag.

xml.parsers.expat.errors.XML\_ERROR\_UNCLOSED\_TOKEN[¶](#xml.parsers.expat.errors.XML_ERROR_UNCLOSED_TOKEN "Link to this definition")
:   Some token (such as a start tag) was not closed before the end of the stream or
    the next token was encountered.

xml.parsers.expat.errors.XML\_ERROR\_UNDEFINED\_ENTITY[¶](#xml.parsers.expat.errors.XML_ERROR_UNDEFINED_ENTITY "Link to this definition")
:   A reference was made to an entity which was not defined.

xml.parsers.expat.errors.XML\_ERROR\_UNKNOWN\_ENCODING[¶](#xml.parsers.expat.errors.XML_ERROR_UNKNOWN_ENCODING "Link to this definition")
:   The document encoding is not supported by Expat.

xml.parsers.expat.errors.XML\_ERROR\_UNCLOSED\_CDATA\_SECTION[¶](#xml.parsers.expat.errors.XML_ERROR_UNCLOSED_CDATA_SECTION "Link to this definition")
:   A CDATA marked section was not closed.

xml.parsers.expat.errors.XML\_ERROR\_EXTERNAL\_ENTITY\_HANDLING[¶](#xml.parsers.expat.errors.XML_ERROR_EXTERNAL_ENTITY_HANDLING "Link to this definition")

xml.parsers.expat.errors.XML\_ERROR\_NOT\_STANDALONE[¶](#xml.parsers.expat.errors.XML_ERROR_NOT_STANDALONE "Link to this definition")
:   The parser determined that the document was not “standalone” though it declared
    itself to be in the XML declaration, and the `NotStandaloneHandler` was
    set and returned `0`.

xml.parsers.expat.errors.XML\_ERROR\_UNEXPECTED\_STATE[¶](#xml.parsers.expat.errors.XML_ERROR_UNEXPECTED_STATE "Link to this definition")

xml.parsers.expat.errors.XML\_ERROR\_ENTITY\_DECLARED\_IN\_PE[¶](#xml.parsers.expat.errors.XML_ERROR_ENTITY_DECLARED_IN_PE "Link to this definition")

xml.parsers.expat.errors.XML\_ERROR\_FEATURE\_REQUIRES\_XML\_DTD[¶](#xml.parsers.expat.errors.XML_ERROR_FEATURE_REQUIRES_XML_DTD "Link to this definition")
:   An operation was requested that requires DTD support to be compiled in, but
    Expat was configured without DTD support. This should never be reported by a
    standard build of the `xml.parsers.expat` module.

xml.parsers.expat.errors.XML\_ERROR\_CANT\_CHANGE\_FEATURE\_ONCE\_PARSING[¶](#xml.parsers.expat.errors.XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING "Link to this definition")
:   A behavioral change was requested after parsing started that can only be changed
    before parsing has started. This is (currently) only raised by
    `UseForeignDTD()`.

xml.parsers.expat.errors.XML\_ERROR\_UNBOUND\_PREFIX[¶](#xml.parsers.expat.errors.XML_ERROR_UNBOUND_PREFIX "Link to this definition")
:   An undeclared prefix was found when namespace processing was enabled.

xml.parsers.expat.errors.XML\_ERROR\_UNDECLARING\_PREFIX[¶](#xml.parsers.expat.errors.XML_ERROR_UNDECLARING_PREFIX "Link to this definition")
:   The document attempted to remove the namespace declaration associated with a
    prefix.

xml.parsers.expat.errors.XML\_ERROR\_INCOMPLETE\_PE[¶](#xml.parsers.expat.errors.XML_ERROR_INCOMPLETE_PE "Link to this definition")
:   A parameter entity contained incomplete markup.

xml.parsers.expat.errors.XML\_ERROR\_XML\_DECL[¶](#xml.parsers.expat.errors.XML_ERROR_XML_DECL "Link to this definition")
:   The document contained no document element at all.

xml.parsers.expat.errors.XML\_ERROR\_TEXT\_DECL[¶](#xml.parsers.expat.errors.XML_ERROR_TEXT_DECL "Link to this definition")
:   There was an error parsing a text declaration in an external entity.

xml.parsers.expat.errors.XML\_ERROR\_PUBLICID[¶](#xml.parsers.expat.errors.XML_ERROR_PUBLICID "Link to this definition")
:   Characters were found in the public id that are not allowed.

xml.parsers.expat.errors.XML\_ERROR\_SUSPENDED[¶](#xml.parsers.expat.errors.XML_ERROR_SUSPENDED "Link to this definition")
:   The requested operation was made on a suspended parser, but isn’t allowed. This
    includes attempts to provide additional input or to stop the parser.

xml.parsers.expat.errors.XML\_ERROR\_NOT\_SUSPENDED[¶](#xml.parsers.expat.errors.XML_ERROR_NOT_SUSPENDED "Link to this definition")
:   An attempt to resume the parser was made when the parser had not been suspended.

xml.parsers.expat.errors.XML\_ERROR\_ABORTED[¶](#xml.parsers.expat.errors.XML_ERROR_ABORTED "Link to this definition")
:   This should not be reported to Python applications.

xml.parsers.expat.errors.XML\_ERROR\_FINISHED[¶](#xml.parsers.expat.errors.XML_ERROR_FINISHED "Link to this definition")
:   The requested operation was made on a parser which was finished parsing input,
    but isn’t allowed. This includes attempts to provide additional input or to
    stop the parser.

xml.parsers.expat.errors.XML\_ERROR\_SUSPEND\_PE[¶](#xml.parsers.expat.errors.XML_ERROR_SUSPEND_PE "Link to this definition")

xml.parsers.expat.errors.XML\_ERROR\_RESERVED\_PREFIX\_XML[¶](#xml.parsers.expat.errors.XML_ERROR_RESERVED_PREFIX_XML "Link to this definition")
:   An attempt was made to
    undeclare reserved namespace prefix `xml`
    or to bind it to another namespace URI.

xml.parsers.expat.errors.XML\_ERROR\_RESERVED\_PREFIX\_XMLNS[¶](#xml.parsers.expat.errors.XML_ERROR_RESERVED_PREFIX_XMLNS "Link to this definition")
:   An attempt was made to declare or undeclare reserved namespace prefix `xmlns`.

xml.parsers.expat.errors.XML\_ERROR\_RESERVED\_NAMESPACE\_URI[¶](#xml.parsers.expat.errors.XML_ERROR_RESERVED_NAMESPACE_URI "Link to this definition")
:   An attempt was made to bind the URI of one the reserved namespace
    prefixes `xml` and `xmlns` to another namespace prefix.

xml.parsers.expat.errors.XML\_ERROR\_INVALID\_ARGUMENT[¶](#xml.parsers.expat.errors.XML_ERROR_INVALID_ARGUMENT "Link to this definition")
:   This should not be reported to Python applications.

xml.parsers.expat.errors.XML\_ERROR\_NO\_BUFFER[¶](#xml.parsers.expat.errors.XML_ERROR_NO_BUFFER "Link to this definition")
:   This should not be reported to Python applications.

xml.parsers.expat.errors.XML\_ERROR\_AMPLIFICATION\_LIMIT\_BREACH[¶](#xml.parsers.expat.errors.XML_ERROR_AMPLIFICATION_LIMIT_BREACH "Link to this definition")
:   The limit on input amplification factor (from DTD and entities)
    has been breached.

xml.parsers.expat.errors.XML\_ERROR\_NOT\_STARTED[¶](#xml.parsers.expat.errors.XML_ERROR_NOT_STARTED "Link to this definition")
:   The parser was tried to be stopped or suspended before it started.

    Added in version 3.14.

Footnotes

[[1](#id1)]

The encoding string included in XML output should conform to the
appropriate standards. For example, “UTF-8” is valid, but “UTF8” is
not. See <https://www.w3.org/TR/2006/REC-xml11-20060816/#NT-EncodingDecl>
and <https://www.iana.org/assignments/character-sets/character-sets.xhtml>.

### [Table of Contents](../contents.html)

* [`xml.parsers.expat` — Fast XML parsing using Expat](#)
  + [XMLParser Objects](#xmlparser-objects)
  + [ExpatError Exceptions](#expaterror-exceptions)
  + [Example](#example)
  + [Content Model Descriptions](#module-xml.parsers.expat.model)
  + [Expat error constants](#module-xml.parsers.expat.errors)

#### Previous topic

[`xml.sax.xmlreader` — Interface for XML parsers](xml.sax.reader.html "previous chapter")

#### Next topic

[Internet Protocols and Support](internet.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/pyexpat.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](internet.html "Internet Protocols and Support") |
* [previous](xml.sax.reader.html "xml.sax.xmlreader — Interface for XML parsers") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Structured Markup Processing Tools](markup.html) »
* `xml.parsers.expat` — Fast XML parsing using Expat
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
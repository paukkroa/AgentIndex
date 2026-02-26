### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](urllib.robotparser.html "urllib.robotparser — Parser for robots.txt") |
* [previous](urllib.parse.html "urllib.parse — Parse URLs into components") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Protocols and Support](internet.html) »
* `urllib.error` — Exception classes raised by urllib.request
* |
* Theme
  Auto
  Light
  Dark
   |

# `urllib.error` — Exception classes raised by urllib.request[¶](#module-urllib.error "Link to this heading")

**Source code:** [Lib/urllib/error.py](https://github.com/python/cpython/tree/3.14/Lib/urllib/error.py)

---

The `urllib.error` module defines the exception classes for exceptions
raised by [`urllib.request`](urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs."). The base exception class is [`URLError`](#urllib.error.URLError "urllib.error.URLError").

The following exceptions are raised by `urllib.error` as appropriate:

*exception* urllib.error.URLError[¶](#urllib.error.URLError "Link to this definition")
:   The handlers raise this exception (or derived exceptions) when they run into
    a problem. It is a subclass of [`OSError`](exceptions.html#OSError "OSError").

    reason[¶](#urllib.error.URLError.reason "Link to this definition")
    :   The reason for this error. It can be a message string or another
        exception instance.

    Changed in version 3.3: [`URLError`](#urllib.error.URLError "urllib.error.URLError") used to be a subtype of [`IOError`](exceptions.html#IOError "IOError"), which is now an
    alias of [`OSError`](exceptions.html#OSError "OSError").

*exception* urllib.error.HTTPError(*url*, *code*, *msg*, *hdrs*, *fp*)[¶](#urllib.error.HTTPError "Link to this definition")
:   Though being an exception (a subclass of [`URLError`](#urllib.error.URLError "urllib.error.URLError")), an
    [`HTTPError`](#urllib.error.HTTPError "urllib.error.HTTPError") can also function as a non-exceptional file-like return
    value (the same thing that [`urlopen()`](urllib.request.html#urllib.request.urlopen "urllib.request.urlopen") returns). This
    is useful when handling exotic HTTP errors, such as requests for
    authentication.

    url[¶](#urllib.error.HTTPError.url "Link to this definition")
    :   Contains the request URL.
        An alias for *filename* attribute.

    code[¶](#urllib.error.HTTPError.code "Link to this definition")
    :   An HTTP status code as defined in [**RFC 2616**](https://datatracker.ietf.org/doc/html/rfc2616.html). This numeric value corresponds
        to a value found in the dictionary of codes as found in
        [`http.server.BaseHTTPRequestHandler.responses`](http.server.html#http.server.BaseHTTPRequestHandler.responses "http.server.BaseHTTPRequestHandler.responses").

    reason[¶](#urllib.error.HTTPError.reason "Link to this definition")
    :   This is usually a string explaining the reason for this error.
        An alias for *msg* attribute.

    headers[¶](#urllib.error.HTTPError.headers "Link to this definition")
    :   The HTTP response headers for the HTTP request that caused the
        [`HTTPError`](#urllib.error.HTTPError "urllib.error.HTTPError").
        An alias for *hdrs* attribute.

        Added in version 3.4.

    fp[¶](#urllib.error.HTTPError.fp "Link to this definition")
    :   A file-like object where the HTTP error body can be read from.

*exception* urllib.error.ContentTooShortError(*msg*, *content*)[¶](#urllib.error.ContentTooShortError "Link to this definition")
:   This exception is raised when the [`urlretrieve()`](urllib.request.html#urllib.request.urlretrieve "urllib.request.urlretrieve")
    function detects that
    the amount of the downloaded data is less than the expected amount (given by
    the *Content-Length* header).

    content[¶](#urllib.error.ContentTooShortError.content "Link to this definition")
    :   The downloaded (and supposedly truncated) data.

#### Previous topic

[`urllib.parse` — Parse URLs into components](urllib.parse.html "previous chapter")

#### Next topic

[`urllib.robotparser` — Parser for robots.txt](urllib.robotparser.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/urllib.error.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](urllib.robotparser.html "urllib.robotparser — Parser for robots.txt") |
* [previous](urllib.parse.html "urllib.parse — Parse URLs into components") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Protocols and Support](internet.html) »
* `urllib.error` — Exception classes raised by urllib.request
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
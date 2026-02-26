### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](http.cookiejar.html "http.cookiejar — Cookie handling for HTTP clients") |
* [previous](http.server.html "http.server — HTTP servers") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Protocols and Support](internet.html) »
* `http.cookies` — HTTP state management
* |
* Theme
  Auto
  Light
  Dark
   |

# `http.cookies` — HTTP state management[¶](#module-http.cookies "Link to this heading")

**Source code:** [Lib/http/cookies.py](https://github.com/python/cpython/tree/3.14/Lib/http/cookies.py)

---

The `http.cookies` module defines classes for abstracting the concept of
cookies, an HTTP state management mechanism. It supports both simple string-only
cookies, and provides an abstraction for having any serializable data-type as
cookie value.

The module formerly strictly applied the parsing rules described in the
[**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) and [**RFC 2068**](https://datatracker.ietf.org/doc/html/rfc2068.html) specifications. It has since been discovered that
MSIE 3.0x didn’t follow the character rules outlined in those specs; many
current-day browsers and servers have also relaxed parsing rules when it comes
to cookie handling. As a result, this module now uses parsing rules that are a
bit less strict than they once were.

The character set, [`string.ascii_letters`](string.html#string.ascii_letters "string.ascii_letters"), [`string.digits`](string.html#string.digits "string.digits") and
`` !#$%&'*+-.^_`|~: `` denote the set of valid characters allowed by this module
in a cookie name (as [`key`](#http.cookies.Morsel.key "http.cookies.Morsel.key")).

Changed in version 3.3: Allowed ‘:’ as a valid cookie name character.

Note

On encountering an invalid cookie, [`CookieError`](#http.cookies.CookieError "http.cookies.CookieError") is raised, so if your
cookie data comes from a browser you should always prepare for invalid data
and catch [`CookieError`](#http.cookies.CookieError "http.cookies.CookieError") on parsing.

*exception* http.cookies.CookieError[¶](#http.cookies.CookieError "Link to this definition")
:   Exception failing because of [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) invalidity: incorrect attributes,
    incorrect *Set-Cookie* header, etc.

*class* http.cookies.BaseCookie([*input*])[¶](#http.cookies.BaseCookie "Link to this definition")
:   This class is a dictionary-like object whose keys are strings and whose values
    are [`Morsel`](#http.cookies.Morsel "http.cookies.Morsel") instances. Note that upon setting a key to a value, the
    value is first converted to a [`Morsel`](#http.cookies.Morsel "http.cookies.Morsel") containing the key and the value.

    If *input* is given, it is passed to the [`load()`](#http.cookies.BaseCookie.load "http.cookies.BaseCookie.load") method.

*class* http.cookies.SimpleCookie([*input*])[¶](#http.cookies.SimpleCookie "Link to this definition")
:   This class derives from [`BaseCookie`](#http.cookies.BaseCookie "http.cookies.BaseCookie") and overrides [`value_decode()`](#http.cookies.BaseCookie.value_decode "http.cookies.BaseCookie.value_decode")
    and [`value_encode()`](#http.cookies.BaseCookie.value_encode "http.cookies.BaseCookie.value_encode"). `SimpleCookie` supports
    strings as cookie values. When setting the value, `SimpleCookie`
    calls the builtin [`str()`](stdtypes.html#str "str") to convert
    the value to a string. Values received from HTTP are kept as strings.

See also

Module [`http.cookiejar`](http.cookiejar.html#module-http.cookiejar "http.cookiejar: Classes for automatic handling of HTTP cookies.")
:   HTTP cookie handling for web *clients*. The [`http.cookiejar`](http.cookiejar.html#module-http.cookiejar "http.cookiejar: Classes for automatic handling of HTTP cookies.") and
    `http.cookies` modules do not depend on each other.

[**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) - HTTP State Management Mechanism
:   This is the state management specification implemented by this module.

## Cookie Objects[¶](#cookie-objects "Link to this heading")

BaseCookie.value\_decode(*val*)[¶](#http.cookies.BaseCookie.value_decode "Link to this definition")
:   Return a tuple `(real_value, coded_value)` from a string representation.
    `real_value` can be any type. This method does no decoding in
    [`BaseCookie`](#http.cookies.BaseCookie "http.cookies.BaseCookie") — it exists so it can be overridden.

BaseCookie.value\_encode(*val*)[¶](#http.cookies.BaseCookie.value_encode "Link to this definition")
:   Return a tuple `(real_value, coded_value)`. *val* can be any type, but
    `coded_value` will always be converted to a string.
    This method does no encoding in [`BaseCookie`](#http.cookies.BaseCookie "http.cookies.BaseCookie") — it exists so it can
    be overridden.

    In general, it should be the case that [`value_encode()`](#http.cookies.BaseCookie.value_encode "http.cookies.BaseCookie.value_encode") and
    [`value_decode()`](#http.cookies.BaseCookie.value_decode "http.cookies.BaseCookie.value_decode") are inverses on the range of *value\_decode*.

BaseCookie.output(*attrs=None*, *header='Set-Cookie:'*, *sep='\r\n'*)[¶](#http.cookies.BaseCookie.output "Link to this definition")
:   Return a string representation suitable to be sent as HTTP headers. *attrs* and
    *header* are sent to each [`Morsel`](#http.cookies.Morsel "http.cookies.Morsel")’s [`output()`](#http.cookies.Morsel.output "http.cookies.Morsel.output") method. *sep* is used
    to join the headers together, and is by default the combination `'\r\n'`
    (CRLF).

BaseCookie.js\_output(*attrs=None*)[¶](#http.cookies.BaseCookie.js_output "Link to this definition")
:   Return an embeddable JavaScript snippet, which, if run on a browser which
    supports JavaScript, will act the same as if the HTTP headers was sent.

    The meaning for *attrs* is the same as in [`output()`](#http.cookies.BaseCookie.output "http.cookies.BaseCookie.output").

BaseCookie.load(*rawdata*)[¶](#http.cookies.BaseCookie.load "Link to this definition")
:   If *rawdata* is a string, parse it as an `HTTP_COOKIE` and add the values
    found there as [`Morsel`](#http.cookies.Morsel "http.cookies.Morsel")s. If it is a dictionary, it is equivalent to:

    ```
    for k, v in rawdata.items():
        cookie[k] = v
    ```

## Morsel Objects[¶](#morsel-objects "Link to this heading")

*class* http.cookies.Morsel[¶](#http.cookies.Morsel "Link to this definition")
:   Abstract a key/value pair, which has some [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) attributes.

    Morsels are dictionary-like objects, whose set of keys is constant — the valid
    [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) attributes, which are:

    > expires[¶](#http.cookies.Morsel.expires "Link to this definition")
    >
    > path[¶](#http.cookies.Morsel.path "Link to this definition")
    >
    > comment[¶](#http.cookies.Morsel.comment "Link to this definition")
    >
    > domain[¶](#http.cookies.Morsel.domain "Link to this definition")
    >
    > max-age
    >
    > secure[¶](#http.cookies.Morsel.secure "Link to this definition")
    >
    > version[¶](#http.cookies.Morsel.version "Link to this definition")
    >
    > httponly[¶](#http.cookies.Morsel.httponly "Link to this definition")
    >
    > samesite[¶](#http.cookies.Morsel.samesite "Link to this definition")
    >
    > partitioned[¶](#http.cookies.Morsel.partitioned "Link to this definition")

    The attribute [`httponly`](#http.cookies.Morsel.httponly "http.cookies.Morsel.httponly") specifies that the cookie is only transferred
    in HTTP requests, and is not accessible through JavaScript. This is intended
    to mitigate some forms of cross-site scripting.

    The attribute [`samesite`](#http.cookies.Morsel.samesite "http.cookies.Morsel.samesite") controls when the browser sends the cookie with
    cross-site requests. This helps to mitigate CSRF attacks. Valid values are
    “Strict” (only sent with same-site requests), “Lax” (sent with same-site
    requests and top-level navigations), and “None” (sent with same-site and
    cross-site requests). When using “None”, the “secure” attribute must also
    be set, as required by modern browsers.

    The attribute [`partitioned`](#http.cookies.Morsel.partitioned "http.cookies.Morsel.partitioned") indicates to user agents that these
    cross-site cookies *should* only be available in the same top-level context
    that the cookie was first set in. For this to be accepted by the user agent,
    you **must** also set `Secure`.

    In addition, it is recommended to use the `__Host` prefix when setting
    partitioned cookies to make them bound to the hostname and not the
    registrable domain. Read
    [CHIPS (Cookies Having Independent Partitioned State)](https://github.com/privacycg/CHIPS/blob/main/README.md)
    for full details and examples.

    The keys are case-insensitive and their default value is `''`.

    Changed in version 3.5: `__eq__()` now takes [`key`](#http.cookies.Morsel.key "http.cookies.Morsel.key") and [`value`](#http.cookies.Morsel.value "http.cookies.Morsel.value")
    into account.

    Changed in version 3.7: Attributes [`key`](#http.cookies.Morsel.key "http.cookies.Morsel.key"), [`value`](#http.cookies.Morsel.value "http.cookies.Morsel.value") and
    [`coded_value`](#http.cookies.Morsel.coded_value "http.cookies.Morsel.coded_value") are read-only. Use [`set()`](#http.cookies.Morsel.set "http.cookies.Morsel.set") for
    setting them.

    Changed in version 3.8: Added support for the [`samesite`](#http.cookies.Morsel.samesite "http.cookies.Morsel.samesite") attribute.

    Changed in version 3.14: Added support for the [`partitioned`](#http.cookies.Morsel.partitioned "http.cookies.Morsel.partitioned") attribute.

Morsel.value[¶](#http.cookies.Morsel.value "Link to this definition")
:   The value of the cookie.

Morsel.coded\_value[¶](#http.cookies.Morsel.coded_value "Link to this definition")
:   The encoded value of the cookie — this is what should be sent.

Morsel.key[¶](#http.cookies.Morsel.key "Link to this definition")
:   The name of the cookie.

Morsel.set(*key*, *value*, *coded\_value*)[¶](#http.cookies.Morsel.set "Link to this definition")
:   Set the *key*, *value* and *coded\_value* attributes.

Morsel.isReservedKey(*K*)[¶](#http.cookies.Morsel.isReservedKey "Link to this definition")
:   Whether *K* is a member of the set of keys of a [`Morsel`](#http.cookies.Morsel "http.cookies.Morsel").

Morsel.output(*attrs=None*, *header='Set-Cookie:'*)[¶](#http.cookies.Morsel.output "Link to this definition")
:   Return a string representation of the Morsel, suitable to be sent as an HTTP
    header. By default, all the attributes are included, unless *attrs* is given, in
    which case it should be a list of attributes to use. *header* is by default
    `"Set-Cookie:"`.

Morsel.js\_output(*attrs=None*)[¶](#http.cookies.Morsel.js_output "Link to this definition")
:   Return an embeddable JavaScript snippet, which, if run on a browser which
    supports JavaScript, will act the same as if the HTTP header was sent.

    The meaning for *attrs* is the same as in [`output()`](#http.cookies.Morsel.output "http.cookies.Morsel.output").

Morsel.OutputString(*attrs=None*)[¶](#http.cookies.Morsel.OutputString "Link to this definition")
:   Return a string representing the Morsel, without any surrounding HTTP or
    JavaScript.

    The meaning for *attrs* is the same as in [`output()`](#http.cookies.Morsel.output "http.cookies.Morsel.output").

Morsel.update(*values*)[¶](#http.cookies.Morsel.update "Link to this definition")
:   Update the values in the Morsel dictionary with the values in the dictionary
    *values*. Raise an error if any of the keys in the *values* dict is not a
    valid [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) attribute.

    Changed in version 3.5: an error is raised for invalid keys.

Morsel.copy(*value*)[¶](#http.cookies.Morsel.copy "Link to this definition")
:   Return a shallow copy of the Morsel object.

    Changed in version 3.5: return a Morsel object instead of a dict.

Morsel.setdefault(*key*, *value=None*)[¶](#http.cookies.Morsel.setdefault "Link to this definition")
:   Raise an error if key is not a valid [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) attribute, otherwise
    behave the same as [`dict.setdefault()`](stdtypes.html#dict.setdefault "dict.setdefault").

## Example[¶](#example "Link to this heading")

The following example demonstrates how to use the `http.cookies` module.

```
>>> from http import cookies
>>> C = cookies.SimpleCookie()
>>> C["fig"] = "newton"
>>> C["sugar"] = "wafer"
>>> print(C) # generate HTTP headers
Set-Cookie: fig=newton
Set-Cookie: sugar=wafer
>>> print(C.output()) # same thing
Set-Cookie: fig=newton
Set-Cookie: sugar=wafer
>>> C = cookies.SimpleCookie()
>>> C["rocky"] = "road"
>>> C["rocky"]["path"] = "/cookie"
>>> print(C.output(header="Cookie:"))
Cookie: rocky=road; Path=/cookie
>>> print(C.output(attrs=[], header="Cookie:"))
Cookie: rocky=road
>>> C = cookies.SimpleCookie()
>>> C.load("chips=ahoy; vienna=finger") # load from a string (HTTP header)
>>> print(C)
Set-Cookie: chips=ahoy
Set-Cookie: vienna=finger
>>> C = cookies.SimpleCookie()
>>> C.load('keebler="E=everybody; L=\\"Loves\\"; fudge=;";')
>>> print(C)
Set-Cookie: keebler="E=everybody; L=\"Loves\"; fudge=;"
>>> C = cookies.SimpleCookie()
>>> C["oreo"] = "doublestuff"
>>> C["oreo"]["path"] = "/"
>>> print(C)
Set-Cookie: oreo=doublestuff; Path=/
>>> C = cookies.SimpleCookie()
>>> C["twix"] = "none for you"
>>> C["twix"].value
'none for you'
>>> C = cookies.SimpleCookie()
>>> C["number"] = 7 # equivalent to C["number"] = str(7)
>>> C["string"] = "seven"
>>> C["number"].value
'7'
>>> C["string"].value
'seven'
>>> print(C)
Set-Cookie: number=7
Set-Cookie: string=seven
```

### [Table of Contents](../contents.html)

* [`http.cookies` — HTTP state management](#)
  + [Cookie Objects](#cookie-objects)
  + [Morsel Objects](#morsel-objects)
  + [Example](#example)

#### Previous topic

[`http.server` — HTTP servers](http.server.html "previous chapter")

#### Next topic

[`http.cookiejar` — Cookie handling for HTTP clients](http.cookiejar.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/http.cookies.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](http.cookiejar.html "http.cookiejar — Cookie handling for HTTP clients") |
* [previous](http.server.html "http.server — HTTP servers") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Protocols and Support](internet.html) »
* `http.cookies` — HTTP state management
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
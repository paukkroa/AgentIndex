### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](xmlrpc.html "xmlrpc — XMLRPC server and client modules") |
* [previous](http.cookies.html "http.cookies — HTTP state management") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Protocols and Support](internet.html) »
* `http.cookiejar` — Cookie handling for HTTP clients
* |
* Theme
  Auto
  Light
  Dark
   |

# `http.cookiejar` — Cookie handling for HTTP clients[¶](#module-http.cookiejar "Link to this heading")

**Source code:** [Lib/http/cookiejar.py](https://github.com/python/cpython/tree/3.14/Lib/http/cookiejar.py)

---

The `http.cookiejar` module defines classes for automatic handling of HTTP
cookies. It is useful for accessing websites that require small pieces of data
– *cookies* – to be set on the client machine by an HTTP response from a
web server, and then returned to the server in later HTTP requests.

Both the regular Netscape cookie protocol and the protocol defined by
[**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) are handled. RFC 2965 handling is switched off by default.
[**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) cookies are parsed as Netscape cookies and subsequently treated
either as Netscape or RFC 2965 cookies according to the ‘policy’ in effect.
Note that the great majority of cookies on the internet are Netscape cookies.
`http.cookiejar` attempts to follow the de-facto Netscape cookie protocol (which
differs substantially from that set out in the original Netscape specification),
including taking note of the `max-age` and `port` cookie-attributes
introduced with RFC 2965.

Note

The various named parameters found in *Set-Cookie* and
*Set-Cookie2* headers (eg. `domain` and `expires`) are
conventionally referred to as *attributes*. To distinguish them from
Python attributes, the documentation for this module uses the term
*cookie-attribute* instead.

The module defines the following exception:

*exception* http.cookiejar.LoadError[¶](#http.cookiejar.LoadError "Link to this definition")
:   Instances of [`FileCookieJar`](#http.cookiejar.FileCookieJar "http.cookiejar.FileCookieJar") raise this exception on failure to load
    cookies from a file. [`LoadError`](#http.cookiejar.LoadError "http.cookiejar.LoadError") is a subclass of [`OSError`](exceptions.html#OSError "OSError").

    Changed in version 3.3: [`LoadError`](#http.cookiejar.LoadError "http.cookiejar.LoadError") used to be a subtype of [`IOError`](exceptions.html#IOError "IOError"), which is now an
    alias of [`OSError`](exceptions.html#OSError "OSError").

The following classes are provided:

*class* http.cookiejar.CookieJar(*policy=None*)[¶](#http.cookiejar.CookieJar "Link to this definition")
:   *policy* is an object implementing the [`CookiePolicy`](#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") interface.

    The [`CookieJar`](#http.cookiejar.CookieJar "http.cookiejar.CookieJar") class stores HTTP cookies. It extracts cookies from HTTP
    requests, and returns them in HTTP responses. [`CookieJar`](#http.cookiejar.CookieJar "http.cookiejar.CookieJar") instances
    automatically expire contained cookies when necessary. Subclasses are also
    responsible for storing and retrieving cookies from a file or database.

*class* http.cookiejar.FileCookieJar(*filename=None*, *delayload=None*, *policy=None*)[¶](#http.cookiejar.FileCookieJar "Link to this definition")
:   *policy* is an object implementing the [`CookiePolicy`](#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") interface. For the
    other arguments, see the documentation for the corresponding attributes.

    A [`CookieJar`](#http.cookiejar.CookieJar "http.cookiejar.CookieJar") which can load cookies from, and perhaps save cookies to, a
    file on disk. Cookies are **NOT** loaded from the named file until either the
    [`load()`](#http.cookiejar.FileCookieJar.load "http.cookiejar.FileCookieJar.load") or [`revert()`](#http.cookiejar.FileCookieJar.revert "http.cookiejar.FileCookieJar.revert") method is called. Subclasses of this class are
    documented in section [FileCookieJar subclasses and co-operation with web browsers](#file-cookie-jar-classes).

    This should not be initialized directly – use its subclasses below instead.

    Changed in version 3.8: The filename parameter supports a [path-like object](../glossary.html#term-path-like-object).

*class* http.cookiejar.CookiePolicy[¶](#http.cookiejar.CookiePolicy "Link to this definition")
:   This class is responsible for deciding whether each cookie should be accepted
    from / returned to the server.

*class* http.cookiejar.DefaultCookiePolicy(*blocked\_domains=None*, *allowed\_domains=None*, *netscape=True*, *rfc2965=False*, *rfc2109\_as\_netscape=None*, *hide\_cookie2=False*, *strict\_domain=False*, *strict\_rfc2965\_unverifiable=True*, *strict\_ns\_unverifiable=False*, *strict\_ns\_domain=DefaultCookiePolicy.DomainLiberal*, *strict\_ns\_set\_initial\_dollar=False*, *strict\_ns\_set\_path=False*, *secure\_protocols=('https', 'wss')*)[¶](#http.cookiejar.DefaultCookiePolicy "Link to this definition")
:   Constructor arguments should be passed as keyword arguments only.
    *blocked\_domains* is a sequence of domain names that we never accept cookies
    from, nor return cookies to. *allowed\_domains* if not [`None`](constants.html#None "None"), this is a
    sequence of the only domains for which we accept and return cookies.
    *secure\_protocols* is a sequence of protocols for which secure cookies can be
    added to. By default *https* and *wss* (secure websocket) are considered
    secure protocols. For all other arguments, see the documentation for
    [`CookiePolicy`](#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") and [`DefaultCookiePolicy`](#http.cookiejar.DefaultCookiePolicy "http.cookiejar.DefaultCookiePolicy") objects.

    [`DefaultCookiePolicy`](#http.cookiejar.DefaultCookiePolicy "http.cookiejar.DefaultCookiePolicy") implements the standard accept / reject rules for
    Netscape and [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) cookies. By default, [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) cookies (ie. cookies
    received in a *Set-Cookie* header with a version cookie-attribute of
    1) are treated according to the RFC 2965 rules. However, if RFC 2965 handling
    is turned off or [`rfc2109_as_netscape`](#http.cookiejar.DefaultCookiePolicy.rfc2109_as_netscape "http.cookiejar.DefaultCookiePolicy.rfc2109_as_netscape") is `True`, RFC 2109 cookies are
    ‘downgraded’ by the [`CookieJar`](#http.cookiejar.CookieJar "http.cookiejar.CookieJar") instance to Netscape cookies, by
    setting the `version` attribute of the [`Cookie`](#http.cookiejar.Cookie "http.cookiejar.Cookie") instance to 0.
    [`DefaultCookiePolicy`](#http.cookiejar.DefaultCookiePolicy "http.cookiejar.DefaultCookiePolicy") also provides some parameters to allow some
    fine-tuning of policy.

*class* http.cookiejar.Cookie[¶](#http.cookiejar.Cookie "Link to this definition")
:   This class represents Netscape, [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) and [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) cookies. It is not
    expected that users of `http.cookiejar` construct their own [`Cookie`](#http.cookiejar.Cookie "http.cookiejar.Cookie")
    instances. Instead, if necessary, call `make_cookies()` on a
    [`CookieJar`](#http.cookiejar.CookieJar "http.cookiejar.CookieJar") instance.

See also

Module [`urllib.request`](urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.")
:   URL opening with automatic cookie handling.

Module [`http.cookies`](http.cookies.html#module-http.cookies "http.cookies: Support for HTTP state management (cookies).")
:   HTTP cookie classes, principally useful for server-side code. The
    `http.cookiejar` and [`http.cookies`](http.cookies.html#module-http.cookies "http.cookies: Support for HTTP state management (cookies).") modules do not depend on each
    other.

<https://curl.se/rfc/cookie_spec.html>
:   The specification of the original Netscape cookie protocol. Though this is
    still the dominant protocol, the ‘Netscape cookie protocol’ implemented by all
    the major browsers (and `http.cookiejar`) only bears a passing resemblance to
    the one sketched out in `cookie_spec.html`.

[**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) - HTTP State Management Mechanism
:   Obsoleted by [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html). Uses *Set-Cookie* with version=1.

[**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) - HTTP State Management Mechanism
:   The Netscape protocol with the bugs fixed. Uses *Set-Cookie2* in
    place of *Set-Cookie*. Not widely used.

<https://kristol.org/cookie/errata.html>
:   Unfinished errata to [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html).

[**RFC 2964**](https://datatracker.ietf.org/doc/html/rfc2964.html) - Use of HTTP State Management

## CookieJar and FileCookieJar Objects[¶](#cookiejar-and-filecookiejar-objects "Link to this heading")

[`CookieJar`](#http.cookiejar.CookieJar "http.cookiejar.CookieJar") objects support the [iterator](../glossary.html#term-iterator) protocol for iterating over
contained [`Cookie`](#http.cookiejar.Cookie "http.cookiejar.Cookie") objects.

[`CookieJar`](#http.cookiejar.CookieJar "http.cookiejar.CookieJar") has the following methods:

CookieJar.add\_cookie\_header(*request*)[¶](#http.cookiejar.CookieJar.add_cookie_header "Link to this definition")
:   Add correct *Cookie* header to *request*.

    If policy allows (ie. the `rfc2965` and `hide_cookie2` attributes of
    the [`CookieJar`](#http.cookiejar.CookieJar "http.cookiejar.CookieJar")’s [`CookiePolicy`](#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") instance are true and false
    respectively), the *Cookie2* header is also added when appropriate.

    The *request* object (usually a [`urllib.request.Request`](urllib.request.html#urllib.request.Request "urllib.request.Request") instance)
    must support the methods `get_full_url()`, `has_header()`,
    `get_header()`, `header_items()`, `add_unredirected_header()`
    and the attributes `host`, `type`, `unverifiable`
    and `origin_req_host` as documented by [`urllib.request`](urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.").

    Changed in version 3.3: *request* object needs `origin_req_host` attribute. Dependency on a
    deprecated method `get_origin_req_host()` has been removed.

CookieJar.extract\_cookies(*response*, *request*)[¶](#http.cookiejar.CookieJar.extract_cookies "Link to this definition")
:   Extract cookies from HTTP *response* and store them in the [`CookieJar`](#http.cookiejar.CookieJar "http.cookiejar.CookieJar"),
    where allowed by policy.

    The [`CookieJar`](#http.cookiejar.CookieJar "http.cookiejar.CookieJar") will look for allowable *Set-Cookie* and
    *Set-Cookie2* headers in the *response* argument, and store cookies
    as appropriate (subject to the [`CookiePolicy.set_ok()`](#http.cookiejar.CookiePolicy.set_ok "http.cookiejar.CookiePolicy.set_ok") method’s approval).

    The *response* object (usually the result of a call to
    [`urllib.request.urlopen()`](urllib.request.html#urllib.request.urlopen "urllib.request.urlopen"), or similar) should support an `info()`
    method, which returns an [`email.message.Message`](email.compat32-message.html#email.message.Message "email.message.Message") instance.

    The *request* object (usually a [`urllib.request.Request`](urllib.request.html#urllib.request.Request "urllib.request.Request") instance)
    must support the method `get_full_url()` and the attributes
    `host`, `unverifiable` and `origin_req_host`,
    as documented by [`urllib.request`](urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs."). The request is used to set
    default values for cookie-attributes as well as for checking that the
    cookie is allowed to be set.

    Changed in version 3.3: *request* object needs `origin_req_host` attribute. Dependency on a
    deprecated method `get_origin_req_host()` has been removed.

CookieJar.set\_policy(*policy*)[¶](#http.cookiejar.CookieJar.set_policy "Link to this definition")
:   Set the [`CookiePolicy`](#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") instance to be used.

CookieJar.make\_cookies(*response*, *request*)[¶](#http.cookiejar.CookieJar.make_cookies "Link to this definition")
:   Return sequence of [`Cookie`](#http.cookiejar.Cookie "http.cookiejar.Cookie") objects extracted from *response* object.

    See the documentation for [`extract_cookies()`](#http.cookiejar.CookieJar.extract_cookies "http.cookiejar.CookieJar.extract_cookies") for the interfaces required of
    the *response* and *request* arguments.

CookieJar.set\_cookie\_if\_ok(*cookie*, *request*)[¶](#http.cookiejar.CookieJar.set_cookie_if_ok "Link to this definition")
:   Set a [`Cookie`](#http.cookiejar.Cookie "http.cookiejar.Cookie") if policy says it’s OK to do so.

CookieJar.set\_cookie(*cookie*)[¶](#http.cookiejar.CookieJar.set_cookie "Link to this definition")
:   Set a [`Cookie`](#http.cookiejar.Cookie "http.cookiejar.Cookie"), without checking with policy to see whether or not it
    should be set.

CookieJar.clear([*domain*[, *path*[, *name*]]])[¶](#http.cookiejar.CookieJar.clear "Link to this definition")
:   Clear some cookies.

    If invoked without arguments, clear all cookies. If given a single argument,
    only cookies belonging to that *domain* will be removed. If given two arguments,
    cookies belonging to the specified *domain* and URL *path* are removed. If
    given three arguments, then the cookie with the specified *domain*, *path* and
    *name* is removed.

    Raises [`KeyError`](exceptions.html#KeyError "KeyError") if no matching cookie exists.

CookieJar.clear\_session\_cookies()[¶](#http.cookiejar.CookieJar.clear_session_cookies "Link to this definition")
:   Discard all session cookies.

    Discards all contained cookies that have a true `discard` attribute
    (usually because they had either no `max-age` or `expires` cookie-attribute,
    or an explicit `discard` cookie-attribute). For interactive browsers, the end
    of a session usually corresponds to closing the browser window.

    Note that the `save()` method won’t save session cookies anyway, unless you
    ask otherwise by passing a true *ignore\_discard* argument.

[`FileCookieJar`](#http.cookiejar.FileCookieJar "http.cookiejar.FileCookieJar") implements the following additional methods:

FileCookieJar.save(*filename=None*, *ignore\_discard=False*, *ignore\_expires=False*)[¶](#http.cookiejar.FileCookieJar.save "Link to this definition")
:   Save cookies to a file.

    This base class raises [`NotImplementedError`](exceptions.html#NotImplementedError "NotImplementedError"). Subclasses may leave this
    method unimplemented.

    *filename* is the name of file in which to save cookies. If *filename* is not
    specified, `self.filename` is used (whose default is the value passed to
    the constructor, if any); if `self.filename` is [`None`](constants.html#None "None"),
    [`ValueError`](exceptions.html#ValueError "ValueError") is raised.

    *ignore\_discard*: save even cookies set to be discarded. *ignore\_expires*: save
    even cookies that have expired

    The file is overwritten if it already exists, thus wiping all the cookies it
    contains. Saved cookies can be restored later using the [`load()`](#http.cookiejar.FileCookieJar.load "http.cookiejar.FileCookieJar.load") or
    [`revert()`](#http.cookiejar.FileCookieJar.revert "http.cookiejar.FileCookieJar.revert") methods.

FileCookieJar.load(*filename=None*, *ignore\_discard=False*, *ignore\_expires=False*)[¶](#http.cookiejar.FileCookieJar.load "Link to this definition")
:   Load cookies from a file.

    Old cookies are kept unless overwritten by newly loaded ones.

    Arguments are as for [`save()`](#http.cookiejar.FileCookieJar.save "http.cookiejar.FileCookieJar.save").

    The named file must be in the format understood by the class, or
    [`LoadError`](#http.cookiejar.LoadError "http.cookiejar.LoadError") will be raised. Also, [`OSError`](exceptions.html#OSError "OSError") may be raised, for
    example if the file does not exist.

    Changed in version 3.3: [`IOError`](exceptions.html#IOError "IOError") used to be raised, it is now an alias of [`OSError`](exceptions.html#OSError "OSError").

FileCookieJar.revert(*filename=None*, *ignore\_discard=False*, *ignore\_expires=False*)[¶](#http.cookiejar.FileCookieJar.revert "Link to this definition")
:   Clear all cookies and reload cookies from a saved file.

    [`revert()`](#http.cookiejar.FileCookieJar.revert "http.cookiejar.FileCookieJar.revert") can raise the same exceptions as [`load()`](#http.cookiejar.FileCookieJar.load "http.cookiejar.FileCookieJar.load"). If there is a
    failure, the object’s state will not be altered.

[`FileCookieJar`](#http.cookiejar.FileCookieJar "http.cookiejar.FileCookieJar") instances have the following public attributes:

FileCookieJar.filename[¶](#http.cookiejar.FileCookieJar.filename "Link to this definition")
:   Filename of default file in which to keep cookies. This attribute may be
    assigned to.

FileCookieJar.delayload[¶](#http.cookiejar.FileCookieJar.delayload "Link to this definition")
:   If true, load cookies lazily from disk. This attribute should not be assigned
    to. This is only a hint, since this only affects performance, not behaviour
    (unless the cookies on disk are changing). A [`CookieJar`](#http.cookiejar.CookieJar "http.cookiejar.CookieJar") object may
    ignore it. None of the [`FileCookieJar`](#http.cookiejar.FileCookieJar "http.cookiejar.FileCookieJar") classes included in the standard
    library lazily loads cookies.

## FileCookieJar subclasses and co-operation with web browsers[¶](#filecookiejar-subclasses-and-co-operation-with-web-browsers "Link to this heading")

The following [`CookieJar`](#http.cookiejar.CookieJar "http.cookiejar.CookieJar") subclasses are provided for reading and
writing.

*class* http.cookiejar.MozillaCookieJar(*filename=None*, *delayload=None*, *policy=None*)[¶](#http.cookiejar.MozillaCookieJar "Link to this definition")
:   A [`FileCookieJar`](#http.cookiejar.FileCookieJar "http.cookiejar.FileCookieJar") that can load from and save cookies to disk in the
    Mozilla `cookies.txt` file format (which is also used by curl and the Lynx
    and Netscape browsers).

    Note

    This loses information about [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) cookies, and also about newer or
    non-standard cookie-attributes such as `port`.

    Warning

    Back up your cookies before saving if you have cookies whose loss / corruption
    would be inconvenient (there are some subtleties which may lead to slight
    changes in the file over a load / save round-trip).

    Also note that cookies saved while Mozilla is running will get clobbered by
    Mozilla.

*class* http.cookiejar.LWPCookieJar(*filename=None*, *delayload=None*, *policy=None*)[¶](#http.cookiejar.LWPCookieJar "Link to this definition")
:   A [`FileCookieJar`](#http.cookiejar.FileCookieJar "http.cookiejar.FileCookieJar") that can load from and save cookies to disk in format
    compatible with the libwww-perl library’s `Set-Cookie3` file format. This is
    convenient if you want to store cookies in a human-readable file.

    Changed in version 3.8: The filename parameter supports a [path-like object](../glossary.html#term-path-like-object).

## CookiePolicy Objects[¶](#cookiepolicy-objects "Link to this heading")

Objects implementing the [`CookiePolicy`](#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") interface have the following
methods:

CookiePolicy.set\_ok(*cookie*, *request*)[¶](#http.cookiejar.CookiePolicy.set_ok "Link to this definition")
:   Return boolean value indicating whether cookie should be accepted from server.

    *cookie* is a [`Cookie`](#http.cookiejar.Cookie "http.cookiejar.Cookie") instance. *request* is an object
    implementing the interface defined by the documentation for
    [`CookieJar.extract_cookies()`](#http.cookiejar.CookieJar.extract_cookies "http.cookiejar.CookieJar.extract_cookies").

CookiePolicy.return\_ok(*cookie*, *request*)[¶](#http.cookiejar.CookiePolicy.return_ok "Link to this definition")
:   Return boolean value indicating whether cookie should be returned to server.

    *cookie* is a [`Cookie`](#http.cookiejar.Cookie "http.cookiejar.Cookie") instance. *request* is an object
    implementing the interface defined by the documentation for
    [`CookieJar.add_cookie_header()`](#http.cookiejar.CookieJar.add_cookie_header "http.cookiejar.CookieJar.add_cookie_header").

CookiePolicy.domain\_return\_ok(*domain*, *request*)[¶](#http.cookiejar.CookiePolicy.domain_return_ok "Link to this definition")
:   Return `False` if cookies should not be returned, given cookie domain.

    This method is an optimization. It removes the need for checking every cookie
    with a particular domain (which might involve reading many files). Returning
    true from [`domain_return_ok()`](#http.cookiejar.CookiePolicy.domain_return_ok "http.cookiejar.CookiePolicy.domain_return_ok") and [`path_return_ok()`](#http.cookiejar.CookiePolicy.path_return_ok "http.cookiejar.CookiePolicy.path_return_ok") leaves all the
    work to [`return_ok()`](#http.cookiejar.CookiePolicy.return_ok "http.cookiejar.CookiePolicy.return_ok").

    If [`domain_return_ok()`](#http.cookiejar.CookiePolicy.domain_return_ok "http.cookiejar.CookiePolicy.domain_return_ok") returns true for the cookie domain,
    [`path_return_ok()`](#http.cookiejar.CookiePolicy.path_return_ok "http.cookiejar.CookiePolicy.path_return_ok") is called for the cookie path. Otherwise,
    [`path_return_ok()`](#http.cookiejar.CookiePolicy.path_return_ok "http.cookiejar.CookiePolicy.path_return_ok") and [`return_ok()`](#http.cookiejar.CookiePolicy.return_ok "http.cookiejar.CookiePolicy.return_ok") are never called for that cookie
    domain. If [`path_return_ok()`](#http.cookiejar.CookiePolicy.path_return_ok "http.cookiejar.CookiePolicy.path_return_ok") returns true, [`return_ok()`](#http.cookiejar.CookiePolicy.return_ok "http.cookiejar.CookiePolicy.return_ok") is called
    with the [`Cookie`](#http.cookiejar.Cookie "http.cookiejar.Cookie") object itself for a full check. Otherwise,
    [`return_ok()`](#http.cookiejar.CookiePolicy.return_ok "http.cookiejar.CookiePolicy.return_ok") is never called for that cookie path.

    Note that [`domain_return_ok()`](#http.cookiejar.CookiePolicy.domain_return_ok "http.cookiejar.CookiePolicy.domain_return_ok") is called for every *cookie* domain, not just
    for the *request* domain. For example, the function might be called with both
    `".example.com"` and `"www.example.com"` if the request domain is
    `"www.example.com"`. The same goes for [`path_return_ok()`](#http.cookiejar.CookiePolicy.path_return_ok "http.cookiejar.CookiePolicy.path_return_ok").

    The *request* argument is as documented for [`return_ok()`](#http.cookiejar.CookiePolicy.return_ok "http.cookiejar.CookiePolicy.return_ok").

CookiePolicy.path\_return\_ok(*path*, *request*)[¶](#http.cookiejar.CookiePolicy.path_return_ok "Link to this definition")
:   Return `False` if cookies should not be returned, given cookie path.

    See the documentation for [`domain_return_ok()`](#http.cookiejar.CookiePolicy.domain_return_ok "http.cookiejar.CookiePolicy.domain_return_ok").

In addition to implementing the methods above, implementations of the
[`CookiePolicy`](#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") interface must also supply the following attributes,
indicating which protocols should be used, and how. All of these attributes may
be assigned to.

CookiePolicy.netscape[¶](#http.cookiejar.CookiePolicy.netscape "Link to this definition")
:   Implement Netscape protocol.

CookiePolicy.rfc2965[¶](#http.cookiejar.CookiePolicy.rfc2965 "Link to this definition")
:   Implement [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) protocol.

CookiePolicy.hide\_cookie2[¶](#http.cookiejar.CookiePolicy.hide_cookie2 "Link to this definition")
:   Don’t add *Cookie2* header to requests (the presence of this header
    indicates to the server that we understand [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) cookies).

The most useful way to define a [`CookiePolicy`](#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") class is by subclassing
from [`DefaultCookiePolicy`](#http.cookiejar.DefaultCookiePolicy "http.cookiejar.DefaultCookiePolicy") and overriding some or all of the methods
above. [`CookiePolicy`](#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") itself may be used as a ‘null policy’ to allow
setting and receiving any and all cookies (this is unlikely to be useful).

## DefaultCookiePolicy Objects[¶](#defaultcookiepolicy-objects "Link to this heading")

Implements the standard rules for accepting and returning cookies.

Both [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) and Netscape cookies are covered. RFC 2965 handling is switched
off by default.

The easiest way to provide your own policy is to override this class and call
its methods in your overridden implementations before adding your own additional
checks:

```
import http.cookiejar
class MyCookiePolicy(http.cookiejar.DefaultCookiePolicy):
    def set_ok(self, cookie, request):
        if not http.cookiejar.DefaultCookiePolicy.set_ok(self, cookie, request):
            return False
        if i_dont_want_to_store_this_cookie(cookie):
            return False
        return True
```

In addition to the features required to implement the [`CookiePolicy`](#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy")
interface, this class allows you to block and allow domains from setting and
receiving cookies. There are also some strictness switches that allow you to
tighten up the rather loose Netscape protocol rules a little bit (at the cost of
blocking some benign cookies).

A domain blocklist and allowlist is provided (both off by default). Only domains
not in the blocklist and present in the allowlist (if the allowlist is active)
participate in cookie setting and returning. Use the *blocked\_domains*
constructor argument, and `blocked_domains()` and
`set_blocked_domains()` methods (and the corresponding argument and methods
for *allowed\_domains*). If you set an allowlist, you can turn it off again by
setting it to [`None`](constants.html#None "None").

Domains in block or allow lists that do not start with a dot must equal the
cookie domain to be matched. For example, `"example.com"` matches a blocklist
entry of `"example.com"`, but `"www.example.com"` does not. Domains that do
start with a dot are matched by more specific domains too. For example, both
`"www.example.com"` and `"www.coyote.example.com"` match `".example.com"`
(but `"example.com"` itself does not). IP addresses are an exception, and
must match exactly. For example, if blocked\_domains contains `"192.168.1.2"`
and `".168.1.2"`, 192.168.1.2 is blocked, but 193.168.1.2 is not.

[`DefaultCookiePolicy`](#http.cookiejar.DefaultCookiePolicy "http.cookiejar.DefaultCookiePolicy") implements the following additional methods:

DefaultCookiePolicy.blocked\_domains()[¶](#http.cookiejar.DefaultCookiePolicy.blocked_domains "Link to this definition")
:   Return the sequence of blocked domains (as a tuple).

DefaultCookiePolicy.set\_blocked\_domains(*blocked\_domains*)[¶](#http.cookiejar.DefaultCookiePolicy.set_blocked_domains "Link to this definition")
:   Set the sequence of blocked domains.

DefaultCookiePolicy.is\_blocked(*domain*)[¶](#http.cookiejar.DefaultCookiePolicy.is_blocked "Link to this definition")
:   Return `True` if *domain* is on the blocklist for setting or receiving
    cookies.

DefaultCookiePolicy.allowed\_domains()[¶](#http.cookiejar.DefaultCookiePolicy.allowed_domains "Link to this definition")
:   Return [`None`](constants.html#None "None"), or the sequence of allowed domains (as a tuple).

DefaultCookiePolicy.set\_allowed\_domains(*allowed\_domains*)[¶](#http.cookiejar.DefaultCookiePolicy.set_allowed_domains "Link to this definition")
:   Set the sequence of allowed domains, or [`None`](constants.html#None "None").

DefaultCookiePolicy.is\_not\_allowed(*domain*)[¶](#http.cookiejar.DefaultCookiePolicy.is_not_allowed "Link to this definition")
:   Return `True` if *domain* is not on the allowlist for setting or receiving
    cookies.

[`DefaultCookiePolicy`](#http.cookiejar.DefaultCookiePolicy "http.cookiejar.DefaultCookiePolicy") instances have the following attributes, which are
all initialised from the constructor arguments of the same name, and which may
all be assigned to.

DefaultCookiePolicy.rfc2109\_as\_netscape[¶](#http.cookiejar.DefaultCookiePolicy.rfc2109_as_netscape "Link to this definition")
:   If true, request that the [`CookieJar`](#http.cookiejar.CookieJar "http.cookiejar.CookieJar") instance downgrade [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) cookies
    (ie. cookies received in a *Set-Cookie* header with a version
    cookie-attribute of 1) to Netscape cookies by setting the version attribute of
    the [`Cookie`](#http.cookiejar.Cookie "http.cookiejar.Cookie") instance to 0. The default value is [`None`](constants.html#None "None"), in which
    case RFC 2109 cookies are downgraded if and only if [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) handling is turned
    off. Therefore, RFC 2109 cookies are downgraded by default.

General strictness switches:

DefaultCookiePolicy.strict\_domain[¶](#http.cookiejar.DefaultCookiePolicy.strict_domain "Link to this definition")
:   Don’t allow sites to set two-component domains with country-code top-level
    domains like `.co.uk`, `.gov.uk`, `.co.nz`.etc. This is far from perfect
    and isn’t guaranteed to work!

[**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) protocol strictness switches:

DefaultCookiePolicy.strict\_rfc2965\_unverifiable[¶](#http.cookiejar.DefaultCookiePolicy.strict_rfc2965_unverifiable "Link to this definition")
:   Follow [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) rules on unverifiable transactions (usually, an unverifiable
    transaction is one resulting from a redirect or a request for an image hosted on
    another site). If this is false, cookies are *never* blocked on the basis of
    verifiability

Netscape protocol strictness switches:

DefaultCookiePolicy.strict\_ns\_unverifiable[¶](#http.cookiejar.DefaultCookiePolicy.strict_ns_unverifiable "Link to this definition")
:   Apply [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) rules on unverifiable transactions even to Netscape cookies.

DefaultCookiePolicy.strict\_ns\_domain[¶](#http.cookiejar.DefaultCookiePolicy.strict_ns_domain "Link to this definition")
:   Flags indicating how strict to be with domain-matching rules for Netscape
    cookies. See below for acceptable values.

DefaultCookiePolicy.strict\_ns\_set\_initial\_dollar[¶](#http.cookiejar.DefaultCookiePolicy.strict_ns_set_initial_dollar "Link to this definition")
:   Ignore cookies in Set-Cookie: headers that have names starting with `'$'`.

DefaultCookiePolicy.strict\_ns\_set\_path[¶](#http.cookiejar.DefaultCookiePolicy.strict_ns_set_path "Link to this definition")
:   Don’t allow setting cookies whose path doesn’t path-match request URI.

[`strict_ns_domain`](#http.cookiejar.DefaultCookiePolicy.strict_ns_domain "http.cookiejar.DefaultCookiePolicy.strict_ns_domain") is a collection of flags. Its value is constructed by
or-ing together (for example, `DomainStrictNoDots|DomainStrictNonDomain` means
both flags are set).

DefaultCookiePolicy.DomainStrictNoDots[¶](#http.cookiejar.DefaultCookiePolicy.DomainStrictNoDots "Link to this definition")
:   When setting cookies, the ‘host prefix’ must not contain a dot (eg.
    `www.foo.bar.com` can’t set a cookie for `.bar.com`, because `www.foo`
    contains a dot).

DefaultCookiePolicy.DomainStrictNonDomain[¶](#http.cookiejar.DefaultCookiePolicy.DomainStrictNonDomain "Link to this definition")
:   Cookies that did not explicitly specify a `domain` cookie-attribute can only
    be returned to a domain equal to the domain that set the cookie (eg.
    `spam.example.com` won’t be returned cookies from `example.com` that had no
    `domain` cookie-attribute).

DefaultCookiePolicy.DomainRFC2965Match[¶](#http.cookiejar.DefaultCookiePolicy.DomainRFC2965Match "Link to this definition")
:   When setting cookies, require a full [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) domain-match.

The following attributes are provided for convenience, and are the most useful
combinations of the above flags:

DefaultCookiePolicy.DomainLiberal[¶](#http.cookiejar.DefaultCookiePolicy.DomainLiberal "Link to this definition")
:   Equivalent to 0 (ie. all of the above Netscape domain strictness flags switched
    off).

DefaultCookiePolicy.DomainStrict[¶](#http.cookiejar.DefaultCookiePolicy.DomainStrict "Link to this definition")
:   Equivalent to `DomainStrictNoDots|DomainStrictNonDomain`.

## Cookie Objects[¶](#cookie-objects "Link to this heading")

[`Cookie`](#http.cookiejar.Cookie "http.cookiejar.Cookie") instances have Python attributes roughly corresponding to the
standard cookie-attributes specified in the various cookie standards. The
correspondence is not one-to-one, because there are complicated rules for
assigning default values, because the `max-age` and `expires`
cookie-attributes contain equivalent information, and because [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) cookies
may be ‘downgraded’ by `http.cookiejar` from version 1 to version 0 (Netscape)
cookies.

Assignment to these attributes should not be necessary other than in rare
circumstances in a [`CookiePolicy`](#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") method. The class does not enforce
internal consistency, so you should know what you’re doing if you do that.

Cookie.version[¶](#http.cookiejar.Cookie.version "Link to this definition")
:   Integer or [`None`](constants.html#None "None"). Netscape cookies have [`version`](#http.cookiejar.Cookie.version "http.cookiejar.Cookie.version") 0. [**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) and
    [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) cookies have a `version` cookie-attribute of 1. However, note that
    `http.cookiejar` may ‘downgrade’ RFC 2109 cookies to Netscape cookies, in which
    case [`version`](#http.cookiejar.Cookie.version "http.cookiejar.Cookie.version") is 0.

Cookie.name[¶](#http.cookiejar.Cookie.name "Link to this definition")
:   Cookie name (a string).

Cookie.value[¶](#http.cookiejar.Cookie.value "Link to this definition")
:   Cookie value (a string), or [`None`](constants.html#None "None").

Cookie.port[¶](#http.cookiejar.Cookie.port "Link to this definition")
:   String representing a port or a set of ports (eg. ‘80’, or ‘80,8080’), or
    [`None`](constants.html#None "None").

Cookie.domain[¶](#http.cookiejar.Cookie.domain "Link to this definition")
:   Cookie domain (a string).

Cookie.path[¶](#http.cookiejar.Cookie.path "Link to this definition")
:   Cookie path (a string, eg. `'/acme/rocket_launchers'`).

Cookie.secure[¶](#http.cookiejar.Cookie.secure "Link to this definition")
:   `True` if cookie should only be returned over a secure connection.

Cookie.expires[¶](#http.cookiejar.Cookie.expires "Link to this definition")
:   Integer expiry date in seconds since epoch, or [`None`](constants.html#None "None"). See also the
    [`is_expired()`](#http.cookiejar.Cookie.is_expired "http.cookiejar.Cookie.is_expired") method.

Cookie.discard[¶](#http.cookiejar.Cookie.discard "Link to this definition")
:   `True` if this is a session cookie.

Cookie.comment[¶](#http.cookiejar.Cookie.comment "Link to this definition")
:   String comment from the server explaining the function of this cookie, or
    [`None`](constants.html#None "None").

Cookie.comment\_url[¶](#http.cookiejar.Cookie.comment_url "Link to this definition")
:   URL linking to a comment from the server explaining the function of this cookie,
    or [`None`](constants.html#None "None").

Cookie.rfc2109[¶](#http.cookiejar.Cookie.rfc2109 "Link to this definition")
:   `True` if this cookie was received as an [**RFC 2109**](https://datatracker.ietf.org/doc/html/rfc2109.html) cookie (ie. the cookie
    arrived in a *Set-Cookie* header, and the value of the Version
    cookie-attribute in that header was 1). This attribute is provided because
    `http.cookiejar` may ‘downgrade’ RFC 2109 cookies to Netscape cookies, in
    which case [`version`](#http.cookiejar.Cookie.version "http.cookiejar.Cookie.version") is 0.

Cookie.port\_specified[¶](#http.cookiejar.Cookie.port_specified "Link to this definition")
:   `True` if a port or set of ports was explicitly specified by the server (in the
    *Set-Cookie* / *Set-Cookie2* header).

Cookie.domain\_specified[¶](#http.cookiejar.Cookie.domain_specified "Link to this definition")
:   `True` if a domain was explicitly specified by the server.

Cookie.domain\_initial\_dot[¶](#http.cookiejar.Cookie.domain_initial_dot "Link to this definition")
:   `True` if the domain explicitly specified by the server began with a dot
    (`'.'`).

Cookies may have additional non-standard cookie-attributes. These may be
accessed using the following methods:

Cookie.has\_nonstandard\_attr(*name*)[¶](#http.cookiejar.Cookie.has_nonstandard_attr "Link to this definition")
:   Return `True` if cookie has the named cookie-attribute.

Cookie.get\_nonstandard\_attr(*name*, *default=None*)[¶](#http.cookiejar.Cookie.get_nonstandard_attr "Link to this definition")
:   If cookie has the named cookie-attribute, return its value. Otherwise, return
    *default*.

Cookie.set\_nonstandard\_attr(*name*, *value*)[¶](#http.cookiejar.Cookie.set_nonstandard_attr "Link to this definition")
:   Set the value of the named cookie-attribute.

The [`Cookie`](#http.cookiejar.Cookie "http.cookiejar.Cookie") class also defines the following method:

Cookie.is\_expired(*now=None*)[¶](#http.cookiejar.Cookie.is_expired "Link to this definition")
:   `True` if cookie has passed the time at which the server requested it should
    expire. If *now* is given (in seconds since the epoch), return whether the
    cookie has expired at the specified time.

## Examples[¶](#examples "Link to this heading")

The first example shows the most common usage of `http.cookiejar`:

```
import http.cookiejar, urllib.request
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://example.com/")
```

This example illustrates how to open a URL using your Netscape, Mozilla, or Lynx
cookies (assumes Unix/Netscape convention for location of the cookies file):

```
import os, http.cookiejar, urllib.request
cj = http.cookiejar.MozillaCookieJar()
cj.load(os.path.join(os.path.expanduser("~"), ".netscape", "cookies.txt"))
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://example.com/")
```

The next example illustrates the use of [`DefaultCookiePolicy`](#http.cookiejar.DefaultCookiePolicy "http.cookiejar.DefaultCookiePolicy"). Turn on
[**RFC 2965**](https://datatracker.ietf.org/doc/html/rfc2965.html) cookies, be more strict about domains when setting and returning
Netscape cookies, and block some domains from setting cookies or having them
returned:

```
import urllib.request
from http.cookiejar import CookieJar, DefaultCookiePolicy
policy = DefaultCookiePolicy(
    rfc2965=True, strict_ns_domain=Policy.DomainStrict,
    blocked_domains=["ads.net", ".ads.net"])
cj = CookieJar(policy)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://example.com/")
```

### [Table of Contents](../contents.html)

* [`http.cookiejar` — Cookie handling for HTTP clients](#)
  + [CookieJar and FileCookieJar Objects](#cookiejar-and-filecookiejar-objects)
  + [FileCookieJar subclasses and co-operation with web browsers](#filecookiejar-subclasses-and-co-operation-with-web-browsers)
  + [CookiePolicy Objects](#cookiepolicy-objects)
  + [DefaultCookiePolicy Objects](#defaultcookiepolicy-objects)
  + [Cookie Objects](#cookie-objects)
  + [Examples](#examples)

#### Previous topic

[`http.cookies` — HTTP state management](http.cookies.html "previous chapter")

#### Next topic

[`xmlrpc` — XMLRPC server and client modules](xmlrpc.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/http.cookiejar.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](xmlrpc.html "xmlrpc — XMLRPC server and client modules") |
* [previous](http.cookies.html "http.cookies — HTTP state management") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internet Protocols and Support](internet.html) »
* `http.cookiejar` — Cookie handling for HTTP clients
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
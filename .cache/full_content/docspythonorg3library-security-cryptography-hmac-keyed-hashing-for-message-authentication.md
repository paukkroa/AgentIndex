### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](secrets.html "secrets — Generate secure random numbers for managing secrets") |
* [previous](hashlib.html "hashlib — Secure hashes and message digests") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Cryptographic Services](crypto.html) »
* `hmac` — Keyed-Hashing for Message Authentication
* |
* Theme
  Auto
  Light
  Dark
   |

# `hmac` — Keyed-Hashing for Message Authentication[¶](#module-hmac "Link to this heading")

**Source code:** [Lib/hmac.py](https://github.com/python/cpython/tree/3.14/Lib/hmac.py)

---

This module implements the HMAC algorithm as described by [**RFC 2104**](https://datatracker.ietf.org/doc/html/rfc2104.html).
The interface allows to use any hash function with a *fixed* digest size.
In particular, extendable output functions such as SHAKE-128 or SHAKE-256
cannot be used with HMAC.

hmac.new(*key*, *msg=None*, *digestmod*)[¶](#hmac.new "Link to this definition")
:   Return a new hmac object. *key* is a bytes or bytearray object giving the
    secret key. If *msg* is present, the method call `update(msg)` is made.
    *digestmod* is the digest name, digest constructor or module for the HMAC
    object to use. It may be any name suitable to [`hashlib.new()`](hashlib.html#hashlib.new "hashlib.new").
    Despite its argument position, it is required.

    Changed in version 3.4: Parameter *key* can be a bytes or bytearray object.
    Parameter *msg* can be of any type supported by [`hashlib`](hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.").
    Parameter *digestmod* can be the name of a hash algorithm.

    Changed in version 3.8: The *digestmod* argument is now required. Pass it as a keyword
    argument to avoid awkwardness when you do not have an initial *msg*.

hmac.digest(*key*, *msg*, *digest*)[¶](#hmac.digest "Link to this definition")
:   Return digest of *msg* for given secret *key* and *digest*. The
    function is equivalent to `HMAC(key, msg, digest).digest()`, but
    uses an optimized C or inline implementation, which is faster for messages
    that fit into memory. The parameters *key*, *msg*, and *digest* have
    the same meaning as in [`new()`](#hmac.new "hmac.new").

    CPython implementation detail, the optimized C implementation is only used
    when *digest* is a string and name of a digest algorithm, which is
    supported by OpenSSL.

    Added in version 3.7.

*class* hmac.HMAC[¶](#hmac.HMAC "Link to this definition")
:   An HMAC object has the following methods:

HMAC.update(*msg*)[¶](#hmac.HMAC.update "Link to this definition")
:   Update the hmac object with *msg*. Repeated calls are equivalent to a
    single call with the concatenation of all the arguments:
    `m.update(a); m.update(b)` is equivalent to `m.update(a + b)`.

    Changed in version 3.4: Parameter *msg* can be of any type supported by [`hashlib`](hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.").

HMAC.digest()[¶](#hmac.HMAC.digest "Link to this definition")
:   Return the digest of the bytes passed to the [`update()`](#hmac.HMAC.update "hmac.HMAC.update") method so far.
    This bytes object will be the same length as the *digest\_size* of the digest
    given to the constructor. It may contain non-ASCII bytes, including NUL
    bytes.

    Warning

    When comparing the output of [`digest()`](#hmac.digest "hmac.digest") to an externally supplied
    digest during a verification routine, it is recommended to use the
    [`compare_digest()`](#hmac.compare_digest "hmac.compare_digest") function instead of the `==` operator
    to reduce the vulnerability to timing attacks.

HMAC.hexdigest()[¶](#hmac.HMAC.hexdigest "Link to this definition")
:   Like [`digest()`](#hmac.digest "hmac.digest") except the digest is returned as a string twice the
    length containing only hexadecimal digits. This may be used to exchange the
    value safely in email or other non-binary environments.

    Warning

    When comparing the output of [`hexdigest()`](#hmac.HMAC.hexdigest "hmac.HMAC.hexdigest") to an externally supplied
    digest during a verification routine, it is recommended to use the
    [`compare_digest()`](#hmac.compare_digest "hmac.compare_digest") function instead of the `==` operator
    to reduce the vulnerability to timing attacks.

HMAC.copy()[¶](#hmac.HMAC.copy "Link to this definition")
:   Return a copy (“clone”) of the hmac object. This can be used to efficiently
    compute the digests of strings that share a common initial substring.

A hash object has the following attributes:

HMAC.digest\_size[¶](#hmac.HMAC.digest_size "Link to this definition")
:   The size of the resulting HMAC digest in bytes.

HMAC.block\_size[¶](#hmac.HMAC.block_size "Link to this definition")
:   The internal block size of the hash algorithm in bytes.

    Added in version 3.4.

HMAC.name[¶](#hmac.HMAC.name "Link to this definition")
:   The canonical name of this HMAC, always lowercase, e.g. `hmac-md5`.

    Added in version 3.4.

Changed in version 3.10: Removed the undocumented attributes `HMAC.digest_cons`, `HMAC.inner`,
and `HMAC.outer`.

This module also provides the following helper function:

hmac.compare\_digest(*a*, *b*)[¶](#hmac.compare_digest "Link to this definition")
:   Return `a == b`. This function uses an approach designed to prevent
    timing analysis by avoiding content-based short circuiting behaviour,
    making it appropriate for cryptography. *a* and *b* must both be of the
    same type: either [`str`](stdtypes.html#str "str") (ASCII only, as e.g. returned by
    [`HMAC.hexdigest()`](#hmac.HMAC.hexdigest "hmac.HMAC.hexdigest")), or a [bytes-like object](../glossary.html#term-bytes-like-object).

    Note

    If *a* and *b* are of different lengths, or if an error occurs,
    a timing attack could theoretically reveal information about the
    types and lengths of *a* and *b*—but not their values.

    Added in version 3.3.

    Changed in version 3.10: The function uses OpenSSL’s `CRYPTO_memcmp()` internally when
    available.

See also

Module [`hashlib`](hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
:   The Python module providing secure hash functions.

#### Previous topic

[`hashlib` — Secure hashes and message digests](hashlib.html "previous chapter")

#### Next topic

[`secrets` — Generate secure random numbers for managing secrets](secrets.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/hmac.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](secrets.html "secrets — Generate secure random numbers for managing secrets") |
* [previous](hashlib.html "hashlib — Secure hashes and message digests") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Cryptographic Services](crypto.html) »
* `hmac` — Keyed-Hashing for Message Authentication
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
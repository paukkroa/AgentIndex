### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](allos.html "Generic Operating System Services") |
* [previous](hmac.html "hmac — Keyed-Hashing for Message Authentication") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Cryptographic Services](crypto.html) »
* `secrets` — Generate secure random numbers for managing secrets
* |
* Theme
  Auto
  Light
  Dark
   |

# `secrets` — Generate secure random numbers for managing secrets[¶](#module-secrets "Link to this heading")

Added in version 3.6.

**Source code:** [Lib/secrets.py](https://github.com/python/cpython/tree/3.14/Lib/secrets.py)

---

The `secrets` module is used for generating cryptographically strong
random numbers suitable for managing data such as passwords, account
authentication, security tokens, and related secrets.

In particular, `secrets` should be used in preference to the
default pseudo-random number generator in the [`random`](random.html#module-random "random: Generate pseudo-random numbers with various common distributions.") module, which
is designed for modelling and simulation, not security or cryptography.

See also

[**PEP 506**](https://peps.python.org/pep-0506/)

## Random numbers[¶](#random-numbers "Link to this heading")

The `secrets` module provides access to the most secure source of
randomness that your operating system provides.

*class* secrets.SystemRandom[¶](#secrets.SystemRandom "Link to this definition")
:   A class for generating random numbers using the highest-quality
    sources provided by the operating system. See
    [`random.SystemRandom`](random.html#random.SystemRandom "random.SystemRandom") for additional details.

secrets.choice(*seq*)[¶](#secrets.choice "Link to this definition")
:   Return a randomly chosen element from a non-empty sequence.

secrets.randbelow(*exclusive\_upper\_bound*)[¶](#secrets.randbelow "Link to this definition")
:   Return a random int in the range [0, *exclusive\_upper\_bound*).

secrets.randbits(*k*)[¶](#secrets.randbits "Link to this definition")
:   Return a non-negative int with *k* random bits.

## Generating tokens[¶](#generating-tokens "Link to this heading")

The `secrets` module provides functions for generating secure
tokens, suitable for applications such as password resets,
hard-to-guess URLs, and similar.

secrets.token\_bytes(*nbytes=None*)[¶](#secrets.token_bytes "Link to this definition")
:   Return a random byte string containing *nbytes* number of bytes.

    If *nbytes* is not specified or `None`, [`DEFAULT_ENTROPY`](#secrets.DEFAULT_ENTROPY "secrets.DEFAULT_ENTROPY")
    is used instead.

    ```
    >>> token_bytes(16)
    b'\xebr\x17D*t\xae\xd4\xe3S\xb6\xe2\xebP1\x8b'
    ```

secrets.token\_hex(*nbytes=None*)[¶](#secrets.token_hex "Link to this definition")
:   Return a random text string, in hexadecimal. The string has *nbytes*
    random bytes, each byte converted to two hex digits.

    If *nbytes* is not specified or `None`, [`DEFAULT_ENTROPY`](#secrets.DEFAULT_ENTROPY "secrets.DEFAULT_ENTROPY")
    is used instead.

    ```
    >>> token_hex(16)
    'f9bf78b9a18ce6d46a0cd2b0b86df9da'
    ```

secrets.token\_urlsafe(*nbytes=None*)[¶](#secrets.token_urlsafe "Link to this definition")
:   Return a random URL-safe text string, containing *nbytes* random
    bytes. The text is Base64 encoded, so on average each byte results
    in approximately 1.3 characters.

    If *nbytes* is not specified or `None`, [`DEFAULT_ENTROPY`](#secrets.DEFAULT_ENTROPY "secrets.DEFAULT_ENTROPY")
    is used instead.

    ```
    >>> token_urlsafe(16)
    'Drmhze6EPcv0fN_81Bj-nA'
    ```

### How many bytes should tokens use?[¶](#how-many-bytes-should-tokens-use "Link to this heading")

To be secure against
[brute-force attacks](https://en.wikipedia.org/wiki/Brute-force_attack),
tokens need to have sufficient randomness. Unfortunately, what is
considered sufficient will necessarily increase as computers get more
powerful and able to make more guesses in a shorter period. As of 2015,
it is believed that 32 bytes (256 bits) of randomness is sufficient for
the typical use-case expected for the `secrets` module.

For those who want to manage their own token length, you can explicitly
specify how much randomness is used for tokens by giving an [`int`](functions.html#int "int")
argument to the various `token_*` functions. That argument is taken
as the number of bytes of randomness to use.

Otherwise, if no argument is provided, or if the argument is `None`,
the `token_*` functions use [`DEFAULT_ENTROPY`](#secrets.DEFAULT_ENTROPY "secrets.DEFAULT_ENTROPY") instead.

secrets.DEFAULT\_ENTROPY[¶](#secrets.DEFAULT_ENTROPY "Link to this definition")
:   Default number of bytes of randomness used by the `token_*` functions.

    The exact value is subject to change at any time, including during
    maintenance releases.

## Other functions[¶](#other-functions "Link to this heading")

secrets.compare\_digest(*a*, *b*)[¶](#secrets.compare_digest "Link to this definition")
:   Return `True` if strings or
    [bytes-like objects](../glossary.html#term-bytes-like-object)
    *a* and *b* are equal, otherwise `False`,
    using a “constant-time compare” to reduce the risk of
    [timing attacks](https://codahale.com/a-lesson-in-timing-attacks/).
    See [`hmac.compare_digest()`](hmac.html#hmac.compare_digest "hmac.compare_digest") for additional details.

## Recipes and best practices[¶](#recipes-and-best-practices "Link to this heading")

This section shows recipes and best practices for using `secrets`
to manage a basic level of security.

Generate an eight-character alphanumeric password:

```
import string
import secrets
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))
```

Note

Applications should not
[**store passwords in a recoverable format**](https://cwe.mitre.org/data/definitions/257.html),
whether plain text or encrypted. They should be salted and hashed
using a cryptographically strong one-way (irreversible) hash function.

Generate a ten-character alphanumeric password with at least one
lowercase character, at least one uppercase character, and at least
three digits:

```
import string
import secrets
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break
```

Generate an [XKCD-style passphrase](https://xkcd.com/936/):

```
import secrets
# On standard Linux systems, use a convenient dictionary file.
# Other platforms may need to provide their own word-list.
with open('/usr/share/dict/words') as f:
    words = [word.strip() for word in f]
    password = ' '.join(secrets.choice(words) for i in range(4))
```

Generate a hard-to-guess temporary URL containing a security token
suitable for password recovery applications:

```
import secrets
url = 'https://example.com/reset=' + secrets.token_urlsafe()
```

### [Table of Contents](../contents.html)

* [`secrets` — Generate secure random numbers for managing secrets](#)
  + [Random numbers](#random-numbers)
  + [Generating tokens](#generating-tokens)
    - [How many bytes should tokens use?](#how-many-bytes-should-tokens-use)
  + [Other functions](#other-functions)
  + [Recipes and best practices](#recipes-and-best-practices)

#### Previous topic

[`hmac` — Keyed-Hashing for Message Authentication](hmac.html "previous chapter")

#### Next topic

[Generic Operating System Services](allos.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/secrets.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](allos.html "Generic Operating System Services") |
* [previous](hmac.html "hmac — Keyed-Hashing for Message Authentication") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Cryptographic Services](crypto.html) »
* `secrets` — Generate secure random numbers for managing secrets
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
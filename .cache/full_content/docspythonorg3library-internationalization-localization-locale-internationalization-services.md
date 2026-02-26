### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tk.html "Graphical user interfaces with Tk") |
* [previous](gettext.html "gettext — Multilingual internationalization services") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internationalization](i18n.html) »
* `locale` — Internationalization services
* |
* Theme
  Auto
  Light
  Dark
   |

# `locale` — Internationalization services[¶](#module-locale "Link to this heading")

**Source code:** [Lib/locale.py](https://github.com/python/cpython/tree/3.14/Lib/locale.py)

---

The `locale` module opens access to the POSIX locale database and
functionality. The POSIX locale mechanism allows programmers to deal with
certain cultural issues in an application, without requiring the programmer to
know all the specifics of each country where the software is executed.

The `locale` module is implemented on top of the `_locale` module,
which in turn uses an ANSI C locale implementation if available.

The `locale` module defines the following exception and functions:

*exception* locale.Error[¶](#locale.Error "Link to this definition")
:   Exception raised when the locale passed to [`setlocale()`](#locale.setlocale "locale.setlocale") is not
    recognized.

locale.setlocale(*category*, *locale=None*)[¶](#locale.setlocale "Link to this definition")
:   If *locale* is given and not `None`, [`setlocale()`](#locale.setlocale "locale.setlocale") modifies the locale
    setting for the *category*. The available categories are listed in the data
    description below. *locale* may be a [string](#locale-name), or a pair,
    language code and encoding. An empty string specifies the user’s
    default settings. If the modification of the locale fails, the exception
    [`Error`](#locale.Error "locale.Error") is raised. If successful, the new locale setting is returned.

    If *locale* is a pair, it is converted to a locale name using
    the locale aliasing engine.
    The language code has the same format as a [locale name](#locale-name),
    but without encoding and `@`-modifier.
    The language code and encoding can be `None`.

    If *locale* is omitted or `None`, the current setting for *category* is
    returned.

    Example:

    ```
    >>> import locale
    >>> loc = locale.setlocale(locale.LC_ALL)  # get current locale
    # use German locale; name and availability varies with platform
    >>> locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
    >>> locale.strcoll('f\xe4n', 'foo')  # compare a string containing an umlaut
    >>> locale.setlocale(locale.LC_ALL, '')   # use user's preferred locale
    >>> locale.setlocale(locale.LC_ALL, 'C')  # use default (C) locale
    >>> locale.setlocale(locale.LC_ALL, loc)  # restore saved locale
    ```

    [`setlocale()`](#locale.setlocale "locale.setlocale") is not thread-safe on most systems. Applications typically
    start with a call of:

    ```
    import locale
    locale.setlocale(locale.LC_ALL, '')
    ```

    This sets the locale for all categories to the user’s default setting (typically
    specified in the `LANG` environment variable). If the locale is not
    changed thereafter, using multithreading should not cause problems.

locale.localeconv()[¶](#locale.localeconv "Link to this definition")
:   Returns the database of the local conventions as a dictionary. This dictionary
    has the following strings as keys:

    | Category | Key | Meaning |
    | --- | --- | --- |
    | [`LC_NUMERIC`](#locale.LC_NUMERIC "locale.LC_NUMERIC") | `'decimal_point'` | Decimal point character. |
    |  | `'grouping'` | Sequence of numbers specifying which relative positions the `'thousands_sep'` is expected. If the sequence is terminated with [`CHAR_MAX`](#locale.CHAR_MAX "locale.CHAR_MAX"), no further grouping is performed. If the sequence terminates with a `0`, the last group size is repeatedly used. |
    |  | `'thousands_sep'` | Character used between groups. |
    | [`LC_MONETARY`](#locale.LC_MONETARY "locale.LC_MONETARY") | `'int_curr_symbol'` | International currency symbol. |
    |  | `'currency_symbol'` | Local currency symbol. |
    |  | `'p_cs_precedes/n_cs_precedes'` | Whether the currency symbol precedes the value (for positive resp. negative values). |
    |  | `'p_sep_by_space/n_sep_by_space'` | Whether the currency symbol is separated from the value by a space (for positive resp. negative values). |
    |  | `'mon_decimal_point'` | Decimal point used for monetary values. |
    |  | `'frac_digits'` | Number of fractional digits used in local formatting of monetary values. |
    |  | `'int_frac_digits'` | Number of fractional digits used in international formatting of monetary values. |
    |  | `'mon_thousands_sep'` | Group separator used for monetary values. |
    |  | `'mon_grouping'` | Equivalent to `'grouping'`, used for monetary values. |
    |  | `'positive_sign'` | Symbol used to annotate a positive monetary value. |
    |  | `'negative_sign'` | Symbol used to annotate a negative monetary value. |
    |  | `'p_sign_posn/n_sign_posn'` | The position of the sign (for positive resp. negative values), see below. |

    All numeric values can be set to [`CHAR_MAX`](#locale.CHAR_MAX "locale.CHAR_MAX") to indicate that there is no
    value specified in this locale.

    The possible values for `'p_sign_posn'` and `'n_sign_posn'` are given below.

    | Value | Explanation |
    | --- | --- |
    | `0` | Currency and value are surrounded by parentheses. |
    | `1` | The sign should precede the value and currency symbol. |
    | `2` | The sign should follow the value and currency symbol. |
    | `3` | The sign should immediately precede the value. |
    | `4` | The sign should immediately follow the value. |
    | `CHAR_MAX` | Nothing is specified in this locale. |

    The function temporarily sets the `LC_CTYPE` locale to the `LC_NUMERIC`
    locale or the `LC_MONETARY` locale if locales are different and numeric or
    monetary strings are non-ASCII. This temporary change affects other threads.

    Changed in version 3.7: The function now temporarily sets the `LC_CTYPE` locale to the
    `LC_NUMERIC` locale in some cases.

locale.nl\_langinfo(*option*)[¶](#locale.nl_langinfo "Link to this definition")
:   Return some locale-specific information as a string. This function is not
    available on all systems, and the set of possible options might also vary
    across platforms. The possible argument values are numbers, for which
    symbolic constants are available in the locale module.

    The [`nl_langinfo()`](#locale.nl_langinfo "locale.nl_langinfo") function accepts one of the following keys. Most
    descriptions are taken from the corresponding description in the GNU C
    library.

    locale.CODESET[¶](#locale.CODESET "Link to this definition")
    :   Get a string with the name of the character encoding used in the
        selected locale.

    locale.D\_T\_FMT[¶](#locale.D_T_FMT "Link to this definition")
    :   Get a string that can be used as a format string for [`time.strftime()`](time.html#time.strftime "time.strftime") to
        represent date and time in a locale-specific way.

    locale.D\_FMT[¶](#locale.D_FMT "Link to this definition")
    :   Get a string that can be used as a format string for [`time.strftime()`](time.html#time.strftime "time.strftime") to
        represent a date in a locale-specific way.

    locale.T\_FMT[¶](#locale.T_FMT "Link to this definition")
    :   Get a string that can be used as a format string for [`time.strftime()`](time.html#time.strftime "time.strftime") to
        represent a time in a locale-specific way.

    locale.T\_FMT\_AMPM[¶](#locale.T_FMT_AMPM "Link to this definition")
    :   Get a format string for [`time.strftime()`](time.html#time.strftime "time.strftime") to represent time in the am/pm
        format.

    locale.DAY\_1[¶](#locale.DAY_1 "Link to this definition")

    locale.DAY\_2[¶](#locale.DAY_2 "Link to this definition")

    locale.DAY\_3[¶](#locale.DAY_3 "Link to this definition")

    locale.DAY\_4[¶](#locale.DAY_4 "Link to this definition")

    locale.DAY\_5[¶](#locale.DAY_5 "Link to this definition")

    locale.DAY\_6[¶](#locale.DAY_6 "Link to this definition")

    locale.DAY\_7[¶](#locale.DAY_7 "Link to this definition")
    :   Get the name of the n-th day of the week.

        Note

        This follows the US convention of [`DAY_1`](#locale.DAY_1 "locale.DAY_1") being Sunday, not the
        international convention (ISO 8601) that Monday is the first day of the
        week.

    locale.ABDAY\_1[¶](#locale.ABDAY_1 "Link to this definition")

    locale.ABDAY\_2[¶](#locale.ABDAY_2 "Link to this definition")

    locale.ABDAY\_3[¶](#locale.ABDAY_3 "Link to this definition")

    locale.ABDAY\_4[¶](#locale.ABDAY_4 "Link to this definition")

    locale.ABDAY\_5[¶](#locale.ABDAY_5 "Link to this definition")

    locale.ABDAY\_6[¶](#locale.ABDAY_6 "Link to this definition")

    locale.ABDAY\_7[¶](#locale.ABDAY_7 "Link to this definition")
    :   Get the abbreviated name of the n-th day of the week.

    locale.MON\_1[¶](#locale.MON_1 "Link to this definition")

    locale.MON\_2[¶](#locale.MON_2 "Link to this definition")

    locale.MON\_3[¶](#locale.MON_3 "Link to this definition")

    locale.MON\_4[¶](#locale.MON_4 "Link to this definition")

    locale.MON\_5[¶](#locale.MON_5 "Link to this definition")

    locale.MON\_6[¶](#locale.MON_6 "Link to this definition")

    locale.MON\_7[¶](#locale.MON_7 "Link to this definition")

    locale.MON\_8[¶](#locale.MON_8 "Link to this definition")

    locale.MON\_9[¶](#locale.MON_9 "Link to this definition")

    locale.MON\_10[¶](#locale.MON_10 "Link to this definition")

    locale.MON\_11[¶](#locale.MON_11 "Link to this definition")

    locale.MON\_12[¶](#locale.MON_12 "Link to this definition")
    :   Get the name of the n-th month.

    locale.ABMON\_1[¶](#locale.ABMON_1 "Link to this definition")

    locale.ABMON\_2[¶](#locale.ABMON_2 "Link to this definition")

    locale.ABMON\_3[¶](#locale.ABMON_3 "Link to this definition")

    locale.ABMON\_4[¶](#locale.ABMON_4 "Link to this definition")

    locale.ABMON\_5[¶](#locale.ABMON_5 "Link to this definition")

    locale.ABMON\_6[¶](#locale.ABMON_6 "Link to this definition")

    locale.ABMON\_7[¶](#locale.ABMON_7 "Link to this definition")

    locale.ABMON\_8[¶](#locale.ABMON_8 "Link to this definition")

    locale.ABMON\_9[¶](#locale.ABMON_9 "Link to this definition")

    locale.ABMON\_10[¶](#locale.ABMON_10 "Link to this definition")

    locale.ABMON\_11[¶](#locale.ABMON_11 "Link to this definition")

    locale.ABMON\_12[¶](#locale.ABMON_12 "Link to this definition")
    :   Get the abbreviated name of the n-th month.

    locale.RADIXCHAR[¶](#locale.RADIXCHAR "Link to this definition")
    :   Get the radix character (decimal dot, decimal comma, etc.).

    locale.THOUSEP[¶](#locale.THOUSEP "Link to this definition")
    :   Get the separator character for thousands (groups of three digits).

    locale.YESEXPR[¶](#locale.YESEXPR "Link to this definition")
    :   Get a regular expression that can be used with the regex function to
        recognize a positive response to a yes/no question.

    locale.NOEXPR[¶](#locale.NOEXPR "Link to this definition")
    :   Get a regular expression that can be used with the `regex(3)` function to
        recognize a negative response to a yes/no question.

        Note

        The regular expressions for [`YESEXPR`](#locale.YESEXPR "locale.YESEXPR") and
        [`NOEXPR`](#locale.NOEXPR "locale.NOEXPR") use syntax suitable for the
        `regex` function from the C library, which might
        differ from the syntax used in [`re`](re.html#module-re "re: Regular expression operations.").

    locale.CRNCYSTR[¶](#locale.CRNCYSTR "Link to this definition")
    :   Get the currency symbol, preceded by “-” if the symbol should appear before
        the value, “+” if the symbol should appear after the value, or “.” if the
        symbol should replace the radix character.

    locale.ERA[¶](#locale.ERA "Link to this definition")
    :   Get a string which describes how years are counted and displayed for
        each era in a locale.

        Most locales do not define this value. An example of a locale which does
        define this value is the Japanese one. In Japan, the traditional
        representation of dates includes the name of the era corresponding to the
        then-emperor’s reign.

        Normally it should not be necessary to use this value directly. Specifying
        the `E` modifier in their format strings causes the [`time.strftime()`](time.html#time.strftime "time.strftime")
        function to use this information.
        The format of the returned string is specified in *The Open Group Base
        Specifications Issue 8*, paragraph [7.3.5.2 LC\_TIME C-Language Access](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap07.html#tag_07_03_05_02).

    locale.ERA\_D\_T\_FMT[¶](#locale.ERA_D_T_FMT "Link to this definition")
    :   Get a format string for [`time.strftime()`](time.html#time.strftime "time.strftime") to represent date and time in a
        locale-specific era-based way.

    locale.ERA\_D\_FMT[¶](#locale.ERA_D_FMT "Link to this definition")
    :   Get a format string for [`time.strftime()`](time.html#time.strftime "time.strftime") to represent a date in a
        locale-specific era-based way.

    locale.ERA\_T\_FMT[¶](#locale.ERA_T_FMT "Link to this definition")
    :   Get a format string for [`time.strftime()`](time.html#time.strftime "time.strftime") to represent a time in a
        locale-specific era-based way.

    locale.ALT\_DIGITS[¶](#locale.ALT_DIGITS "Link to this definition")
    :   Get a string consisting of up to 100 semicolon-separated symbols used
        to represent the values 0 to 99 in a locale-specific way.
        In most locales this is an empty string.

    The function temporarily sets the `LC_CTYPE` locale to the locale
    of the category that determines the requested value (`LC_TIME`,
    `LC_NUMERIC`, `LC_MONETARY` or `LC_MESSAGES`) if locales are
    different and the resulting string is non-ASCII.
    This temporary change affects other threads.

    Changed in version 3.14: The function now temporarily sets the `LC_CTYPE` locale in some cases.

locale.getdefaultlocale([*envvars*])[¶](#locale.getdefaultlocale "Link to this definition")
:   Tries to determine the default locale settings and returns them as a tuple of
    the form `(language code, encoding)`.

    According to POSIX, a program which has not called `setlocale(LC_ALL, '')`
    runs using the portable `'C'` locale. Calling `setlocale(LC_ALL, '')` lets
    it use the default locale as defined by the `LANG` variable. Since we
    do not want to interfere with the current locale setting we thus emulate the
    behavior in the way described above.

    To maintain compatibility with other platforms, not only the `LANG`
    variable is tested, but a list of variables given as envvars parameter. The
    first found to be defined will be used. *envvars* defaults to the search
    path used in GNU gettext; it must always contain the variable name
    `'LANG'`. The GNU gettext search path contains `'LC_ALL'`,
    `'LC_CTYPE'`, `'LANG'` and `'LANGUAGE'`, in that order.

    The language code has the same format as a [locale name](#locale-name),
    but without encoding and `@`-modifier.
    The language code and encoding may be `None` if their values cannot be
    determined.
    The “C” locale is represented as `(None, None)`.

    Deprecated since version 3.11, will be removed in version 3.15.

locale.getlocale(*category=LC\_CTYPE*)[¶](#locale.getlocale "Link to this definition")
:   Returns the current setting for the given locale category as a tuple containing
    the language code and encoding. *category* may be one of the `LC_*`
    values except [`LC_ALL`](#locale.LC_ALL "locale.LC_ALL"). It defaults to [`LC_CTYPE`](#locale.LC_CTYPE "locale.LC_CTYPE").

    The language code has the same format as a [locale name](#locale-name),
    but without encoding and `@`-modifier.
    The language code and encoding may be `None` if their values cannot be
    determined.
    The “C” locale is represented as `(None, None)`.

locale.getpreferredencoding(*do\_setlocale=True*)[¶](#locale.getpreferredencoding "Link to this definition")
:   Return the [locale encoding](../glossary.html#term-locale-encoding) used for text data, according to user
    preferences. User preferences are expressed differently on different
    systems, and might not be available programmatically on some systems, so
    this function only returns a guess.

    On some systems, it is necessary to invoke [`setlocale()`](#locale.setlocale "locale.setlocale") to obtain the
    user preferences, so this function is not thread-safe. If invoking setlocale
    is not necessary or desired, *do\_setlocale* should be set to `False`.

    On Android or if the [Python UTF-8 Mode](os.html#utf8-mode) is enabled, always
    return `'utf-8'`, the [locale encoding](../glossary.html#term-locale-encoding) and the *do\_setlocale*
    argument are ignored.

    The [Python preinitialization](../c-api/init_config.html#c-preinit) configures the LC\_CTYPE
    locale. See also the [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler).

    Changed in version 3.7: The function now always returns `"utf-8"` on Android or if the
    [Python UTF-8 Mode](os.html#utf8-mode) is enabled.

locale.getencoding()[¶](#locale.getencoding "Link to this definition")
:   Get the current [locale encoding](../glossary.html#term-locale-encoding):

    * On Android and VxWorks, return `"utf-8"`.
    * On Unix, return the encoding of the current [`LC_CTYPE`](#locale.LC_CTYPE "locale.LC_CTYPE") locale.
      Return `"utf-8"` if `nl_langinfo(CODESET)` returns an empty string:
      for example, if the current LC\_CTYPE locale is not supported.
    * On Windows, return the ANSI code page.

    The [Python preinitialization](../c-api/init_config.html#c-preinit) configures the LC\_CTYPE
    locale. See also the [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler).

    This function is similar to
    [`getpreferredencoding(False)`](#locale.getpreferredencoding "locale.getpreferredencoding") except this
    function ignores the [Python UTF-8 Mode](os.html#utf8-mode).

    Added in version 3.11.

locale.normalize(*localename*)[¶](#locale.normalize "Link to this definition")
:   Returns a normalized locale code for the given locale name. The returned locale
    code is formatted for use with [`setlocale()`](#locale.setlocale "locale.setlocale"). If normalization fails, the
    original name is returned unchanged.

    If the given encoding is not known, the function defaults to the default
    encoding for the locale code just like [`setlocale()`](#locale.setlocale "locale.setlocale").

locale.strcoll(*string1*, *string2*)[¶](#locale.strcoll "Link to this definition")
:   Compares two strings according to the current [`LC_COLLATE`](#locale.LC_COLLATE "locale.LC_COLLATE") setting. As
    any other compare function, returns a negative, or a positive value, or `0`,
    depending on whether *string1* collates before or after *string2* or is equal to
    it.

locale.strxfrm(*string*)[¶](#locale.strxfrm "Link to this definition")
:   Transforms a string to one that can be used in locale-aware
    comparisons. For example, `strxfrm(s1) < strxfrm(s2)` is
    equivalent to `strcoll(s1, s2) < 0`. This function can be used
    when the same string is compared repeatedly, e.g. when collating a
    sequence of strings.

locale.format\_string(*format*, *val*, *grouping=False*, *monetary=False*)[¶](#locale.format_string "Link to this definition")
:   Formats a number *val* according to the current [`LC_NUMERIC`](#locale.LC_NUMERIC "locale.LC_NUMERIC") setting.
    The format follows the conventions of the `%` operator. For floating-point
    values, the decimal point is modified if appropriate. If *grouping* is `True`,
    also takes the grouping into account.

    If *monetary* is true, the conversion uses monetary thousands separator and
    grouping strings.

    Processes formatting specifiers as in `format % val`, but takes the current
    locale settings into account.

    Changed in version 3.7: The *monetary* keyword parameter was added.

locale.currency(*val*, *symbol=True*, *grouping=False*, *international=False*)[¶](#locale.currency "Link to this definition")
:   Formats a number *val* according to the current [`LC_MONETARY`](#locale.LC_MONETARY "locale.LC_MONETARY") settings.

    The returned string includes the currency symbol if *symbol* is true, which is
    the default. If *grouping* is `True` (which is not the default), grouping is done
    with the value. If *international* is `True` (which is not the default), the
    international currency symbol is used.

    Note

    This function will not work with the ‘C’ locale, so you have to set a
    locale via [`setlocale()`](#locale.setlocale "locale.setlocale") first.

locale.str(*float*)[¶](#locale.str "Link to this definition")
:   Formats a floating-point number using the same format as the built-in function
    `str(float)`, but takes the decimal point into account.

locale.delocalize(*string*)[¶](#locale.delocalize "Link to this definition")
:   Converts a string into a normalized number string, following the
    [`LC_NUMERIC`](#locale.LC_NUMERIC "locale.LC_NUMERIC") settings.

    Added in version 3.5.

locale.localize(*string*, *grouping=False*, *monetary=False*)[¶](#locale.localize "Link to this definition")
:   Converts a normalized number string into a formatted string following the
    [`LC_NUMERIC`](#locale.LC_NUMERIC "locale.LC_NUMERIC") settings.

    Added in version 3.10.

locale.atof(*string*, *func=float*)[¶](#locale.atof "Link to this definition")
:   Converts a string to a number, following the [`LC_NUMERIC`](#locale.LC_NUMERIC "locale.LC_NUMERIC") settings,
    by calling *func* on the result of calling [`delocalize()`](#locale.delocalize "locale.delocalize") on *string*.

locale.atoi(*string*)[¶](#locale.atoi "Link to this definition")
:   Converts a string to an integer, following the [`LC_NUMERIC`](#locale.LC_NUMERIC "locale.LC_NUMERIC") conventions.

locale.LC\_CTYPE[¶](#locale.LC_CTYPE "Link to this definition")
:   Locale category for the character type functions. Most importantly, this
    category defines the text encoding, i.e. how bytes are interpreted as
    Unicode codepoints. See [**PEP 538**](https://peps.python.org/pep-0538/) and [**PEP 540**](https://peps.python.org/pep-0540/) for how this variable
    might be automatically coerced to `C.UTF-8` to avoid issues created by
    invalid settings in containers or incompatible settings passed over remote
    SSH connections.

    Python doesn’t internally use locale-dependent character transformation functions
    from `ctype.h`. Instead, `pyctype.h` provides locale-independent
    equivalents like [`Py_TOLOWER`](../c-api/conversion.html#c.Py_TOLOWER "Py_TOLOWER").

locale.LC\_COLLATE[¶](#locale.LC_COLLATE "Link to this definition")
:   Locale category for sorting strings. The functions [`strcoll()`](#locale.strcoll "locale.strcoll") and
    [`strxfrm()`](#locale.strxfrm "locale.strxfrm") of the `locale` module are affected.

locale.LC\_TIME[¶](#locale.LC_TIME "Link to this definition")
:   Locale category for the formatting of time. The function [`time.strftime()`](time.html#time.strftime "time.strftime")
    follows these conventions.

locale.LC\_MONETARY[¶](#locale.LC_MONETARY "Link to this definition")
:   Locale category for formatting of monetary values. The available options are
    available from the [`localeconv()`](#locale.localeconv "locale.localeconv") function.

locale.LC\_MESSAGES[¶](#locale.LC_MESSAGES "Link to this definition")
:   Locale category for message display. Python currently does not support
    application specific locale-aware messages. Messages displayed by the operating
    system, like those returned by [`os.strerror()`](os.html#os.strerror "os.strerror") might be affected by this
    category.

    This value may not be available on operating systems not conforming to the
    POSIX standard, most notably Windows.

locale.LC\_NUMERIC[¶](#locale.LC_NUMERIC "Link to this definition")
:   Locale category for formatting numbers. The functions [`format_string()`](#locale.format_string "locale.format_string"),
    [`atoi()`](#locale.atoi "locale.atoi"), [`atof()`](#locale.atof "locale.atof") and [`str()`](#locale.str "locale.str") of the `locale` module are
    affected by that category. All other numeric formatting operations are not
    affected.

locale.LC\_ALL[¶](#locale.LC_ALL "Link to this definition")
:   Combination of all locale settings. If this flag is used when the locale is
    changed, setting the locale for all categories is attempted. If that fails for
    any category, no category is changed at all. When the locale is retrieved using
    this flag, a string indicating the setting for all categories is returned. This
    string can be later used to restore the settings.

locale.CHAR\_MAX[¶](#locale.CHAR_MAX "Link to this definition")
:   This is a symbolic constant used for different values returned by
    [`localeconv()`](#locale.localeconv "locale.localeconv").

## Background, details, hints, tips and caveats[¶](#background-details-hints-tips-and-caveats "Link to this heading")

The C standard defines the locale as a program-wide property that may be
relatively expensive to change. On top of that, some implementations are broken
in such a way that frequent locale changes may cause core dumps. This makes the
locale somewhat painful to use correctly.

Initially, when a program is started, the locale is the `C` locale, no matter
what the user’s preferred locale is. There is one exception: the
[`LC_CTYPE`](#locale.LC_CTYPE "locale.LC_CTYPE") category is changed at startup to set the current locale
encoding to the user’s preferred locale encoding. The program must explicitly
say that it wants the user’s preferred locale settings for other categories by
calling `setlocale(LC_ALL, '')`.

It is generally a bad idea to call [`setlocale()`](#locale.setlocale "locale.setlocale") in some library routine,
since as a side effect it affects the entire program. Saving and restoring it
is almost as bad: it is expensive and affects other threads that happen to run
before the settings have been restored.

If, when coding a module for general use, you need a locale independent version
of an operation that is affected by the locale (such as
certain formats used with [`time.strftime()`](time.html#time.strftime "time.strftime")), you will have to find a way to
do it without using the standard library routine. Even better is convincing
yourself that using locale settings is okay. Only as a last resort should you
document that your module is not compatible with non-`C` locale settings.

The only way to perform numeric operations according to the locale is to use the
special functions defined by this module: [`atof()`](#locale.atof "locale.atof"), [`atoi()`](#locale.atoi "locale.atoi"),
[`format_string()`](#locale.format_string "locale.format_string"), [`str()`](#locale.str "locale.str").

There is no way to perform case conversions and character classifications
according to the locale. For (Unicode) text strings these are done according
to the character value only, while for byte strings, the conversions and
classifications are done according to the ASCII value of the byte, and bytes
whose high bit is set (i.e., non-ASCII bytes) are never converted or considered
part of a character class such as letter or whitespace.

## Locale names[¶](#locale-names "Link to this heading")

The format of the locale name is platform dependent, and the set of supported
locales can depend on the system configuration.

On Posix platforms, it usually has the format [[1]](#id4):

```
  language ["_" territory] ["." charset] ["@" modifier]
```

where *language* is a two- or three-letter language code from [ISO 639](https://www.iso.org/iso-639-language-code),
*territory* is a two-letter country or region code from [ISO 3166](https://www.iso.org/iso-3166-country-codes.html),
*charset* is a locale encoding, and *modifier* is a script name,
a language subtag, a sort order identifier, or other locale modifier
(for example, “latin”, “valencia”, “stroke” and “euro”).

On Windows, several formats are supported. [[2]](#id5) [[3]](#id6)
A subset of [IETF BCP 47](https://www.rfc-editor.org/info/bcp47) tags:

```
  language ["-" script] ["-" territory] ["." charset]
  language ["-" script] "-" territory "-" modifier
```

where *language* and *territory* have the same meaning as in Posix,
*script* is a four-letter script code from [ISO 15924](https://www.unicode.org/iso15924/),
and *modifier* is a language subtag, a sort order identifier
or custom modifier (for example, “valencia”, “stroke” or “x-python”).
Both hyphen (`'-'`) and underscore (`'_'`) separators are supported.
Only UTF-8 encoding is allowed for BCP 47 tags.

Windows also supports locale names in the format:

```
  language ["_" territory] ["." charset]
```

where *language* and *territory* are full names, such as “English” and
“United States”, and *charset* is either a code page number (for example, “1252”)
or UTF-8.
Only the underscore separator is supported in this format.

The “C” locale is supported on all platforms.

[[1](#id1)]

[IEEE Std 1003.1-2024; 8.2 Internationalization Variables](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap08.html#tag_08_02)


[[2](#id2)]

[UCRT Locale names, Languages, and Country/Region strings](https://learn.microsoft.com/en-us/cpp/c-runtime-library/locale-names-languages-and-country-region-strings)


[[3](#id3)]

[Locale Names](https://learn.microsoft.com/en-us/windows/win32/intl/locale-names)

## For extension writers and programs that embed Python[¶](#for-extension-writers-and-programs-that-embed-python "Link to this heading")

Extension modules should never call [`setlocale()`](#locale.setlocale "locale.setlocale"), except to find out what
the current locale is. But since the return value can only be used portably to
restore it, that is not very useful (except perhaps to find out whether or not
the locale is `C`).

When Python code uses the `locale` module to change the locale, this also
affects the embedding application. If the embedding application doesn’t want
this to happen, it should remove the `_locale` extension module (which does
all the work) from the table of built-in modules in the `config.c` file,
and make sure that the `_locale` module is not accessible as a shared
library.

## Access to message catalogs[¶](#access-to-message-catalogs "Link to this heading")

locale.gettext(*msg*)[¶](#locale.gettext "Link to this definition")

locale.dgettext(*domain*, *msg*)[¶](#locale.dgettext "Link to this definition")

locale.dcgettext(*domain*, *msg*, *category*)[¶](#locale.dcgettext "Link to this definition")

locale.textdomain(*domain*)[¶](#locale.textdomain "Link to this definition")

locale.bindtextdomain(*domain*, *dir*)[¶](#locale.bindtextdomain "Link to this definition")

locale.bind\_textdomain\_codeset(*domain*, *codeset*)[¶](#locale.bind_textdomain_codeset "Link to this definition")

The locale module exposes the C library’s gettext interface on systems that
provide this interface. It consists of the functions [`gettext()`](gettext.html#module-gettext "gettext: Multilingual internationalization services."),
[`dgettext()`](#locale.dgettext "locale.dgettext"), [`dcgettext()`](#locale.dcgettext "locale.dcgettext"), [`textdomain()`](#locale.textdomain "locale.textdomain"), [`bindtextdomain()`](#locale.bindtextdomain "locale.bindtextdomain"),
and [`bind_textdomain_codeset()`](#locale.bind_textdomain_codeset "locale.bind_textdomain_codeset"). These are similar to the same functions in
the [`gettext`](gettext.html#module-gettext "gettext: Multilingual internationalization services.") module, but use the C library’s binary format for message
catalogs, and the C library’s search algorithms for locating message catalogs.

Python applications should normally find no need to invoke these functions, and
should use [`gettext`](gettext.html#module-gettext "gettext: Multilingual internationalization services.") instead. A known exception to this rule are
applications that link with additional C libraries which internally invoke
C functions `gettext` or `dcgettext`. For these applications, it may be
necessary to bind the text domain, so that the libraries can properly locate
their message catalogs.

### [Table of Contents](../contents.html)

* [`locale` — Internationalization services](#)
  + [Background, details, hints, tips and caveats](#background-details-hints-tips-and-caveats)
  + [Locale names](#locale-names)
  + [For extension writers and programs that embed Python](#for-extension-writers-and-programs-that-embed-python)
  + [Access to message catalogs](#access-to-message-catalogs)

#### Previous topic

[`gettext` — Multilingual internationalization services](gettext.html "previous chapter")

#### Next topic

[Graphical user interfaces with Tk](tk.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/locale.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](tk.html "Graphical user interfaces with Tk") |
* [previous](gettext.html "gettext — Multilingual internationalization services") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Internationalization](i18n.html) »
* `locale` — Internationalization services
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
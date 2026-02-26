### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](collections.html "collections — Container datatypes") |
* [previous](zoneinfo.html "zoneinfo — IANA time zone support") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Types](datatypes.html) »
* `calendar` — General calendar-related functions
* |
* Theme
  Auto
  Light
  Dark
   |

# `calendar` — General calendar-related functions[¶](#module-calendar "Link to this heading")

**Source code:** [Lib/calendar.py](https://github.com/python/cpython/tree/3.14/Lib/calendar.py)

---

This module allows you to output calendars like the Unix **cal** program,
and provides additional useful functions related to the calendar. By default,
these calendars have Monday as the first day of the week, and Sunday as the last
(the European convention). Use [`setfirstweekday()`](#calendar.setfirstweekday "calendar.setfirstweekday") to set the first day of
the week to Sunday (6) or to any other weekday. Parameters that specify dates
are given as integers. For related
functionality, see also the [`datetime`](datetime.html#module-datetime "datetime: Basic date and time types.") and [`time`](time.html#module-time "time: Time access and conversions.") modules.

The functions and classes defined in this module
use an idealized calendar, the current Gregorian calendar extended indefinitely
in both directions. This matches the definition of the “proleptic Gregorian”
calendar in Dershowitz and Reingold’s book “Calendrical Calculations”, where
it’s the base calendar for all computations. Zero and negative years are
interpreted as prescribed by the ISO 8601 standard. Year 0 is 1 BC, year -1 is
2 BC, and so on.

*class* calendar.Calendar(*firstweekday=0*)[¶](#calendar.Calendar "Link to this definition")
:   Creates a [`Calendar`](#calendar.Calendar "calendar.Calendar") object. *firstweekday* is an integer specifying the
    first day of the week. [`MONDAY`](#calendar.MONDAY "calendar.MONDAY") is `0` (the default), [`SUNDAY`](#calendar.SUNDAY "calendar.SUNDAY") is `6`.

    A [`Calendar`](#calendar.Calendar "calendar.Calendar") object provides several methods that can be used for
    preparing the calendar data for formatting. This class doesn’t do any formatting
    itself. This is the job of subclasses.

    [`Calendar`](#calendar.Calendar "calendar.Calendar") instances have the following methods and attributes:

    firstweekday[¶](#calendar.Calendar.firstweekday "Link to this definition")
    :   The first weekday as an integer (0–6).

        This property can also be set and read using
        [`setfirstweekday()`](#calendar.Calendar.setfirstweekday "calendar.Calendar.setfirstweekday") and
        [`getfirstweekday()`](#calendar.Calendar.getfirstweekday "calendar.Calendar.getfirstweekday") respectively.

    getfirstweekday()[¶](#calendar.Calendar.getfirstweekday "Link to this definition")
    :   Return an [`int`](functions.html#int "int") for the current first weekday (0–6).

        Identical to reading the [`firstweekday`](#calendar.Calendar.firstweekday "calendar.Calendar.firstweekday") property.

    setfirstweekday(*firstweekday*)[¶](#calendar.Calendar.setfirstweekday "Link to this definition")
    :   Set the first weekday to *firstweekday*, passed as an [`int`](functions.html#int "int") (0–6)

        Identical to setting the [`firstweekday`](#calendar.Calendar.firstweekday "calendar.Calendar.firstweekday") property.

    iterweekdays()[¶](#calendar.Calendar.iterweekdays "Link to this definition")
    :   Return an iterator for the week day numbers that will be used for one
        week. The first value from the iterator will be the same as the value of
        the [`firstweekday`](#calendar.Calendar.firstweekday "calendar.Calendar.firstweekday") property.

    itermonthdates(*year*, *month*)[¶](#calendar.Calendar.itermonthdates "Link to this definition")
    :   Return an iterator for the month *month* (1–12) in the year *year*. This
        iterator will return all days (as [`datetime.date`](datetime.html#datetime.date "datetime.date") objects) for the
        month and all days before the start of the month or after the end of the
        month that are required to get a complete week.

    itermonthdays(*year*, *month*)[¶](#calendar.Calendar.itermonthdays "Link to this definition")
    :   Return an iterator for the month *month* in the year *year* similar to
        [`itermonthdates()`](#calendar.Calendar.itermonthdates "calendar.Calendar.itermonthdates"), but not restricted by the [`datetime.date`](datetime.html#datetime.date "datetime.date")
        range. Days returned will simply be day of the month numbers. For the
        days outside of the specified month, the day number is `0`.

    itermonthdays2(*year*, *month*)[¶](#calendar.Calendar.itermonthdays2 "Link to this definition")
    :   Return an iterator for the month *month* in the year *year* similar to
        [`itermonthdates()`](#calendar.Calendar.itermonthdates "calendar.Calendar.itermonthdates"), but not restricted by the [`datetime.date`](datetime.html#datetime.date "datetime.date")
        range. Days returned will be tuples consisting of a day of the month
        number and a week day number.

    itermonthdays3(*year*, *month*)[¶](#calendar.Calendar.itermonthdays3 "Link to this definition")
    :   Return an iterator for the month *month* in the year *year* similar to
        [`itermonthdates()`](#calendar.Calendar.itermonthdates "calendar.Calendar.itermonthdates"), but not restricted by the [`datetime.date`](datetime.html#datetime.date "datetime.date")
        range. Days returned will be tuples consisting of a year, a month and a day
        of the month numbers.

        Added in version 3.7.

    itermonthdays4(*year*, *month*)[¶](#calendar.Calendar.itermonthdays4 "Link to this definition")
    :   Return an iterator for the month *month* in the year *year* similar to
        [`itermonthdates()`](#calendar.Calendar.itermonthdates "calendar.Calendar.itermonthdates"), but not restricted by the [`datetime.date`](datetime.html#datetime.date "datetime.date")
        range. Days returned will be tuples consisting of a year, a month, a day
        of the month, and a day of the week numbers.

        Added in version 3.7.

    monthdatescalendar(*year*, *month*)[¶](#calendar.Calendar.monthdatescalendar "Link to this definition")
    :   Return a list of the weeks in the month *month* of the *year* as full
        weeks. Weeks are lists of seven [`datetime.date`](datetime.html#datetime.date "datetime.date") objects.

    monthdays2calendar(*year*, *month*)[¶](#calendar.Calendar.monthdays2calendar "Link to this definition")
    :   Return a list of the weeks in the month *month* of the *year* as full
        weeks. Weeks are lists of seven tuples of day numbers and weekday
        numbers.

    monthdayscalendar(*year*, *month*)[¶](#calendar.Calendar.monthdayscalendar "Link to this definition")
    :   Return a list of the weeks in the month *month* of the *year* as full
        weeks. Weeks are lists of seven day numbers.

    yeardatescalendar(*year*, *width=3*)[¶](#calendar.Calendar.yeardatescalendar "Link to this definition")
    :   Return the data for the specified year ready for formatting. The return
        value is a list of month rows. Each month row contains up to *width*
        months (defaulting to 3). Each month contains between 4 and 6 weeks and
        each week contains 1–7 days. Days are [`datetime.date`](datetime.html#datetime.date "datetime.date") objects.

    yeardays2calendar(*year*, *width=3*)[¶](#calendar.Calendar.yeardays2calendar "Link to this definition")
    :   Return the data for the specified year ready for formatting (similar to
        [`yeardatescalendar()`](#calendar.Calendar.yeardatescalendar "calendar.Calendar.yeardatescalendar")). Entries in the week lists are tuples of day
        numbers and weekday numbers. Day numbers outside this month are zero.

    yeardayscalendar(*year*, *width=3*)[¶](#calendar.Calendar.yeardayscalendar "Link to this definition")
    :   Return the data for the specified year ready for formatting (similar to
        [`yeardatescalendar()`](#calendar.Calendar.yeardatescalendar "calendar.Calendar.yeardatescalendar")). Entries in the week lists are day numbers. Day
        numbers outside this month are zero.

*class* calendar.TextCalendar(*firstweekday=0*)[¶](#calendar.TextCalendar "Link to this definition")
:   This class can be used to generate plain text calendars.

    [`TextCalendar`](#calendar.TextCalendar "calendar.TextCalendar") instances have the following methods:

    formatday(*theday*, *weekday*, *width*)[¶](#calendar.TextCalendar.formatday "Link to this definition")
    :   Return a string representing a single day formatted with the given *width*.
        If *theday* is `0`, return a string of spaces of
        the specified width, representing an empty day. The *weekday* parameter
        is unused.

    formatweek(*theweek*, *w=0*)[¶](#calendar.TextCalendar.formatweek "Link to this definition")
    :   Return a single week in a string with no newline. If *w* is provided, it
        specifies the width of the date columns, which are centered. Depends
        on the first weekday as specified in the constructor or set by the
        [`setfirstweekday()`](#calendar.setfirstweekday "calendar.setfirstweekday") method.

    formatweekday(*weekday*, *width*)[¶](#calendar.TextCalendar.formatweekday "Link to this definition")
    :   Return a string representing the name of a single weekday formatted to
        the specified *width*. The *weekday* parameter is an integer representing
        the day of the week, where `0` is Monday and `6` is Sunday.

    formatweekheader(*width*)[¶](#calendar.TextCalendar.formatweekheader "Link to this definition")
    :   Return a string containing the header row of weekday names, formatted
        with the given *width* for each column. The names depend on the locale
        settings and are padded to the specified width.

    formatmonth(*theyear*, *themonth*, *w=0*, *l=0*)[¶](#calendar.TextCalendar.formatmonth "Link to this definition")
    :   Return a month’s calendar in a multi-line string. If *w* is provided, it
        specifies the width of the date columns, which are centered. If *l* is
        given, it specifies the number of lines that each week will use. Depends
        on the first weekday as specified in the constructor or set by the
        [`setfirstweekday()`](#calendar.setfirstweekday "calendar.setfirstweekday") method.

    formatmonthname(*theyear*, *themonth*, *width=0*, *withyear=True*)[¶](#calendar.TextCalendar.formatmonthname "Link to this definition")
    :   Return a string representing the month’s name centered within the
        specified *width*. If *withyear* is `True`, include the year in the
        output. The *theyear* and *themonth* parameters specify the year
        and month for the name to be formatted respectively.

    prmonth(*theyear*, *themonth*, *w=0*, *l=0*)[¶](#calendar.TextCalendar.prmonth "Link to this definition")
    :   Print a month’s calendar as returned by [`formatmonth()`](#calendar.TextCalendar.formatmonth "calendar.TextCalendar.formatmonth").

    formatyear(*theyear*, *w=2*, *l=1*, *c=6*, *m=3*)[¶](#calendar.TextCalendar.formatyear "Link to this definition")
    :   Return a *m*-column calendar for an entire year as a multi-line string.
        Optional parameters *w*, *l*, and *c* are for date column width, lines per
        week, and number of spaces between month columns, respectively. Depends on
        the first weekday as specified in the constructor or set by the
        [`setfirstweekday()`](#calendar.setfirstweekday "calendar.setfirstweekday") method. The earliest year for which a calendar
        can be generated is platform-dependent.

    pryear(*theyear*, *w=2*, *l=1*, *c=6*, *m=3*)[¶](#calendar.TextCalendar.pryear "Link to this definition")
    :   Print the calendar for an entire year as returned by [`formatyear()`](#calendar.TextCalendar.formatyear "calendar.TextCalendar.formatyear").

*class* calendar.HTMLCalendar(*firstweekday=0*)[¶](#calendar.HTMLCalendar "Link to this definition")
:   This class can be used to generate HTML calendars.

    `HTMLCalendar` instances have the following methods:

    formatmonth(*theyear*, *themonth*, *withyear=True*)[¶](#calendar.HTMLCalendar.formatmonth "Link to this definition")
    :   Return a month’s calendar as an HTML table. If *withyear* is true the year
        will be included in the header, otherwise just the month name will be
        used.

    formatyear(*theyear*, *width=3*)[¶](#calendar.HTMLCalendar.formatyear "Link to this definition")
    :   Return a year’s calendar as an HTML table. *width* (defaulting to 3)
        specifies the number of months per row.

    formatyearpage(*theyear*, *width=3*, *css='calendar.css'*, *encoding=None*)[¶](#calendar.HTMLCalendar.formatyearpage "Link to this definition")
    :   Return a year’s calendar as a complete HTML page. *width* (defaulting to
        3) specifies the number of months per row. *css* is the name for the
        cascading style sheet to be used. [`None`](constants.html#None "None") can be passed if no style
        sheet should be used. *encoding* specifies the encoding to be used for the
        output (defaulting to the system default encoding).

    formatmonthname(*theyear*, *themonth*, *withyear=True*)[¶](#calendar.HTMLCalendar.formatmonthname "Link to this definition")
    :   Return a month name as an HTML table row. If *withyear* is true the year
        will be included in the row, otherwise just the month name will be
        used.

    `HTMLCalendar` has the following attributes you can override to
    customize the CSS classes used by the calendar:

    cssclasses[¶](#calendar.HTMLCalendar.cssclasses "Link to this definition")
    :   A list of CSS classes used for each weekday. The default class list is:

        ```
        cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        ```

        more styles can be added for each day:

        ```
        cssclasses = ["mon text-bold", "tue", "wed", "thu", "fri", "sat", "sun red"]
        ```

        Note that the length of this list must be seven items.

    cssclass\_noday[¶](#calendar.HTMLCalendar.cssclass_noday "Link to this definition")
    :   The CSS class for a weekday occurring in the previous or coming month.

        Added in version 3.7.

    cssclasses\_weekday\_head[¶](#calendar.HTMLCalendar.cssclasses_weekday_head "Link to this definition")
    :   A list of CSS classes used for weekday names in the header row.
        The default is the same as [`cssclasses`](#calendar.HTMLCalendar.cssclasses "calendar.HTMLCalendar.cssclasses").

        Added in version 3.7.

    cssclass\_month\_head[¶](#calendar.HTMLCalendar.cssclass_month_head "Link to this definition")
    :   The month’s head CSS class (used by [`formatmonthname()`](#calendar.HTMLCalendar.formatmonthname "calendar.HTMLCalendar.formatmonthname")).
        The default value is `"month"`.

        Added in version 3.7.

    cssclass\_month[¶](#calendar.HTMLCalendar.cssclass_month "Link to this definition")
    :   The CSS class for the whole month’s table (used by [`formatmonth()`](#calendar.HTMLCalendar.formatmonth "calendar.HTMLCalendar.formatmonth")).
        The default value is `"month"`.

        Added in version 3.7.

    cssclass\_year[¶](#calendar.HTMLCalendar.cssclass_year "Link to this definition")
    :   The CSS class for the whole year’s table of tables (used by
        [`formatyear()`](#calendar.HTMLCalendar.formatyear "calendar.HTMLCalendar.formatyear")). The default value is `"year"`.

        Added in version 3.7.

    cssclass\_year\_head[¶](#calendar.HTMLCalendar.cssclass_year_head "Link to this definition")
    :   The CSS class for the table head for the whole year (used by
        [`formatyear()`](#calendar.HTMLCalendar.formatyear "calendar.HTMLCalendar.formatyear")). The default value is `"year"`.

        Added in version 3.7.

    Note that although the naming for the above described class attributes is
    singular (e.g. `cssclass_month` `cssclass_noday`), one can replace the
    single CSS class with a space separated list of CSS classes, for example:

    ```
    "text-bold text-red"
    ```

    Here is an example how `HTMLCalendar` can be customized:

    ```
    class CustomHTMLCal(calendar.HTMLCalendar):
        cssclasses = [style + " text-nowrap" for style in
                      calendar.HTMLCalendar.cssclasses]
        cssclass_month_head = "text-center month-head"
        cssclass_month = "text-center month"
        cssclass_year = "text-italic lead"
    ```

*class* calendar.LocaleTextCalendar(*firstweekday=0*, *locale=None*)[¶](#calendar.LocaleTextCalendar "Link to this definition")
:   This subclass of [`TextCalendar`](#calendar.TextCalendar "calendar.TextCalendar") can be passed a locale name in the
    constructor and will return month and weekday names in the specified locale.

*class* calendar.LocaleHTMLCalendar(*firstweekday=0*, *locale=None*)[¶](#calendar.LocaleHTMLCalendar "Link to this definition")
:   This subclass of [`HTMLCalendar`](#calendar.HTMLCalendar "calendar.HTMLCalendar") can be passed a locale name in the
    constructor and will return month and weekday names in the specified
    locale.

Note

The constructor, `formatweekday()` and `formatmonthname()` methods
of these two classes temporarily change the `LC_TIME` locale to the given
*locale*. Because the current locale is a process-wide setting, they are
not thread-safe.

For simple text calendars this module provides the following functions.

calendar.setfirstweekday(*weekday*)[¶](#calendar.setfirstweekday "Link to this definition")
:   Sets the weekday (`0` is Monday, `6` is Sunday) to start each week. The
    values [`MONDAY`](#calendar.MONDAY "calendar.MONDAY"), [`TUESDAY`](#calendar.TUESDAY "calendar.TUESDAY"), [`WEDNESDAY`](#calendar.WEDNESDAY "calendar.WEDNESDAY"), [`THURSDAY`](#calendar.THURSDAY "calendar.THURSDAY"),
    [`FRIDAY`](#calendar.FRIDAY "calendar.FRIDAY"), [`SATURDAY`](#calendar.SATURDAY "calendar.SATURDAY"), and [`SUNDAY`](#calendar.SUNDAY "calendar.SUNDAY") are provided for
    convenience. For example, to set the first weekday to Sunday:

    ```
    import calendar
    calendar.setfirstweekday(calendar.SUNDAY)
    ```

calendar.firstweekday()[¶](#calendar.firstweekday "Link to this definition")
:   Returns the current setting for the weekday to start each week.

calendar.isleap(*year*)[¶](#calendar.isleap "Link to this definition")
:   Returns [`True`](constants.html#True "True") if *year* is a leap year, otherwise [`False`](constants.html#False "False").

calendar.leapdays(*y1*, *y2*)[¶](#calendar.leapdays "Link to this definition")
:   Returns the number of leap years in the range from *y1* to *y2* (exclusive),
    where *y1* and *y2* are years.

    This function works for ranges spanning a century change.

calendar.weekday(*year*, *month*, *day*)[¶](#calendar.weekday "Link to this definition")
:   Returns the day of the week (`0` is Monday) for *year* (`1970`–…),
    *month* (`1`–`12`), *day* (`1`–`31`).

calendar.weekheader(*n*)[¶](#calendar.weekheader "Link to this definition")
:   Return a header containing abbreviated weekday names. *n* specifies the width in
    characters for one weekday.

calendar.monthrange(*year*, *month*)[¶](#calendar.monthrange "Link to this definition")
:   Returns weekday of first day of the month and number of days in month, for the
    specified *year* and *month*.

calendar.monthcalendar(*year*, *month*)[¶](#calendar.monthcalendar "Link to this definition")
:   Returns a matrix representing a month’s calendar. Each row represents a week;
    days outside of the month are represented by zeros. Each week begins with Monday
    unless set by [`setfirstweekday()`](#calendar.setfirstweekday "calendar.setfirstweekday").

calendar.prmonth(*theyear*, *themonth*, *w=0*, *l=0*)[¶](#calendar.prmonth "Link to this definition")
:   Prints a month’s calendar as returned by [`month()`](#calendar.month "calendar.month").

calendar.month(*theyear*, *themonth*, *w=0*, *l=0*)[¶](#calendar.month "Link to this definition")
:   Returns a month’s calendar in a multi-line string using the [`formatmonth()`](#calendar.TextCalendar.formatmonth "calendar.TextCalendar.formatmonth")
    of the [`TextCalendar`](#calendar.TextCalendar "calendar.TextCalendar") class.

calendar.prcal(*year*, *w=0*, *l=0*, *c=6*, *m=3*)[¶](#calendar.prcal "Link to this definition")
:   Prints the calendar for an entire year as returned by [`calendar()`](#module-calendar "calendar: Functions for working with calendars, including some emulation of the Unix cal program.").

calendar.calendar(*year*, *w=2*, *l=1*, *c=6*, *m=3*)[¶](#calendar.calendar "Link to this definition")
:   Returns a 3-column calendar for an entire year as a multi-line string using
    the [`formatyear()`](#calendar.TextCalendar.formatyear "calendar.TextCalendar.formatyear") of the [`TextCalendar`](#calendar.TextCalendar "calendar.TextCalendar") class.

calendar.timegm(*tuple*)[¶](#calendar.timegm "Link to this definition")
:   An unrelated but handy function that takes a time tuple such as returned by
    the [`gmtime()`](time.html#time.gmtime "time.gmtime") function in the [`time`](time.html#module-time "time: Time access and conversions.") module, and returns the
    corresponding Unix timestamp value, assuming an epoch of 1970, and the POSIX
    encoding. In fact, [`time.gmtime()`](time.html#time.gmtime "time.gmtime") and [`timegm()`](#calendar.timegm "calendar.timegm") are each others’
    inverse.

The `calendar` module exports the following data attributes:

calendar.day\_name[¶](#calendar.day_name "Link to this definition")
:   A sequence that represents the days of the week in the current locale,
    where Monday is day number 0.

    ```
    >>> import calendar
    >>> list(calendar.day_name)
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ```

calendar.day\_abbr[¶](#calendar.day_abbr "Link to this definition")
:   A sequence that represents the abbreviated days of the week in the current locale,
    where Mon is day number 0.

    ```
    >>> import calendar
    >>> list(calendar.day_abbr)
    ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ```

calendar.MONDAY[¶](#calendar.MONDAY "Link to this definition")

calendar.TUESDAY[¶](#calendar.TUESDAY "Link to this definition")

calendar.WEDNESDAY[¶](#calendar.WEDNESDAY "Link to this definition")

calendar.THURSDAY[¶](#calendar.THURSDAY "Link to this definition")

calendar.FRIDAY[¶](#calendar.FRIDAY "Link to this definition")

calendar.SATURDAY[¶](#calendar.SATURDAY "Link to this definition")

calendar.SUNDAY[¶](#calendar.SUNDAY "Link to this definition")
:   Aliases for the days of the week,
    where `MONDAY` is `0` and `SUNDAY` is `6`.

    Added in version 3.12.

*class* calendar.Day[¶](#calendar.Day "Link to this definition")
:   Enumeration defining days of the week as integer constants.
    The members of this enumeration are exported to the module scope as
    [`MONDAY`](#calendar.MONDAY "calendar.MONDAY") through [`SUNDAY`](#calendar.SUNDAY "calendar.SUNDAY").

    Added in version 3.12.

calendar.month\_name[¶](#calendar.month_name "Link to this definition")
:   A sequence that represents the months of the year in the current locale. This
    follows normal convention of January being month number 1, so it has a length of
    13 and `month_name[0]` is the empty string.

    ```
    >>> import calendar
    >>> list(calendar.month_name)
    ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ```

calendar.month\_abbr[¶](#calendar.month_abbr "Link to this definition")
:   A sequence that represents the abbreviated months of the year in the current
    locale. This follows normal convention of January being month number 1, so it
    has a length of 13 and `month_abbr[0]` is the empty string.

    ```
    >>> import calendar
    >>> list(calendar.month_abbr)
    ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ```

calendar.JANUARY[¶](#calendar.JANUARY "Link to this definition")

calendar.FEBRUARY[¶](#calendar.FEBRUARY "Link to this definition")

calendar.MARCH[¶](#calendar.MARCH "Link to this definition")

calendar.APRIL[¶](#calendar.APRIL "Link to this definition")

calendar.MAY[¶](#calendar.MAY "Link to this definition")

calendar.JUNE[¶](#calendar.JUNE "Link to this definition")

calendar.JULY[¶](#calendar.JULY "Link to this definition")

calendar.AUGUST[¶](#calendar.AUGUST "Link to this definition")

calendar.SEPTEMBER[¶](#calendar.SEPTEMBER "Link to this definition")

calendar.OCTOBER[¶](#calendar.OCTOBER "Link to this definition")

calendar.NOVEMBER[¶](#calendar.NOVEMBER "Link to this definition")

calendar.DECEMBER[¶](#calendar.DECEMBER "Link to this definition")
:   Aliases for the months of the year,
    where `JANUARY` is `1` and `DECEMBER` is `12`.

    Added in version 3.12.

*class* calendar.Month[¶](#calendar.Month "Link to this definition")
:   Enumeration defining months of the year as integer constants.
    The members of this enumeration are exported to the module scope as
    [`JANUARY`](#calendar.JANUARY "calendar.JANUARY") through [`DECEMBER`](#calendar.DECEMBER "calendar.DECEMBER").

    Added in version 3.12.

The `calendar` module defines the following exceptions:

*exception* calendar.IllegalMonthError(*month*)[¶](#calendar.IllegalMonthError "Link to this definition")
:   A subclass of [`ValueError`](exceptions.html#ValueError "ValueError"),
    raised when the given month number is outside of the range 1-12 (inclusive).

    month[¶](#calendar.IllegalMonthError.month "Link to this definition")
    :   The invalid month number.

*exception* calendar.IllegalWeekdayError(*weekday*)[¶](#calendar.IllegalWeekdayError "Link to this definition")
:   A subclass of [`ValueError`](exceptions.html#ValueError "ValueError"),
    raised when the given weekday number is outside of the range 0-6 (inclusive).

    weekday[¶](#calendar.IllegalWeekdayError.weekday "Link to this definition")
    :   The invalid weekday number.

See also

Module [`datetime`](datetime.html#module-datetime "datetime: Basic date and time types.")
:   Object-oriented interface to dates and times with similar functionality to the
    [`time`](time.html#module-time "time: Time access and conversions.") module.

Module [`time`](time.html#module-time "time: Time access and conversions.")
:   Low-level time related functions.

## Command-line usage[¶](#command-line-usage "Link to this heading")

Added in version 2.5.

The `calendar` module can be executed as a script from the command line
to interactively print a calendar.

```
python -m calendar [-h] [-L LOCALE] [-e ENCODING] [-t {text,html}]
                   [-w WIDTH] [-l LINES] [-s SPACING] [-m MONTHS] [-c CSS]
                   [-f FIRST_WEEKDAY] [year] [month]
```

For example, to print a calendar for the year 2000:

```
$ python -m calendar 2000
                                  2000

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6             1  2  3  4  5
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       6  7  8  9 10 11 12
10 11 12 13 14 15 16      14 15 16 17 18 19 20      13 14 15 16 17 18 19
17 18 19 20 21 22 23      21 22 23 24 25 26 27      20 21 22 23 24 25 26
24 25 26 27 28 29 30      28 29                     27 28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2       1  2  3  4  5  6  7                1  2  3  4
 3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                   1  2  3
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5                   1  2  3
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
30 31
```

The following options are accepted:

--help, -h[¶](#cmdoption-calendar-help "Link to this definition")
:   Show the help message and exit.

--locale LOCALE, -L LOCALE[¶](#cmdoption-calendar-locale "Link to this definition")
:   The locale to use for month and weekday names.
    Defaults to English.

--encoding ENCODING, -e ENCODING[¶](#cmdoption-calendar-encoding "Link to this definition")
:   The encoding to use for output.
    [`--encoding`](#cmdoption-calendar-encoding) is required if [`--locale`](#cmdoption-calendar-locale) is set.

--type {text,html}, -t {text,html}[¶](#cmdoption-calendar-type "Link to this definition")
:   Print the calendar to the terminal as text,
    or as an HTML document.

--first-weekday FIRST\_WEEKDAY, -f FIRST\_WEEKDAY[¶](#cmdoption-calendar-first-weekday "Link to this definition")
:   The weekday to start each week.
    Must be a number between 0 (Monday) and 6 (Sunday).
    Defaults to 0.

    Added in version 3.13.

year[¶](#cmdoption-calendar-arg-year "Link to this definition")
:   The year to print the calendar for.
    Defaults to the current year.

month[¶](#cmdoption-calendar-arg-month "Link to this definition")
:   The month of the specified [`year`](#cmdoption-calendar-arg-year) to print the calendar for.
    Must be a number between 1 and 12,
    and may only be used in text mode.
    Defaults to printing a calendar for the full year.

*Text-mode options:*

--width WIDTH, -w WIDTH[¶](#cmdoption-calendar-width "Link to this definition")
:   The width of the date column in terminal columns.
    The date is printed centred in the column.
    Any value lower than 2 is ignored.
    Defaults to 2.

--lines LINES, -l LINES[¶](#cmdoption-calendar-lines "Link to this definition")
:   The number of lines for each week in terminal rows.
    The date is printed top-aligned.
    Any value lower than 1 is ignored.
    Defaults to 1.

--spacing SPACING, -s SPACING[¶](#cmdoption-calendar-spacing "Link to this definition")
:   The space between months in columns.
    Any value lower than 2 is ignored.
    Defaults to 6.

--months MONTHS, -m MONTHS[¶](#cmdoption-calendar-months "Link to this definition")
:   The number of months printed per row.
    Defaults to 3.

Changed in version 3.14: By default, today’s date is highlighted in color and can be
[controlled using environment variables](../using/cmdline.html#using-on-controlling-color).

*HTML-mode options:*

--css CSS, -c CSS[¶](#cmdoption-calendar-css "Link to this definition")
:   The path of a CSS stylesheet to use for the calendar.
    This must either be relative to the generated HTML,
    or an absolute HTTP or `file:///` URL.

### [Table of Contents](../contents.html)

* [`calendar` — General calendar-related functions](#)
  + [Command-line usage](#command-line-usage)

#### Previous topic

[`zoneinfo` — IANA time zone support](zoneinfo.html "previous chapter")

#### Next topic

[`collections` — Container datatypes](collections.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/calendar.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](collections.html "collections — Container datatypes") |
* [previous](zoneinfo.html "zoneinfo — IANA time zone support") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Data Types](datatypes.html) »
* `calendar` — General calendar-related functions
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
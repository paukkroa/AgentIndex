### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](datetime.html "datetime — Basic date and time types") |
* [previous](codecs.html "codecs — Codec registry and base classes") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Data Types
* |
* Theme
  Auto
  Light
  Dark
   |

# Data Types[¶](#data-types "Link to this heading")

The modules described in this chapter provide a variety of specialized data
types such as dates and times, fixed-type arrays, heap queues, double-ended
queues, and enumerations.

Python also provides some built-in data types, in particular,
[`dict`](stdtypes.html#dict "dict"), [`list`](stdtypes.html#list "list"), [`set`](stdtypes.html#set "set") and [`frozenset`](stdtypes.html#frozenset "frozenset"), and
[`tuple`](stdtypes.html#tuple "tuple"). The [`str`](stdtypes.html#str "str") class is used to hold
Unicode strings, and the [`bytes`](stdtypes.html#bytes "bytes") and [`bytearray`](stdtypes.html#bytearray "bytearray") classes are used
to hold binary data.

The following modules are documented in this chapter:

* [`datetime` — Basic date and time types](datetime.html)
  + [Aware and naive objects](datetime.html#aware-and-naive-objects)
  + [Constants](datetime.html#constants)
  + [Available types](datetime.html#available-types)
    - [Common properties](datetime.html#common-properties)
    - [Determining if an object is aware or naive](datetime.html#determining-if-an-object-is-aware-or-naive)
  + [`timedelta` objects](datetime.html#timedelta-objects)
    - [Examples of usage: `timedelta`](datetime.html#examples-of-usage-timedelta)
  + [`date` objects](datetime.html#date-objects)
    - [Examples of usage: `date`](datetime.html#examples-of-usage-date)
  + [`datetime` objects](datetime.html#datetime-objects)
    - [Examples of usage: `datetime`](datetime.html#examples-of-usage-datetime)
  + [`time` objects](datetime.html#time-objects)
    - [Examples of usage: `time`](datetime.html#examples-of-usage-time)
  + [`tzinfo` objects](datetime.html#tzinfo-objects)
  + [`timezone` objects](datetime.html#timezone-objects)
  + [`strftime()` and `strptime()` behavior](datetime.html#strftime-and-strptime-behavior)
    - [`strftime()` and `strptime()` format codes](datetime.html#strftime-and-strptime-format-codes)
    - [Technical detail](datetime.html#technical-detail)
* [`zoneinfo` — IANA time zone support](zoneinfo.html)
  + [Using `ZoneInfo`](zoneinfo.html#using-zoneinfo)
  + [Data sources](zoneinfo.html#data-sources)
    - [Configuring the data sources](zoneinfo.html#configuring-the-data-sources)
      * [Compile-time configuration](zoneinfo.html#compile-time-configuration)
      * [Environment configuration](zoneinfo.html#environment-configuration)
      * [Runtime configuration](zoneinfo.html#runtime-configuration)
  + [The `ZoneInfo` class](zoneinfo.html#the-zoneinfo-class)
    - [String representations](zoneinfo.html#string-representations)
    - [Pickle serialization](zoneinfo.html#pickle-serialization)
  + [Functions](zoneinfo.html#functions)
  + [Globals](zoneinfo.html#globals)
  + [Exceptions and warnings](zoneinfo.html#exceptions-and-warnings)
* [`calendar` — General calendar-related functions](calendar.html)
  + [Command-line usage](calendar.html#command-line-usage)
* [`collections` — Container datatypes](collections.html)
  + [`ChainMap` objects](collections.html#chainmap-objects)
    - [`ChainMap` Examples and Recipes](collections.html#chainmap-examples-and-recipes)
  + [`Counter` objects](collections.html#counter-objects)
  + [`deque` objects](collections.html#deque-objects)
    - [`deque` Recipes](collections.html#deque-recipes)
  + [`defaultdict` objects](collections.html#defaultdict-objects)
    - [`defaultdict` Examples](collections.html#defaultdict-examples)
  + [`namedtuple()` Factory Function for Tuples with Named Fields](collections.html#namedtuple-factory-function-for-tuples-with-named-fields)
  + [`OrderedDict` objects](collections.html#ordereddict-objects)
    - [`OrderedDict` Examples and Recipes](collections.html#ordereddict-examples-and-recipes)
  + [`UserDict` objects](collections.html#userdict-objects)
  + [`UserList` objects](collections.html#userlist-objects)
  + [`UserString` objects](collections.html#userstring-objects)
* [`collections.abc` — Abstract Base Classes for Containers](collections.abc.html)
  + [Collections Abstract Base Classes](collections.abc.html#collections-abstract-base-classes)
  + [Collections Abstract Base Classes – Detailed Descriptions](collections.abc.html#collections-abstract-base-classes-detailed-descriptions)
  + [Examples and Recipes](collections.abc.html#examples-and-recipes)
* [`heapq` — Heap queue algorithm](heapq.html)
  + [Basic Examples](heapq.html#basic-examples)
  + [Other Applications](heapq.html#other-applications)
  + [Priority Queue Implementation Notes](heapq.html#priority-queue-implementation-notes)
  + [Theory](heapq.html#theory)
* [`bisect` — Array bisection algorithm](bisect.html)
  + [Performance Notes](bisect.html#performance-notes)
  + [Searching Sorted Lists](bisect.html#searching-sorted-lists)
  + [Examples](bisect.html#examples)
* [`array` — Efficient arrays of numeric values](array.html)
* [`weakref` — Weak references](weakref.html)
  + [Weak Reference Objects](weakref.html#weak-reference-objects)
  + [Example](weakref.html#example)
  + [Finalizer Objects](weakref.html#finalizer-objects)
  + [Comparing finalizers with `__del__()` methods](weakref.html#comparing-finalizers-with-del-methods)
* [`types` — Dynamic type creation and names for built-in types](types.html)
  + [Dynamic Type Creation](types.html#dynamic-type-creation)
  + [Standard Interpreter Types](types.html#standard-interpreter-types)
  + [Additional Utility Classes and Functions](types.html#additional-utility-classes-and-functions)
  + [Coroutine Utility Functions](types.html#coroutine-utility-functions)
* [`copy` — Shallow and deep copy operations](copy.html)
* [`pprint` — Data pretty printer](pprint.html)
  + [Functions](pprint.html#functions)
  + [PrettyPrinter Objects](pprint.html#prettyprinter-objects)
  + [Example](pprint.html#example)
* [`reprlib` — Alternate `repr()` implementation](reprlib.html)
  + [Repr Objects](reprlib.html#repr-objects)
  + [Subclassing Repr Objects](reprlib.html#subclassing-repr-objects)
* [`enum` — Support for enumerations](enum.html)
  + [Module Contents](enum.html#module-contents)
  + [Data Types](enum.html#data-types)
    - [Supported `__dunder__` names](enum.html#supported-dunder-names)
    - [Supported `_sunder_` names](enum.html#supported-sunder-names)
  + [Utilities and Decorators](enum.html#utilities-and-decorators)
  + [Notes](enum.html#notes)
* [`graphlib` — Functionality to operate with graph-like structures](graphlib.html)
  + [Exceptions](graphlib.html#exceptions)

#### Previous topic

[`codecs` — Codec registry and base classes](codecs.html "previous chapter")

#### Next topic

[`datetime` — Basic date and time types](datetime.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/datatypes.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](datetime.html "datetime — Basic date and time types") |
* [previous](codecs.html "codecs — Codec registry and base classes") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Data Types
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
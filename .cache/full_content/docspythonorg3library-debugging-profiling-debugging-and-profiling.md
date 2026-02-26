### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](audit_events.html "Audit events table") |
* [previous](test.html "test — Regression tests package for Python") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Debugging and Profiling
* |
* Theme
  Auto
  Light
  Dark
   |

# Debugging and Profiling[¶](#debugging-and-profiling "Link to this heading")

These libraries help you with Python development: the debugger enables you to
step through code, analyze stack frames and set breakpoints etc., and the
profilers run code and give you a detailed breakdown of execution times,
allowing you to identify bottlenecks in your programs. Auditing events
provide visibility into runtime behaviors that would otherwise require
intrusive debugging or patching.

* [Audit events table](audit_events.html)
* [`bdb` — Debugger framework](bdb.html)
* [`faulthandler` — Dump the Python traceback](faulthandler.html)
  + [Dumping the traceback](faulthandler.html#dumping-the-traceback)
  + [Dumping the C stack](faulthandler.html#dumping-the-c-stack)
    - [C Stack Compatibility](faulthandler.html#c-stack-compatibility)
  + [Fault handler state](faulthandler.html#fault-handler-state)
  + [Dumping the tracebacks after a timeout](faulthandler.html#dumping-the-tracebacks-after-a-timeout)
  + [Dumping the traceback on a user signal](faulthandler.html#dumping-the-traceback-on-a-user-signal)
  + [Issue with file descriptors](faulthandler.html#issue-with-file-descriptors)
  + [Example](faulthandler.html#example)
* [`pdb` — The Python Debugger](pdb.html)
  + [Command-line interface](pdb.html#command-line-interface)
  + [Debugger commands](pdb.html#debugger-commands)
* [The Python Profilers](profile.html)
  + [Introduction to the profilers](profile.html#introduction-to-the-profilers)
  + [Instant User’s Manual](profile.html#instant-user-s-manual)
  + [`profile` and `cProfile` Module Reference](profile.html#module-cProfile)
  + [The `Stats` Class](profile.html#the-stats-class)
  + [What Is Deterministic Profiling?](profile.html#what-is-deterministic-profiling)
  + [Limitations](profile.html#limitations)
  + [Calibration](profile.html#calibration)
  + [Using a custom timer](profile.html#using-a-custom-timer)
* [`timeit` — Measure execution time of small code snippets](timeit.html)
  + [Basic Examples](timeit.html#basic-examples)
  + [Python Interface](timeit.html#python-interface)
  + [Command-Line Interface](timeit.html#command-line-interface)
  + [Examples](timeit.html#examples)
* [`trace` — Trace or track Python statement execution](trace.html)
  + [Command-Line Usage](trace.html#command-line-usage)
    - [Main options](trace.html#main-options)
    - [Modifiers](trace.html#modifiers)
    - [Filters](trace.html#filters)
  + [Programmatic Interface](trace.html#programmatic-interface)
* [`tracemalloc` — Trace memory allocations](tracemalloc.html)
  + [Examples](tracemalloc.html#examples)
    - [Display the top 10](tracemalloc.html#display-the-top-10)
    - [Compute differences](tracemalloc.html#compute-differences)
    - [Get the traceback of a memory block](tracemalloc.html#get-the-traceback-of-a-memory-block)
    - [Pretty top](tracemalloc.html#pretty-top)
      * [Record the current and peak size of all traced memory blocks](tracemalloc.html#record-the-current-and-peak-size-of-all-traced-memory-blocks)
  + [API](tracemalloc.html#api)
    - [Functions](tracemalloc.html#functions)
    - [DomainFilter](tracemalloc.html#domainfilter)
    - [Filter](tracemalloc.html#filter)
    - [Frame](tracemalloc.html#frame)
    - [Snapshot](tracemalloc.html#snapshot)
    - [Statistic](tracemalloc.html#statistic)
    - [StatisticDiff](tracemalloc.html#statisticdiff)
    - [Trace](tracemalloc.html#trace)
    - [Traceback](tracemalloc.html#traceback)

#### Previous topic

[`test` — Regression tests package for Python](test.html "previous chapter")

#### Next topic

[Audit events table](audit_events.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/debug.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](audit_events.html "Audit events table") |
* [previous](test.html "test — Regression tests package for Python") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Debugging and Profiling
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
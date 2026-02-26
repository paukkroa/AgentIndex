### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](queue.html "queue — A synchronized queue class") |
* [previous](subprocess.html "subprocess — Subprocess management") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Concurrent Execution](concurrency.html) »
* `sched` — Event scheduler
* |
* Theme
  Auto
  Light
  Dark
   |

# `sched` — Event scheduler[¶](#module-sched "Link to this heading")

**Source code:** [Lib/sched.py](https://github.com/python/cpython/tree/3.14/Lib/sched.py)

---

The `sched` module defines a class which implements a general purpose event
scheduler:

*class* sched.scheduler(*timefunc=time.monotonic*, *delayfunc=time.sleep*)[¶](#sched.scheduler "Link to this definition")
:   The [`scheduler`](#sched.scheduler "sched.scheduler") class defines a generic interface to scheduling events.
    It needs two functions to actually deal with the “outside world” — *timefunc*
    should be callable without arguments, and return a number (the “time”, in any
    units whatsoever). The *delayfunc* function should be callable with one
    argument, compatible with the output of *timefunc*, and should delay that many
    time units. *delayfunc* will also be called with the argument `0` after each
    event is run to allow other threads an opportunity to run in multi-threaded
    applications.

    Changed in version 3.3: *timefunc* and *delayfunc* parameters are optional.

    Changed in version 3.3: [`scheduler`](#sched.scheduler "sched.scheduler") class can be safely used in multi-threaded
    environments.

Example:

```
>>> import sched, time
>>> s = sched.scheduler(time.time, time.sleep)
>>> def print_time(a='default'):
...     print("From print_time", time.time(), a)
...
>>> def print_some_times():
...     print(time.time())
...     s.enter(10, 1, print_time)
...     s.enter(5, 2, print_time, argument=('positional',))
...     # despite having higher priority, 'keyword' runs after 'positional' as enter() is relative
...     s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
...     s.enterabs(1_650_000_000, 10, print_time, argument=("first enterabs",))
...     s.enterabs(1_650_000_000, 5, print_time, argument=("second enterabs",))
...     s.run()
...     print(time.time())
...
>>> print_some_times()
1652342830.3640375
From print_time 1652342830.3642538 second enterabs
From print_time 1652342830.3643398 first enterabs
From print_time 1652342835.3694863 positional
From print_time 1652342835.3696074 keyword
From print_time 1652342840.369612 default
1652342840.3697174
```

## Scheduler Objects[¶](#scheduler-objects "Link to this heading")

[`scheduler`](#sched.scheduler "sched.scheduler") instances have the following methods and attributes:

scheduler.enterabs(*time*, *priority*, *action*, *argument=()*, *kwargs={}*)[¶](#sched.scheduler.enterabs "Link to this definition")
:   Schedule a new event. The *time* argument should be a numeric type compatible
    with the return value of the *timefunc* function passed to the constructor.
    Events scheduled for the same *time* will be executed in the order of their
    *priority*. A lower number represents a higher priority.

    Executing the event means executing `action(*argument, **kwargs)`.
    *argument* is a sequence holding the positional arguments for *action*.
    *kwargs* is a dictionary holding the keyword arguments for *action*.

    Return value is an event which may be used for later cancellation of the event
    (see [`cancel()`](#sched.scheduler.cancel "sched.scheduler.cancel")).

    Changed in version 3.3: *argument* parameter is optional.

    Changed in version 3.3: *kwargs* parameter was added.

scheduler.enter(*delay*, *priority*, *action*, *argument=()*, *kwargs={}*)[¶](#sched.scheduler.enter "Link to this definition")
:   Schedule an event for *delay* more time units. Other than the relative time, the
    other arguments, the effect and the return value are the same as those for
    [`enterabs()`](#sched.scheduler.enterabs "sched.scheduler.enterabs").

    Changed in version 3.3: *argument* parameter is optional.

    Changed in version 3.3: *kwargs* parameter was added.

scheduler.cancel(*event*)[¶](#sched.scheduler.cancel "Link to this definition")
:   Remove the event from the queue. If *event* is not an event currently in the
    queue, this method will raise a [`ValueError`](exceptions.html#ValueError "ValueError").

scheduler.empty()[¶](#sched.scheduler.empty "Link to this definition")
:   Return `True` if the event queue is empty.

scheduler.run(*blocking=True*)[¶](#sched.scheduler.run "Link to this definition")
:   Run all scheduled events. This method will wait (using the *delayfunc*
    function passed to the constructor) for the next event, then execute it and so
    on until there are no more scheduled events.

    If *blocking* is false executes the scheduled events due to expire soonest
    (if any) and then return the deadline of the next scheduled call in the
    scheduler (if any).

    Either *action* or *delayfunc* can raise an exception. In either case, the
    scheduler will maintain a consistent state and propagate the exception. If an
    exception is raised by *action*, the event will not be attempted in future calls
    to [`run()`](#sched.scheduler.run "sched.scheduler.run").

    If a sequence of events takes longer to run than the time available before the
    next event, the scheduler will simply fall behind. No events will be dropped;
    the calling code is responsible for canceling events which are no longer
    pertinent.

    Changed in version 3.3: *blocking* parameter was added.

scheduler.queue[¶](#sched.scheduler.queue "Link to this definition")
:   Read-only attribute returning a list of upcoming events in the order they
    will be run. Each event is shown as a [named tuple](../glossary.html#term-named-tuple) with the
    following fields: time, priority, action, argument, kwargs.

### [Table of Contents](../contents.html)

* [`sched` — Event scheduler](#)
  + [Scheduler Objects](#scheduler-objects)

#### Previous topic

[`subprocess` — Subprocess management](subprocess.html "previous chapter")

#### Next topic

[`queue` — A synchronized queue class](queue.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/sched.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](queue.html "queue — A synchronized queue class") |
* [previous](subprocess.html "subprocess — Subprocess management") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Concurrent Execution](concurrency.html) »
* `sched` — Event scheduler
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
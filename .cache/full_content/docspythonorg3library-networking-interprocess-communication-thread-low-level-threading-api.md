### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](ipc.html "Networking and Interprocess Communication") |
* [previous](contextvars.html "contextvars — Context Variables") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Concurrent Execution](concurrency.html) »
* `_thread` — Low-level threading API
* |
* Theme
  Auto
  Light
  Dark
   |

# `_thread` — Low-level threading API[¶](#module-_thread "Link to this heading")

---

This module provides low-level primitives for working with multiple threads
(also called *light-weight processes* or *tasks*) — multiple threads of
control sharing their global data space. For synchronization, simple locks
(also called *mutexes* or *binary semaphores*) are provided.
The [`threading`](threading.html#module-threading "threading: Thread-based parallelism.") module provides an easier to use and higher-level
threading API built on top of this module.

Changed in version 3.7: This module used to be optional, it is now always available.

This module defines the following constants and functions:

*exception* \_thread.error[¶](#thread.error "Link to this definition")
:   Raised on thread-specific errors.

    Changed in version 3.3: This is now a synonym of the built-in [`RuntimeError`](exceptions.html#RuntimeError "RuntimeError").

\_thread.LockType[¶](#thread.LockType "Link to this definition")
:   This is the type of lock objects.

\_thread.start\_new\_thread(*function*, *args*[, *kwargs*])[¶](#thread.start_new_thread "Link to this definition")
:   Start a new thread and return its identifier. The thread executes the
    function *function* with the argument list *args* (which must be a tuple).
    The optional *kwargs* argument specifies a dictionary of keyword arguments.

    When the function returns, the thread silently exits.

    When the function terminates with an unhandled exception,
    [`sys.unraisablehook()`](sys.html#sys.unraisablehook "sys.unraisablehook") is called to handle the exception. The *object*
    attribute of the hook argument is *function*. By default, a stack trace is
    printed and then the thread exits (but other threads continue to run).

    When the function raises a [`SystemExit`](exceptions.html#SystemExit "SystemExit") exception, it is silently
    ignored.

    Raises an [auditing event](sys.html#auditing) `_thread.start_new_thread` with arguments `function`, `args`, `kwargs`.

    Changed in version 3.8: [`sys.unraisablehook()`](sys.html#sys.unraisablehook "sys.unraisablehook") is now used to handle unhandled exceptions.

\_thread.interrupt\_main(*signum=signal.SIGINT*, */*)[¶](#thread.interrupt_main "Link to this definition")
:   Simulate the effect of a signal arriving in the main thread.
    A thread can use this function to interrupt the main thread, though
    there is no guarantee that the interruption will happen immediately.

    If given, *signum* is the number of the signal to simulate.
    If *signum* is not given, [`signal.SIGINT`](signal.html#signal.SIGINT "signal.SIGINT") is simulated.

    If the given signal isn’t handled by Python (it was set to
    [`signal.SIG_DFL`](signal.html#signal.SIG_DFL "signal.SIG_DFL") or [`signal.SIG_IGN`](signal.html#signal.SIG_IGN "signal.SIG_IGN")), this function does
    nothing.

    Changed in version 3.10: The *signum* argument is added to customize the signal number.

    Note

    This does not emit the corresponding signal but schedules a call to
    the associated handler (if it exists).
    If you want to truly emit the signal, use [`signal.raise_signal()`](signal.html#signal.raise_signal "signal.raise_signal").

\_thread.exit()[¶](#thread.exit "Link to this definition")
:   Raise the [`SystemExit`](exceptions.html#SystemExit "SystemExit") exception. When not caught, this will cause the
    thread to exit silently.

\_thread.allocate\_lock()[¶](#thread.allocate_lock "Link to this definition")
:   Return a new lock object. Methods of locks are described below. The lock is
    initially unlocked.

\_thread.get\_ident()[¶](#thread.get_ident "Link to this definition")
:   Return the ‘thread identifier’ of the current thread. This is a nonzero
    integer. Its value has no direct meaning; it is intended as a magic cookie to
    be used e.g. to index a dictionary of thread-specific data. Thread identifiers
    may be recycled when a thread exits and another thread is created.

\_thread.get\_native\_id()[¶](#thread.get_native_id "Link to this definition")
:   Return the native integral Thread ID of the current thread assigned by the kernel.
    This is a non-negative integer.
    Its value may be used to uniquely identify this particular thread system-wide
    (until the thread terminates, after which the value may be recycled by the OS).

    [Availability](intro.html#availability): Windows, FreeBSD, Linux, macOS, OpenBSD, NetBSD, AIX, DragonFlyBSD, GNU/kFreeBSD.

    Added in version 3.8.

    Changed in version 3.13: Added support for GNU/kFreeBSD.

\_thread.stack\_size([*size*])[¶](#thread.stack_size "Link to this definition")
:   Return the thread stack size used when creating new threads. The optional
    *size* argument specifies the stack size to be used for subsequently created
    threads, and must be 0 (use platform or configured default) or a positive
    integer value of at least 32,768 (32 KiB). If *size* is not specified,
    0 is used. If changing the thread stack size is
    unsupported, a [`RuntimeError`](exceptions.html#RuntimeError "RuntimeError") is raised. If the specified stack size is
    invalid, a [`ValueError`](exceptions.html#ValueError "ValueError") is raised and the stack size is unmodified. 32 KiB
    is currently the minimum supported stack size value to guarantee sufficient
    stack space for the interpreter itself. Note that some platforms may have
    particular restrictions on values for the stack size, such as requiring a
    minimum stack size > 32 KiB or requiring allocation in multiples of the system
    memory page size - platform documentation should be referred to for more
    information (4 KiB pages are common; using multiples of 4096 for the stack size is
    the suggested approach in the absence of more specific information).

    [Availability](intro.html#availability): Windows, pthreads.

    Unix platforms with POSIX threads support.

\_thread.TIMEOUT\_MAX[¶](#thread.TIMEOUT_MAX "Link to this definition")
:   The maximum value allowed for the *timeout* parameter of
    [`Lock.acquire`](threading.html#threading.Lock.acquire "threading.Lock.acquire"). Specifying a timeout greater
    than this value will raise an [`OverflowError`](exceptions.html#OverflowError "OverflowError").

    Added in version 3.2.

Lock objects have the following methods:

lock.acquire(*blocking=True*, *timeout=-1*)[¶](#thread.lock.acquire "Link to this definition")
:   Without any optional argument, this method acquires the lock unconditionally, if
    necessary waiting until it is released by another thread (only one thread at a
    time can acquire a lock — that’s their reason for existence).

    If the *blocking* argument is present, the action depends on its
    value: if it is false, the lock is only acquired if it can be acquired
    immediately without waiting, while if it is true, the lock is acquired
    unconditionally as above.

    If the floating-point *timeout* argument is present and positive, it
    specifies the maximum wait time in seconds before returning. A negative
    *timeout* argument specifies an unbounded wait. You cannot specify
    a *timeout* if *blocking* is false.

    The return value is `True` if the lock is acquired successfully,
    `False` if not.

    Changed in version 3.2: The *timeout* parameter is new.

    Changed in version 3.2: Lock acquires can now be interrupted by signals on POSIX.

    Changed in version 3.14: Lock acquires can now be interrupted by signals on Windows.

lock.release()[¶](#thread.lock.release "Link to this definition")
:   Releases the lock. The lock must have been acquired earlier, but not
    necessarily by the same thread.

lock.locked()[¶](#thread.lock.locked "Link to this definition")
:   Return the status of the lock: `True` if it has been acquired by some thread,
    `False` if not.

In addition to these methods, lock objects can also be used via the
[`with`](../reference/compound_stmts.html#with) statement, e.g.:

```
import _thread

a_lock = _thread.allocate_lock()

with a_lock:
    print("a_lock is locked while this executes")
```

**Caveats:**

* Interrupts always go to the main thread (the [`KeyboardInterrupt`](exceptions.html#KeyboardInterrupt "KeyboardInterrupt")
  exception will be received by that thread.)
* Calling [`sys.exit()`](sys.html#sys.exit "sys.exit") or raising the [`SystemExit`](exceptions.html#SystemExit "SystemExit") exception is
  equivalent to calling [`_thread.exit()`](#thread.exit "_thread.exit").
* When the main thread exits, it is system defined whether the other threads
  survive. On most systems, they are killed without executing
  [`try`](../reference/compound_stmts.html#try) … [`finally`](../reference/compound_stmts.html#finally) clauses or executing object
  destructors.

#### Previous topic

[`contextvars` — Context Variables](contextvars.html "previous chapter")

#### Next topic

[Networking and Interprocess Communication](ipc.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/_thread.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](ipc.html "Networking and Interprocess Communication") |
* [previous](contextvars.html "contextvars — Context Variables") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Concurrent Execution](concurrency.html) »
* `_thread` — Low-level threading API
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
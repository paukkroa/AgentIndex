### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](subprocess.html "subprocess — Subprocess management") |
* [previous](concurrent.futures.html "concurrent.futures — Launching parallel tasks") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Concurrent Execution](concurrency.html) »
* `concurrent.interpreters` — Multiple interpreters in the same process
* |
* Theme
  Auto
  Light
  Dark
   |

# `concurrent.interpreters` — Multiple interpreters in the same process[¶](#module-concurrent.interpreters "Link to this heading")

Added in version 3.14.

**Source code:** [Lib/concurrent/interpreters](https://github.com/python/cpython/tree/3.14/Lib/concurrent/interpreters)

---

The `concurrent.interpreters` module constructs higher-level
interfaces on top of the lower level `_interpreters` module.

The module is primarily meant to provide a basic API for managing
interpreters (AKA “subinterpreters”) and running things in them.
Running mostly involves switching to an interpreter (in the current
thread) and calling a function in that execution context.

For concurrency, interpreters themselves (and this module) don’t
provide much more than isolation, which on its own isn’t useful.
Actual concurrency is available separately through
[`threads`](threading.html#module-threading "threading: Thread-based parallelism.") See [below](#interp-concurrency)

See also

[`InterpreterPoolExecutor`](concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor "concurrent.futures.InterpreterPoolExecutor")
:   Combines threads with interpreters in a familiar interface.

[Isolating Extension Modules](../howto/isolating-extensions.html#isolating-extensions-howto)
:   How to update an extension module to support multiple interpreters.

[**PEP 554**](https://peps.python.org/pep-0554/)

[**PEP 734**](https://peps.python.org/pep-0734/)

[**PEP 684**](https://peps.python.org/pep-0684/)

[Availability](intro.html#availability): not WASI.

This module does not work or is not available on WebAssembly. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

## Key details[¶](#key-details "Link to this heading")

Before we dive in further, there are a small number of details
to keep in mind about using multiple interpreters:

* [isolated](#interp-isolation), by default
* no implicit threads
* not all PyPI packages support use in multiple interpreters yet

## Introduction[¶](#introduction "Link to this heading")

An “interpreter” is effectively the execution context of the Python
runtime. It contains all of the state the runtime needs to execute
a program. This includes things like the import state and builtins.
(Each thread, even if there’s only the main thread, has some extra
runtime state, in addition to the current interpreter, related to
the current exception and the bytecode eval loop.)

The concept and functionality of the interpreter have been a part of
Python since version 2.2, but the feature was only available through
the C-API and not well known, and the [isolation](#interp-isolation)
was relatively incomplete until version 3.12.

### Multiple Interpreters and Isolation[¶](#multiple-interpreters-and-isolation "Link to this heading")

A Python implementation may support using multiple interpreters in the
same process. CPython has this support. Each interpreter is
effectively isolated from the others (with a limited number of
carefully managed process-global exceptions to the rule).

That isolation is primarily useful as a strong separation between
distinct logical components of a program, where you want to have
careful control of how those components interact.

Note

Interpreters in the same process can technically never be strictly
isolated from one another since there are few restrictions on memory
access within the same process. The Python runtime makes a best
effort at isolation but extension modules may easily violate that.
Therefore, do not use multiple interpreters in security-sensitive
situations, where they shouldn’t have access to each other’s data.

### Running in an Interpreter[¶](#running-in-an-interpreter "Link to this heading")

Running in a different interpreter involves switching to it in the
current thread and then calling some function. The runtime will
execute the function using the current interpreter’s state. The
`concurrent.interpreters` module provides a basic API for
creating and managing interpreters, as well as the switch-and-call
operation.

No other threads are automatically started for the operation.
There is [a helper](#interp-call-in-thread) for that though.
There is another dedicated helper for calling the builtin
[`exec()`](functions.html#exec "exec") in an interpreter.

When [`exec()`](functions.html#exec "exec") (or [`eval()`](functions.html#eval "eval")) are called in an interpreter,
they run using the interpreter’s `__main__` module as the
“globals” namespace. The same is true for functions that aren’t
associated with any module. This is the same as how scripts invoked
from the command-line run in the `__main__` module.

### Concurrency and Parallelism[¶](#concurrency-and-parallelism "Link to this heading")

As noted earlier, interpreters do not provide any concurrency
on their own. They strictly represent the isolated execution
context the runtime will use *in the current thread*. That isolation
makes them similar to processes, but they still enjoy in-process
efficiency, like threads.

All that said, interpreters do naturally support certain flavors of
concurrency.
There’s a powerful side effect of that isolation. It enables a
different approach to concurrency than you can take with async or
threads. It’s a similar concurrency model to CSP or the actor model,
a model which is relatively easy to reason about.

You can take advantage of that concurrency model in a single thread,
switching back and forth between interpreters, Stackless-style.
However, this model is more useful when you combine interpreters
with multiple threads. This mostly involves starting a new thread,
where you switch to another interpreter and run what you want there.

Each actual thread in Python, even if you’re only running in the main
thread, has its own *current* execution context. Multiple threads can
use the same interpreter or different ones.

At a high level, you can think of the combination of threads and
interpreters as threads with opt-in sharing.

As a significant bonus, interpreters are sufficiently isolated that
they do not share the [GIL](../glossary.html#term-GIL), which means combining threads with
multiple interpreters enables full multi-core parallelism.
(This has been the case since Python 3.12.)

### Communication Between Interpreters[¶](#communication-between-interpreters "Link to this heading")

In practice, multiple interpreters are useful only if we have a way
to communicate between them. This usually involves some form of
message passing, but can even mean sharing data in some carefully
managed way.

With this in mind, the `concurrent.interpreters` module provides
a [`queue.Queue`](queue.html#queue.Queue "queue.Queue") implementation, available through
[`create_queue()`](#concurrent.interpreters.create_queue "concurrent.interpreters.create_queue").

### “Sharing” Objects[¶](#sharing-objects "Link to this heading")

Any data actually shared between interpreters loses the thread-safety
provided by the [GIL](../glossary.html#term-GIL). There are various options for dealing with
this in extension modules. However, from Python code the lack of
thread-safety means objects can’t actually be shared, with a few
exceptions. Instead, a copy must be created, which means mutable
objects won’t stay in sync.

By default, most objects are copied with [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") when they are
passed to another interpreter. Nearly all of the immutable builtin
objects are either directly shared or copied efficiently. For example:

* [`None`](constants.html#None "None")
* [`bool`](functions.html#bool "bool") ([`True`](constants.html#True "True") and [`False`](constants.html#False "False"))
* [`bytes`](stdtypes.html#bytes "bytes")
* [`str`](stdtypes.html#str "str")
* [`int`](functions.html#int "int")
* [`float`](functions.html#float "float")
* [`tuple`](stdtypes.html#tuple "tuple") (of similarly supported objects)

There is a small number of Python types that actually share mutable
data between interpreters:

* [`memoryview`](stdtypes.html#memoryview "memoryview")
* [`Queue`](#concurrent.interpreters.Queue "concurrent.interpreters.Queue")

## Reference[¶](#reference "Link to this heading")

This module defines the following functions:

concurrent.interpreters.list\_all()[¶](#concurrent.interpreters.list_all "Link to this definition")
:   Return a [`list`](stdtypes.html#list "list") of [`Interpreter`](#concurrent.interpreters.Interpreter "concurrent.interpreters.Interpreter") objects,
    one for each existing interpreter.

concurrent.interpreters.get\_current()[¶](#concurrent.interpreters.get_current "Link to this definition")
:   Return an [`Interpreter`](#concurrent.interpreters.Interpreter "concurrent.interpreters.Interpreter") object for the currently running
    interpreter.

concurrent.interpreters.get\_main()[¶](#concurrent.interpreters.get_main "Link to this definition")
:   Return an [`Interpreter`](#concurrent.interpreters.Interpreter "concurrent.interpreters.Interpreter") object for the main interpreter.
    This is the interpreter the runtime created to run the [REPL](../glossary.html#term-REPL)
    or the script given at the command-line. It is usually the only one.

concurrent.interpreters.create()[¶](#concurrent.interpreters.create "Link to this definition")
:   Initialize a new (idle) Python interpreter
    and return a [`Interpreter`](#concurrent.interpreters.Interpreter "concurrent.interpreters.Interpreter") object for it.

concurrent.interpreters.create\_queue()[¶](#concurrent.interpreters.create_queue "Link to this definition")
:   Initialize a new cross-interpreter queue and return a [`Queue`](#concurrent.interpreters.Queue "concurrent.interpreters.Queue")
    object for it.

### Interpreter objects[¶](#interpreter-objects "Link to this heading")

*class* concurrent.interpreters.Interpreter(*id*)[¶](#concurrent.interpreters.Interpreter "Link to this definition")
:   A single interpreter in the current process.

    Generally, [`Interpreter`](#concurrent.interpreters.Interpreter "concurrent.interpreters.Interpreter") shouldn’t be called directly.
    Instead, use [`create()`](#concurrent.interpreters.create "concurrent.interpreters.create") or one of the other module functions.

    id[¶](#concurrent.interpreters.Interpreter.id "Link to this definition")
    :   (read-only)

        The underlying interpreter’s ID.

    whence[¶](#concurrent.interpreters.Interpreter.whence "Link to this definition")
    :   (read-only)

        A string describing where the interpreter came from.

    is\_running()[¶](#concurrent.interpreters.Interpreter.is_running "Link to this definition")
    :   Return `True` if the interpreter is currently executing code
        in its `__main__` module and `False` otherwise.

    close()[¶](#concurrent.interpreters.Interpreter.close "Link to this definition")
    :   Finalize and destroy the interpreter.

    prepare\_main(*ns=None*, *\*\*kwargs*)[¶](#concurrent.interpreters.Interpreter.prepare_main "Link to this definition")
    :   Bind objects in the interpreter’s `__main__` module.

        Some objects are actually shared and some are copied efficiently,
        but most are copied via [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back."). See [“Sharing” Objects](#interp-object-sharing).

    exec(*code*, */*, *dedent=True*)[¶](#concurrent.interpreters.Interpreter.exec "Link to this definition")
    :   Run the given source code in the interpreter (in the current thread).

    call(*callable*, */*, *\*args*, *\*\*kwargs*)[¶](#concurrent.interpreters.Interpreter.call "Link to this definition")
    :   Return the result of calling running the given function in the
        interpreter (in the current thread).

    call\_in\_thread(*callable*, */*, *\*args*, *\*\*kwargs*)[¶](#concurrent.interpreters.Interpreter.call_in_thread "Link to this definition")
    :   Run the given function in the interpreter (in a new thread).

### Exceptions[¶](#exceptions "Link to this heading")

*exception* concurrent.interpreters.InterpreterError[¶](#concurrent.interpreters.InterpreterError "Link to this definition")
:   This exception, a subclass of [`Exception`](exceptions.html#Exception "Exception"), is raised when
    an interpreter-related error happens.

*exception* concurrent.interpreters.InterpreterNotFoundError[¶](#concurrent.interpreters.InterpreterNotFoundError "Link to this definition")
:   This exception, a subclass of [`InterpreterError`](#concurrent.interpreters.InterpreterError "concurrent.interpreters.InterpreterError"), is raised when
    the targeted interpreter no longer exists.

*exception* concurrent.interpreters.ExecutionFailed[¶](#concurrent.interpreters.ExecutionFailed "Link to this definition")
:   This exception, a subclass of [`InterpreterError`](#concurrent.interpreters.InterpreterError "concurrent.interpreters.InterpreterError"), is raised when
    the running code raised an uncaught exception.

    excinfo[¶](#concurrent.interpreters.ExecutionFailed.excinfo "Link to this definition")
    :   A basic snapshot of the exception raised in the other interpreter.

*exception* concurrent.interpreters.NotShareableError[¶](#concurrent.interpreters.NotShareableError "Link to this definition")
:   This exception, a subclass of [`TypeError`](exceptions.html#TypeError "TypeError"), is raised when
    an object cannot be sent to another interpreter.

### Communicating Between Interpreters[¶](#communicating-between-interpreters "Link to this heading")

*class* concurrent.interpreters.Queue(*id*)[¶](#concurrent.interpreters.Queue "Link to this definition")
:   A wrapper around a low-level, cross-interpreter queue, which
    implements the [`queue.Queue`](queue.html#queue.Queue "queue.Queue") interface. The underlying queue
    can only be created through [`create_queue()`](#concurrent.interpreters.create_queue "concurrent.interpreters.create_queue").

    Some objects are actually shared and some are copied efficiently,
    but most are copied via [`pickle`](pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back."). See [“Sharing” Objects](#interp-object-sharing).

    id[¶](#concurrent.interpreters.Queue.id "Link to this definition")
    :   (read-only)

        The queue’s ID.

*exception* concurrent.interpreters.QueueEmptyError[¶](#concurrent.interpreters.QueueEmptyError "Link to this definition")
:   This exception, a subclass of [`queue.Empty`](queue.html#queue.Empty "queue.Empty"), is raised from
    `Queue.get()` and `Queue.get_nowait()` when the queue
    is empty.

*exception* concurrent.interpreters.QueueFullError[¶](#concurrent.interpreters.QueueFullError "Link to this definition")
:   This exception, a subclass of [`queue.Full`](queue.html#queue.Full "queue.Full"), is raised from
    `Queue.put()` and `Queue.put_nowait()` when the queue
    is full.

## Basic usage[¶](#basic-usage "Link to this heading")

Creating an interpreter and running code in it:

```
from concurrent import interpreters

interp = interpreters.create()

# Run in the current OS thread.

interp.exec('print("spam!")')

interp.exec("""if True:
    print('spam!')
    """)

from textwrap import dedent
interp.exec(dedent("""
    print('spam!')
    """))

def run(arg):
    return arg

res = interp.call(run, 'spam!')
print(res)

def run():
    print('spam!')

interp.call(run)

# Run in new OS thread.

t = interp.call_in_thread(run)
t.join()
```

### [Table of Contents](../contents.html)

* [`concurrent.interpreters` — Multiple interpreters in the same process](#)
  + [Key details](#key-details)
  + [Introduction](#introduction)
    - [Multiple Interpreters and Isolation](#multiple-interpreters-and-isolation)
    - [Running in an Interpreter](#running-in-an-interpreter)
    - [Concurrency and Parallelism](#concurrency-and-parallelism)
    - [Communication Between Interpreters](#communication-between-interpreters)
    - [“Sharing” Objects](#sharing-objects)
  + [Reference](#reference)
    - [Interpreter objects](#interpreter-objects)
    - [Exceptions](#exceptions)
    - [Communicating Between Interpreters](#communicating-between-interpreters)
  + [Basic usage](#basic-usage)

#### Previous topic

[`concurrent.futures` — Launching parallel tasks](concurrent.futures.html "previous chapter")

#### Next topic

[`subprocess` — Subprocess management](subprocess.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/concurrent.interpreters.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](subprocess.html "subprocess — Subprocess management") |
* [previous](concurrent.futures.html "concurrent.futures — Launching parallel tasks") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Concurrent Execution](concurrency.html) »
* `concurrent.interpreters` — Multiple interpreters in the same process
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
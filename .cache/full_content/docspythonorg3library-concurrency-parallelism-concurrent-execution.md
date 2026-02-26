### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](threading.html "threading — Thread-based parallelism") |
* [previous](cmd.html "cmd — Support for line-oriented command interpreters") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Concurrent Execution
* |
* Theme
  Auto
  Light
  Dark
   |

# Concurrent Execution[¶](#concurrent-execution "Link to this heading")

The modules described in this chapter provide support for concurrent
execution of code. The appropriate choice of tool will depend on the
task to be executed (CPU bound vs IO bound) and preferred style of
development (event driven cooperative multitasking vs preemptive
multitasking). Here’s an overview:

* [`threading` — Thread-based parallelism](threading.html)
  + [Introduction](threading.html#introduction)
  + [GIL and performance considerations](threading.html#gil-and-performance-considerations)
  + [Reference](threading.html#reference)
    - [Thread-local data](threading.html#thread-local-data)
    - [Thread objects](threading.html#thread-objects)
    - [Lock objects](threading.html#lock-objects)
    - [RLock objects](threading.html#rlock-objects)
    - [Condition objects](threading.html#condition-objects)
    - [Semaphore objects](threading.html#semaphore-objects)
    - [`Semaphore` example](threading.html#semaphore-example)
    - [Event objects](threading.html#event-objects)
    - [Timer objects](threading.html#timer-objects)
    - [Barrier objects](threading.html#barrier-objects)
  + [Using locks, conditions, and semaphores in the `with` statement](threading.html#using-locks-conditions-and-semaphores-in-the-with-statement)
* [`multiprocessing` — Process-based parallelism](multiprocessing.html)
  + [Introduction](multiprocessing.html#introduction)
    - [The `Process` class](multiprocessing.html#the-process-class)
    - [Contexts and start methods](multiprocessing.html#contexts-and-start-methods)
    - [Exchanging objects between processes](multiprocessing.html#exchanging-objects-between-processes)
    - [Synchronization between processes](multiprocessing.html#synchronization-between-processes)
    - [Sharing state between processes](multiprocessing.html#sharing-state-between-processes)
    - [Using a pool of workers](multiprocessing.html#using-a-pool-of-workers)
  + [Reference](multiprocessing.html#reference)
    - [Global start method](multiprocessing.html#global-start-method)
    - [`Process` and exceptions](multiprocessing.html#process-and-exceptions)
    - [Pipes and Queues](multiprocessing.html#pipes-and-queues)
    - [Miscellaneous](multiprocessing.html#miscellaneous)
    - [Connection Objects](multiprocessing.html#connection-objects)
    - [Synchronization primitives](multiprocessing.html#synchronization-primitives)
    - [Shared `ctypes` Objects](multiprocessing.html#shared-ctypes-objects)
      * [The `multiprocessing.sharedctypes` module](multiprocessing.html#module-multiprocessing.sharedctypes)
    - [Managers](multiprocessing.html#managers)
      * [Customized managers](multiprocessing.html#customized-managers)
      * [Using a remote manager](multiprocessing.html#using-a-remote-manager)
    - [Proxy Objects](multiprocessing.html#proxy-objects)
      * [Cleanup](multiprocessing.html#cleanup)
    - [Process Pools](multiprocessing.html#module-multiprocessing.pool)
    - [Listeners and Clients](multiprocessing.html#module-multiprocessing.connection)
      * [Address Formats](multiprocessing.html#address-formats)
    - [Authentication keys](multiprocessing.html#authentication-keys)
    - [Logging](multiprocessing.html#logging)
    - [The `multiprocessing.dummy` module](multiprocessing.html#module-multiprocessing.dummy)
  + [Programming guidelines](multiprocessing.html#programming-guidelines)
    - [All start methods](multiprocessing.html#all-start-methods)
    - [The *spawn* and *forkserver* start methods](multiprocessing.html#the-spawn-and-forkserver-start-methods)
  + [Examples](multiprocessing.html#examples)
* [`multiprocessing.shared_memory` — Shared memory for direct access across processes](multiprocessing.shared_memory.html)
* [The `concurrent` package](concurrent.html)
* [`concurrent.futures` — Launching parallel tasks](concurrent.futures.html)
  + [Executor Objects](concurrent.futures.html#executor-objects)
  + [ThreadPoolExecutor](concurrent.futures.html#threadpoolexecutor)
    - [ThreadPoolExecutor Example](concurrent.futures.html#threadpoolexecutor-example)
  + [InterpreterPoolExecutor](concurrent.futures.html#interpreterpoolexecutor)
  + [ProcessPoolExecutor](concurrent.futures.html#processpoolexecutor)
    - [ProcessPoolExecutor Example](concurrent.futures.html#processpoolexecutor-example)
  + [Future Objects](concurrent.futures.html#future-objects)
  + [Module Functions](concurrent.futures.html#module-functions)
  + [Exception classes](concurrent.futures.html#exception-classes)
* [`concurrent.interpreters` — Multiple interpreters in the same process](concurrent.interpreters.html)
  + [Key details](concurrent.interpreters.html#key-details)
  + [Introduction](concurrent.interpreters.html#introduction)
    - [Multiple Interpreters and Isolation](concurrent.interpreters.html#multiple-interpreters-and-isolation)
    - [Running in an Interpreter](concurrent.interpreters.html#running-in-an-interpreter)
    - [Concurrency and Parallelism](concurrent.interpreters.html#concurrency-and-parallelism)
    - [Communication Between Interpreters](concurrent.interpreters.html#communication-between-interpreters)
    - [“Sharing” Objects](concurrent.interpreters.html#sharing-objects)
  + [Reference](concurrent.interpreters.html#reference)
    - [Interpreter objects](concurrent.interpreters.html#interpreter-objects)
    - [Exceptions](concurrent.interpreters.html#exceptions)
    - [Communicating Between Interpreters](concurrent.interpreters.html#communicating-between-interpreters)
  + [Basic usage](concurrent.interpreters.html#basic-usage)
* [`subprocess` — Subprocess management](subprocess.html)
  + [Using the `subprocess` Module](subprocess.html#using-the-subprocess-module)
    - [Frequently Used Arguments](subprocess.html#frequently-used-arguments)
    - [Popen Constructor](subprocess.html#popen-constructor)
    - [Exceptions](subprocess.html#exceptions)
  + [Security Considerations](subprocess.html#security-considerations)
  + [Popen Objects](subprocess.html#popen-objects)
  + [Windows Popen Helpers](subprocess.html#windows-popen-helpers)
    - [Windows Constants](subprocess.html#windows-constants)
  + [Older high-level API](subprocess.html#older-high-level-api)
  + [Replacing Older Functions with the `subprocess` Module](subprocess.html#replacing-older-functions-with-the-subprocess-module)
    - [Replacing **/bin/sh** shell command substitution](subprocess.html#replacing-bin-sh-shell-command-substitution)
    - [Replacing shell pipeline](subprocess.html#replacing-shell-pipeline)
    - [Replacing `os.system()`](subprocess.html#replacing-os-system)
    - [Replacing the `os.spawn` family](subprocess.html#replacing-the-os-spawn-family)
    - [Replacing `os.popen()`](subprocess.html#replacing-os-popen)
  + [Legacy Shell Invocation Functions](subprocess.html#legacy-shell-invocation-functions)
  + [Notes](subprocess.html#notes)
    - [Timeout Behavior](subprocess.html#timeout-behavior)
    - [Converting an argument sequence to a string on Windows](subprocess.html#converting-an-argument-sequence-to-a-string-on-windows)
    - [Disable use of `posix_spawn()`](subprocess.html#disable-use-of-posix-spawn)
* [`sched` — Event scheduler](sched.html)
  + [Scheduler Objects](sched.html#scheduler-objects)
* [`queue` — A synchronized queue class](queue.html)
  + [Queue Objects](queue.html#queue-objects)
    - [Waiting for task completion](queue.html#waiting-for-task-completion)
    - [Terminating queues](queue.html#terminating-queues)
  + [SimpleQueue Objects](queue.html#simplequeue-objects)
* [`contextvars` — Context Variables](contextvars.html)
  + [Context Variables](contextvars.html#context-variables)
  + [Manual Context Management](contextvars.html#manual-context-management)
  + [asyncio support](contextvars.html#asyncio-support)

The following are support modules for some of the above services:

* [`_thread` — Low-level threading API](_thread.html)

#### Previous topic

[`cmd` — Support for line-oriented command interpreters](cmd.html "previous chapter")

#### Next topic

[`threading` — Thread-based parallelism](threading.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/concurrency.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](threading.html "threading — Thread-based parallelism") |
* [previous](cmd.html "cmd — Support for line-oriented command interpreters") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* Concurrent Execution
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
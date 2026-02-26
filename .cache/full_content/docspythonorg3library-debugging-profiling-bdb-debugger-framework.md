### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](faulthandler.html "faulthandler — Dump the Python traceback") |
* [previous](audit_events.html "Audit events table") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Debugging and Profiling](debug.html) »
* `bdb` — Debugger framework
* |
* Theme
  Auto
  Light
  Dark
   |

# `bdb` — Debugger framework[¶](#module-bdb "Link to this heading")

**Source code:** [Lib/bdb.py](https://github.com/python/cpython/tree/3.14/Lib/bdb.py)

---

The `bdb` module handles basic debugger functions, like setting breakpoints
or managing execution via the debugger.

The following exception is defined:

*exception* bdb.BdbQuit[¶](#bdb.BdbQuit "Link to this definition")
:   Exception raised by the [`Bdb`](#bdb.Bdb "bdb.Bdb") class for quitting the debugger.

The `bdb` module also defines two classes:

*class* bdb.Breakpoint(*self*, *file*, *line*, *temporary=False*, *cond=None*, *funcname=None*)[¶](#bdb.Breakpoint "Link to this definition")
:   This class implements temporary breakpoints, ignore counts, disabling and
    (re-)enabling, and conditionals.

    Breakpoints are indexed by number through a list called [`bpbynumber`](#bdb.Breakpoint.bpbynumber "bdb.Breakpoint.bpbynumber")
    and by `(file, line)` pairs through [`bplist`](#bdb.Breakpoint.bplist "bdb.Breakpoint.bplist"). The former points to
    a single instance of class [`Breakpoint`](#bdb.Breakpoint "bdb.Breakpoint"). The latter points to a list
    of such instances since there may be more than one breakpoint per line.

    When creating a breakpoint, its associated [`file name`](#bdb.Breakpoint.file "bdb.Breakpoint.file") should
    be in canonical form. If a [`funcname`](#bdb.Breakpoint.funcname "bdb.Breakpoint.funcname") is defined, a breakpoint
    [`hit`](#bdb.Breakpoint.hits "bdb.Breakpoint.hits") will be counted when the first line of that function is
    executed. A [`conditional`](#bdb.Breakpoint.cond "bdb.Breakpoint.cond") breakpoint always counts a
    [`hit`](#bdb.Breakpoint.hits "bdb.Breakpoint.hits").

    [`Breakpoint`](#bdb.Breakpoint "bdb.Breakpoint") instances have the following methods:

    deleteMe()[¶](#bdb.Breakpoint.deleteMe "Link to this definition")
    :   Delete the breakpoint from the list associated to a file/line. If it is
        the last breakpoint in that position, it also deletes the entry for the
        file/line.

    enable()[¶](#bdb.Breakpoint.enable "Link to this definition")
    :   Mark the breakpoint as enabled.

    disable()[¶](#bdb.Breakpoint.disable "Link to this definition")
    :   Mark the breakpoint as disabled.

    bpformat()[¶](#bdb.Breakpoint.bpformat "Link to this definition")
    :   Return a string with all the information about the breakpoint, nicely
        formatted:

        * Breakpoint number.
        * Temporary status (del or keep).
        * File/line position.
        * Break condition.
        * Number of times to ignore.
        * Number of times hit.

        Added in version 3.2.

    bpprint(*out=None*)[¶](#bdb.Breakpoint.bpprint "Link to this definition")
    :   Print the output of [`bpformat()`](#bdb.Breakpoint.bpformat "bdb.Breakpoint.bpformat") to the file *out*, or if it is
        `None`, to standard output.

    [`Breakpoint`](#bdb.Breakpoint "bdb.Breakpoint") instances have the following attributes:

    file[¶](#bdb.Breakpoint.file "Link to this definition")
    :   File name of the [`Breakpoint`](#bdb.Breakpoint "bdb.Breakpoint").

    line[¶](#bdb.Breakpoint.line "Link to this definition")
    :   Line number of the [`Breakpoint`](#bdb.Breakpoint "bdb.Breakpoint") within [`file`](#bdb.Breakpoint.file "bdb.Breakpoint.file").

    temporary[¶](#bdb.Breakpoint.temporary "Link to this definition")
    :   `True` if a [`Breakpoint`](#bdb.Breakpoint "bdb.Breakpoint") at (file, line) is temporary.

    cond[¶](#bdb.Breakpoint.cond "Link to this definition")
    :   Condition for evaluating a [`Breakpoint`](#bdb.Breakpoint "bdb.Breakpoint") at (file, line).

    funcname[¶](#bdb.Breakpoint.funcname "Link to this definition")
    :   Function name that defines whether a [`Breakpoint`](#bdb.Breakpoint "bdb.Breakpoint") is hit upon
        entering the function.

    enabled[¶](#bdb.Breakpoint.enabled "Link to this definition")
    :   `True` if [`Breakpoint`](#bdb.Breakpoint "bdb.Breakpoint") is enabled.

    bpbynumber[¶](#bdb.Breakpoint.bpbynumber "Link to this definition")
    :   Numeric index for a single instance of a [`Breakpoint`](#bdb.Breakpoint "bdb.Breakpoint").

    bplist[¶](#bdb.Breakpoint.bplist "Link to this definition")
    :   Dictionary of [`Breakpoint`](#bdb.Breakpoint "bdb.Breakpoint") instances indexed by
        ([`file`](#bdb.Breakpoint.file "bdb.Breakpoint.file"), [`line`](#bdb.Breakpoint.line "bdb.Breakpoint.line")) tuples.

    ignore[¶](#bdb.Breakpoint.ignore "Link to this definition")
    :   Number of times to ignore a [`Breakpoint`](#bdb.Breakpoint "bdb.Breakpoint").

    hits[¶](#bdb.Breakpoint.hits "Link to this definition")
    :   Count of the number of times a [`Breakpoint`](#bdb.Breakpoint "bdb.Breakpoint") has been hit.

*class* bdb.Bdb(*skip=None*, *backend='settrace'*)[¶](#bdb.Bdb "Link to this definition")
:   The [`Bdb`](#bdb.Bdb "bdb.Bdb") class acts as a generic Python debugger base class.

    This class takes care of the details of the trace facility; a derived class
    should implement user interaction. The standard debugger class
    ([`pdb.Pdb`](pdb.html#pdb.Pdb "pdb.Pdb")) is an example.

    The *skip* argument, if given, must be an iterable of glob-style
    module name patterns. The debugger will not step into frames that
    originate in a module that matches one of these patterns. Whether a
    frame is considered to originate in a certain module is determined
    by the `__name__` in the frame globals.

    The *backend* argument specifies the backend to use for [`Bdb`](#bdb.Bdb "bdb.Bdb"). It
    can be either `'settrace'` or `'monitoring'`. `'settrace'` uses
    [`sys.settrace()`](sys.html#sys.settrace "sys.settrace") which has the best backward compatibility. The
    `'monitoring'` backend uses the new [`sys.monitoring`](sys.monitoring.html#module-sys.monitoring "sys.monitoring: Access and control event monitoring") that was
    introduced in Python 3.12, which can be much more efficient because it
    can disable unused events. We are trying to keep the exact interfaces
    for both backends, but there are some differences. The debugger developers
    are encouraged to use the `'monitoring'` backend to achieve better
    performance.

    Changed in version 3.1: Added the *skip* parameter.

    Changed in version 3.14: Added the *backend* parameter.

    The following methods of [`Bdb`](#bdb.Bdb "bdb.Bdb") normally don’t need to be overridden.

    canonic(*filename*)[¶](#bdb.Bdb.canonic "Link to this definition")
    :   Return canonical form of *filename*.

        For real file names, the canonical form is an operating-system-dependent,
        [`case-normalized`](os.path.html#os.path.normcase "os.path.normcase") [`absolute path`](os.path.html#os.path.abspath "os.path.abspath"). A *filename* with angle brackets, such as `"<stdin>"`
        generated in interactive mode, is returned unchanged.

    start\_trace(*self*)[¶](#bdb.Bdb.start_trace "Link to this definition")
    :   Start tracing. For `'settrace'` backend, this method is equivalent to
        `sys.settrace(self.trace_dispatch)`

        Added in version 3.14.

    stop\_trace(*self*)[¶](#bdb.Bdb.stop_trace "Link to this definition")
    :   Stop tracing. For `'settrace'` backend, this method is equivalent to
        `sys.settrace(None)`

        Added in version 3.14.

    reset()[¶](#bdb.Bdb.reset "Link to this definition")
    :   Set the `botframe`, `stopframe`, `returnframe` and
        [`quitting`](#bdb.Bdb.set_quit "bdb.Bdb.set_quit") attributes with values ready to start debugging.

    trace\_dispatch(*frame*, *event*, *arg*)[¶](#bdb.Bdb.trace_dispatch "Link to this definition")
    :   This function is installed as the trace function of debugged frames. Its
        return value is the new trace function (in most cases, that is, itself).

        The default implementation decides how to dispatch a frame, depending on
        the type of event (passed as a string) that is about to be executed.
        *event* can be one of the following:

        * `"line"`: A new line of code is going to be executed.
        * `"call"`: A function is about to be called, or another code block
          entered.
        * `"return"`: A function or other code block is about to return.
        * `"exception"`: An exception has occurred.
        * `"c_call"`: A C function is about to be called.
        * `"c_return"`: A C function has returned.
        * `"c_exception"`: A C function has raised an exception.

        For the Python events, specialized functions (see below) are called. For
        the C events, no action is taken.

        The *arg* parameter depends on the previous event.

        See the documentation for [`sys.settrace()`](sys.html#sys.settrace "sys.settrace") for more information on the
        trace function. For more information on code and frame objects, refer to
        [The standard type hierarchy](../reference/datamodel.html#types).

    dispatch\_line(*frame*)[¶](#bdb.Bdb.dispatch_line "Link to this definition")
    :   If the debugger should stop on the current line, invoke the
        [`user_line()`](#bdb.Bdb.user_line "bdb.Bdb.user_line") method (which should be overridden in subclasses).
        Raise a [`BdbQuit`](#bdb.BdbQuit "bdb.BdbQuit") exception if the [`quitting`](#bdb.Bdb.set_quit "bdb.Bdb.set_quit") flag is set
        (which can be set from [`user_line()`](#bdb.Bdb.user_line "bdb.Bdb.user_line")). Return a reference to the
        [`trace_dispatch()`](#bdb.Bdb.trace_dispatch "bdb.Bdb.trace_dispatch") method for further tracing in that scope.

    dispatch\_call(*frame*, *arg*)[¶](#bdb.Bdb.dispatch_call "Link to this definition")
    :   If the debugger should stop on this function call, invoke the
        [`user_call()`](#bdb.Bdb.user_call "bdb.Bdb.user_call") method (which should be overridden in subclasses).
        Raise a [`BdbQuit`](#bdb.BdbQuit "bdb.BdbQuit") exception if the [`quitting`](#bdb.Bdb.set_quit "bdb.Bdb.set_quit") flag is set
        (which can be set from [`user_call()`](#bdb.Bdb.user_call "bdb.Bdb.user_call")). Return a reference to the
        [`trace_dispatch()`](#bdb.Bdb.trace_dispatch "bdb.Bdb.trace_dispatch") method for further tracing in that scope.

    dispatch\_return(*frame*, *arg*)[¶](#bdb.Bdb.dispatch_return "Link to this definition")
    :   If the debugger should stop on this function return, invoke the
        [`user_return()`](#bdb.Bdb.user_return "bdb.Bdb.user_return") method (which should be overridden in subclasses).
        Raise a [`BdbQuit`](#bdb.BdbQuit "bdb.BdbQuit") exception if the [`quitting`](#bdb.Bdb.set_quit "bdb.Bdb.set_quit") flag is set
        (which can be set from [`user_return()`](#bdb.Bdb.user_return "bdb.Bdb.user_return")). Return a reference to the
        [`trace_dispatch()`](#bdb.Bdb.trace_dispatch "bdb.Bdb.trace_dispatch") method for further tracing in that scope.

    dispatch\_exception(*frame*, *arg*)[¶](#bdb.Bdb.dispatch_exception "Link to this definition")
    :   If the debugger should stop at this exception, invokes the
        [`user_exception()`](#bdb.Bdb.user_exception "bdb.Bdb.user_exception") method (which should be overridden in subclasses).
        Raise a [`BdbQuit`](#bdb.BdbQuit "bdb.BdbQuit") exception if the [`quitting`](#bdb.Bdb.set_quit "bdb.Bdb.set_quit") flag is set
        (which can be set from [`user_exception()`](#bdb.Bdb.user_exception "bdb.Bdb.user_exception")). Return a reference to the
        [`trace_dispatch()`](#bdb.Bdb.trace_dispatch "bdb.Bdb.trace_dispatch") method for further tracing in that scope.

    Normally derived classes don’t override the following methods, but they may
    if they want to redefine the definition of stopping and breakpoints.

    is\_skipped\_module(*module\_name*)[¶](#bdb.Bdb.is_skipped_module "Link to this definition")
    :   Return `True` if *module\_name* matches any skip pattern.

    stop\_here(*frame*)[¶](#bdb.Bdb.stop_here "Link to this definition")
    :   Return `True` if *frame* is below the starting frame in the stack.

    break\_here(*frame*)[¶](#bdb.Bdb.break_here "Link to this definition")
    :   Return `True` if there is an effective breakpoint for this line.

        Check whether a line or function breakpoint exists and is in effect. Delete temporary
        breakpoints based on information from [`effective()`](#bdb.effective "bdb.effective").

    break\_anywhere(*frame*)[¶](#bdb.Bdb.break_anywhere "Link to this definition")
    :   Return `True` if any breakpoint exists for *frame*’s filename.

    Derived classes should override these methods to gain control over debugger
    operation.

    user\_call(*frame*, *argument\_list*)[¶](#bdb.Bdb.user_call "Link to this definition")
    :   Called from [`dispatch_call()`](#bdb.Bdb.dispatch_call "bdb.Bdb.dispatch_call") if a break might stop inside the
        called function.

        *argument\_list* is not used anymore and will always be `None`.
        The argument is kept for backwards compatibility.

    user\_line(*frame*)[¶](#bdb.Bdb.user_line "Link to this definition")
    :   Called from [`dispatch_line()`](#bdb.Bdb.dispatch_line "bdb.Bdb.dispatch_line") when either [`stop_here()`](#bdb.Bdb.stop_here "bdb.Bdb.stop_here") or
        [`break_here()`](#bdb.Bdb.break_here "bdb.Bdb.break_here") returns `True`.

    user\_return(*frame*, *return\_value*)[¶](#bdb.Bdb.user_return "Link to this definition")
    :   Called from [`dispatch_return()`](#bdb.Bdb.dispatch_return "bdb.Bdb.dispatch_return") when [`stop_here()`](#bdb.Bdb.stop_here "bdb.Bdb.stop_here") returns `True`.

    user\_exception(*frame*, *exc\_info*)[¶](#bdb.Bdb.user_exception "Link to this definition")
    :   Called from [`dispatch_exception()`](#bdb.Bdb.dispatch_exception "bdb.Bdb.dispatch_exception") when [`stop_here()`](#bdb.Bdb.stop_here "bdb.Bdb.stop_here")
        returns `True`.

    do\_clear(*arg*)[¶](#bdb.Bdb.do_clear "Link to this definition")
    :   Handle how a breakpoint must be removed when it is a temporary one.

        This method must be implemented by derived classes.

    Derived classes and clients can call the following methods to affect the
    stepping state.

    set\_step()[¶](#bdb.Bdb.set_step "Link to this definition")
    :   Stop after one line of code.

    set\_next(*frame*)[¶](#bdb.Bdb.set_next "Link to this definition")
    :   Stop on the next line in or below the given frame.

    set\_return(*frame*)[¶](#bdb.Bdb.set_return "Link to this definition")
    :   Stop when returning from the given frame.

    set\_until(*frame*, *lineno=None*)[¶](#bdb.Bdb.set_until "Link to this definition")
    :   Stop when the line with the *lineno* greater than the current one is
        reached or when returning from current frame.

    set\_trace([*frame*])[¶](#bdb.Bdb.set_trace "Link to this definition")
    :   Start debugging from *frame*. If *frame* is not specified, debugging
        starts from caller’s frame.

        Changed in version 3.13: [`set_trace()`](#bdb.set_trace "bdb.set_trace") will enter the debugger immediately, rather than
        on the next line of code to be executed.

    set\_continue()[¶](#bdb.Bdb.set_continue "Link to this definition")
    :   Stop only at breakpoints or when finished. If there are no breakpoints,
        set the system trace function to `None`.

    set\_quit()[¶](#bdb.Bdb.set_quit "Link to this definition")
    :   Set the `quitting` attribute to `True`. This raises [`BdbQuit`](#bdb.BdbQuit "bdb.BdbQuit") in
        the next call to one of the `dispatch_*()` methods.

    Derived classes and clients can call the following methods to manipulate
    breakpoints. These methods return a string containing an error message if
    something went wrong, or `None` if all is well.

    set\_break(*filename*, *lineno*, *temporary=False*, *cond=None*, *funcname=None*)[¶](#bdb.Bdb.set_break "Link to this definition")
    :   Set a new breakpoint. If the *lineno* line doesn’t exist for the
        *filename* passed as argument, return an error message. The *filename*
        should be in canonical form, as described in the [`canonic()`](#bdb.Bdb.canonic "bdb.Bdb.canonic") method.

    clear\_break(*filename*, *lineno*)[¶](#bdb.Bdb.clear_break "Link to this definition")
    :   Delete the breakpoints in *filename* and *lineno*. If none were set,
        return an error message.

    clear\_bpbynumber(*arg*)[¶](#bdb.Bdb.clear_bpbynumber "Link to this definition")
    :   Delete the breakpoint which has the index *arg* in the
        [`Breakpoint.bpbynumber`](#bdb.Breakpoint.bpbynumber "bdb.Breakpoint.bpbynumber"). If *arg* is not numeric or out of range,
        return an error message.

    clear\_all\_file\_breaks(*filename*)[¶](#bdb.Bdb.clear_all_file_breaks "Link to this definition")
    :   Delete all breakpoints in *filename*. If none were set, return an error
        message.

    clear\_all\_breaks()[¶](#bdb.Bdb.clear_all_breaks "Link to this definition")
    :   Delete all existing breakpoints. If none were set, return an error
        message.

    get\_bpbynumber(*arg*)[¶](#bdb.Bdb.get_bpbynumber "Link to this definition")
    :   Return a breakpoint specified by the given number. If *arg* is a string,
        it will be converted to a number. If *arg* is a non-numeric string, if
        the given breakpoint never existed or has been deleted, a
        [`ValueError`](exceptions.html#ValueError "ValueError") is raised.

        Added in version 3.2.

    get\_break(*filename*, *lineno*)[¶](#bdb.Bdb.get_break "Link to this definition")
    :   Return `True` if there is a breakpoint for *lineno* in *filename*.

    get\_breaks(*filename*, *lineno*)[¶](#bdb.Bdb.get_breaks "Link to this definition")
    :   Return all breakpoints for *lineno* in *filename*, or an empty list if
        none are set.

    get\_file\_breaks(*filename*)[¶](#bdb.Bdb.get_file_breaks "Link to this definition")
    :   Return all breakpoints in *filename*, or an empty list if none are set.

    get\_all\_breaks()[¶](#bdb.Bdb.get_all_breaks "Link to this definition")
    :   Return all breakpoints that are set.

    Derived classes and clients can call the following methods to disable and
    restart events to achieve better performance. These methods only work
    when using the `'monitoring'` backend.

    disable\_current\_event()[¶](#bdb.Bdb.disable_current_event "Link to this definition")
    :   Disable the current event until the next time [`restart_events()`](#bdb.Bdb.restart_events "bdb.Bdb.restart_events") is
        called. This is helpful when the debugger is not interested in the current
        line.

        Added in version 3.14.

    restart\_events()[¶](#bdb.Bdb.restart_events "Link to this definition")
    :   Restart all the disabled events. This function is automatically called in
        `dispatch_*` methods after `user_*` methods are called. If the
        `dispatch_*` methods are not overridden, the disabled events will be
        restarted after each user interaction.

        Added in version 3.14.

    Derived classes and clients can call the following methods to get a data
    structure representing a stack trace.

    get\_stack(*f*, *t*)[¶](#bdb.Bdb.get_stack "Link to this definition")
    :   Return a list of (frame, lineno) tuples in a stack trace, and a size.

        The most recently called frame is last in the list. The size is the number
        of frames below the frame where the debugger was invoked.

    format\_stack\_entry(*frame\_lineno*, *lprefix=': '*)[¶](#bdb.Bdb.format_stack_entry "Link to this definition")
    :   Return a string with information about a stack entry, which is a
        `(frame, lineno)` tuple. The return string contains:

        * The canonical filename which contains the frame.
        * The function name or `"<lambda>"`.
        * The input arguments.
        * The return value.
        * The line of code (if it exists).

    The following two methods can be called by clients to use a debugger to debug
    a [statement](../glossary.html#term-statement), given as a string.

    run(*cmd*, *globals=None*, *locals=None*)[¶](#bdb.Bdb.run "Link to this definition")
    :   Debug a statement executed via the [`exec()`](functions.html#exec "exec") function. *globals*
        defaults to `__main__.__dict__`, *locals* defaults to *globals*.

    runeval(*expr*, *globals=None*, *locals=None*)[¶](#bdb.Bdb.runeval "Link to this definition")
    :   Debug an expression executed via the [`eval()`](functions.html#eval "eval") function. *globals* and
        *locals* have the same meaning as in [`run()`](#bdb.Bdb.run "bdb.Bdb.run").

    runctx(*cmd*, *globals*, *locals*)[¶](#bdb.Bdb.runctx "Link to this definition")
    :   For backwards compatibility. Calls the [`run()`](#bdb.Bdb.run "bdb.Bdb.run") method.

    runcall(*func*, */*, *\*args*, *\*\*kwds*)[¶](#bdb.Bdb.runcall "Link to this definition")
    :   Debug a single function call, and return its result.

Finally, the module defines the following functions:

bdb.checkfuncname(*b*, *frame*)[¶](#bdb.checkfuncname "Link to this definition")
:   Return `True` if we should break here, depending on the way the
    [`Breakpoint`](#bdb.Breakpoint "bdb.Breakpoint") *b* was set.

    If it was set via line number, it checks if
    [`b.line`](#bdb.Breakpoint.line "bdb.Breakpoint.line") is the same as the one in *frame*.
    If the breakpoint was set via
    [`function name`](#bdb.Breakpoint.funcname "bdb.Breakpoint.funcname"), we have to check we are in
    the right *frame* (the right function) and if we are on its first executable
    line.

bdb.effective(*file*, *line*, *frame*)[¶](#bdb.effective "Link to this definition")
:   Return `(active breakpoint, delete temporary flag)` or `(None, None)` as the
    breakpoint to act upon.

    The *active breakpoint* is the first entry in
    [`bplist`](#bdb.Breakpoint.bplist "bdb.Breakpoint.bplist") for the
    ([`file`](#bdb.Breakpoint.file "bdb.Breakpoint.file"), [`line`](#bdb.Breakpoint.line "bdb.Breakpoint.line"))
    (which must exist) that is [`enabled`](#bdb.Breakpoint.enabled "bdb.Breakpoint.enabled"), for
    which [`checkfuncname()`](#bdb.checkfuncname "bdb.checkfuncname") is true, and that has neither a false
    [`condition`](#bdb.Breakpoint.cond "bdb.Breakpoint.cond") nor positive
    [`ignore`](#bdb.Breakpoint.ignore "bdb.Breakpoint.ignore") count. The *flag*, meaning that a
    temporary breakpoint should be deleted, is `False` only when the
    [`cond`](#bdb.Breakpoint.cond "bdb.Breakpoint.cond") cannot be evaluated (in which case,
    [`ignore`](#bdb.Breakpoint.ignore "bdb.Breakpoint.ignore") count is ignored).

    If no such entry exists, then `(None, None)` is returned.

bdb.set\_trace()[¶](#bdb.set_trace "Link to this definition")
:   Start debugging with a [`Bdb`](#bdb.Bdb "bdb.Bdb") instance from caller’s frame.

#### Previous topic

[Audit events table](audit_events.html "previous chapter")

#### Next topic

[`faulthandler` — Dump the Python traceback](faulthandler.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/bdb.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](faulthandler.html "faulthandler — Dump the Python traceback") |
* [previous](audit_events.html "Audit events table") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Debugging and Profiling](debug.html) »
* `bdb` — Debugger framework
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
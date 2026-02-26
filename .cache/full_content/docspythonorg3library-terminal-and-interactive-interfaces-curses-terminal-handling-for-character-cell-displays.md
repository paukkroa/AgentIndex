### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](curses.ascii.html "curses.ascii — Utilities for ASCII characters") |
* [previous](fileinput.html "fileinput — Iterate over lines from multiple input streams") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Command-line interface libraries](cmdlinelibs.html) »
* `curses` — Terminal handling for character-cell displays
* |
* Theme
  Auto
  Light
  Dark
   |

# `curses` — Terminal handling for character-cell displays[¶](#module-curses "Link to this heading")

**Source code:** [Lib/curses](https://github.com/python/cpython/tree/3.14/Lib/curses)

---

The `curses` module provides an interface to the curses library, the
de-facto standard for portable advanced terminal handling.

While curses is most widely used in the Unix environment, versions are available
for Windows, DOS, and possibly other systems as well. This extension module is
designed to match the API of ncurses, an open-source curses library hosted on
Linux and the BSD variants of Unix.

[Availability](intro.html#availability): not Android, not iOS, not WASI.

This module is not supported on [mobile platforms](intro.html#mobile-availability)
or [WebAssembly platforms](intro.html#wasm-availability).

This is an [optional module](../glossary.html#term-optional-module).
If it is missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](../using/configure.html#optional-module-requirements).

[Availability](intro.html#availability): Unix.

Note

Whenever the documentation mentions a *character* it can be specified
as an integer, a one-character Unicode string or a one-byte byte string.

Whenever the documentation mentions a *character string* it can be specified
as a Unicode string or a byte string.

See also

Module [`curses.ascii`](curses.ascii.html#module-curses.ascii "curses.ascii: Constants and set-membership functions for ASCII characters.")
:   Utilities for working with ASCII characters, regardless of your locale settings.

Module [`curses.panel`](curses.panel.html#module-curses.panel "curses.panel: A panel stack extension that adds depth to curses windows.")
:   A panel stack extension that adds depth to curses windows.

Module [`curses.textpad`](#module-curses.textpad "curses.textpad: Emacs-like input editing in a curses window.")
:   Editable text widget for curses supporting **Emacs**-like bindings.

[Curses Programming with Python](../howto/curses.html#curses-howto)
:   Tutorial material on using curses with Python, by Andrew Kuchling and Eric
    Raymond.

## Functions[¶](#functions "Link to this heading")

The module `curses` defines the following exception:

*exception* curses.error[¶](#curses.error "Link to this definition")
:   Exception raised when a curses library function returns an error.

Note

Whenever *x* or *y* arguments to a function or a method are optional, they
default to the current cursor location. Whenever *attr* is optional, it defaults
to [`A_NORMAL`](#curses.A_NORMAL "curses.A_NORMAL").

The module `curses` defines the following functions:

curses.assume\_default\_colors(*fg*, *bg*, */*)[¶](#curses.assume_default_colors "Link to this definition")
:   Allow use of default values for colors on terminals supporting this feature.
    Use this to support transparency in your application.

    * Assign terminal default foreground/background colors to color number `-1`.
      So `init_pair(x, COLOR_RED, -1)` will initialize pair *x* as red
      on default background and `init_pair(x, -1, COLOR_BLUE)` will
      initialize pair *x* as default foreground on blue.
    * Change the definition of the color-pair `0` to `(fg, bg)`.

    Added in version 3.14.

curses.baudrate()[¶](#curses.baudrate "Link to this definition")
:   Return the output speed of the terminal in bits per second. On software
    terminal emulators it will have a fixed high value. Included for historical
    reasons; in former times, it was used to write output loops for time delays and
    occasionally to change interfaces depending on the line speed.

curses.beep()[¶](#curses.beep "Link to this definition")
:   Emit a short attention sound.

curses.can\_change\_color()[¶](#curses.can_change_color "Link to this definition")
:   Return `True` or `False`, depending on whether the programmer can change the colors
    displayed by the terminal.

curses.cbreak()[¶](#curses.cbreak "Link to this definition")
:   Enter cbreak mode. In cbreak mode (sometimes called “rare” mode) normal tty
    line buffering is turned off and characters are available to be read one by one.
    However, unlike raw mode, special characters (interrupt, quit, suspend, and flow
    control) retain their effects on the tty driver and calling program. Calling
    first [`raw()`](#curses.raw "curses.raw") then [`cbreak()`](#curses.cbreak "curses.cbreak") leaves the terminal in cbreak mode.

curses.color\_content(*color\_number*)[¶](#curses.color_content "Link to this definition")
:   Return the intensity of the red, green, and blue (RGB) components in the color
    *color\_number*, which must be between `0` and `COLORS - 1`. Return a 3-tuple,
    containing the R,G,B values for the given color, which will be between
    `0` (no component) and `1000` (maximum amount of component).

curses.color\_pair(*pair\_number*)[¶](#curses.color_pair "Link to this definition")
:   Return the attribute value for displaying text in the specified color pair.
    Only the first 256 color pairs are supported. This
    attribute value can be combined with [`A_STANDOUT`](#curses.A_STANDOUT "curses.A_STANDOUT"), [`A_REVERSE`](#curses.A_REVERSE "curses.A_REVERSE"),
    and the other `A_*` attributes. [`pair_number()`](#curses.pair_number "curses.pair_number") is the counterpart
    to this function.

curses.curs\_set(*visibility*)[¶](#curses.curs_set "Link to this definition")
:   Set the cursor state. *visibility* can be set to `0`, `1`, or `2`, for invisible,
    normal, or very visible. If the terminal supports the visibility requested, return the
    previous cursor state; otherwise raise an exception. On many
    terminals, the “visible” mode is an underline cursor and the “very visible” mode
    is a block cursor.

curses.def\_prog\_mode()[¶](#curses.def_prog_mode "Link to this definition")
:   Save the current terminal mode as the “program” mode, the mode when the running
    program is using curses. (Its counterpart is the “shell” mode, for when the
    program is not in curses.) Subsequent calls to [`reset_prog_mode()`](#curses.reset_prog_mode "curses.reset_prog_mode") will
    restore this mode.

curses.def\_shell\_mode()[¶](#curses.def_shell_mode "Link to this definition")
:   Save the current terminal mode as the “shell” mode, the mode when the running
    program is not using curses. (Its counterpart is the “program” mode, when the
    program is using curses capabilities.) Subsequent calls to
    [`reset_shell_mode()`](#curses.reset_shell_mode "curses.reset_shell_mode") will restore this mode.

curses.delay\_output(*ms*)[¶](#curses.delay_output "Link to this definition")
:   Insert an *ms* millisecond pause in output.

curses.doupdate()[¶](#curses.doupdate "Link to this definition")
:   Update the physical screen. The curses library keeps two data structures, one
    representing the current physical screen contents and a virtual screen
    representing the desired next state. The [`doupdate()`](#curses.doupdate "curses.doupdate") ground updates the
    physical screen to match the virtual screen.

    The virtual screen may be updated by a [`noutrefresh()`](#curses.window.noutrefresh "curses.window.noutrefresh") call after write
    operations such as [`addstr()`](#curses.window.addstr "curses.window.addstr") have been performed on a window. The normal
    [`refresh()`](#curses.window.refresh "curses.window.refresh") call is simply `noutrefresh()` followed by `doupdate()`;
    if you have to update multiple windows, you can speed performance and perhaps
    reduce screen flicker by issuing `noutrefresh()` calls on all windows,
    followed by a single `doupdate()`.

curses.echo()[¶](#curses.echo "Link to this definition")
:   Enter echo mode. In echo mode, each character input is echoed to the screen as
    it is entered.

curses.endwin()[¶](#curses.endwin "Link to this definition")
:   De-initialize the library, and return terminal to normal status.

curses.erasechar()[¶](#curses.erasechar "Link to this definition")
:   Return the user’s current erase character as a one-byte bytes object. Under Unix operating systems this
    is a property of the controlling tty of the curses program, and is not set by
    the curses library itself.

curses.filter()[¶](#curses.filter "Link to this definition")
:   The [`filter()`](#curses.filter "curses.filter") routine, if used, must be called before [`initscr()`](#curses.initscr "curses.initscr") is
    called. The effect is that, during those calls, `LINES` is set to `1`; the
    capabilities `clear`, `cup`, `cud`, `cud1`, `cuu1`, `cuu`, `vpa` are disabled; and the `home`
    string is set to the value of `cr`. The effect is that the cursor is confined to
    the current line, and so are screen updates. This may be used for enabling
    character-at-a-time line editing without touching the rest of the screen.

curses.flash()[¶](#curses.flash "Link to this definition")
:   Flash the screen. That is, change it to reverse-video and then change it back
    in a short interval. Some people prefer such as ‘visible bell’ to the audible
    attention signal produced by [`beep()`](#curses.beep "curses.beep").

curses.flushinp()[¶](#curses.flushinp "Link to this definition")
:   Flush all input buffers. This throws away any typeahead that has been typed
    by the user and has not yet been processed by the program.

curses.getmouse()[¶](#curses.getmouse "Link to this definition")
:   After [`getch()`](#curses.window.getch "curses.window.getch") returns [`KEY_MOUSE`](#curses.KEY_MOUSE "curses.KEY_MOUSE") to signal a mouse event, this
    method should be called to retrieve the queued mouse event, represented as a
    5-tuple `(id, x, y, z, bstate)`. *id* is an ID value used to distinguish
    multiple devices, and *x*, *y*, *z* are the event’s coordinates. (*z* is
    currently unused.) *bstate* is an integer value whose bits will be set to
    indicate the type of event, and will be the bitwise OR of one or more of the
    following constants, where *n* is the button number from 1 to 5:
    [`BUTTONn_PRESSED`](#curses.BUTTONn_PRESSED "curses.BUTTONn_PRESSED"), [`BUTTONn_RELEASED`](#curses.BUTTONn_RELEASED "curses.BUTTONn_RELEASED"), [`BUTTONn_CLICKED`](#curses.BUTTONn_CLICKED "curses.BUTTONn_CLICKED"),
    [`BUTTONn_DOUBLE_CLICKED`](#curses.BUTTONn_DOUBLE_CLICKED "curses.BUTTONn_DOUBLE_CLICKED"), [`BUTTONn_TRIPLE_CLICKED`](#curses.BUTTONn_TRIPLE_CLICKED "curses.BUTTONn_TRIPLE_CLICKED"),
    [`BUTTON_SHIFT`](#curses.BUTTON_SHIFT "curses.BUTTON_SHIFT"), [`BUTTON_CTRL`](#curses.BUTTON_CTRL "curses.BUTTON_CTRL"), [`BUTTON_ALT`](#curses.BUTTON_ALT "curses.BUTTON_ALT").

    Changed in version 3.10: The `BUTTON5_*` constants are now exposed if they are provided by the
    underlying curses library.

curses.getsyx()[¶](#curses.getsyx "Link to this definition")
:   Return the current coordinates of the virtual screen cursor as a tuple
    `(y, x)`. If [`leaveok`](#curses.window.leaveok "curses.window.leaveok") is currently `True`, then return `(-1, -1)`.

curses.getwin(*file*)[¶](#curses.getwin "Link to this definition")
:   Read window related data stored in the file by an earlier [`window.putwin()`](#curses.window.putwin "curses.window.putwin") call.
    The routine then creates and initializes a new window using that data, returning
    the new window object.

curses.has\_colors()[¶](#curses.has_colors "Link to this definition")
:   Return `True` if the terminal can display colors; otherwise, return `False`.

curses.has\_extended\_color\_support()[¶](#curses.has_extended_color_support "Link to this definition")
:   Return `True` if the module supports extended colors; otherwise, return
    `False`. Extended color support allows more than 256 color pairs for
    terminals that support more than 16 colors (e.g. xterm-256color).

    Extended color support requires ncurses version 6.1 or later.

    Added in version 3.10.

curses.has\_ic()[¶](#curses.has_ic "Link to this definition")
:   Return `True` if the terminal has insert- and delete-character capabilities.
    This function is included for historical reasons only, as all modern software
    terminal emulators have such capabilities.

curses.has\_il()[¶](#curses.has_il "Link to this definition")
:   Return `True` if the terminal has insert- and delete-line capabilities, or can
    simulate them using scrolling regions. This function is included for
    historical reasons only, as all modern software terminal emulators have such
    capabilities.

curses.has\_key(*ch*)[¶](#curses.has_key "Link to this definition")
:   Take a key value *ch*, and return `True` if the current terminal type recognizes
    a key with that value.

curses.halfdelay(*tenths*)[¶](#curses.halfdelay "Link to this definition")
:   Used for half-delay mode, which is similar to cbreak mode in that characters
    typed by the user are immediately available to the program. However, after
    blocking for *tenths* tenths of seconds, raise an exception if nothing has
    been typed. The value of *tenths* must be a number between `1` and `255`. Use
    [`nocbreak()`](#curses.nocbreak "curses.nocbreak") to leave half-delay mode.

curses.init\_color(*color\_number*, *r*, *g*, *b*)[¶](#curses.init_color "Link to this definition")
:   Change the definition of a color, taking the number of the color to be changed
    followed by three RGB values (for the amounts of red, green, and blue
    components). The value of *color\_number* must be between `0` and
    `COLORS - 1`. Each of *r*, *g*, *b*, must be a value between `0` and
    `1000`. When [`init_color()`](#curses.init_color "curses.init_color") is used, all occurrences of that color on the
    screen immediately change to the new definition. This function is a no-op on
    most terminals; it is active only if [`can_change_color()`](#curses.can_change_color "curses.can_change_color") returns `True`.

curses.init\_pair(*pair\_number*, *fg*, *bg*)[¶](#curses.init_pair "Link to this definition")
:   Change the definition of a color-pair. It takes three arguments: the number of
    the color-pair to be changed, the foreground color number, and the background
    color number. The value of *pair\_number* must be between `1` and
    `COLOR_PAIRS - 1` (the `0` color pair can only be changed by
    [`use_default_colors()`](#curses.use_default_colors "curses.use_default_colors") and [`assume_default_colors()`](#curses.assume_default_colors "curses.assume_default_colors")).
    The value of *fg* and *bg* arguments must be between `0` and
    `COLORS - 1`, or, after calling `use_default_colors()` or
    `assume_default_colors()`, `-1`.
    If the color-pair was previously initialized, the screen is
    refreshed and all occurrences of that color-pair are changed to the new
    definition.

curses.initscr()[¶](#curses.initscr "Link to this definition")
:   Initialize the library. Return a [window](#curses-window-objects) object
    which represents the whole screen.

    Note

    If there is an error opening the terminal, the underlying curses library may
    cause the interpreter to exit.

curses.is\_term\_resized(*nlines*, *ncols*)[¶](#curses.is_term_resized "Link to this definition")
:   Return `True` if [`resize_term()`](#curses.resize_term "curses.resize_term") would modify the window structure,
    `False` otherwise.

curses.isendwin()[¶](#curses.isendwin "Link to this definition")
:   Return `True` if [`endwin()`](#curses.endwin "curses.endwin") has been called (that is, the curses library has
    been deinitialized).

curses.keyname(*k*)[¶](#curses.keyname "Link to this definition")
:   Return the name of the key numbered *k* as a bytes object. The name of a key generating printable
    ASCII character is the key’s character. The name of a control-key combination
    is a two-byte bytes object consisting of a caret (`b'^'`) followed by the corresponding
    printable ASCII character. The name of an alt-key combination (128–255) is a
    bytes object consisting of the prefix `b'M-'` followed by the name of the corresponding
    ASCII character.

curses.killchar()[¶](#curses.killchar "Link to this definition")
:   Return the user’s current line kill character as a one-byte bytes object. Under Unix operating systems
    this is a property of the controlling tty of the curses program, and is not set
    by the curses library itself.

curses.longname()[¶](#curses.longname "Link to this definition")
:   Return a bytes object containing the terminfo long name field describing the current
    terminal. The maximum length of a verbose description is 128 characters. It is
    defined only after the call to [`initscr()`](#curses.initscr "curses.initscr").

curses.meta(*flag*)[¶](#curses.meta "Link to this definition")
:   If *flag* is `True`, allow 8-bit characters to be input. If
    *flag* is `False`, allow only 7-bit chars.

curses.mouseinterval(*interval*)[¶](#curses.mouseinterval "Link to this definition")
:   Set the maximum time in milliseconds that can elapse between press and release
    events in order for them to be recognized as a click, and return the previous
    interval value. The default value is 200 milliseconds, or one fifth of a second.

curses.mousemask(*mousemask*)[¶](#curses.mousemask "Link to this definition")
:   Set the mouse events to be reported, and return a tuple `(availmask,
    oldmask)`. *availmask* indicates which of the specified mouse events can be
    reported; on complete failure it returns `0`. *oldmask* is the previous value of
    the given window’s mouse event mask. If this function is never called, no mouse
    events are ever reported.

curses.napms(*ms*)[¶](#curses.napms "Link to this definition")
:   Sleep for *ms* milliseconds.

curses.newpad(*nlines*, *ncols*)[¶](#curses.newpad "Link to this definition")
:   Create and return a pointer to a new pad data structure with the given number
    of lines and columns. Return a pad as a window object.

    A pad is like a window, except that it is not restricted by the screen size, and
    is not necessarily associated with a particular part of the screen. Pads can be
    used when a large window is needed, and only a part of the window will be on the
    screen at one time. Automatic refreshes of pads (such as from scrolling or
    echoing of input) do not occur. The [`refresh()`](#curses.window.refresh "curses.window.refresh") and [`noutrefresh()`](#curses.window.noutrefresh "curses.window.noutrefresh")
    methods of a pad require 6 arguments to specify the part of the pad to be
    displayed and the location on the screen to be used for the display. The
    arguments are *pminrow*, *pmincol*, *sminrow*, *smincol*, *smaxrow*, *smaxcol*; the *p*
    arguments refer to the upper left corner of the pad region to be displayed and
    the *s* arguments define a clipping box on the screen within which the pad region
    is to be displayed.

curses.newwin(*nlines*, *ncols*)[¶](#curses.newwin "Link to this definition")

curses.newwin(*nlines*, *ncols*, *begin\_y*, *begin\_x*)
:   Return a new [window](#curses-window-objects), whose left-upper corner
    is at `(begin_y, begin_x)`, and whose height/width is *nlines*/*ncols*.

    By default, the window will extend from the specified position to the lower
    right corner of the screen.

curses.nl()[¶](#curses.nl "Link to this definition")
:   Enter newline mode. This mode translates the return key into newline on input,
    and translates newline into return and line-feed on output. Newline mode is
    initially on.

curses.nocbreak()[¶](#curses.nocbreak "Link to this definition")
:   Leave cbreak mode. Return to normal “cooked” mode with line buffering.

curses.noecho()[¶](#curses.noecho "Link to this definition")
:   Leave echo mode. Echoing of input characters is turned off.

curses.nonl()[¶](#curses.nonl "Link to this definition")
:   Leave newline mode. Disable translation of return into newline on input, and
    disable low-level translation of newline into newline/return on output (but this
    does not change the behavior of `addch('\n')`, which always does the
    equivalent of return and line feed on the virtual screen). With translation
    off, curses can sometimes speed up vertical motion a little; also, it will be
    able to detect the return key on input.

curses.noqiflush()[¶](#curses.noqiflush "Link to this definition")
:   When the `noqiflush()` routine is used, normal flush of input and output queues
    associated with the `INTR`, `QUIT` and `SUSP` characters will not be done. You may
    want to call `noqiflush()` in a signal handler if you want output to
    continue as though the interrupt had not occurred, after the handler exits.

curses.noraw()[¶](#curses.noraw "Link to this definition")
:   Leave raw mode. Return to normal “cooked” mode with line buffering.

curses.pair\_content(*pair\_number*)[¶](#curses.pair_content "Link to this definition")
:   Return a tuple `(fg, bg)` containing the colors for the requested color pair.
    The value of *pair\_number* must be between `0` and `COLOR_PAIRS - 1`.

curses.pair\_number(*attr*)[¶](#curses.pair_number "Link to this definition")
:   Return the number of the color-pair set by the attribute value *attr*.
    [`color_pair()`](#curses.color_pair "curses.color_pair") is the counterpart to this function.

curses.putp(*str*)[¶](#curses.putp "Link to this definition")
:   Equivalent to `tputs(str, 1, putchar)`; emit the value of a specified
    terminfo capability for the current terminal. Note that the output of [`putp()`](#curses.putp "curses.putp")
    always goes to standard output.

curses.qiflush([*flag*])[¶](#curses.qiflush "Link to this definition")
:   If *flag* is `False`, the effect is the same as calling [`noqiflush()`](#curses.noqiflush "curses.noqiflush"). If
    *flag* is `True`, or no argument is provided, the queues will be flushed when
    these control characters are read.

curses.raw()[¶](#curses.raw "Link to this definition")
:   Enter raw mode. In raw mode, normal line buffering and processing of
    interrupt, quit, suspend, and flow control keys are turned off; characters are
    presented to curses input functions one by one.

curses.reset\_prog\_mode()[¶](#curses.reset_prog_mode "Link to this definition")
:   Restore the terminal to “program” mode, as previously saved by
    [`def_prog_mode()`](#curses.def_prog_mode "curses.def_prog_mode").

curses.reset\_shell\_mode()[¶](#curses.reset_shell_mode "Link to this definition")
:   Restore the terminal to “shell” mode, as previously saved by
    [`def_shell_mode()`](#curses.def_shell_mode "curses.def_shell_mode").

curses.resetty()[¶](#curses.resetty "Link to this definition")
:   Restore the state of the terminal modes to what it was at the last call to
    [`savetty()`](#curses.savetty "curses.savetty").

curses.resize\_term(*nlines*, *ncols*)[¶](#curses.resize_term "Link to this definition")
:   Backend function used by [`resizeterm()`](#curses.resizeterm "curses.resizeterm"), performing most of the work;
    when resizing the windows, [`resize_term()`](#curses.resize_term "curses.resize_term") blank-fills the areas that are
    extended. The calling application should fill in these areas with
    appropriate data. The `resize_term()` function attempts to resize all
    windows. However, due to the calling convention of pads, it is not possible
    to resize these without additional interaction with the application.

curses.resizeterm(*nlines*, *ncols*)[¶](#curses.resizeterm "Link to this definition")
:   Resize the standard and current windows to the specified dimensions, and
    adjusts other bookkeeping data used by the curses library that record the
    window dimensions (in particular the SIGWINCH handler).

curses.savetty()[¶](#curses.savetty "Link to this definition")
:   Save the current state of the terminal modes in a buffer, usable by
    [`resetty()`](#curses.resetty "curses.resetty").

curses.get\_escdelay()[¶](#curses.get_escdelay "Link to this definition")
:   Retrieves the value set by [`set_escdelay()`](#curses.set_escdelay "curses.set_escdelay").

    Added in version 3.9.

curses.set\_escdelay(*ms*)[¶](#curses.set_escdelay "Link to this definition")
:   Sets the number of milliseconds to wait after reading an escape character,
    to distinguish between an individual escape character entered on the
    keyboard from escape sequences sent by cursor and function keys.

    Added in version 3.9.

curses.get\_tabsize()[¶](#curses.get_tabsize "Link to this definition")
:   Retrieves the value set by [`set_tabsize()`](#curses.set_tabsize "curses.set_tabsize").

    Added in version 3.9.

curses.set\_tabsize(*size*)[¶](#curses.set_tabsize "Link to this definition")
:   Sets the number of columns used by the curses library when converting a tab
    character to spaces as it adds the tab to a window.

    Added in version 3.9.

curses.setsyx(*y*, *x*)[¶](#curses.setsyx "Link to this definition")
:   Set the virtual screen cursor to *y*, *x*. If *y* and *x* are both `-1`, then
    [`leaveok`](#curses.window.leaveok "curses.window.leaveok") is set `True`.

curses.setupterm(*term=None*, *fd=-1*)[¶](#curses.setupterm "Link to this definition")
:   Initialize the terminal. *term* is a string giving
    the terminal name, or `None`; if omitted or `None`, the value of the
    `TERM` environment variable will be used. *fd* is the
    file descriptor to which any initialization sequences will be sent; if not
    supplied or `-1`, the file descriptor for `sys.stdout` will be used.

curses.start\_color()[¶](#curses.start_color "Link to this definition")
:   Must be called if the programmer wants to use colors, and before any other color
    manipulation routine is called. It is good practice to call this routine right
    after [`initscr()`](#curses.initscr "curses.initscr").

    [`start_color()`](#curses.start_color "curses.start_color") initializes eight basic colors (black, red, green, yellow,
    blue, magenta, cyan, and white), and two global variables in the `curses`
    module, [`COLORS`](#curses.COLORS "curses.COLORS") and [`COLOR_PAIRS`](#curses.COLOR_PAIRS "curses.COLOR_PAIRS"), containing the maximum number
    of colors and color-pairs the terminal can support. It also restores the colors
    on the terminal to the values they had when the terminal was just turned on.

curses.termattrs()[¶](#curses.termattrs "Link to this definition")
:   Return a logical OR of all video attributes supported by the terminal. This
    information is useful when a curses program needs complete control over the
    appearance of the screen.

curses.termname()[¶](#curses.termname "Link to this definition")
:   Return the value of the environment variable `TERM`, as a bytes object,
    truncated to 14 characters.

curses.tigetflag(*capname*)[¶](#curses.tigetflag "Link to this definition")
:   Return the value of the Boolean capability corresponding to the terminfo
    capability name *capname* as an integer. Return the value `-1` if *capname* is not a
    Boolean capability, or `0` if it is canceled or absent from the terminal
    description.

curses.tigetnum(*capname*)[¶](#curses.tigetnum "Link to this definition")
:   Return the value of the numeric capability corresponding to the terminfo
    capability name *capname* as an integer. Return the value `-2` if *capname* is not a
    numeric capability, or `-1` if it is canceled or absent from the terminal
    description.

curses.tigetstr(*capname*)[¶](#curses.tigetstr "Link to this definition")
:   Return the value of the string capability corresponding to the terminfo
    capability name *capname* as a bytes object. Return `None` if *capname*
    is not a terminfo “string capability”, or is canceled or absent from the
    terminal description.

curses.tparm(*str*[, *...*])[¶](#curses.tparm "Link to this definition")
:   Instantiate the bytes object *str* with the supplied parameters, where *str* should
    be a parameterized string obtained from the terminfo database. E.g.
    `tparm(tigetstr("cup"), 5, 3)` could result in `b'\033[6;4H'`, the exact
    result depending on terminal type.

curses.typeahead(*fd*)[¶](#curses.typeahead "Link to this definition")
:   Specify that the file descriptor *fd* be used for typeahead checking. If *fd*
    is `-1`, then no typeahead checking is done.

    The curses library does “line-breakout optimization” by looking for typeahead
    periodically while updating the screen. If input is found, and it is coming
    from a tty, the current update is postponed until refresh or doupdate is called
    again, allowing faster response to commands typed in advance. This function
    allows specifying a different file descriptor for typeahead checking.

curses.unctrl(*ch*)[¶](#curses.unctrl "Link to this definition")
:   Return a bytes object which is a printable representation of the character *ch*.
    Control characters are represented as a caret followed by the character, for
    example as `b'^C'`. Printing characters are left as they are.

curses.ungetch(*ch*)[¶](#curses.ungetch "Link to this definition")
:   Push *ch* so the next [`getch()`](#curses.window.getch "curses.window.getch") will return it.

    Note

    Only one *ch* can be pushed before `getch()` is called.

curses.update\_lines\_cols()[¶](#curses.update_lines_cols "Link to this definition")
:   Update the [`LINES`](#curses.LINES "curses.LINES") and [`COLS`](#curses.COLS "curses.COLS") module variables.
    Useful for detecting manual screen resize.

    Added in version 3.5.

curses.unget\_wch(*ch*)[¶](#curses.unget_wch "Link to this definition")
:   Push *ch* so the next [`get_wch()`](#curses.window.get_wch "curses.window.get_wch") will return it.

    Note

    Only one *ch* can be pushed before `get_wch()` is called.

    Added in version 3.3.

curses.ungetmouse(*id*, *x*, *y*, *z*, *bstate*)[¶](#curses.ungetmouse "Link to this definition")
:   Push a [`KEY_MOUSE`](#curses.KEY_MOUSE "curses.KEY_MOUSE") event onto the input queue, associating the given
    state data with it.

curses.use\_env(*flag*)[¶](#curses.use_env "Link to this definition")
:   If used, this function should be called before [`initscr()`](#curses.initscr "curses.initscr") or newterm are
    called. When *flag* is `False`, the values of lines and columns specified in the
    terminfo database will be used, even if environment variables `LINES`
    and `COLUMNS` (used by default) are set, or if curses is running in a
    window (in which case default behavior would be to use the window size if
    `LINES` and `COLUMNS` are not set).

curses.use\_default\_colors()[¶](#curses.use_default_colors "Link to this definition")
:   Equivalent to `assume_default_colors(-1, -1)`.

curses.wrapper(*func*, */*, *\*args*, *\*\*kwargs*)[¶](#curses.wrapper "Link to this definition")
:   Initialize curses and call another callable object, *func*, which should be the
    rest of your curses-using application. If the application raises an exception,
    this function will restore the terminal to a sane state before re-raising the
    exception and generating a traceback. The callable object *func* is then passed
    the main window ‘stdscr’ as its first argument, followed by any other arguments
    passed to `wrapper()`. Before calling *func*, `wrapper()` turns on
    cbreak mode, turns off echo, enables the terminal keypad, and initializes colors
    if the terminal has color support. On exit (whether normally or by exception)
    it restores cooked mode, turns on echo, and disables the terminal keypad.

## Window Objects[¶](#window-objects "Link to this heading")

*class* curses.window[¶](#curses.window "Link to this definition")
:   Window objects, as returned by [`initscr()`](#curses.initscr "curses.initscr") and [`newwin()`](#curses.newwin "curses.newwin") above, have
    the following methods and attributes:

window.addch(*ch*[, *attr*])[¶](#curses.window.addch "Link to this definition")

window.addch(*y*, *x*, *ch*[, *attr*])
:   Paint character *ch* at `(y, x)` with attributes *attr*, overwriting any
    character previously painted at that location. By default, the character
    position and attributes are the current settings for the window object.

    Note

    Writing outside the window, subwindow, or pad raises a [`curses.error`](#curses.error "curses.error").
    Attempting to write to the lower right corner of a window, subwindow,
    or pad will cause an exception to be raised after the character is printed.

window.addnstr(*str*, *n*[, *attr*])[¶](#curses.window.addnstr "Link to this definition")

window.addnstr(*y*, *x*, *str*, *n*[, *attr*])
:   Paint at most *n* characters of the character string *str* at
    `(y, x)` with attributes
    *attr*, overwriting anything previously on the display.

window.addstr(*str*[, *attr*])[¶](#curses.window.addstr "Link to this definition")

window.addstr(*y*, *x*, *str*[, *attr*])
:   Paint the character string *str* at `(y, x)` with attributes
    *attr*, overwriting anything previously on the display.

    Note

    * Writing outside the window, subwindow, or pad raises [`curses.error`](#curses.error "curses.error").
      Attempting to write to the lower right corner of a window, subwindow,
      or pad will cause an exception to be raised after the string is printed.
    * A [bug in ncurses](https://bugs.python.org/issue35924), the backend
      for this Python module, can cause SegFaults when resizing windows. This
      is fixed in ncurses-6.1-20190511. If you are stuck with an earlier
      ncurses, you can avoid triggering this if you do not call [`addstr()`](#curses.window.addstr "curses.window.addstr")
      with a *str* that has embedded newlines. Instead, call [`addstr()`](#curses.window.addstr "curses.window.addstr")
      separately for each line.

window.attroff(*attr*)[¶](#curses.window.attroff "Link to this definition")
:   Remove attribute *attr* from the “background” set applied to all writes to the
    current window.

window.attron(*attr*)[¶](#curses.window.attron "Link to this definition")
:   Add attribute *attr* to the “background” set applied to all writes to the
    current window.

window.attrset(*attr*)[¶](#curses.window.attrset "Link to this definition")
:   Set the “background” set of attributes to *attr*. This set is initially
    `0` (no attributes).

window.bkgd(*ch*[, *attr*])[¶](#curses.window.bkgd "Link to this definition")
:   Set the background property of the window to the character *ch*, with
    attributes *attr*. The change is then applied to every character position in
    that window:

    * The attribute of every character in the window is changed to the new
      background attribute.
    * Wherever the former background character appears, it is changed to the new
      background character.

window.bkgdset(*ch*[, *attr*])[¶](#curses.window.bkgdset "Link to this definition")
:   Set the window’s background. A window’s background consists of a character and
    any combination of attributes. The attribute part of the background is combined
    (OR’ed) with all non-blank characters that are written into the window. Both
    the character and attribute parts of the background are combined with the blank
    characters. The background becomes a property of the character and moves with
    the character through any scrolling and insert/delete line/character operations.

window.border([*ls*[, *rs*[, *ts*[, *bs*[, *tl*[, *tr*[, *bl*[, *br*]]]]]]]])[¶](#curses.window.border "Link to this definition")
:   Draw a border around the edges of the window. Each parameter specifies the
    character to use for a specific part of the border; see the table below for more
    details.

    Note

    A `0` value for any parameter will cause the default character to be used for
    that parameter. Keyword parameters can *not* be used. The defaults are listed
    in this table:

    | Parameter | Description | Default value |
    | --- | --- | --- |
    | *ls* | Left side | [`ACS_VLINE`](#curses.ACS_VLINE "curses.ACS_VLINE") |
    | *rs* | Right side | [`ACS_VLINE`](#curses.ACS_VLINE "curses.ACS_VLINE") |
    | *ts* | Top | [`ACS_HLINE`](#curses.ACS_HLINE "curses.ACS_HLINE") |
    | *bs* | Bottom | [`ACS_HLINE`](#curses.ACS_HLINE "curses.ACS_HLINE") |
    | *tl* | Upper-left corner | [`ACS_ULCORNER`](#curses.ACS_ULCORNER "curses.ACS_ULCORNER") |
    | *tr* | Upper-right corner | [`ACS_URCORNER`](#curses.ACS_URCORNER "curses.ACS_URCORNER") |
    | *bl* | Bottom-left corner | [`ACS_LLCORNER`](#curses.ACS_LLCORNER "curses.ACS_LLCORNER") |
    | *br* | Bottom-right corner | [`ACS_LRCORNER`](#curses.ACS_LRCORNER "curses.ACS_LRCORNER") |

window.box([*vertch*, *horch*])[¶](#curses.window.box "Link to this definition")
:   Similar to [`border()`](#curses.window.border "curses.window.border"), but both *ls* and *rs* are *vertch* and both *ts* and
    *bs* are *horch*. The default corner characters are always used by this function.

window.chgat(*attr*)[¶](#curses.window.chgat "Link to this definition")

window.chgat(*num*, *attr*)

window.chgat(*y*, *x*, *attr*)

window.chgat(*y*, *x*, *num*, *attr*)
:   Set the attributes of *num* characters at the current cursor position, or at
    position `(y, x)` if supplied. If *num* is not given or is `-1`,
    the attribute will be set on all the characters to the end of the line. This
    function moves cursor to position `(y, x)` if supplied. The changed line
    will be touched using the [`touchline()`](#curses.window.touchline "curses.window.touchline") method so that the contents will
    be redisplayed by the next window refresh.

window.clear()[¶](#curses.window.clear "Link to this definition")
:   Like [`erase()`](#curses.window.erase "curses.window.erase"), but also cause the whole window to be repainted upon next
    call to [`refresh()`](#curses.window.refresh "curses.window.refresh").

window.clearok(*flag*)[¶](#curses.window.clearok "Link to this definition")
:   If *flag* is `True`, the next call to [`refresh()`](#curses.window.refresh "curses.window.refresh") will clear the window
    completely.

window.clrtobot()[¶](#curses.window.clrtobot "Link to this definition")
:   Erase from cursor to the end of the window: all lines below the cursor are
    deleted, and then the equivalent of [`clrtoeol()`](#curses.window.clrtoeol "curses.window.clrtoeol") is performed.

window.clrtoeol()[¶](#curses.window.clrtoeol "Link to this definition")
:   Erase from cursor to the end of the line.

window.cursyncup()[¶](#curses.window.cursyncup "Link to this definition")
:   Update the current cursor position of all the ancestors of the window to
    reflect the current cursor position of the window.

window.delch([*y*, *x*])[¶](#curses.window.delch "Link to this definition")
:   Delete any character at `(y, x)`.

window.deleteln()[¶](#curses.window.deleteln "Link to this definition")
:   Delete the line under the cursor. All following lines are moved up by one line.

window.derwin(*begin\_y*, *begin\_x*)[¶](#curses.window.derwin "Link to this definition")

window.derwin(*nlines*, *ncols*, *begin\_y*, *begin\_x*)
:   An abbreviation for “derive window”, [`derwin()`](#curses.window.derwin "curses.window.derwin") is the same as calling
    [`subwin()`](#curses.window.subwin "curses.window.subwin"), except that *begin\_y* and *begin\_x* are relative to the origin
    of the window, rather than relative to the entire screen. Return a window
    object for the derived window.

window.echochar(*ch*[, *attr*])[¶](#curses.window.echochar "Link to this definition")
:   Add character *ch* with attribute *attr*, and immediately call [`refresh()`](#curses.window.refresh "curses.window.refresh")
    on the window.

window.enclose(*y*, *x*)[¶](#curses.window.enclose "Link to this definition")
:   Test whether the given pair of screen-relative character-cell coordinates are
    enclosed by the given window, returning `True` or `False`. It is useful for
    determining what subset of the screen windows enclose the location of a mouse
    event.

    Changed in version 3.10: Previously it returned `1` or `0` instead of `True` or `False`.

window.encoding[¶](#curses.window.encoding "Link to this definition")
:   Encoding used to encode method arguments (Unicode strings and characters).
    The encoding attribute is inherited from the parent window when a subwindow
    is created, for example with [`window.subwin()`](#curses.window.subwin "curses.window.subwin").
    By default, current locale encoding is used (see [`locale.getencoding()`](locale.html#locale.getencoding "locale.getencoding")).

    Added in version 3.3.

window.erase()[¶](#curses.window.erase "Link to this definition")
:   Clear the window.

window.getbegyx()[¶](#curses.window.getbegyx "Link to this definition")
:   Return a tuple `(y, x)` of coordinates of upper-left corner.

window.getbkgd()[¶](#curses.window.getbkgd "Link to this definition")
:   Return the given window’s current background character/attribute pair.

window.getch([*y*, *x*])[¶](#curses.window.getch "Link to this definition")
:   Get a character. Note that the integer returned does *not* have to be in ASCII
    range: function keys, keypad keys and so on are represented by numbers higher
    than 255. In no-delay mode, return `-1` if there is no input, otherwise
    wait until a key is pressed.

window.get\_wch([*y*, *x*])[¶](#curses.window.get_wch "Link to this definition")
:   Get a wide character. Return a character for most keys, or an integer for
    function keys, keypad keys, and other special keys.
    In no-delay mode, raise an exception if there is no input.

    Added in version 3.3.

window.getkey([*y*, *x*])[¶](#curses.window.getkey "Link to this definition")
:   Get a character, returning a string instead of an integer, as [`getch()`](#curses.window.getch "curses.window.getch")
    does. Function keys, keypad keys and other special keys return a multibyte
    string containing the key name. In no-delay mode, raise an exception if
    there is no input.

window.getmaxyx()[¶](#curses.window.getmaxyx "Link to this definition")
:   Return a tuple `(y, x)` of the height and width of the window.

window.getparyx()[¶](#curses.window.getparyx "Link to this definition")
:   Return the beginning coordinates of this window relative to its parent window
    as a tuple `(y, x)`. Return `(-1, -1)` if this window has no
    parent.

window.getstr()[¶](#curses.window.getstr "Link to this definition")

window.getstr(*n*)

window.getstr(*y*, *x*)

window.getstr(*y*, *x*, *n*)
:   Read a bytes object from the user, with primitive line editing capacity.
    The maximum value for *n* is 2047.

    Changed in version 3.14: The maximum value for *n* was increased from 1023 to 2047.

window.getyx()[¶](#curses.window.getyx "Link to this definition")
:   Return a tuple `(y, x)` of current cursor position relative to the window’s
    upper-left corner.

window.hline(*ch*, *n*)[¶](#curses.window.hline "Link to this definition")

window.hline(*y*, *x*, *ch*, *n*)
:   Display a horizontal line starting at `(y, x)` with length *n* consisting of
    the character *ch*.

window.idcok(*flag*)[¶](#curses.window.idcok "Link to this definition")
:   If *flag* is `False`, curses no longer considers using the hardware insert/delete
    character feature of the terminal; if *flag* is `True`, use of character insertion
    and deletion is enabled. When curses is first initialized, use of character
    insert/delete is enabled by default.

window.idlok(*flag*)[¶](#curses.window.idlok "Link to this definition")
:   If *flag* is `True`, `curses` will try and use hardware line
    editing facilities. Otherwise, line insertion/deletion are disabled.

window.immedok(*flag*)[¶](#curses.window.immedok "Link to this definition")
:   If *flag* is `True`, any change in the window image automatically causes the
    window to be refreshed; you no longer have to call [`refresh()`](#curses.window.refresh "curses.window.refresh") yourself.
    However, it may degrade performance considerably, due to repeated calls to
    wrefresh. This option is disabled by default.

window.inch([*y*, *x*])[¶](#curses.window.inch "Link to this definition")
:   Return the character at the given position in the window. The bottom 8 bits are
    the character proper, and upper bits are the attributes.

window.insch(*ch*[, *attr*])[¶](#curses.window.insch "Link to this definition")

window.insch(*y*, *x*, *ch*[, *attr*])
:   Paint character *ch* at `(y, x)` with attributes *attr*, moving the line from
    position *x* right by one character.

window.insdelln(*nlines*)[¶](#curses.window.insdelln "Link to this definition")
:   Insert *nlines* lines into the specified window above the current line. The
    *nlines* bottom lines are lost. For negative *nlines*, delete *nlines* lines
    starting with the one under the cursor, and move the remaining lines up. The
    bottom *nlines* lines are cleared. The current cursor position remains the
    same.

window.insertln()[¶](#curses.window.insertln "Link to this definition")
:   Insert a blank line under the cursor. All following lines are moved down by one
    line.

window.insnstr(*str*, *n*[, *attr*])[¶](#curses.window.insnstr "Link to this definition")

window.insnstr(*y*, *x*, *str*, *n*[, *attr*])
:   Insert a character string (as many characters as will fit on the line) before
    the character under the cursor, up to *n* characters. If *n* is zero or
    negative, the entire string is inserted. All characters to the right of the
    cursor are shifted right, with the rightmost characters on the line being lost.
    The cursor position does not change (after moving to *y*, *x*, if specified).

window.insstr(*str*[, *attr*])[¶](#curses.window.insstr "Link to this definition")

window.insstr(*y*, *x*, *str*[, *attr*])
:   Insert a character string (as many characters as will fit on the line) before
    the character under the cursor. All characters to the right of the cursor are
    shifted right, with the rightmost characters on the line being lost. The cursor
    position does not change (after moving to *y*, *x*, if specified).

window.instr([*n*])[¶](#curses.window.instr "Link to this definition")

window.instr(*y*, *x*[, *n*])
:   Return a bytes object of characters, extracted from the window starting at the
    current cursor position, or at *y*, *x* if specified. Attributes are stripped
    from the characters. If *n* is specified, [`instr()`](#curses.window.instr "curses.window.instr") returns a string
    at most *n* characters long (exclusive of the trailing NUL).
    The maximum value for *n* is 2047.

    Changed in version 3.14: The maximum value for *n* was increased from 1023 to 2047.

window.is\_linetouched(*line*)[¶](#curses.window.is_linetouched "Link to this definition")
:   Return `True` if the specified line was modified since the last call to
    [`refresh()`](#curses.window.refresh "curses.window.refresh"); otherwise return `False`. Raise a [`curses.error`](#curses.error "curses.error")
    exception if *line* is not valid for the given window.

window.is\_wintouched()[¶](#curses.window.is_wintouched "Link to this definition")
:   Return `True` if the specified window was modified since the last call to
    [`refresh()`](#curses.window.refresh "curses.window.refresh"); otherwise return `False`.

window.keypad(*flag*)[¶](#curses.window.keypad "Link to this definition")
:   If *flag* is `True`, escape sequences generated by some keys (keypad, function keys)
    will be interpreted by `curses`. If *flag* is `False`, escape sequences will be
    left as is in the input stream.

window.leaveok(*flag*)[¶](#curses.window.leaveok "Link to this definition")
:   If *flag* is `True`, cursor is left where it is on update, instead of being at “cursor
    position.” This reduces cursor movement where possible. If possible the cursor
    will be made invisible.

    If *flag* is `False`, cursor will always be at “cursor position” after an update.

window.move(*new\_y*, *new\_x*)[¶](#curses.window.move "Link to this definition")
:   Move cursor to `(new_y, new_x)`.

window.mvderwin(*y*, *x*)[¶](#curses.window.mvderwin "Link to this definition")
:   Move the window inside its parent window. The screen-relative parameters of
    the window are not changed. This routine is used to display different parts of
    the parent window at the same physical position on the screen.

window.mvwin(*new\_y*, *new\_x*)[¶](#curses.window.mvwin "Link to this definition")
:   Move the window so its upper-left corner is at `(new_y, new_x)`.

window.nodelay(*flag*)[¶](#curses.window.nodelay "Link to this definition")
:   If *flag* is `True`, [`getch()`](#curses.window.getch "curses.window.getch") will be non-blocking.

window.notimeout(*flag*)[¶](#curses.window.notimeout "Link to this definition")
:   If *flag* is `True`, escape sequences will not be timed out.

    If *flag* is `False`, after a few milliseconds, an escape sequence will not be
    interpreted, and will be left in the input stream as is.

window.noutrefresh()[¶](#curses.window.noutrefresh "Link to this definition")
:   Mark for refresh but wait. This function updates the data structure
    representing the desired state of the window, but does not force an update of
    the physical screen. To accomplish that, call [`doupdate()`](#curses.doupdate "curses.doupdate").

window.overlay(*destwin*[, *sminrow*, *smincol*, *dminrow*, *dmincol*, *dmaxrow*, *dmaxcol*])[¶](#curses.window.overlay "Link to this definition")
:   Overlay the window on top of *destwin*. The windows need not be the same size,
    only the overlapping region is copied. This copy is non-destructive, which means
    that the current background character does not overwrite the old contents of
    *destwin*.

    To get fine-grained control over the copied region, the second form of
    [`overlay()`](#curses.window.overlay "curses.window.overlay") can be used. *sminrow* and *smincol* are the upper-left
    coordinates of the source window, and the other variables mark a rectangle in
    the destination window.

window.overwrite(*destwin*[, *sminrow*, *smincol*, *dminrow*, *dmincol*, *dmaxrow*, *dmaxcol*])[¶](#curses.window.overwrite "Link to this definition")
:   Overwrite the window on top of *destwin*. The windows need not be the same size,
    in which case only the overlapping region is copied. This copy is destructive,
    which means that the current background character overwrites the old contents of
    *destwin*.

    To get fine-grained control over the copied region, the second form of
    [`overwrite()`](#curses.window.overwrite "curses.window.overwrite") can be used. *sminrow* and *smincol* are the upper-left
    coordinates of the source window, the other variables mark a rectangle in the
    destination window.

window.putwin(*file*)[¶](#curses.window.putwin "Link to this definition")
:   Write all data associated with the window into the provided file object. This
    information can be later retrieved using the [`getwin()`](#curses.getwin "curses.getwin") function.

window.redrawln(*beg*, *num*)[¶](#curses.window.redrawln "Link to this definition")
:   Indicate that the *num* screen lines, starting at line *beg*, are corrupted and
    should be completely redrawn on the next [`refresh()`](#curses.window.refresh "curses.window.refresh") call.

window.redrawwin()[¶](#curses.window.redrawwin "Link to this definition")
:   Touch the entire window, causing it to be completely redrawn on the next
    [`refresh()`](#curses.window.refresh "curses.window.refresh") call.

window.refresh([*pminrow*, *pmincol*, *sminrow*, *smincol*, *smaxrow*, *smaxcol*])[¶](#curses.window.refresh "Link to this definition")
:   Update the display immediately (sync actual screen with previous
    drawing/deleting methods).

    The 6 optional arguments can only be specified when the window is a pad created
    with [`newpad()`](#curses.newpad "curses.newpad"). The additional parameters are needed to indicate what part
    of the pad and screen are involved. *pminrow* and *pmincol* specify the upper
    left-hand corner of the rectangle to be displayed in the pad. *sminrow*,
    *smincol*, *smaxrow*, and *smaxcol* specify the edges of the rectangle to be
    displayed on the screen. The lower right-hand corner of the rectangle to be
    displayed in the pad is calculated from the screen coordinates, since the
    rectangles must be the same size. Both rectangles must be entirely contained
    within their respective structures. Negative values of *pminrow*, *pmincol*,
    *sminrow*, or *smincol* are treated as if they were zero.

window.resize(*nlines*, *ncols*)[¶](#curses.window.resize "Link to this definition")
:   Reallocate storage for a curses window to adjust its dimensions to the
    specified values. If either dimension is larger than the current values, the
    window’s data is filled with blanks that have the current background
    rendition (as set by [`bkgdset()`](#curses.window.bkgdset "curses.window.bkgdset")) merged into them.

window.scroll([*lines=1*])[¶](#curses.window.scroll "Link to this definition")
:   Scroll the screen or scrolling region upward by *lines* lines.

window.scrollok(*flag*)[¶](#curses.window.scrollok "Link to this definition")
:   Control what happens when the cursor of a window is moved off the edge of the
    window or scrolling region, either as a result of a newline action on the bottom
    line, or typing the last character of the last line. If *flag* is `False`, the
    cursor is left on the bottom line. If *flag* is `True`, the window is scrolled up
    one line. Note that in order to get the physical scrolling effect on the
    terminal, it is also necessary to call [`idlok()`](#curses.window.idlok "curses.window.idlok").

window.setscrreg(*top*, *bottom*)[¶](#curses.window.setscrreg "Link to this definition")
:   Set the scrolling region from line *top* to line *bottom*. All scrolling actions
    will take place in this region.

window.standend()[¶](#curses.window.standend "Link to this definition")
:   Turn off the standout attribute. On some terminals this has the side effect of
    turning off all attributes.

window.standout()[¶](#curses.window.standout "Link to this definition")
:   Turn on attribute *A\_STANDOUT*.

window.subpad(*begin\_y*, *begin\_x*)[¶](#curses.window.subpad "Link to this definition")

window.subpad(*nlines*, *ncols*, *begin\_y*, *begin\_x*)
:   Return a sub-window, whose upper-left corner is at `(begin_y, begin_x)`, and
    whose width/height is *ncols*/*nlines*.

window.subwin(*begin\_y*, *begin\_x*)[¶](#curses.window.subwin "Link to this definition")

window.subwin(*nlines*, *ncols*, *begin\_y*, *begin\_x*)
:   Return a sub-window, whose upper-left corner is at `(begin_y, begin_x)`, and
    whose width/height is *ncols*/*nlines*.

    By default, the sub-window will extend from the specified position to the lower
    right corner of the window.

window.syncdown()[¶](#curses.window.syncdown "Link to this definition")
:   Touch each location in the window that has been touched in any of its ancestor
    windows. This routine is called by [`refresh()`](#curses.window.refresh "curses.window.refresh"), so it should almost never
    be necessary to call it manually.

window.syncok(*flag*)[¶](#curses.window.syncok "Link to this definition")
:   If *flag* is `True`, then [`syncup()`](#curses.window.syncup "curses.window.syncup") is called automatically
    whenever there is a change in the window.

window.syncup()[¶](#curses.window.syncup "Link to this definition")
:   Touch all locations in ancestors of the window that have been changed in the
    window.

window.timeout(*delay*)[¶](#curses.window.timeout "Link to this definition")
:   Set blocking or non-blocking read behavior for the window. If *delay* is
    negative, blocking read is used (which will wait indefinitely for input). If
    *delay* is zero, then non-blocking read is used, and [`getch()`](#curses.window.getch "curses.window.getch") will
    return `-1` if no input is waiting. If *delay* is positive, then
    [`getch()`](#curses.window.getch "curses.window.getch") will block for *delay* milliseconds, and return `-1` if there is
    still no input at the end of that time.

window.touchline(*start*, *count*[, *changed*])[¶](#curses.window.touchline "Link to this definition")
:   Pretend *count* lines have been changed, starting with line *start*. If
    *changed* is supplied, it specifies whether the affected lines are marked as
    having been changed (*changed*`=True`) or unchanged (*changed*`=False`).

window.touchwin()[¶](#curses.window.touchwin "Link to this definition")
:   Pretend the whole window has been changed, for purposes of drawing
    optimizations.

window.untouchwin()[¶](#curses.window.untouchwin "Link to this definition")
:   Mark all lines in the window as unchanged since the last call to
    [`refresh()`](#curses.window.refresh "curses.window.refresh").

window.vline(*ch*, *n*[, *attr*])[¶](#curses.window.vline "Link to this definition")

window.vline(*y*, *x*, *ch*, *n*[, *attr*])
:   Display a vertical line starting at `(y, x)` with length *n* consisting of the
    character *ch* with attributes *attr*.

## Constants[¶](#constants "Link to this heading")

The `curses` module defines the following data members:

curses.ERR[¶](#curses.ERR "Link to this definition")
:   Some curses routines that return an integer, such as [`getch()`](#curses.window.getch "curses.window.getch"), return
    [`ERR`](#curses.ERR "curses.ERR") upon failure.

curses.OK[¶](#curses.OK "Link to this definition")
:   Some curses routines that return an integer, such as [`napms()`](#curses.napms "curses.napms"), return
    [`OK`](#curses.OK "curses.OK") upon success.

curses.version[¶](#curses.version "Link to this definition")
:   A bytes object representing the current version of the module.

curses.ncurses\_version[¶](#curses.ncurses_version "Link to this definition")
:   A named tuple containing the three components of the ncurses library
    version: *major*, *minor*, and *patch*. All values are integers. The
    components can also be accessed by name, so `curses.ncurses_version[0]`
    is equivalent to `curses.ncurses_version.major` and so on.

    Availability: if the ncurses library is used.

    Added in version 3.8.

curses.COLORS[¶](#curses.COLORS "Link to this definition")
:   The maximum number of colors the terminal can support.
    It is defined only after the call to [`start_color()`](#curses.start_color "curses.start_color").

curses.COLOR\_PAIRS[¶](#curses.COLOR_PAIRS "Link to this definition")
:   The maximum number of color pairs the terminal can support.
    It is defined only after the call to [`start_color()`](#curses.start_color "curses.start_color").

curses.COLS[¶](#curses.COLS "Link to this definition")
:   The width of the screen, i.e., the number of columns.
    It is defined only after the call to [`initscr()`](#curses.initscr "curses.initscr").
    Updated by [`update_lines_cols()`](#curses.update_lines_cols "curses.update_lines_cols"), [`resizeterm()`](#curses.resizeterm "curses.resizeterm") and
    [`resize_term()`](#curses.resize_term "curses.resize_term").

curses.LINES[¶](#curses.LINES "Link to this definition")
:   The height of the screen, i.e., the number of lines.
    It is defined only after the call to [`initscr()`](#curses.initscr "curses.initscr").
    Updated by [`update_lines_cols()`](#curses.update_lines_cols "curses.update_lines_cols"), [`resizeterm()`](#curses.resizeterm "curses.resizeterm") and
    [`resize_term()`](#curses.resize_term "curses.resize_term").

Some constants are available to specify character cell attributes.
The exact constants available are system dependent.

| Attribute | Meaning |
| --- | --- |
| curses.A\_ALTCHARSET[¶](#curses.A_ALTCHARSET "Link to this definition") | Alternate character set mode |
| curses.A\_BLINK[¶](#curses.A_BLINK "Link to this definition") | Blink mode |
| curses.A\_BOLD[¶](#curses.A_BOLD "Link to this definition") | Bold mode |
| curses.A\_DIM[¶](#curses.A_DIM "Link to this definition") | Dim mode |
| curses.A\_INVIS[¶](#curses.A_INVIS "Link to this definition") | Invisible or blank mode |
| curses.A\_ITALIC[¶](#curses.A_ITALIC "Link to this definition") | Italic mode |
| curses.A\_NORMAL[¶](#curses.A_NORMAL "Link to this definition") | Normal attribute |
| curses.A\_PROTECT[¶](#curses.A_PROTECT "Link to this definition") | Protected mode |
| curses.A\_REVERSE[¶](#curses.A_REVERSE "Link to this definition") | Reverse background and foreground colors |
| curses.A\_STANDOUT[¶](#curses.A_STANDOUT "Link to this definition") | Standout mode |
| curses.A\_UNDERLINE[¶](#curses.A_UNDERLINE "Link to this definition") | Underline mode |
| curses.A\_HORIZONTAL[¶](#curses.A_HORIZONTAL "Link to this definition") | Horizontal highlight |
| curses.A\_LEFT[¶](#curses.A_LEFT "Link to this definition") | Left highlight |
| curses.A\_LOW[¶](#curses.A_LOW "Link to this definition") | Low highlight |
| curses.A\_RIGHT[¶](#curses.A_RIGHT "Link to this definition") | Right highlight |
| curses.A\_TOP[¶](#curses.A_TOP "Link to this definition") | Top highlight |
| curses.A\_VERTICAL[¶](#curses.A_VERTICAL "Link to this definition") | Vertical highlight |

Added in version 3.7: `A_ITALIC` was added.

Several constants are available to extract corresponding attributes returned
by some methods.

| Bit-mask | Meaning |
| --- | --- |
| curses.A\_ATTRIBUTES[¶](#curses.A_ATTRIBUTES "Link to this definition") | Bit-mask to extract attributes |
| curses.A\_CHARTEXT[¶](#curses.A_CHARTEXT "Link to this definition") | Bit-mask to extract a character |
| curses.A\_COLOR[¶](#curses.A_COLOR "Link to this definition") | Bit-mask to extract color-pair field information |

Keys are referred to by integer constants with names starting with `KEY_`.
The exact keycaps available are system dependent.

| Key constant | Key |
| --- | --- |
| curses.KEY\_MIN[¶](#curses.KEY_MIN "Link to this definition") | Minimum key value |
| curses.KEY\_BREAK[¶](#curses.KEY_BREAK "Link to this definition") | Break key (unreliable) |
| curses.KEY\_DOWN[¶](#curses.KEY_DOWN "Link to this definition") | Down-arrow |
| curses.KEY\_UP[¶](#curses.KEY_UP "Link to this definition") | Up-arrow |
| curses.KEY\_LEFT[¶](#curses.KEY_LEFT "Link to this definition") | Left-arrow |
| curses.KEY\_RIGHT[¶](#curses.KEY_RIGHT "Link to this definition") | Right-arrow |
| curses.KEY\_HOME[¶](#curses.KEY_HOME "Link to this definition") | Home key (upward+left arrow) |
| curses.KEY\_BACKSPACE[¶](#curses.KEY_BACKSPACE "Link to this definition") | Backspace (unreliable) |
| curses.KEY\_F0[¶](#curses.KEY_F0 "Link to this definition") | Function keys. Up to 64 function keys are supported. |
| curses.KEY\_Fn[¶](#curses.KEY_Fn "Link to this definition") | Value of function key *n* |
| curses.KEY\_DL[¶](#curses.KEY_DL "Link to this definition") | Delete line |
| curses.KEY\_IL[¶](#curses.KEY_IL "Link to this definition") | Insert line |
| curses.KEY\_DC[¶](#curses.KEY_DC "Link to this definition") | Delete character |
| curses.KEY\_IC[¶](#curses.KEY_IC "Link to this definition") | Insert char or enter insert mode |
| curses.KEY\_EIC[¶](#curses.KEY_EIC "Link to this definition") | Exit insert char mode |
| curses.KEY\_CLEAR[¶](#curses.KEY_CLEAR "Link to this definition") | Clear screen |
| curses.KEY\_EOS[¶](#curses.KEY_EOS "Link to this definition") | Clear to end of screen |
| curses.KEY\_EOL[¶](#curses.KEY_EOL "Link to this definition") | Clear to end of line |
| curses.KEY\_SF[¶](#curses.KEY_SF "Link to this definition") | Scroll 1 line forward |
| curses.KEY\_SR[¶](#curses.KEY_SR "Link to this definition") | Scroll 1 line backward (reverse) |
| curses.KEY\_NPAGE[¶](#curses.KEY_NPAGE "Link to this definition") | Next page |
| curses.KEY\_PPAGE[¶](#curses.KEY_PPAGE "Link to this definition") | Previous page |
| curses.KEY\_STAB[¶](#curses.KEY_STAB "Link to this definition") | Set tab |
| curses.KEY\_CTAB[¶](#curses.KEY_CTAB "Link to this definition") | Clear tab |
| curses.KEY\_CATAB[¶](#curses.KEY_CATAB "Link to this definition") | Clear all tabs |
| curses.KEY\_ENTER[¶](#curses.KEY_ENTER "Link to this definition") | Enter or send (unreliable) |
| curses.KEY\_SRESET[¶](#curses.KEY_SRESET "Link to this definition") | Soft (partial) reset (unreliable) |
| curses.KEY\_RESET[¶](#curses.KEY_RESET "Link to this definition") | Reset or hard reset (unreliable) |
| curses.KEY\_PRINT[¶](#curses.KEY_PRINT "Link to this definition") | Print |
| curses.KEY\_LL[¶](#curses.KEY_LL "Link to this definition") | Home down or bottom (lower left) |
| curses.KEY\_A1[¶](#curses.KEY_A1 "Link to this definition") | Upper left of keypad |
| curses.KEY\_A3[¶](#curses.KEY_A3 "Link to this definition") | Upper right of keypad |
| curses.KEY\_B2[¶](#curses.KEY_B2 "Link to this definition") | Center of keypad |
| curses.KEY\_C1[¶](#curses.KEY_C1 "Link to this definition") | Lower left of keypad |
| curses.KEY\_C3[¶](#curses.KEY_C3 "Link to this definition") | Lower right of keypad |
| curses.KEY\_BTAB[¶](#curses.KEY_BTAB "Link to this definition") | Back tab |
| curses.KEY\_BEG[¶](#curses.KEY_BEG "Link to this definition") | Beg (beginning) |
| curses.KEY\_CANCEL[¶](#curses.KEY_CANCEL "Link to this definition") | Cancel |
| curses.KEY\_CLOSE[¶](#curses.KEY_CLOSE "Link to this definition") | Close |
| curses.KEY\_COMMAND[¶](#curses.KEY_COMMAND "Link to this definition") | Cmd (command) |
| curses.KEY\_COPY[¶](#curses.KEY_COPY "Link to this definition") | Copy |
| curses.KEY\_CREATE[¶](#curses.KEY_CREATE "Link to this definition") | Create |
| curses.KEY\_END[¶](#curses.KEY_END "Link to this definition") | End |
| curses.KEY\_EXIT[¶](#curses.KEY_EXIT "Link to this definition") | Exit |
| curses.KEY\_FIND[¶](#curses.KEY_FIND "Link to this definition") | Find |
| curses.KEY\_HELP[¶](#curses.KEY_HELP "Link to this definition") | Help |
| curses.KEY\_MARK[¶](#curses.KEY_MARK "Link to this definition") | Mark |
| curses.KEY\_MESSAGE[¶](#curses.KEY_MESSAGE "Link to this definition") | Message |
| curses.KEY\_MOVE[¶](#curses.KEY_MOVE "Link to this definition") | Move |
| curses.KEY\_NEXT[¶](#curses.KEY_NEXT "Link to this definition") | Next |
| curses.KEY\_OPEN[¶](#curses.KEY_OPEN "Link to this definition") | Open |
| curses.KEY\_OPTIONS[¶](#curses.KEY_OPTIONS "Link to this definition") | Options |
| curses.KEY\_PREVIOUS[¶](#curses.KEY_PREVIOUS "Link to this definition") | Prev (previous) |
| curses.KEY\_REDO[¶](#curses.KEY_REDO "Link to this definition") | Redo |
| curses.KEY\_REFERENCE[¶](#curses.KEY_REFERENCE "Link to this definition") | Ref (reference) |
| curses.KEY\_REFRESH[¶](#curses.KEY_REFRESH "Link to this definition") | Refresh |
| curses.KEY\_REPLACE[¶](#curses.KEY_REPLACE "Link to this definition") | Replace |
| curses.KEY\_RESTART[¶](#curses.KEY_RESTART "Link to this definition") | Restart |
| curses.KEY\_RESUME[¶](#curses.KEY_RESUME "Link to this definition") | Resume |
| curses.KEY\_SAVE[¶](#curses.KEY_SAVE "Link to this definition") | Save |
| curses.KEY\_SBEG[¶](#curses.KEY_SBEG "Link to this definition") | Shifted Beg (beginning) |
| curses.KEY\_SCANCEL[¶](#curses.KEY_SCANCEL "Link to this definition") | Shifted Cancel |
| curses.KEY\_SCOMMAND[¶](#curses.KEY_SCOMMAND "Link to this definition") | Shifted Command |
| curses.KEY\_SCOPY[¶](#curses.KEY_SCOPY "Link to this definition") | Shifted Copy |
| curses.KEY\_SCREATE[¶](#curses.KEY_SCREATE "Link to this definition") | Shifted Create |
| curses.KEY\_SDC[¶](#curses.KEY_SDC "Link to this definition") | Shifted Delete char |
| curses.KEY\_SDL[¶](#curses.KEY_SDL "Link to this definition") | Shifted Delete line |
| curses.KEY\_SELECT[¶](#curses.KEY_SELECT "Link to this definition") | Select |
| curses.KEY\_SEND[¶](#curses.KEY_SEND "Link to this definition") | Shifted End |
| curses.KEY\_SEOL[¶](#curses.KEY_SEOL "Link to this definition") | Shifted Clear line |
| curses.KEY\_SEXIT[¶](#curses.KEY_SEXIT "Link to this definition") | Shifted Exit |
| curses.KEY\_SFIND[¶](#curses.KEY_SFIND "Link to this definition") | Shifted Find |
| curses.KEY\_SHELP[¶](#curses.KEY_SHELP "Link to this definition") | Shifted Help |
| curses.KEY\_SHOME[¶](#curses.KEY_SHOME "Link to this definition") | Shifted Home |
| curses.KEY\_SIC[¶](#curses.KEY_SIC "Link to this definition") | Shifted Input |
| curses.KEY\_SLEFT[¶](#curses.KEY_SLEFT "Link to this definition") | Shifted Left arrow |
| curses.KEY\_SMESSAGE[¶](#curses.KEY_SMESSAGE "Link to this definition") | Shifted Message |
| curses.KEY\_SMOVE[¶](#curses.KEY_SMOVE "Link to this definition") | Shifted Move |
| curses.KEY\_SNEXT[¶](#curses.KEY_SNEXT "Link to this definition") | Shifted Next |
| curses.KEY\_SOPTIONS[¶](#curses.KEY_SOPTIONS "Link to this definition") | Shifted Options |
| curses.KEY\_SPREVIOUS[¶](#curses.KEY_SPREVIOUS "Link to this definition") | Shifted Prev |
| curses.KEY\_SPRINT[¶](#curses.KEY_SPRINT "Link to this definition") | Shifted Print |
| curses.KEY\_SREDO[¶](#curses.KEY_SREDO "Link to this definition") | Shifted Redo |
| curses.KEY\_SREPLACE[¶](#curses.KEY_SREPLACE "Link to this definition") | Shifted Replace |
| curses.KEY\_SRIGHT[¶](#curses.KEY_SRIGHT "Link to this definition") | Shifted Right arrow |
| curses.KEY\_SRSUME[¶](#curses.KEY_SRSUME "Link to this definition") | Shifted Resume |
| curses.KEY\_SSAVE[¶](#curses.KEY_SSAVE "Link to this definition") | Shifted Save |
| curses.KEY\_SSUSPEND[¶](#curses.KEY_SSUSPEND "Link to this definition") | Shifted Suspend |
| curses.KEY\_SUNDO[¶](#curses.KEY_SUNDO "Link to this definition") | Shifted Undo |
| curses.KEY\_SUSPEND[¶](#curses.KEY_SUSPEND "Link to this definition") | Suspend |
| curses.KEY\_UNDO[¶](#curses.KEY_UNDO "Link to this definition") | Undo |
| curses.KEY\_MOUSE[¶](#curses.KEY_MOUSE "Link to this definition") | Mouse event has occurred |
| curses.KEY\_RESIZE[¶](#curses.KEY_RESIZE "Link to this definition") | Terminal resize event |
| curses.KEY\_MAX[¶](#curses.KEY_MAX "Link to this definition") | Maximum key value |

On VT100s and their software emulations, such as X terminal emulators, there are
normally at least four function keys ([`KEY_F1`](#curses.KEY_Fn "curses.KEY_Fn"), [`KEY_F2`](#curses.KEY_Fn "curses.KEY_Fn"),
[`KEY_F3`](#curses.KEY_Fn "curses.KEY_Fn"), [`KEY_F4`](#curses.KEY_Fn "curses.KEY_Fn")) available, and the arrow keys mapped to
[`KEY_UP`](#curses.KEY_UP "curses.KEY_UP"), [`KEY_DOWN`](#curses.KEY_DOWN "curses.KEY_DOWN"), [`KEY_LEFT`](#curses.KEY_LEFT "curses.KEY_LEFT") and [`KEY_RIGHT`](#curses.KEY_RIGHT "curses.KEY_RIGHT") in
the obvious way. If your machine has a PC keyboard, it is safe to expect arrow
keys and twelve function keys (older PC keyboards may have only ten function
keys); also, the following keypad mappings are standard:

| Keycap | Constant |
| --- | --- |
| `Insert` | KEY\_IC |
| `Delete` | KEY\_DC |
| `Home` | KEY\_HOME |
| `End` | KEY\_END |
| `Page Up` | KEY\_PPAGE |
| `Page Down` | KEY\_NPAGE |

The following table lists characters from the alternate character set. These are
inherited from the VT100 terminal, and will generally be available on software
emulations such as X terminals. When there is no graphic available, curses
falls back on a crude printable ASCII approximation.

Note

These are available only after [`initscr()`](#curses.initscr "curses.initscr") has been called.

| ACS code | Meaning |
| --- | --- |
| curses.ACS\_BBSS[¶](#curses.ACS_BBSS "Link to this definition") | alternate name for upper right corner |
| curses.ACS\_BLOCK[¶](#curses.ACS_BLOCK "Link to this definition") | solid square block |
| curses.ACS\_BOARD[¶](#curses.ACS_BOARD "Link to this definition") | board of squares |
| curses.ACS\_BSBS[¶](#curses.ACS_BSBS "Link to this definition") | alternate name for horizontal line |
| curses.ACS\_BSSB[¶](#curses.ACS_BSSB "Link to this definition") | alternate name for upper left corner |
| curses.ACS\_BSSS[¶](#curses.ACS_BSSS "Link to this definition") | alternate name for top tee |
| curses.ACS\_BTEE[¶](#curses.ACS_BTEE "Link to this definition") | bottom tee |
| curses.ACS\_BULLET[¶](#curses.ACS_BULLET "Link to this definition") | bullet |
| curses.ACS\_CKBOARD[¶](#curses.ACS_CKBOARD "Link to this definition") | checker board (stipple) |
| curses.ACS\_DARROW[¶](#curses.ACS_DARROW "Link to this definition") | arrow pointing down |
| curses.ACS\_DEGREE[¶](#curses.ACS_DEGREE "Link to this definition") | degree symbol |
| curses.ACS\_DIAMOND[¶](#curses.ACS_DIAMOND "Link to this definition") | diamond |
| curses.ACS\_GEQUAL[¶](#curses.ACS_GEQUAL "Link to this definition") | greater-than-or-equal-to |
| curses.ACS\_HLINE[¶](#curses.ACS_HLINE "Link to this definition") | horizontal line |
| curses.ACS\_LANTERN[¶](#curses.ACS_LANTERN "Link to this definition") | lantern symbol |
| curses.ACS\_LARROW[¶](#curses.ACS_LARROW "Link to this definition") | left arrow |
| curses.ACS\_LEQUAL[¶](#curses.ACS_LEQUAL "Link to this definition") | less-than-or-equal-to |
| curses.ACS\_LLCORNER[¶](#curses.ACS_LLCORNER "Link to this definition") | lower left-hand corner |
| curses.ACS\_LRCORNER[¶](#curses.ACS_LRCORNER "Link to this definition") | lower right-hand corner |
| curses.ACS\_LTEE[¶](#curses.ACS_LTEE "Link to this definition") | left tee |
| curses.ACS\_NEQUAL[¶](#curses.ACS_NEQUAL "Link to this definition") | not-equal sign |
| curses.ACS\_PI[¶](#curses.ACS_PI "Link to this definition") | letter pi |
| curses.ACS\_PLMINUS[¶](#curses.ACS_PLMINUS "Link to this definition") | plus-or-minus sign |
| curses.ACS\_PLUS[¶](#curses.ACS_PLUS "Link to this definition") | big plus sign |
| curses.ACS\_RARROW[¶](#curses.ACS_RARROW "Link to this definition") | right arrow |
| curses.ACS\_RTEE[¶](#curses.ACS_RTEE "Link to this definition") | right tee |
| curses.ACS\_S1[¶](#curses.ACS_S1 "Link to this definition") | scan line 1 |
| curses.ACS\_S3[¶](#curses.ACS_S3 "Link to this definition") | scan line 3 |
| curses.ACS\_S7[¶](#curses.ACS_S7 "Link to this definition") | scan line 7 |
| curses.ACS\_S9[¶](#curses.ACS_S9 "Link to this definition") | scan line 9 |
| curses.ACS\_SBBS[¶](#curses.ACS_SBBS "Link to this definition") | alternate name for lower right corner |
| curses.ACS\_SBSB[¶](#curses.ACS_SBSB "Link to this definition") | alternate name for vertical line |
| curses.ACS\_SBSS[¶](#curses.ACS_SBSS "Link to this definition") | alternate name for right tee |
| curses.ACS\_SSBB[¶](#curses.ACS_SSBB "Link to this definition") | alternate name for lower left corner |
| curses.ACS\_SSBS[¶](#curses.ACS_SSBS "Link to this definition") | alternate name for bottom tee |
| curses.ACS\_SSSB[¶](#curses.ACS_SSSB "Link to this definition") | alternate name for left tee |
| curses.ACS\_SSSS[¶](#curses.ACS_SSSS "Link to this definition") | alternate name for crossover or big plus |
| curses.ACS\_STERLING[¶](#curses.ACS_STERLING "Link to this definition") | pound sterling |
| curses.ACS\_TTEE[¶](#curses.ACS_TTEE "Link to this definition") | top tee |
| curses.ACS\_UARROW[¶](#curses.ACS_UARROW "Link to this definition") | up arrow |
| curses.ACS\_ULCORNER[¶](#curses.ACS_ULCORNER "Link to this definition") | upper left corner |
| curses.ACS\_URCORNER[¶](#curses.ACS_URCORNER "Link to this definition") | upper right corner |
| curses.ACS\_VLINE[¶](#curses.ACS_VLINE "Link to this definition") | vertical line |

The following table lists mouse button constants used by [`getmouse()`](#curses.getmouse "curses.getmouse"):

| Mouse button constant | Meaning |
| --- | --- |
| curses.BUTTONn\_PRESSED[¶](#curses.BUTTONn_PRESSED "Link to this definition") | Mouse button *n* pressed |
| curses.BUTTONn\_RELEASED[¶](#curses.BUTTONn_RELEASED "Link to this definition") | Mouse button *n* released |
| curses.BUTTONn\_CLICKED[¶](#curses.BUTTONn_CLICKED "Link to this definition") | Mouse button *n* clicked |
| curses.BUTTONn\_DOUBLE\_CLICKED[¶](#curses.BUTTONn_DOUBLE_CLICKED "Link to this definition") | Mouse button *n* double clicked |
| curses.BUTTONn\_TRIPLE\_CLICKED[¶](#curses.BUTTONn_TRIPLE_CLICKED "Link to this definition") | Mouse button *n* triple clicked |
| curses.BUTTON\_SHIFT[¶](#curses.BUTTON_SHIFT "Link to this definition") | Shift was down during button state change |
| curses.BUTTON\_CTRL[¶](#curses.BUTTON_CTRL "Link to this definition") | Control was down during button state change |
| curses.BUTTON\_ALT[¶](#curses.BUTTON_ALT "Link to this definition") | Control was down during button state change |

Changed in version 3.10: The `BUTTON5_*` constants are now exposed if they are provided by the
underlying curses library.

The following table lists the predefined colors:

| Constant | Color |
| --- | --- |
| curses.COLOR\_BLACK[¶](#curses.COLOR_BLACK "Link to this definition") | Black |
| curses.COLOR\_BLUE[¶](#curses.COLOR_BLUE "Link to this definition") | Blue |
| curses.COLOR\_CYAN[¶](#curses.COLOR_CYAN "Link to this definition") | Cyan (light greenish blue) |
| curses.COLOR\_GREEN[¶](#curses.COLOR_GREEN "Link to this definition") | Green |
| curses.COLOR\_MAGENTA[¶](#curses.COLOR_MAGENTA "Link to this definition") | Magenta (purplish red) |
| curses.COLOR\_RED[¶](#curses.COLOR_RED "Link to this definition") | Red |
| curses.COLOR\_WHITE[¶](#curses.COLOR_WHITE "Link to this definition") | White |
| curses.COLOR\_YELLOW[¶](#curses.COLOR_YELLOW "Link to this definition") | Yellow |

# `curses.textpad` — Text input widget for curses programs[¶](#module-curses.textpad "Link to this heading")

The `curses.textpad` module provides a [`Textbox`](#curses.textpad.Textbox "curses.textpad.Textbox") class that handles
elementary text editing in a curses window, supporting a set of keybindings
resembling those of Emacs (thus, also of Netscape Navigator, BBedit 6.x,
FrameMaker, and many other programs). The module also provides a
rectangle-drawing function useful for framing text boxes or for other purposes.

The module `curses.textpad` defines the following function:

curses.textpad.rectangle(*win*, *uly*, *ulx*, *lry*, *lrx*)[¶](#curses.textpad.rectangle "Link to this definition")
:   Draw a rectangle. The first argument must be a window object; the remaining
    arguments are coordinates relative to that window. The second and third
    arguments are the y and x coordinates of the upper left hand corner of the
    rectangle to be drawn; the fourth and fifth arguments are the y and x
    coordinates of the lower right hand corner. The rectangle will be drawn using
    VT100/IBM PC forms characters on terminals that make this possible (including
    xterm and most other software terminal emulators). Otherwise it will be drawn
    with ASCII dashes, vertical bars, and plus signs.

## Textbox objects[¶](#textbox-objects "Link to this heading")

You can instantiate a [`Textbox`](#curses.textpad.Textbox "curses.textpad.Textbox") object as follows:

*class* curses.textpad.Textbox(*win*)[¶](#curses.textpad.Textbox "Link to this definition")
:   Return a textbox widget object. The *win* argument should be a curses
    [window](#curses-window-objects) object in which the textbox is to
    be contained. The edit cursor of the textbox is initially located at the
    upper left hand corner of the containing window, with coordinates `(0, 0)`.
    The instance’s [`stripspaces`](#curses.textpad.Textbox.stripspaces "curses.textpad.Textbox.stripspaces") flag is initially on.

    [`Textbox`](#curses.textpad.Textbox "curses.textpad.Textbox") objects have the following methods:

    edit([*validator*])[¶](#curses.textpad.Textbox.edit "Link to this definition")
    :   This is the entry point you will normally use. It accepts editing
        keystrokes until one of the termination keystrokes is entered. If
        *validator* is supplied, it must be a function. It will be called for
        each keystroke entered with the keystroke as a parameter; command dispatch
        is done on the result. This method returns the window contents as a
        string; whether blanks in the window are included is affected by the
        [`stripspaces`](#curses.textpad.Textbox.stripspaces "curses.textpad.Textbox.stripspaces") attribute.

    do\_command(*ch*)[¶](#curses.textpad.Textbox.do_command "Link to this definition")
    :   Process a single command keystroke. Here are the supported special
        keystrokes:

        | Keystroke | Action |
        | --- | --- |
        | `Control`-`A` | Go to left edge of window. |
        | `Control`-`B` | Cursor left, wrapping to previous line if appropriate. |
        | `Control`-`D` | Delete character under cursor. |
        | `Control`-`E` | Go to right edge (stripspaces off) or end of line (stripspaces on). |
        | `Control`-`F` | Cursor right, wrapping to next line when appropriate. |
        | `Control`-`G` | Terminate, returning the window contents. |
        | `Control`-`H` | Delete character backward. |
        | `Control`-`J` | Terminate if the window is 1 line, otherwise insert newline. |
        | `Control`-`K` | If line is blank, delete it, otherwise clear to end of line. |
        | `Control`-`L` | Refresh screen. |
        | `Control`-`N` | Cursor down; move down one line. |
        | `Control`-`O` | Insert a blank line at cursor location. |
        | `Control`-`P` | Cursor up; move up one line. |

        Move operations do nothing if the cursor is at an edge where the movement
        is not possible. The following synonyms are supported where possible:

        | Constant | Keystroke |
        | --- | --- |
        | [`KEY_LEFT`](#curses.KEY_LEFT "curses.KEY_LEFT") | `Control`-`B` |
        | [`KEY_RIGHT`](#curses.KEY_RIGHT "curses.KEY_RIGHT") | `Control`-`F` |
        | [`KEY_UP`](#curses.KEY_UP "curses.KEY_UP") | `Control`-`P` |
        | [`KEY_DOWN`](#curses.KEY_DOWN "curses.KEY_DOWN") | `Control`-`N` |
        | [`KEY_BACKSPACE`](#curses.KEY_BACKSPACE "curses.KEY_BACKSPACE") | `Control`-`h` |

        All other keystrokes are treated as a command to insert the given
        character and move right (with line wrapping).

    gather()[¶](#curses.textpad.Textbox.gather "Link to this definition")
    :   Return the window contents as a string; whether blanks in the
        window are included is affected by the [`stripspaces`](#curses.textpad.Textbox.stripspaces "curses.textpad.Textbox.stripspaces") member.

    stripspaces[¶](#curses.textpad.Textbox.stripspaces "Link to this definition")
    :   This attribute is a flag which controls the interpretation of blanks in
        the window. When it is on, trailing blanks on each line are ignored; any
        cursor motion that would land the cursor on a trailing blank goes to the
        end of that line instead, and trailing blanks are stripped when the window
        contents are gathered.

### [Table of Contents](../contents.html)

* [`curses` — Terminal handling for character-cell displays](#)
  + [Functions](#functions)
  + [Window Objects](#window-objects)
  + [Constants](#constants)
* [`curses.textpad` — Text input widget for curses programs](#module-curses.textpad)
  + [Textbox objects](#textbox-objects)

#### Previous topic

[`fileinput` — Iterate over lines from multiple input streams](fileinput.html "previous chapter")

#### Next topic

[`curses.ascii` — Utilities for ASCII characters](curses.ascii.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/curses.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](curses.ascii.html "curses.ascii — Utilities for ASCII characters") |
* [previous](fileinput.html "fileinput — Iterate over lines from multiple input streams") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Command-line interface libraries](cmdlinelibs.html) »
* `curses` — Terminal handling for character-cell displays
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
### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](bdb.html "bdb — Debugger framework") |
* [previous](debug.html "Debugging and Profiling") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Debugging and Profiling](debug.html) »
* Audit events table
* |
* Theme
  Auto
  Light
  Dark
   |

# Audit events table[¶](#audit-events-table "Link to this heading")

This table contains all events raised by [`sys.audit()`](sys.html#sys.audit "sys.audit") or
[`PySys_Audit()`](../c-api/sys.html#c.PySys_Audit "PySys_Audit") calls throughout the CPython runtime and the
standard library. These calls were added in 3.8 or later (see [**PEP 578**](https://peps.python.org/pep-0578/)).

See [`sys.addaudithook()`](sys.html#sys.addaudithook "sys.addaudithook") and [`PySys_AddAuditHook()`](../c-api/sys.html#c.PySys_AddAuditHook "PySys_AddAuditHook") for
information on handling these events.

**CPython implementation detail:** This table is generated from the CPython documentation, and may not
represent events raised by other implementations. See your runtime
specific documentation for actual events raised.

| Audit event | Arguments | References |
| --- | --- | --- |
| \_thread.start\_new\_thread | `function`, `args`, `kwargs` | [[1]](_thread.html#start_new_thread) |
| array.\_\_new\_\_ | `typecode`, `initializer` | [[1]](array.html#array.array) |
| builtins.breakpoint | `breakpointhook` | [[1]](functions.html#breakpoint) |
| builtins.id | `id` | [[1]](functions.html#id) |
| builtins.input | `prompt` | [[1]](functions.html#input) |
| builtins.input/result | `result` | [[1]](functions.html#input) |
| code.\_\_new\_\_ | `code`, `filename`, `name`, `argcount`, `posonlyargcount`, `kwonlyargcount`, `nlocals`, `stacksize`, `flags` | [[1]](types.html#types.CodeType) |
| compile | `source`, `filename` | [[1]](functions.html#compile) |
| cpython.PyConfig\_Set | `name`, `value` | [[1]](../c-api/init_config.html#c.PyConfig_Set) |
| cpython.PyInterpreterState\_Clear |  | [[1]](../c-api/init.html#c.PyInterpreterState_Clear) |
| cpython.PyInterpreterState\_New |  | [[1]](../c-api/init.html#c.PyInterpreterState_New) |
| cpython.\_PySys\_ClearAuditHooks |  | [[1]](../c-api/init.html#c.Py_FinalizeEx) |
| cpython.remote\_debugger\_script | `script_path` | [[1]](sys.html#audit_event_cpython_remote_debugger_script_0) |
| cpython.run\_command | `command` | [[1]](../using/cmdline.html#cmdoption-c) |
| cpython.run\_file | `filename` | [[1]](../using/cmdline.html#audit_event_cpython_run_file_0) |
| cpython.run\_interactivehook | `hook` | [[1]](sys.html#sys.__interactivehook__) |
| cpython.run\_module | `module-name` | [[1]](../using/cmdline.html#cmdoption-m) |
| cpython.run\_startup | `filename` | [[1]](../using/cmdline.html#envvar-PYTHONSTARTUP) |
| cpython.run\_stdin |  | [[1]](asyncio.html#audit_event_cpython_run_stdin_2)[[2]](../using/cmdline.html#audit_event_cpython_run_stdin_0)[[3]](../using/cmdline.html#audit_event_cpython_run_stdin_1) |
| ctypes.addressof | `obj` | [[1]](ctypes.html#ctypes.addressof) |
| ctypes.call\_function | `func_pointer`, `arguments` | [[1]](ctypes.html#foreign-functions) |
| ctypes.cdata | `address` | [[1]](ctypes.html#ctypes._CData.from_address) |
| ctypes.cdata/buffer | `pointer`, `size`, `offset` | [[1]](ctypes.html#ctypes._CData.from_buffer)[[2]](ctypes.html#ctypes._CData.from_buffer_copy) |
| ctypes.create\_string\_buffer | `init`, `size` | [[1]](ctypes.html#ctypes.create_string_buffer) |
| ctypes.create\_unicode\_buffer | `init`, `size` | [[1]](ctypes.html#ctypes.create_unicode_buffer) |
| ctypes.dlopen | `name` | [[1]](ctypes.html#ctypes.LibraryLoader) |
| ctypes.dlsym | `library`, `name` | [[1]](ctypes.html#ctypes.LibraryLoader) |
| ctypes.dlsym/handle | `handle`, `name` | [[1]](ctypes.html#ctypes.LibraryLoader) |
| ctypes.get\_errno |  | [[1]](ctypes.html#ctypes.get_errno) |
| ctypes.get\_last\_error |  | [[1]](ctypes.html#ctypes.get_last_error) |
| ctypes.memoryview\_at | `address`, `size`, `readonly` | [[1]](ctypes.html#audit_event_ctypes_memoryview_at_0) |
| ctypes.set\_errno | `errno` | [[1]](ctypes.html#ctypes.set_errno) |
| ctypes.set\_exception | `code` | [[1]](ctypes.html#foreign-functions) |
| ctypes.set\_last\_error | `error` | [[1]](ctypes.html#ctypes.set_last_error) |
| ctypes.string\_at | `ptr`, `size` | [[1]](ctypes.html#ctypes.string_at) |
| ctypes.wstring\_at | `ptr`, `size` | [[1]](ctypes.html#ctypes.wstring_at) |
| ensurepip.bootstrap | `root` | [[1]](ensurepip.html#ensurepip.bootstrap) |
| exec | `code_object` | [[1]](functions.html#eval)[[2]](functions.html#exec) |
| fcntl.fcntl | `fd`, `cmd`, `arg` | [[1]](fcntl.html#fcntl.fcntl) |
| fcntl.flock | `fd`, `operation` | [[1]](fcntl.html#fcntl.flock) |
| fcntl.ioctl | `fd`, `request`, `arg` | [[1]](fcntl.html#fcntl.ioctl) |
| fcntl.lockf | `fd`, `cmd`, `len`, `start`, `whence` | [[1]](fcntl.html#fcntl.lockf) |
| ftplib.connect | `self`, `host`, `port` | [[1]](ftplib.html#ftplib.FTP.connect) |
| ftplib.sendcmd | `self`, `cmd` | [[1]](ftplib.html#ftplib.FTP.sendcmd)[[2]](ftplib.html#ftplib.FTP.voidcmd) |
| function.\_\_new\_\_ | `code` | [[1]](types.html#types.FunctionType) |
| gc.get\_objects | `generation` | [[1]](gc.html#gc.get_objects) |
| gc.get\_referents | `objs` | [[1]](gc.html#gc.get_referents) |
| gc.get\_referrers | `objs` | [[1]](gc.html#gc.get_referrers) |
| glob.glob | `pathname`, `recursive` | [[1]](glob.html#glob.glob)[[2]](glob.html#glob.iglob) |
| glob.glob/2 | `pathname`, `recursive`, `root_dir`, `dir_fd` | [[1]](glob.html#glob.glob)[[2]](glob.html#glob.iglob) |
| http.client.connect | `self`, `host`, `port` | [[1]](http.client.html#http.client.HTTPConnection.connect) |
| http.client.send | `self`, `data` | [[1]](http.client.html#http.client.HTTPConnection.send) |
| imaplib.open | `self`, `host`, `port` | [[1]](imaplib.html#imaplib.IMAP4.open) |
| imaplib.send | `self`, `data` | [[1]](imaplib.html#imaplib.IMAP4.send) |
| import | `module`, `filename`, `sys.path`, `sys.meta_path`, `sys.path_hooks` | [[1]](../reference/simple_stmts.html#import) |
| marshal.dumps | `value`, `version` | [[1]](marshal.html#marshal.dump) |
| marshal.load |  | [[1]](marshal.html#marshal.load) |
| marshal.loads | `bytes` | [[1]](marshal.html#marshal.load) |
| mmap.\_\_new\_\_ | `fileno`, `length`, `access`, `offset` | [[1]](mmap.html#mmap.mmap) |
| msvcrt.get\_osfhandle | `fd` | [[1]](msvcrt.html#msvcrt.get_osfhandle) |
| msvcrt.locking | `fd`, `mode`, `nbytes` | [[1]](msvcrt.html#msvcrt.locking) |
| msvcrt.open\_osfhandle | `handle`, `flags` | [[1]](msvcrt.html#msvcrt.open_osfhandle) |
| object.\_\_delattr\_\_ | `obj`, `name` | [[1]](../reference/datamodel.html#object.__delattr__) |
| object.\_\_getattr\_\_ | `obj`, `name` | [[1]](../reference/datamodel.html#object.__getattribute__) |
| object.\_\_setattr\_\_ | `obj`, `name`, `value` | [[1]](../reference/datamodel.html#object.__setattr__) |
| open | `path`, `mode`, `flags` | [[1]](functions.html#open)[[2]](io.html#io.open)[[3]](os.html#os.open) |
| os.add\_dll\_directory | `path` | [[1]](os.html#os.add_dll_directory) |
| os.chdir | `path` | [[1]](os.html#os.chdir)[[2]](os.html#os.fchdir) |
| os.chflags | `path`, `flags` | [[1]](os.html#os.chflags)[[2]](os.html#os.lchflags) |
| os.chmod | `path`, `mode`, `dir_fd` | [[1]](os.html#os.chmod)[[2]](os.html#os.fchmod)[[3]](os.html#os.lchmod) |
| os.chown | `path`, `uid`, `gid`, `dir_fd` | [[1]](os.html#os.chown)[[2]](os.html#os.fchown)[[3]](os.html#os.lchown) |
| os.exec | `path`, `args`, `env` | [[1]](os.html#os.execl) |
| os.fork |  | [[1]](os.html#os.fork) |
| os.forkpty |  | [[1]](os.html#os.forkpty) |
| os.fwalk | `top`, `topdown`, `onerror`, `follow_symlinks`, `dir_fd` | [[1]](os.html#os.fwalk) |
| os.getxattr | `path`, `attribute` | [[1]](os.html#os.getxattr) |
| os.kill | `pid`, `sig` | [[1]](os.html#os.kill) |
| os.killpg | `pgid`, `sig` | [[1]](os.html#os.killpg) |
| os.link | `src`, `dst`, `src_dir_fd`, `dst_dir_fd` | [[1]](os.html#os.link) |
| os.listdir | `path` | [[1]](os.html#os.listdir) |
| os.listdrives |  | [[1]](os.html#os.listdrives) |
| os.listmounts | `volume` | [[1]](os.html#os.listmounts) |
| os.listvolumes |  | [[1]](os.html#os.listvolumes) |
| os.listxattr | `path` | [[1]](os.html#os.listxattr) |
| os.lockf | `fd`, `cmd`, `len` | [[1]](os.html#os.lockf) |
| os.mkdir | `path`, `mode`, `dir_fd` | [[1]](os.html#os.makedirs)[[2]](os.html#os.mkdir) |
| os.posix\_spawn | `path`, `argv`, `env` | [[1]](os.html#os.posix_spawn)[[2]](os.html#os.posix_spawnp) |
| os.putenv | `key`, `value` | [[1]](os.html#os.putenv) |
| os.remove | `path`, `dir_fd` | [[1]](os.html#os.remove)[[2]](os.html#os.removedirs)[[3]](os.html#os.unlink) |
| os.removexattr | `path`, `attribute` | [[1]](os.html#os.removexattr) |
| os.rename | `src`, `dst`, `src_dir_fd`, `dst_dir_fd` | [[1]](os.html#os.rename)[[2]](os.html#os.renames)[[3]](os.html#os.replace) |
| os.rmdir | `path`, `dir_fd` | [[1]](os.html#os.rmdir) |
| os.scandir | `path` | [[1]](os.html#os.scandir) |
| os.setxattr | `path`, `attribute`, `value`, `flags` | [[1]](os.html#os.setxattr) |
| os.spawn | `mode`, `path`, `args`, `env` | [[1]](os.html#os.spawnl) |
| os.startfile | `path`, `operation` | [[1]](os.html#os.startfile) |
| os.startfile/2 | `path`, `operation`, `arguments`, `cwd`, `show_cmd` | [[1]](os.html#os.startfile) |
| os.symlink | `src`, `dst`, `dir_fd` | [[1]](os.html#os.symlink) |
| os.system | `command` | [[1]](os.html#os.system) |
| os.truncate | `fd`, `length` | [[1]](os.html#os.ftruncate)[[2]](os.html#os.truncate) |
| os.unsetenv | `key` | [[1]](os.html#os.unsetenv) |
| os.utime | `path`, `times`, `ns`, `dir_fd` | [[1]](os.html#os.utime) |
| os.walk | `top`, `topdown`, `onerror`, `followlinks` | [[1]](os.html#os.walk) |
| pathlib.Path.glob | `self`, `pattern` | [[1]](pathlib.html#pathlib.Path.glob) |
| pathlib.Path.rglob | `self`, `pattern` | [[1]](pathlib.html#pathlib.Path.rglob) |
| pdb.Pdb |  | [[1]](pdb.html#pdb.Pdb) |
| pickle.find\_class | `module`, `name` | [[1]](pickle.html#pickle.Unpickler.find_class) |
| poplib.connect | `self`, `host`, `port` | [[1]](poplib.html#poplib.POP3)[[2]](poplib.html#poplib.POP3_SSL) |
| poplib.putline | `self`, `line` | [[1]](poplib.html#poplib.POP3)[[2]](poplib.html#poplib.POP3_SSL) |
| pty.spawn | `argv` | [[1]](pty.html#pty.spawn) |
| resource.prlimit | `pid`, `resource`, `limits` | [[1]](resource.html#resource.prlimit) |
| resource.setrlimit | `resource`, `limits` | [[1]](resource.html#resource.setrlimit) |
| setopencodehook |  | [[1]](../c-api/file.html#c.PyFile_SetOpenCodeHook) |
| shutil.chown | `path`, `user`, `group` | [[1]](shutil.html#shutil.chown) |
| shutil.copyfile | `src`, `dst` | [[1]](shutil.html#shutil.copy)[[2]](shutil.html#shutil.copy2)[[3]](shutil.html#shutil.copyfile) |
| shutil.copymode | `src`, `dst` | [[1]](shutil.html#shutil.copy)[[2]](shutil.html#shutil.copymode) |
| shutil.copystat | `src`, `dst` | [[1]](shutil.html#shutil.copy2)[[2]](shutil.html#shutil.copystat) |
| shutil.copytree | `src`, `dst` | [[1]](shutil.html#shutil.copytree) |
| shutil.make\_archive | `base_name`, `format`, `root_dir`, `base_dir` | [[1]](shutil.html#shutil.make_archive) |
| shutil.move | `src`, `dst` | [[1]](shutil.html#shutil.move) |
| shutil.rmtree | `path`, `dir_fd` | [[1]](shutil.html#shutil.rmtree) |
| shutil.unpack\_archive | `filename`, `extract_dir`, `format` | [[1]](shutil.html#shutil.unpack_archive) |
| signal.pthread\_kill | `thread_id`, `signalnum` | [[1]](signal.html#signal.pthread_kill) |
| smtplib.connect | `self`, `host`, `port` | [[1]](smtplib.html#smtplib.SMTP.connect) |
| smtplib.send | `self`, `data` | [[1]](smtplib.html#smtplib.SMTP) |
| socket.\_\_new\_\_ | `self`, `family`, `type`, `protocol` | [[1]](socket.html#socket.socket) |
| socket.bind | `self`, `address` | [[1]](socket.html#socket.socket.bind) |
| socket.connect | `self`, `address` | [[1]](socket.html#socket.socket.connect)[[2]](socket.html#socket.socket.connect_ex) |
| socket.getaddrinfo | `host`, `port`, `family`, `type`, `protocol` | [[1]](socket.html#socket.getaddrinfo) |
| socket.gethostbyaddr | `ip_address` | [[1]](socket.html#socket.gethostbyaddr) |
| socket.gethostbyname | `hostname` | [[1]](socket.html#socket.gethostbyname)[[2]](socket.html#socket.gethostbyname_ex) |
| socket.gethostname |  | [[1]](socket.html#socket.gethostname) |
| socket.getnameinfo | `sockaddr` | [[1]](socket.html#socket.getnameinfo) |
| socket.getservbyname | `servicename`, `protocolname` | [[1]](socket.html#socket.getservbyname) |
| socket.getservbyport | `port`, `protocolname` | [[1]](socket.html#socket.getservbyport) |
| socket.sendmsg | `self`, `address` | [[1]](socket.html#socket.socket.sendmsg) |
| socket.sendto | `self`, `address` | [[1]](socket.html#socket.socket.sendto) |
| socket.sethostname | `name` | [[1]](socket.html#socket.sethostname) |
| sqlite3.connect | `database` | [[1]](sqlite3.html#sqlite3.connect) |
| sqlite3.connect/handle | `connection_handle` | [[1]](sqlite3.html#sqlite3.connect) |
| sqlite3.enable\_load\_extension | `connection`, `enabled` | [[1]](sqlite3.html#sqlite3.Connection.enable_load_extension) |
| sqlite3.load\_extension | `connection`, `path` | [[1]](sqlite3.html#sqlite3.Connection.load_extension) |
| subprocess.Popen | `executable`, `args`, `cwd`, `env` | [[1]](subprocess.html#subprocess.Popen) |
| sys.\_current\_exceptions |  | [[1]](sys.html#sys._current_exceptions) |
| sys.\_current\_frames |  | [[1]](sys.html#sys._current_frames) |
| sys.\_getframe | `frame` | [[1]](sys.html#sys._getframe) |
| sys.\_getframemodulename | `depth` | [[1]](sys.html#sys._getframemodulename) |
| sys.addaudithook |  | [[1]](../c-api/sys.html#c.PySys_AddAuditHook)[[2]](sys.html#sys.addaudithook) |
| sys.excepthook | `hook`, `type`, `value`, `traceback` | [[1]](sys.html#sys.excepthook) |
| sys.monitoring.register\_callback | `func` | [[1]](sys.monitoring.html#sys.monitoring.register_callback) |
| sys.remote\_exec | `pid` | [[1]](sys.html#script_path) |
| sys.set\_asyncgen\_hooks\_finalizer |  | [[1]](sys.html#sys.set_asyncgen_hooks) |
| sys.set\_asyncgen\_hooks\_firstiter |  | [[1]](sys.html#sys.set_asyncgen_hooks) |
| sys.setprofile |  | [[1]](sys.html#sys.setprofile) |
| sys.settrace |  | [[1]](sys.html#sys.settrace) |
| sys.unraisablehook | `hook`, `unraisable` | [[1]](sys.html#sys.unraisablehook) |
| syslog.closelog |  | [[1]](syslog.html#syslog.closelog) |
| syslog.openlog | `ident`, `logoption`, `facility` | [[1]](syslog.html#syslog.openlog) |
| syslog.setlogmask | `maskpri` | [[1]](syslog.html#syslog.setlogmask) |
| syslog.syslog | `priority`, `message` | [[1]](syslog.html#syslog.syslog) |
| tempfile.mkdtemp | `fullpath` | [[1]](tempfile.html#tempfile.TemporaryDirectory)[[2]](tempfile.html#tempfile.mkdtemp) |
| tempfile.mkstemp | `fullpath` | [[1]](tempfile.html#tempfile.NamedTemporaryFile)[[2]](tempfile.html#tempfile.TemporaryFile)[[3]](tempfile.html#tempfile.mkstemp) |
| time.sleep | `secs` | [[1]](time.html#audit_event_time_sleep_0) |
| urllib.Request | `fullurl`, `data`, `headers`, `method` | [[1]](urllib.request.html#urllib.request.urlopen) |
| webbrowser.open | `url` | [[1]](webbrowser.html#webbrowser.open) |
| winreg.ConnectRegistry | `computer_name`, `key` | [[1]](winreg.html#winreg.ConnectRegistry) |
| winreg.CreateKey | `key`, `sub_key`, `access` | [[1]](winreg.html#winreg.CreateKey)[[2]](winreg.html#winreg.CreateKeyEx) |
| winreg.DeleteKey | `key`, `sub_key`, `access` | [[1]](winreg.html#winreg.DeleteKey)[[2]](winreg.html#winreg.DeleteKeyEx) |
| winreg.DeleteValue | `key`, `value` | [[1]](winreg.html#winreg.DeleteValue) |
| winreg.DisableReflectionKey | `key` | [[1]](winreg.html#winreg.DisableReflectionKey) |
| winreg.EnableReflectionKey | `key` | [[1]](winreg.html#winreg.EnableReflectionKey) |
| winreg.EnumKey | `key`, `index` | [[1]](winreg.html#winreg.EnumKey) |
| winreg.EnumValue | `key`, `index` | [[1]](winreg.html#winreg.EnumValue) |
| winreg.ExpandEnvironmentStrings | `str` | [[1]](winreg.html#winreg.ExpandEnvironmentStrings) |
| winreg.LoadKey | `key`, `sub_key`, `file_name` | [[1]](winreg.html#winreg.LoadKey) |
| winreg.OpenKey | `key`, `sub_key`, `access` | [[1]](winreg.html#winreg.OpenKey) |
| winreg.OpenKey/result | `key` | [[1]](winreg.html#winreg.CreateKey)[[2]](winreg.html#winreg.CreateKeyEx)[[3]](winreg.html#winreg.OpenKey) |
| winreg.PyHKEY.Detach | `key` | [[1]](winreg.html#winreg.PyHKEY.Detach) |
| winreg.QueryInfoKey | `key` | [[1]](winreg.html#winreg.QueryInfoKey) |
| winreg.QueryReflectionKey | `key` | [[1]](winreg.html#winreg.QueryReflectionKey) |
| winreg.QueryValue | `key`, `sub_key`, `value_name` | [[1]](winreg.html#winreg.QueryValue)[[2]](winreg.html#winreg.QueryValueEx) |
| winreg.SaveKey | `key`, `file_name` | [[1]](winreg.html#winreg.SaveKey) |
| winreg.SetValue | `key`, `sub_key`, `type`, `value` | [[1]](winreg.html#winreg.SetValue)[[2]](winreg.html#winreg.SetValueEx) |

The following events are raised internally and do not correspond to any
public API of CPython:

| Audit event | Arguments |
| --- | --- |
| \_winapi.CreateFile | `file_name`, `desired_access`, `share_mode`, `creation_disposition`, `flags_and_attributes` |
| \_winapi.CreateJunction | `src_path`, `dst_path` |
| \_winapi.CreateNamedPipe | `name`, `open_mode`, `pipe_mode` |
| \_winapi.CreatePipe |  |
| \_winapi.CreateProcess | `application_name`, `command_line`, `current_directory` |
| \_winapi.OpenProcess | `process_id`, `desired_access` |
| \_winapi.TerminateProcess | `handle`, `exit_code` |
| \_posixsubprocess.fork\_exec | `exec_list`, `args`, `env` |
| ctypes.PyObj\_FromPtr | `obj` |

Added in version 3.14: The `_posixsubprocess.fork_exec` internal audit event.

#### Previous topic

[Debugging and Profiling](debug.html "previous chapter")

#### Next topic

[`bdb` — Debugger framework](bdb.html "next chapter")

### This page

* [Report a bug](../bugs.html)
* [Improve this page](../improve-page-nojs.html)
* [Show source](https://github.com/python/cpython/blob/main/Doc/library/audit_events.rst?plain=1)

«

### Navigation

* [index](../genindex.html "General Index")
* [modules](../py-modindex.html "Python Module Index") |
* [next](bdb.html "bdb — Debugger framework") |
* [previous](debug.html "Debugging and Profiling") |
* ![Python logo](../_static/py.svg)
* [Python](https://www.python.org/) »

* [3.14.3 Documentation](../index.html) »
* [The Python Standard Library](index.html) »
* [Debugging and Profiling](debug.html) »
* Audit events table
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
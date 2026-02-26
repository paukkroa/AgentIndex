---
id: 0.0.9.0.1
title: "contextvars— Context Variables¶"
nav_summary: "`contextvars` module: manage scoped context-local state safely via `ContextVar` and `Token`."
ref: https://docs.python.org/3/library/contextvars.html
ref_type: url
---

# contextvars— Context Variables¶

The `contextvars` module in Python (introduced in **3.7**) provides a robust mechanism for managing **context-local state** in concurrent applications, replacing traditional `threading.local()` for safer, scoped state handling. Central to this module is the **`ContextVar`** class, which declares a named variable tied to a specific execution context (e.g., async tasks, threads, or coroutines). Each `ContextVar` holds a **default value** (optional) and allows retrieval (`get()`) or modification (`set()`) of its value within the current context. Setting a value returns a **`Token`** object, enabling temporary overrides via context managers or explicit resets (`reset()`). The module also supports **context copying** (`copy_context()`) and **`Context`** objects for managing asynchronous frameworks. Key advantages include **preventing state leakage** across contexts and **garbage collection safety** (avoid creating `ContextVar` instances in closures). For deeper details, refer to **PEP 567**.

---

[Link to original](https://docs.python.org/3/library/contextvars.html)

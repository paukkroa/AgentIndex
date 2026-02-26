---
id: 0.0.4.1
title: "pickle— Python object serialization¶"
nav_summary: "`pickle`: Secure binary serialization for Python objects (use cautiously)."
ref: https://docs.python.org/3/library/pickle.html
ref_type: url
---

# pickle— Python object serialization¶

The `pickle` module in Python provides binary serialization (pickling) and deserialization (unpickling) mechanisms for converting Python object hierarchies into byte streams and vice versa. It supports complex data structures, including custom classes, with transparent serialization of instances, though class definitions must remain importable and accessible. Unlike the primitive `marshal` module (used for `.pyc` files), `pickle` ensures cross-version compatibility (backward and forward) for Python releases, handles Python 2/3 type differences, and supports arbitrary code execution during unpickling—**requiring strict security precautions** (e.g., avoiding untrusted data). Safer alternatives like `json` are recommended for untrusted data, though they lack support for Python-specific objects. Key protocols (e.g., Protocol 4) optimize performance and compatibility.

---

[Link to original](https://docs.python.org/3/library/pickle.html)

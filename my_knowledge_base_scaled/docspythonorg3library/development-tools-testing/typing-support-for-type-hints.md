---
id: 0.0.14.0
title: "typing— Support for type hints¶"
nav_summary: "`typing` module: Advanced type hints for static analysis."
ref: https://docs.python.org/3/library/typing.html
ref_type: url
---

# typing— Support for type hints¶

The `typing` module (introduced in Python 3.5) provides **runtime support for type hints**, enabling static type checking, IDE tooling, and linters to enforce type safety without runtime enforcement. It extends basic types like `float` or `str` with advanced constructs such as **type aliases** (using `type Vector = list[float]`), **generic types** (e.g., `list[T]`), **union types** (`Union[A, B]`), and **callable types** (`Callable[[T], R]`). While Python ignores type hints at runtime, tools like `mypy` leverage them for early bug detection. The module evolves frequently, with newer features backported via [`typing_extensions`](https://pypi.org/project/typing_extensions/). Key resources include the [Python Type System Specification](https://typing.python.org/spec/) and community-driven guides like the [Typing Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html).

---

[Link to original](https://docs.python.org/3/library/typing.html)

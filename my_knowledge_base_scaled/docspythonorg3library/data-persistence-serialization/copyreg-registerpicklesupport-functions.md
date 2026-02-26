---
id: 0.0.4.2
title: "copyreg— Registerpicklesupport functions¶"
nav_summary: "`copyreg`: Register custom pickle reduction functions for objects."
ref: https://docs.python.org/3/library/copyreg.html
ref_type: url
---

# copyreg— Registerpicklesupport functions¶

The `copyreg` module in Python’s standard library enables customization of the pickling process for non-class objects by registering reduction functions. It integrates with `pickle` and `copy` modules to define how specific objects are serialized/deserialized. Key functions include `copyreg.constructor()`, which validates constructors, and `copyreg.pickle(type, function, constructor_ob=None)`, which associates a reduction function with a type. The reduction function must return a string or tuple (2-6 elements) for reconstruction. This mechanism allows fine-grained control over object persistence, particularly for factory functions or instances lacking class definitions. The example demonstrates registering a custom `pickle` function for a class `C`, triggering it during `copy.copy()` and `pickle.dumps()` operations.

---

[Link to original](https://docs.python.org/3/library/copyreg.html)

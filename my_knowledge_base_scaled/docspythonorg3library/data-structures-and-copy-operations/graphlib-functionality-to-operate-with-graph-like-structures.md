---
id: 0.0.18.1
title: "graphlib— Functionality to operate with graph-like structures¶"
nav_summary: "`graphlib` module: Topological sorting for DAGs via `TopologicalSorter`."
ref: https://docs.python.org/3/library/graphlib.html
ref_type: url
---

# graphlib— Functionality to operate with graph-like structures¶

The `graphlib` module provides Python’s built-in functionality for manipulating graph-like structures, with a primary focus on **topological sorting** via the `TopologicalSorter` class. This class enables linear ordering of directed acyclic graph (DAG) nodes such that every directed edge `u → v` ensures `u` precedes `v` in the sequence. The graph is represented as a dictionary where keys are nodes and values are iterables of predecessors. Key methods include:
- **`add()`**: Dynamically inserts nodes/edges into the graph.
- **`prepare()`**: Initializes the sorting process.
- **`get_ready()`**: Retrieves nodes with no remaining dependencies (ready for processing).
- **`done()`**: Marks a node as processed.
- **`is_active()`**: Checks if sorting remains incomplete.
For static sorting (non-parallel), use `static_order()` for a direct topological sequence. The module supports parallel processing by decoupling node retrieval (`get_ready()`) from completion (`done()`), enabling distributed task execution.

---

[Link to original](https://docs.python.org/3/library/graphlib.html)

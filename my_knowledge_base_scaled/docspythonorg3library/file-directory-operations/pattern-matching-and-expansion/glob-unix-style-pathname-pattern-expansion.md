---
id: 0.0.3.3.0
title: "glob— Unix style pathname pattern expansion¶"
nav_summary: "The `glob` module in Python implements Unix-style pathname pattern expansion without invoking a subshell, leveraging `os"
ref: https://docs.python.org/3/library/glob.html
ref_type: url
---

# glob— Unix style pathname pattern expansion¶

The `glob` module in Python implements Unix-style pathname pattern expansion without invoking a subshell, leveraging `os.scandir()` and `fnmatch.fnmatch()` for efficient matching. It supports wildcards (`*`, `?`) and character ranges (`[abc]`) in pathnames, returning unordered lists of matching files/directories. Key features include:
- **Pattern Matching**: Supports `*`, `?`, and `[seq]` (e.g., `[0-9]`) for globs, with literal meta-characters escaped via brackets (e.g., `'[?]'`).
- **Recursive Search**: The `**` wildcard recursively traverses directories (enabled via `recursive=True`), including hidden files if `include_hidden=True`.
- **Root Directory Control**: Specify a root directory (`root_dir`) or file descriptor (`dir_fd`) to constrain searches.
- **Symlink Handling**: Broken symlinks are included in results, mirroring shell behavior.
- **Limitations**: Hidden files (e.g., `.gitignore`) require explicit dot-prefixed patterns; no tilde expansion (use `os.path.expanduser()` for home dirs). For sorted results, manually sort the output.

**

[Link to original](https://docs.python.org/3/library/glob.html)

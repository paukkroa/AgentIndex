---
id: 0.0.10.4.4
title: "urllib.robotparser—  Parser for robots.txt¶"
nav_summary: "`urllib.robotparser: Parse robots.txt rules for URL access."
ref: https://docs.python.org/3/library/urllib.robotparser.html
ref_type: url
---

# urllib.robotparser—  Parser for robots.txt¶

The `urllib.robotparser` module provides the **`RobotFileParser`** class, a tool for parsing and querying `robots.txt` files to determine whether a specific user agent is permitted to access a given URL. It adheres to the [robots.txt specification](http://www.robotstxt.org/orig.html) and supports core functionalities like setting the target URL, reading and parsing the file, and checking fetch permissions (`can_fetch`). Additional features include tracking the last modification time (`mtime`, `modified`), enforcing crawl delays (`crawl_delay`), managing request rates (`request_rate`), and listing sitemaps (`site_maps`). Introduced in Python 3.6+, it enables web crawlers to respect website restrictions while dynamically updating rules via `modified()`.

[Link to original](https://docs.python.org/3/library/urllib.robotparser.html)

---
id: 0.0.16.3
title: "ipaddress— IPv4/IPv6 manipulation library¶"
nav_summary: "The `ipaddress` module in Python (introduced in **Python 3"
ref: https://docs.python.org/3/library/ipaddress.html
ref_type: url
---

# ipaddress— IPv4/IPv6 manipulation library¶

The `ipaddress` module in Python (introduced in **Python 3.3**) provides a robust library for **IPv4/IPv6 address and network manipulation**, enabling creation, validation, and operations like subnet checks, host iteration, and network segmentation. It offers **three primary factory functions**:
- `ip_address()`: Constructs `IPv4Address` or `IPv6Address` objects from strings/integers (e.g., `'192.168.0.1'` or `'2001:db8::'`), with automatic IPv4/IPv6 detection for integers < `2**32`.
- `ip_network()`: Generates `IPv4Network` or `IPv6Network` objects (e.g., `'192.168.0.0/28'`), validating network prefixes and rejecting host-bit-set addresses. The `strict` parameter enforces strict CIDR compliance.
- `ip_interface()`: Creates `IPv4Interface`/`IPv6Interface` objects for hybrid IP/prefix configurations (e.g., `'192.168.1.1/24'`).

Key features include **

[Link to original](https://docs.python.org/3/library/ipaddress.html)

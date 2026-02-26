---
id: 0.0.11.2
title: "colorsys— Conversions between color systems¶"
nav_summary: "`colorsys` – RGB ↔ YIQ/HLS/HSV conversions."
ref: https://docs.python.org/3/library/colorsys.html
ref_type: url
---

# colorsys— Conversions between color systems¶

The `colorsys` module in Python’s standard library provides bidirectional conversion functions between **RGB (Red-Green-Blue)** and three alternative color spaces: **YIQ** (used in analog television), **HLS (Hue-Lightness-Saturation)**, and **HSV (Hue-Saturation-Value)**. All coordinates are normalized floating-point values between **0.0 and 1.0**, except YIQ’s **I/Q** components, which can be negative. Functions include `rgb_to_yiq()`/`yiq_to_rgb()`, `rgb_to_hls()`/`hls_to_rgb()`, and `rgb_to_hsv()`/`hsv_to_rgb()`, enabling seamless interoperability for graphics, image processing, and visualization tasks. Example usage demonstrates round-trip conversions between RGB and HSV/HLS.

---

[Link to original](https://docs.python.org/3/library/colorsys.html)

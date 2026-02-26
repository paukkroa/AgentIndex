---
id: 0.0.11.1
title: "wave— Read and write WAV files¶"
nav_summary: "The `wave` module in Python’s standard library provides a high-level interface for reading and writing **uncompressed PCM-encoded WAV files**, adherin"
ref: https://docs.python.org/3/library/wave.html
ref_type: url
---

# wave— Read and write WAV files¶

The `wave` module in Python’s standard library provides a high-level interface for reading and writing **uncompressed PCM-encoded WAV files**, adhering to the Waveform Audio (WAV) format specification. Introduced in Python 3.12, it now supports **`WAVE_FORMAT_EXTENSIBLE` headers** for PCM data (`KSDATAFORMAT_SUBTYPE_PCM`). The module’s core functionality revolves around the `wave.open()` function, which accepts either a file path (string) or a file-like object for reading (`'rb'`) or writing (`'wb'`). It returns `Wave_read` or `Wave_write` objects, respectively, enabling metadata retrieval (e.g., channels, sample width, frame rate) and audio data manipulation. Key methods include `getnchannels()`, `getframerate()`, and `getnframes()`, while exceptions like `wave.Error` signal violations of WAV specifications. The module supports **context managers** (`with` statements) for automatic resource cleanup and handles **unseekable files** (since Python 3.4). Notably, it **exclusively supports uncompressed audio** and lacks read/write mode support.

---
**NAV

[Link to original](https://docs.python.org/3/library/wave.html)

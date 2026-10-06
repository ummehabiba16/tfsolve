---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A small allocation unit makes the bitmap large and the search for free runs slow; a large unit makes the bitmap small but wastes memory through internal fragmentation."
sources: ["Tanenbaum MOS 4e, sec. 3.2.3 (memory management with bitmaps)"]
---
With a **bitmap**, memory is divided into **allocation units** and one bit per unit says free (0) or used (1). The unit size is a design trade-off:

- **Small allocation unit** (e.g. 4 bytes): little wasted space inside the last unit of each process (small internal fragmentation), but the **bitmap becomes large**: with 4-byte units one bit per 32 bits wastes $1/33$ of memory ($\approx3\%$) on the map; and the **search for a run of $k$ consecutive 0 bits** is slow (long map, runs that cross word boundaries).
- **Large allocation unit** (e.g. 4 KB): the **bitmap is tiny** and searching is fast, but on average **half a unit per process is wasted** (internal fragmentation), which can be significant for small processes.

The size should be chosen according to the typical process size and the memory available: small enough that the average waste is acceptable, large enough that the bitmap does not take too much memory or search time.

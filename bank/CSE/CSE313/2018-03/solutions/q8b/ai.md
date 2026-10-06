---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Use multilevel page tables when the address space is large and sparsely used (e.g. a process using 12 MB of a 4 GB space needs 16 KB of tables instead of 4 MB)."
sources: ["Tanenbaum MOS 4e, sec. 3.3.2"]
---
**Scenario.** A system with a large virtual address space (32 or 64 bits) in which each process uses only a small, scattered part of it (code at the bottom, heap above it, stack at the top, with a big unused gap in between), and many processes run at the same time.

With 4 KB pages and 4-byte entries a **single-level** table for a 32-bit space needs $2^{20}$ entries $=4$ MB *per process*, even if the process uses only 12 MB of memory. With a **two-level** table (10+10+12 bits) the same process needs one top-level table (4 KB) and only the second-level tables for the regions in use (3 regions of 4 MB $\Rightarrow$ 3 tables of 4 KB), i.e. $4\times4$ KB $=16$ KB.

For a 64-bit address space a single-level table is impossible at all, so multilevel (or inverted) tables are required.

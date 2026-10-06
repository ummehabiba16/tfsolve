---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Too large a page wastes memory (internal fragmentation, unused data loaded); too small a page enlarges the page table and makes transfers inefficient."
sources: ["Tanenbaum MOS 4e, sec. 3.5.1 (page size)"]
---
- **Page size too large:** **internal fragmentation**: on average half a page of every process segment is wasted; more **unneeded data** is loaded into memory with each page (it may hold only a little useful data), so fewer useful pages fit in memory and more page faults can occur; page-in/out of big pages takes longer.
- **Page size too small:** the **page table becomes large** (more entries per process) and more **TLB entries** are needed, so more TLB misses; **disk transfers are inefficient** because the seek and rotational delay (about 10 ms) dominate the transfer time of a small page; more page faults for sequential access.

The optimum minimises the sum of the page-table overhead and the fragmentation: $p=\sqrt{2se}$ ($s$ = average process size, $e$ = page-table entry size); typical sizes are 4 KB to 64 KB.

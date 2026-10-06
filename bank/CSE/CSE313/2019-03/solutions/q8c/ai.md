---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "File-system consistency check: build two per-block counter tables (blocks in files, blocks in the free list); every block must have 1 in exactly one table."
sources: ["Tanenbaum MOS 4e, sec. 4.4.5 (file-system consistency)"]
---
**Block-consistency check** (as done by `fsck`):

1. Build **two tables of counters**, one counter per block, initially $0$.
2. **Table 1** ("in use"): read every **i-node** and, for each block it addresses (including indirect blocks), increment that block's counter.
3. **Table 2** ("free"): read the **free list** (or bitmap) and increment the counter of each block listed there.

In a consistent file system every block has **exactly one 1**, either in the used table or in the free table:

| (in use, free) | Meaning | Action |
|:-:|:--|:--|
| (1, 0) or (0, 1) | consistent | none |
| (0, 0) | **missing block** (lost) | add it to the free list |
| (0, 2) | block **twice in the free list** (only possible with a list) | rebuild the free list |
| (1, 1) | block **both in a file and free** | remove it from the free list |
| (2, 0) or more | block **in two (or more) files** | allocate a free block, copy the data and give each file its own copy (one file will probably be garbled; the system reports the error) |

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Not directly: page faults depend on which pages are resident, not on the table structure; the saved memory can hold more pages (fewer faults), but pageable page-table pages can add faults."
sources: ["Tanenbaum MOS 4e, sec. 3.3.2"]
---
**Not directly.** A page fault occurs when the page referenced is not in main memory. This depends on the replacement policy, the amount of memory and the program's locality, not on how the page table is organised; a multilevel table is only a different data structure that maps the same pages to frames.

- **Possible indirect gain:** the memory saved by not allocating page-table space for unused regions can be used for more user pages, which may lower the page-fault rate.
- **Possible loss:** the lower-level page-table pages may themselves be swapped out, so a reference can cause an additional fault to bring in the *page table page* before the page itself can be located; the TLB hides this cost in the common case but cannot remove it.

So multilevel tables are for **saving space**, not for reducing page faults.

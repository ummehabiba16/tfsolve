---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Only some regions can change size: the stack grows automatically on overflow and the data region grows with brk/sbrk; the text region (and shared memory) is fixed because it is read-only/shared and mapped once."
sources: ["Bach, ch. 6 (regions; algorithm growreg)"]
---
`growreg` increases or decreases the size of a region by allocating/freeing pages and adjusting the page table. Whether it may be used depends on the **kind of region**:

| Region | Can its size change? | Why / how |
|:--|:--|:--|
| **Stack** | **Yes** | grows automatically: when the process overflows the stack, the resulting fault makes the kernel call `growreg` and the stack is extended (the amount of stack in use is not known in advance) |
| **Data (heap)** | **Yes** | grows or shrinks explicitly with the `brk`/`sbrk` system calls (used by `malloc`) |
| **Text (code)** | **No** | read-only, its size is fixed by the executable file and it may be **shared** by several processes running the same program; changing its size would affect all sharers |
| **Shared memory** | **No** (after attach) | its size is fixed when created; all attached processes see the same pages |

**Example.** A process calling `sbrk(4096)` grows the data region by one page; recursion that uses more stack than allocated grows the stack region. A write beyond the end of the text region is a protection violation, not an extension.

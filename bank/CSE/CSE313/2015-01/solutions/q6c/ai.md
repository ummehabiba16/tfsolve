---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Give each process a fixed contiguous swap area at creation; the disk address of a page is the area's start address plus the page number times the page size, so only one number per process is kept in memory."
sources: ["Tanenbaum MOS 4e, sec. 3.6.3 (backing store: static swap area)"]
---
When each process needs a **fixed amount of memory**, a **static swap area** can be reserved for it:

- When the process is created, a **contiguous area on the disk, as large as the process's address space,** is allocated in the swap area (a partition).
- The **disk address of the area** (a single number) is stored in the **process table**.
- To swap page $k$ out or in, the kernel computes its disk address as

$$\text{address}(P,k)=\text{swap area start of }P+k\times\text{page size}$$

so **no table of per-page disk addresses is needed**, and nothing but one number per process uses main memory. Pages go back to the same place every time (no fragmentation search); when the process terminates, the area is freed.

![Static swap area](figures/swap.png)

*Drawback:* the whole space is reserved even for pages never used, and the swap area must be at least as large as the sum of the address spaces.

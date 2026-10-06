---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Paging shows the programmer one linear address space; segmentation shows several independent segments addressed by (segment, offset)."
sources: ["Tanenbaum MOS 4e, sec. 3.7 (segmentation) and 3.3 (paging)"]
---
![Memory models seen by the programmer with paging and with segmentation](figures/models.png)

- **Paging:** the programmer sees **one linear (one-dimensional) virtual address space**, an array of bytes numbered $0\ldots2^n-1$ that holds code, data and stack together; the division into fixed-size pages is invisible and done by the system. An address is a single number.
- **Segmentation:** the programmer sees a **collection of independent segments** (code, data, stack, tables), each with its own linear space starting at 0 and its own size, which can grow or shrink separately. An address is **two-dimensional**: (segment number, offset).

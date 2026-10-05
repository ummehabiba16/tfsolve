---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Physical: 4 GB (32-bit address bus, 80386DX). Virtual: 64 TB = 16K segments x 4 GB each (8K GDT + 8K LDT descriptors). Selector -> descriptor -> 32-bit base + 32-bit offset gives a linear address in 4 GB; paging (4 KB pages, page directory/tables) maps linear to physical and swaps pages to disk."
sources: ["MHE 80386-updated slides 4, 16-23 (4 GB physical, 16K segments x 4 GB = 64 TB virtual, segmentation then paging)"]
---
**Physical memory: 4 GB.** The 80386DX has a **32-bit address bus**, so it can address $2^{32}$ bytes = **4 GB** of physical memory. (The 80386SX has 24 address lines: 16 MB.)

**Virtual memory: 64 TB.** A program can use **16K segments** (8K through the GDT + 8K through its LDT), and each segment can be up to **4 GB** (32-bit offset, limit up to 4 GB with G = 1):

$$16\text{K} \times 4\ \text{GB} = 2^{14} \times 2^{32} = 2^{46}\ \text{bytes} = \mathbf{64\ TB}$$

**How they are addressed**

1. **Segmentation:** the selector in a segment register picks a descriptor in the GDT or LDT. Its **32-bit base** plus the **32-bit offset** (after limit and privilege checks) gives a 32-bit **linear address** in a 4 GB linear space.
2. **Paging** (if PG = 1): the linear address is split 10 + 10 + 12 bits; through the page directory (CR3) and a page table it is mapped to a 4 KB **physical page frame**. Pages that are not in memory are marked not present; accessing them causes a page fault, and the OS loads the page from disk. In this way the large virtual space is supported by a smaller physical memory plus disk storage. (Without paging, linear = physical.)

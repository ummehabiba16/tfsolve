---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Segmentation gives separate, growable, shareable and protectable logical address spaces; MULTICS pages each segment: segment number indexes the (paged) descriptor segment, page number indexes the segment's page table."
sources: ["Tanenbaum MOS 4e, sec. 3.7.2 (segmentation with paging: MULTICS)"]
---
**Advantages of segmentation over paging**

- A segment is a **logical unit** (procedure, array, stack) with its **own address space**; several segments can grow or shrink independently without colliding (no compile-time layout problems like the "fixed table" problems).
- **Sharing** and **protection** are simple and natural: a shared library is one segment; each segment has its own protection (read-only code, read/write data, execute-only), and the programmer knows the unit.
- **Linking** is easier: procedures in separate segments can be recompiled without re-addressing others.
- No *internal* fragmentation (but external fragmentation appears; paging has the opposite property).

**MULTICS: segmentation with paging.** The virtual address has a 34-bit format: **segment number (18 bits)**, **page number (6 bits)**, **offset (10 bits)** within a 1024-word page.

![MULTICS address translation](figures/multics.png)

1. The segment number indexes the **descriptor segment** (a segment holding the segment descriptors of the process, which is itself paged); the **segment descriptor** gives the address of the segment's **page table**, the segment length and protection bits.
2. The page number indexes the **page table of that segment**, giving the page frame number.
3. The frame number is combined with the 10-bit offset to form the physical address.

To avoid the two extra memory references, MULTICS uses a small fast associative memory (a TLB of 16 words) holding the most recently used (segment, page) translations.

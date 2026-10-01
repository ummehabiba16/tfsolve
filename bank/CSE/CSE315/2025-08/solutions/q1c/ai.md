---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Virtual memory of 80386 = 16K segments x 4GB = 64TB. Paging is needed because swapping whole segments of up to 4GB is too slow. The linear address is split 10/10/12 into directory/table/offset, starting from CR3."
sources: ["MHE 80386-updated slides 4, 21-26 (virtual memory, paging, worked example)"]
---
**Total virtual memory of the 80386**

- A segment can be as large as $2^{32}$ B = 4GB (32-bit offset).
- The 16-bit selector has 13 index bits plus the TI bit (GDT or LDT), so a program can use $2^{13}\times2 = 2^{14}$ = 16K segments.

$$\text{Virtual memory} = 2^{14}\times 2^{32} = 2^{46}\text{ B} = \mathbf{64\,TB}$$

**Why paging is needed**

- With segmentation alone, the unit of swapping is a whole segment, which can be up to 4GB. Swapping such segments between disk and physical memory takes far too long.
- Paging divides the 4GB linear space into **1M pages of 4KB**. Only the pages actually needed are kept in memory and swapped in and out, so swapping is fast and memory is not fragmented by large segments.

**Linear to physical address translation (paging enabled: MSB of CR0 = 1)**

The segmentation unit first gives the 32-bit linear address: base from the descriptor plus offset. It is split into 3 fields:

```text
 31            22 21            12 11             0
+----------------+----------------+----------------+
|   Directory    |   Page table   |     Offset     |
|   (10 bits)    |   (10 bits)    |   (12 bits)    |
+----------------+----------------+----------------+
```

1. **CR3** holds the starting address of the single page directory (1K entries of 4 bytes).
2. Page directory entry address $= CR3 + \text{Directory}\times4$. Its upper 20 bits give the start of a page table.
3. Page table entry address $= \text{page table base} + \text{Page table}\times4$. Its upper 20 bits give the start of the 4KB page frame.
4. Physical address $=$ page frame base $+$ 12-bit Offset.

The **TLB** caches the 32 most recently used page translations, so most accesses skip the two table reads.

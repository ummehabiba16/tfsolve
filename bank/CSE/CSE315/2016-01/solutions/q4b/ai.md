---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Same 4 KB, two-level (directory + table) paging as the 80386, but the Pentium adds 4 MB pages: with PSE = 1 in CR4 and PS = 1 in a page directory entry, the PDE maps a 4 MB page directly (10-bit directory index + 22-bit offset, no page table). It has separate TLBs for code and data (and for 4 KB and 4 MB pages) instead of the 386's single 32-entry TLB."
sources: ["Brey, The Intel Microprocessors, Ch. 18 (Pentium memory management: 4 MB paging, CR4, TLBs)", "MHE 80386-updated slides 21-24 (80386 paging and TLB)"]
---
**80386 paging:** fixed **4 KB pages**; every translation uses two levels: page directory (CR3) $\to$ page table $\to$ page frame; linear address split 10 + 10 + 12; one **32-entry TLB**.

**Pentium paging differences**

1. **4 MB pages (page size extension).** The Pentium adds control register **CR4**. If **PSE = 1** in CR4 and the **PS bit = 1** in a page directory entry, that PDE points **directly to a 4 MB page**; there is **no page table** for it. The linear address is then split:

```text
 4 KB page (as 80386):  | directory (10) | table (10) | offset (12) |
 4 MB page (Pentium):   | directory (10) |       offset (22)        |
```

   This saves page-table memory and table walks for large regions such as the OS kernel or video memory. 4 KB and 4 MB pages can be mixed.

2. **Separate TLBs.** The Pentium has a code TLB and a data TLB (data TLB: 64 entries for 4 KB pages and 8 entries for 4 MB pages; code TLB: 32 entries), so instruction fetch and data access can be translated in the same clock for the two pipelines.
3. The page-table entry format is otherwise the same as the 80386 (present, R/W, U/S, accessed, dirty), with added cache-control bits (PCD, PWT) for its write-back cache.

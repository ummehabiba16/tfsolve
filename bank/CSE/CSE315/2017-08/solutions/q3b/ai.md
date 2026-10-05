---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "The TLB is a small cache inside the 80386 paging unit holding the 32 most recently used page translations (linear page number -> page frame, with attributes). On each access it is checked first: a hit gives the physical frame at once; a miss makes the processor read the page directory and page table and store the new entry. It avoids two extra memory reads per access; loading CR3 flushes it."
sources: ["MHE 80386-updated slide 24 (Translation Look-aside Buffer)", "Brey, The Intel Microprocessors, Sec. 2-4 (TLB)"]
---
**What it is.** The **Translation Look-aside Buffer (TLB)** is a small, fast, special cache inside the 80386 paging unit. It stores the **page addresses of the 32 most recently accessed pages**: for each, the upper 20 bits of the linear address (page number) and the matching page-frame address with its attribute bits (on the 80386: 4-way set associative, 32 entries, covering 128 KB).

**Why it is needed.** Without it, every memory access with paging would need **two extra memory reads** (page directory entry and page table entry) before the operand itself, roughly tripling memory access time.

**How it is used**

1. For every memory access the paging unit first looks up the linear page number in the TLB.
2. **Hit** (about 98% of accesses for typical programs): the page frame address comes straight from the TLB, and physical address = frame + 12-bit offset, with no table reads.
3. **Miss:** the processor reads the PDE (via CR3) and the PTE, forms the physical address, and stores the new translation in the TLB, replacing an old entry.
4. When the page tables change, the OS must **flush** the TLB (loading CR3 flushes it), otherwise stale translations would be used.

```text
linear page no. --> [ TLB: 32 entries ] --hit--> frame address --> + offset --> physical
                          | miss
                          v
               read PDE (CR3 + 4 x dir), read PTE --> frame; store in TLB
```

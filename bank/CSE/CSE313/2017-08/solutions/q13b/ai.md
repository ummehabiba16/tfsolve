---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "TLB = small associative hardware cache of recent page-number to frame mappings; the MMU searches it in parallel and only on a miss walks the page table."
sources: ["Tanenbaum MOS 4e, sec. 3.3.3 (TLBs)"]
---
**TLB (translation lookaside buffer):** a small, fast **associative memory** inside the MMU that stores the translations (virtual page number $\to$ page frame, plus protection and valid bits) of the **most recently used pages**. It exists because a page-table lookup needs an extra memory access for every reference, and programs have strong locality, so a small number of entries (typically 8-256) gives a **hit ratio above 90%**.

**How it functions.**

1. The CPU generates a virtual address; the MMU sends the **virtual page number to the TLB**, which compares it with **all its entries in parallel**.
2. **TLB hit** (match found and protection OK): the frame number is read from the entry and combined with the offset to form the physical address, with no page-table access.
3. **TLB miss:** the MMU (or the OS) **walks the page table** in memory; if the page is present, the translation is loaded into the TLB, **replacing** another entry, and the instruction is retried; if the page is not present, a **page fault** occurs.
4. On a **context switch** the TLB is flushed (or entries carry an address-space identifier).

The effective access time is $h\cdot t_{TLB+mem}+(1-h)\cdot(\ldots+\text{page-table access})$, close to one memory access when $h$ is high.

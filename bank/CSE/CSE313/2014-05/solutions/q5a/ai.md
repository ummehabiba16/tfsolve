---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Speed up paging with a TLB: a small associative cache of recent translations avoids the extra memory access to the page table on a hit."
sources: ["Tanenbaum MOS 4e, sec. 3.3.3 (speeding up paging: TLBs)"]
---
**Problem.** With the page table in main memory, every virtual address needs **two memory accesses**: one to read the page-table entry, one for the data. This halves the speed of the machine.

**Solution: a translation lookaside buffer (TLB)**, a small associative memory in the MMU that holds the translations of the most recently used pages (virtual page $\to$ page frame, with protection bits), exploiting **locality of reference**.

![TLB, page table and physical memory](figures/tlbflow.png)

1. The virtual page number is looked up **in parallel in all TLB entries**.
2. **Hit:** the frame number comes from the TLB, so the data is accessed with **one** memory reference.
3. **Miss:** the page table is read from memory (extra reference), the translation is **loaded into the TLB** (replacing an old entry), and the access completes.

With hit ratio $h$, TLB time $t$ and memory time $m$, the effective access time is $h(t+m)+(1-h)(t+2m)$; e.g. $h=0.98$, $t=1$ ns, $m=100$ ns gives about $103$ ns instead of $200$ ns. On a context switch the TLB is flushed (or tagged with a process ID). Other ways to speed up paging: multilevel tables (smaller tables), inverted page tables with a hash.

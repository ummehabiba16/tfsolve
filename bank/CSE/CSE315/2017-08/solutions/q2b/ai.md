---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Identity mapping: page tables set so that each linear page maps to the physical page with the same address (linear = physical). Uses: the code that turns paging on keeps running at the same addresses; the OS can reach page tables, DMA buffers and memory-mapped I/O at their physical addresses; simple/flat systems and real-mode style programs can run with paging protection."
sources: ["Intel 80386 Programmer's Reference Manual, Sec. 10.4 (identity mapping when enabling paging)", "MHE 80386-updated slides 21-23 (paging)"]
---
**Identity mapping** means building the page directory and page tables so that a range of linear pages is mapped to **physical pages with the same addresses**: page frame base = linear page base, so

$$\text{physical address} = \text{linear address}$$

for that range (e.g. the first 4 MB: PTE $i$ points to frame $i \times 4\text{K}$).

**Uses**

1. **Turning paging on.** After `MOV CR0` sets PG, the next instruction is fetched through the page tables. If the code that enables paging is identity-mapped, it continues at the same physical place; otherwise the processor would jump to an unrelated page. The same holds when paging is turned off.
2. **Access to physical structures.** The OS can use the physical addresses of page tables, DMA buffers (DMA controllers use physical addresses) and memory-mapped I/O devices directly, without translating them.
3. **Simple systems.** A small embedded or single-task system can run with "linear = physical" (together with a flat segment model) and still use paging's per-page protection (read-only, supervisor-only, not-present pages for catching bad pointers).

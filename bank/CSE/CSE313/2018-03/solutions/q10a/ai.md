---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Paging with a multilevel (or inverted) page table and a TLB: any size and number of processes, per-process page tables for protection and relocation; a 64-bit space needs hierarchical or inverted tables."
sources: ["Tanenbaum MOS 4e, sec. 3.3 (virtual memory: page tables, TLBs, inverted page tables)"]
---
**Requirements:** 8 GB of physical memory, 64-bit virtual addresses, any number of processes of arbitrary size, with **protection** (a process cannot touch others) and **relocation** (a process can be loaded anywhere).

**Technique chosen: demand-paged virtual memory** with **hierarchical (multilevel) page tables** and a **TLB**.

- **Relocation:** the virtual address space of each process is divided into fixed-size pages (4 KB) that can be mapped to *any* frame; no contiguous memory is needed, so there is no external fragmentation and processes of any size (even larger than 8 GB of RAM, via demand paging) can run.
- **Protection:** each process has its **own page table**, so it can only address the frames mapped into it; per-page bits (read/write/execute, user/supervisor) give fine-grained protection, and the page-table base register is writable only in kernel mode.
- **64-bit address space:** a single-level table is impossible ($2^{52}$ entries for 4 KB pages), so use a **multilevel table** (e.g. four levels of 9 bits as in x86-64), whose lower levels are allocated only for the regions in use; or an **inverted page table** with one entry per physical frame ($8\text{ GB}/4\text{ KB}=2^{21}$ entries $\approx$ 32 MB in total), searched through a hash table, which has size independent of the number of processes.
- **Speed:** a **TLB** caches recent translations so most references need no table walk.

**Why not the alternatives:** base/limit registers need contiguous memory and suffer from fragmentation and swapping of whole processes; plain segmentation has external fragmentation. Paging gives the most robust solution.

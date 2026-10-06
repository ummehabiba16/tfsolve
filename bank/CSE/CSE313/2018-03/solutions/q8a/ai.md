---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A multilevel page table splits the page number into several fields and allocates lower-level tables only for used regions."
sources: ["Tanenbaum MOS 4e, sec. 3.3.2 (multilevel page tables)"]
---
A **multilevel page table** organises the page table as a **tree** instead of one big array. The virtual page number is split into several fields; the first indexes the **top-level table**, whose entries point to **second-level tables**, and so on; the last field indexes a table whose entry holds the page frame number.

Example for a 32-bit address with 4 KB pages: PT1 (10 bits), PT2 (10 bits), offset (12 bits).

![Two-level page table](figures/twolevel.png)

Second-level tables are **allocated only for the regions of the address space that are in use** (and can themselves be paged out), so a process that uses little memory needs only a small amount of page-table memory.

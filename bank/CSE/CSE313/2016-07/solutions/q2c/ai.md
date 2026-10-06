---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Save/restore: base and bounds registers; segment table pointer and length; page table pointer (and flush or tag the TLB); the tables stay in memory."
sources: ["Anderson and Dahlin, OSPP, ch. 8-9 (base and bound, segmentation, paging)"]
---
In every case the **general registers, PC, stack pointer and status** are saved/restored too; what differs is the *memory-management state*.

| Memory management | Saved on the switch-out | Restored on the switch-in | Notes |
|:--|:--|:--|:--|
| **(i) virtually addressed base and bounds** | the **base** and **bounds (limit)** registers | the next process's base and bounds | just two registers; the process's memory itself stays where it is |
| **(ii) segmentation** | the **segment-table base register** and **length** (pointer to the segment table; for a small table the **segment registers**) | those of the next process | the segment table is kept in memory (in the PCB), only the pointer is switched; a **TLB/segment-register flush** may be needed |
| **(iii) paging** | the **page-table base register (PTBR)** and **length** | the next process's PTBR | the page tables stay in memory; the **TLB is flushed** (or entries are tagged with the process id/ASID so no flush is needed) |

The big memory contents (the program, data, page tables) are **not copied**: only the pointers/registers that locate them are switched.

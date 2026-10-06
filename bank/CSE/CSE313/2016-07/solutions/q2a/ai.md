---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Privileged: (ii) setting up a page table and (iii) halt; the register add (i) is not privileged."
sources: ["Anderson and Dahlin, OSPP, ch. 2 (hardware support: privileged instructions)"]
---
**Privileged instructions** can be executed only in **kernel mode**; in user mode they cause an exception. They are the instructions that could break protection or affect the whole machine: changing the memory-management registers/page tables, I/O instructions, disabling interrupts, halting the CPU, switching mode.

| Instruction | Privileged? | Reason |
|:--|:-:|:--|
| (i) add two registers, store in a third | **No** | affects only the process's own registers; harmless |
| (ii) set up a page table for a process | **Yes** | decides which physical memory a process can access; a user program could map anyone's memory |
| (iii) put the CPU in idle state with `halt` | **Yes** | would stop the machine for all other processes |

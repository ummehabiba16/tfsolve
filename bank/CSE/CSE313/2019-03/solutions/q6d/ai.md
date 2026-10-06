---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A context switch saves/restores registers and the PCB, runs the scheduler, changes the address space (MMU/TLB flush) and loses cache contents; threads of one process share the address space so switching between them avoids the memory-map change."
sources: ["Tanenbaum MOS 4e, sec. 2.1.6 and 2.2 (context switching, threads)"]
---
**Why a (process) context switch is expensive.**

- It needs a **trap into the kernel**, saving the old process's registers, program counter and status in its PCB, and running the **scheduler** to choose the next process.
- The kernel must **switch the address space**: load the new page-table base register, which invalidates the **TLB** (or tags have to be managed); the new process starts with many TLB misses.
- **Caches** (instruction and data caches, branch predictors) contain the old process's data, so the new process suffers cache misses (a *cold* cache); a pipeline flush also occurs.
- The new process's registers are restored and the mode is switched back to user mode.

**How threads help.** Threads of the same process **share the address space** (code, data, heap, open files). A switch between two threads of one process only needs to save and restore the registers, program counter and stack pointer: **no change of the page tables, no TLB flush, and the cache stays warm**. With user-level threads, the switch is even a procedure call in user space (no trap). So thread switching is much cheaper than process switching (and communication between threads uses shared memory directly).

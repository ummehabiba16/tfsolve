---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) a zombie has exited and awaits its parent's wait; (ii) the dynamic part of the system-level context is the stack of kernel context layers; (iii) memory-mapped I/O maps device registers into the address space."
sources: ["Bach, ch. 6 (zombie state; process context)", "Tanenbaum MOS 4e, sec. 5.1.3"]
---
**(i) Zombie state of a process in UNIX.** A process that has called `exit` is in the **zombie** state: it has released its memory and most resources, but its **process-table entry remains** and holds the exit status and the accounting information (CPU times) until the **parent executes `wait`** to collect them. If the parent does not wait, the zombie stays; if the parent dies first, `init` adopts and reaps it.

**(ii) Dynamic part of the system-level context of a process.** The system-level context consists of a *static* part (the process-table entry, the u area, and the region/page-table information that define the process) and a *dynamic* part: a **stack of context layers**. Each layer holds the information needed to recover the previous layer: the saved registers, program counter and kernel stack frames at the moment of an interrupt, system call or context switch. The kernel **pushes** a layer on these events (e.g. when an interrupt arrives while the process is in the kernel) and **pops** it on return, so the number of layers changes dynamically while the process runs.

**(iii) Memory-mapped I/O.** The registers and buffers of I/O devices are mapped into the **ordinary address space**, so they are read and written with normal `LOAD`/`STORE` instructions instead of special I/O instructions (`IN`/`OUT`); drivers can be written in C and protection is done with the page tables, but the device pages must not be cached and every memory access must be checked against the device addresses.

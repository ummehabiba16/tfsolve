---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Real mode: the 386 as a fast 8086 after reset, 1 MB, no protection or paging, all instructions allowed, one program. Virtual 86 mode: a protected-mode task with VM = 1 that runs 8086 code with the same segment x 16 + offset addressing, but at CPL 3, with paging (its 1 MB anywhere in 4 GB), I/O and IOPL-sensitive instructions trapped to a monitor, interrupts going to protected-mode handlers, and many V86 tasks running together."
sources: ["MHE 80386-updated slides 14-15 (real mode, protected mode, virtual 86 mode)"]
---
| | Real mode | Virtual 8086 (V86) mode |
|:--|:--|:--|
| How entered | after reset (PE = 0) | from protected mode: IRET or task switch with **VM = 1** in EFLAGS |
| Addressing | segment $\times$ 16 + offset, 1 MB | same 1 MB addressing, but a **linear** address; **paging** can place it anywhere in 4 GB |
| Protection | none; the program has full control | runs as a protected task at **CPL 3**; privileged and IOPL-sensitive instructions (CLI, STI, INT n, IN/OUT ...) cause faults handled by a **V86 monitor** |
| Interrupts | real-mode vector table at 0 | go to protected-mode handlers in the IDT (the monitor may reflect them to the 8086 program) |
| Multitasking | one program | several V86 tasks (several "8086 machines", e.g. DOS boxes) alongside protected-mode tasks |
| Leaving | set PE to enter protected mode | any interrupt or exception switches to protected mode |

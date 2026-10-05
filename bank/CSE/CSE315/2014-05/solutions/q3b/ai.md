---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Virtual 8086 mode (VM = 1 in EFLAGS) runs real-mode 8086 programs as tasks inside protected mode: addresses are segment x 16 + offset (1 MB), placed anywhere in 4 GB by paging; the program runs at CPL 3 under a protected-mode monitor, which handles interrupts and IOPL-sensitive/privileged instructions; entered by IRET or a task switch with VM = 1, left on any interrupt or exception. Several DOS programs can run together with protection."
sources: ["MHE 80386-updated slides 3, 10, 14-15 (VM flag, virtual 86 mode, multi-user system)", "Brey, The Intel Microprocessors, Sec. 17-5 (virtual 8086 mode)"]
---
**Virtual 8086 (V86) mode** lets the 80386 run 8086 (real-mode) programs **inside protected mode**, as tasks under a protected-mode operating system.

- It is selected by the **VM flag (bit 17 of EFLAGS)**. VM can be set only from protected mode, by an `IRET` (popping an EFLAGS image with VM = 1) or by a **task switch** to a TSS whose EFLAGS has VM = 1.
- **Addressing** is the same as real mode: linear address = segment $\times$ 16 + offset, so each V86 task sees 1 MB. With **paging**, that 1 MB can be placed **anywhere in the 4 GB** physical memory, and several V86 tasks can each have their own "first megabyte".
- The V86 program always runs at **CPL 3**. Privileged instructions and IOPL-sensitive ones (`CLI`, `STI`, `INT n`, `PUSHF`, `POPF`, `IRET` when IOPL < 3) and I/O instructions (via the I/O permission bitmap) cause a **general protection fault**, which goes to a **virtual machine monitor** running at PL0. The monitor emulates them (e.g. simulates DOS/BIOS services, virtual devices).
- **Leaving V86 mode:** every interrupt or exception switches the processor to protected mode (PL0 handler); `IRET` returns to the V86 task.

**Advantages:** old DOS programs can run together with 32-bit protected-mode programs, with full protection and paging, multitasking several "8086 machines" (e.g. DOS boxes in Windows); the 80386 does not need a reset to run real-mode code, unlike the 80286.

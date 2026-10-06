---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Dual-mode operation uses a mode bit so that privileged instructions run only in kernel mode; a user program obtains OS services through a system call (trap), which switches to kernel mode and back."
sources: ["Tanenbaum MOS 4e, sec. 1.3 and 1.6 (kernel mode/user mode, system calls)"]
---
**Dual-mode operation.** The hardware has (at least) two modes, selected by a **mode bit** in the processor status register:

- **Kernel (supervisor) mode:** the OS runs here; **all** instructions are allowed, including *privileged* ones (I/O instructions, writing the page-table base register, disabling interrupts, halt) and access to all memory and devices.
- **User mode:** application programs run here; privileged instructions or access to protected memory cause a trap to the OS (the process is usually killed).

This protects the OS and the processes from each other: a buggy or malicious program cannot take over the machine.

**How a user program gets OS services: system calls.**

1. The program (usually through a library wrapper such as `read()`) puts the system-call number and arguments in registers/on the stack.
2. It executes a **trap** instruction (`syscall`/`int`). The hardware switches the mode to kernel mode, saves the PC and jumps to the kernel's system-call handler.
3. The kernel checks the arguments and performs the service in kernel mode.
4. It places the result in a register and executes a **return-from-trap**; the hardware switches back to user mode and execution continues after the trap instruction.

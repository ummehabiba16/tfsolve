---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The CPU runs in kernel mode on a system call (trap), on a hardware interrupt, and on an exception (fault) such as a page fault."
sources: ["Tanenbaum MOS 4e, sec. 1.3 and 1.6 (kernel/user mode, system calls)"]
---
The CPU switches from user mode to kernel mode in three cases (apart from the initial boot, when the kernel is already running):

1. **System call (software trap).** A user process executes a trap instruction (e.g. `syscall`, `int 0x80`) to request an OS service such as `read` or `fork`. The hardware sets the mode bit to kernel mode, saves the PC and jumps to the system-call handler; on return the mode is set back to user.
2. **Hardware interrupt.** A device (disk, keyboard, network card) or the timer signals the CPU asynchronously. The CPU stops the current program, switches to kernel mode and runs the interrupt handler; the timer interrupt is how the OS regains control for scheduling.
3. **Exception (fault/trap caused by the program).** The current instruction cannot be executed normally: page fault, divide by zero, illegal instruction, protection violation. The hardware enters kernel mode and runs the exception handler (which may fix the problem, as in a page fault, or kill the process).

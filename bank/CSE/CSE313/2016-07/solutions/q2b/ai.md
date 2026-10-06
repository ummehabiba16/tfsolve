---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "i. kernel to user; ii. user to kernel; iii. kernel to user; iv. upcall (kernel to user, a signal-like notification)."
sources: ["Anderson and Dahlin, OSPP, ch. 2.3 (mode switch: user-to-kernel, kernel-to-user, upcalls)"]
---
**Definitions.** *User-to-kernel transfer:* the CPU leaves user mode to run kernel code (interrupt, exception, system call). *Kernel-to-user transfer:* the kernel returns to user code (resume after an interrupt or exception, start a new process, switch to another process). *Upcall:* a **kernel-to-user** transfer in which the kernel **notifies the user program of an event** (a virtual interrupt, like a signal) and the user handler runs.

| Scenario | Type | Explanation |
|:--|:--|:--|
| i. **Resume after an interrupt**: execution of the interrupted process continues by restoring its PC | **Kernel to user** transfer | the kernel finishes the handler and returns to the process |
| ii. **Processor exception**: a hardware event caused by user program behaviour, the hardware saves the state and runs the exception handler | **User to kernel** transfer | the CPU enters the kernel handler |
| iii. **New process**: program copied into memory, PC set to its first instruction, stack pointer set, process started | **Kernel to user** transfer | the kernel starts user-mode execution |
| iv. **Resource allocation**: the OS informs a resource-adaptive process (e.g. the Java run time) that its memory allocation has changed | **Upcall** (kernel to user) | the kernel notifies the user process asynchronously so it can adapt (e.g. change the garbage-collection frequency) |

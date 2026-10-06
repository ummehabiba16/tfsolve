---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A process needs a kernel stack because kernel code cannot trust the user stack and must keep the kernel frames of each process while it sleeps; user stack holds user-mode calls."
sources: ["Bach, ch. 6 (the context of a process: user stack and kernel stack)"]
---
Each process has **two stacks**: a **user stack** (used while running in user mode: frames of user functions, local variables) and a **kernel stack** (used while the process executes in kernel mode, e.g. inside a system call or interrupt handler).

**Why a separate kernel stack is needed**

1. **Security/protection:** the kernel cannot trust the user stack: the user pointer may be wrong, the stack may be too small or unmapped, and a user process could read kernel data left on a shared stack or corrupt it. The kernel stack lives in kernel space and is inaccessible to user mode.
2. **Correctness:** the kernel must always have a valid, big-enough stack, independent of what the user program did.
3. **Sleeping in the kernel:** a process can **sleep inside a system call** while another process runs; its kernel frames (the chain of kernel function calls) must stay intact until it is woken. So **each process needs its own kernel stack** (a single shared kernel stack would be overwritten by the next process).

**Example.** A process calls `read()`. The trap switches to kernel mode and the kernel's `read` $\to$ `bread` $\to$ `getblk` $\to$ `sleep` frames are pushed on **that process's kernel stack**. The process sleeps waiting for the disk, and the scheduler runs process B (with its own kernel stack). When the disk interrupt wakes the first process, it continues exactly in `sleep` and returns up its chain of kernel frames, then returns to user mode, where its (untouched) user stack is used again.

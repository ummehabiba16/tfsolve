---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Agree: each thread has its own flow of control, so it needs its own stack for return addresses, parameters and local variables."
sources: ["Tanenbaum MOS 4e, sec. 2.2.1-2.2.2 (the thread model; per-thread items)"]
---
**Yes, I agree.** The threads of a process share the code, global data, heap and open files, but each thread has an **independent flow of control**: it calls and returns from procedures, so it needs its own place to keep **return addresses, parameters and local variables**. If two threads used the same stack, their procedure calls would be interleaved and would overwrite each other's frames.

For user-level threads the kernel knows only one stack for the process, so the **thread library allocates a separate stack for every thread** (inside the process's address space) when the thread is created, and the context switch of the library switches the stack pointer (together with the registers) from one thread to the other. (Stacks of the other threads cannot grow automatically, so their size must be chosen at creation.)

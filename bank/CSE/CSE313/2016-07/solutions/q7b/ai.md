---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A buggy thread can corrupt the shared address space, crash the entire process, hog the CPU or deadlock the others, because threads are not isolated from each other."
sources: ["Anderson and Dahlin, OSPP, ch. 4 (threads)"]
---
Threads of a process **share the address space** (heap, globals, files) and there is **no protection between them**, so a bug in one thread can harm all the others:

- **Memory corruption:** a wild pointer or buffer overflow can overwrite another thread's data or its stack.
- **Crash of the whole process:** a segmentation fault, an unhandled exception, `exit()` or a call to `abort()` in one thread **kills every thread** of the process.
- **CPU hogging:** an infinite loop in one thread (especially with user-level threads) starves the others.
- **Deadlock/livelock** if it forgets to release a lock (or acquires locks in the wrong order), blocking all threads that need the lock.
- **Resource leaks** (memory, file descriptors) that affect the whole process, and **data races** that give non-deterministic results that are very hard to debug.

With separate processes, such a bug stays confined to one process.

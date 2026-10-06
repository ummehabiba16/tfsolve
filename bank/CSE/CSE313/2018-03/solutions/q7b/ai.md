---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Threads share the address space and resources, so they are cheaper to create and switch, communicate through shared memory, and let a process keep working while one thread blocks."
sources: ["Tanenbaum MOS 4e, sec. 2.2.1 (the thread model)"]
---
Threads of one process share the **address space, global data, open files** and other resources, which gives these advantages over several processes doing the same job:

1. **Cheaper creation, termination and switching:** no new address space and no resource duplication (creating a thread is about 10-100 times faster than creating a process); switching between threads of one process avoids changing the memory map and flushing the TLB.
2. **Easy communication and data sharing:** threads communicate through shared memory without kernel-mediated IPC (pipes, messages).
3. **Responsiveness / overlap of activities:** while one thread blocks (I/O), the others continue, e.g. a word processor with threads for input, formatting and auto-saving; a server with a thread per request.
4. **Parallelism** on multiprocessors with shared data structures.

(The price is the need for explicit synchronisation, and the lack of protection among the threads of a process.)

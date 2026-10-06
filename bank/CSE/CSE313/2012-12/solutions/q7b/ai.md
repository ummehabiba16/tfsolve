---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Kernel threads: a blocking call blocks only one thread and threads run in parallel on several CPUs, but creation and switching cost system calls and kernel table space."
sources: ["Tanenbaum MOS 4e, sec. 2.2.4 (threads in the kernel)"]
---
**Advantages**

- A **blocking system call or page fault blocks only the calling thread**; the kernel can run another thread of the same process.
- The kernel can run **different threads of a process on different CPUs** (true parallelism).
- No special non-blocking system calls or run-time system are needed; the kernel schedules each thread (and can pre-empt it with the timer).

**Disadvantages**

- Thread **creation, destruction and switching are system calls**: they are much more expensive than user-level operations (although threads can be *recycled* to reduce the cost).
- A **thread table in the kernel** with a fixed size and memory per thread.
- Messy semantics: what happens on `fork` of a multithreaded process (does the child get all the threads?), and **signals** (which thread should receive a signal?).

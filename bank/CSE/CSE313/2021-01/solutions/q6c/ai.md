---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "User threads: managed by a library in user space, fast but a blocking call blocks the whole process and no multiprocessor parallelism; kernel threads: managed by the OS, scheduled individually, slower to create/switch."
sources: ["Tanenbaum MOS 4e, sec. 2.2.4-2.2.5 (user-space vs kernel threads)"]
---
| | **User-level thread** | **Kernel-level thread** |
|:--|:--|:--|
| Managed by | a run-time library in user space; the kernel sees only one process | the OS kernel (thread table in the kernel) |
| Creation / switch | very fast (procedure calls, no trap, no mode switch) | slower (system call, kernel involved) |
| Blocking system call | blocks the **whole process** (all threads) | blocks only that thread; others can run |
| Multiprocessors | all threads of the process run on one CPU at a time | different threads can run on different CPUs |
| Scheduling | by the library (own algorithm, usually cooperative: no clock interrupts inside a process) | by the kernel scheduler (pre-emptive) |
| Portability | runs on any OS, even one without thread support | depends on the OS |
| Drawbacks | page fault of one thread blocks all; one thread that never yields starves the others | more kernel resources per thread; higher cost of operations |

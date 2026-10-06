---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "User threads: cheap and portable but one blocking call blocks all and no multiprocessor speed-up; kernel threads: parallel and non-blocking but slower creation/switching and kernel resources."
sources: ["Tanenbaum MOS 4e, sec. 2.2.4-2.2.5"]
---
| | **Threads in user space** | **Threads in kernel space** |
|:--|:--|:--|
| Advantages | **Fast** creation and switching (library calls, no trap); can be implemented on an OS without thread support; each process can have its own **scheduling algorithm**; no kernel thread table. | A **blocking system call or page fault blocks only that thread**; threads can run on **different CPUs** in parallel; the kernel schedules each thread (pre-emptive, with time slices); no non-blocking system call wrappers needed. |
| Disadvantages | A **blocking system call** (or a page fault) blocks the **whole process**; no true parallelism on a multiprocessor (the kernel sees only one schedulable entity); no clock interrupts within a process, so a thread that never yields starves the others (cooperative). | Creating, destroying and switching threads need **system calls** (more expensive); a fixed-size **thread table** in the kernel; problems with `fork` and signals in a multithreaded process; less portable. |

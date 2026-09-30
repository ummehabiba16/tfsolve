---
author: ai
via: chat
status: unverified
summary: Monolithic = whole OS in one kernel-mode program (fast, but large and fragile). Microkernel = tiny kernel (IPC + basic scheduling/I/O) with services as user-mode servers (reliable and modular, but message overhead).
sources: [Introduction slides 27-33, 'Tanenbaum, MOS 4e, sec. 1.7.1-1.7.3']
imported_from: tfsolve-questions/data/solutions/2021-22.json
---
- Monolithic kernel: the whole OS (scheduler, memory manager, file system, drivers) runs as one program in kernel mode; services call each other as ordinary functions. Fast (no message overhead) but large, hard to maintain, and a bug anywhere can crash the whole system.
- Microkernel: the kernel is reduced to a minimum (IPC, basic scheduling, low-level I/O); file systems, drivers, etc. run as separate user-mode server processes that communicate by messages. More reliable and modular (a failed server can be restarted, better isolation) but incurs message-passing and user$\leftrightarrow$kernel overhead.

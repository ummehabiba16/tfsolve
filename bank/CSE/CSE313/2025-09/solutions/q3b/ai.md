---
author: ai
via: chat
status: unverified
summary: Mode = CPU privilege level (kernel mode can run all instructions and touch all memory; user mode cannot). Space = the address-space split (protected kernel space vs the process's user space), crossed only via system calls.
sources: [Introduction slides 12-16, 'Tanenbaum, MOS 4e, sec. 1.3.3']
imported_from: tfsolve-questions/data/solutions/2023-24.json
---
- User mode vs kernel mode: two CPU privilege levels. In kernel mode the CPU can execute every instruction, including privileged ones (I/O, set timers, change the MMU, halt), and access all memory. In user mode privileged instructions trap, and only the process's own memory is reachable. The OS runs in kernel mode, applications in user mode.
- User space vs kernel space: the address-space division. Kernel space holds OS code and data and is protected; user space holds the process's text, data, heap and stack. User-space code reaches kernel space only through a system call (a controlled mode switch).

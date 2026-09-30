---
author: ai
via: chat
status: unverified
summary: In ULT the thread table and scheduler sit in user space over a single kernel process entry; in KLT they sit in the kernel. KLT is better for blocking because the kernel can run another thread of the same process when one blocks.
sources: [Process/Thread slides 31-38, 'Tanenbaum, MOS 4e, sec. 2.2.4']
imported_from: tfsolve-questions/data/solutions/2021-22.json
---
- User-level threads (ULT): the run-time library holds the thread table and the thread scheduler, both in user space. The kernel sees only one process (one process-table entry) and is unaware of the threads.
- Kernel-level threads (KLT): the kernel holds the thread table (alongside the process table) and does the thread scheduling; the user-space library only makes system calls.

Blocking: with ULT a blocking system call by one thread traps into the kernel, which, seeing only the process, blocks the whole process, so no other thread of it can run. With KLT the kernel knows the sibling threads and dispatches a runnable one, so only the calling thread blocks. That is why KLT is better with respect to blocking.

Diagram: draw the process box; for ULT place [thread table + scheduler] in user space above a single kernel process entry; for KLT place [thread table + scheduler] inside the kernel.

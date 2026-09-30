---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
**(i) Low and bursty arrival rate:** **interrupt-driven I/O** is preferable. If packets arrive rarely and unpredictably, a polling loop would waste the CPU continuously checking a device that has nothing to report almost all of the time. With interrupts, the CPU is free to do other useful work and is only disturbed exactly when a packet genuinely arrives, which is the efficient choice when events are infrequent.

**(ii) High and regular arrival rate:** **polling** is preferable. When packets arrive extremely frequently, the fixed per-event overhead of an interrupt (trap into the kernel, save/restore state, run the handler, return) is paid on almost every packet, and can even cause *receive livelock* -- the CPU spends 100% of its time inside interrupt handlers and never makes progress on user-level work. Polling avoids this per-event trap cost entirely: the CPU simply checks the device status directly and processes data in a tight loop, which is far more efficient when it can be fairly certain there will be more work to do almost every time it checks. (In practice, real high-throughput NICs often use a hybrid: interrupts when idle, switching to polling once traffic is high -- e.g. Linux's NAPI -- to get the best of both worlds.)

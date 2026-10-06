---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Microkernel advantages: reliability and fault isolation (drivers and servers in user space), security with a small trusted kernel, easier extension and porting."
sources: ["Tanenbaum MOS 4e, sec. 1.7.3 (microkernels)"]
---
In a **microkernel** only a minimal set of functions (address spaces, threads and scheduling basics, interprocess communication) runs in kernel mode; the file system, device drivers, network stack, etc. run as **servers in user mode**. Advantages:

1. **Reliability / fault isolation:** a bug in a driver or a server crashes only that user-mode process, which can be restarted, not the whole system (about 3-10 bugs per 1000 lines of code, so a small kernel has far fewer bugs than a monolithic one).
2. **Security / small trusted computing base:** only a few thousand lines run with full privilege; drivers have limited access, so a compromised component cannot take over the system.
3. **Flexibility, extensibility and portability:** services can be added, replaced or updated without rebuilding the kernel (even while running); only the small kernel is machine dependent.

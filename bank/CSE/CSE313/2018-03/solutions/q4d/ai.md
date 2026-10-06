---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The u area is the per-process kernel data (open files, current directory, I/O parameters, signal handlers, user IDs, ...) that the kernel can access only for the running process; three processes have three u areas but the kernel sees only one at a time."
sources: ["Bach, ch. 6 (the u area; process context)"]
---
**Purpose.** The **u area** (user area) is a per-process structure in the process's own address space, used by the kernel only while that process is running (kernel mode on its behalf). The process table entry is always visible to the kernel; the u area is needed only for the current process, so it can be swapped out with the process.

**Major information in the u area**

- pointer to the process table entry of the running process;
- real and effective user IDs (permissions);
- timers (user and kernel CPU time);
- the array of **signal handler** addresses;
- the control terminal;
- **error field** and **return value** of the current system call;
- **I/O parameters:** address, count and file offset of the current `read`/`write`;
- current directory and current root (inodes);
- the **user file descriptor table** (open files);
- limit fields (max file size) and the permission-mode mask (`umask`);
- the kernel stack lives next to it.

**How the kernel uses it.** The u area is mapped at a fixed virtual address, **`u`**. On a context switch the kernel remaps that address to the u area of the next process, so kernel code can always refer to `u.u_...` without knowing which process it is.

**Number of u areas for P, Q, R.** Each of the three processes has **its own u area** (three exist), but the kernel can address **only one at a time: that of the currently running process**, i.e. one u area is "active" at any instant (one per CPU on a multiprocessor).

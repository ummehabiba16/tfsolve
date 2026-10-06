---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "UNIX protects kernel consistency by never preempting a process in kernel mode (context switches only at sleep points), by raising the processor level to block interrupts in critical regions and by locking buffers/inodes across sleeps."
sources: ["Bach, ch. 2 (kernel consistency: no preemption, interrupt levels, locks)"]
---
Several processes (and interrupt handlers) execute kernel code and share kernel data structures (buffer cache, inode table, free lists). UNIX keeps these consistent with these rules:

1. **The kernel is non-preemptive:** a process running in kernel mode is **not preempted** by the scheduler (the kernel does not switch contexts on a timer tick); it keeps the CPU until it finishes the system call or **voluntarily goes to sleep**. So no other process can run *in the middle of* an update of a kernel structure (on a uniprocessor). *Example:* a process that is in the middle of linking a buffer into the free list will not be replaced by another process that traverses the list.
2. **Blocking interrupts in critical regions:** interrupt handlers also use kernel data. The kernel **raises the processor execution level** to block the relevant interrupts while it manipulates such structures and lowers it afterwards. *Example:* `brelse` and `getblk` raise the level while they manipulate the free list, so a disk interrupt cannot call `brelse` for another buffer at the same moment.
3. **Locks for resources held across sleeps:** if a process must sleep while it uses a structure (waiting for disk I/O on a buffer, or for a locked inode), the structure is **locked** (buffer busy, inode locked); other processes that find it locked **sleep** until it is unlocked. *Example:* a process sleeping in the middle of reading a buffer has the buffer marked busy, so no other process can use or reassign it.
4. **Data structures are left consistent before sleeping:** the kernel makes sure that, before it sleeps, it leaves the structures in a consistent state (updating pointers completely), so whoever runs next sees a consistent picture.

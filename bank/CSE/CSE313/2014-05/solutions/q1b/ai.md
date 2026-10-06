---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The buffer cache reduces disk accesses by keeping recently used blocks in memory, gives uniform access to block devices, hides alignment and allows read-ahead and delayed writes, at the cost of copying and a risk of data loss after a crash."
sources: ["Bach, ch. 3 (buffer cache: advantages and disadvantages)"]
---
**Why a buffer cache.** Disk access is thousands of times slower than memory access. The kernel keeps recently used disk blocks in a pool of **buffers in main memory**; all disk I/O of the file system (data, inodes, directories, superblock) goes through it.

**Benefits**

- **Fewer disk accesses:** a block that is read again (e.g. the root directory, an inode or a hot file) is found in the cache (a *hit*) without I/O; the kernel also does **read-ahead** of the next block in sequential reads.
- **Delayed writes:** data that is modified again soon is written once, not every time, and the writes can be sorted/combined, improving disk throughput.
- **Uniform interface and alignment:** the file system code does not have to care about the physical alignment of user buffers, and the cache hides the block size from user programs (a user can read one byte); the data is copied to the right place.
- **Synchronisation point:** the buffer headers and locks serialise concurrent access to a block (only one process uses it at a time), and the block is cached once for all processes.
- Reduces disk traffic generally, increasing the throughput of the whole system.

**Disadvantages (for completeness):** data is copied twice (disk $\to$ buffer $\to$ user space); with delayed write a **crash can lose data** not yet written to disk (hence `sync` and update daemons); the cache uses memory.

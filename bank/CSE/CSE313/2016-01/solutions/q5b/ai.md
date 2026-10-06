---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "After fork() (or dup/dup2) two entries of the user file descriptor table, in the same or different processes, point to the same file-table entry and so share the file offset."
sources: ["Bach, ch. 5 (file system calls: dup, fork; file table)"]
---
Each process has a **user file descriptor table** (in its u area) whose entries point to entries in the system-wide **file table** (which holds the current offset, the access mode and a reference count, and points to the in-core inode).

**Scenario 1: `dup`.** After `fd2 = dup(fd1)`, the kernel copies the pointer of `fd1` into the first free slot of the descriptor table: **two entries of the same table point to the same file-table entry**; the entry's count becomes 2. Reading or writing through either descriptor uses the **same offset**. (Shells use `dup2` for redirection, e.g. `2>&1`.)

**Scenario 2: `fork`.** The child gets a **copy of the parent's descriptor table**; every entry still points to the same file-table entry and the counts are incremented. So the descriptors of parent and child (two tables) refer to the same file-table entry: they share the offset, which is why output of a parent and child written to the same open file is not overwritten but appended in order.

(Calling `open` twice on the same file gives *two different* file-table entries pointing to the same inode, with independent offsets.)

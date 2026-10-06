---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A disk inode holds file attributes and block pointers; an in-core inode adds status (locked, wanted, modified), device and inode number, links to hash queue/free list and the reference count, which are meaningful only in memory."
sources: ["Bach, ch. 4 (in-core copy of the inode)"]
---
**Two types of inodes.**

- The **disk inode** is the permanent copy kept in the inode list on the disk: owner, group, file type, permissions, access/modification/change times, link count, size, and the table of contents of disk block numbers (10 direct + 3 indirect).
- The **in-core inode** is the copy in the kernel's **inode table** while the file is in use. It has all the fields of the disk inode **plus**:
  - **status:** locked, a process is waiting for it to be unlocked, the in-core copy differs from the disk copy (**modified**: the inode data or the file data changed), the inode is a mount point;
  - the **logical device number** of the file system containing the file;
  - the **inode number** (it is implied by the position on disk, so it is not stored on disk);
  - **pointers to other in-core inodes**: the next/previous links of the inode **hash queue** and of the **free list**;
  - the **reference count**: the number of active references (e.g. open file-table entries, current directories).

**Why they are absent on disk.** These fields describe the *run-time state* of the inode in memory: lock and modification state, the links of kernel lists (memory addresses), and the number of current users are meaningless once the file is not in use or after a reboot; the device number and inode number are known from where the inode is read. Storing them would waste disk space and each update would require disk writes.

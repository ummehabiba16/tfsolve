---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Boot block: boot program; super block: file-system parameters and free lists; inode list: the file inodes; data blocks: file and directory contents and indirect blocks."
sources: ["Bach, ch. 4 (file system layout); Tanenbaum MOS 4e, sec. 4.5.2"]
---
A UNIX file system on a disk partition is laid out as:

| Block(s) | Purpose |
|:--|:--|
| **Boot block** | block 0: holds the **bootstrap code** that is loaded into memory when the machine is booted from this file system and that loads the kernel (present in every file system, used only in the bootable one) |
| **Super block** | describes the **state of the file system**: its size, the number of inodes and where the inode list starts, the **free-block list** and the **free-inode list** (with the remembered inode), the number of free blocks/inodes and lock/modified flags; it is read into memory when the file system is mounted |
| **Inode list** | an array of all the **disk inodes**: one per file, with its owner, type, permissions, times, link count, size and block pointers; the inode number is the index in this list; the size of this list (fixed when the file system is made) limits the number of files |
| **Data blocks** | the contents of **regular files and directories**, indirect (pointer) blocks of large files, and the free blocks; allocated to files as they grow |

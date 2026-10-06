---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "An in-core inode is the memory copy of a file's disk inode plus status; a buffer header describes a cached disk block (device, block number, status, pointers) whose data is in a separate data area."
sources: ["Bach, ch. 3 and ch. 4"]
---
| | **In-core inode** | **Buffer header** |
|:--|:--|:--|
| Describes | a **file** (its metadata) | a **cached disk block** |
| Contents | copy of the disk inode: owner, permissions, file type, size, times, link count and the table of contents of block numbers; plus status (locked, modified), device and inode number, reference count, hash/free-list pointers | device number, block number, status (locked, valid, delayed write, I/O in progress, wanted), pointer to the **data area** (the block's data), hash-queue and free-list pointers |
| Where its data are | the inode itself (metadata only, no file data) | in the separate buffer data area (the block contents) |
| Source on disk | inode list | any disk block (data blocks, inodes, directories, superblock) |
| Cache structure | **inode table** with hash queue and free list | **buffer pool** with hash queues and free list |
| Written back | when modified, on `iput`/`sync` | when marked delayed write or on `sync`/reuse |

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "No: the superblock list is only a cache of at most about 100 free inode numbers; the other free inodes are found by scanning the disk inode list from the remembered inode."
sources: ["Bach, ch. 4 (assigning inodes: algorithm ialloc, remembered inode)"]
---
**No, I do not agree.**

The superblock contains a **fixed-size array** (about 100 entries) of free inode numbers: it is only a **cache** of free inodes, not a list of all of them. A disk may have thousands of free inodes; the others are known only by their `type` field in the inode list on disk (a free inode has file type 0).

- **Allocating (`ialloc`):** the kernel takes inode numbers from the superblock list. When the list **becomes empty**, the kernel **searches the on-disk inode list** (reading the blocks of inodes) starting from the **remembered inode** (the highest inode number put in the list last time), collects free ones until the list is full again and updates the remembered inode.
- **Freeing (`ifree`):** if the list is **full**, the inode number is *not* recorded in it (the inode just stays marked free on disk); if its number is lower than the remembered inode, it becomes the new remembered inode so that the next search will find it.

So the superblock list holds only *some* of the free inodes: those found by the last scan, plus recently freed ones when there was room.

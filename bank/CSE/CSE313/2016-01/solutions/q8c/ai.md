---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A linked list of free blocks is simple and uses the free blocks themselves, but allocating several blocks needs several accesses and contiguous runs are hard to find."
sources: ["Tanenbaum MOS 4e, sec. 4.4.3 (managing free disk space: linked list of disk blocks)"]
---
**Linked-list free-space management:** each free block contains the **number of the next free block** (or, in the improved version, a list of many free block numbers plus a pointer to the next such block). The superblock/OS keeps the head of the list.

![Linked list of free disk blocks](figures/freelist.png)

**Advantages**

- **No extra space** is needed: the list is stored inside the free blocks themselves, which are unused anyway.
- Only **one block** (the head, kept in memory) has to be held in memory; allocating and freeing one block is quick: take or add at the head.
- Very simple.

**Disadvantages**

- **Allocating $n$ blocks** may need $n$ disk accesses if each free block holds only one pointer (the improved version with many pointers per block reduces this).
- It is **difficult to find contiguous free blocks**, and the list is in random order, so files become scattered (poor locality).
- The list can be **damaged** by a single corrupted block (the rest of the list is lost); there is no easy way to check how much space is free without traversing the list.
- Freeing a file with many blocks needs many updates.

*Example:* free blocks 106, 108, 112, 145: the head points to 106; 106 contains 108; 108 contains 112; 112 contains 145; allocating three blocks requires reading 106, 108 and 112.

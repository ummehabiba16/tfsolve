---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "In System V the remembered number belongs to inodes (the scan restarts from it); free blocks are found by following the linked list; with bitmaps the remembered block is the next-fit search start."
sources: ["Bach, ch. 4 (remembered inode; free block list)"]
---
**The statement needs care.** In System V UNIX the **"remembered" number is the *remembered inode*** (see 3(c)), used by `ialloc` to resume the scan of the inode list for free inodes. For **disk blocks** the next available blocks are not found by a search: they come from the **linked list of free-block arrays**; when the superblock array runs out, the kernel reads the next list block (the block number stored in entry 0), so the position in the chain is the "memory" of where to continue.

**In an allocator that does search for free blocks** (e.g. a bitmap-based file system such as FFS or ext2), the statement is justified as follows: the file system remembers the **last allocated block number** (the *allocation goal*, a next-fit rotor) and starts the next search **from there** instead of from the beginning of the bitmap, because

1. blocks before it were found to be in use a moment ago, so scanning them again would waste time;
2. a file's blocks are allocated one after the other, so continuing from the last block gives **contiguous (sequential) blocks** and good disk locality, with fewer seeks.

*Note:* the question mixes the two systems; for the classical System V file system it is the remembered **inode** that is used.

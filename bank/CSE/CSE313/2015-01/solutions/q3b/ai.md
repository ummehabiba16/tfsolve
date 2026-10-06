---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) with a single entry (the pointer to the next list block) that block is taken and its contents become the new list; (ii) when the list is full the freed block becomes a new list block holding the full list."
sources: ["Bach, ch. 4 (algorithms alloc and free)"]
---
Recall the structure: the superblock holds an array of free block numbers whose **entry 0 is the number of a block that contains the next array**, and so on (see the figure of the free-block list).

![Free disk-block list](figures/freelist.png)

**(i) The list in the superblock contains a single entry and a process requests a new block (`alloc`).** The single entry is the pointer to the **next block of the list**. The kernel **takes that block as the allocated block**, but first reads its contents (a full array of free block numbers) into the superblock, so the superblock list is refilled; then it clears the new block's contents (via the buffer cache) and returns it. (If the entry were 0, there is no free block: the error "no space".)

**(ii) The list in the superblock is full and a process frees a block (`free`).** There is no room for another number. The kernel **writes the superblock's current array into the block being freed** (so the freed block becomes a new list block holding the 100 numbers), and then sets the superblock list to contain a **single entry: the number of the freed block** (the pointer to the list block just written). Subsequent frees add numbers after it.

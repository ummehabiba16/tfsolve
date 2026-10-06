---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A bitmap needs one bit per block, makes contiguous runs easy to find but must be kept in memory and gets slow to scan when the disk is full; a linked list uses the free blocks themselves, is fast for single blocks but poor for contiguous or bulk allocation."
sources: ["Tanenbaum MOS 4e, sec. 4.4.3 (keeping track of free blocks)"]
---
**Bitmap implementation.** One bit per disk block: 1 = free, 0 = in use (the map is kept in memory, or the block with the bit is read as needed). Example: 8 blocks, blocks 0-2 used, 3-7 free: `00011111`. Allocation: find a 1, set it to 0; freeing: set the bit to 1.

**Advantages**

- **Very compact:** one bit per block (a 1 TB disk with 4 KB blocks: $2^{28}$ bits $=32$ MB), far less than a list holding a 32-bit number for each free block (32 times more).
- **Easy to find contiguous free blocks** (a run of 1 bits) and blocks near a given one, so it supports contiguous allocation and **locality**.
- Easy to count free blocks and to check for consistency.

**Disadvantages**

- The map should be **in memory** (large for a huge disk), and every allocation or free updates the map, which must be written back (a crash may leave it inconsistent).
- **Searching** for a free block can be slow when the disk is **almost full** (long scans for the next 1 bit).

**Linked list of free blocks:** uses the free blocks themselves to hold the pointers (no extra space when the disk is full, only the first block needs memory), allocating one block is fast, but contiguous allocation and bulk allocation are poor, so the bitmap is preferable unless the disk is nearly full.

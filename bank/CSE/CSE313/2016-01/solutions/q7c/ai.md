---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A bitmap uses one bit per block (small, easy to find runs, easy to allocate contiguously) but must be in memory and scanning is slow when the disk is nearly full."
sources: ["Tanenbaum MOS 4e, sec. 4.4.3 (managing free disk space: bitmaps)"]
---
**Bitmap free-space management:** one **bit per disk block**: 1 = free, 0 = in use (or the reverse). Example: for the 10-block SSD above with data blocks 3-9, after storing A (3-6), B (7) and C (8) the map of blocks 3-9 is `0000001`... (only block 9 free).

**Advantages**

- **Very compact:** one bit per block (a 1 TB disk with 4 KB blocks needs $2^{28}$ bits $=32$ MB), much smaller than a list of block numbers.
- **Easy to find $k$ consecutive free blocks** (look for a run of $k$ ones), so it supports **contiguous allocation**, and it is easy to allocate blocks close to a given block (locality).
- Simple to implement and to check for consistency; blocks are freed by simply setting the bit.

**Disadvantages**

- The map must be **kept in memory** (or each allocation needs a disk access); for a very large disk the bitmap is large.
- **Searching** for a free block can be slow when the disk is **almost full** (many 0 bits to skip), and is unnecessary when most of the disk is free.
- Updating the bitmap on every allocation/deallocation costs disk writes, and the map must be kept consistent after a crash.

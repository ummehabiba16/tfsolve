---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A buffer is always on a hash queue (so cached blocks can be found) but is on the free list only while it is not busy; the two structures give fast lookup and LRU reuse."
sources: ["Bach, ch. 3 (buffer cache structure)"]
---
**"Each buffer always exists on a hash queue but not always on the free list" is true:**

- A buffer in the cache always contains **some disk block** (identified by device and block number), so it is always on the **hash queue** for that block, even while it is being used, so `getblk` can find it (and find that it is busy).
- A buffer is on the **free list** only while it is **not locked (not busy)**, i.e. available for reuse. When a process gets it (`getblk` locks it), it is **removed from the free list** but stays on its hash queue; `brelse` puts it back on the free list.

**Why two separate data structures?**

- The **hash queues** give **fast lookup**: to find whether block $(d,b)$ is in the cache the kernel searches only one short queue instead of the whole pool.
- The **free list** gives **fast replacement**: it is an **LRU list** that tells which buffer to reuse when a new block is needed (the head), without searching the pool.

The two serve different purposes (search by identity vs. choice of a victim); combining them in a single structure would make either the lookup or the allocation slow.

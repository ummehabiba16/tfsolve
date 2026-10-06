---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "LRU order is kept by taking buffers from the head of the free list in getblk and putting released buffers at the tail in brelse, so the head is the least recently used."
sources: ["Bach, ch. 3 (getblk, brelse: free list as LRU)"]
---
The Least Recently Used structure is the **free list**, and it is maintained jointly by two pieces of the algorithms:

- In **`getblk`**, scenario 1: the buffer is **removed from the free list** (wherever it is) when it is used; scenarios 2 and 3: the buffer taken is the one **at the head** of the free list (`remove buffer from free list`), the **least recently used** one.
- In **`brelse`**, a buffer whose contents are valid is put **at the end (tail)** of the free list (`enqueue buffer at end of free list`): the most recently used buffer becomes the last.

So the part of `getblk` responsible is the `remove buffer from free list` of the "block in hash queue / buffer not busy" case (scenario 1: a hit takes the buffer out of its LRU position) and of the "get a buffer from the head of the free list" case (scenarios 2, 3), together with the enqueue at the **end** in `brelse`. The head of the list always contains the buffer that has not been used for the longest time.

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A buffer header has four link pointers (next/previous on the hash queue and on the free list), plus one pointer to the data area; the doubly linked lists allow removal of a buffer from the middle in constant time."
sources: ["Bach, ch. 3 (buffer headers)"]
---
A buffer header contains **four pointers** for the lists, plus **one pointer to the data area**:

1. **next buffer on the hash queue,**
2. **previous buffer on the hash queue,**
3. **next buffer on the free list,**
4. **previous buffer on the free list,**
5. (the pointer to the buffer's **data area**, i.e. to the memory holding the block).

**Necessity.** A buffer must be on a **hash queue** (to be found quickly by device and block number) and on the **free list** (to be reused in LRU order). Both are **doubly linked** lists, because the kernel must remove a buffer **from the middle of a list in constant time**:

- a buffer that is found in the hash queue and is free is **removed from the free list** wherever it is (scenario 1): a previous pointer is needed to relink its neighbours without traversing the list;
- a free buffer taken for a new block is removed from its **old hash queue** and inserted in a **new** one (scenario 2);
- inserting at the beginning or at the end of the free list (`brelse`) also needs both neighbours.

With only singly linked lists these removals would require searching the list from its head.

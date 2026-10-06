---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A delayed-write buffer holds modified data not yet on disk; when getblk finds such a buffer at the head of the free list it starts an asynchronous write and takes another buffer instead."
sources: ["Bach, ch. 3 (getblk scenario 3; delayed write)"]
---
**Meaning.** When a process writes data, the kernel often stores it in a cache buffer and marks the buffer **"delayed write"** instead of writing it to disk at once: the data in the buffer is **newer than the data on disk**, and the physical write is postponed (in the hope that the block will be modified again, or until the buffer is needed for another block). The buffer is then released to the **free list** (still holding the valid, modified data), so it may be reused for a different block later.

**Handling while allocating a new buffer (`getblk`, scenario 3).** The block is not in the cache, so `getblk` takes the buffer at the head of the free list. If that buffer is marked *delayed write*, the kernel cannot give it away yet, because its data would be lost:

1. remove the buffer from the free list (it is now busy);
2. start an **asynchronous write** of its contents to disk; and, **without waiting**,
3. `continue` the loop and take the next buffer from the free list (again checking for delayed write);
4. when the asynchronous write completes, the I/O interrupt handler clears the delayed-write mark and releases the buffer (`brelse`), at the **head** of the free list so that it is reused soon.

If the free list contains only delayed-write buffers, the process finds the list empty (scenario 4) and sleeps until a write completes and a buffer is freed.

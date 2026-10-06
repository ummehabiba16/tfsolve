---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The while loop makes getblk restart its search after every sleep or asynchronous write, because the state of the cache may have changed while the process waited."
sources: ["Bach, ch. 3 (getblk loop, continue statements)"]
---
The loop `while (buffer not found)` exists because in three places `getblk` cannot give the buffer immediately and has to **wait or do something else**, after which it must **start from the beginning** (`continue`):

1. **Block in the cache, buffer busy** (scenario 5): the process sleeps; after the wakeup the buffer may have been **reassigned to another block** by a process that ran first, or taken by another waiting process, so the process must search the hash queue again.
2. **Block not in the cache and the free list is empty** (scenario 4): the process sleeps until *any* buffer is freed; when it wakes up the **block may have been brought into the cache by another process**, or the free buffer may already be gone, so it again starts with the hash queue search.
3. **A free buffer is marked delayed write** (scenario 3): the kernel starts an asynchronous write of it and looks for another buffer; the cache may have changed in the meantime.

Thus the loop guarantees that when `getblk` finally returns, the decision was made on the **current** state of the cache: either the block's own buffer (hit), or a free buffer correctly reassigned to the block; this avoids two processes ending up with different buffers for the same block, or with the same buffer for two blocks.

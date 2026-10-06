---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The statement is wrong for getblk: it never returns an error; if no buffer is available the process sleeps until it can get one (unlike iget, which returns an error)."
sources: ["Bach, ch. 3 (algorithm getblk)"]
---
**The statement cannot be justified for the buffer cache: `getblk` never returns an error.** Its only result is a **locked buffer** assigned to the requested block.

```text
while (buffer not found) {
    if (block in hash queue)   { if (busy) { sleep; continue; }  take it; return buffer; }
    else {  if (free list empty) { sleep; continue; }
            take buffer from free list; if (delayed write) { async write; continue; }
            reassign; return buffer; }
}
```

- If the block is cached and free: return it. If it is cached but busy: the process **sleeps** (scenario 5) and tries again.
- If the block is not cached: take a free buffer. If there is none, the process **sleeps** until some buffer is released (scenario 4) and tries again; delayed-write buffers are written out and skipped (scenario 3).

The loop ends only when a buffer has been found; the caller waits as long as necessary. Failure to *read the data* is a different matter (`bread` reports an I/O error after the buffer has been allocated). The statement "returns a locked in-core inode **or returns an error**" is true of `iget` (an error when the inode table is full), not of `getblk`.

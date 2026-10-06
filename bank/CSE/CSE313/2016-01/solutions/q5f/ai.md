---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "brelse wakes waiting processes, then puts a valid buffer at the end of the free list (kept for reuse) and a buffer with invalid or old content at the front (reused first)."
sources: ["Bach, ch. 3 (algorithm brelse)"]
---
```text
algorithm brelse
input:  locked buffer
output: none
{
    wakeup all procs: event, waiting for any buffer to become free;
    wakeup all procs: event, waiting for this buffer to become free;
    raise processor execution level to block interrupts;
    if (buffer contents valid and buffer not old)
        enqueue buffer at end of free list
    else
        enqueue buffer at beginning of free list
    lower processor execution level to allow interrupts;
    unlock(buffer);
}
```

**The if-else.** The free list is an LRU list: buffers are taken from its **head** (beginning) for reuse, so the position decides how soon a buffer is reused.

- **`if` (contents valid and not "old")** $\to$ enqueue at the **end** of the free list. The buffer holds good data of a block that may be needed again, so it should stay in the cache as long as possible: it will be reused only after all the buffers in front of it (least-recently-used policy). *Example:* a process reads block 99 into a buffer and releases it; later another process asks for block 99 and finds it in the cache (a hit).
- **`else`** (contents invalid, e.g. after an I/O **error**, or marked **old**, e.g. the block was just written and will not be reused, or the file was deleted) $\to$ enqueue at the **beginning**: the buffer is useless as a cache entry, so it should be the **first to be reused** and does not displace good buffers. *Example:* a read error leaves the buffer invalid; it goes to the front so the next `getblk` takes it immediately.

The wakeups come first so that waiting processes can run when the buffer becomes free; the interrupt level is raised because the free list is also manipulated by disk interrupt handlers.

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The three continue statements restart the while loop after the process has slept (buffer busy, or free list empty) or after starting an asynchronous write of a delayed-write buffer, because the situation may have changed."
sources: ["Bach, ch. 3 (algorithm getblk: scenarios 3, 4, 5)"]
---
In `getblk` the loop `while (buffer not found)` is restarted by `continue` in **three** places:

1. **`if (buffer busy) { sleep (event buffer becomes free); continue; }`** (scenario 5): the block is in the cache but its buffer is **locked by another process**. The process sleeps; when it is woken it **cannot assume that the buffer is still free or still holds the block** (another process may have taken or reassigned it), so it **starts the search again** from the hash queue. *Example:* P waits for block 99; Q releases it; R grabs the buffer for block 53 before P runs; P's `continue` finds block 99 absent and takes another free buffer.
2. **`if (there are no buffers on free list) { sleep (event any buffer becomes free); continue; }`** (scenario 4): no buffer can be reassigned; the process sleeps until *any* buffer is released and then **restarts**, because several processes may have been woken for the same freed buffer and the first one takes it; the block might also have been brought in by another process meanwhile (then it is found in the hash queue).
3. **`if (buffer marked for delayed write) { asynchronous write buffer to disk; continue; }`** (scenario 3): the free buffer taken from the head holds data not yet on disk, so it cannot be reused. The kernel **starts an asynchronous write** and does **not wait**: `continue` goes back to look for another free buffer (the written buffer is freed when its I/O completes). The search starts from the beginning because the state may have changed during the call.

So each `continue` means "the state of the cache may have changed (or the chosen buffer was unusable), so re-evaluate from the start".

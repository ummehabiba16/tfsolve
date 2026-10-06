---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "When a specific buffer is released, brelse wakes all processes waiting for 'any buffer free' and all waiting for 'this buffer'; each restarts getblk and re-searches, the first gets the buffer, the others find it busy and sleep again."
sources: ["Bach, ch. 3 (algorithms getblk and brelse, scenarios 4 and 5)"]
---
**The two sleep events** in `getblk`:

- **(i) "any buffer becomes free"**: scenario 4: the block is not in the cache and the **free list is empty**, so the process sleeps until some buffer is released.
- **(ii) "a specific buffer becomes free"**: scenario 5: the block *is* in the cache but its buffer is **busy** (locked by another process), so the process sleeps until *that* buffer is released.

**What happens when the specific buffer becomes free.** The process using it calls `brelse`:

```text
algorithm brelse
{
    wakeup all procs: event, waiting for any buffer to become free;
    wakeup all procs: event, waiting for this buffer to become free;
    raise processor execution level to block interrupts;
    if (buffer contents valid and buffer not old) enqueue buffer at end of free list;
    else enqueue buffer at beginning of free list;
    lower processor execution level to allow interrupts;
    unlock(buffer);
}
```

- `brelse` wakes up **all** processes waiting for this buffer **and** all processes waiting for any buffer (they become *ready to run*; nothing is handed over to them).
- Each woken process **restarts the `while (buffer not found)` loop of `getblk`** (the `continue` after `sleep`) and searches the hash queue again, because the situation may have changed while it was ready but not running (another process may have taken the buffer, or even reassigned it to another block).
- If the buffer is still there and not busy, the **first** process to run marks it busy and removes it from the free list; the others then find it busy and **sleep again**.
- If the buffer was reassigned in the meantime, the block is no longer on the hash queue and the process allocates another free buffer for it.

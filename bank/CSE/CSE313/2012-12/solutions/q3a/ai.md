---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Use a mutex (lock) per buffer/queue instead of raising the processor level: a process locks the hash queue, finds the buffer busy and waits on a condition variable that atomically releases the lock; on a multiprocessor this also works across CPUs."
sources: ["Bach, ch. 3 (getblk, scenario 5); OSTEP ch. 28-30 (locks and condition variables)"]
---
**Yes, it is possible.** Raising/lowering the processor execution level (blocking interrupts) is used because interrupt handlers (e.g. `brelse` called from the disk interrupt) and processes manipulate the same lists; it only works on a **uniprocessor**. Equivalent protection can be obtained with **locks**, provided that interrupt handlers use the same locks (spin locks that also block local interrupts on a multiprocessor, or sleeping locks if the handler runs as a thread).

**Applying a lock in scenario 5** (the block is in the cache, but its buffer is busy):

```c
lock(&hash_queue_lock[h]);                 /* protects the hash queue and the free list */
while (1) {
    buf = search(hash_queue[h], dev, blk);
    if (buf != NULL && buf->busy) {
        buf->wanted = 1;
        cond_wait(&buf->free_cv, &hash_queue_lock[h]);   /* releases the lock, sleeps, re-takes it */
        continue;                                         /* search again (the "while" of getblk) */
    }
    ...
}
```

The `cond_wait` **atomically releases the lock and puts the process to sleep**, so no wakeup can be lost between the test and the sleep (the job the raised processor level did on a uniprocessor); `brelse` takes the same lock, sets `busy = 0` and does `cond_broadcast(&buf->free_cv)`. The process re-checks the condition after waking up.

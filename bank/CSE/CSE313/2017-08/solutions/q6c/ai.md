---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The code deadlocks: down(&empty) is done while holding the mutex, so a producer blocks with the lock held when the buffer is full and no consumer can enter; correct order: down(&empty) before lock."
sources: ["Tanenbaum MOS 4e, sec. 2.3.5 (producer-consumer with semaphores)"]
---
**No, the code does not work correctly.** The producer does `lock(&m)` first and then `down(&empty)`. If the buffer is **full** (`empty == 0`), the producer **blocks in `down(&empty)` while still holding the mutex `m`**. A consumer, which has to take `m` (to remove an item and then `up(&empty)`) can never enter its critical section, so nobody ever does `up(&empty)`: **deadlock** (the producer waits for a consumer, the consumer for the lock).

**Correct producer:** wait for a free slot *before* taking the lock, and release the lock *before* signalling:

```c
semaphore empty = 10;
semaphore full  = 0;
mutex m;

void producer(void) {
    int item;
    while (TRUE) {
        item = produce_item();
        down(&empty);          /* wait for a free slot (without holding m) */
        lock(&m);
        insert_item(item);
        unlock(&m);
        up(&full);             /* one more item available */
    }
}
```

**Corresponding consumer:**

```c
void consumer(void) {
    int item;
    while (TRUE) {
        down(&full);           /* wait for an item (without holding m) */
        lock(&m);
        item = remove_item();
        unlock(&m);
        up(&empty);            /* one more free slot */
        consume_item(item);
    }
}
```

The semaphores `empty` and `full` do the counting/synchronisation; the mutex only protects the buffer structure and is never held while blocking.

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Producer with down(&mutex) before down(&empty) deadlocks when the buffer is full (it holds the mutex while blocked); swap the order of the two downs."
sources: ["Tanenbaum MOS 4e, sec. 2.3.5 (producer-consumer with semaphores)"]
---
**The code does not work (disproved).** The producer executes `down(&mutex)` **before** `down(&empty)`.

**Deadlock scenario.** The buffer is full ($\text{empty}=0$, $\text{full}=5$). The producer takes the mutex (`down(&mutex)`) and then blocks in `down(&empty)` **while holding the mutex**. The consumer executes `down(&full)` (succeeds, since full $>0$) and then `down(&mutex)`, which **blocks** because the producer holds it. The consumer can never reach `up(&empty)`, and the producer will never get past `down(&empty)`: **deadlock**.

(An analogous problem occurs if the consumer takes the mutex before `down(&full)` on an empty buffer. The order in the consumer shown, `down(&full)` first and then `down(&mutex)`, is correct.)

**Correct code:** wait on the counting semaphore **before** taking the mutex, and never block while holding it.

```c
void producer(void) {
    int item;
    while (TRUE) {
        item = produce_item();
        down(&empty);          /* first the counting semaphore */
        down(&mutex);          /* then the mutex */
        insert_item(item);
        up(&mutex);
        up(&full);
    }
}
```

The consumer (`down(&full); down(&mutex); item = remove_item(); up(&mutex); up(&empty);`) is unchanged.

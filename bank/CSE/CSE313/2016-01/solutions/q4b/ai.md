---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Monitor resource_manager with a condition variable: decrease_count waits while available < count; increase_count adds and broadcasts so every waiter re-checks."
sources: ["Tanenbaum MOS 4e, sec. 2.3.7 (monitors); Silberschatz, OS Concepts, ch. 5 (monitors)"]
---
A **monitor** allows only one process at a time to be active inside it (mutual exclusion is automatic) and provides **condition variables** with `wait` and `signal`. The waiting process must not busy-wait.

```c
monitor resource_manager {
    int available_resources = MAX_RESOURCES;
    condition enough;                         /* waiters for more resources */

    void decrease_count(int count) {
        while (available_resources < count)   /* re-test after every wakeup */
            wait(enough);                     /* releases the monitor and sleeps */
        available_resources -= count;
    }

    void increase_count(int count) {
        available_resources += count;
        broadcast(enough);                    /* wake all waiters: each re-checks */
    }
}
```

A process uses it by simply calling `resource_manager.decrease_count(count);`, which returns only when enough resources are available; it later calls `resource_manager.increase_count(count);`.

**Why `while` and `broadcast`.**

- Different waiting processes need **different amounts** `count`; after `increase_count` the available number may satisfy some of them but not others. `broadcast` wakes **all** waiters, and each re-tests its own condition in the `while` loop, so every process that can proceed does, and the others go back to waiting. This **maximises parallelism**: a plain `signal` that wakes just one process could wake one whose request is still too big while a smaller request that could proceed keeps waiting.
- The resources are **used outside the monitor** (the monitor functions only update the counter), so many processes can use their resources in parallel: only the short bookkeeping is serialised.

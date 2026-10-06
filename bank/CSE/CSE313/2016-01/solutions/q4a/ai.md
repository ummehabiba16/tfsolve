---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) the shared counter available_resources; (ii) lines 7-11 of decrease_count (test and subtract) and line 16 of increase_count; (iii) protect both with one binary semaphore."
sources: ["Tanenbaum MOS 4e, sec. 2.3 (race conditions, semaphores); Silberschatz, OS Concepts, ch. 5"]
---
**(i) Data involved:** the shared global variable `available_resources`.

**(ii) Statements responsible.**

- In `decrease_count`: the **test** in line 7 (`if (available_resources < count)`) followed by the **update** in line 10 (`available_resources -= count;`): these two statements are not executed atomically (a check-then-act race), and line 10 is itself a read-modify-write.
- In `increase_count`: line 16 (`available_resources += count;`), another read-modify-write that can interleave with line 10 (and with another call of line 16).

*Example.* With `available_resources = 3`, two processes call `decrease_count(2)` at about the same time: both pass the test in line 7 (3 $\ge$ 2) and then both execute line 10, leaving $-1$. Or an update is lost: both load 3, one stores 1 and one stores 5.

**(iii) Fix with a single binary semaphore** (`mutex`, initial value 1):

```c
#define MAX_RESOURCES 5
int available_resources = MAX_RESOURCES;
semaphore mutex = 1;                      /* binary semaphore */

/* return 0 if sufficient resources available, otherwise -1 */
int decrease_count(int count) {
    int result;
    down(&mutex);                         /* enter critical section */
    if (available_resources < count)
        result = -1;
    else {
        available_resources -= count;
        result = 0;
    }
    up(&mutex);                           /* leave critical section */
    return result;
}

void increase_count(int count) {
    down(&mutex);
    available_resources += count;
    up(&mutex);
}
```

The test and the update of `decrease_count` are now one critical section, and `increase_count` cannot interleave with it; the function still returns 0 if enough resources are available and $-1$ otherwise.

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Each philosopher needs just one of his two forks: protect each fork with a lock/condition and let him take whichever is free; all 5 can eat at once, and no deadlock arises because nobody holds a fork while waiting for another."
sources: ["Tanenbaum MOS 4e, sec. 2.5.1 (dining philosophers), 2.3.7 (monitors)"]
---
**Assumptions.** In this modified problem a philosopher can eat as soon as **one** of his two adjacent forks is available. There are 5 forks, so **at most 5 philosophers can eat simultaneously** (each with a different fork): the target is maximum parallelism.

**Solution (monitor/mutex with condition variables).** `free[f]` records whether fork $f$ is free; philosopher $i$ has the forks $i$ (left) and $(i+1)\bmod5$ (right).

```c
#define N 5
int   free_fork[N] = {1,1,1,1,1};
mutex_t m;                       /* protects free_fork[] only for short periods */
cond_t  can_eat[N];              /* one condition per philosopher */

void philosopher(int i) {
    int f;
    while (TRUE) {
        think();
        lock(&m);
        while (!free_fork[i] && !free_fork[(i+1) % N])   /* both neighbours' forks in use */
            wait(&can_eat[i], &m);
        f = free_fork[i] ? i : (i+1) % N;                /* take whichever is free */
        free_fork[f] = 0;
        unlock(&m);

        eat();                                           /* outside the lock: parallel */

        lock(&m);
        free_fork[f] = 1;                                /* put the fork down */
        signal(&can_eat[f]);                             /* the philosopher on one side */
        signal(&can_eat[(f + N - 1) % N]);               /* ... and on the other side */
        unlock(&m);
    }
}
```

**Properties.**

- **Mutual exclusion on each fork** (`free_fork[f]`).
- **Maximum parallelism:** `eat()` is outside the critical section, and each philosopher takes only one fork, so all 5 can eat together.
- **No deadlock:** a philosopher never holds one fork while waiting for another (no hold-and-wait).
- **Starvation** is possible in principle (the neighbours may keep both forks busy alternately); it can be removed by giving priority to the philosopher who has waited longest (e.g. a FIFO queue of hungry philosophers).

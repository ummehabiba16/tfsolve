---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Binary semaphore (initial 1) for mutual exclusion; counting semaphore (initial N) for a limited resource; semaphore initialised to 0 for ordering/synchronisation."
sources: ["Tanenbaum MOS 4e, sec. 2.3.5 (semaphores)"]
---
Semaphore operations: `down(s)` (wait/P): if $s>0$ decrement, else block; `up(s)` (signal/V): increment $s$ and wake one waiting process, if any.

**(i) Mutual exclusion.** A *binary semaphore* `mutex`, initialised to $1$:

```c
semaphore mutex = 1;

down(&mutex);        // enter critical section
    /* critical section */
up(&mutex);          // leave critical section
```

Only one process at a time can pass the `down`; the others block until the `up`.

**(ii) Access to a limited resource.** A *counting semaphore* `slots`, initialised to the number $N$ of identical resources (e.g. 3 printers or $N$ buffers):

```c
semaphore slots = N;

down(&slots);        // wait until one of the N resources is free
    /* use one resource */
up(&slots);          // release it
```

At most $N$ processes can be inside at the same time; the $(N+1)$-st blocks.

**(iii) Synchronisation (ordering).** To make statement $S_2$ of process $B$ execute only **after** $S_1$ of process $A$, use a semaphore initialised to $0$:

```c
semaphore sync = 0;

/* Process A */          /* Process B */
S1;                      down(&sync);   // blocks until A is done with S1
up(&sync);               S2;
```

If $B$ gets there first it blocks; if $A$ finishes first the `up` makes the semaphore $1$ and $B$'s `down` does not block.

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Ticket lock built on FetchAndSubtract: tickets are handed out by decrementing; the lock is released by decrementing the turn counter."
sources: ["OSTEP ch. 28 (ticket lock with fetch-and-add)"]
---
`FetchAndSubtract` is the mirror image of OSTEP's `FetchAndAdd`, so we can build a **ticket lock** whose counters count *down*. A thread takes a ticket by atomically decrementing `ticket`; it may enter when `turn` equals its ticket; unlocking just decrements `turn`.

```c
typedef struct __lock_t {
    volatile int ticket;   // next ticket to hand out
    volatile int turn;     // ticket currently allowed in
} lock_t;

void lock_init(lock_t *lock) {
    lock->ticket = 0;
    lock->turn   = 0;
}

void lock(lock_t *lock) {
    int myturn = FetchAndSubtract(&lock->ticket);  // returns old value, then ticket--
    while (lock->turn != myturn)
        ;                                          // spin
}

void unlock(lock_t *lock) {
    lock->turn = lock->turn - 1;                   // only the holder writes turn
}
```

**Why it works.**

- The first caller gets ticket $0$ (and `ticket` becomes $-1$), which equals `turn`, so it enters at once.
- The next caller gets ticket $-1$ and spins until the holder's `unlock` makes `turn` $= -1$, and so on. Each thread is served in the order it asked.
- **Mutual exclusion:** `FetchAndSubtract` is atomic, so no two threads get the same ticket, and only the thread whose ticket equals `turn` proceeds.
- **Fairness / no starvation:** tickets are served in FIFO order (a plain test-and-set spinlock gives no such guarantee).
- No thread ever has to undo a failed attempt. A simple "lock = 1, subtract, test for 1" attempt is *not* used: a failed subtract would leave the value wrong and we have no atomic "add back".

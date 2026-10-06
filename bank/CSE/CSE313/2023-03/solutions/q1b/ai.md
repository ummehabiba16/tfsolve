---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Best case 4A+C; worst case 4A+3C+T with a spinlock (the waiting thread burns a whole slice); with a queue-based lock the T term disappears: 4A+3C."
sources: ["OSTEP ch. 28 (Locks), spin locks and queue locks"]
---
Let thread $T_1$ run first and $T_2$ second. `do_something()` takes no time, so each thread costs one lock ($A$) and one unlock ($A$).

**i. Best case.** $T_1$ locks, unlocks and finishes inside its slice; one context switch; then $T_2$ does the same.

$$A + A + C + A + A = \mathbf{4A + C}$$

**ii. Worst case (at most three context switches, spinlock).**

1. $T_1$ acquires the lock: $A$.
2. The timer fires before $T_1$ unlocks: context switch to $T_2$: $C$.
3. $T_2$ tries to lock and **spins for its entire slice**, achieving nothing: $T$.
4. Context switch back to $T_1$: $C$.
5. $T_1$ unlocks: $A$ (it is done).
6. Context switch to $T_2$: $C$.
7. $T_2$ locks and unlocks: $A + A$.

$$A + C + T + C + A + C + 2A = \mathbf{4A + 3C + T}$$

**iii. Queue-based lock.** When $T_2$ finds the lock held it puts itself on the lock's wait queue and sleeps (yields the CPU) instead of spinning, so the wasted slice $T$ disappears. The sequence is: $T_1$ lock ($A$), switch ($C$), $T_2$ tries the lock, enqueues and sleeps ($A$), switch back ($C$), $T_1$ unlock hands the lock to $T_2$ ($A$), switch ($C$), $T_2$ unlocks ($A$):

$$\mathbf{4A + 3C}$$

The worst case no longer depends on the time slice $T$; it is shorter by $T$ (the whole time $T_2$ would have spun).

*Assumption:* a spinning thread never yields before its slice ends; lock hand-off in the queue lock costs no extra $A$.

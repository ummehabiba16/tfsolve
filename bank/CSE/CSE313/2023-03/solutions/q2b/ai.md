---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Yes, deadlock is possible: T1 holds A needs B, T2 holds B needs C, T3 holds C needs D, T4 holds D needs A (circular wait)."
sources: ["OSTEP ch. 32 (deadlock)", "Tanenbaum MOS 4e, sec. 6.2"]
---
**Yes.** The four threads form a ring of lock dependencies $A\!-\!B$, $B\!-\!C$, $C\!-\!D$, $D\!-\!A$. Suppose each thread acquires its *first* lock and is then preempted:

- Thread 1 holds **A**, waits for **B**
- Thread 2 holds **B**, waits for **C**
- Thread 3 holds **C**, waits for **D**
- Thread 4 holds **D**, waits for **A**

This is a circular wait $T_1\to T_2\to T_3\to T_4\to T_1$; mutual exclusion, hold-and-wait and no-preemption also hold, so all four Coffman conditions are met and the threads deadlock. (It can be prevented by a global lock order, e.g. always acquire in alphabetical order A, B, C, D.)

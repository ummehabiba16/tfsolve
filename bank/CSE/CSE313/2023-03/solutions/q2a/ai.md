---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Use two semaphores so B stores after A (and after B has loaded): counter = 2. To avoid 3, make both load before either stores."
sources: ["Tanenbaum MOS 4e, sec. 2.3.5 (semaphores)"]
---
Without synchronisation the possible final values are 1, 2 or 3: the result is 3 only when the two read-modify-write sequences do not overlap; 1 or 2 when one update is lost.

**i. Final value 2.** We must lose A's update and let B's value be the last store, i.e. B must have loaded `counter = 0` and must store after A. Use two semaphores, both initialised to $0$:

| Process A | Process B |
|:--|:--|
| `LOAD (counter, R0)` | `LOAD (counter, R0)` |
| `ADD (R0, 1, R0)` | `up(s1)` |
| `down(s1)` | `ADD (R0, 2, R0)` |
| `STORE (R0, counter)` | `down(s2)` |
| `up(s2)` | `STORE (R0, counter)` |

*Check.* B loads $0$ and then does `up(s1)`; A cannot store until `s1` is up, and B cannot store until A has stored (`s2`). So A's `LOAD` sees $0$ (nobody has stored yet) and stores $1$; B then stores $0+2$. Final value: $\mathbf{counter = 2}$ in every execution (no deadlock: the waits are satisfied in order).

**ii. Final value not 3.** The value is 3 only if one process finishes its `STORE` before the other `LOAD`s. Force both loads to happen before either store. Semaphores `a = b = 0`:

| Process A | Process B |
|:--|:--|
| `LOAD (counter, R0)` | `LOAD (counter, R0)` |
| `ADD (R0, 1, R0)` | `ADD (R0, 2, R0)` |
| `up(a)` | `up(b)` |
| `down(b)` | `down(a)` |
| `STORE (R0, counter)` | `STORE (R0, counter)` |

Both processes have read $0$ before either stores, so the final value is $1$ or $2$ (whichever stores last), **never 3**.

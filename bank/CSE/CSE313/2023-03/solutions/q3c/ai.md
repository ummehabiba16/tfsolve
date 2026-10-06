---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Broken because if is used instead of while around cond_wait (Mesa semantics): a woken consumer can find count==0 after another consumer stole the item."
sources: ["OSTEP ch. 30 (condition variables, broken solution with if)"]
---
**Why it is broken.** Both functions test the condition with `if` and then `cond_wait`. With **Mesa semantics** (signal only moves the waiter to the ready queue; it does not hand over the mutex), the state may change between the signal and the moment the woken thread runs again. The woken thread does **not** re-check the condition (`if` instead of `while`), so it proceeds even though the condition is false again.

**Interleaving** (one producer $P$, two consumers $C_1$, $C_2$; `count = 0` initially):

| Step | Thread | Line | Effect |
|:-:|:-:|:--|:--|
| 1 | $C_1$ | c1, c2 | locks the mutex, sees `count == 0` |
| 2 | $C_1$ | c3 | `cond_wait(&full)`: releases the mutex and sleeps |
| 3 | $P$ | p1-p4 | locks, `count != MAX`, puts an item: `count = 1` |
| 4 | $P$ | p5, p6 | `cond_signal(&full)`: $C_1$ becomes *ready* (not running); unlocks |
| 5 | $C_2$ | c1, c2 | gets the mutex first, `count == 1` so it does **not** wait |
| 6 | $C_2$ | c4-c6 | `get()` takes the item: `count = 0`; signals; unlocks |
| 7 | $C_1$ | c3 returns, then c4 | re-acquires the mutex and goes straight to `get()` although `count == 0` |

In step 7 $C_1$ reads from an empty buffer (underflow: garbage or an invalid item).

**Fix.** Use `while` instead of `if` in both functions (re-test after every wakeup):

```c
while (count == 0)
    cond_wait(&full, &mutex);
```

The code already uses two condition variables (`empty`, `full`), so a consumer only wakes a producer and vice versa; with a single CV and `if` there is a second failure (a consumer may wake another consumer and all threads can sleep).

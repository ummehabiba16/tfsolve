---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Copy propagation: after x = y, use y for later uses of x (e.g. x = t1; a[t2] = t3; a[t4] = x becomes a[t4] = t1, and x = t1 becomes dead). Code motion: move a loop-invariant computation out of the loop, e.g. while (i <= limit - 2) becomes t = limit - 2; while (i <= t)."
sources: ["KMS Chapter 9 slides 21-23 (Copy Propagation), 27 (Code Motion)", "Dragon book 2e sec. 9.1.5-9.1.6"]
---
**(i) Copy propagation.** After a copy statement `u = v`, use `v` instead of `u` in later statements (as long as neither is reassigned in between). The copy often becomes dead and can be removed.

Example (from the textbook's quicksort block):

```text
Before:                 After copy propagation:     After dead-code elimination:
x = t3                  x = t3                      a[t2] = t5
a[t2] = t5              a[t2] = t5                  a[t4] = t3
a[t4] = x               a[t4] = t3
goto B2                 goto B2                     goto B2
```

Once `a[t4] = x` uses `t3` directly, `x` is no longer used (assuming it is dead after the block), so `x = t3` is removed. One instruction is saved.

**(ii) Code motion.** A computation whose result does not change from one loop iteration to the next (**loop-invariant**) is moved to just before the loop, so it is evaluated once instead of on every iteration.

Example:

```text
Before:                         After:
while (i <= limit - 2) {        t = limit - 2;
    a[i] = 0;                   while (i <= t) {
    i = i + 1;                      a[i] = 0;
}                                   i = i + 1;
                                }
```

`limit` does not change inside the loop, so `limit - 2` is computed once. If the loop runs $n$ times, $n - 1$ subtractions are saved.

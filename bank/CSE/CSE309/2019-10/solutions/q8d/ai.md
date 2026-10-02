---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Copy propagation: after a copy x = y, uses of x are replaced by y, which often makes the copy dead (e.g. after CSE: t = a + b; x = t; y = x \\* 2 becomes y = t \\* 2 and x = t is removed). Code motion: a loop-invariant computation is moved before the loop, e.g. while (i <= limit - 2) becomes t = limit - 2; while (i <= t), so it is computed once instead of on every iteration."
sources: ["KMS Chapter 9 slides 21-23 (Copy Propagation), 27 (Code Motion)", "Dragon book 2e sec. 9.1.5-9.1.6"]
---
**(i) Copy propagation.** After a copy statement `u = v`, use `v` instead of `u` wherever possible (as long as neither is reassigned in between). This alone does not shorten the code, but it often makes the copy itself **dead**, so dead-code elimination can remove it.

Example (textbook): common-subexpression elimination of `d + e` introduces copies.

```text
Before:                 After CSE:               After copy propagation
                                                 and dead-code elimination:
a = d + e               t = d + e                t = d + e
b = d + e               a = t                    c = t + 4
c = b + 4               b = t                    (a = t, b = t removed if
                        c = b + 4                 a, b are not used later)
```

In the third column, `c = b + 4` became `c = t + 4`, after which the copies `a = t` and `b = t` are dead (assuming `a` and `b` are not used later).

**(ii) Code motion.** An expression that yields the **same result every time a loop is executed (loop-invariant)** is moved out of the loop, to a point before the loop (the preheader). It is then evaluated once instead of on every iteration.

Example (textbook):

```text
Before:                         After:
while (i <= limit - 2) {        t = limit - 2;
    ...                         while (i <= t) {
}                                   ...
                                }
```

Provided `limit` is not changed in the loop, `limit - 2` is computed once. A loop that runs 1000 times saves 999 subtractions. The moved computation must be safe: it must not change the program's meaning (for example, it should not be executed when the loop would not have executed it at all, if it could cause an error).

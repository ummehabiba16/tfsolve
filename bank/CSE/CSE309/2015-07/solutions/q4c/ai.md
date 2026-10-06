---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Copy propagation replaces uses of x after x = y by y; dead-code elimination removes statements whose results are never used; induction-variable elimination (with strength reduction) replaces i and t = 4*i by the single variable t with t = t + 4 and a test against a precomputed limit."
sources: ["KMS Chapter 9 slides 21-35 (copy propagation, dead-code elimination, induction variables)", "Dragon book 2e sec. 9.1.5-9.1.8"]
---
**Copy propagation** (sec. 9.1.5). After a copy statement `x = y`, uses of `x` are replaced by `y` as long as neither is redefined in between. It does not shorten the code by itself, but it often makes the copy dead.

```text
x = y                    x = y
z = x + 1     ==>        z = y + 1       (x = y may now be dead and removed)
```

**Dead-code elimination** (sec. 9.1.6). A statement that computes a value that is never used afterwards (the variable is *dead*) is removed. Dead code often comes from copy propagation or from debugging flags that are always false.

```text
x = y                    z = y + 1       (after propagation x is dead, so x = y is deleted)
z = y + 1     ==>
```

**Induction-variable elimination** (sec. 9.1.8). A variable whose value changes by a constant in every iteration of a loop (an *induction variable*) can often be removed when another variable moves in lock step with it. In

```text
L:  t = 4 * i               t = 0 ; limit = 4 * n
    a[t] = 0          ==>   L:  a[t] = 0
    i = i + 1                    t = t + 4
    if i < n goto L              if t < limit goto L
```

$i$ and $t = 4i$ both are induction variables. *Strength reduction* replaces the multiplication $4 * i$ by $t = t + 4$ (initialised before the loop). The remaining use of $i$ is the test `i < n`, which is rewritten as `t < 4*n`; the limit `4*n` is computed once before the loop. Now $i$ is dead and **eliminated**: the loop has one addition and one comparison, and no multiplication.

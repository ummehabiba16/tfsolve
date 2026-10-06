---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Leader statements: the first statement, any statement that is the target of a jump, and any statement that follows a jump; each starts a basic block. Global CSE: an expression computed on every path to a point with unchanged operands is not recomputed. Copy propagation replaces uses of x after x = y by y, and dead-code elimination deletes statements whose result is never used. Induction-variable elimination replaces i and 4*i by one variable t with t = t + 4 and rewrites the loop test."
sources: ["KMS Chapter 8 slides 27-36; Chapter 9 slides 10-35", "Dragon book 2e sec. 8.4.1, 9.1.4-9.1.8"]
---
**(i) Leader statements** (Dragon book sec. 8.4.1). The leaders are the first statements of the basic blocks:

1. the **first** statement of the program;
2. every statement that is the **target of a jump** (conditional or unconditional);
3. every statement that **immediately follows a jump**.

A basic block is a leader and all statements up to, but not including, the next leader.

```text
 1:  i = 1                 <- leader (first statement)
 2:  t = i * 4             <- leader (target of the jump in 5)
 3:  a[t] = 0
 4:  i = i + 1
 5:  if i <= 10 goto 2
 6:  x = a[0]              <- leader (follows a jump)
```

Basic blocks: $\{1\}$, $\{2, 3, 4, 5\}$, $\{6\}$.

**(ii) Global common-subexpression elimination** (sec. 9.1.4). An expression $x + y$ is a common subexpression at a point if it was **computed on every path** reaching that point and the values of $x$ and $y$ have **not changed** since. Its earlier value is then reused instead of being recomputed, possibly through a new temporary, across basic blocks.

```text
B1:  a = x + y           B1:  t = x + y
B2:  ...                      a = t
B3:  ...         ==>     B2/B3: (no change to x or y)
B4:  c = x + y           B4:  c = t
```

**(iii) Copy propagation and dead-code elimination** (sec. 9.1.5-9.1.6). *Copy propagation*: after a copy `x = y`, uses of `x` are replaced by `y` while neither is redefined. *Dead-code elimination*: a statement is removed if the variable it defines is **dead** (never used afterwards). Copy propagation often makes the copy dead, so the two work together:

```text
x = y                     (x = y deleted: x is no longer used)
z = x + 1     ==>         z = y + 1
```

**(iv) Induction-variable elimination** (sec. 9.1.8). In

```text
L:  t = 4 * i               t = 0 ; limit = 4 * n
    a[t] = 0          ==>   L:  a[t] = 0
    i = i + 1                    t = t + 4
    if i < n goto L              if t < limit goto L
```

$i$ and $t = 4 * i$ change by a constant in every iteration (*induction variables*). The multiplication is replaced by an addition (*strength reduction*), and the only other use of $i$, the test `i < n`, is rewritten as `t < limit`, where `limit = 4 * n` is computed once before the loop. Then $i$ is dead and is **eliminated**.

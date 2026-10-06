---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A semantics-preserving transformation changes the code but not the computed result. CSE: a = b + c; b = a - d; c = b + c; d = a - d becomes d = b. Strength reduction: x * 2 or 4 * i becomes x + x or t = t + 4. Backward copy propagation: t = a + b; x = t becomes x = a + b. Constant folding: x = 2 * 3.14 becomes x = 6.28."
sources: ["KMS Chapter 9 slides 10-35; Chapter 8 slides 40-50", "Dragon book 2e sec. 9.1, 8.5.1, 9.1.8, 9.4"]
---
**Semantics-preserving transformation.** A code-improving transformation that **does not change what the program computes** (its output and side effects) for any input, while making it faster or smaller (Dragon book sec. 9.1). Every optimization must be semantics preserving; otherwise it is wrong however fast the result is.

**(i) Common-subexpression elimination.** An expression computed earlier whose operands have not changed is not recomputed; its earlier value is reused (Dragon book sec. 8.5.1, 9.1.4). Local example in one basic block:

```text
a = b + c            a = b + c
b = a - d            b = a - d
c = b + c     ==>    c = b + c
d = a - d            d = b
```

The 2nd and 4th statements compute the same value `a - d` (neither `a` nor `d` changed between them), so the fourth becomes `d = b`. The 1st and 3rd do not match, since `b` changed in between.

**(ii) Strength reduction.** Replace an expensive operation by a cheaper equivalent one. Examples: `x * 2` $\to$ `x + x` (or `x << 1`), `x * x` for `x^2`; in loops, the multiplication in an induction variable is replaced by an addition (sec. 9.1.8):

```text
for (i = 0; i < n; i++) { t = 4 * i; ... }   ==>   t = 0;  ... t = t + 4;   (in the loop)
```

**(iii) Backward copy propagation.** Ordinary (forward) copy propagation replaces a use of `x` after the copy `x = y` by `y`. *Backward* copy propagation works in the opposite direction: for `t = e; x = t;` where `t` is used nowhere else, the **target of the computation is propagated backwards**, so that `e` is computed directly into `x` and the copy disappears:

```text
t = a + b        x = a + b
x = t      ==>   (t is gone, one statement and one temporary less)
```

**(iv) Constant folding.** An expression whose operands are all constants is evaluated by the compiler and replaced by its value:

```text
x = 2 * 3.14;    ==>   x = 6.28;
if (3 > 5) ...   ==>   (false: the branch is removed)
```

Folded constants can be propagated further (constant propagation), which allows more folding and dead-code elimination.

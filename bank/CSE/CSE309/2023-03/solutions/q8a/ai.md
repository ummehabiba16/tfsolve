---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "t3 = i\\*8 is a common subexpression (t4 = B[t1]); t1 = 8i is a derived induction variable, so replace the multiplication by t1 = t1 + 8 (initialised t1 = 0) and eliminate i by testing t1 < t6 with t6 = 8\\*n computed before the loop. Result: dp = 0; t1 = 0; t6 = n \\* 8; L: t2 = A[t1]; t4 = B[t1]; t5 = t2 \\* t4; dp = dp + t5; t1 = t1 + 8; if t1 < t6 goto L."
sources: ["KMS Chapter 9 slides 10-35 (Common-Subexpression Elimination, Induction Variables and Strength Reduction)", "Dragon book 2e sec. 9.1.4-9.1.8"]
---
**Assumptions.** `n` is not changed in the loop, `8*n` does not overflow, and the loop body executes at least once (as the code is written: the test is at the bottom). Arrays have 8-byte elements, as the code shows.

**1. Common-subexpression elimination.** `t3 = i * 8` recomputes `t1 = i * 8` (`i` has not changed in between). Remove it and use `t1`: `t4 = B[t1]`.

**2. Reduction in strength.** `i` is a basic induction variable (`i = i + 1` once per iteration), and `t1 = 8 * i` is an induction variable in the same family. Instead of multiplying, keep `t1` up to date by adding 8 each time `i` increases:

- initialise `t1 = 0` before the loop (since `i = 0`);
- replace `t1 = i * 8` by `t1 = t1 + 8` placed right after `i = i + 1`.

**3. Induction-variable elimination.** Now `i` is used only in the test `i < n`. Since $t_1 = 8i$ at that point, the test is equivalent to $t_1 < 8n$. Compute `t6 = n * 8` once before the loop (loop-invariant) and test `t1 < t6`. Then `i = 0` and `i = i + 1` are dead and removed.

**Optimised code:**

```text
    dp = 0
    t1 = 0
    t6 = n * 8
L:  t2 = A[t1]
    t4 = B[t1]
    t5 = t2 * t4
    dp = dp + t5
    t1 = t1 + 8
    if t1 < t6 goto L
```

The loop body went from 8 instructions with 2 multiplications by 8 to 6 instructions with only the real multiplication `t2 * t4`. Check: at the top of iteration $k$ (starting from 0), `t1` $= 8k$, as before. After the increment, `t1` $= 8(k+1)$, and `t1 < 8n` holds exactly when $k + 1 < n$, which is the original test `i < n` with `i` $= k + 1$.

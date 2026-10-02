---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Global CSE (4\\*i -> t2, 4\\*j -> t4, 4\\*n -> t1, a[t2] -> t3, a[t4] -> t5, a[t1] -> v), copy propagation (x = t3), dead-code elimination, code motion of v = a[t1] out of the B2 loop, strength reduction (t2 = t2 + 4, t4 = t4 - 4) and induction-variable elimination (test t2 >= t4). Final: B1: i = m-1; t1 = 4\\*n; t2 = 4\\*i; t4 = t1;  B2: t2 = t2+4; t3 = a[t2]; if t3 < v goto B2 (v = a[t1] in a preheader);  B3: t4 = t4-4; t5 = a[t4]; if t5 > v goto B3;  B4: if t2 >= t4 goto B6;  B5: a[t2] = t5; a[t4] = t3; goto B2;  B6: a[t2] = v; a[t1] = t3."
sources: ["KMS Chapter 9 slides 9-35 (Semantic-Preserving Transformations)", "Dragon book 2e sec. 9.1 (Figs. 9.5-9.9)"]
---
This is the textbook quicksort fragment. Apply the transformations step by step.

**1. Global common-subexpression elimination (CSE).**

- In B5, `t6 = 4*i` and `t7 = 4*i` compute the same value as `t2 = 4*i` in B2: `i` is not changed on any path B2 $\to$ B3 $\to$ B4 $\to$ B5. Similarly `t8 = 4*j` and `t10 = 4*j` equal `t4` from B3. So `t6`, `t7` become `t2`, and `t8`, `t10` become `t4`.
- In B6, `t11`, `t12` become `t2`, and `t13 = 4*n`, `t15 = 4*n` become `t1` (from B1; `n` never changes).
- Array loads: `a` is not stored on the paths B2 $\to$ B3 $\to$ B4 $\to$ B5/B6. So `x = a[t6]` = `a[t2]` = `t3`; `t9 = a[t8]` = `a[t4]` = `t5`; in B6 `x = a[t11]` = `t3` and `t14 = a[t13]` = `a[t1]` = `v` (computed in B2 on every pass).

```text
B5: x = t3              B6: x = t3
    a[t2] = t5              t14 = v
    a[t4] = x               a[t2] = t14
    goto B2                 a[t1] = x
```

**2. Copy propagation.** After the copies `x = t3` and `t14 = v`, use `t3` and `v` directly: `a[t4] = t3`, `a[t2] = v`, `a[t1] = t3`.

**3. Dead-code elimination.** `x`, `t14`, `t6` to `t13` and `t15` are no longer used, so their assignments are removed.

**4. Code motion.** In the self-loop of B2, `v = a[t1]` is loop-invariant: `t1` does not change and `a` is not stored inside B2. Move it to a new preheader block that runs before the loop is entered (from B1 and from B5). It cannot go to B1, because B5 stores into `a`, which may change `a[t1]` between outer-loop iterations.

**5. Strength reduction of induction variables.**

- In B2, `i` is an induction variable (`i = i + 1`) and `t2 = 4*i` is a derived induction variable. Replace the multiplication with `t2 = t2 + 4`, initialising `t2 = 4*i` in B1.
- In B3, `j = j - 1` and `t4 = 4*j` give `t4 = t4 - 4`, initialised in B1 to `4*j` = `4*n` = `t1`.

**6. Induction-variable elimination.** After step 5, `i` and `j` are used only in the test `if i >= j goto B6`. Since $t_2 = 4i$ and $t_4 = 4j$, the test is equivalent to `if t2 >= t4 goto B6`. Then `i = i + 1`, `j = j - 1` and `j = n` are dead and removed (`i = m - 1` stays only to initialise `t2`).

**Optimised flow graph:**

```text
B1:  i = m - 1
     t1 = 4 * n
     t2 = 4 * i
     t4 = t1
B2': v = a[t1]                  (preheader, entered from B1 and B5)
B2:  t2 = t2 + 4
     t3 = a[t2]
     if t3 < v goto B2
B3:  t4 = t4 - 4
     t5 = a[t4]
     if t5 > v goto B3
B4:  if t2 >= t4 goto B6
B5:  a[t2] = t5
     a[t4] = t3
     goto B2'
B6:  a[t2] = v
     a[t1] = t3
```

| Transformation | Where |
|:--|:--|
| Common-subexpression elimination | `4*i`, `4*j`, `4*n`, `a[t2]`, `a[t4]`, `a[t1]` in B5, B6 |
| Copy propagation | `x = t3`, `t14 = v` |
| Dead-code elimination | `x`, `t6`-`t15`, `i`/`j` updates |
| Code motion | `v = a[t1]` out of the B2 loop |
| Reduction in strength | `t2 = t2 + 4`, `t4 = t4 - 4` |
| Induction-variable elimination | test `i >= j` replaced by `t2 >= t4` |

---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "With a, b, c, d live and t, u, v dead on exit (temporaries), backward scan: (1) t = a - b: t live nu 3, a live nu 2, b live; (2) u = a - c: u live nu 3, a dead (redefined in 4), c live; (3) v = t + u: v live nu 5, t dead, u live nu 5; (4) a = d: a live, d dead (redefined in 5); (5) d = v + u: d live, v dead, u dead."
sources: ["KMS Chapter 8 slides 37-39 (Liveliness and Next-Use Information)", "Dragon book 2e sec. 8.4.2 (Algorithm 8.7)"]
---
**Assumptions.** The question does not give liveness on exit. As in the textbook's example of this block, `t`, `u`, `v` are temporaries (**dead on exit**) and `a`, `b`, `c`, `d` are **live on exit**.

**Algorithm 8.7.** Scan backwards. For statement $i$: `x = y op z` (or `x = y`):

1. attach the current information of `x`, `y`, `z` to $i$;
2. set `x` to dead, no next use;
3. set `y` and `z` to live, next use $i$.

**Symbol table after each step** (L = live, D = dead; next use in brackets, "-" = none in the block):

| After processing | a | b | c | d | t | u | v |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| initial (exit) | L(-) | L(-) | L(-) | L(-) | D | D | D |
| 5: `d = v + u` | L(-) | L(-) | L(-) | D | D | L(5) | L(5) |
| 4: `a = d` | D | L(-) | L(-) | L(4) | D | L(5) | L(5) |
| 3: `v = t + u` | D | L(-) | L(-) | L(4) | L(3) | L(3) | D |
| 2: `u = a - c` | L(2) | L(-) | L(2) | L(4) | L(3) | D | D |
| 1: `t = a - b` | L(1) | L(1) | L(2) | L(4) | D | D | D |

**Liveness and next-use attached to each statement:**

| Statement | Result | Operands |
|:--|:--|:--|
| 1: `t = a - b` | t: live, next use 3 | a: live, next use 2; b: live, no next use |
| 2: `u = a - c` | u: live, next use 3 | a: **dead** (redefined in 4); c: live, no next use |
| 3: `v = t + u` | v: live, next use 5 | t: dead after 3; u: live, next use 5 |
| 4: `a = d` | a: live, no next use | d: dead (redefined in 5) |
| 5: `d = v + u` | d: live, no next use | v: dead after 5; u: dead after 5 |

On entry, `a`, `b`, `c`, `d` are live. No statement is dead here. A code generator can use this information to free the registers of `t` after statement 3, `a` after statement 2 (its value is still in memory), and `u` and `v` after statement 5.

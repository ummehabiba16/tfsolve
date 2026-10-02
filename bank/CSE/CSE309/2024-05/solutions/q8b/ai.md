---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Scanning backwards with a, b, c, d live and t, u, v dead on exit: (5) d = t + v: d live, t dead, v dead; (4) a = u + t: a live, u dead, t live nu 5; (3) t = a + b: t live nu 4, a dead, b live; (2) u = d - b: u live nu 4, d dead, b live nu 3; (1) t = a - c: t dead, a live nu 3, c live. Statement 1 assigns a dead t, so it is dead code. On entry a, b, c, d and v are live."
sources: ["KMS Chapter 8 slides 37-39 (Liveliness and Next-Use Information)", "Dragon book 2e sec. 8.4.2 (Algorithm 8.7)"]
---
**Assumptions.** As stated, `a`, `b`, `c`, `d` are live on exit (next use: none in the block) and `t`, `u`, `v` are dead on exit. `v` is used in statement 5 without a definition in the block, so it must come from before the block (it is live on entry).

**Algorithm 8.7** (scan the block backwards). For statement $i$: `x = y op z`:

1. Attach to $i$ the information currently in the symbol table for `x`, `y`, `z`.
2. Set `x` to "not live, no next use".
3. Set `y` and `z` to "live, next use $i$".

Step 2 must be done before step 3, in case `x` is also an operand.

**Symbol table at each step** (L = live, D = dead; next use in brackets, "-" = none):

| After processing | a | b | c | d | t | u | v |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| initial (exit) | L(-) | L(-) | L(-) | L(-) | D | D | D |
| 5: `d = t + v` | L(-) | L(-) | L(-) | D | L(5) | D | L(5) |
| 4: `a = u + t` | D | L(-) | L(-) | D | L(4) | L(4) | L(5) |
| 3: `t = a + b` | L(3) | L(3) | L(-) | D | D | L(4) | L(5) |
| 2: `u = d - b` | L(3) | L(2) | L(-) | L(2) | D | D | L(5) |
| 1: `t = a - c` | L(1) | L(2) | L(1) | L(2) | D | D | L(5) |

**Information attached to each statement** (the table entry *before* the statement was processed):

| Statement | Result (x) | Operand y | Operand z |
|:--|:--|:--|:--|
| 1: `t = a - c` | t: **dead**, no next use | a: live, next use 3 | c: live, no next use |
| 2: `u = d - b` | u: live, next use 4 | d: **dead** (redefined in 5) | b: live, next use 3 |
| 3: `t = a + b` | t: live, next use 4 | a: **dead** (redefined in 4) | b: live, no next use |
| 4: `a = u + t` | a: live, no next use | u: **dead** after this | t: live, next use 5 |
| 5: `d = t + v` | d: live, no next use | t: dead after this | v: dead after this |

**Observations:**

- Statement 1 assigns `t`, but `t` is dead there: it is redefined in statement 3 before any use. **Statement 1 is dead code** and can be removed.
- On entry to the block, `a`, `b`, `c`, `d` and `v` are live.

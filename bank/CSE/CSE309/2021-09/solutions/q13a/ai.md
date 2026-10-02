---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Taking a, b, c, d live and t, u, v dead on exit, a backward scan gives: (1) t = a + b: t dead, a live nu 4, b live nu 3; (2) u = c + d: u dead, c live nu 4, d live nu 3; (3) t = d - b: t live nu 5, d dead, b live; (4) v = a + c: v live nu 5, a live, c live; (5) d = t + v: d live, t and v dead. Statements 1 and 2 assign dead variables, so they are dead code; next-use information shows this and also lets the code generator free a register as soon as its value has no next use."
sources: ["KMS Chapter 8 slides 37-39 (Liveliness and Next-Use Information)", "Dragon book 2e sec. 8.4.2 (Algorithm 8.7)"]
---
**Assumptions.** The question does not say which variables are live on exit. Following the convention of Q13(b) and of other years, take `t`, `u`, `v` to be temporaries (**dead on exit**) and `a`, `b`, `c`, `d` to be **live on exit** (next use outside the block).

**Algorithm 8.7.** Scan backwards. At statement $i$: `x = y op z`:

1. attach the current table entries of `x`, `y`, `z` to statement $i$;
2. set `x` to dead, no next use;
3. set `y` and `z` to live, next use $i$.

**State of the symbol table at each step** (L = live, D = dead, next use in brackets, "-" = none in the block):

| After processing | a | b | c | d | t | u | v |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| initial (block exit) | L(-) | L(-) | L(-) | L(-) | D | D | D |
| 5: `d = t + v` | L(-) | L(-) | L(-) | D | L(5) | D | L(5) |
| 4: `v = a + c` | L(4) | L(-) | L(4) | D | L(5) | D | D |
| 3: `t = d - b` | L(4) | L(3) | L(4) | L(3) | D | D | D |
| 2: `u = c + d` | L(4) | L(3) | L(2) | L(2) | D | D | D |
| 1: `t = a + b` | L(1) | L(1) | L(2) | L(2) | D | D | D |

**Liveness and next-use information attached to each statement** (the entry before that statement was processed):

| Statement | Result | Operand 1 | Operand 2 |
|:--|:--|:--|:--|
| 1: `t = a + b` | t: **dead** | a: live, next use 4 | b: live, next use 3 |
| 2: `u = c + d` | u: **dead** | c: live, next use 4 | d: live, next use 3 |
| 3: `t = d - b` | t: live, next use 5 | d: dead after 3 | b: live, no next use |
| 4: `v = a + c` | v: live, next use 5 | a: live, no next use | c: live, no next use |
| 5: `d = t + v` | d: live, no next use | t: dead after 5 | v: dead after 5 |

**How next-use information helps optimisation (6 marks):**

1. **Dead-code elimination.** In statement 1, `t` is dead: it is overwritten in statement 3 before any use. In statement 2, `u` is dead (never used, and a temporary). Both statements can be **deleted**, and the block shrinks to `t = d - b; v = a + c; d = t + v`.
2. **Register allocation and code generation.** When a variable has **no next use** and is dead, its register can be **reused immediately**, with no store. After statement 5, `t` and `v` are dead, so their registers are free and are never stored. In statement 3, `d` has no next use in its old value, so its register can hold `t`. Live variables with no further next use (`a`, `c` after statement 4) need not stay in registers, but must be in memory at the exit.
3. **Choosing which register to spill.** The variable whose next use is **furthest away** (or that has none) is the best one to evict.

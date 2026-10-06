---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Taking unary minus to bind tighter than +: t1 = b + c; t2 = minus t1; t3 = minus d; t4 = t2 + t3; a = t4. Triples: (0) + b c; (1) minus (0); (2) minus d; (3) + (1) (2); (4) = a (3)."
sources: ["KMS Chapter 6 slides 20-36 (three-address code, triples), 52-62 (translation of expressions)", "Dragon book 2e sec. 6.2.1-6.2.3, 6.4.1, Fig. 6.19"]
---
**Assumptions.** $-$ in front of $(b+c)$ and in front of $d$ is the unary minus, which binds tighter than $+$, so the expression is $a = (-(b + c)) + (-d)$. Temporaries $t_1, t_2, \ldots$ are numbered in the order `new Temp()` is evaluated (bottom-up, left to right).

**Parse.** $S \to \textbf{id}\,{=}\,E$ with $E \to E_1 + E_2$, $E_1 \to -E_3$, $E_3 \to (E_4)$, $E_4 \to E_5 + E_6$ with $E_5 \to \textbf{id}_b$, $E_6 \to \textbf{id}_c$; and $E_2 \to -E_7$, $E_7 \to \textbf{id}_d$.

**Bottom-up evaluation with the SDD:**

| Node | Rule used | $E.addr$ | Code contributed |
|:--|:--|:-:|:--|
| $E_5$ ($b$) | $E \to \textbf{id}$ | `b` | (none) |
| $E_6$ ($c$) | $E \to \textbf{id}$ | `c` | (none) |
| $E_4$ ($b + c$) | $E \to E_1 + E_2$ | `t1` | `t1 = b + c` |
| $E_3$ | $E \to (E_1)$ | `t1` | (copies $E_4.code$) |
| $E_1$ ($-(b+c)$) | $E \to -E_1$ | `t2` | `t2 = minus t1` |
| $E_7$ ($d$) | $E \to \textbf{id}$ | `d` | (none) |
| $E_2$ ($-d$) | $E \to -E_1$ | `t3` | `t3 = minus d` |
| $E$ ($E_1 + E_2$) | $E \to E_1 + E_2$ | `t4` | `t4 = t2 + t3` |
| $S$ | $S \to \textbf{id} = E$ | | `a = t4` |

**Three-address code:**

```text
t1 = b + c
t2 = minus t1
t3 = minus d
t4 = t2 + t3
a  = t4
```

**Triples** (a triple has operator, arg1, arg2; a reference to an earlier triple is its number in parentheses; the temporaries disappear):

| # | op | arg1 | arg2 |
|:-:|:-:|:-:|:-:|
| (0) | `+` | `b` | `c` |
| (1) | `minus` | `(0)` | |
| (2) | `minus` | `d` | |
| (3) | `+` | `(1)` | `(2)` |
| (4) | `=` | `a` | `(3)` |

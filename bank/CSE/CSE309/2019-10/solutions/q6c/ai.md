---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "A quadruple has four fields (op, arg1, arg2, result) and names results explicitly with temporaries; a triple has only (op, arg1, arg2) and refers to a result by the position of the triple that computes it. For a = b \\* -c + b \\* -c: quads use t1-t5, triples (0)-(5) refer to (0), (1), ... Problem in an optimizing compiler: moving an instruction changes its position, so every triple that refers to it must be changed; quadruples (or indirect triples) avoid this."
sources: ["KMS Chapter 6 slides 29-34 (Representing Three Address Code, Quadruples, Triples, Indirect Triples)", "Dragon book 2e sec. 6.2.2-6.2.3 (Figs. 6.10, 6.11)"]
---
**Difference (5 marks).**

- A **quadruple** has four fields: `op`, `arg1`, `arg2`, `result`. Results are named explicitly by temporaries, which are entered in the symbol table. Instructions like `x = minus y` or `param` leave fields unused.
- A **triple** has only three fields: `op`, `arg1`, `arg2`. The result of an operation is referred to by its **position** (the number of the triple), not by a temporary name. Copy statements like `x[i] = y` need two triples.

**Example:** `a = b * - c + b * - c`. Three-address code:

```text
t1 = minus c
t2 = b * t1
t3 = minus c
t4 = b * t3
t5 = t2 + t4
a  = t5
```

**Quadruples:**

| | op | arg1 | arg2 | result |
|:-:|:--|:--|:--|:--|
| 0 | minus | c | | t1 |
| 1 | \* | b | t1 | t2 |
| 2 | minus | c | | t3 |
| 3 | \* | b | t3 | t4 |
| 4 | + | t2 | t4 | t5 |
| 5 | = | t5 | | a |

**Triples:**

| | op | arg1 | arg2 |
|:-:|:--|:--|:--|
| 0 | minus | c | |
| 1 | \* | b | (0) |
| 2 | minus | c | |
| 3 | \* | b | (2) |
| 4 | + | (1) | (3) |
| 5 | = | a | (4) |

**Problem with triples in an optimizing compiler (3 marks).** Optimisers frequently **move** instructions (code motion out of loops, reordering, deletion). With triples, the result of an instruction *is* its position. Moving triple (2) to another place changes its number, so every triple that refers to (2) must be found and changed. With quadruples, an instruction refers to `t3`, which stays the same wherever the instruction defining it is placed. **Indirect triples** solve the problem by keeping a separate list of pointers to triples; the optimiser reorders the list, and the triples themselves do not move.

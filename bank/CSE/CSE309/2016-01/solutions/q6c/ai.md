---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "With X = a-b, Y = a+b: AST has 9 operator nodes (+, outer -, three copies of a-b, two *, two a+b) and gives 9 three-address statements; the DAG shares a-b (used 3 times), a+b and (a-b)*(a+b), has 5 operator nodes and gives 5 statements: t1 = a - b; t2 = a + b; t3 = t1 * t2; t4 = t1 - t3; t5 = t4 + t3."
sources: ["KMS Chapter 6 slides 1-36 (syntax trees, DAGs, three-address code)", "Dragon book 2e sec. 6.1.1-6.1.2, 6.2.1"]
---
Fully parenthesized expression, with $X = (a - b)$ and $Y = (a + b)$:

$$(X - (X * Y)) + (X * Y)$$

(The grammar is taken as the usual expression grammar; the printed one lacks $T \to F$, which is obviously intended.)

**(i) Abstract syntax tree.** One node for every operator occurrence, nothing shared: 9 operator nodes and 10 leaves.

![AST](figures/ast.png)

**(ii) DAG.** A node is shared whenever the same operator is applied to the same children (value-number method, Dragon book sec. 6.1.2):

| Node | Operation | Left | Right |
|:-:|:-:|:-:|:-:|
| 1 | $a - b$ | `a` | `b` |
| 2 | $a + b$ | `a` | `b` |
| 3 | $*$ | 1 | 2 |
| 4 | $-$ | 1 | 3 |
| 5 | $+$ | 4 | 3 |

The sub-expression $a - b$ (node 1) is used three times and $(a-b)*(a+b)$ (node 3) twice, but each is built once.

![DAG](figures/dag.png)

**(iii) Three-address code for the AST** (post-order, one statement for every operator node, 9 temporaries):

```text
t1 = a - b
t2 = a - b
t3 = a + b
t4 = t2 * t3
t5 = t1 - t4
t6 = a - b
t7 = a + b
t8 = t6 * t7
t9 = t5 + t8
```

**(iv) Three-address code for the DAG** (one statement per DAG node, 5 temporaries):

```text
t1 = a - b
t2 = a + b
t3 = t1 * t2
t4 = t1 - t3
t5 = t4 + t3
```

The DAG saves 4 statements (and 4 temporaries): `a - b` is computed once instead of three times, `a + b` once instead of twice, and `(a-b)*(a+b)` once instead of twice.

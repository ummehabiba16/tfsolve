---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "DAG nodes by value number: 1 x, 2 y, 3 (1 - 2), 4 (1 + 2), 5 (3 * 4), 6 (3 + 5); the sub-expression x - y is shared by the + and * nodes, and the leaves x, y are shared by - and +."
sources: ["KMS Chapter 6 slides 1-19 (DAGs and the value-number method)", "Dragon book 2e sec. 6.1.1-6.1.2"]
---
Fully parenthesized with usual precedence: $x - y + (x - y) * (x + y) = (x - y) + \big((x - y) * (x + y)\big)$.

A **DAG** shares a node whenever the same operator is applied to the same operands, so the common sub-expression $x - y$ is a single node. Constructing it with the **value-number method** (Dragon book sec. 6.1.2), each new `(op, left, right)` is looked up before a node is created:

| Value number | Node | Operation | Left | Right |
|:-:|:--|:-:|:-:|:-:|
| 1 | leaf $x$ | | | |
| 2 | leaf $y$ | | | |
| 3 | $x - y$ | $-$ | 1 | 2 |
| 4 | $x + y$ | $+$ | 1 | 2 |
| 5 | $(x - y) * (x + y)$ | $*$ | 3 | 4 |
| — | second $x - y$ | found: **node 3 is reused** | | |
| 6 | whole expression | $+$ | 3 | 5 |

![DAG for x - y + (x - y) * (x + y)](figures/dag.png)

The DAG has 6 nodes (2 leaves, 4 operators) instead of 11 nodes in the syntax tree; node 3 ($x - y$) has two parents (nodes 5 and 6), and the leaves $x$, $y$ have two parents each (nodes 3 and 4).

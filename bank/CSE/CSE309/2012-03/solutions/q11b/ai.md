---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The DAG has one leaf a and 6 shared + nodes (n2 = a+a, n3 = n2+a, n4 = n3+a, n5 = n3+n4, n6 = n2+n5, n7 = a+n6), plus the array-assignment node []= with children b, i and n7; a syntax tree would need 10 leaves a and 9 + nodes."
sources: ["KMS Chapter 6 slides 1-19 (DAGs, value numbering)", "Dragon book 2e sec. 6.1.1-6.1.2"]
---
Expression: $b[i] = a + (a + a + (a + a + a + (a + a + a + a)))$. With left associativity inside each bracket:

- $R = a + a + a + a = ((a + a) + a) + a$;
- $Q = a + a + a + R = ((a + a) + a) + R$;
- $P = a + a + Q = (a + a) + Q$;
- whole right side $= a + P$.

**Value-number construction** (Dragon book sec. 6.1.2): each `(op, left, right)` is searched in the table before a node is created.

| Number | Node | Left | Right | How it arises |
|:-:|:--|:-:|:-:|:--|
| 1 | leaf $a$ | | | |
| 2 | $+$ | 1 | 1 | $a + a$ (first occurrence) |
| 3 | $+$ | 2 | 1 | $(a + a) + a$ |
| 4 | $+$ | 3 | 1 | $((a + a) + a) + a = R$ |
| 5 | $+$ | 3 | 4 | $((a + a) + a) + R = Q$; the node 3 is **reused** |
| 6 | $+$ | 2 | 5 | $(a + a) + Q = P$; the node 2 is **reused** |
| 7 | $+$ | 1 | 6 | $a + P$ |

The assignment to the array element is the node `[]=` with the three children $b$, $i$ and node 7.

![DAG for the assignment](figures/dag.png)

The sub-expressions $a + a$ (node 2) and $(a + a) + a$ (node 3) occur several times in the expression but exist once in the DAG, and the leaf $a$ has a single node with many parents. The syntax tree would need 10 leaves $a$ and 9 `+` nodes; the DAG needs 1 leaf $a$ and 6 `+` nodes.

*Check:* the value-number table was produced by a script and agrees with the table (6 operator nodes).

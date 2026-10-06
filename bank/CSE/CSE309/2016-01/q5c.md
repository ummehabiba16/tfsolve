---
marks: 15
topics: [sdd-attributes, dependency-graph]
kind: analysis
source: {page: 49}
---
Consider the following syntax-directed definition:

| Production | Semantic Rule |
|:--|:--|
| $F \to 0.B$ | $F.val = B.val$ |
| $B \to 0B_1$ | $B.val = B_1.val/2$ |
| $B \to 1B_1$ | $B.val = B_1.val/2 + 1/2$ |
| $B \to 0$ | $B.val = 0$ |
| $B \to 1$ | $B.val = 1/2$ |

The numeric value of a binary fraction $0.b_1b_2 \ldots b_n$ is calculated as $\sum_{i=1}^{n} b_i 2^{-i}$. Each non-terminal has a synthesized attribute 'val' that is used to store its value.

(i) Show the annotated parse tree for the sentences:

```text
0.101011
```

(ii) Show the dependency graph of the annotated parse tree generated in question 5(c)(i).

(iii) Find a topological order of the dependency graph generated in question 5(c)(ii).

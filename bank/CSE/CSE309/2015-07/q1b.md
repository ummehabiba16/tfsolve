---
marks: 12
topics: [sdd-attributes, l-attributed-impl]
kind: analysis
source: {page: 51}
---
For the following SDD, give annotated parse tree to evaluate the expression, 5\*4\*3.

| | PRODUCTION | SEMANTIC RULES |
|:-:|:--|:--|
| 1) | $T \to F T'$ | $T'.inh = F.val$ |
| | | $T.val = T'.syn$ |
| 2) | $T' \to * F T_1'$ | $T_1'.inh = T'.inh \times F.val$ |
| | | $T'.syn = T_1'.syn$ |
| 3) | $T' \to \epsilon$ | $T'.syn = T'.inh$ |
| 4) | $F \to \textbf{digit}$ | $F.val = \textbf{digit}.lexval$ |

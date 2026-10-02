---
marks: 15
topics: [sdd-attributes, l-attributed-impl]
kind: analysis
source: {page: 38}
---
Look at the following, Syntax Directed Definition (SDD).

| | PRODUCTION | SEMANTIC RULES |
|:-:|:--|:--|
| 1) | $T \to F T'$ | $T'.inh = F.val$ |
| | | $T.val = T'.syn$ |
| 2) | $T' \to * F T_1'$ | $T_1'.inh = T'.inh \times F.val$ |
| | | $T'.syn = T_1'.syn$ |
| 3) | $T' \to \epsilon$ | $T'.syn = T'.inh$ |
| 4) | $F \to \textbf{digit}$ | $F.val = \textbf{digit}.lexval$ |

This SDD can evaluate the value of an expression in the attribute val. However, it cannot handle addition/subtractions. For example, the given SDD will successfully handle the expression "2\*3\*4" but fail for the expression "2+3\*4". Extend the SDD so that it is capable of handling addition/subtraction operators (+ and $-$) and consequently, is able to evaluate expressions with arbitrary number of addition, subtraction and multiplication operators.

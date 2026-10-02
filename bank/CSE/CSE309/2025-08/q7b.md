---
marks: 12
topics: [control-flow]
kind: analysis
source: {page: 6}
---
Consider the following SDD for generating three-address codes using the fall-through technique.

| Production | Semantic Rules |
|:--|:--|
| $S \to \textbf{if}\ (B)\ S_1$ | $B.true = fall$ |
| | $B.false = S_1.next = S.next$ |
| | $S.code = B.code \,\Vert\, S_1.code$ |
| $B \to B_1 \Vert B_2$ | $B_1.true =$ **if** $B.true \ne fall$ **then** $B.true$ **else** $newLabel()$ |
| | $B_1.false = fall$ |
| | $B_2.true = B.true$ |
| | $B_2.false = B.false$ |
| | $B.code =$ **if** $B.true \ne fall$ **then** $B_1.code \,\Vert\, B_2.code$ |
| | **else** $B_1.code \,\Vert\, B_2.code \,\Vert\, label(B_1.true)$ |

Now add rules to the SDD above for the following two productions using the same fall-through technique

(i) $B \to B_1\ \&\&\ B_2$

(ii) $B \to E_1\ \textbf{rel}\ E_2$

Assume all the symbols, attributes, functions, tables, and notations have their usual meanings.

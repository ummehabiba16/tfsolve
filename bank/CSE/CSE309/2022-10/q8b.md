---
marks: 20
topics: [table-driven-ll, ll1]
kind: numerical
source: {page: 24}
note: "The marks are cut off at the page edge on the scan; 20 is assumed (the question total is 35)."
---
Consider the following grammar.

$$E \to TE'$$

$$E' \to +TE' \mid \epsilon$$

$$T \to FT'$$

$$T' \to *FT' \mid \epsilon$$

$$F \to (E) \mid id$$

On input id + id \* id, construct a table by showing the moves that will be made by the non-recursive predictive parser algorithm.

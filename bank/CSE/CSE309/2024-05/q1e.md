---
marks: 5
topics: [recursive-descent, left-recursion]
kind: code
mandatory: true
source: {page: 9}
---
Write a procedure based predictive parser for the following grammar keeping the grammar unaltered:

$$E \to E + F \mid E - F \mid F$$

$$F \to \textbf{NUM} \mid \textbf{ID}(E)$$

Point out any possible flaw of the parser you have constructed.

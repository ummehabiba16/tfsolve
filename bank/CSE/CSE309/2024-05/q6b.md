---
marks: 9
topics: [sdt-schemes, l-attributed-impl]
kind: analysis
source: {page: 12}
note: "Marks printed as (5+4)."
---
Consider the following E-productions from an SDT for translating infix expressions to postfix notation. Transform the SDT such that it can be implemented during top-down parsing. Show the correctness of your SDT by computing the output for the expression 2+3+4.

$$E \to E_1 + T\ \ \{\text{print}('+');\}$$

$$E \to T$$

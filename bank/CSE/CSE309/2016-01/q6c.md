---
marks: 15
topics: [ir-forms, three-address-code]
kind: numerical
source: {page: 49}
---
Given the following expression:

$$((a - b) - ((a - b) * (a + b))) + ((a - b) * (a + b))$$

(i) Construct AST

(ii) Construct the DAG

(iii) Construct three address code for AST

(iv) Construct three address code for DAG

Assume the following grammar for this question.

$$E \to E + T \mid E - T$$

$$T \to T * F$$

$$F \to (E) \mid \textbf{id}$$

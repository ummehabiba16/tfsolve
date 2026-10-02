---
marks: 12
topics: [ir-forms, sdt-schemes]
kind: code
source: {page: 11}
---
Below is a grammar for simple expressions involving only numbers and the operators '+' and '\*' such as 2\*(3+4)\*5. Write a postfix Syntax-Directed Translation Scheme (SDT) to compute the DAG (Directed Acyclic Graph) for an expression represented by the given grammar. Explain how your SDT would detect common subexpressions.

$$E \to E + T$$

$$E \to T$$

$$T \to T * F$$

$$T \to F$$

$$F \to (E)$$

$$F \to id$$

$$F \to num$$

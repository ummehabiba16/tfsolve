---
marks: 10
topics: [syntax-tree-construction]
kind: code
source: {page: 33}
---
Below is a grammar for simple expressions involving '+' and '\*' operators. Give an SDD to construct syntax trees for expressions represented by the given grammar.

$$E \to E + T$$

$$E \to T$$

$$T \to T * F$$

$$T \to F$$

$$F \to (E)$$

$$F \to \text{id}$$

$$F \to \text{num}$$

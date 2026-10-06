---
marks: 10
topics: [syntax-tree-construction, sdt-schemes]
kind: analysis
source: {page: 44}
---
What is the difference between parse tree and abstract syntax tree? Write down a Postfix SDT using parser-stack to construct abstract syntax tree for the following context free grammar. The symbols have their usual meaning.

$$S \to \textbf{id} = E \mid \textbf{id}\ [E] = E$$

$$E \to E + T \mid T$$

$$T \to T * F \mid F$$

$$F \to \textbf{id} \mid \textbf{id}\ [E] \mid \textbf{num}$$

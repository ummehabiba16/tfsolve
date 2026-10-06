---
marks: 9
topics: [types-declarations, sdt-schemes]
kind: analysis
source: {page: 62}
---
Consider the following grammar for declaration statement.

$$D \to T\ \textbf{id};$$

$$T \to \textbf{B}\ \textbf{C}$$

$$B \to \textbf{int} \mid \textbf{float}$$

$$C \to [\textbf{num}]\ C \mid \epsilon$$

Design an SDT for the above grammar that will compute the type and width of a declared identifier and insert them in a symbol table. Assume the width of an integer is 4 and that of a float is 8.

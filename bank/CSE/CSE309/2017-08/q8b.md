---
marks: 10
topics: [three-address-code]
kind: numerical
source: {page: 45}
---
Construct three address code for the expression $a = -(b + c) + -d$ according to the following SDD. Also show them in triples data structure.

| Production | Semantic Rules |
|:--|:--|
| $S \to \textbf{id} = E$ | $S.code = E.code \parallel$ |
| | $\quad gen(top.get(\textbf{id}.lexeme)\ \text{'='}\ E.addr)$ |
| $E \to E_1 + E_2$ | $E.addr = \textbf{new}\ Temp()$ |
| | $E.code = E_1.code \parallel E_2.code \parallel$ |
| | $\quad gen(E.addr\ \text{'='}\ E_1.addr\ \text{'+'}\ E_2.addr)$ |
| $\mid\ -E_1$ | $E.addr = \textbf{new}\ Temp()$ |
| | $E.code = E_1.code \parallel$ |
| | $\quad gen(E.addr\ \text{'='}\ \text{'minus'}\ E_1.addr)$ |
| $\mid\ (E_1)$ | $E.addr = E_1.addr$ |
| | $E.code = E_1.code$ |
| $\mid\ \textbf{id}$ | $E.addr = top.get(\textbf{id}.lexeme)$ |
| | $E.code = \text{''}$ |

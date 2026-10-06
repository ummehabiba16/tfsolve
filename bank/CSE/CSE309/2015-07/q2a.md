---
marks: 20
topics: [three-address-code]
kind: numerical
source: {page: 52}
note: "Marks printed as (10+10=20). The scan of the SDD table is partly broken; rules read from context and by comparison with the standard SDD."
---
Translate the expression, $\textbf{d = (a + b) + -c;}$ into three-address code using the following SDD. Show the corresponding annotated parse tree with annotations for attributes, **addr** and **code** Then illustrate the quadruples and triples representation of the generated three-address code.

| Production | Semantic Rules |
|:--|:--|
| $S \to \textbf{id} = E\ ;$ | $S.code = E.code \parallel$ |
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

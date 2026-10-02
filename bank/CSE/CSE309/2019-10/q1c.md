---
marks: 9
topics: [tokens]
kind: analysis
source: {page: 31}
note: "Table header printed as 'Schme'."
---
Analyze clearly the acceptability / unacceptability, merits / demerits of the following tokenization schemes:

| Schme | Pattern | Token |
|:-:|:-:|:-:|
| 1 | + or - or \* or / | $\langle$MATHOP, attribute$\rangle$ |
| 2 | + or - | $\langle$PM, attribute$\rangle$ |
| | \* or / | $\langle$MD, attribute$\rangle$ |
| 3 | + | $\langle$PLUS$\rangle$ |
| | - | $\langle$MINUS$\rangle$ |
| | \* | $\langle$MULT$\rangle$ |
| | / | $\langle$DIV$\rangle$ |

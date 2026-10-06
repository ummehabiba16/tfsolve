---
marks: 8
topics: [sdt-schemes, control-flow]
kind: analysis
source: {page: 44}
note: "The concatenation operator is printed as '//'."
---
Convert the following SDD into SDT.

| Productions | Semantic Rules |
|:--|:--|
| $S \to \textbf{while}\ (B)\ S_1$ | $begin = newlabel()$ |
| | $B.true = newlabel()$ |
| | $B.false = S.next$ |
| | $S_1.next = begin$ |
| | $S.code = label(begin)$ |
| | $/\!/\ B.code\ /\!/\ label(B.true)$ |
| | $/\!/\ S_1.code$ |
| | $/\!/\ gen(\text{'goto'}\ begin)$ |

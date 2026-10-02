---
marks: 13
topics: [viable-prefixes, clr]
kind: analysis
mandatory: true
source: {page: 2}
---
Consider the grammar given below:

$$S \to aB \mid bA$$

$$A \to a$$

$$B \to b$$

By carrying out rightmost derivations, find out whether the LR(1) items shown in the following table are valid for the corresponding viable prefixes shown in the same table.

| Viable Prefix | Item |
|:--|:--|
| a | $[S \to a \cdot B, \$]$ |
| b | $[S \to b \cdot A, \$]$ |
| b | $[A \to \cdot a, \$]$ |
| ab | $[B \to \cdot b, b]$ |
| baa | $[A \to A \cdot a, \$]$ |
| ab | $[B \to b \cdot, \$]$ |
| ba | $[A \to a \cdot, \$]$ |
| a | $[A \to \cdot a, a]$ |
| b | $[S \to b \cdot A, a]$ |

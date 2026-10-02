---
marks: 13
topics: [sdt-schemes]
kind: analysis
source: {page: 5}
note: "Marks printed as (4+9). There is a handwritten mark over the '*' in the T-production on the scan."
---
The following SDT prints the prefix form of an expression, i. e., performs infix to prefix translation. Explain why it is not possible to implement the SDT during either top-down or bottom-up parsing. Describe, then, how such an SDT can be implemented.

$$L \to E\,\textbf{n}$$

$$E \to \{\text{print}('+');\}\ E_1 + T$$

$$E \to T$$

$$T \to \{\text{print}('*');\}\ T_1 * F$$

$$T \to F$$

$$F \to (E)$$

$$F \to \textbf{digit}\ \{\text{print}(\textbf{digit}.\text{level});\}$$

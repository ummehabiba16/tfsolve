---
marks: 7
topics: [sdt-schemes, left-recursion]
kind: analysis
source: {page: 33}
---
The following SDT computes the value of string of 0's and 1's interpreted as a positive, binary integer.

$$B \to B_1\,0\ \{B.val = 2 \times B_1.val\}$$

$$\quad \mid B_1\,1\ \{B.val = 2 \times B_1.val + 1\}$$

$$\quad \mid 1\ \{B.val = 1\}$$

Rewrite this SDT so that the underlying grammar is not left recursive, and yet the same value of *B.val* is computed for the entire input string.

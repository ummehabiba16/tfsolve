---
marks: 10
topics: [optimization, cse, induction-variables]
kind: numerical
source: {page: 18}
---
Optimize the following three-address code by eliminating common subexpressions, performing reduction in strength on induction variables, and eliminating all the induction variables as possible.

```text
    dp = 0
    i = 0
L:  t1 = i*8
    t2 = A[t1]
    t3 = i*8
    t4 = B[t3]
    t5 = t2*t4
    dp = dp + t5
    i = i + 1
    if i<n goto L
```

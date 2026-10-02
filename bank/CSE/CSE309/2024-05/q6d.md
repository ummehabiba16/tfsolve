---
marks: 6
topics: [expr-array-translation]
kind: numerical
source: {page: 12}
note: "Printed as given: the assumption mentions 'i' although the statement uses j."
---
Write the three-address code for the statement

```c
x = a[b[c[j]]]
```

Assume that- (i) the arrays a, b and c are declared as, int a[5], b[3], c[3]; types and widths of the arrays have correctly been saved in the symbol table, (ii) i and x are integers, and (iii) the size of an integer is 2 byte.

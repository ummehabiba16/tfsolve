---
marks: 10
topics: [dag-optimization]
kind: numerical
mandatory: true
source: {page: 5}
---
How can DAGs (Directed Acyclic Graph) be used to optimize basic blocks? Illustrate using the example basic block below. Assume d and f are not live on exit from the block.

```text
d = b * c
e = a[i]
f = e + d
b = a[i]
a[j] = b
c = a[i]
```

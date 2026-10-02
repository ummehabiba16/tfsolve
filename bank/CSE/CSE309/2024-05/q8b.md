---
marks: 8
topics: [liveness-next-use]
kind: numerical
source: {page: 13}
---
Determine the liveliness and next-use information for each statement in the basic block below. Assume t, u and v are temporary variables and the remaining variables are live on exit from the block.

```text
t = a - c
u = d - b
t = a + b
a = u + t
d = t + v
```

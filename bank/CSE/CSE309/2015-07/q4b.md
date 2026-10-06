---
marks: 15
topics: [basic-blocks]
kind: numerical
source: {page: 53}
note: "Marks printed as (8+7=15)."
---
For the following three-address code sequence, identify the basic blocks and construct the corresponding flow graph.

```text
 1) c = 0
 2) i = 0
 3) j = 0
 4) t1 = 8 * i
 5) t2 = t1 + j
 6) t3 = 8 * t2
 7) mat[t3] = c
 8) c = c + 1
 9) j = j + 1
10) if j < 8 goto (4)
11) i = i + 1
12) if i < 8 goto (3)
```

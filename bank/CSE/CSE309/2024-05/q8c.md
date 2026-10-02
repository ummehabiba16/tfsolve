---
marks: 17
topics: [register-allocation]
kind: analysis
source: {page: 13}
note: "Marks printed as (15+2)."
---
Illustrate the 'linear scan' register allocation algorithm using the following three-address code as an example. Assume three physical registers are available. Make any other justified assumptions as required. What is the advantage of this algorithm?

```text
 1        a=b+c
 2        d=d-b
 3        e=a+f
 4        ifFalse e goto L1
 5        f=a-d
 6        goto L2
 7   L1:
 8        b=d+f
 9        e=a-c
10   L2:
11        b=d+c
```

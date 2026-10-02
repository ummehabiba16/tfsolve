---
marks: 25
topics: [basic-blocks, optimization, cse, copy-propagation, dead-code-elimination, induction-variables]
kind: analysis
mandatory: true
source: {page: 10}
note: "Marks printed as (10+15) for (i) and (ii)."
---
Consider the three-address code below and answer the following questions.

(i) Identify the basic blocks and construct the flow graph for the given code. Give each block an identifier and replace the label references in the statements with the corresponding identifiers.

(ii) Optimize the code by discovering all possible semantic preserving transformations. For each of the transformations used, specify the name of the transformation.

```text
 1   L1:  i = 0
 2   L3:  t1 = n - 1
 3        iffalse i < t1 goto L2
 4   L4:  j = i + 1
 5   L5:  iffalse j < n goto L6
 6   L7:  t2 = i * 8
 7        t3 = a [ t2 ]
 8        t4 = j * 8
 9        t5 = a [ t4 ]
10        iffalse t3 > t5 goto L8
11   L9:  t6 = i * 8
12        p = a [ t6 ]
13   L10: t7 = i * 8
14        t8 = j * 8
15        t9 = a [ t8 ]
16        a [ t7 ] = t9
17   L11: t10 = j * 8
18        a [ t10 ] = p
19   L8:  j = j + 1
20        goto L5
21   L6:  i = i + 1
22        goto L3
23   L2:
```

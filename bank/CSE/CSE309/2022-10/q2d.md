---
marks: 6
topics: [control-flow]
kind: numerical
source: {page: 20}
---
translate the following if-else statement to three-address code avoiding redundant gotos. Assume &&, || are left associative and && has higher precedence than ||.

```c
if (( x != y || x > 20) && x < 10) flag = 0; else flag = 1;
```

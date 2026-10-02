---
marks: 5
topics: [control-flow]
kind: numerical
source: {page: 12}
note: "Printed as 'x = 0,' in the then-branch."
---
Write down the three-address code for the statement below avoiding redundant gotos. Assume &&, || are left associative and precedence order is && then ||.

```c
if ( x > 20 && (x < 10 || x != y ))
    x = 0;
else x = 1;
```

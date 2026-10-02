---
marks: 14
topics: [simple-codegen]
kind: numerical
source: {page: 35}
---
Convert the following three address code into machine code for the simple machine model of your text. Assume three registers are available. Make sure the registers are allocated and assigned efficiently to avoid unnecessary loads and stores. Show the register and address descriptors after each step. Assume *t*, *u* and *v* are temporary variables and the remaining variables are live on exit from the block.

```text
t = a - b
u = a + b
v = t + u
a = d
d = v + c
```

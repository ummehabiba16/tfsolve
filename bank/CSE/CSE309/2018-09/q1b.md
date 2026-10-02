---
marks: 15
topics: [token-recognition]
kind: analysis
source: {page: 36}
---
In a certain programming language, the decimal numbers are like, 123.456E $\pm$ 789. Here, decimal part and exponent part are optional. Furthermore, the plus or minus in the exponent is optional. In formulating regular definitions for these numbers, some one came up with the following:

```text
number -> [0-9] [0-9]*.[0-9] [0-9]*?(E +-?[0-9]*)
```

The above definition has got a number of flaws in it. Point out these flaws with necessary explanations.

---
marks: 15
topics: [activation-records]
kind: analysis
source: {page: 52}
note: "Marks printed as (8+7=15)."
---
The following code computes Fibonacci numbers recursively.

```c
int fibonacci (int n) {
    if (n<2) return 1;
    return fibonacci (n-1) + fibonacci (n-2) ;
}
```

Show the complete activation tree for it. What does the control stack look like when the third call of **fibonacci(1)** is about to return? Show only the arguments and return values in an activation record. (Assume that the initial call is fibonacci(5)).

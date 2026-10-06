---
marks: 10
topics: [distributed]
kind: analysis
source: {page: 22}
---
What is RPC? Suppose the user has written the following codes:

```c
int main() {
    ...
    m = f1(x1, x2);
    ...
}
int f1(char* a, char* b){
    ...
    p = f2(*a);
}
float f2(int t){
    ...
}
```

If the user wishes to run the function `f2` in a distributed manner, how will a RPC run-time library handle it? Write down which steps it needs to take and corresponding details that are needed to be taken care of in each step.

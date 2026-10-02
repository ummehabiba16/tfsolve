---
marks: 15
topics: [scope-access]
kind: analysis
source: {page: 40}
---
What is the output of the following code segment if $-$

(i) The program names are handled in compilation time?

(ii) The program names are handled in runtime?

```c
int x = 137;
int y = 42;
void Function1() {
    Print(x + y);
}
void Function2() {
    int x = 0;
    Function1();
}
void Function3() {
    int y = 0;
    Function2();
}
Function1();
Function2();
Function3();
```

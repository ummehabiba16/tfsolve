---
marks: 10
topics: [linker-loader]
kind: conceptual
mandatory: true
source: {page: 1}
---
Consider the following three files written in C programming language:

**main.c**

```c
extern int foo(int x);  // Defined in libfoo
extern int bar(int x);  // Defined in libbar

int main() {
    return foo(5) + bar(3);
}
```

**libfoo.c**

```c
extern int baz(int x);  // Defined in libbar

int foo(int x) {
    return baz(x + 1);
}
```

**libbar.c**

```c
int baz(int x) {
    return x * 2;
}

int bar(int x) {
    return x + baz(x);
}
```

Assume these files are compiled into:

- `main.o` (relocatable object file for main),
- `libfoo.o` (shared library),
- `libbar.o` (shared library).

Explain the terms relocatable machine code, linker, and loader from the perspective of compilation and execution of the above program.

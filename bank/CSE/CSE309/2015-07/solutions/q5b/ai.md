---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A valid C program that uses the C++ keyword class as an identifier and assigns malloc's void * result to an int * without a cast compiles with a C compiler but is rejected by a C++ compiler."
sources: ["MMA introduction slides 4-13", "Dragon book 2e sec. 1.1, 3.1"]
---
C++ is *almost* a superset of C, but there are valid C programs that a C++ compiler rejects, mainly because (1) C++ has more keywords (`class`, `new`, `delete`, `this`, `template`, `public`, ...) that are ordinary identifiers in C, and (2) C++ is stricter about types: `void *` is converted to another pointer type implicitly in C but only with a cast in C++.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int class = 3;                     /* legal in C: class is an identifier       */
    int *p = malloc(sizeof(int));      /* legal in C: void * converts implicitly   */
    *p = class;
    printf("%d\n", *p);
    return 0;
}
```

- A C compiler (`gcc t.c`) compiles it and the program prints `3`.
- A C++ compiler (`g++ t.cpp`) reports errors: `class` is a keyword ("declaration of anonymous class must be a definition"), and "cannot initialize a variable of type `int *` with an rvalue of type `void *`".

*Check:* the program was compiled with both `gcc` (success, prints 3) and `g++` (the two errors above).

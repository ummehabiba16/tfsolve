---
marks: 13
topics: [linker-loader]
kind: conceptual
mandatory: true
source: {page: 14}
note: "Printed as 'when he program is compiled'."
---
Consider the C code shown below contained in two separate files. Discuss in detail the issues faced by the linker and the loader when he program is compiled and then executed. How will these issues be resolved? Explain.

**main.c**

```c
#include <stdio.h>
void main()
{
  .......;
  int i;
  i = subfunction();
  exit();
}
```

**subcode.c**

```c
void subfunction()
{
  int i, n = 0;
  for (i = 1; i <= 50; i++)
    {
      n = n + i;
    }
  return n;
}
```

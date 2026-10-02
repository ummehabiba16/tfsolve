---
marks: 10
topics: [lexical-errors, tokens]
kind: analysis
source: {page: 23}
note: "Printed as 'Does lexical analyzer will find errors'."
---
Does lexical analyzer will find errors from the following code snippet? If you think lexical analyzer will find some errors then explain them properly.

```c
int arr[] = {1, 2, 3, 5};
int i = 0;
do {
    if (arr[i] %2 == 0)
        print("EVEN\n");
    else
        print("ODD\n");
    i++;
} while (index < 4);
```

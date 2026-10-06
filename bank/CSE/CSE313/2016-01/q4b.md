---
marks: 10
topics: [producer-consumer-semaphores]
kind: code
source: {page: 55}
note: "Printed as 'Te decrease_count() function'; the call is printed 'Resource_manager.decrease_count(count);' and the loop as 'while (decrease count(count)== -1);'."
---
The `decrease_count()` function in the question 4(a) currently returns 0 if sufficient resources are available and -1 otherwise. This leads to busy waiting for a process that wishes to obtain a number of resources:

```c
while (decrease_count(count) == -1);
```

Implement a monitor named **resource_manager** which contains necessary data variables, condition variables and two functions named **void decrease_count(int count)**, **void increase_count(int count)** such that `decrease_count()` function suspends the calling process until sufficient resources are available. This will allow a process to invoke `decrease_count()` by simply calling

```c
Resource_manager.decrease_count(count);
```

The calling process will return from this function call only when sufficient resources are available. You must maximize the degree of parallelism.

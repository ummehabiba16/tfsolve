---
marks: 10
topics: [locks]
kind: code
source: {page: 18}
---
You are given a new atomic function, called `FetchAndSubtract()`. It executes as a single atomic instruction, and is defined as follows:

```c
int FetchAndSubtract (int *location) {
    int value = *location;     // read the value pointed to by location
    *location = value - 1;     // decrement it and store result back
    return value;              // return old value
}
```

You are given the task: write the `lock_init()`, `lock()`, and `unlock()` functions (and also define a `lock_t` structure) that use `FetchAndSubtract()` to implement a working lock.

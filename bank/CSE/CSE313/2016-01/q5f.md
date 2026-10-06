---
marks: 6
topics: [buffer-cache]
kind: code
source: {page: 56}
---
Describe the if-else statements in the given algorithm for releasing a buffer in UNIX using illustrative examples.

```text
algorithm brelse
input:  locked buffer
output: none
{
    wakeup all procs: event, waiting for any buffer to become free;
    wakeup all procs: event, waiting for this buffer to become free;
    raise processor execution level to block interrupts;
    if (buffer contents valid and buffer not old)
        enqueue buffer at end of free list
    else
        enqueue buffer at beginning of free list
    lower processor execution level to allow interrupts;
    unlock(buffer);
}
```

*Algorithm for Question 5 (f)*

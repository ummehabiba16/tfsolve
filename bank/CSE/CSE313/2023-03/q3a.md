---
marks: 5
topics: [ipc]
kind: code
source: {page: 19}
---
Let's examine a program having two threads:

| Thread 1 | Thread 2 |
|:--|:--|
| `pending = 1;` | `pending = 0;` |
| `while (pending) {` | |
| `    printf("hello\n");` | |
| `}` | |

How could we re-write the code such that Thread 2 would only run after "hello" has been printed at least twice? You can use any synchronization primitive of your choice.

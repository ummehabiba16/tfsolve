---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Use a counting semaphore posted once per printed hello; Thread 2 does two waits before clearing pending."
sources: ["OSTEP ch. 31 (semaphores)"]
---
Use a semaphore `s` initialised to $0$ that counts how many times "hello" has been printed:

```c
sem_t s;            // sem_init(&s, 0, 0);
volatile int pending;
```

| Thread 1 | Thread 2 |
|:--|:--|
| `pending = 1;` | `sem_wait(&s);` |
| `while (pending) {` | `sem_wait(&s);` |
| `printf("hello\n");` | `pending = 0;` |
| `sem_post(&s);` | |
| `}` | |

Thread 2 blocks in the first `sem_wait` until Thread 1 has printed once, in the second until it has printed twice; only then does it set `pending = 0`. Thread 1 keeps printing until `pending` becomes $0$, so "hello" is printed **at least twice** before Thread 2's assignment. (`pending = 1` is executed before the first `sem_post`, so Thread 2 cannot clear it too early.)

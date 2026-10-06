---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A thread pool: a dispatcher thread puts requests in a queue and 50 pre-created worker threads take them, each serving one request at a time, in parallel on the 50 cores."
sources: ["Tanenbaum MOS 4e, sec. 2.2.3 (a multithreaded web server: dispatcher and worker threads)"]
---
**Design.** Use a **thread pool**: one **dispatcher** thread accepts requests and 50 **worker** threads (one per core, created once at start-up) each process a request from a shared queue. This avoids creating a thread per request, keeps all 50 cores busy, and because requests have variable duration, an idle worker immediately picks the next request (good load balance); workers block (without wasting CPU) while waiting for disk or the network, so the cores are used by other workers.

```c
#define N_WORKERS 50
queue_t   queue;                 /* shared bounded queue of requests */
mutex_t   m;  cond_t not_empty, not_full;

void dispatcher(void) {          /* one thread */
    while (TRUE) {
        req = get_next_request();            /* blocks until a request arrives */
        lock(&m);
        while (queue_full(&queue)) wait(&not_full, &m);
        enqueue(&queue, req);
        signal(&not_empty);
        unlock(&m);
    }
}

void worker(void) {              /* 50 identical threads */
    while (TRUE) {
        lock(&m);
        while (queue_empty(&queue)) wait(&not_empty, &m);
        req = dequeue(&queue);
        signal(&not_full);
        unlock(&m);
        handle_request(req);     /* long, variable work: done outside the lock */
    }
}

main() { for (i = 0; i < N_WORKERS; i++) thread_create(worker); dispatcher(); }
```

The lock protects only the short queue operations; the real work runs in parallel. (If requests are mostly I/O bound, more than 50 workers could be useful.)

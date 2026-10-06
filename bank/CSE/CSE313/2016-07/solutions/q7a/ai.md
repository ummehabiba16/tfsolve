---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) scheduling is nondeterministic, no guarantee; (ii) main joins in order, so guaranteed; (iii) all threads and main print to the same stdout concurrently; (iv) min 1, max 10; (v) min 1, no fixed maximum; (vi) running."
sources: ["Anderson and Dahlin, OSPP, ch. 4 (threads: create, join, exit; states)"]
---
The program creates 10 threads in a loop; each prints "Hello from thread n" and exits with `100+n`; then `main` **joins the threads in the order 0, 1, ..., 9**, printing "Thread i returned ..." after each join.

**(i) "Hello" from thread 3 before thread 2: why? guaranteed?** After `thread_create` returns, the new thread is only *ready*; the **scheduler decides** which ready thread runs next, so thread 3 can happen to run (and print) before thread 2 even though it was created later. The order is **not guaranteed**: it can differ in every run.

**(ii) "Thread 3 returned" after "Thread 2 returned": why? guaranteed?** `main` calls `thread_join(threads[i])` for $i=0,1,2,\dots$ **in order**, and prints after each join returns. It cannot print for thread 3 before it has finished the join (and the print) for thread 2, whatever the order in which the threads finished. So this order **is always maintained**.

**(iii) Why the "Hello" messages are merged (interleaved) with the "Thread returned" messages?** The threads and `main` all run **concurrently** and write to the **same standard output** without any synchronisation. `main` starts joining (and printing) while the other threads have not yet printed their greeting, so their lines come in between (the `printf` output of different threads can even be interleaved within a line, as seen in "Hel?lo").

**(iv) Min and max number of threads when `main` prints a "Thread returned" message.** All 10 threads are created before the join loop. When `main` prints the message for thread $i$, thread $i$ has terminated and threads $0..i-1$ have been joined (terminated); threads $i+1..9$ may still be alive or may already have finished.

- **Maximum:** at the first message (thread 0), threads 1-9 may all still exist: $9+1$ (main) $=\mathbf{10}$ threads.
- **Minimum:** at the last message (thread 9) all others are gone: only `main` remains: $\mathbf{1}$ thread.

**(v) Times thread 2 enters the READY state on a uniprocessor.** *Minimum:* **1** (when it is created it becomes ready, then runs to completion without being preempted or blocked). *Maximum:* there is **no fixed upper bound**: it becomes ready again every time it is preempted by the timer (time slice) or wakes after blocking (e.g. in the `printf` while writing to the terminal, or while waiting for the stdout lock); each such event adds one entry to READY. With this short thread, a few (e.g. 3-4) are realistic.

**(vi) State of `main` when `thread_join` returns for thread 3.** `main` was **blocked** in `thread_join(threads[3])` until thread 3 exited (which made it ready); it is executing the return from the join and the next `printf`, so it is in the **RUNNING** state.

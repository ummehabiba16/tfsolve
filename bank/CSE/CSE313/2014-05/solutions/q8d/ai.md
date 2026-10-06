---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Semaphore: an integer with atomic down and up used for mutual exclusion and synchronisation; monitor: a language construct (module) in which only one process at a time is active, with condition variables wait and signal."
sources: ["Tanenbaum MOS 4e, sec. 2.3.5 and 2.3.7 (semaphores, monitors)"]
---
**(i) Semaphore** (Dijkstra, 1965). An integer variable with two **atomic** operations: `down` (P, wait): if the value is $>0$ decrement it, else **block** the calling process; `up` (V, signal): increment the value, or, if processes are blocked on it, **wake one** of them (the value stays 0). *Uses:* a **binary semaphore** (mutex) for mutual exclusion, a **counting semaphore** for limited resources, and ordering/synchronisation (initial value 0). It solves the producer-consumer problem (`mutex`, `empty`, `full`). *Weakness:* error-prone: forgetting or misordering `down`/`up` (e.g. `down(mutex)` before `down(empty)`) gives deadlocks.

**(ii) Monitor** (Hoare, Brinch Hansen). A **high-level synchronisation construct**: a collection of procedures, variables and data structures grouped together in a module; **only one process can be active in the monitor at any instant**, so mutual exclusion is guaranteed by the compiler. Processes that cannot proceed use **condition variables** with `wait(c)` (block and release the monitor) and `signal(c)` (wake a waiting process). It makes programming safer because the programmer does not write the locking code, but it requires language support (Java `synchronized`, `wait`/`notify`) and, as a language construct, is not available in C.

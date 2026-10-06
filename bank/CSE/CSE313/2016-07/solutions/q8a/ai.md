---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Disabling interrupts stops only the local CPU; other CPUs can still enter the critical section, so an atomic read-modify-write instruction (test-and-set) spin lock is needed, usually together with disabling local interrupts."
sources: ["Anderson and Dahlin, OSPP, ch. 5 (implementing locks on a multiprocessor)", "OSTEP ch. 28"]
---
**Why disabling interrupts is not enough.** On a **uniprocessor**, a critical section is protected by disabling interrupts, because the only way another thread can run is by a timer/I/O interrupt. On a **multiprocessor** each CPU has its own interrupt flag: disabling interrupts affects **only the local CPU**. Threads running on **other CPUs continue to execute** and can enter the critical section at the same time, so mutual exclusion is **not** guaranteed. (Also, disabling interrupts on all CPUs would be very slow.)

**Extra measure.** Use a hardware **atomic read-modify-write instruction** (test-and-set, compare-and-swap, exchange) to implement a **spin lock** (a lock variable in shared memory that is atomically tested and set; a CPU that finds it set spins until it is cleared). To avoid deadlock with interrupt handlers (an interrupt on the CPU that holds the lock whose handler needs the same lock), the OS also **disables interrupts on the local CPU while holding a spin lock** (kernel spin locks do both).

```c
void lock(int *l)   { while (test_and_set(l)) ; }   // atomic, spins on other CPUs
void unlock(int *l) { *l = 0; }
```

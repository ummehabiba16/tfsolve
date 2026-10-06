---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "TSL RX,LOCK atomically copies the lock into a register and sets it to 1; enter_region loops until the old value was 0; leave_region stores 0; drawbacks: busy waiting, priority inversion, a multiprocessor feature."
sources: ["Tanenbaum MOS 4e, sec. 2.3.3 (the TSL instruction)"]
---
**TSL (Test and Set Lock).** An **atomic hardware instruction** `TSL RX, LOCK`: it reads the memory word `LOCK` into register `RX` and **stores a non-zero value in `LOCK`** in one indivisible operation (the memory bus is locked for other CPUs). It allows mutual exclusion on multiprocessors, where disabling interrupts is not enough.

```text
enter_region:
    TSL REGISTER, LOCK     | copy lock to register and set lock to 1 (atomic)
    CMP REGISTER, #0       | was lock zero?
    JNE enter_region       | if it was non-zero, the lock was set, so loop (busy wait)
    RET                    | return to caller; critical region entered

leave_region:
    MOVE LOCK, #0          | store a 0 in lock
    RET                    | return to caller
```

**Use:** each process calls `enter_region()` before entering its critical region (it returns only when it has set the lock) and `leave_region()` after leaving it (clears the lock).

**Drawbacks**

- **Busy waiting (spin lock):** a process waiting for the lock burns CPU cycles.
- **Priority inversion:** a high-priority process spinning for a lock held by a low-priority process (which never gets the CPU on a single processor) can loop forever.
- It generates **bus traffic** (every TSL locks the memory bus) and gives **no fairness** (no queue; a process may starve).
- It requires hardware support, and the user can forget to call `leave_region` (not enforced).

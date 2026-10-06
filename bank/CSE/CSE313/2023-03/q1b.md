---
marks: 15
topics: [locks]
kind: numerical
source: {page: 18}
note: "Printed as 'worst-cast time' in (ii)."
---
Given a basic spinlock, assume that locking the spinlock takes **A** time units (if no one is holding the lock); unlock also takes **A** time units. Assume further that a context switch takes **C** time units, and that a time slice is **T** time units long.

Assume this code sequence, executed by **two** threads on **one** processor at roughly the same time:

```c
mutex_lock();
do_something();   // takes no time to execute
mutex_unlock();
```

i. What is the best-case time for the two threads on one CPU to finish this code sequence?

ii. What is the worst-cast time for the two threads to finish this code sequence? Assume that only **three** context switches can occur at a maximum.

iii. If the spin lock is instead changed to a queue-based lock, how does that change the worst-case time?

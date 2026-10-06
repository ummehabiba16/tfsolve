---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "wakeup moves every process sleeping on the address from the sleep hash queue to ready (in memory or swapped), puts it on the run queue and sets a flag if it should preempt the current process."
sources: ["Bach, ch. 6 (algorithm wakeup)"]
---
```text
algorithm wakeup
input:  sleep address
output: none
{
    raise processor execution level to block all interrupts;
    find sleep hash queue for the sleep address;
    for (every process asleep on the sleep address)
    {
        remove process from the hash queue of sleeping processes;
        mark the process state "ready to run";
        put the process on the scheduler's list of processes ready to run;
        clear the field in the process table entry that marked its sleep address;
        if (process is not loaded in memory)
            wake up the swapper process (process 0);
        else if (awakened process is more eligible to run than the currently running process)
            set the scheduler flag (run the scheduler on return to user mode);
    }
    restore processor execution level to its original level;
}
```

The processor level is raised because **interrupt handlers also call `wakeup`**. Note that waking a process does **not** run it immediately: it only becomes ready, and the scheduler picks it later, which is why processes must re-check the condition they slept for.

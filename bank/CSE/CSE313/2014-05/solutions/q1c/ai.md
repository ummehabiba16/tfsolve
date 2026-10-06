---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A race for a free buffer: two processes find the same free buffer, or an interrupt handler frees a buffer while the kernel manipulates the list; solved by blocking interrupts and by locking the buffer (marking it busy) before use, and re-searching after any sleep."
sources: ["Bach, ch. 3 (races in getblk/brelse)"]
---
**Scenario 1: a race between two processes.** Block $b$ is not in the cache and the free list has a single buffer $X$. Process P calls `getblk(b)`, sees that the free list is not empty, and is about to take $X$; before it marks $X$ busy, the process **is interrupted/preempted** (for example it starts reading the free list and an I/O interrupt occurs or its quantum ends) and process Q runs `getblk(c)` and **takes $X$** for block $c$. When P continues it would use a buffer that is no longer free: two processes use the same buffer, and the cache is corrupted.

**Scenario 2: a race between a process and an interrupt handler.** While `getblk` is removing a buffer from the free list, a **disk interrupt handler** calls `brelse` for another buffer and inserts it into the same list, in the middle of the pointer manipulation: the list pointers are corrupted.

**Solutions**

- **Raise the processor execution level to block interrupts** while the free list and hash queues are manipulated (as `brelse` and `getblk` do), so the update is atomic with respect to interrupt handlers.
- A buffer is **locked ("marked busy") and removed from the free list** by the process that gets it, before the process can do anything that might sleep; anyone else who needs it **sleeps**.
- A process that slept re-runs the **`while (buffer not found)` loop** after waking up (the `continue` statements), so it never relies on a state observed before it slept.
- On a multiprocessor, spin locks around the lists are used in addition.

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Cache coherence overhead: a process that moves to another CPU finds a cold cache and its data must be invalidated/transferred in the old one; solve with cache affinity, per-processor ready queues and migrate only to balance load."
sources: ["Anderson and Dahlin, OSPP, ch. 7 (multiprocessor scheduling: affinity scheduling)"]
---
**The problem.** On a multiprocessor each CPU has its own **cache**. A sequential application builds up useful state (code, data) in the cache of the CPU on which it runs. If the scheduler moves the process to **another CPU** (e.g. taking the next ready process from a **single shared ready queue**):

- the new CPU's cache is **cold**: the process suffers a burst of cache misses until its working set is reloaded;
- the data cached by the old CPU must be **invalidated or transferred** by the cache-coherence hardware, which generates **bus/interconnect traffic**; and
- the shared queue is also a point of **lock contention**.

This extra cost of migrating a process, caused by keeping caches coherent and by losing cached state, is the "cache coherence overhead" (it can make a parallel system slower than expected).

**Solution: cache (processor) affinity scheduling.**

1. Keep a **per-processor ready queue** (no shared-queue lock contention).
2. Schedule a process on the **same CPU** that ran it last whenever possible, so it finds its data still in the cache.
3. Allow **migration only when needed to balance the load** (e.g. an idle CPU steals work from a busy CPU's queue), i.e. when the cost of an idle CPU outweighs the cost of the cache reload.

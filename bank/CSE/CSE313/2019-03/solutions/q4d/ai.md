---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A cache coherence protocol keeps the copies of a shared word in different caches consistent; a write to a word cached elsewhere invalidates (or updates) the other copies."
sources: ["Tanenbaum MOS 4e, sec. 8.1.3 (cache coherence; snooping and directory protocols)"]
---
**Cache coherence protocol.** In a multiprocessor each CPU has its own cache, so the same memory word may be in several caches. A coherence protocol ensures that **all CPUs always see the same value of a word**, i.e. that no CPU reads a stale copy after another CPU has written it.

**Writing a word that is in one or more remote caches.** In the common *write-invalidate* protocols (e.g. snooping write-through, or MESI with a directory in NUMA machines):

1. The writing CPU's cache controller sends an **invalidation** for that cache line on the bus (or, in a directory-based machine, to the node that is the line's home, which looks up the nodes that cache it and sends them invalidation messages).
2. Every other cache that holds the line **marks its copy invalid** (and a cache holding a dirty copy first writes it back).
3. The writer then updates its own copy (in write-through, also memory); it now holds the only valid copy.
4. If another CPU later reads the word, it takes a cache miss and fetches the up-to-date value.

(A *write-update* protocol would instead send the new value to all other caches that hold the line.)

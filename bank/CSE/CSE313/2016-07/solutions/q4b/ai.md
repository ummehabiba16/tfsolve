---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Web server cache: LFU (LRU also works); DNS cache: LRU; e-mail inbox: LRU (FIFO acceptable); looping references larger than the cache: MRU (random next best)."
sources: ["Anderson and Dahlin, OSPP, ch. 9.3 / ch. 10 (caching and replacement policies)"]
---
| Usage scenario | Random | FIFO | LRU | LFU | MRU | Reason |
|:--|:-:|:-:|:-:|:-:|:-:|:--|
| **Web server cache** | | | $\checkmark$ | $\checkmark$ | | a few pages are requested over and over (Zipf-like): keep the **most frequently** (and recently) used ones; LFU best, LRU also good |
| **Browser DNS cache** | | | $\checkmark$ | | | sites visited recently are visited again soon (**temporal locality**); LRU (entries also expire by TTL) |
| **E-mail client inbox** | | $\checkmark$ | $\checkmark$ | | | the newest/most recently read messages are the ones read again; LRU (FIFO by arrival is a simple approximation) |
| **Looping memory references** (loop over more blocks than the cache holds) | $\checkmark$ | | | | $\checkmark$ | LRU and FIFO always evict the block that will be needed next (every reference misses); **MRU** (or random) keeps part of the loop in the cache |

*Note:* the paper leaves the cells blank, so one best choice and acceptable alternatives are marked; the answer depends on the stated workload.

---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "First-fit: allocate from the first free chunk that is large enough (advantage: fast, simple). Best-fit: allocate from the smallest free chunk that is large enough (advantage: least wasted space / less fragmentation; large chunks are kept for large requests). Next-fit: like first-fit but start searching where the last allocation ended (advantage: faster search and better spatial locality, since objects allocated together end up close together)."
sources: ["KMS Chapter 7 slides 36-43 (Heap Fragmentation, Heap Allocation Strategies, Bin-based Heap)", "Dragon book 2e sec. 7.4.4"]
---
The memory manager keeps the free space of the heap as a set of free chunks ("holes"). A request for $n$ bytes is satisfied from a free chunk of size $\ge n$; any remainder stays free.

**(i) First-fit.** Scan the free chunks from the beginning, and allocate from the **first** chunk that is large enough.

*Advantage:* simple and **fast**: the search stops at the first match. In practice its fragmentation is also reasonable.

**(ii) Best-fit.** Search the free chunks and allocate from the **smallest** chunk that is large enough. With bins of chunks sorted by size, this is efficient.

*Advantage:* **least waste and least fragmentation.** The leftover piece is as small as possible, and large free chunks are not broken up, so they remain available for later large requests. Studies show best-fit gives good overall memory utilisation.

**(iii) Next-fit.** Like first-fit, but the search starts from **where the last allocation was made** (a roving pointer), wrapping around if needed.

*Advantage:* **faster** on average, because it does not repeatedly scan the many small chunks that accumulate at the start of the heap. It also improves **spatial locality**: objects allocated one after another are placed close together, and such objects are often used together.

**Example:** free chunks of 100, 30 and 60 bytes (in that order), request 25 bytes. First-fit takes it from the 100-byte chunk. Best-fit takes it from the 30-byte chunk, leaving only 5 bytes. Next-fit takes it from the chunk after the previous allocation point.

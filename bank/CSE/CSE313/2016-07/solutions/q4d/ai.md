---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) True: the last page of every segment is partly empty. (ii) True: example with a 2-block cache where direct-mapped gets 5 hits and fully associative FIFO gets 3 on the same references."
sources: ["Anderson and Dahlin, OSPP, ch. 9-10 (internal fragmentation; cache associativity and replacement)"]
---
**(i) "A virtual memory system that uses paging is vulnerable to internal fragmentation": TRUE.** Memory is allocated in fixed-size pages; a program's size is generally not a multiple of the page size, so the **last page** of each segment (code, data, stack) is only partly used; the unused remainder cannot be given to anyone else. On average half a page per segment is wasted.

**(ii) "A direct-mapped cache can sometimes have a higher hit rate than a fully associative cache with FIFO replacement": TRUE.** A fully associative cache with FIFO evicts the *oldest* block even if it is used very often, while a direct-mapped cache happens to keep a hot block because conflicting blocks map elsewhere.

*Example.* A cache with 2 blocks. Blocks $A$ (maps to set 0) and $B$, $C$ (both map to set 1) are referenced as

$$A\,B\,A\,C\,A\,B\,A\,C\,A\,B\,A\,C$$

| Cache | Result per reference (H = hit, M = miss) | Hits |
|:--|:--|:-:|
| **Direct-mapped** | M M H M H M H M H M H M | **5** |
| **Fully associative, FIFO** | M M H M M M H M M M H M | **3** |

In the direct-mapped cache $A$ stays in its own line (only $B$ and $C$ conflict with each other); with FIFO the block $A$, loaded first, is always the one evicted when $C$ or $B$ arrives, so $A$ keeps missing. So the direct-mapped cache has the higher hit rate (5/12 vs 3/12), which shows that the more flexible cache is not always better.

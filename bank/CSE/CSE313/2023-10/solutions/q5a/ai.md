---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
changes:
  - "2026-09-30 (import review): stated the pure-LRU TLB assumption and the result with TLB invalidation on eviction."
---
Reference string: $1,2,3,4,5,2,3,1,2,3,4,5,1$ (13 references).

**(i) Belady's anomaly.** It is the counter-intuitive result that, for some replacement policies (notably FIFO), *increasing* the number of available page frames can *increase* the number of page faults, instead of decreasing or staying the same as one would expect. (Policies such as LRU/Optimal are "stack algorithms" and never exhibit this; only non-stack algorithms like FIFO can.)

*FIFO with 3 frames* (evict oldest):

|  Ref   |  1  |  2  |  3  |  4  |  5  |  2  |  3  |  1  |  2  |  3  |  4  |  5  |  1  |
|:------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Fault? |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  F  |  H  |  H  |  F  |  F  |  H  |

Total faults with 3 frames $=\mathbf{10}$ (hits only at the 9th,10th,13th references).

*FIFO with 4 frames*:

|  Ref   |  1  |  2  |  3  |  4  |  5  |  2  |  3  |  1  |  2  |  3  |  4  |  5  |  1  |
|:------:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Fault? |  F  |  F  |  F  |  F  |  F  |  H  |  H  |  F  |  F  |  F  |  F  |  F  |  F  |

Total faults with 4 frames $=\mathbf{11}$ (hits only at the 6th,7th references).

Since faults *increased* from 10 (3 frames) to 11 (4 frames) under FIFO, **Belady's anomaly is demonstrated** for this reference string at cache sizes 3 and 4.

**(ii) Optimal algorithm hit/miss rate.** (Evict the page whose next use is farthest in the future / never used again.)

*Optimal, 3 frames*: faults at refs 1,2,3,4,5,8,11,12 $\Rightarrow$ **8 faults**, 5 hits (refs 6,7,9,10,13). Hit rate $=5/13\approx38.5\%$, miss rate $=8/13\approx61.5\%$.

*Optimal, 4 frames*: faults at refs 1,2,3,4,5,11 $\Rightarrow$ **6 faults**, 7 hits. Hit rate $=7/13\approx53.8\%$, miss rate $=6/13\approx46.2\%$.

Note Optimal's fault count *decreases* (8$\to$ 6) as frames increase from 3 to 4 -- the opposite of FIFO above -- confirming that Optimal (like LRU) is a stack algorithm immune to Belady's anomaly.

**(iii) TLB (4-entry, LRU) + CLOCK (4-frame page cache) memory access time.** Using the given hint table, the page-cache CLOCK simulation for the 13 references yields **8 page-cache faults** (refs 1,2,3,4,5,8,11,12) and **5 page-cache hits** (refs 6,7,9,10,13) -- worked out by extending the given first-5-access table forward with the same sweep-and-second-chance rule.

Running a parallel 4-entry LRU TLB simulation over the same 13 references (TLB miss on every page-cache-cold/faulted access, since a never-before-mapped or evicted page cannot have a valid TLB entry either) gives:

- References 1--5: TLB miss *and* page fault (cold start) -- cost each $=$ TLB(5ns) $+$ page-table walk(60ns) $+$ disk(4,000,000ns) $+$ memory(60ns) $=\mathbf{4{,}000{,}125}$ns.

- References 6,7,9,10: page present, VPN still resident in the TLB $\to$ **TLB hit**, cost $=5+60=\mathbf{65}$ns each.

- References 8,11,12: page evicted from the cache earlier $\to$ TLB miss *and* page fault again, cost $=\mathbf{4{,}000{,}125}$ns each.

- Reference 13: page *is* present (frame from ref. 7's eviction cycle) but its TLB entry has since been evicted by the 4-entry LRU TLB $\to$ TLB miss but no page fault: cost $=$ TLB(5) $+$ page-table walk(60) $+$ memory(60) $=\mathbf{125}$ns.

**Total time** $= 8\times4{,}000{,}125 \;+\; 4\times65 \;+\; 1\times125$ $= 32{,}001{,}000 + 260 + 125 = \mathbf{32{,}001{,}385\text{ ns} \;\approx\; 32.0\text{ ms}}$.

*Assumption:* the TLB is managed purely by LRU over the reference string. A real OS must also invalidate a page's TLB entry when CLOCK evicts that page; with that rule page 2's entry is dropped at reference 12, page 1 stays in the TLB, reference 13 becomes a TLB hit (65 ns), and the total is $32{,}001{,}325$ ns. The totals differ by only 60 ns; write down which assumption you use.

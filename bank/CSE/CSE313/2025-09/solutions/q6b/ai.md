---
author: ai
via: chat
status: unverified
summary: "(i) Not really: it survives any one failure, and two only if one of them is the backup disk. (ii) (N-2) disks of capacity. (iii) Reads and sequential writes match an (N-1)-disk RAID-5; random writes collapse to a single disk's rate R because every small write also hits the fixed backup disk."
imported_from: cse313_mem_fs_solved.tex
changes:
  - "2026-09-30 (import review): sequential-write throughput corrected from S to (N-2)*S. On full-stripe writes the backup disk writes one block per stripe, like every other disk, so it is not a bottleneck. Only small random writes are capped at R."
---
Setup: $N$ disks in total. $N-1$ of them form an ordinary RAID-5 (rotating parity); the last one is a fixed **backup-parity disk** that gets a second copy of every parity block. $S$ and $R$ are one disk's sequential and random throughput.

**(i) Reliability: no real improvement.** RAID-5 already rebuilds any one lost disk. The copy of parity only helps when the *parity* is lost:

- It survives any single failure, as RAID-5 does.
- It survives two failures only if one of them is the backup disk (or, stripe by stripe, if one failed disk held that stripe's parity).
- Two failed disks that both hold data for the same stripes still lose data, because each stripe still has just one parity equation.

So Alice cannot promise tolerance of two disk failures, and she pays a whole extra disk for it. RAID-6 (two *different*, distributed parity blocks per stripe) is the design that survives any two failures.

**(ii) Effective capacity:** one disk's worth of rotating parity plus one backup disk, so $(N-2)$ disks of data, i.e. $\frac{N-2}{N}$ of raw capacity. That is one disk less than plain RAID-5 with the same $N$.

**(iii) Performance.** The inner RAID-5 has $N-1$ disks: sequential read and write $=(N-2)\,S$, random read $=(N-1)\,R$, random write $=\frac{N-1}{4}R$ (each small write is 4 I/Os: read old data and parity, write new data and parity).

- **Reads** never touch the backup disk: sequential $(N-2)\,S$, random $(N-1)\,R$. Unchanged.
- **Sequential (full-stripe) writes**: each stripe writes $N-2$ data blocks, 1 parity block and 1 backup-parity block, which is exactly **one block on every disk**, all in parallel. The backup disk does no more work than any other disk, so throughput stays $(N-2)\,S$.
- **Random (small) writes**: each needs the usual read-modify-write on its data and parity disks, *plus one write on the backup disk*. All small writes in the whole array land on that one disk, making it a hot spot like RAID-4's parity disk: random writes $\le R$. Together with the inner limit, $\min\!\big(\tfrac{N-1}{4}R,\;R\big)=R$ once $N\ge5$.

| | **Random** | **Sequential** |
|:--|:-:|:-:|
| **Read** | $(N-1)\cdot R$ | $(N-2)\cdot S$ |
| **Write** | $\min\{\tfrac{N-1}{4}R,\,R\} = R$ for $N\ge5$ | $(N-2)\cdot S$ |

**Conclusion for Alice.** RAID-5X costs one disk of capacity, still cannot promise to survive two failures, and turns the backup disk into a bottleneck for small random writes. With 9 disks, for example, plain RAID-5 gives $\tfrac{9}{4}R=2.25R$ of random writes; RAID-5X gives only $R$. Use RAID-6 instead.

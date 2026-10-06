---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Mirroring the parity disk lifts RAID-4 random-write throughput from R/2 to 2R/3 (still a bottleneck); random read and sequential read/write do not change."
sources: ["OSTEP ch. 38 (RAID-4, small-write problem)"]
---
**Plain RAID-4 random write.** Each small write needs the *subtractive parity* method: read the old data and the old parity, then write the new data and the new parity (4 I/Os). The two parity I/Os land on the **single parity disk**, every time, so the parity disk serialises all the writes: each user write costs it one read and one write, i.e. 2 I/Os, so

$$\text{random write} \approx \frac{R}{2}\quad(\text{independent of the number of disks }N).$$

**With the parity disk mirrored.**

- The parity *write* goes to both mirrors, in parallel; the parity *read* can be served by either mirror.
- Per user write, each mirror does 1 write plus half a read on average $= 1.5$ I/Os instead of 2.

$$\text{random write} \approx \frac{R}{1.5} = \frac{2R}{3}$$

A modest improvement (a factor $4/3$), but it is still limited by the parity pair (a bottleneck that does not grow with $N$), unlike RAID-5, which spreads the parity.

**Other workloads.**

- **Random read:** unchanged; the parity disk is never read, so $(N-1)\cdot R$.
- **Sequential read:** unchanged, $(N-1)\cdot S$ (parity not read).
- **Sequential write:** unchanged, $(N-1)\cdot S$: full-stripe writes compute the parity once and write it to both mirrors in parallel, taking the same time as before.

The mirror also improves *reliability* (the parity disk is no longer a single point of failure) at the cost of one more disk.

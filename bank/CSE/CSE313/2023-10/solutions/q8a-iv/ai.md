---
author: ai
via: chat
status: unverified
summary: "Segment writes: RAID-0 about 842 MB/s, RAID-1 about 457 MB/s (every byte is written twice). Single 4 KB reads: about 266 KB/s per disk in both, up to 10x under concurrent reads."
imported_from: cse313_mem_fs_solved.tex
changes:
  - "2026-09-30 (import review): RAID-1 segment write corrected. In OSTEP's RAID-1 model the 10 disks form 5 mirrored pairs and data is striped across the pairs, so sequential writes reach (N/2)*S, not a single disk's rate."
  - "2026-09-30 (import review): added a note on using the maximum vs. average seek time."
---
Disk config: capacity 1TB, 10,000 RPM, max seek 12ms, max transfer 100MB/s, block size 4KB, sector 1KB. Convention: lfs reads one 4KB block at a time; writes one 64MB segment at a time; a single disk operation moves one sector (1KB) at a time.

Average rotational latency $=\frac{60000\text{ms}}{10000\text{RPM}}\Big/2 = 3$ms (half a rotation, at 6ms/revolution).

**Single random 4KB block read (lfs read granularity), one disk:** time $\approx$ seek(12ms, the given maximum) $+$ rotational latency(3ms) $+$ transfer($4$KB$/100$MB/s $\approx0.04$ms) $\approx \mathbf{15.04}$ms $\Rightarrow$ throughput $\approx 4\text{KB}/15.04\text{ms}\approx266$KB/s *per outstanding request*.

*Note:* the table gives only the **maximum** seek time, used above as a conservative bound. OSTEP approximates the average seek as one third of a full seek ($\approx4$ms); with that, a random 4KB read takes $\approx4+3+0.04=7.04$ms ($\approx568$KB/s per disk). State whichever assumption you use.

**64MB segment write, one disk (baseline):** time $\approx12\text{ms (seek)}+64\text{MB}/100\text{MB/s}(=640\text{ms})\approx652$ms $\Rightarrow$ throughput $\approx64\text{MB}/0.652\text{s}\approx98$MB/s.

**RAID-0 (striped across all 10 disks, no redundancy):**

- *Segment write*: the 64MB segment is striped across the 10 disks in parallel, each disk only has to write $64/10=6.4$MB. Time $\approx12\text{ms}+6.4\text{MB}/100\text{MB/s}(=64\text{ms})\approx76$ms $\Rightarrow$ **throughput $\approx64\text{MB}/0.076\text{s}\approx842$MB/s**, roughly $8.6\times$ a single disk ($N\cdot S$ minus the seek).
- *Single 4KB block read*: one small block lands on (and is served by) one disk, so a single isolated request sees no speedup ($\approx266$KB/s). Striping helps only when *several* reads are outstanding and hit different disks: up to $\approx10\times266\text{KB/s}\approx2.6$MB/s ($N\cdot R$).

**RAID-1 (10 disks = 5 mirrored pairs; data striped across the pairs, as in OSTEP's RAID-1):**

- *Segment write*: every block is written to *both* disks of its pair, so only 5 pairs' worth of bandwidth is useful. The segment is striped over the 5 pairs; each pair writes $64/5=12.8$MB (both mirrors in parallel). Time $\approx12\text{ms}+12.8\text{MB}/100\text{MB/s}(=128\text{ms})\approx140$ms $\Rightarrow$ **throughput $\approx64\text{MB}/0.140\text{s}\approx457$MB/s**, about $(N/2)\cdot S$: half of RAID-0, because every byte is written twice.
- *Single 4KB block read*: either copy can serve it, so an isolated read takes about the same time as on one disk ($\approx266$KB/s). Under concurrent random reads all 10 disks can serve different requests, giving up to $\approx10\times$ a single disk ($N\cdot R$), the same as RAID-0.

**Summary**: for lfs's large segment *writes*, RAID-0 ($\approx842$MB/s) beats RAID-1 ($\approx457$MB/s) because mirroring writes every byte twice. For lfs's small block *reads*, a single request runs at single-disk speed in both; with many concurrent reads both scale to about $10\times$.

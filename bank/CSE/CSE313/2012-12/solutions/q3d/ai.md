---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Block size trades space against speed: large blocks waste space (internal fragmentation) but give high transfer rates, small blocks save space but need more seeks and metadata."
sources: ["Tanenbaum MOS 4e, sec. 4.4.1 (block size)"]
---
The disk block is the **unit of allocation and transfer**, so its size affects both disk space utilisation and performance, in opposite directions:

- **Too large:** **internal fragmentation**: on average half a block per file is wasted, and for small files (median file size about 2 KB) most of a big block is empty. E.g. 64 KB blocks would waste about 97% of the disk for 2 KB files.
- **Too small:** a file occupies **many blocks**, so it needs more **disk transfers (seeks and rotational delays)**: reading $s$ bytes costs about $(\text{seek}+\text{rotational delay}+\text{block transfer time})\times s/k$ for block size $k$, and the time is dominated by seek and rotation for small $k$. Also more per-block **metadata** (pointers in the inode/FAT, bigger free-space bitmap) is needed.

**Example** (disk with a 10 ms seek, 8.33 ms rotation time, 256 KB per track): the time to read a $k$-byte block is $10+4.17+k/256\text{ KB}\times8.33$ ms. For $k=1$ KB the data rate is about 70 KB/s; for $k=32$ KB about 1.7 MB/s: the larger the block, the better the speed, but the lower the space efficiency (about 100% for 1 KB and only about 6% for 32 KB with 2 KB files). The block size must be chosen as a compromise (typically 1-8 KB).

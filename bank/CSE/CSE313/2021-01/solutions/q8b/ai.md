---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "V7 i-node: 10 direct pointers plus single, double and triple indirect blocks; with 1 KB blocks and 4-byte addresses the maximum file is about 16 GB."
sources: ["Tanenbaum MOS 4e, sec. 4.5.2 (the UNIX V7 file system)"]
---
The UNIX V7 file system keeps all the block addresses of a file in its **i-node**, which has **13 disk addresses**: the first **10 are direct**, the other 3 are **single, double and triple indirect**. Small files need no extra block; large files use pointer blocks.

![UNIX V7 i-node and its indirect blocks](figures/v7inode.png)

With 1 KB blocks and 4-byte disk addresses, a pointer block holds $1024/4=256$ addresses:

| Pointers | Blocks reached |
|:--|:-:|
| 10 direct | 10 |
| single indirect | $256$ |
| double indirect | $256^2 = 65{,}536$ |
| triple indirect | $256^3 = 16{,}777{,}216$ |
| **Total** | about $16.8\times10^6$ blocks $\approx$ **16 GB** |

To read block number $b$ of a file: if $b<10$ use the direct pointer; else if $b<10+256$ read the single-indirect block and use entry $b-10$; else use the double (and, for still larger $b$, the triple) indirect block, going one level deeper for each extra level. The extra pointer blocks are read only for large files, and frequently used ones stay in the buffer cache.

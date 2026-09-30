---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
changes:
  - "2026-09-30 (import review): layout after the three requests now includes A's 256 KB block."
---
Total memory $=1024$KB, minimum block $=64$KB, so blocks can be sized $1024,512,256,128,64$ KB (a binary buddy tree).

**(i) Satisfying the requests.**

- **A (200KB)** $\to$ rounded up to the nearest power of two $=256$KB. Split $1024\to512+512$, split one $512\to256+256$, allocate one $256$KB block to A. *Free:* one 256KB block, one 512KB block.

- **B (100KB)** $\to$ rounded up to $128$KB. Split the free 256KB block into $128+128$, allocate one $128$KB block to B. *Free:* one 128KB block, one 512KB block.

- **C (300KB)** $\to$ rounded up to $512$KB. Allocate the whole free 512KB block to C (internal fragmentation $=512-300=212$KB). *Free:* one 128KB block only.

Layout after all three requests: `[256KB: A] [256KB: split -> 128(B) | 128(free)] [512KB: C]`.

**(ii) After freeing A.** A's 256KB block becomes free. Its *buddy* is the other 256KB half of the original 512KB block -- but that buddy is currently *split* (one 128KB half is allocated to B, the other is free), i.e., it is not free *as a whole* 256KB unit. **Merging is therefore not possible.** The freed 256KB block simply becomes a free chunk on its own.

New layout: `Free 256KB` $\;|\;$ `128KB (B)` $\;|\;$ `Free 128KB` $\;|\;$ `512KB (C)`.

**(iii) Fragmentation.**

- *Internal fragmentation*: B wastes $128-100=28$KB; C wastes $512-300=212$KB. **Total internal fragmentation $=240$KB.**

- *External fragmentation*: total free memory is $256+128=384$KB, but it exists as two separate, non-buddy chunks that cannot be merged into one. So a request for, say, $300$KB could *not* be satisfied even though $384$KB is free in total $\Rightarrow$ external fragmentation is present.

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Assuming 1 KB blocks and 4-byte addresses, byte 400,000 is in logical block 390 (offset 640): double indirect entry, first index block, entry 124."
sources: ["Bach, ch. 4 (algorithm bmap)"]
---
**Assumptions.** The question gives no block size: take 1 KB blocks and 4-byte block numbers ($256$ pointers per index block) in the System V inode: 10 direct entries, then single, double and triple indirect.

$$\text{logical block}=\lfloor400{,}000/1024\rfloor=390,\qquad\text{offset in block}=400{,}000-390\times1024=640$$

| Range of logical blocks | Reached through |
|:--|:--|
| 0-9 | direct |
| 10-265 (256 blocks) | single indirect |
| **266-65,801** ($256^2$ blocks) | **double indirect** |

$390\ge266$, so the block is in the **double-indirect** range; $390-266=124$.

- index in the double-indirect block: $\lfloor124/256\rfloor=\mathbf0$
- index in that single-indirect block: $124\bmod256=\mathbf{124}$

**Path:** inode entry 11 (double indirect, 0-based entry 11) $\to$ double-indirect block, entry **0** $\to$ single-indirect block, entry **124** $\to$ **data block**, at byte **640**.

*(With 4 KB blocks and 1024 pointers per block the byte would be in logical block 97, offset 2,688, reached through the single indirect block, entry $97-10=87$.)*

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "i. about 513 MB (262,668 blocks x 2 KB); ii. yes: 12 direct + 1 indirect + 99 second-level indirect blocks, spread over block groups; iii. about 1.5 s."
sources: ["OSTEP ch. 40 (multi-level index)", "OSTEP ch. 41 (FFS, large-file exception)"]
---
**Parameters.** $1\text{ TB}/2\text{ KB} = 2^{29}$ blocks, so a block address needs 29 bits $\Rightarrow$ a 4-byte pointer. Pointers per block $=2048/4 = 512$.

**i. Maximum file size.**

$$\text{blocks} = 12 + 512 + 512^2 = 262{,}668$$

$$262{,}668 \times 2\text{ KB} = 525{,}336\text{ KB} \approx \mathbf{513\ MB}$$

**ii. A 100 MB file.** $100\text{ MB}/2\text{ KB} = 51{,}200$ blocks, which is below the limit, so **it can be stored**. The pointers used:

- 12 direct blocks: 12;
- single indirect: 512 more blocks (total 524);
- double indirect: the remaining $51{,}200-524 = 50{,}676$ blocks, which need $\lceil 50676/512\rceil = 99$ second-level indirect blocks (98 full ones and one with 500 pointers), plus the double-indirect block itself.

**Placement in FFS.** FFS puts the inode and the first chunk of the data (the 12 direct blocks, 24 KB) in the **same block group**. If it kept filling that group, one big file would fill it and spoil locality for the other files, so (the *large-file exception*, OSTEP ch. 41) FFS puts every further chunk in a **different block group**: the single-indirect block with its 512 data blocks in one group, and each of the 99 second-level indirect blocks together with its (up to) 512 data blocks in other groups, chosen in turn. Each chunk is contiguous, so it can be read sequentially.

**iii. Time to read the file.** Assume one positioning (5 ms) per chunk: 1 (direct) + 1 (indirect) + 99 (double-indirect chunks) $= 101$ chunks, plus one for the inode and the double-indirect block:

$$T_{\text{position}} \approx 102\times 5\text{ ms} = 510\text{ ms}$$

$$T_{\text{transfer}} = \frac{100\text{ MB}}{100\text{ MB/s}} = 1000\text{ ms}$$

$$T \approx 1000 + 510 \approx \mathbf{1.5\ s}$$

(About two thirds of the time is useful transfer; the large-file exception costs an extra half second but keeps the groups balanced.)

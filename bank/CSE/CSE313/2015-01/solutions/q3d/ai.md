---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Max file size (9+512+512^2+512^3+512^4) x 4 KB = 282,025,808,400,384 B (about 256.5 TB); byte 1,000,000 is in block 244 (offset 576), reached through the single indirect entry, index 235."
sources: ["Bach, ch. 4 (bmap); Tanenbaum MOS 4e, sec. 4.3.2"]
---
Block 4 KB; block address 64 bits $=8$ bytes $\Rightarrow$ $4096/8=512$ pointers per block. The variant table of contents: **9 direct**, 1 single, 1 double, 1 triple, 1 quadruple indirect.

| Entries | Data blocks |
|:--|:-:|
| 9 direct | 9 |
| single indirect | $512$ |
| double indirect | $512^2=262{,}144$ |
| triple indirect | $512^3=134{,}217{,}728$ |
| quadruple indirect | $512^4=68{,}719{,}476{,}736$ |
| **Total** | **68,853,957,129** |

$$68{,}853{,}957{,}129\times4096\text{ B}=282{,}025{,}808{,}400{,}384\text{ B}\approx\mathbf{256.5\ TB}\ (2^{48}\text{ B plus a little})$$

**Location of byte offset 1,000,000.**

$$\text{block}=\lfloor1{,}000{,}000/4096\rfloor=244,\qquad\text{offset in block}=1{,}000{,}000-244\times4096=576$$

Direct entries cover blocks $0\ldots8$; the **single indirect** entry covers blocks $9\ldots520$. Block 244 is in this range, at index $244-9=235$ of the single-indirect block.

**Path:** inode entry 9 (the single-indirect entry, 0-based) $\to$ index block, entry **235** $\to$ **data block**, byte **576** within it.

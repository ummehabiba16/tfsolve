---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(ii) (10+256+256^2+256^3) x 1024 B = 17,247,250,432 B; (iii) the pointer structure (about 16 GiB) is the limit, not the 8-byte size field; (iv) offset 360,000 = block 351, in the double indirect range: DI entry 0, single-indirect entry 85, byte 576."
sources: ["Bach, ch. 4 (inode structure, algorithm bmap)"]
---
**(i) The inode table of contents (UNIX System V).** The inode contains a table of contents of **13 entries** holding disk block numbers: **entries 0-9 are direct** (they point to the first 10 data blocks of the file), **entry 10 is single indirect** (a block of block numbers), **entry 11 is double indirect** (a block of single-indirect blocks) and **entry 12 is triple indirect**. Small files use only the direct entries; larger files use the indirect entries.

**(ii) Maximum byte capacity** (block 1024 B, 4-byte block numbers $\Rightarrow$ $1024/4=256$ pointers per block):

$$\text{blocks}=10+256+256^2+256^3=10+256+65{,}536+16{,}777{,}216=16{,}843{,}018$$

$$16{,}843{,}018\times1024\text{ B}=\mathbf{17{,}247{,}250{,}432\text{ bytes}}\approx16.06\text{ GiB}$$

**(iii) 8-byte file-size field.** The field could hold sizes up to $2^{64}-1$ bytes ($\approx16$ EiB), so the **limit is imposed by the block-pointer structure**: the maximum file size of the system is still **$17{,}247{,}250{,}432$ bytes** ($\approx16$ GiB). (With a 4-byte size field it would be limited to $2^{32}$ bytes $=4$ GiB.)

**(iv) Where is byte offset 360,000?**

$$\text{block}=\lfloor360{,}000/1024\rfloor=351,\qquad\text{offset in block}=360{,}000-351\times1024=576$$

- Direct entries cover blocks $0\ldots9$; single indirect covers $10\ldots265$; **double indirect covers $266\ldots65{,}801$.**
- Block 351 is in the **double-indirect range**: $351-266=85$.
- First-level index in the double-indirect block: $\lfloor85/256\rfloor=0$; index in that single-indirect block: $85\bmod256=85$.

**Path:** inode table-of-contents entry 11 $\to$ **double-indirect block**, entry **0** $\to$ **single-indirect block**, entry **85** $\to$ **data block**, byte **576** of that block.

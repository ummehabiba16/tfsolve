---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(10 + 1024 + 1024^2 + 1024^3) blocks x 4 KB = 1,074,791,434 blocks, about 4.4e12 bytes (4.0 TiB); a 32-bit size field would limit files to 4 GB."
sources: ["Bach, ch. 4 (inode block addressing)", "Tanenbaum MOS 4e, sec. 4.3.2"]
---
Usual UNIX System V table of contents: **10 direct** blocks and **single, double and triple indirect** blocks. Block size $=4$ KB, block address $=32$ bits $=4$ bytes, so a pointer block holds $4096/4=1024$ addresses.

| Entries | Data blocks addressed |
|:--|:-:|
| 10 direct | 10 |
| single indirect | $1024$ |
| double indirect | $1024^2=1{,}048{,}576$ |
| triple indirect | $1024^3=1{,}073{,}741{,}824$ |
| **Total** | **1,074,791,434** |

$$1{,}074{,}791{,}434\times4096\text{ B}=4{,}402{,}345{,}713{,}664\text{ B}\approx\mathbf{4.0\ TiB\ (4.4\times10^{12}\text{ bytes})}$$

*Remark.* If the inode's size field is only 32 bits, the file size is limited to $2^{32}=4$ GB regardless of the pointer structure; the figure above is the capacity of the block-pointer structure.

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Max file size (16+128+128^2+128^3) x 512 = 1,082,204,160 B (about 1.01 GiB); the middle data block is block 1,056,840, reached through the triple indirect block, indices 63, 63, 56."
sources: ["Bach, ch. 4 (algorithm bmap)"]
---
Block size 512 B, block number 4 bytes $\Rightarrow$ $512/4=128$ pointers per index block.

| Entries | Data blocks |
|:--|:-:|
| 16 direct | 16 |
| single indirect | $128$ |
| double indirect | $128^2=16{,}384$ |
| triple indirect | $128^3=2{,}097{,}152$ |
| **Total** | **2,113,680** |

$$2{,}113{,}680\times512\text{ B}=\mathbf{1{,}082{,}204{,}160\text{ bytes}}\approx1.01\text{ GiB}$$

**The middle data block.** The file has 2,113,680 blocks, so the middle block is number $2{,}113{,}680/2=\mathbf{1{,}056{,}840}$ (counting from 0).

- Direct blocks: $0\ldots15$; single indirect: $16\ldots143$; double indirect: $144\ldots16{,}527$. Block 1,056,840 is beyond these, so it is in the **triple-indirect** range.
- Offset in the triple range: $1{,}056{,}840-(16+128+16{,}384)=1{,}040{,}312$.
- First-level index (in the triple-indirect block): $\lfloor1{,}040{,}312/16{,}384\rfloor=\mathbf{63}$ (remainder $8{,}120$).
- Second-level index: $\lfloor8{,}120/128\rfloor=\mathbf{63}$ (remainder $\mathbf{56}$).
- Third-level index (in the single-indirect block): **56**.

**Path:** inode triple-indirect entry $\to$ block, entry **63** $\to$ block, entry **63** $\to$ block, entry **56** $\to$ the **data block** (the middle block of the file).

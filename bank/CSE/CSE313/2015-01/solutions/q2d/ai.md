---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Block = start + (inode-1)/inodes-per-block, byte offset = ((inode-1) mod inodes-per-block) x inode size: inode 555 is in block 22 at byte offset 720."
sources: ["Bach, ch. 4 (algorithm iget: locating the disk inode)"]
---
The inodes are stored in the inode list consecutively starting at a known block; inode numbers start at 1.

$$\text{block number}=\left\lfloor\frac{\text{inode number}-1}{\text{inodes per block}}\right\rfloor+\text{start block of the inode list}$$

$$\text{byte offset in block}=\big((\text{inode number}-1)\bmod\text{inodes per block}\big)\times\text{size of a disk inode}$$

For inode number 555, start block 5, 32 inodes per block, inode size 72 bytes:

- $(555-1)/32=554/32=17$ (remainder $554-17\times32=10$)
- **block number** $=17+5=\mathbf{22}$
- **byte offset** $=10\times72=\mathbf{720}$ bytes within block 22.

(The kernel reads block 22 with `bread` and copies the 72 bytes at offset 720 into the in-core inode.)

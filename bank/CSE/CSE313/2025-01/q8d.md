---
marks: 13
topics: [lfs]
---
Suppose you are using a Log-structured File System (LFS). Given the initial layout of the file shown in Figure for 8(d) below, if a byte in the file is modified, what changes will occur? Finally, draw the updated layout after the modification.

| $D$ | $I$ &nbsp; ($b[0]{:}A0$) |
|:-:|:-:|
| data block at address $A0$ | the file's inode, pointing to $A0$ |

*Figure for 8(d): Layout of a file in LFS*

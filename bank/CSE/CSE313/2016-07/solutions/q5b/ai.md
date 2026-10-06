---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "FFS multi-level index: a fixed-depth, unbalanced tree in the inode (12 direct + single/double/triple indirect), efficient for small files, good for large files, constant-time random access, supports sparse files."
sources: ["OSTEP ch. 40-41; Anderson and Dahlin, OSPP, ch. 13 (FFS inode)"]
---
In FFS (like Unix) the **inode** holds a fixed number of pointers: about **12 direct pointers** to data blocks, then a **single indirect**, a **double indirect** and a **triple indirect** pointer, each pointing to a block of pointers. Characteristics:

- **Efficient for small files:** most files are small, and they are reached through the direct pointers with **no extra block read**.
- **Scales to very large files:** each extra level multiplies the file size by the number of pointers per block (e.g. 1024); the triple-indirect level reaches terabytes.
- **Fixed depth (at most 4 block accesses, constant time):** a block's location is found in a bounded number of steps, so **random access is fast** and does not depend on the file size or on the position (unlike a linked list).
- **Unbalanced (asymmetric) tree:** deep levels exist only for large files, so the structure is not wasted on the common small file.
- **Flexible allocation:** data blocks can be anywhere on the disk (no contiguity), so growth and fragmentation are easy to handle; allocation heuristics (block groups) provide locality.
- **Sparse files** are supported: a null pointer means "no block allocated".
- **Small, fixed-size metadata:** the inode has a fixed size, so it can be found by number; indirect blocks are allocated only when needed.

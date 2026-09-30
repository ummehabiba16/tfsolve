---
author: ai
via: chat
status: unverified
summary: "create: read root inode, root data, foo inode, foo data; read and write the inode bitmap; write foo data; read and write bar inode; write foo inode (10 I/Os). write(): read bar inode; read and write the data bitmap; write bar data[0]; write bar inode (5 I/Os per block)."
imported_from: cse313_mem_fs_solved.tex
changes:
  - "2026-09-30 (import review): rewritten to follow OSTEP's creation timeline (Fig. 40.4, which the question's figure copies). The earlier answer skipped the path-traversal reads of root inode, root data and foo inode, and the read of bar's inode."
---
This is the file-creation timeline from OSTEP's *File System Implementation* chapter (Fig. 40.4). The question's figure uses the same columns. Nothing is cached, so opening `/foo/bar` starts by walking the path from the root.

**`create(/foo/bar)`**, in order:

1. read **root inode**, to find the root directory's data blocks
2. read **root data**, to find the entry `foo` and its inode number
3. read **foo inode**
4. read **foo data**, to check that `bar` does not exist and find a free slot
5. read **inode bitmap**, to find a free inode
6. write **inode bitmap**, marking it used
7. write **foo data**, adding the entry `bar` with its new inode number
8. read **bar inode**
9. write **bar inode**, initialising it (type, size 0, no blocks)
10. write **foo inode**, updating its modification time (and size, if the directory grew)

**`write()`**, appending text to `bar`:

1. read **bar inode**, to find where the data goes
2. read **data bitmap**, to find a free block
3. write **data bitmap**, marking it used
4. write **bar data[0]**
5. write **bar inode**, recording the new block pointer, size and time

If the appended text needs a second block, the same five steps repeat for **bar data[1]**. OSTEP draws one `write()` row per block.

**Filled figure** (numbers give the order within each row):

| | data bitmap | inode bitmap | root inode | foo inode | bar inode | root data | foo data | bar data[0] | bar data[1] |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| create(/foo/bar) | | 5 read, 6 write | 1 read | 3 read, 10 write | 8 read, 9 write | 2 read | 4 read, 7 write | | |
| write() | 2 read, 3 write | | | | 1 read, 5 write | | | 4 write | (if needed) |

So creating one file costs **10 I/Os**, and every appended block costs **5**: the bitmap read and write, the data write, and the inode read and write. This overhead is why real file systems cache these blocks.

---
marks: 10
topics: [ffs]
kind: diagram
source: {page: 23}
---
Bob has created the following files in an FFS (file sizes are written inside brackets).

- `/a/f1` (2KB)
- `/b/f2` (1KB)
- `/c/b/f3` (10 KB)
- `/c/f4` (7KB)
- `/b/f5` (60KB)

Suppose, the disk has 4KB blocks and 5 block group. If `/c/b` is symbolic link to the directory `/b`, show how the files will be saved with illustrative diagrams.

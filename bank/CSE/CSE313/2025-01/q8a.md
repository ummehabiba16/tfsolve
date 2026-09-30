---
marks: 10
topics: [ffs]
---
Bob has created the following files in an FFS (file sizes are written in brackets):

- /a/f1 (3KB)

- /b/f2 (5KB)

- /c/b/f3 (9KB)

- /c/f4 (7KB)

- /b/f5 (10KB)

Suppose the disk has 4KB blocks and 5 block groups. If `/c/b` is a symbolic link to the directory `/b` (we are uplifting the limitation) and the files were created in the order they appear, show how the files will be saved with illustrative diagram.

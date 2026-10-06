---
marks: 10
topics: [vsfs]
kind: numerical
source: {page: 27}
---
The i-node of a Unix-like file system has 12 direct, one single-indirect and one double-indirect pointers. The disk block size is 4 kB and the disk block address is 32-bits long. Calculate the maximum possible file size for this file system. (Note that a single-indirect pointer points to a block of pointers that then point to blocks of the file's data. A double-indirect pointer points to a block of pointers that point to other blocks of the pointers that then point to blocks of the file's data.)

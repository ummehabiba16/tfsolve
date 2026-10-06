---
marks: 15
topics: [ffs, vsfs]
kind: numerical
source: {page: 22}
---
Alice has implemented a fast file system (FFS) with inodes having 12 direct pointers, 1 indirect pointer and 1 double indirect pointer.

i. In a 1TB disk with 2KB blocks, how big of a file can be handled using Alice's file system?

ii. FFS divides the disk into multiple block groups. Now, can a 100 MB file be saved in Alice's file system? If so, then how all the data will be distributed on disk?

iii. If the disk spends 5ms time for positioning on the average and has 100MB/s transfer rate, how long will it take to read the file in (ii)?

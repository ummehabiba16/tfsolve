---
marks: 15
topics: [disk-scheduling]
kind: numerical
source: {page: 22-23}
---
Suppose the OS made the following 3 batch of block requests to a disk (each number represents block id):

- 1, 40, 2, 15
- 10, 1, 13, 32, 2, 7
- 70, 49, 0, 6, 28

The requests were sent in such a way that one batch is requested after the previous one is handled. The disk has 1GB capacity, 4KB blocks, 8 blocks in each track and max seek time of 100ms. Now, calculate how much time the disk will spend on seeking, if the disk head is initially on the first track and the scheduling algorithm is

i. SSTF

ii. SCAN

iii. C-SCAN

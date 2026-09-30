---
marks: 12
topics: [free-space]
---
The system has a total of 1024 KB of memory managed using the Buddy Memory Allocation algorithm. The minimum allocatable block size is 64 KB. Assume no memory is used initially. A sequence of memory allocation requests comes in:

I.  Request A: 200 KB

II. Request B: 100 KB

III. Request C: 300 KB

IV. Then Request A is freed.

Now answer the following (6+3+3=12):

i.  Show how the memory is divided to fulfill these requests using the Buddy system.

ii. After A is freed, explain if Buddy merging is possible. If so, show the new memory layout.

iii. What is the fragmentation after all allocations and deallocation? (Internal + External, if any)

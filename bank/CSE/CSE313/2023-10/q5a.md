---
marks: 28
topics: [page-replacement, tlb]
---
The following sequence of Virtual Page Numbers (VPN) has been referenced in your system:

$$1,2,3,4,5,2,3,1,2,3,4,5,1$$

Now, answer the following questions (7+7+14=28):

i.  Explain Belady's anomaly. Show that this anomaly occurs for cache size 3 and 4 in the above case.

ii. Calculate hit and miss rate for the optimal page replacement algorithm.

iii. If the TLB can keep at most 4 entries and employs LRU for TLB replacement and Page replacement uses CLOCK algorithm with cache size 4, calculate the memory access time for the above memory access sequence. TLB access takes 5ns, memory access takes 60ns, and disk access takes 4ms.

*Hint: The first 5 memory references in the CLOCK algorithm give the following cache states* ("?" refers to unused cache, the number in bracket refers to the *use bit*, and "\*" is the location of the clock hand):

| Access | Frame 1 | Frame 2 | Frame 3 | Frame 4 |
|:-:|:-:|:-:|:-:|:-:|
| 1 | 1(1)\* | ?(0) | ?(0) | ?(0) |
| 2 | 1(1) | 2(1)\* | ?(0) | ?(0) |
| 3 | 1(1) | 2(1) | 3(1)\* | ?(0) |
| 4 | 1(1) | 2(1) | 3(1) | 4(1)\* |
| 5 | 5(1)\* | 2(0) | 3(0) | 4(0) |

*Cache state after each access.*

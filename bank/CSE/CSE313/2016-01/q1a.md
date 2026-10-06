---
marks: 15
topics: [page-replacement]
kind: numerical
source: {page: 50}
note: "The reference string is printed '2, 3, 2, 1, 5, 2, 4, 5, 3, 2 5, 2' (a comma is missing between 2 and 5)."
---
Suppose the execution of a particular process requires reference to five distinct pages. The page reference sequence of the program is:

$$2, 3, 2, 1, 5, 2, 4, 5, 3, 2\ 5, 2$$

which means that the first page referenced is 2, the second page referenced is 3, and so on. Assume that the physical memory contains three page frames and all the page frames are initially empty. Depict the behavior of each of the following page replacement algorithms for this process.

(i) Optimal page replacement algorithm

(ii) First-In First-Out (FIFO) page replacement algorithm

(iii) Least Recently Used (LRU) page replacement algorithm

You must show the state of physical memory after each page reference and calculate total page hit for each algorithm.

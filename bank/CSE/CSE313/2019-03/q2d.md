---
marks: 5
topics: [paging]
kind: numerical
source: {page: 34}
note: "The page-table figure is kept as an image; the physical memory frames on the right are left blank in the paper."
---
Using the page table below, give the physical address corresponding to each of the following virtual addresses: (i) 20, (ii) 4100, and (iii) 8300

![Page table figure for Q2(d): 16 virtual pages of 4K (0K-64K) mapped to page frames](figures/q2d-1.png)

The virtual pages and their page-frame entries, as read from the figure (X = not mapped):

| Virtual page | Frame |
|:--|:-:|
| 0K-4K | 2 |
| 4K-8K | 1 |
| 8K-12K | 6 |
| 12K-16K | 0 |
| 16K-20K | 4 |
| 20K-24K | 3 |
| 24K-28K, 28K-32K, 32K-36K | X |
| 36K-40K | 5 |
| 40K-44K | X |
| 44K-48K | 7 |
| 48K-64K | X |

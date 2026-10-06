---
marks: 9
topics: [filesystems]
kind: diagram
source: {page: 57}
---
Assume, Shahid has a 10 MB solid-state drive in his PC. There is currently only one partition and no file in the SSD. The advertised block size of the SSD is 1 MB (1024 KB). Internally the file system layout of the SSD is as follows:

| Block 0 | Block 1 | Block 2 | Blocks 3...9 |
|:-:|:-:|:-:|:-:|
| MBR | Boot block | Super block / FATs | Data blocks |

Shahid now wants to create 4 files as described in the following table in the only partition of the SSD.

| File Name | Size |
|:-:|:-:|
| A | 3.6 MB |
| B | 1.0 MB |
| C | 0.9 MB |
| D | 0.6 MB |

How will the file system (installed on his SSD) allocate hard disk blocks to the above files if it uses any of the following allocation schemes? Describe using illustrative figures. (3x3=9)

(i) Contiguous allocation

(ii) Linked-List allocation

(iii) Linked-List allocation using a FAT in memory

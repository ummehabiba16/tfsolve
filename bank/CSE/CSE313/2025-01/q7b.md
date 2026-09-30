---
marks: 10
topics: [vsfs]
---
In VSFS, a new file (`/foo/bar`) was created and some text was appended. Mention the order of reading and writing to the blocks. You have to fill up the Figure for 7(b).

|  | data bitmap | inode bitmap | root inode | foo inode | bar inode | root data | foo data | bar data\[0\] | bar data\[1\] |
|:---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| create(/foo/bar) |  |  |  |  |  |  |  |  |  |
| write() |  |  |  |  |  |  |  |  |  |

*Figure for 7(b): File Creation Timeline (Time Increasing Downward)*

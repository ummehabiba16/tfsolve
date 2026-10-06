---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A directory is a file, so it can hold at most (max file size)/32 entries: 4,402,345,713,664 / 32 = 137,573,303,552 entries."
sources: ["Bach, ch. 4 (directories)"]
---
A directory is an ordinary file whose contents are a sequence of **fixed-size entries** (here 32 bytes: an inode number and a file name). The largest possible directory is therefore as large as the largest file of the system in 3(a):

$$\text{entries}=\frac{4{,}402{,}345{,}713{,}664\text{ B}}{32\text{ B}}=\mathbf{137{,}573{,}303{,}552}\text{ entries}\ (\approx1.4\times10^{11})$$

That is the maximum number of files and subdirectories in one directory (two of them are the entries `.` and `..`). In practice the number of inodes of the file system and the length of the inode-number field in the entry limit the number of different files further.

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Example: created 10:00, read 10:30, chmod 11:00: atime 10:30, mtime 10:00, ctime 11:00."
sources: ["Bach, ch. 4 (inode times: access, modification, change); Tanenbaum MOS 4e, sec. 10.6"]
---
An inode has three times: **atime** (last access to the data), **mtime** (last modification of the *contents*) and **ctime** (last change of the *inode*: permissions, owner, link count, size).

**Example.** A file `report.txt` is created and written at 10:00, read by a user at 10:30 and its permission bits are changed with `chmod 600 report.txt` at 11:00.

| Time | Event | atime | mtime | ctime |
|:-:|:--|:-:|:-:|:-:|
| 10:00 | file created and written | 10:00 | 10:00 | 10:00 |
| 10:30 | file read (`cat`) | **10:30** | 10:00 | 10:00 |
| 11:00 | `chmod 600` | 10:30 | **10:00** | **11:00** |

After the `chmod` the **content was not changed recently** (mtime still 10:00) and the file was not accessed (atime 10:30), but the **inode-change time is 11:00**: only ctime is updated by changing the permission bits (`ls -l --time=ctime` shows it).

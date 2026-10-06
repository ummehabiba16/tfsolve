---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "chmod changes the inode only: the inode-change time is updated; access and modification times stay unchanged."
sources: ["Bach, ch. 4 (inode fields: access, modification and inode-change times)"]
---
A UNIX inode keeps three times:

| Time | Updated when |
|:--|:--|
| **access** time (atime) | the file's data is read/executed |
| **modification** time (mtime) | the file's *contents* are written |
| **inode-change** time (ctime) | the *inode* changes: permissions, owner, link count, size, etc. |

`chmod` only changes the **permission bits stored in the inode**; it neither reads nor writes the file's data. Hence only the **inode-change time (ctime)** is set to the current time; the **access time and the modification time are unchanged**. (The kernel writes the inode back to disk as the in-core inode is released, since the inode changed.)

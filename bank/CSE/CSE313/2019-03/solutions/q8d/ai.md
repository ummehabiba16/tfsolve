---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "UNIX V7 i-node: mode, link count, owner and group, size, three timestamps, 13 disk addresses (10 direct + single, double, triple indirect)."
sources: ["Tanenbaum MOS 4e, sec. 4.5.2 (the UNIX V7 file system)"]
---
The i-node of the UNIX V7 file system holds the **attributes** of one file and the **disk addresses** of its blocks (but not the file name, which is in the directory):

| Field | Meaning |
|:--|:--|
| mode | file type (regular, directory, block/character special, ...) and the 9 protection bits (rwx for owner, group, others) plus set-uid/set-gid bits |
| link count | number of directory entries (hard links) pointing to the i-node |
| uid, gid | owner and group |
| size | file size in bytes |
| times | last access, last modification, last i-node change |
| disk addresses | **13 addresses**: the first 10 are *direct* (data blocks), the 11th is *single indirect*, the 12th *double indirect*, the 13th *triple indirect* |

![UNIX V7 i-node](figures/v7inode.png)

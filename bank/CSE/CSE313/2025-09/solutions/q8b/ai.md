---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
Disk: 4KB blocks, 5 block groups, chunk size $=4$ blocks (i.e. FFS switches a large file to a new group after every 4 consecutive blocks). Files (in creation order), sizes rounded up to whole 4KB blocks:

| Path                                | Size | Blocks needed |
|:------------------------------------|:-----|:--------------|
| /a/f1                               | 3KB  | 1             |
| /b/f2                               | 5KB  | 2             |
| /c/b/f3 (via symlink /c/b $\to$ /b) | 9KB  | 3             |
| /c/f4                               | 20KB | 5             |
| /b/f5                               | 10KB | 3             |

FFS places each new directory in the group with the most free inodes (here, with everything initially empty, this spreads them out): `a`$\to$Group0, `b`$\to$Group1, `c`$\to$Group2. A file's data blocks are placed in the *same* group as its parent directory's inode.

Because `/c/b` is a *symbolic link* to `/b` (not a real subdirectory), path resolution of `/c/b/f3` follows the link: `c`(Group2) $\to$ symlink `b` (a small special file that itself lives inside `c`'s directory, Group2, since that is where the entry "b" was created) $\to$ redirected to the *real* directory `/b` (Group1) $\to$ `f3` is created *inside* `/b`, so its data blocks go to **Group1**, right alongside `f2`.

`/c/f4` needs 5 blocks but the chunk size is only 4, so FFS's large-file policy kicks in: the first 4 blocks are placed with the parent (`c`, Group2); once the chunk limit is hit, FFS switches to a *different*, more free group for the remainder -- the 5th block spills into Group3.

**Resulting layout:**

| Group | Contents |
|:---|:---|
| Group 0 | dir `a`; `f1` (1 block) |
| Group 1 | dir `b`; `f2` (2 blocks); `f3` (3 blocks, arrived via the `/c/b` symlink); `f5` (3 blocks) |
| Group 2 | dir `c` (incl. the `b`$\to$/b symlink entry); `f4`'s first chunk (4 blocks) |
| Group 3 | `f4`'s overflow chunk (1 remaining block) |
| Group 4 | (empty) |

This illustrates two FFS principles at once: (1) a file always lands with its *real*, symlink-resolved parent directory, not with whichever path component was written in the pathname; (2) a large file that exceeds the chunk size is deliberately spread across multiple groups so it does not monopolize the free space of a single group.

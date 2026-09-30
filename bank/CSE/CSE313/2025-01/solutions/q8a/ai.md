---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
Disk: 4KB blocks, 5 block groups (no chunk-size limit is specified here, and all files below are small, so FFS's large-file group-spreading heuristic does not need to trigger). Files, sizes rounded up to whole 4KB blocks:

| Path                                | Size | Blocks needed |
|:------------------------------------|:-----|:--------------|
| /a/f1                               | 3KB  | 1             |
| /b/f2                               | 5KB  | 2             |
| /c/b/f3 (via symlink /c/b $\to$ /b) | 9KB  | 3             |
| /c/f4                               | 7KB  | 2             |
| /b/f5                               | 10KB | 3             |

As before, directories are spread across initially-empty groups: `a`$\to$Group0, `b`$\to$Group1, `c`$\to$Group2. Since `/c/b` is a symlink to `/b`, `f3` is actually created *inside* the real directory `/b` (Group1), not inside `c`.

**Resulting layout:**

| Group | Contents |
|:---|:---|
| Group 0 | dir `a`; `f1` (1 block) |
| Group 1 | dir `b`; `f2` (2 blocks); `f3` (3 blocks, via the `/c/b` symlink); `f5` (3 blocks) -- 8 data blocks total |
| Group 2 | dir `c` (incl. the symlink entry `b`$\to$`/b`); `f4` (2 blocks) |
| Group 3, 4 | (empty) |

Because none of the files here exceeds a would-be chunk-size threshold, every file's data stays entirely within its (symlink-resolved) parent directory's group -- unlike the 2023--24 version of this question, no large-file spreading across groups is needed.

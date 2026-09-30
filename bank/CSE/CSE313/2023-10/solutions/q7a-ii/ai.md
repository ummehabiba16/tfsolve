---
author: ai
via: chat
status: unverified
summary: "mv does not move data. FFS's large-file rule keeps the first 48 KB with the inode and puts every 4 MB chunk (one indirect block's worth) in a different group, so reading 1 GB takes about 257 x 10 ms + 10.24 s = 12.8 s."
imported_from: cse313_mem_fs_solved.tex
changes:
  - "2026-09-30 (import review): rewritten. The earlier answer assumed the 1 GB file sits in one block group (10.25 s). FFS's large-file exception (OSTEP ch. 41) spreads it over about 257 groups; the question's '4-byte block number, 4 KB block' and 'only moving between groups costs a positioning' point to that."
---
**Layout.** `mv` within one file system only rewrites directory entries: it removes `foo.txt` from `/q`'s directory data and adds `bar.txt`, with the same inode number, to `/p`'s. The file's inode and data blocks stay exactly where FFS put them when `foo.txt` was created, so the layout is decided by how FFS allocates a **large file**:

- The inode and the first **12 direct blocks** (48 KB) are placed in the same block group, the one FFS chose for the inode (near its parent directory `/q`).
- After that, each chunk that one **indirect block** maps goes to a **different block group** (one with plenty of free space). With 4-byte block numbers and 4 KB blocks, an indirect block holds $4096/4=1024$ pointers, so each chunk is $1024\times4$KB $=4$MB.

1 GB $=262{,}144$ blocks. After the 12 direct blocks, $262{,}132$ blocks remain, which is $\lceil 262{,}132/1024\rceil=256$ chunks. So the file occupies $1+256=257$ block groups: the first 48 KB, then 256 chunks of up to 4 MB. This keeps one huge file from filling a single group and wrecking locality for the other files in it.

**How ffs gets the information it needs.** Placement is decided when each block is allocated:

- The **block's position in the file** (direct, or which indirect block covers it) tells FFS when a new chunk starts, so it must switch groups.
- **Per-group free-space summaries** (free-block and free-inode counts in the superblock and group descriptors) tell it which group to use next.

Later, reads just follow the inode's direct and indirect pointers, which `mv` did not change.

**Sequential read time.** Reading the file visits 257 groups: 1 initial positioning plus 256 moves between groups, each costing 10 ms.

$$T \approx \underbrace{257\times10\text{ms}}_{2.57\text{ s positioning}} + \underbrace{\frac{1024\text{MB}}{100\text{MB/s}}}_{10.24\text{ s transfer}} \approx \mathbf{12.8\text{ s}}$$

If the file were contiguous in one group it would take $\approx10\text{ms}+10.24\text{s}\approx10.25$ s. The large-file rule costs about 25% more here in exchange for keeping every block group usable; bigger chunks would shrink that overhead.

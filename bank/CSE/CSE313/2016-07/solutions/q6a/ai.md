---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "FAT: no real locality heuristic (first free block), so fragmentation; FFS: block groups keep inode, directory and data together, large-file exception, reserved free space; NTFS: best-fit allocation of extents, MFT/metadata placement, defragmentation."
sources: ["Anderson and Dahlin, OSPP, ch. 13 (locality heuristics of FAT, FFS and NTFS)"]
---
| | **FAT** | **FFS** | **NTFS** |
|:--|:--|:--|:--|
| **Placement heuristic** | essentially **none**: a new block is the **first free block** found in the FAT (first fit), wherever it is | **block groups** (cylinder groups): the inode, the directory entries and the data of a file are placed in the **same group**; subdirectories are spread over groups | **best-fit** extent allocation: the allocator looks in the free-space bitmap for the smallest free run that fits the request; files grow by extents |
| **Locality of related data** | poor: files become fragmented over time; the FAT is at one end of the disk, so each access needs a seek to the FAT | good: related blocks are close, so reads of a file or directory need little seeking; a **large file exception** puts big files in several groups so one file does not fill a group | good for sequential access: contiguous extents; the MFT is placed in the middle of the disk to reduce seeks; small files stored in the MFT record |
| **Keeping free space usable** | needs a periodic **defragmentation** utility | **reserves 10% of the blocks** (the disk is considered full at 90%) so a free block near the file can be found | defragmenter, and best fit to limit external fragmentation; grows files in larger extents (pre-allocation) |

**Summary.** FAT has no real heuristic (locality only by luck), FFS places by **location (group)**, and NTFS by **extent size (best fit)** and metadata placement.

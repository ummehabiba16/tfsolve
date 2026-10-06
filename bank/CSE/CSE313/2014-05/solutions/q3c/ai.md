---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The remembered inode is the point from where the next scan for free inodes starts; when an inode with a smaller number is freed while the list is full, it becomes the new remembered inode so it is not missed."
sources: ["Bach, ch. 4 (algorithms ialloc and ifree)"]
---
The superblock free-inode list holds only a limited number of free inode numbers. The **remembered inode** is the **highest-numbered inode that was put into the list** the last time the list was refilled by scanning the inode list; the next scan starts from it, so the kernel does not have to rescan inodes it already looked at (the inodes below it are assumed in use or already in the list).

**Role when freeing an inode (`ifree`):**

- If the superblock list is **not full**: put the inode number in the list.
- If the list is **full**: do not store it, but **if its number is less than the remembered inode, set the remembered inode to this number**. The scan will then start from here and will find the freed inode again. (If the number is greater than the remembered inode, nothing needs to be done: a later scan from the remembered inode upward will reach it anyway.)

**Example.** The list is full and the remembered inode is 470 (the list holds numbers up to 470). Inode 120 is freed: list full, $120<470$, so the remembered inode becomes **120**; when the list empties, the scan starts at 120 and finds it. If inode 600 is freed instead: $600>470$, so it is ignored and will be found later, when the scan reaches it.

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A hard link needs no new inode (a new directory entry for the same inode, link count +1); a symbolic link (shortcut) uses one new inode of type link plus a data block with the path."
sources: ["Bach, ch. 5 (link) and ch. 4; Tanenbaum MOS 4e, sec. 4.5.2"]
---
It depends on the kind of shortcut.

**Hard link** (`ln /a/foo /b/bar`): **0 new inodes.** A new directory entry (`bar`, inode number $i$) is added to directory `b` and the **link count of the existing inode $i$** is incremented. Both names refer to the same inode.

**Symbolic link** (`ln -s /a/foo /b/sym`, the usual "shortcut"): **1 new inode**, of type *symbolic link*, whose data block holds the **path name** `/a/foo`; the directory entry `sym` points to this new inode. The original inode is not changed.

**Example of the changes in the disk inodes** (original file `/a/foo` = inode 7, link count 1):

| Action | Directory `b` | inode 7 | New inode |
|:--|:--|:--|:--|
| `ln /a/foo /b/bar` | new entry (`bar`, 7) | link count $1\to2$ | none |
| `ln -s /a/foo /b/sym` | new entry (`sym`, 12) | unchanged (count 1) | inode 12: type = symlink, size = 6, data block contains `/a/foo` |

Deleting the original name leaves the hard link working (count back to 1), while the symbolic link becomes dangling.

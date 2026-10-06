---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "namei walks the path name component by component: start at root or current directory, search each directory for the next component, iget the inode, check permissions and mount points, until the last component."
sources: ["Bach, ch. 4 (algorithm namei)"]
---
**Algorithm `namei`** (path name $\to$ inode):

1. **Starting point:** if the path starts with `/`, the working inode is the **root inode** (`iget` of the process's root); otherwise it is the **current directory** inode.
2. **Loop over the components** (e.g. `a`, `b`, `c` for `/a/b/c`):
   1. Read the next component of the path name.
   2. Check that the working inode is a **directory** and that the process has **search (execute) permission** for it; otherwise return an error.
   3. If the component is `..` at the root of the process, stay at root (and, at the root of a mounted file system, move to the mount point's file system).
   4. **Search the directory** block by block (using `bmap` and the buffer cache) for an entry with the component's name; if not found, return an error (no such file).
   5. **Release** the old working inode (`iput`) and get the inode of the matched entry with `iget` (checking whether it is a mount point and crossing to the root of the mounted file system if so).
   6. Set the working inode to the new inode.
3. When the path name has no more components, **return the (locked) working inode.**

The result is the in-core inode of the last component (or its parent directory for `creat`).

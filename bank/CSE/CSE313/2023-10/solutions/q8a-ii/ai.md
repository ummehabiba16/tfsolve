---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
changes:
  - "2026-09-30 (import): split from the combined (i)-(iii) solution."
---
Removing a file in lfs is handled by simply appending new information to the log rather than erasing anything in place:

1. Look up `lfsfile.txt`'s directory entry (via the parent directory data, itself found via its inode from the imap) to get its inode number.
2. Write a new version of the **parent directory's data** block (in the log) with the entry for `lfsfile.txt` removed.
3. Update the parent directory's **inode** (also newly logged) to reflect its changed data location/size.
4. **Invalidate/free the file's inode**: update the imap so that inode number no longer maps to any valid location (or maps it to a special "deleted" marker), and mark the file's inode and data blocks as *dead* (they still physically exist on disk, but nothing valid references them any longer).

Any subsequent access to `lfsfile.txt` fails simply because the directory lookup for that name no longer finds an entry at all -- there is nothing to invalidate on the data itself; the blocks are just orphaned and become eligible for reclamation by segment cleaning.

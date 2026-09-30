---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
A **hard link** is just another directory entry (a name) that points directly to the same **inode number** as an existing file. Inode numbers, however, are only meaningful *within one specific file system* -- each file system has its own independent inode table starting from inode 0/1. A hard link on file system A therefore cannot reference an inode number that actually lives in file system B's inode table (that number, on B, means something completely different, or nothing at all) -- there is no way to encode "inode 42 *of file system B*" in a plain hard-link directory entry. This is why hard links are restricted to a single file system / partition (cannot cross mount points or devices).

A **symbolic link** solves this because it does not reference an inode number at all -- it is a small special file whose content is simply a text **pathname** string pointing at the target (e.g., `/mnt/otherdisk/file.txt`). Resolving a symlink means performing a brand-new pathname lookup starting from that string, exactly like resolving any other path -- and an ordinary pathname lookup can freely cross mount-point / file-system boundaries. So a symlink can point at a target on an entirely different file system, at the cost of an extra level of indirection (the OS must first read the symlink, then perform a fresh lookup) and a small amount of fragility (a \"dangling\" link if the target is later moved or removed, since there is no reference-count tie between the symlink and the target's inode).

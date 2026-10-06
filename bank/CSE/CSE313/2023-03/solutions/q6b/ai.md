---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Opening /etc/out.txt for redirection creates the file (walk the path, allocate an inode, update the directory); each write then allocates a data block and updates the inode: timeline tables."
sources: ["OSTEP ch. 40 (reading/writing a file, file creation timeline)"]
---
`./test > /etc/out.txt`: the shell forks; in the child it opens `/etc/out.txt` with `O_CREAT|O_WRONLY|O_TRUNC`, `dup2`s it to fd 1 (stdout) and `exec`s `test`. Every `write(1, ...)` of `test` therefore goes to the file. Since there is no cache, every access goes to disk. Assume the file does not exist yet and that `test` writes one block of data.

**1. `open("/etc/out.txt", O_CREAT)`: path lookup and file creation**

| Step | Reads | Writes |
|:--|:--|:--|
| Look up `/`: root inode, then root data | root inode, root data block | |
| Look up `etc`: its inode, then its data (directory) | `etc` inode, `etc` data | |
| `out.txt` not found: allocate an inode | inode bitmap | inode bitmap |
| Initialise the new inode | out.txt inode | out.txt inode |
| Add entry `out.txt` to directory `etc` | | `etc` data |
| Update `etc` inode (size, mtime) | `etc` inode | `etc` inode |

The file is now opened (an entry in the open-file table and in the process's fd table; no disk I/O).

**2. `write()` of the output (one data block)**

| Step | Reads | Writes |
|:--|:--|:--|
| Read the file's inode | out.txt inode | |
| Allocate a data block | data bitmap | data bitmap |
| Write the data | | out.txt data block |
| Update the inode (new size, block pointer, mtime) | | out.txt inode |

Each further `write()` repeats these steps (the allocation only when a new block is needed).

**3. `close()`:** no disk I/O.

So creating the file and writing one block costs about a dozen reads and writes for creation and a few more for the write: creation is expensive in a simple file system, because it must update the bitmap, the new inode, the directory block and the directory inode.

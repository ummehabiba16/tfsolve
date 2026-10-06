---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "creat: namei the path; if the file exists truncate it, else allocate an inode (ialloc) and add a directory entry; allocate a file-table entry and a user file-descriptor; return the descriptor."
sources: ["Bach, ch. 5 (algorithm creat; file table, user file descriptor table)"]
---
**Algorithm `creat`** (`creat(pathname, modes)`):

```text
algorithm creat
input:  file name; permission modes
output: file descriptor
{
    get inode for file name (namei);
    if (file already exists)
    {
        if (not permitted access) { release inode; return error; }
    }
    else    /* file does not exist yet */
    {
        assign free inode from file system (algorithm ialloc);
        create new directory entry in parent directory:
                  include new file name and newly assigned inode number;
    }
    allocate file table entry for inode, initialise count;
    if (file did exist) free all file blocks (algorithm free);   /* truncate */
    unlock(inode);
    return (user file descriptor);
}
```

1. `namei` parses the path name and returns the inode of the file (or of the parent directory if the file does not exist).
2. If the file exists, the kernel checks write permission and **truncates** it to zero length (freeing its blocks); if not, `ialloc` assigns a **new inode** and the kernel adds a **directory entry** (name, inode number) to the parent directory (and writes the new inode to disk).
3. The kernel allocates an entry in the **file table** (count 1, offset 0, access mode) pointing to the in-core inode and sets the lowest free slot of the **user file descriptor table** (in the u area) to point to it; this index is returned.

**File data structures:**

![User file descriptor table, file table and inode table](figures/filetables.png)

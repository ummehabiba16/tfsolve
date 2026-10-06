---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Reference count = active users of the in-core inode, link count = directory entries; iput frees the file only when both are zero; with reference count 0 and link count non-zero the inode just goes to the free list and its data stays on disk."
sources: ["Bach, ch. 4 (algorithm iput)"]
---
**Algorithm `iput`** (release an in-core inode):

```text
algorithm iput
{
    lock inode if not already locked;
    decrement inode reference count;
    if (reference count == 0)
    {
        if (inode link count == 0)
        {
            free disk blocks for file;      (algorithm free)
            set file type to 0;
            free inode;                     (algorithm ifree)
        }
        if (file accessed or inode changed or file changed)
            update disk inode;
        put inode on free list;
    }
    release inode lock;
}
```

- **Reference count:** how many times the in-core inode is currently in use (open file-table entries, current directories, ...).
- **Link count:** how many directory entries (names) point to the file; it is stored in the disk inode.

**Significance of the link count in `iput`.** When the last user releases the inode (reference count 0), the kernel looks at the link count: if it is **0**, nobody can reach the file by any name any more, so the kernel **frees the file's disk blocks and the inode**. If it is non-zero, the file must continue to exist.

**Reference count 0 but link count non-zero:** the file is still named in some directory, so its blocks and the disk inode are **kept**. If the file was accessed or changed, the in-core inode is written back to the disk inode, and then the in-core inode is placed on the **free list of in-core inodes** (it stays cached in the hash queue and can be found again quickly, but its slot may be reused later).

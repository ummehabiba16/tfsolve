---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "iget returns a locked inode or an error: a cached unlocked inode is locked and returned, a locked one is waited for (sleep and retry), an uncached one is read into a free in-core inode (error if the inode table is full)."
sources: ["Bach, ch. 4 (algorithm iget)"]
---
**Algorithm `iget`** allocates (gets) an in-core inode for a given (file system, inode number):

```text
algorithm iget
input:  file system inode number
output: locked inode
{
    while (not done)
    {
        if (inode in inode cache)
        {
            if (inode locked)
                { sleep (event inode becomes unlocked); continue; }   /* retry */
            if (inode a mount point)  { ... find root inode of mounted fs; continue; }
            if (inode on inode free list) remove it from free list;
            increment inode reference count;
            return (inode);                         /* locked */
        }
        /* inode not in cache */
        if (no inodes on free list)  return (error);   /* inode table overflow */
        remove new inode from free list;
        reset inode number and file system;
        remove inode from old hash queue, put on new one;
        read inode from disk (algorithm bread);
        initialise inode (e.g. reference count = 1);
        return (inode);                                /* locked */
    }
}
```

**Justification** by the cases:

1. **Inode in the cache, not locked** (e.g. an inode just released and on the free list): the kernel increments its reference count, removes it from the free list if it was there and returns it **locked**.
2. **Inode in the cache but locked** by another process: the process **sleeps** until it is unlocked, then **restarts the loop** (it must search again, as the inode may have been reassigned): this never returns an unlocked inode.
3. **Inode not in the cache** and a free in-core inode exists: it is taken from the free list, reassigned (inode number, file system, hash queue), **read from the disk inode** and returned **locked**.
4. **Inode not in the cache and the free list is empty:** no in-core inode can be used (all are in use), so `iget` **returns an error** ("inode table overflow").

So the only results are a locked in-core inode or an error.

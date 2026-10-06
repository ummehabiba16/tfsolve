---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "freereg: if other processes still reference the region just unlock it; otherwise release its inode, free its memory pages, page tables and fields, and put the region on the free list."
sources: ["Bach, ch. 6 (algorithm freereg)"]
---
```text
algorithm freereg      /* free an allocated region */
input:  pointer to a (locked) region
output: none
{
    if (region reference count non zero)
    {
        /* some process still using region */
        release region lock;
        if (region has an associated inode) release inode lock;
        return;
    }
    if (region has an associated inode) release inode (algorithm iput);
    free physical memory still associated with region;
    free auxiliary tables associated with region (page tables);
    clear region fields;
    place region on region free list;
    unlock region;
}
```

**Steps.** (1) `freereg` is given a **locked region**. (2) If the region's **reference count is non-zero** (other processes still share it, e.g. a text region used by several processes), nothing is freed: only the locks are released. (3) Otherwise the kernel **releases the inode** of the file from which the region was loaded (text regions), (4) **frees the physical pages** (and swap space) that still belong to the region, (5) frees the **page tables**, (6) **clears the region fields** and (7) puts the region on the **free list** and unlocks it. It is called when a process exits or `exec`s, and from `detachreg`.

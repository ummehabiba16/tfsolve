---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "dupreg allocates a new region, copies the region's attributes, allocates page tables and copies the pages (unless the region is shared); it is used by fork for data and stack regions."
sources: ["Bach, ch. 6 (algorithm dupreg)"]
---
```text
algorithm dupreg
input:  pointer to region table entry
output: pointer to a region that looks identical to the input region
{
    if (region type shared) return (input region pointer); /* caller will increment reference count */
    allocate new region;
    set size of new region to size of input region;
    copy other fields from input region;
    if (region has an associated inode) increment inode reference count;
    allocate auxiliary tables (page tables) for new region;
    allocate physical memory for new region contents;
    "copy" contents of old region to contents of new region;
    return (pointer to allocated region);
}
```

**Steps.** (1) If the region is **shared** (text), return the same region (its reference count is incremented by the caller). (2) Otherwise allocate a **new region table entry** and give it the same size and attributes. (3) If the region came from a file (text), increment the **inode's reference count**. (4) Allocate **page tables** and **physical memory** for the new region. (5) **Copy the contents** of the old pages into the new pages (or share the pages copy-on-write in some systems). (6) Return a pointer to the new region.

**When does the duplication happen?** In the **`fork`** system call: for each region of the parent, the kernel calls `dupreg` (data and stack regions are copied; the text region is shared and just has its reference count incremented) and attaches the result to the child. (It is not done by `exec`, which frees the old regions and builds new ones.)

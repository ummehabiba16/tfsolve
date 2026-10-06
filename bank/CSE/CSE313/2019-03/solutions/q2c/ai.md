---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "True: a fault is cheap if the page is already in memory (minor fault) but costs a disk read, and possibly a write-back, for a major fault; copy-on-write shares pages after fork and copies only on the first write."
sources: ["Tanenbaum MOS 4e, sec. 3.6.2 (page fault handling)", "OSTEP ch. 22"]
---
**True.** A page fault's cost is not fixed; it depends on what the handler has to do:

- **Minor (soft) fault:** the page is already in memory (e.g. in the page cache, or being freed) and only the page table must be updated: a few microseconds.
- **Major (hard) fault:** the page must be read from disk (milliseconds, about $10^5$ times slower).
- If no free frame is available, a victim must be chosen, and if it is **dirty** it has to be written back first: two disk operations instead of one.
- **Zero-fill** faults (first touch of a heap/stack page) need no disk read, only clearing a frame; **copy-on-write** faults need a page copy.
- Other factors: disk queueing, swap-device speed (SSD vs HDD), page replacement policy cost.

**Copy-on-write (COW) for `fork`.** A full copy of the parent's address space at `fork` would be expensive (and wasted if the child calls `exec` at once). Instead:

1. `fork` creates the child's page tables as copies of the parent's, so parent and child **share the same physical frames**, and every shared writable page is marked **read-only** (and flagged as COW) in both.
2. As long as both only *read*, nothing is copied.
3. When either process **writes** to such a page, a protection fault occurs; the kernel allocates a new frame, **copies** the page, maps the copy writable into the faulting process, and the other process keeps the original (made writable again when it is the only user).

So only the pages that are actually modified are copied, and `fork` followed by `exec` copies almost nothing.

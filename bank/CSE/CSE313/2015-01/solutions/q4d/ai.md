---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Regions are locked while manipulated, only data (brk) and stack (automatic) regions can grow, text and shared memory cannot, and a size change may not collide with another region or exceed process limits."
sources: ["Bach, ch. 6 (regions; growreg, locking)"]
---
**Restrictions on manipulating the regions of a process**

1. **Locking:** a region must be **locked** while the kernel changes it (attach, grow, duplicate, free) so that two processes cannot modify the same *shared* region at the same time.
2. **Size changes by type of region:**
   - **Stack** grows automatically on overflow (`growreg`); **data (heap)** grows or shrinks only through the `brk`/`sbrk` system call (used by `malloc`);
   - **text** (read-only, possibly shared by many processes) and **shared memory** regions **cannot change size** (a change would affect all sharers).
3. **Protection:** regions have protection attributes: text is **read-only** (a write is a fault), data/stack read-write, and the kernel enforces them through the page tables; a process cannot touch another process's regions.
4. **Address-space limits:** a region may grow only if it does **not overlap another region** and the new size is **within the process limits** (`ulimit`, the maximum virtual size); `growreg` fails otherwise.
5. **Sharing:** regions are shared only when read-only (text) or explicitly (shared memory); `fork` duplicates writable regions, and each region has a **reference count**, the region being freed only when the last process detaches it.

**Justification.** Shared and read-only regions must be fixed and protected to preserve the integrity of all processes that use them; private regions can grow to suit one process, under the control of the kernel, which prevents processes from interfering with each other.

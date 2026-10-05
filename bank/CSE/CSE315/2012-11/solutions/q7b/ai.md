---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "In the flat model all segment descriptors (code, data, stack) have base 0 and limit 4 GB (FFFFF with G = 1), so segmentation is effectively turned off: the 32-bit offset is the linear address and memory is one linear 4 GB space. Protection and virtual memory are then done with paging. Used by modern OSs (Windows, Linux)."
sources: ["Brey, The Intel Microprocessors, Sec. 2-5 (flat mode memory)", "MHE 80386-updated slides 16-19 (descriptor base, limit, granularity)"]
---
**Flat mode memory system.** The 80386 cannot switch segmentation off, but it can make it transparent:

- All segment descriptors used by a program (code, data, stack) are given **base = 00000000h** and **limit = FFFFFh with G = 1**, i.e. the full **4 GB**.
- Then CS, DS, ES, SS, ... all describe the same 4 GB region starting at 0, and

$$\text{linear address} = 0 + \text{offset} = \text{offset}$$

- The program sees **one linear, unsegmented address space** of 4 GB, addressed by 32-bit offsets (pointers). Segment registers are loaded once by the OS and never changed by programs.

```text
 CS, DS, SS, ES --> descriptors with base 0, limit 4 GB
 0000 0000h  +--------------------------------+
             |  code, data, stack all in one   |
             |  linear 4 GB address space      |
 FFFF FFFFh  +--------------------------------+
```

**Advantages:** simple programming (no segment arithmetic, near 32-bit pointers everywhere), compilers and OSs are portable to other flat-memory CPUs, and no segment-register loads (faster).

**Protection and virtual memory** are provided by **paging** instead (per-page present, read/write, user/supervisor bits). Usually two pairs of flat segments are defined, DPL 0 for the kernel and DPL 3 for user programs. This is how Windows NT/XP and later, and Linux use the x86; in 64-bit mode segmentation is almost entirely flat by design.

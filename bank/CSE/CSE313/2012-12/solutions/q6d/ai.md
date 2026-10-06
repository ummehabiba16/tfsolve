---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Segmentation divides the address space into logical segments of variable size, each with its own address space (segment number + offset); benefits: independent growth, sharing, protection, simpler linking."
sources: ["Tanenbaum MOS 4e, sec. 3.7 (segmentation)"]
---
**Memory segmentation.** The (virtual) address space is divided into several **logical units of variable size called segments** (e.g. code, data, stack, symbol table, each procedure or array), each of which is an independent linear address space from 0 to a maximum. An address is a pair **(segment number, offset)**. A **segment table** gives each segment's base and limit; the hardware adds the offset to the base after checking it against the limit.

**Benefits of using multiple segments**

1. **Independent growth:** each segment can grow or shrink separately (no problem of "tables colliding" in one linear space).
2. **Simpler linking:** procedures compiled separately each start at address 0 of their own segment, so recompiling one does not change the addresses of others.
3. **Sharing:** a segment (e.g. a library) can be shared between processes by being in both segment tables.
4. **Protection:** each segment has its own protection (read-only code, read/write data, execute-only) that matches its logical use; the programmer knows what is in a segment.
5. No *internal* fragmentation (the segment is exactly the size needed).

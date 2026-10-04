---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "(i) IP = 19F2H <= limit 2B1AH: PA = 013B2AH + 19F2H = 01551CH. (ii) IP = A016H > limit 2B1AH: outside the segment, so no physical address; the 80286 raises a general protection fault (exception 13)."
sources: ["MHE 80286 slides (limit checking, general protection fault)", "Brey, The Intel Microprocessors, Sec. 2-3 (protected-mode addressing)"]
---
From Q.5(a): code segment base = 013B2AH, limit = 2B1AH (valid offsets 0000H-2B1AH).

**(i) IP = 19F2H**

19F2H $\le$ 2B1AH, so the offset is inside the segment:

$$PA = 013B2AH + 19F2H = \mathbf{01551CH}$$

**(ii) IP = A016H**

A016H $>$ 2B1AH: the offset is **beyond the segment limit**. The 80286 checks every offset against the limit in protected mode, so this access is **not allowed**. No physical address is produced; the processor generates a **general protection fault (exception 13)** and the operating system handles it.

(Without the limit check, base + offset would be 013B2AH + A016H = 01DB40H, but that location does not belong to this code segment.)

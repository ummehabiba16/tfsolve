---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "CS:IP = 0024:02A0 gives 004E0H; DS:SI = 0040:00E0 gives 004E0H. Both point to the same physical location: different segment:offset pairs can name one address, and the code and data segments overlap."
sources: ["MHE 8086-Memory_Organization slides 7, 12, 18 (address calculation, overlap, redundancy of segment:offset pairs)"]
---
Physical address = segment $\times$ 10H (append 0H) + offset.

**CS:IP = 0024H:02A0H**

$$00240H + 02A0H = \mathbf{004E0H}$$

**DS:SI = 0040H:00E0H**

$$00400H + 00E0H = \mathbf{004E0H}$$

**Comment.** Both pairs give the **same physical address 004E0H**. This shows that:

- a 20-bit physical address can be referred to by many segment:offset pairs (up to $2^{12} = 4096$ of them), because segments start on 16-byte paragraph boundaries but are 64KB long;
- the code segment (starting at 00240H) and the data segment (starting at 00400H) **overlap**. Here the instruction pointer and the data pointer refer to the very same byte, so data written through DS:SI would overwrite the code at CS:IP. Overlapping is allowed, but the programmer must make sure it is intended.

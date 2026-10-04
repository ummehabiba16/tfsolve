---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "CS:IP = 00240H + 02A0H = 004E0H and DS:SI = 00400H + 00E0H = 004E0H: the same physical address, because the code and data segments overlap; the instruction to be fetched and the data byte are the same memory location."
sources: ["MHE 8086-Memory_Organization slides 8-13, 18 (physical address, overlapping segments, many segment:offset pairs per address)"]
---
Physical address = segment $\times$ 10H + offset.

$$CS:IP = 0024H:02A0H \Rightarrow 00240H + 02A0H = \mathbf{004E0H}$$

$$DS:SI = 0040H:00E0H \Rightarrow 00400H + 00E0H = \mathbf{004E0H}$$

**Comment:** two different segment:offset pairs point to the **same physical location**. Segments can start at any paragraph (16-byte boundary) and **overlap**, so one physical address has many logical addresses. Here the code and data segments overlap, and the byte that DS:SI points to is the **next instruction** CS:IP will fetch. Writing data through DS:SI would modify the program (self-modifying code), so in a real program the segments would be placed apart.

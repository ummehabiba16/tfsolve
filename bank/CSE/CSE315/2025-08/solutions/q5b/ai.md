---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "The 80386 has a 32-bit data bus but byte-addressable memory, so memory is split into 4 byte-wide banks (selected by BE0-BE3) to move a whole aligned doubleword in one bus cycle."
sources: ["MHE 80386-updated slides 4, 12 (32-bit data bus, 4 banks)", "MHE 8086-Memory_Organization slides 2-6 (2 banks, BHE/A0)"]
---
- The 80386DX has a **32-bit data bus**, but memory is **byte-addressable**: each address holds 1 byte.
- To transfer 32 bits (4 bytes) in **one bus cycle**, four consecutive bytes must be read or written in parallel. The memory is therefore organized as **4 banks**, each 8 bits wide and connected to one byte lane of the data bus: D0-D7, D8-D15, D16-D23, D24-D31.
- Address lines A31-A2 select the same row in all four banks, and four bank-enable signals ($\overline{BE0}$ to $\overline{BE3}$, replacing $A1$, $A0$) choose which bytes take part. This allows byte, word or doubleword transfers, just as the 8086 uses 2 banks with $\overline{BHE}$ and A0 for its 16-bit bus.
- An aligned doubleword is read in a single cycle. With only one bank it would need 4 cycles.

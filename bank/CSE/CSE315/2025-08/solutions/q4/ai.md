---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "DS = 0014H selects LDT entry 2 at 300010H: shadow register for DS = base 700000H, limit FFFFH, access rights 92H."
sources: ["MHE 80286 slides 43-52 (selector, GDT/LDT, descriptor format)", "MHE 80286 slides 64-71 (program-invisible / shadow registers, LDTR)"]
---
Each 80286 descriptor is 8 bytes. From the lowest address: limit L0-L15 (2 bytes), base B0-B15 (2 bytes), base B16-B23 (1 byte), access rights (1 byte), 0000 (2 bytes).

**Step 1: decode the selectors (index | TI | RPL)**

- DS = 0014H = 0000 0000 0001 0 | 1 | 00: **index 2, TI = 1 (LDT)**, RPL = 00
- LDTR = 0018H = 0000 0000 0001 1 | 0 | 00: index 3, TI = 0 (GDT), RPL = 00

**Step 2: find the LDT (via the GDT)**

The LDTR selector points to a GDT descriptor, which gives the base of the LDT. The GDT descriptors in the snapshot are:

| Address | Bytes | Base | Limit | Access |
|:-:|:-:|:-:|:-:|:-:|
| 200000H | FF FF 00 00 50 D2 00 00 | 500000H | FFFFH | D2H |
| 200008H | FF FF 00 00 40 D2 00 00 | 400000H | FFFFH | D2H |
| 200010H | FF FF 00 00 30 D2 00 00 | 300000H | FFFFH | D2H |

$GDTR + 3\times8 = 200018H$ is not in the snapshot. Counting as the slide does ("3rd descriptor"), the third descriptor shown, at 200010H, gives **LDT base = 300000H**. This is the only GDT descriptor that points to the second snapshot, so we take it as the LDT descriptor.

**Step 3: read the DS descriptor from the LDT**

$$\text{Descriptor address} = LDT\ base + index\times8 = 300000H + 2\times8 = 300010H$$

Bytes at 300010H: FF FF 00 00 70 92 00 00

- Limit = FFFFH
- Base = 70 0000H = **700000H**
- Access rights = 92H = 1 00 1 0 0 1 0: P = 1 (present), DPL = 00, S = 1, E = 0 (data), ED = 0 (expands up), W = 1 (writable), A = 0

**Shadow (cache) register of DS** (loaded once, then used for every DS access):

| Base address (24 bits) | Limit (16 bits) | Access rights (8 bits) |
|:-:|:-:|:-:|
| **700000H** | **FFFFH** | **92H** |

The DS segment therefore covers physical addresses 700000H to 70FFFFH.

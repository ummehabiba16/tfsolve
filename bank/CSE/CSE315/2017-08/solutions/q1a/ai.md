---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Selector 0020h = GDT entry 4 = 0000 EC 00 0028 4672: a present 386 call gate (DPL 3) with destination selector 0028h and offset 00004672h (the 00ABCDEF in the instruction is ignored). 0028h = GDT entry 5: conforming code segment, DPL 3, base 021FFFFFh, limit F000h. Next instruction: 0028:00004672, linear address 021FFFFFh + 4672h = 02204671h."
sources: ["Table B and Table C of the paper (descriptor and call gate formats)", "Intel 80386 Programmer's Reference Manual, Sec. 6.3.4 (call gates)", "MHE 80386-updated slides 16-20 (descriptors)"]
---
**Step 1: the selector in the instruction**

0020h = 0000 0000 0010 0 | 0 | 00: **index 4**, TI = 0 (GDT), RPL = 0. So GDT entry 4 is read.

**Step 2: GDT entry 4 as a call gate (Table C)**

Entry 4 = 0000 EC00 0028 4672h.

| Bits | Field | Value |
|:--|:--|:--|
| 63-48 | destination offset 31-16 | 0000h |
| 47 | P | 1 (present) |
| 46-45 | DPL | 11 = 3 |
| 44-40 | type | 01100 (386 call gate) |
| 39-37, 36-32 | 000, word count | 0 parameters |
| 31-16 | **destination selector** | **0028h** |
| 15-0 | destination offset 15-0 | 4672h |

(Byte 5 = ECh = 1 11 01100.) Because a gate is used, the offset in the instruction (00ABCDEFh) is **ignored**; the entry point is offset **00004672h** in the segment selected by **0028h**.

**Step 3: the destination selector 0028h = GDT entry 5**

0028h: index 5, TI = 0, RPL = 0. Entry 5 = 0230 FC1F FFFF F000h (Table B):

| Bits | Field | Value |
|:--|:--|:--|
| 63-56 | base 31-24 | 02h |
| 55-52 | G, D, L, AV | 0, 0, 1, 1 (G = 0: limit in bytes) |
| 51-48 | limit 19-16 | 0 |
| 47-40 | access byte FCh | P = 1, DPL = 3, S = 1, E = 1 (**code**), C = 1 (**conforming**), R = 0, A = 0 |
| 39-16 | base 23-0 | 1FFFFFh |
| 15-0 | limit 15-0 | F000h |

So the target is a code segment with **base 021FFFFFh** and **limit 0F000h**. The offset 4672h is within the limit.

**Result**

$$\text{next instruction} = \mathbf{0028:00004672}, \qquad \text{linear address} = 021FFFFFh + 4672h = \mathbf{02204671h}$$

(Privilege checks: the gate has DPL 3, so any caller may use it; the target is conforming with DPL 3, which requires DPL $\le$ CPL, so the call is valid for a caller at CPL 3, and the CPL does not change because the segment is conforming.)

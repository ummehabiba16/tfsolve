---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "CS = 0017H (code, base 123456H), DS = 0085H (data, base 951596H), SS = 0046H (stack, base 425478H). Code access is allowed (C = 0, DPL ignored). The data segment has not been accessed (A = 0)."
sources: ["MHE 80286 slides 43-44 (selector: index, TI, RPL)", "MHE 80286 slides 56-63 (access right byte P, DPL, S, E, ED/C, R/W, A)", "MHE 80286 slide 52 (80286 descriptor)"]
---
Each 80286 descriptor value is written from the most significant byte: `00 00 | access rights | base B23-B16 | base B15-B0` (limit bytes not given).

**Decoding the three descriptors (access right byte = P DPL S E ED/C R/W A):**

| Selector | Descriptor | Access byte (bin) | P | DPL | S | E | ED/C | R/W | A | Base |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0046 | 00 00 B7 42 54 78 | 1 01 1 0 1 1 1 | 1 | 01 | 1 | 0 | ED = 1 | W = 1 | 1 | 425478H |
| 0017 | 00 00 9B 12 34 56 | 1 00 1 1 0 1 1 | 1 | 00 | 1 | 1 | C = 0 | R = 1 | 1 | 123456H |
| 0085 | 00 00 D2 95 15 96 | 1 10 1 0 0 1 0 | 1 | 10 | 1 | 0 | ED = 0 | W = 1 | 0 | 951596H |

- B7H: E = 0 (data/stack) and ED = 1, so the segment **expands downward**, which makes it a **stack** segment.
- 9BH: E = 1, so it is executable: a **code** segment.
- D2H: E = 0 and ED = 0, so it expands upward: a **data** segment.

**Selectors (index | TI | RPL):**

- 0046H = 0000 0000 0100 0 | 1 | 10: index 8, TI = 1 (LDT), RPL = 10
- 0017H = 0000 0000 0001 0 | 1 | 11: index 2, TI = 1 (LDT), RPL = 11
- 0085H = 0000 0000 1000 0 | 1 | 01: index 16, TI = 1 (LDT), RPL = 01

**(i)** **CS = 0017H**, **DS = 0085H**, **SS = 0046H**.

**(ii)** Code segment: P = 1, so it is present and mapped into physical memory. The requester's RPL = 11 is the lowest privilege, and DPL = 00 is the highest. But bit 2 of a code segment is the conforming bit, and here **C = 0, which means "ignore DPL"** (slide 61). The privilege check is therefore not enforced, and R = 1 makes the segment readable as well as executable. **So the code segment's physical address (base 123456H) is allowed to be accessed.**

*If the C bit were read the usual Intel way (C = 0 means non-conforming, so the access must obey DPL), then RPL 11 > DPL 00 would be a privilege violation and the access would be refused. The answer above follows the course slide.*

**(iii)** The accessed bit A (bit 0) is 1 for the code (9BH) and stack (B7H) segments but **0 for the data segment (D2H)**. So the **data segment** (DS = 0085H, physical base **951596H**) has not been accessed yet.

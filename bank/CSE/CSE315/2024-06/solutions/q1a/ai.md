---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "(i) 93.36% not reachable with 8086-style segment x 16 + offset; (ii) optimal paragraph = 2^8 = 256 words; (iii) 6 x 56 = 336 bits; (iv) 2^18 segments x 2^20 words = 2^38 words (512GB)."
sources: ["MHE 8086-Memory_Organization slides 9-12, 18 (segment:offset, paragraph)", "MHE 80286 slides 3, 43-44, 64-66 (selector bits, 1GB virtual memory, descriptor cache)"]
---
**Given and assumptions.** Address bus 28 bits and word-addressable memory, so there are $2^{28}$ words (1 word = 2 B). Data bus 20 bits, so this is a 20-bit processor: **offset registers and the 6 segment registers are taken as 20 bits** (their size is not given). Longest instruction 10 bytes. In virtual memory mode 3 bits of a segment register are access-control bits, like TI + RPL of the 80286 selector.

**(i) Memory not accessible with the segment:offset pair**

Using the 8086 rule (append 0H to the segment, i.e. a 16-word paragraph):

$$PA_{max} = FFFFF0H + FFFFFH = 10FFFEFH$$

So only $10FFFF0H = 17{,}825{,}776$ of the $2^{28} = 268{,}435{,}456$ locations are reachable:

$$\text{Not accessible} = 1-\frac{17{,}825{,}776}{268{,}435{,}456} = \mathbf{93.36\%}$$

**(ii) Optimal paragraph size**

A 20-bit segment must reach the whole 28-bit space, so the segment value must be shifted left by $28-20 = 8$ bits:

$$\text{Paragraph} = 2^{8} = \mathbf{256\text{ words}}\ (512\text{ B})$$

Check: $(2^{20}-1)\cdot p + (2^{20}-1)\ge 2^{28}-1$ gives $p\ge 255.0002$, so the smallest power of two is $p=256$. A larger paragraph only wastes the finer placement of segments.

**(iii) Total size of the shadow registers**

Each shadow (descriptor-cache) register holds base + limit + access rights, as in the 80286 (slides 64-66):

- Base = full physical address = **28 bits**
- Limit = maximum offset = **20 bits**
- Access rights = **8 bits** (access-rights byte, as in the 80286)

$$\text{One} = 28+20+8 = 56\text{ bits},\qquad 6\times56 = \mathbf{336\text{ bits}} = 42\text{ B}$$

*If only the 3 access-control bits are kept instead of a full access byte: $6\times(28+20+3) = 306$ bits.*

**(iv) Size of the virtual memory**

Selector = 20 bits, of which 3 are access-control bits. That leaves 17 index bits, and TI selects the GDT or the LDT:

$$\text{Segments} = 2^{17}\times2 = 2^{18}$$

Each segment is up to $2^{20}$ words (20-bit offset):

$$\text{Virtual memory} = 2^{18}\times2^{20} = 2^{38}\text{ words} = 2^{39}\text{ B} = \mathbf{512\,GB}$$

*Check against the 80286: $(2^{13}\times2)\times2^{16} = 2^{30}$ = 1GB.*

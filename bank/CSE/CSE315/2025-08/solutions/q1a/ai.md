---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "X = 6 bytes, the size of the 8086 pre-fetch queue; the BIU would fetch past the end of the 64KB segment, and IP wraps to 0000H."
sources: ["MHE 8086-Architecture slides 3, 10 (6-byte pre-fetch, BIU/EU)", "MHE 8086-Memory_Organization slides 7-12 (segment:offset, 64KB segments)"]
---
**X = 6 bytes.**

**Why.** In the 8086 the work is split between two units (8086-Architecture, slide 10):

- the **BIU** does the fetching: it keeps reading the next bytes of code from CS:IP into a **6-byte pre-fetch queue** while the EU is busy;
- the **EU** decodes and executes the instructions taken from that queue.

So at any moment the BIU tries to have the **next 6 bytes** after the current instruction already in the queue.

A code segment is at most 64KB, and the offset (IP) is only 16 bits, offsets 0000H to FFFFH. The BIU forms the fetch address as $CS\times 10H + IP$, and IP simply wraps around after FFFFH:

$$FFFFH + 1 = 0000H \text{ (16-bit IP)}$$

Suppose code is written in the last 6 bytes, offsets FFFAH to FFFFH. While the instruction there executes, the BIU pre-fetches the "next" bytes. Those are not the bytes at physical address $CS\times10H + 10000H$, which lie outside the segment. They are the bytes at CS:0000H, CS:0001H, ..., the **beginning** of the same code segment. The queue is filled with wrong bytes, and an instruction that starts near FFFFH and is several bytes long would also straddle the segment end. In both cases the EU would decode garbage.

Hence the restriction: **the last X = 6 bytes** of the code segment (the size of the pre-fetch queue, which also covers the longest 8086 instruction of 6 bytes) must not hold code. Keep them as data or unused, or end the code with a jump before them.

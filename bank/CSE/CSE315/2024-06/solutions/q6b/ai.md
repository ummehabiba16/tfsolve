---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "The queue should hold at least the longest instruction, rounded to whole bus transfers (8086: 6 bytes = 3 words; 80386: 15/16-byte queue)."
sources: ["MHE 8086-Architecture slides 3, 10 (6-byte queue)", "MHE 80386-updated slide 7 (15B instruction code queue)"]
---
Choose the queue so that a **complete instruction of maximum length** can always be waiting, and make it a **whole number of bus transfers**:

$$\text{Queue size}\ \ge\ \text{longest instruction length},\ \text{rounded up to a multiple of the data bus width}$$

**Justification:**

- If the queue were smaller than the longest instruction, the decoder would sometimes stall in the middle of an instruction waiting for the bus, which defeats the purpose of pre-fetching.
- Making it much larger gives little benefit, because every jump, call or interrupt **flushes** the queue, so far-ahead bytes are often wasted bus cycles.
- The BIU fills the queue one bus width at a time, so the size should match whole transfers.

**Examples:** 8086, longest instruction 6 bytes on a 16-bit bus: **6-byte queue** (3 words). 80386, longest instruction 15 bytes: a 15/16-byte instruction code queue.

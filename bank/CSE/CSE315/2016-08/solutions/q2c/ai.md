---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Type 4 uses 4 x 4 = 00010H-00013H: IP at 00010H-00011H, CS at 00012H-00013H."
sources: ["MHE INTR slides 14-15, 20 (vector table: 4 bytes per type, type 4 overflow at 00010H/00012H)"]
---
Each vector takes 4 bytes, starting at $4 \times$ type:

$$4 \times 4 = 16 = 10H$$

| Address | Contents |
|:-:|:--|
| 00010H-00011H | **IP** (offset) of the type 4 ISR (low word) |
| 00012H-00013H | **CS** (segment) of the type 4 ISR (high word) |

So the type 4 (overflow) interrupt uses locations **00010H to 00013H**.

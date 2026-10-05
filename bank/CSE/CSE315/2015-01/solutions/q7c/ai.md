---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Type 2 (NMI) vector at 4 x 2 = 00008H-0000BH: IP at 00008H-00009H, CS at 0000AH-0000BH."
sources: ["MHE INTR slides 14-15, 18 (vector table; type 2 NMI: CS from 0000AH, IP from 00008H)"]
---
Each vector is 4 bytes at $4 \times$ type: $4 \times 2 = 8 = 08H$.

| Address | Contents |
|:-:|:--|
| 00008H-00009H | **IP** of the type 2 (NMI) service procedure |
| 0000AH-0000BH | **CS** of the type 2 service procedure |

So the type 2 interrupt uses **00008H to 0000BH**.

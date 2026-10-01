---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Physical address = (segment << 8) + offset: append 00H (8 zero bits) to the 20-bit segment and add the 20-bit offset in a 28-bit adder (no multiplier)."
sources: ["MHE 8086-Memory_Organization slides 10-12 (append 0H, then add offset)"]
---
With the optimal paragraph of $2^{8}$ words from 1(a)(ii), the calculation is the 8086 method ("append 0H, then add"), with **8 zero bits (00H) appended instead of 4**:

1. Take the 20-bit segment value and **append 00H** to its right, i.e. shift left by 8 bits. This is pure wiring (the low 8 lines are grounded), so no multiplier and no shifter is needed.
2. **Add** the 20-bit offset (zero-extended) using a **28-bit adder** in the address unit.
3. The 28-bit sum is the physical (word) address placed on A0-A27. Any carry out of bit 27 is ignored, so the address wraps around.

```text
  segment (20 bits)  S19 ........ S0  0000 0000     <- appended 00H
+ offset  (20 bits)  0000 0000  O19 ........ O0
  -----------------------------------------------
  physical (28 bits) P27 ......................P0
```

**Example:** segment = 12345H, offset = 00ABCH:

$$1234500H + 0000ABCH = 1234FBCH$$

This is efficient: one 28-bit addition per access, every location can be reached, and segments can start on any 256-word boundary.

---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "UBRR = fosc/(16 x 4800) - 1. The clock is not given; with the course default 1 MHz: 12.02 -> 12, so UBRRH = 0x00, UBRRL = 0x0C (4808 bps, +0.16%). (With 8 MHz: 103 -> UBRRH = 0x00, UBRRL = 0x67.)"
sources: ["EHP Serial Communication slides 25-26 (UBRR formula and example)"]
---
In normal (asynchronous, U2X = 0) mode:

$$UBRR = \frac{f_{osc}}{16 \times \text{baud}} - 1$$

The clock frequency is not given. **Assumption: $f_{osc}$ = 1 MHz** (the default internal clock used in the course):

$$UBRR = \frac{10^6}{16 \times 4800} - 1 = 12.02 \approx 12 = 0x000C$$

$$\mathbf{UBRRH = 0x00, \quad UBRRL = 0x0C}$$

Actual rate $= 10^6/(16 \times 13) = 4808$ bps (+0.16% error).

*For other clocks:* 8 MHz gives $UBRR = 103.2 \approx 103$: UBRRH = 0x00, UBRRL = 0x67; 4 MHz gives 51: UBRRL = 0x33. UBRRH is written before UBRRL (with URSEL = 0).

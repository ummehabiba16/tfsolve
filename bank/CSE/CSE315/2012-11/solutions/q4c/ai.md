---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Double speed: UBRR = 2 MHz / (8 x 9600) - 1 = 25.04 -> 25: UBRRH = 0x00, UBRRL = 0x19 (25), UCSRA = 0x02 (U2X = 1), UCSRC bit URSEL = 1 with UMSEL = 0 (asynchronous). Actual 9615 bps (+0.16%)."
sources: ["EHP Serial Communication slides 25-26, 52-54 (UBRR formula, double speed mode)"]
---
In asynchronous **double-speed** mode (U2X = 1) the divisor is 8:

$$UBRR = \frac{f_{osc}}{8 \times \text{baud}} - 1 = \frac{2 \times 10^6}{8 \times 9600} - 1 = 25.04 \approx 25$$

Actual baud rate $= 2 \times 10^6/(8 \times 26) = 9615$ bps, error +0.16%.

| Register | Value | Purpose |
|:--|:--|:--|
| UCSRA | 0b00000010 = 0x02 | **U2X = 1**: double speed |
| UCSRC | URSEL = 1, **UMSEL = 0** | asynchronous mode (with the chosen frame, e.g. 0x86 for 8N1) |
| UBRRH | 0x00 | (written with URSEL = 0) |
| UBRRL | 0x19 (25) | baud rate 9600 bps |

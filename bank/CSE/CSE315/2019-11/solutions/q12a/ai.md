---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "U2X = 1, UBRR = 0x31 = 49: baud = 10^6 / (8 x 50) = 2500 bps, so 2500 x 60 = 150,000 bits per minute on the line (13-bit frames: 1 start + 9 data + odd parity + 2 stop, so about 11,538 characters = 103,846 data bits)."
sources: ["EHP Serial Communication slides 25-31, 52-53 (UBRR formula, double speed, UCSRA/B/C)"]
---
**Decode the configuration**

| Register | Value | Meaning |
|:--|:--|:--|
| UCSRA | 0b00000010 | U2X = 1: **double speed** |
| UCSRB | 0b00011100 | RXEN = 1, TXEN = 1, UCSZ2 = 1 |
| UCSRC | 0b10111110 | URSEL = 1, async, UPM1:0 = 11 (**odd parity**), USBS = 1 (**2 stop bits**), UCSZ1:0 = 11 |
| UCSZ2:0 | 111 | **9 data bits** |
| UBRR | 0x0031 = 49 | |

**Baud rate** (double speed: divisor 8)

$$\text{baud} = \frac{f_{osc}}{8\,(UBRR + 1)} = \frac{10^6}{8 \times 50} = 2500\ \text{bps}$$

**Bits in 1 minute**

$$2500 \times 60 = \mathbf{150\,000\ bits}$$

This is the number of bits on the line. Each frame is 1 start + 9 data + 1 parity + 2 stop = 13 bits, so this is $150000 / 13 \approx 11538$ characters, i.e. about $11538 \times 9 = 103\,846$ **data** bits per minute.

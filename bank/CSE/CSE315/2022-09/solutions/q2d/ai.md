---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "The chain is one 32-bit ring M -> S1 -> S2 -> S3 -> M, MSB first. After 4 pulses: M = 01011100, S1 = 10100101, S2 = 11111010, S3 = 11000000. After 16 pulses: M = 00001111, S1 = 11001100, S2 = 01010101, S3 = 10101010."
sources: ["EHP Serial Communication slides 83-85 (byte exchange per clock pulse, MSB first)"]
---
**How the chain works**

All SS' are grounded, so every slave shifts on every SCK pulse. The data path is a single loop

$$M_{MOSI} \to S1 \to S2 \to S3 \to M_{MISO}$$

so the four registers act as **one 32-bit circular shift register**. With **MSB first** (as in the slide example), on every pulse each register shifts **left by one**: its MSB goes out, and the bit from the device before it in the loop enters at the LSB.

- S1 receives M's MSB, S2 receives S1's MSB, S3 receives S2's MSB, M receives S3's MSB.

**Pulse by pulse**

| Pulse | M | S1 | S2 | S3 |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 01010101 | 10101010 | 00001111 | 11001100 |
| 1 | 10101011 | 01010100 | 00011111 | 10011000 |
| 2 | 01010111 | 10101001 | 00111110 | 00110000 |
| 3 | 10101110 | 01010010 | 01111101 | 01100000 |
| 4 | 01011100 | 10100101 | 11111010 | 11000000 |

**i. After 4 clock pulses**

M = **01011100**, S1 = **10100101**, S2 = **11111010**, S3 = **11000000**

(each register = its own low nibble followed by the high nibble of the device before it).

**ii. After 16 clock pulses**

Every 8 pulses each byte moves one device along the loop. After 8 pulses: M = 11001100 (S3's), S1 = 01010101 (M's), S2 = 10101010 (S1's), S3 = 00001111 (S2's). After 16 pulses each byte has moved two places:

| Device | After 16 pulses | Original owner |
|:-:|:-:|:-:|
| M | **00001111** | S2 |
| S1 | **11001100** | S3 |
| S2 | **01010101** | M |
| S3 | **10101010** | S1 |

*Note:* the wiring is read from the figure. The tables were checked by simulating the 32-bit ring with a short script.

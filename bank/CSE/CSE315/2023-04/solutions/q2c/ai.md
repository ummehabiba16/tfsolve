---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "The chain is one 32-bit ring M -> S3 -> S2 -> S1 -> M, LSB first. After 4 pulses: M = 11001010, S1 = 01011100, S2 = 11110101, S3 = 10100000. After 16 pulses: M = 01010101, S1 = 00001111, S2 = 10101010, S3 = 11001100."
sources: ["EHP Serial Communication slides 83-85 (byte exchange per clock pulse)", "EHP Serial Communication slide 93 (DORD = 1: LSB first)"]
---
**How the chain works**

All SS' inputs are grounded, so all three slaves are selected and all shift on every SCK pulse. The data lines form a single loop:

$$M_{MOSI} \to S3 \to S2 \to S1 \to M_{MISO}$$

so the four 8-bit shift registers act like **one 32-bit circular shift register**.

With **LSB first**, on every pulse each device shifts its register **right by one**: its LSB goes out, and the bit coming from the device before it in the loop enters at the MSB.

- S3 receives M's LSB, S2 receives S3's LSB, S1 receives S2's LSB, M receives S1's LSB.

**Pulse by pulse (first 4 pulses)**

| Pulse | M | S1 | S2 | S3 |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 10101010 | 11001100 | 01010101 | 00001111 |
| 1 | 01010101 | 11100110 | 10101010 | 00000111 |
| 2 | 00101010 | 01110011 | 11010101 | 10000011 |
| 3 | 10010101 | 10111001 | 11101010 | 01000001 |
| 4 | 11001010 | 01011100 | 11110101 | 10100000 |

**i. After 4 clock pulses**

M = **11001010**, S1 = **01011100**, S2 = **11110101**, S3 = **10100000**

(each register = low 4 bits of the previous device's byte in its upper half, its own upper 4 bits in its lower half).

**ii. After 16 clock pulses**

After every 8 pulses each device holds the byte of the device just before it in the loop. After 8 pulses: M = 11001100 (S1's), S1 = 01010101 (S2's), S2 = 00001111 (S3's), S3 = 10101010 (M's). After 8 more:

| Device | After 16 pulses | Original owner |
|:-:|:-:|:-:|
| M | **01010101** | S2 |
| S1 | **00001111** | S3 |
| S2 | **10101010** | M |
| S3 | **11001100** | S1 |

*Note:* the wiring was read from the figure (M's MOSI to S3, S3's MISO to S2's MOSI, S2's MISO to S1's MOSI, S1's MISO to M's MISO). The tables were checked by simulating the 32-bit ring with a short script; after 32 pulses every register is back to its original value.

---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "LSB first: each pulse shifts both registers right and moves the other side's LSB into the MSB. After 8 pulses Master = 11110000 and Slave = 10101010 (bytes exchanged)."
sources: ["EHP Serial Communication slides 83-85, 93 (SPI byte exchange per clock pulse, DORD)"]
---
With **LSB first (DORD = 1)**, on each clock pulse the Master shifts out its LSB on MOSI and the Slave shifts out its LSB on MISO. Each register shifts right by one, and the bit received from the other side enters at the MSB.

| Pulse | Master shift register | Slave shift register |
|:-:|:-:|:-:|
| 0 | 10101010 | 11110000 |
| 1 | 01010101 | 01111000 |
| 2 | 00101010 | 10111100 |
| 3 | 00010101 | 01011110 |
| 4 | 00001010 | 10101111 |
| 5 | 10000101 | 01010111 |
| 6 | 11000010 | 10101011 |
| 7 | 11100001 | 01010101 |
| 8 | **11110000** | **10101010** |

After 8 pulses the two bytes have been **exchanged**: the Master holds the Slave's 11110000 and the Slave holds the Master's 10101010 (full-duplex). This is the LSB-first version of the slide example, which assumes MSB first.

---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Daisy-chain the four slaves: ATmega32 MOSI -> A, A MISO -> B MOSI, B -> C, C -> D; SCK and one SS' line shared by all. Only 3 ATmega32 pins (MOSI PB5, SCK PB7, SS PB4) are used; the master shifts 4 bytes (D's first) per update. (With independent slaves, a 2-to-4 decoder on two pins for the SS' lines needs 4 pins.)"
sources: ["EHP Serial Communication slides 79-84, 108 (SPI pins, multiple slaves with separate SS)", "2023-04 Q2(c) of this course (SPI daisy chain)"]
---
Since data only goes **from** the ATmega32 **to** the devices, the fewest master pins are used by a **daisy chain**: the slaves' shift registers are connected in series, and all share SCK and one slave-select line.

```text
 ATmega32        device A        device B        device C        device D
 MOSI (PB5) --> MOSI  MISO --> MOSI  MISO --> MOSI  MISO --> MOSI  MISO (open)
 SCK  (PB7) --> SCK  ------->  SCK  ------->  SCK  ------->  SCK
 SS   (PB4) --> SS'  ------->  SS'  ------->  SS'  ------->  SS'
                 (SCK and SS' are common lines to all four devices)
```

**Connections**

- ATmega32 **MOSI (PB5)** $\to$ MOSI of A; MISO of A $\to$ MOSI of B; MISO of B $\to$ MOSI of C; MISO of C $\to$ MOSI of D. (D's MISO is left open: nothing is read back.)
- ATmega32 **SCK (PB7)** $\to$ SCK of A, B, C, D.
- ATmega32 **SS (PB4, set as output)** $\to$ SS' of A, B, C, D.

**Pins used: 3** (MOSI, SCK, SS). MISO (PB6) is not needed because nothing is received.

**Sending:** pull SS' low, send **4 bytes** (the byte for D first, then C, B, A); after 32 clocks each byte has shifted into its device. Then raise SS' so all devices latch their data at once.

*Note:* this assumes the devices support daisy-chaining (shift data through MISO). If they do not, use the standard bus: MOSI and SCK shared, with each device's SS' driven by a **2-to-4 decoder** controlled by 2 port pins, which needs **4 pins** (instead of 6 with one SS pin per device).

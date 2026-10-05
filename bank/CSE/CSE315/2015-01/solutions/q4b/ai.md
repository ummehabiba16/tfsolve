---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Parallel sends several bits at once on several wires; serial sends one bit at a time on one line. Parallel: fast over short distances and simple timing, but many wires/pins, costly, skew and crosstalk limit distance. Serial: few wires/pins, cheap, long distances, easier synchronization, but slower per clock and needs framing/conversion hardware (USART/SPI)."
sources: ["EHP Serial Communication slides 2-8 (serial vs parallel, why serial communication, synchronous/asynchronous)"]
---
**Difference**

- **Parallel communication:** several bits (usually 8, 16 or more) are sent **simultaneously**, each on its own wire, plus control lines. Examples: printer port, internal buses, old hard disks (PATA).
- **Serial communication:** data is sent **one bit at a time** over a single line (plus ground, maybe a clock), and the receiver reassembles the bytes. Examples: UART/RS-232, SPI, I2C, USB, Bluetooth.

**Parallel**

| Advantages | Disadvantages |
|:--|:--|
| More bits per clock: high throughput over short distances | Many wires and pins: costly, bulky cables and connectors |
| Simple: no serialization, framing or clock recovery | Skew between lines and crosstalk: unreliable over long distances |
| | Uses many microcontroller I/O pins |

**Serial**

| Advantages | Disadvantages |
|:--|:--|
| Few wires and pins: cheap, thin cables | One bit per clock: slower at the same clock rate |
| Works over long distances (no inter-bit skew; can use line drivers, modems, differential signalling) | Needs shift registers, framing (start/stop/parity) and agreed baud rate or a clock line |
| Easier to synchronize; can reach very high bit rates | Extra overhead bits (start/stop) reduce useful data rate |

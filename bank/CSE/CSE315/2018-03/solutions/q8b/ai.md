---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Serial: over long distances parallel lines suffer from skew (bits arriving at different times), crosstalk between wires and the cost/weight of many wires and drivers; a serial link needs one or two signal lines, can use line drivers/modems/differential signalling, and has no inter-bit skew, so it is preferred."
sources: ["EHP Serial Communication slides 3-4 (serial vs parallel; serial for longer distances, fewer wires, easier synchronization, lower cost)"]
---
**Serial transfer is preferred for long-range communication.** Reasons:

1. **Number of wires and cost.** Parallel needs one wire per bit (8, 16, 32) plus control and ground lines. Over a long distance, many conductors, connectors and line drivers are expensive and heavy. Serial needs one data line per direction (plus ground), so cables are thin and cheap and can use existing channels (telephone line, radio, fibre).
2. **Skew.** In a long parallel cable the wires have slightly different lengths and electrical properties, so the bits of one word arrive at slightly **different times**. As the distance or speed grows, bits of consecutive words overlap and data is corrupted. A serial link sends bits one after another on one line, so there is no skew between bits.
3. **Crosstalk and noise.** Many parallel wires next to each other induce noise in each other (crosstalk), worse for long cables. A serial line can be shielded or use **differential signalling** (RS-485, USB, Ethernet) and modems, which tolerate noise over long distances.
4. **Synchronization.** Only one signal must be timed; asynchronous serial (start/stop bits) or encoded clocks allow reliable timing without a separate clock wire.

Parallel transfer is faster only over very short distances (inside a computer, on a circuit board); for long range, serial is better in cost and reliability.

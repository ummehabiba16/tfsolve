---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Serial: fewer wires/pins and lower cost, works over longer distances (no skew/crosstalk between many lines), easier synchronization (and allows very high bit rates). Parallel: several bits per clock gives higher throughput at a given clock rate, and simpler hardware/timing for short on-board links (no serialization)."
sources: ["EHP Serial Communication slides 3-4 (serial vs parallel, why serial communication)", "Mazidi, AVR Microcontroller and Embedded Systems, Ch. 11 (serial basics)"]
---
**Motivations for serial communication**

1. **Fewer wires and I/O pins, lower cost.** One data line per direction (plus ground, maybe a clock) instead of 8, 16 or 32. Cables, connectors and microcontroller pins are cheaper and smaller.
2. **Longer distances.** With many parallel wires, bits arrive at slightly different times (**skew**) and wires interfere with each other (**crosstalk**). These problems grow with cable length. A serial link avoids them, so it works over much longer distances (RS-232, RS-485, USB, Ethernet).
3. **Easier to synchronize and faster per line.** Only one signal has to be timed, so a serial line can be clocked at very high rates (often faster overall than a parallel bus, e.g. SATA replacing PATA, PCIe replacing PCI).

**Motivations for parallel communication**

1. **Higher throughput at the same clock rate.** $n$ bits move in one clock period instead of $n$ periods. This suits short, high-bandwidth connections such as the CPU-memory bus or a printer port.
2. **Simple hardware and timing for short distances.** No shift registers, framing (start/stop bits) or clock recovery are needed: the data is used directly as a word. Over a few centimetres on a circuit board, skew and crosstalk are not a problem.

---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "A bus is a shared set of parallel lines (address, data, control) connecting CPU, memory and I/O. Since many outputs share each line, only one device may drive it at a time; tri-state buffers let every other device go to the high-impedance (disconnected) state, preventing contention and allowing bidirectional buses."
sources: ["MHE Intro slides (BUS: address, data and control bus)", "Brey, The Intel Microprocessors, Sec. 1-3 and 9-1 (buses, three-state buffers, buffered systems)"]
---
**Computer bus.** A bus is a **set of parallel lines (wires) shared** by several components (CPU, memory, I/O) to carry information between them. A microprocessor system has three buses:

- **Address bus** (unidirectional, from the CPU): selects the memory location or I/O port.
- **Data bus** (bidirectional): carries the data being read or written.
- **Control bus**: timing and command signals such as $\overline{RD}$, $\overline{WR}$, M/$\overline{IO}$, ALE, READY, INTR.

**Why tri-state buffers are needed**

- Many devices have outputs connected to the **same** data-bus line, but only **one** may drive the line at any moment. If two ordinary (totem-pole) outputs are connected and one drives 1 while the other drives 0, there is a **bus conflict**: a short circuit from Vcc to ground through the two outputs, large current, possible damage, and an undefined logic level.
- A **tri-state buffer** has three output states: **0, 1 and high impedance (Z)**. When its enable input is inactive, the output is effectively **disconnected** from the line.

```text
          enable (from address decoder / RD')
              |
  device ---|>----- bus line      enable = 1: output = input (0 or 1)
  output                          enable = 0: output = Z (floating, disconnected)
```

- The address decoder and control signals enable **only the selected device's** buffer; all others stay in Z. Many devices can share one bus without interfering.
- Tri-state buffers also make **bidirectional** data buses possible (e.g. 74LS245 transceiver: direction set by DT/$\overline{R}$, enabled by $\overline{DEN}$), and allow the CPU to **release the bus** (float its pins) for DMA during HOLD/HLDA.
- They also provide extra **drive current** when many chips load the bus (buffered system).

---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Serial: longer distances with fewer wires, easier synchronisation, fewer I/O pins, lower cost."
sources: ["EHP Serial Communication slides 3-4 (why serial communication)"]
---
Benefits of serial communication over parallel:

- **Longer distances:** only a few wires or cables are needed, and there is no skew between many parallel lines.
- **Easier to synchronise:** one bit at a time, with no need to keep many lines aligned.
- **Fewer I/O pins** on the microcontroller (UART needs only TxD and RxD).
- **Lower cost:** fewer wires, smaller connectors and simpler boards.

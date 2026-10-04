---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Same EU and instruction set; the 8088 has an 8-bit external data bus (AD7-AD0, A15-A8 address only), a 4-byte queue (refilled when 1 byte is free), IO/M' instead of M/IO', SS0' instead of BHE'/S7, and one linear memory bank, so it is slower for 16-bit data."
sources: ["MHE 8086-Architecture slides (8086 features: 16-bit data bus, 6-byte queue, two banks)", "Brey, The Intel Microprocessors, Sec. 9-1 (8086/8088 pin-outs and differences)", "Hall, Microprocessors and Interfacing, Ch. 7"]
---
Both are 16-bit processors with the **same EU, registers and instruction set** and a 20-bit address bus (1 MB). They differ in the bus interface:

| Feature | 8086 | 8088 |
|:--|:--|:--|
| External data bus | **16-bit** (AD15-AD0) | **8-bit** (AD7-AD0) |
| Upper 8 address pins | AD15-AD8 multiplexed address/data | A15-A8 address only (no demultiplexing needed) |
| Instruction queue | **6 bytes**, refilled when 2 bytes are free | **4 bytes**, refilled when 1 byte is free |
| Memory organisation | Two 512 KB banks (even/odd), selected by A0 and $\overline{BHE}$ | One 1 MB linear (byte-wide) memory |
| Pin 34 | $\overline{BHE}$/S7 (bus high enable) | $\overline{SS0}$ (status, min mode) |
| Pin 28 | M/$\overline{IO}$ (1 = memory) | IO/$\overline{M}$ (1 = I/O), inverted for 8085 compatibility |
| 16-bit transfer | One bus cycle (if word-aligned) | Always two bus cycles |
| Speed / cost | Faster for 16-bit data | Slower, but cheaper 8-bit memory and peripherals (used in the IBM PC) |

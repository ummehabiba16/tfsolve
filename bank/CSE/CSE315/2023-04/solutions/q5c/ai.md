---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Mode 1 strobed output (e.g. printer interface). Inputs: WR' (from CPU) and ACK' (from device); outputs: OBF', INTR and port data. WR' falling clears INTR; WR' rising sets OBF' low and puts data on the port; ACK' falling returns OBF' high; ACK' rising sets INTR (if INTE = 1)."
sources: ["Brey, The Intel Microprocessors, Sec. 11-3 (82C55 mode 1 strobed output, timing diagram, printer interface)", "Rafiquzzaman, Microprocessors and Microcomputer-Based System Design, Ch. 5 (8255 handshake modes)"]
changes:
  - "2026-10-12: replaced the ASCII sketch by a TikZ timing diagram with the four cause-effect arrows (answer unchanged)"
---
**i. Mode and application**

The signals $\overline{OBF}$ (output buffer full), $\overline{ACK}$ (acknowledge) and INTR belong to **8255 Mode 1 (strobed / handshake) output**.

*Applications:* sending data to a slower peripheral that must confirm each byte, such as a **printer** (the classic example), a plotter, or a display controller. The CPU writes a byte, the device takes it and acknowledges, and the 8255 interrupts the CPU for the next byte.

**ii. Inputs, outputs and cause $\to$ effect**

- **Inputs to the 8255:** $\overline{WR}$ (from the CPU, write to the port) and $\overline{ACK}$ (from the peripheral, "I have taken the data").
- **Outputs from the 8255:** $\overline{OBF}$ (to the peripheral, "new data is waiting"), **INTR** (to the CPU, "ready for the next byte"), and the **port data lines**.

| # | Input change | $\to$ | Output change |
|:-:|:--|:-:|:--|
| 1 | $\overline{WR}$ goes **low** (CPU starts writing) | $\to$ | **INTR goes low** (old request cleared) |
| 2 | $\overline{WR}$ goes **high** (end of write) | $\to$ | **$\overline{OBF}$ goes low** (buffer full) and the **new data appears on the port** |
| 3 | $\overline{ACK}$ goes **low** (device takes the data) | $\to$ | **$\overline{OBF}$ goes high** (buffer empty, data removed from port) |
| 4 | $\overline{ACK}$ goes **high** (end of acknowledge) | $\to$ | **INTR goes high** (interrupt requested, if INTE = 1) |

![8255 mode 1 output: WR', OBF', INTR, ACK' and the port, with arrows from each input change to the output change it causes](figures/mode1.png)

The arrows are: $\overline{WR}\downarrow \to$ INTR$\downarrow$; $\overline{WR}\uparrow \to \overline{OBF}\downarrow$ and data valid; $\overline{ACK}\downarrow \to \overline{OBF}\uparrow$; $\overline{ACK}\uparrow \to$ INTR$\uparrow$.

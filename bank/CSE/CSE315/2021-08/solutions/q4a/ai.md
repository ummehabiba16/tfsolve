---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Flawed at RD': in the proposed Mode 2 diagram INTR stays high when RD' falls. As in Mode 1 input, the falling edge of RD' must reset INTR (the CPU has started reading the latched byte, so no second interrupt for it). Fix: draw INTR going low shortly after RD' falls; it rises again only on the next STB' or ACK' rising edge. WR', OBF', ACK', STB', IBF and Port A are drawn correctly."
sources: ["Brey, The Intel Microprocessors, Sec. 11-3 (82C55 mode 1 strobed input/output and mode 2 bidirectional timing)", "Hall, Microprocessors and Interfacing, Ch. 9 (8255 mode 2 handshaking)"]
---
Mode 2 (bidirectional Port A) is Mode 1 strobed output and Mode 1 strobed input **combined on the same port**. Each signal must therefore behave as in the corresponding Mode 1 diagram:

| Signal change | Required by | In Figure 4(a)-3 |
|:--|:--|:-:|
| $\overline{WR}$ falls $\to$ INTR falls | Mode 1 output | correct |
| $\overline{WR}$ rises $\to$ $\overline{OBF}$ falls | Mode 1 output | correct |
| $\overline{ACK}$ falls $\to$ $\overline{OBF}$ rises, Port A outputs the data | Mode 1 output (in Mode 2 the output buffer is enabled only by $\overline{ACK}$) | correct |
| $\overline{STB}$ falls $\to$ IBF rises, data latched | Mode 1 input | correct |
| $\overline{STB}$ rises $\to$ INTR rises | Mode 1 input | correct |
| **$\overline{RD}$ falls $\to$ INTR falls** | **Mode 1 input** | **missing: INTR stays high** |
| $\overline{RD}$ rises $\to$ IBF falls | Mode 1 input | correct |

**The flaw.** In Mode 1 input (Figure 4(a)-1), the **falling edge of $\overline{RD}$ resets INTR**: the CPU has begun reading the latched byte, so the interrupt request for that byte must be removed. Otherwise, when the ISR returns, the CPU would be interrupted again for data it has already read. In the proposed Mode 2 diagram, INTR stays high through the whole $\overline{RD}$ pulse and afterwards, which is wrong.

**Fix.** Redraw INTR so that it **goes low shortly after the falling edge of $\overline{RD}$** (an arrow from $\overline{RD}\downarrow$ to INTR$\downarrow$, as $\overline{WR}\downarrow$ already does for the output side). INTR then stays low until the next request: the next rising edge of $\overline{STB}$ (new input byte latched) or of $\overline{ACK}$ (output byte taken, if the output interrupt INTE1 is enabled).

```text
RD'   -------------------------------+          +--------
                                     |__________|
INTR  ---------+          +----------+
               |__________|          |____________________
          WR' falls   STB' rises   RD' falls (reset: must be added)
```

*Note:* INTR is one pin shared by the input and output sides of Port A. The diagram is taken to show the input request (set by $\overline{STB}$) being served by the $\overline{RD}$ cycle, as the question's hint about the falling edge of $\overline{RD}$ indicates.

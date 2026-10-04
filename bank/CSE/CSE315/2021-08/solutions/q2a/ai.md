---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "No flaw: 9 multiplexed address pins x 2 (RAS', CAS') = 18 bits = 256K; the 8-bit row address goes to an 8-to-256 decoder that selects one row in each of the four 256 x 256 arrays (4 x 256 = 1024 bits); the 8-bit column address drives four 256-to-1 multiplexers (4 bits); the row and column MSBs (A8) select one bit through the 4-to-1 MUX; WE' picks read or write."
sources: ["Brey, The Intel Microprocessors, Sec. 10-1 (DRAM, internal structure of a 256K x 1 DRAM with four 64K arrays)", "Rafiquzzaman, Microprocessors and Microcomputer-Based System Design, Ch. 5 (DRAM)"]
---
**The design is flawless:** it does exactly what the specification asks. Each requirement can be checked against the figure.

| Requirement | In the design | Check |
|:--|:--|:--|
| 256K $\times$ 1 from four 64K-bit sections | Four 64K arrays, each $256 \times 256$ | $4 \times 64\text{K} = 256\text{K}$ bits, 1-bit data (Din/Dout) |
| Row and column addresses | 9 pins A0-A8, latched into the **row latch** by $\overline{RAS}$ and the **column latch** by $\overline{CAS}$ | $2 \times 9 = 18$ bits, and $2^{18} = 256\text{K}$ |
| Row address selects 1024 bits | 8 row bits drive the **8-line to 256-line decoder**, which activates the same row in all four arrays | $4 \times 256 = 1024$ bits |
| Column address filters 4 bits | 8 column bits drive each array's **256-to-1 multiplexer** | one bit from each array = 4 bits |
| MSBs of row and column pick 1 of 4 | Row A8 and column A8 drive the **4-to-1 MUX** | $2^2 = 4$ choices |
| Read / write | $\overline{WE}$ goes to the multiplexers and the output MUX | $\overline{WE}$ = 1: Dout; $\overline{WE}$ = 0: Din written |

**Operation:**

1. Row address on A0-A8, $\overline{RAS}$ low: row latched; 1024 cells (one row of each array) go to the sense amplifiers.
2. Column address on A0-A8, $\overline{CAS}$ low: column latched; each array's multiplexer picks 1 of its 256 bits.
3. The two MSBs choose one of the four bits through the 4-to-1 MUX: read to Dout, or write from Din.
4. When $\overline{RAS}$ goes high the row is written back, which also refreshes it. Refresh is still needed every few ms, but that is done by the external DRAM controller ($\overline{RAS}$-only refresh), not by this chip, so it is not a flaw of the design.

Multiplexing the address halves the pin count (9 pins instead of 18).

*Note:* the answer depends on the figure feeding the row-latch MSB and the column-latch MSB to the select inputs of the 4-to-1 MUX, as the specification says. If both select lines were taken from the column latch, the row MSB would be unused and only 128K cells could be reached; the fix would be to route row A8 to one select input.

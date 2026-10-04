---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "With a 16-bit data bus the 512 KB becomes 8 pairs of 62256 (even bank on D0-D7, odd bank on D8-D15). RAM A0-A14 move to CPU A1-A15; both 74LS138s decode A18-A16 (one pair = 64 KB), U3 becomes the even-bank decoder enabled by A0 = 0 and U9 the odd-bank decoder enabled by BHE' = 0, both also need A19 = 0 and a memory cycle; add a second 74LS245 for D8-D15 and buffer A16-A19 and BHE'."
sources: ["Brey, The Intel Microprocessors, Sec. 10-3 and 10-4 (8088 and 8086 memory interface, 62256 SRAM, separate bank decoders, BHE and A0)", "MHE 8086-Memory_Organization slides 2-6 (two banks, BHE/A0)"]
---
**What changes with a 16-bit data bus**

The 8088 has an 8-bit data bus, so all 16 RAMs sit on D0-D7 and each one holds 32K consecutive bytes. The 80XX reads 16 bits at once, so memory must be split into an **even (low) bank on D0-D7** and an **odd (high) bank on D8-D15**, selected by **A0** and **$\overline{BHE}$** (assumed to be provided by the 80XX, as on the 8086, since it is needed for byte access on a 16-bit bus):

| $\overline{BHE}$ | A0 | Banks used |
|:-:|:-:|:--|
| 0 | 0 | both (16-bit word) |
| 0 | 1 | odd bank only (D8-D15) |
| 1 | 0 | even bank only (D0-D7) |

The memory size (16 $\times$ 32K $\times$ 8 = 512 KB) and the address range **00000H-7FFFFH** stay the same. Now the RAMs work in **8 pairs** (one even + one odd chip), each pair holding 64 KB.

**Required changes**

1. **RAM address pins.** Each RAM stores 32K words of the bank, addressed by **A1-A15**. Connect the 62256 pins A0-A14 to buffered **A1-A15** (not A0-A14). A0 is no longer a RAM address; it becomes a bank select.
2. **Decoders.** Both 74LS138s decode the **same** address bits **A16, A17, A18** (inputs A, B, C), so output $Y_k$ selects the pair at $k \times 10000\text{H}$ to $k \times 10000\text{H} + \text{FFFFH}$.
   - **U3 = even-bank decoder**: its 8 outputs go to the $\overline{CS}$ of the 8 RAMs on **D0-D7**; enable $\overline{G2A}$ = **A0**.
   - **U9 = odd-bank decoder**: its 8 outputs go to the $\overline{CS}$ of the 8 RAMs on **D8-D15**; enable $\overline{G2A}$ = **$\overline{BHE}$**.
   - Both: $\overline{G2B}$ = **A19** (the board is selected only for 00000H-7FFFFH, A19 = 0) and G1 = memory cycle (IO/$\overline{M}$ = 0, from the 74LS04 inverter, as before).
   - The 74LS139 (U4) that split A18, A19 into two 256K halves is no longer needed for the decoders. A19 alone (with IO/$\overline{M}$) makes the board select.
3. **Data bus.** Add a **second 74LS245** for **D8-D15**, with the same G (board select from the 74LS20/74LS00 logic, now: A19 = 0 and memory cycle) and the same DIR ($\overline{RD}$) as the existing D0-D7 transceiver. The odd-bank RAMs connect their D0-D7 pins to the buffered D8-D15.
4. **Address/control buffers.** The third 74LS244 now buffers $\overline{RD}$, $\overline{WR}$, **A16-A19** and **$\overline{BHE}$** (A15 moves to the second '244 together with A8-A14). $\overline{WR}$ and $\overline{RD}$ still go to $\overline{WE}$ and $\overline{OE}$ of every RAM.

```text
 CPU A1-A15  ------------------------> A0-A14 of all 16 RAMs
 CPU A16-A18 --> C B A of U3 and U9
                 U3 (even bank): G2A' = A0,   G2B' = A19, G1 = memory  -> CS' of 8 RAMs on D0-D7
                 U9 (odd bank):  G2A' = BHE', G2B' = A19, G1 = memory  -> CS' of 8 RAMs on D8-D15
 D0-D7   <=> 74LS245 (existing) <=> even-bank RAM data
 D8-D15  <=> 74LS245 (new)      <=> odd-bank RAM data
             both: G = board select (A19 = 0, memory), DIR = RD'
```

**Address map after the change**

| Decoder output | Address range | Even RAM (U3) holds | Odd RAM (U9) holds |
|:-:|:-:|:--|:--|
| $Y_0$ | 00000H-0FFFFH | 00000H, 00002H, ... | 00001H, 00003H, ... |
| $Y_1$ | 10000H-1FFFFH | even bytes | odd bytes |
| ... | ... | ... | ... |
| $Y_7$ | 70000H-7FFFFH | even bytes | odd bytes |

A word at an even address is read in one bus cycle (both chips of the pair selected); a single byte selects only one chip. This uses the **separate bank decoder** method. Alternatively one decoder could select both chips of a pair, with separate write strobes ($\overline{WR}$ OR A0 for the even bank, $\overline{WR}$ OR $\overline{BHE}$ for the odd bank).

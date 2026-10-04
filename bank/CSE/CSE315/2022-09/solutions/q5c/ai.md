---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "256K x 1 DRAM with 9 multiplexed address pins (A0-A8): RAS' latches the 9-bit row address (8 bits to the 8-to-256 row decoder of all four 64K arrays, 1 bit to the final MUX), CAS' latches the 9-bit column address (8 bits to each 256-to-1 column multiplexer, 1 bit to the 4-to-1 MUX); WE' chooses read (Dout) or write (Din). Activating a row also refreshes it."
sources: ["Brey, The Intel Microprocessors, Sec. 10-1 (DRAM: multiplexed address, RAS and CAS, 256K x 1 organization, refresh)", "Rafiquzzaman, Microprocessors and Microcomputer-Based System Design, Ch. 5 (DRAM)"]
---
**Organisation.** The chip is a **256K $\times$ 1 DRAM** ($2^{18}$ bits) built from **four 64K arrays**, each $256 \times 256$ cells. It needs 18 address bits but has only **9 address pins (A0-A8)**. The address is sent in two halves on the same pins (**address multiplexing**), latched by $\overline{RAS}$ and $\overline{CAS}$.

**Access mechanism**

1. **Row address.** The memory controller puts the 9-bit **row address** on A0-A8 and pulls $\overline{RAS}$ low. The **row latch** stores it. 8 bits go to the **8-line to 256-line row decoder**, which activates one of the 256 rows **in all four arrays** at once. All 256 cells of that row in each array are read into the sense amplifiers.
2. **Column address.** The controller then puts the 9-bit **column address** on A0-A8 and pulls $\overline{CAS}$ low. The **column latch** stores it. 8 bits drive each array's **256-to-1 multiplexer**, which picks one bit out of the 256 in the active row. Each of the four arrays now offers one bit.
3. **Array select.** The remaining address bits (the 9th row bit and the 9th column bit) drive the **4-to-1 multiplexer**, which selects one of the four array outputs.
4. **Read or write.** If $\overline{WE}$ = 1 (read), the selected bit appears on **Dout**. If $\overline{WE}$ = 0 (write), the bit on **Din** is written into the selected cell.
5. **End of cycle.** $\overline{RAS}$ and $\overline{CAS}$ return high. The sense amplifiers write the whole row back, which **refreshes** it (DRAM cells are capacitors that leak). A periodic $\overline{RAS}$-only cycle for each of the 256 rows refreshes all four arrays.

```text
 A0-A8 --+--> [Row latch]  --8--> [8:256 row decoder] --> row in all 4 arrays
         |         (RAS')  --1--------------------------------+
         |                                                    v
         +--> [Column latch] --8--> 4 x [256:1 column mux] --> [4:1 MUX] --> Dout
                   (CAS')  --1------------------------------->     ^  Din
                                                       WE' = read/write
```

Multiplexing halves the number of address pins (9 instead of 18), which keeps the package small, at the cost of needing $\overline{RAS}$/$\overline{CAS}$ timing from the controller.

*Note:* exactly which address bit selects the array (here one row bit and one column bit) depends on the device; the figure shows only that the 4-to-1 MUX takes the leftover address information.

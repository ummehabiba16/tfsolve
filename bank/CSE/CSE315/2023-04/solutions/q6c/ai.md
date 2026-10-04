---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "(i) With D7 pulled high and an active IR line reading 0: IR2 -> 11111011 = FBh, IR5 -> 11011111 = DFh. (ii) Both active give 11011011 = DBh; the higher-priority ISR (IR2, 4C215h, e.g. 4C21h:0005h) is also stored at vector DBh (0036Ch), so IR2 is served first; IR5 (vector DFh, 13D2Bh) is served after IRET while its request is still active."
sources: ["Brey, The Intel Microprocessors, Sec. 12-3 (expanding the interrupt structure with the 74ALS244, Table 12-1, priority by duplicating vectors)", "MHE INTR slides 13-15 (interrupt vector table, IP low word, CS high word)"]
---
**How the circuit works.** IR0-IR6 are active-low request lines with 10K pull-ups. The 74ALS30 NAND gate makes INTR = 1 whenever any IR line is low. During $\overline{INTA}$ the 74ALS244 drives the IR levels onto D0-D6 as the **vector (type) number**. D7 is tied to Vcc through 10K, so it is always 1. Inactive lines read 1 and the active line reads 0.

**i. Vector numbers**

| Request | D7 D6 D5 D4 D3 D2 D1 D0 | Vector |
|:-:|:-:|:-:|
| IR2 alone | 1 1 1 1 1 0 1 1 | **FBh** (vector table address $FBh \times 4$ = 003ECh) |
| IR5 alone | 1 1 0 1 1 1 1 1 | **DFh** (vector table address $DFh \times 4$ = 0037Ch) |

**ii. Priority resolution when IR2 and IR5 are active together**

Both lines are low, so the buffer puts **1101 1011 = DBh** on the data bus. This is a third vector, different from FBh and DFh. Priority is resolved **in the vector table**: at vector DBh we store the address of the **higher-priority** ISR, IR2's.

ISR addresses as CS:IP (one valid choice): IR2 at 4C215h = **4C21h:0005h**, IR5 at 13D2Bh = **13D2h:000Bh**. The IP is stored as the low word and the CS as the high word.

| Vector | Table address | Bytes stored (low to high) | ISR |
|:-:|:-:|:--|:--|
| FBh (IR2 only) | 003ECh-003EFh | 05 00 21 4C | IR2: 4C21h:0005h = 4C215h |
| DFh (IR5 only) | 0037Ch-0037Fh | 0B 00 D2 13 | IR5: 13D2h:000Bh = 13D2Bh |
| DBh (IR2 + IR5) | 0036Ch-0036Fh | 05 00 21 4C | IR2 (higher priority) |

**Sequence**

1. IR2 and IR5 go low together, so INTR = 1. At the end of the current instruction (IF = 1) the 8086 runs the $\overline{INTA}$ cycles and reads vector **DBh**.
2. It pushes FLAGS, CS, IP, clears IF and TF, and jumps to the address in 0036Ch, the **IR2 ISR (4C215h)**. IR5 waits (IF = 0, and its line is still low).
3. The IR2 ISR services the device, which removes the IR2 request, and ends with IRET.
4. IR5 is still low, so INTR is still 1. The next $\overline{INTA}$ reads **DFh** and the **IR5 ISR (13D2Bh)** runs.

So the higher-priority request is always served first by putting its ISR address at every vector where both bits are 0. With 7 inputs, all 128 vectors from 80h to FFh (D7 = 1) may be needed to cover every combination.

*Note:* the IR-to-data-line wiring (IR$n \to$ D$n$, D7 pulled high) is read from the figure, as in Brey's Table 12-1 (IR0 = FEh, ..., IR6 = BFh). CS:IP values are one possible split of each 20-bit address.

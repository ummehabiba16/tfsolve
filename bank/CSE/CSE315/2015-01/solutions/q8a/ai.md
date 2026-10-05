---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "BHE' (pin 34): bus high enable, low when the high (odd) byte D15-D8 is used; with A0 it selects the banks. TEST' (pin 23): checked by the WAIT instruction; the CPU idles until TEST' is low (used with the 8087). ALE (pin 25): address latch enable, a pulse in T1 telling external latches to capture the address from the multiplexed AD lines. MN/MX' (pin 33): 1 = minimum mode (CPU makes bus control signals), 0 = maximum mode (8288 bus controller, multiprocessor)."
sources: ["MHE 8086 Hardware Specifications slides (BHE, TEST, ALE, MN/MX pin descriptions)", "MHE 8086-Memory_Organization slides 3-5 (BHE and A0)"]
---
**(i) $\overline{BHE}$ (Bus High Enable, pin 34, output, active low).** Output during T1 (multiplexed with status S7). When low, it enables the **upper half of the data bus (D15-D8)**, i.e. the **odd memory bank**. Together with A0 it selects: both banks (word, $\overline{BHE}$ = 0, A0 = 0), odd byte (0, 1), even byte (1, 0).

**(ii) $\overline{TEST}$ (pin 23, input, active low).** Examined by the **WAIT** instruction: if $\overline{TEST}$ is high, the processor stays in an idle state until it goes low; if low, execution continues. It is used to **synchronize the 8086 with an external device**, typically the 8087 coprocessor (which drives BUSY to $\overline{TEST}$).

**(iii) ALE (Address Latch Enable, pin 25, output, active high).** The 8086 multiplexes address and data on AD15-AD0 (and address/status on A19-A16). In **T1** it puts out the address and gives an **ALE pulse**; external latches (74LS373) capture the address on ALE, so the address stays valid while the same pins carry data in T2-T4.

**(iv) MN/$\overline{MX}$ (pin 33, input).** Selects the operating mode: **1 (+5 V) = minimum mode**, a single-processor system where the 8086 itself generates the bus control signals ($\overline{RD}$, $\overline{WR}$, M/$\overline{IO}$, ALE, $\overline{DEN}$, DT/$\overline{R}$, HOLD/HLDA); **0 (ground) = maximum mode**, where pins 24-31 give status ($\overline{S0}$-$\overline{S2}$, QS0, QS1, $\overline{LOCK}$, $\overline{RQ}/\overline{GT}$) and an 8288 bus controller generates the commands, for multiprocessor/coprocessor systems.

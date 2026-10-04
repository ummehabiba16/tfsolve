---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Flawed. F/C' is tied to +5 V, so the 8284A takes its clock from EFI, which is unconnected, and the 30 MHz crystal is ignored; CSYNC tied high also holds the dividers reset, so there is no CLK. Fix: ground F/C' and CSYNC. Then CLK = 30/3 = 10 MHz, which suits only an 8086-1; for a standard 8086/8088 (5 MHz) use a 15 MHz crystal."
sources: ["MHE 8086 Hardware Specifications slides 10-11 (clock, 8284A on CLK pin 19)", "Brey, The Intel Microprocessors, Sec. 9-3 (8284A pins F/C', EFI, CSYNC, divide-by-3; 15 MHz crystal gives 5 MHz)"]
---
**Yes, the design has flaws.**

**Flaw 1: F/$\overline{C}$ is tied to +5 V.**
F/$\overline{C}$ selects the clock source of the divide-by-3 counter (the multiplexer in Figure 1(b)-1): **logic 0 = crystal oscillator (X1, X2)**, logic 1 = external frequency input **EFI**. With F/$\overline{C}$ = 1 the counter is fed from EFI, but **EFI is not connected**. The 30 MHz crystal only drives the OSC output, so the 8086/8088 gets **no valid CLK**.

**Flaw 2: CSYNC is tied to +5 V (it is joined to F/$\overline{C}$).**
CSYNC (clock synchronization) is used only with EFI, to synchronize several 8284As. While CSYNC = 1 the divide-by-3 and divide-by-2 counters are **held reset**, so CLK and PCLK stop. With a crystal, CSYNC must be grounded.

**Fix:** connect **F/$\overline{C}$ = 0 and CSYNC = 0** (both to ground), exactly as in the standard 8284A connection. Then

$$f_{CLK} = \frac{f_{crystal}}{3} = \frac{30\ \text{MHz}}{3} = 10\ \text{MHz} \ (33\%\ \text{duty}), \qquad f_{PCLK} = 5\ \text{MHz}$$

**Flaw 3 (speed rating): 10 MHz is too fast for most of the processors named.**
The figure says "8086 **or** 8088". A standard 8086 or 8088 is rated for 5 MHz (8086-2/8088-2: 8 MHz); only the **8086-1** runs at 10 MHz. **Fix:** use an 8086-1, or use a **15 MHz crystal** to get the usual 5 MHz CLK for an 8086/8088.

**Parts that are correct:** the $\overline{RES}$ circuit (10 k$\Omega$, 10 µF, diode and push button) gives a power-on and manual reset; the 8284A synchronizes it and drives RESET of the processor and the system reset line. CLK goes to the processor's CLK input.

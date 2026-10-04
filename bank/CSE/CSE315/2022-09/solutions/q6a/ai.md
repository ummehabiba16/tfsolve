---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "F/C' is grounded, so the 8284A uses the 30 MHz crystal and ignores the 15 MHz on EFI. (i) Yes: 30 MHz / 3 = 10 MHz CLK (33% duty) reaches the processor. (ii) No: PCLK = CLK / 2 = 5 MHz, not 15 MHz; no 8284A output gives 15 MHz from these inputs (OSC = 30 MHz could be halved externally, or the 15 MHz source fed directly to the DAC)."
sources: ["MHE 8086 Hardware Specifications slides 10-11 (clock, 8284A connected to CLK pin 19)", "Brey, The Intel Microprocessors, Sec. 9-3 (8284A: F/C', EFI, X1/X2, divide-by-3 CLK, PCLK = CLK/2, OSC)"]
---
**How the 8284A makes its clocks**

```text
 X1/X2 (crystal) --> [crystal oscillator] --+--> OSC (= crystal frequency)
                                            |
 EFI (external) ----------------------------|--+
                                            v  v
                        F/C' = 0: crystal  [ MUX ]  F/C' = 1: EFI
                                              |
                                        [ divide by 3 ] --> CLK  (f/3, 33% duty)  -> 8086
                                              |
                                        [ divide by 2 ] --> PCLK (f/6, 50% duty)  -> peripherals
```

- **F/$\overline{C}$** (frequency/crystal select) chooses the clock source: **0 = crystal on X1/X2**, 1 = external frequency on EFI.
- The chosen frequency $f$ is divided by **3** to give **CLK** ($f/3$, 33% duty cycle, as the 8086 needs).
- CLK is divided by **2** to give **PCLK** ($f/6$, 50% duty) for peripherals.
- **OSC** outputs the crystal oscillator frequency directly (available only when a crystal is used).

In Figure 6(a), **F/$\overline{C}$ is grounded**, so the **30 MHz crystal** is the source and the 15 MHz signal on EFI is **not used at all**.

**i. Microprocessor: yes, it gets 10 MHz**

$$f_{CLK} = \frac{f_{crystal}}{3} = \frac{30\ \text{MHz}}{3} = \mathbf{10\ MHz}$$

The crystal oscillator runs at 30 MHz. The F/$\overline{C}$ multiplexer selects it, the divide-by-3 counter produces a 10 MHz, 33% duty clock on CLK, and CLK drives pin 19 of the 8086 (an 8086-1 can run at 10 MHz).

**ii. DAC: no, it does not get 15 MHz**

$$f_{PCLK} = \frac{f_{CLK}}{2} = \frac{10\ \text{MHz}}{2} = \mathbf{5\ MHz} \neq 15\ \text{MHz}$$

- PCLK is always CLK/2, i.e. one sixth of the source, so with a 30 MHz source it can only be 5 MHz.
- The 15 MHz on EFI does not help: it is ignored because F/$\overline{C}$ = 0. If F/$\overline{C}$ were 1, EFI would replace the crystal as the source and give CLK = 5 MHz and PCLK = 2.5 MHz, so the processor would be wrong too.
- No 8284A output equals 15 MHz with these inputs. Only one source can be used at a time, and neither divide-by-3 nor divide-by-6 of 30 MHz gives 15 MHz.

**Possible fixes:** feed the DAC directly from the 15 MHz source instead of from PCLK, or take **OSC** (30 MHz) and divide it by 2 with an external flip-flop to get 15 MHz.

*Note:* the paper prints "81212 microprocessor"; the figure shows an 8086, and the answer assumes an 8086.

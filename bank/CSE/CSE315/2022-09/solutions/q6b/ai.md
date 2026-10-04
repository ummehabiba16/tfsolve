---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Not enough. It is an 8088-style circuit: on the 8086, AD15-AD8 carry address in T1 and data later, so the '244 must be replaced by a '373 latch (G = ALE, OE' = GND) for A15-A8, and a second '245 (G = DEN', DIR = DT/R') is needed for D15-D8. The BHE/A19-A16 '373, the AD7-AD0 '373 and '245, and the control '244 are correct."
sources: ["Brey, The Intel Microprocessors, Sec. 9-1 and 9-2 (demultiplexing and fully buffered 8088 and 8086 systems: three 74LS373 latches, two 74LS245 transceivers)", "MHE 8086 Hardware Specifications slides (multiplexed AD15-AD0, ALE, DT/R, DEN)"]
---
**Verdict: the circuit is not enough for a fully buffered 8086.**

**What is correct**

- **Control bus:** M/$\overline{IO}$, $\overline{RD}$, $\overline{WR}$ through a 74LS244 buffer. OK.
- **$\overline{BHE}$/S7 and A19/S6-A16/S3:** these are multiplexed with status, so they are latched in a 74LS373 with G = ALE and $\overline{OE}$ = GND. OK.
- **AD7-AD0:** latched by a 74LS373 (G = ALE) to give A7-A0, and connected through a 74LS245 transceiver (enable from $\overline{DEN}$, direction from DT/$\overline{R}$) to give D7-D0. OK.

**What is wrong**

1. **AD15-AD8 go through a '244 buffer, not a latch.** On the 8086 these pins are **multiplexed**: they carry A15-A8 only during T1 and **data D15-D8** during T2-T4. A '244 just passes whatever is on the pins, so the "buffered address bus" A15-A8 would change to data in the middle of the bus cycle. (The '244 is right only for the 8088, whose A15-A8 pins are address-only.)
2. **No buffered upper data bus D15-D8.** The 8086 has a 16-bit data bus, but only D7-D0 are buffered. Odd-address bytes and the high byte of words could not be read or written.

**Corrections**

- Replace the '244 on AD15-AD8 with a **74LS373 latch**: inputs AD15-AD8, **G = ALE**, $\overline{OE}$ = GND, outputs A15-A8.
- Add a second **74LS245 transceiver** between AD15-AD8 and the buffered **D15-D8**, with its **G = $\overline{DEN}$** and **DIR = DT/$\overline{R}$**, the same as the first '245.

```text
 AD15-AD8 --+--> [ '373 ] --> A15-A8   (G = ALE, OE' = GND)     replaces '244
            +--> [ '245 ] <-> D15-D8   (G = DEN', DIR = DT/R')  new
 AD7-AD0  --+--> [ '373 ] --> A7-A0    (G = ALE)                as drawn
            +--> [ '245 ] <-> D7-D0    (G = DEN', DIR = DT/R')  as drawn
 BHE/S7, A19-A16 -> [ '373 ] --> BHE', A19-A16 (G = ALE)        as drawn
 M/IO', RD', WR' -> [ '244 ] --> buffered control bus           as drawn
```

The fully buffered 8086 then has **three '373 latches** (A19-A16 with $\overline{BHE}$, A15-A8, A7-A0), **two '245 transceivers** (D15-D8, D7-D0) and a '244 for the control signals. If DMA is used, the '244 and '373 output enables are driven by HLDA so the buses can be released, instead of being grounded.

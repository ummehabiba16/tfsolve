---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Pins 1 and 20 are both GND and are connected in parallel so that the large transient (switching) currents of the chip are shared and sunk without a significant voltage drop or ground bounce; both must be grounded."
sources: ["MHE 8086-Architecture slide '8086 Pin Overview' (pins 1 and 20: ground, to sink transient current without significant voltage drop)", "Brey, The Intel Microprocessors, Sec. 9-1 (8086 power supply requirements)"]
---
The 8086 has **two GND pins, pin 1 and pin 20**, connected in parallel to ground:

- When many outputs and internal gates switch at the same instant (e.g. 16 data lines and 20 address lines changing together), the chip draws **large transient currents**. All of this current returns through ground.
- One thin pin and its bond wire have resistance and inductance. A large, fast-changing current through it would make the chip's internal ground rise above the real ground (**ground bounce**), which shifts logic levels and can cause errors.
- With **two ground pins in parallel**, the current is shared, so the **voltage drop is halved** and the transient current is sunk **without a significant voltage drop**. Pins 1 and 20 are at opposite corners of the die, which also spreads the current more evenly.

Both pins must be connected to ground; leaving one open defeats this purpose.

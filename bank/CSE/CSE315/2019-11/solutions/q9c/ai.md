---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Smaller transistors (0.18 um then 0.13 um in the Pentium 4) switch faster (higher clock rates), need lower supply voltage and less power and heat per transistor, and allow more transistors per chip (bigger caches, deeper pipeline, new units) at a lower cost per die."
sources: ["Brey, The Intel Microprocessors, Ch. 19 (Pentium 4: 0.18 and 0.13 micron technology, clock speeds)"]
---
The Pentium 4 moved from 0.18 µm to 0.13 µm (and later 90 nm) transistors. Advantages:

1. **Higher speed.** Smaller transistors have smaller capacitance and shorter channels, so they switch faster. This allowed much higher clock frequencies (from 1.4 GHz up to over 3 GHz).
2. **Lower power and heat per transistor.** They work at a **lower supply voltage** and need less charge to switch, so dynamic power ($\propto CV^2f$) per transistor falls and the chip runs cooler for the same work.
3. **More transistors on the same chip area.** More logic fits on a die: larger L1/L2 caches, the deeper (20-stage) NetBurst pipeline, extra execution units, SSE2 and Hyper-Threading.
4. **Lower cost.** More chips per silicon wafer and smaller dies reduce the cost per chip.
5. **Shorter wires inside the chip,** so signals travel faster between units.

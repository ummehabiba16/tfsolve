---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "DIP: rectangular package with two parallel rows of pins along the long sides (e.g. 8086, 40 pins). PGA: square package with a grid of pins on the whole underside (e.g. 80386, Pentium)."
sources: ["MHE 8086-Architecture slides (8086 packaged in a 40-pin DIP)", "Brey, The Intel Microprocessors, Ch. 9 and 17 (8086 DIP, 80386/Pentium PGA packages)"]
changes:
  - "2026-10-12: replaced the two ASCII sketches by TikZ drawings of the packages (answer unchanged)"
---
**DIP (Dual In-line Package)** (e.g. 8086, 40 pins): top view

![DIP: top view with two rows of 20 pins, and side view](figures/dip.png)

**PGA (Pin Grid Array)** (e.g. 80386, Pentium): bottom view

![PGA: bottom view with pins in a grid](figures/pga.png)

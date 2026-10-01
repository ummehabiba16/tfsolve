---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "16 extra pins: AD0-AD15 carry both address and data, so separate D0-D15 pins are needed (20 if the A16/S3-A19/S6 status lines are also separated)."
sources: ["MHE 8086-Architecture slide 41 (pin overview)", "MHE 8086 Hardware Specifications slides 5-7 (AD0-AD15, A16/S3-A19/S6, ALE)"]
---
In the 8086 (40-pin DIP):

- Pins 2-16 and 39: **AD0-AD15** (16 pins) are **multiplexed address and data** lines. They carry the address when ALE = 1 and data when ALE = 0.
- Pins 35-38: A16/S3-A19/S6 (4 pins) carry address and status.

To **de-multiplex the address bus and the data bus**, the 16-bit data bus needs its own pins **D0-D15**, while the existing 20 pins become a pure address bus A0-A19.

$$\text{Extra pins} = \mathbf{16}\ (\text{a 56-pin package})$$

(If the status signals S3-S6 were also given their own pins, $16+4 = 20$ extra pins would be needed. ALE would then no longer be required. The 80286, with de-multiplexed buses, uses a 68-pin package.)

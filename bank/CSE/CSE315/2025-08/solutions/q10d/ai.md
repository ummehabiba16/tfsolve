---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "With COM1A1:0 = 10, fast PWM gives a wave of f = f_clk/(N(TOP+1)), but CTC only clears OC1A once, so there is no square wave. (For a toggling CTC wave, f_CTC = f_FastPWM / 2.)"
sources: ["EHP Timer_Part_2 slides 28-29, 33-37 (CTC and fast PWM compare output modes, frequency formula)"]
---
**Fast PWM, COM1A1:0 = 10** (clear on compare match, set at BOTTOM): OC1A is set once and cleared once in every timer cycle of $TOP+1$ ticks:

$$f_{FastPWM} = \frac{f_{osc}}{N\,(TOP+1)}$$

**CTC, COM1A1:0 = 10** (clear OC1A on compare match): every match just *clears* OC1A again. Nothing ever sets it back to 1, so after the first match the pin stays **low**. **No square wave is produced**: its frequency is 0, so the two cannot be compared as waves.

**If CTC is used with toggle (COM1A1:0 = 01)**, the usual way to make a square wave in CTC, then OC1A changes once per cycle, so one period takes **two** timer cycles:

$$f_{CTC} = \frac{f_{osc}}{2N\,(TOP+1)} = \frac{1}{2}\,f_{FastPWM}$$

That is, for the same TOP, the **CTC wave has half the frequency of the fast PWM wave**.

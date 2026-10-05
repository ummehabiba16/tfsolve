---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Fast PWM is single slope (0 to TOP, then restart): f = fclk/(N(1+TOP)), up to twice the phase-correct frequency, but the pulse is aligned to BOTTOM so its centre (phase) moves with the duty cycle. Phase correct is dual slope (0 to TOP to 0): f = fclk/(2 N TOP), half the frequency, but pulses are symmetric about BOTTOM/TOP so the phase stays fixed; preferred for motor control."
sources: ["EHP Timer_Part_2 slides 31-48 (fast PWM, phase correct PWM, comparison)"]
---
| | Fast PWM | Phase Correct PWM |
|:--|:--|:--|
| Counting | **Single slope**: 0 $\to$ TOP, then back to 0 at once | **Dual slope**: 0 $\to$ TOP $\to$ 0 |
| Output (non-inverting) | Set at BOTTOM, cleared at compare match | Cleared at match while counting up, set at match while counting down |
| Frequency | $f = \dfrac{f_{clk}}{N(1 + TOP)}$ | $f = \dfrac{f_{clk}}{2N \cdot TOP}$, about **half** of fast PWM |
| Phase | Pulses start at BOTTOM; when the duty changes, the **centre of the pulse moves** (phase changes) | Pulses are **centred** on BOTTOM; the phase stays the same for all duty cycles |
| Use | High frequency where phase does not matter (LED dimming, DAC, power regulation) | Motor control (symmetric, less noise/torque ripple) |

**Example** (1 MHz, no prescaler, TOP = 999, OCR1A = 249, non-inverting):

- Fast PWM: period = 1000 µs (f = 1 kHz), high 250 µs, duty 25%.
- Phase correct (TOP = 999): period = $2 \times 999$ µs $\approx$ 2 ms (f $\approx$ 500 Hz), high time $2 \times 249$ µs, duty $\approx$ 25%.

```text
Fast PWM (single slope)
   TOP|              **              **              **
      |           ***             ***             ***
      |        ***             ***             ***
      |     ***             ***             ***
   OCR|  ***             ***             ***
     0|**              **              **
OC1x 1|----            ----            ----
     0|    ------------    ------------    ------------

Phase correct PWM (dual slope, same TOP: half the frequency)
   TOP|               ***                             **
      |            ***   ***                       ***
      |         ***         ***                 ***
      |     ****               ****         ****
   OCR|  ***                       ***   ***
     0|**                             ***
OC1x 1|-----                       ---------
     0|     -----------------------         ------------
```

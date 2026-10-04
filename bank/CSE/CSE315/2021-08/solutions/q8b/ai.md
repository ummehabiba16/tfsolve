---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Normal: counts 0 to 0xFFFF and overflows (TOV1), used for delays/elapsed time. CTC: counts 0 to TOP (OCR1A or ICR1) and is cleared on match, giving exact periods and 50% toggle waves of adjustable frequency. Fast PWM: single-slope 0 to TOP with OC1x set/cleared at BOTTOM and compare match, giving variable duty-cycle PWM."
sources: ["EHP Timer_Part_1 slides 18-27 (normal mode, overflow)", "EHP Timer_Part_2 slides 22-38 (CTC and fast PWM modes)"]
---
| Feature | Normal mode (WGM = 0000) | CTC mode (WGM = 0100 / 1100) | Fast PWM (WGM = 0101-0111, 1110, 1111) |
|:--|:--|:--|:--|
| Counting | 0 $\to$ 0xFFFF, then wraps to 0 | 0 $\to$ TOP, then **cleared to 0** on compare match | 0 $\to$ TOP, then restarts at 0 (single slope) |
| TOP | Fixed 0xFFFF | OCR1A or ICR1 (programmable) | Fixed 0x00FF/01FF/03FF, or ICR1 / OCR1A |
| Flag / interrupt used | TOV1 (overflow) | OCF1A (or ICF1) on match | TOV1 at TOP, OCF1x at compare match |
| OC1x pin | Not normally used (only toggle/set/clear on match with a fixed period) | **Toggle** on match: 50% square wave, $f = f_{clk}/(2N(1+TOP))$ | **Set at BOTTOM, clear on match** (or inverted): PWM with duty set by OCR1x, $f = f_{clk}/(N(1+TOP))$ |
| Period / frequency control | Fixed period $65536 \times N / f_{clk}$; adjusted only by reloading TCNT1 in software | Exact, set by TOP in hardware | Set by TOP; duty cycle set separately by OCR1x |
| Duty cycle | - | Always 50% (toggle) | Any, from 0 to 100% |
| Typical use | Delays, measuring elapsed time, input capture | Exact periodic interrupts, square waves of chosen frequency | Motor speed, LED brightness, DAC by filtering, servo |

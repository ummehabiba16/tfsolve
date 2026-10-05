---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(1) Overflow: TCNT1 counts to 0xFFFF and sets TOV1; used for delays and measuring elapsed time (count overflows) - TIMER1_OVF_vect. (2) Input capture: an edge on ICP1 copies TCNT1 to ICR1; used to measure period/frequency/pulse width - TIMER1_CAPT_vect (plus TIMER1_OVF_vect for long periods). (3) Output compare: TCNT1 matched with OCR1A/OCR1B to clear the timer, change OC1A/OC1B or interrupt; used for exact periodic events and waveform/PWM generation - TIMER1_COMPA_vect / TIMER1_COMPB_vect."
sources: ["EHP Timer_Part_2 slides 3-4, 8-10 (overflow interrupt, input capture, output compare)", "EHP Timer_Part_1 slides 11, 15-16 (Timer1 features and interrupts)"]
---
**1. Overflow (normal mode)**

- TCNT1 counts from its start value up to 0xFFFF; the next count wraps to 0 and sets **TOV1**.
- Applications: **time delays** (preload TCNT1, wait for overflow) and **measuring elapsed time** (count overflows and add TCNT1: $t = (n \times 65536 + TCNT1) \times$ tick).
- Interrupt: **Timer1 overflow, `TIMER1_OVF_vect`** (TOIE1).

**2. Input capture**

- On the selected edge of the **ICP1** pin, the hardware copies TCNT1 into **ICR1** and sets **ICF1**.
- Applications: measuring the **period, frequency or pulse width** of a signal, time-stamping external events.
- Interrupts: **input capture, `TIMER1_CAPT_vect`** (TICIE1), plus `TIMER1_OVF_vect` to count overflows when the period is longer than 65536 ticks.

**3. Output compare**

- TCNT1 is compared continuously with **OCR1A** and **OCR1B**. On a match, **OCF1A/OCF1B** is set and, depending on the mode, the timer is cleared (CTC) and/or the pins **OC1A/OC1B** are set, cleared or toggled.
- Applications: **exact periodic interrupts**, **square waves** of chosen frequency, **PWM** (fast or phase-correct) for motors, servos, LED dimming, and triggering ADC conversions at precise times.
- Interrupts: **output compare A/B, `TIMER1_COMPA_vect` and `TIMER1_COMPB_vect`** (OCIE1A, OCIE1B); in PWM modes the overflow interrupt marks each period.

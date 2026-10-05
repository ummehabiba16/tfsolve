---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "The timer/counter is a register that increments on a clock: with the internal (prescaled) system clock it is a timer (counts time), with pulses on the external T0/T1 pin it is a counter (counts events); the clock-select bits choose. Delays: (1) normal mode: load TCNT with 256 - n (or 65536 - n), wait for the overflow flag TOV (polling or interrupt); (2) CTC mode: put n - 1 in OCR, wait for the compare-match flag OCF; the timer clears itself and repeats exactly."
sources: ["EHP Timer_Part_1 slides 6-8, 21-27 (timer with internal or external clock, clock select, normal mode, overflow delay)", "EHP Timer_Part_2 slides 23-30 (CTC mode)"]
---
**Timer and counter in the same hardware**

Each ATmega timer is a register (TCNT0, TCNT1, TCNT2) that **increments by 1 on every pulse of its clock input**. The clock-select bits CS02:00 (in TCCR0) decide where the pulses come from:

- **Internal system clock** (directly or through the prescaler: /8, /64, /256, /1024): the register counts **time**, so it is a **timer**. Each count = prescaler / $f_{clk}$.
- **External pin T0 (PB0) or T1 (PB1)**, on the rising or falling edge (CS = 110 / 111): it counts **external events** (e.g. pulses from a sensor), so it is a **counter**.

The same register, flags (TOV, OCF) and interrupts are used in both cases.

**Two ways to generate a time delay**

**1. Normal mode (overflow).** The timer counts up to its maximum (0xFF or 0xFFFF) and sets the **overflow flag TOV** when it rolls over to 0.

- Load TCNT with $256 - n$ (8-bit) so that it overflows after $n$ counts; start the clock; wait until TOV = 1 (poll TIFR or use the overflow interrupt); stop the timer and clear TOV by writing 1.
- For longer delays count several overflows.

**2. CTC mode (clear timer on compare match).** Put $n - 1$ in **OCR0** (or OCR1A); TCNT counts 0 to OCR and then is **cleared automatically**, setting the **compare flag OCF**.

- Wait for OCF (poll or compare-match interrupt) and clear it. No reloading is needed, so periodic delays are exact.

*Example (Timer0, 1 MHz, prescaler 1):* a 100 µs delay needs 100 counts: normal mode TCNT0 = 256 - 100 = 156; CTC mode OCR0 = 99.

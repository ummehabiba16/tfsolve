---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Three timers: Timer0 (8-bit), Timer1 (16-bit), Timer2 (8-bit). PWM applications: DC motor speed control, servo position control, LED brightness/dimming, simple DAC (analog voltage by filtering), power control (SMPS, heaters), tone generation."
sources: ["EHP Timer_Part_1 slide 6 (ATmega32 has 3 timers)", "EHP Timer_Part_2 slides 2, 5-7, 55-57 (PWM: motors, servo, simulating an analog signal, controlling power)"]
---
**Timers:** the ATmega32 has **three** timer/counters: **Timer0** (8-bit), **Timer1** (16-bit, with input capture and two compare channels) and **Timer2** (8-bit, can run asynchronously from a 32 kHz crystal).

**Applications of PWM**

- **Speed control of DC motors** (average voltage set by the duty cycle).
- **Position control of servo motors** (pulse width sets the angle, e.g. 1-2 ms every 20 ms).
- **LED brightness** control (dimming).
- **Simulating an analog signal / simple DAC** by low-pass filtering the PWM wave.
- **Controlling power to a load** (heaters, switching power supplies) and generating tones.

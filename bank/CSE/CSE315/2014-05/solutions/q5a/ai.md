---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "ATmega16: S (0/5 V) to INT0 (PD2, rising-edge interrupt); T (0-5 V analog) to ADC0 (PA0), conversion started in the INT0 ISR and read in the ADC interrupt (alarm if ADC > 614, i.e. 60 C = 3 V); buzzer on PB0 through a transistor driver; alarm-stop switch to INT1 (PD3); Timer1 interrupt counts 1 minute; start signal to the fire-fighting system on PB1. No polling."
sources: ["EHP ATmega32 Interrupt slides 16-23 (external interrupts INT0, INT1)", "EHP 6. AVR ADC slides 16-36 (ADC0, AVCC reference, ADC interrupt)", "EHP Timer_Part_1 slides 25-27 (timer overflow interrupt for long delays)"]
---
**Block diagram**

```text
                             ATmega16
                     +---------------------------+
 Smoke sensor S ---->| PD2 / INT0                |
 (0 V / 5 V)         |                           |
                     |                    PB0    |---> transistor driver ---> Buzzer
 Temp sensor T ----->| PA0 / ADC0                |
 (0-5 V = 0-100 C)   |                    PB1    |---> START signal to automated
                     |                           |     fire-fighting system
 Stop-alarm switch ->| PD3 / INT1  (pull-up,     |
 (to GND)            |              active low)  |
                     | AVCC, AREF (+5 V, 100 nF) |
 +5 V, GND --------->| VCC, GND                  |
                     | (Timer1 internal: 1 min)  |
                     +---------------------------+
```

**How it works without polling**

1. **S sensor $\to$ INT0 (PD2), rising edge.** When smoke appears (0 $\to$ 5 V) the INT0 ISR starts an ADC conversion of the temperature.
2. **T sensor $\to$ ADC0 (PA0)**, $V_{ref}$ = AVCC = 5 V, ADC interrupt enabled. 60 °C corresponds to $60/100 \times 5 = 3.0$ V, i.e. $ADC = 3.0 \times 1024/5 = 614.4$. In the **ADC ISR**: if ADC > 614 (and smoke is still present) the alarm starts: **buzzer on (PB0)** and **Timer1 started**.
3. **Timer1 interrupt** (e.g. overflow or CTC every 1 s, counted to 60) measures **one minute** from the start of the buzz.
4. **Stop switch $\to$ INT1 (PD3)**, falling edge: its ISR turns the buzzer off and stops Timer1.
5. If the minute expires before the switch is pressed, the Timer1 ISR drives **PB1 high: start signal** to the automated fire-fighting system.

*Assumptions:* 5 V supply, active-high buzzer driver and start input, stop switch to ground with the internal pull-up.

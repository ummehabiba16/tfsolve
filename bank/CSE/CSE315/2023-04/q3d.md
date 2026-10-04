---
marks: 15
topics: [timer-ctc]
kind: numerical
source: {page: 27}
---
Suppose TIMER1 of ATmega32 is running in mode WGM = 0100 (Table 2). The value of OCR1A = 32768 and OCR1B = 15625. Pin OC1A and OC1B are configured to toggle on compare match. Initially, OC1A and OC1B are both low, and TCNT1 = 0. Prescaler is 64. Draw the wave shape of OC1A and OC1B with respect to TCNT1. Also, calculate the duty cycle and frequency of OC1A and OC1B.

**Table 2: Wave Generation Modes of TIMER1** (attached)

| WGM | Timer/Counter Mode of Operation | TOP | Update of OCR1X | TOV1 Flag Set on |
|:-:|:--|:-:|:-:|:-:|
| 1110 | Fast PWM | ICR1 | BOTTOM | TOP |
| 0100 | CTC | OCR1A | Immediate | MAX |
| 1010 | Phase Correct PWM | ICR1 | TOP | BOTTOM |

Attached sheet: [Figures and Tables for Section A](figures/sheet-1.png), [ATmega32 pinout](figures/sheet-2.png).

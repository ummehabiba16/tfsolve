---
marks: 10
topics: [timer-pwm]
kind: numerical
source: {page: 27}
---
Suppose TIMER1 of ATmega32 is operating in mode WGM = 1010 (Table 2). Prescaler is 8. The value of ICR1 is 2000, and OCR1A is 400. OC1A is configured to be clear on compare match when up-counting and set on compare match when down-counting. Draw the waveshape of OC1A with respect to TCNT1. Also, calculate the duty cycle and frequency of OC1A.

**Table 2: Wave Generation Modes of TIMER1** (attached)

| WGM | Timer/Counter Mode of Operation | TOP | Update of OCR1X | TOV1 Flag Set on |
|:-:|:--|:-:|:-:|:-:|
| 1110 | Fast PWM | ICR1 | BOTTOM | TOP |
| 0100 | CTC | OCR1A | Immediate | MAX |
| 1010 | Phase Correct PWM | ICR1 | TOP | BOTTOM |

Attached sheet: [Figures and Tables for Section A](figures/sheet-1.png), [ATmega32 pinout](figures/sheet-2.png).

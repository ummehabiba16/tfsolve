---
marks: 10
topics: [timer-pwm]
kind: code
source: {page: 27}
---
Write a C code for ATmega32 using TIMER1 to generate a square wave signal with period 2000 µs and high time 300 µs. You must use Fast PWM mode for this. Refer to Tables 2 and 3 for relevant configurations.

**Table 2: Wave Generation Modes of TIMER1** (attached)

| WGM | Timer/Counter Mode of Operation | TOP | Update of OCR1X | TOV1 Flag Set on |
|:-:|:--|:-:|:-:|:-:|
| 1110 | Fast PWM | ICR1 | BOTTOM | TOP |
| 0100 | CTC | OCR1A | Immediate | MAX |
| 1010 | Phase Correct PWM | ICR1 | TOP | BOTTOM |

**Table 3: Behavior of OC1A for Fast PWM** (attached)

| COM1A1 | COM1A0 | Description |
|:-:|:-:|:--|
| 0 | 0 | Normal port operation. OC1A is disconnected. |
| 0 | 1 | WGM=1110: Toggle OC1A. For other WGM, OC1A disconnected. |
| 1 | 0 | Clear OC1A on compare match. Set OC1A at BOTTOM. |
| 1 | 1 | Set OC1A on compare match. Clear OC1A at BOTTOM. |

**Registers (from Table 1, attached)**

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| TCCR1A | COM1A1 | COM1A0 | COM1B1 | COM1B0 | FOC1A | FOC1B | WGM11 | WGM10 |
| TCCR1B | ICNC1 | ICES1 | - | WGM13 | WGM12 | CS12 | CS11 | CS10 |
| TIMSK | OCIE2 | TOIE2 | TICIE1 | OCIE1A | OCIE1B | TOIE1 | OCIE0 | TOIE0 |
| TIFR | OCF2 | TOV2 | ICF1 | OCF1A | OCF1B | TOV1 | OCF0 | TOV0 |

*CS12, CS11, CS10: 001 = No prescaling, 010 = clk/8, 011 = clk/64, 100 = clk/256.*

Attached sheet: [Figures and Tables for Section A](figures/sheet-1.png), [ATmega32 pinout](figures/sheet-2.png).

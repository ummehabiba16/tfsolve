---
marks: 15
topics: [timer-input-capture]
kind: numerical
source: {page: 48}
note: "The edges are called E1 and E2, and then 'From T1 to T2', as printed."
---
Suppose you are measuring period of a square wave using TIMER1 of Atmega32. Square wave is fed to ICP1. At the point of rising edge E1, the value of TCNT1 is 6700. At the rising edge E2, the value of TCNT1 is 8000. From T1 to T2, TIMER1 overflow occurred 2 times. Prescaler is 0 i.e. TIMER1 clock is running as fast as internal 1MHz clock. What is the period of the square wave?

![Square waveform with rising edges E1 and E2; the period is from E1 to E2](figures/q6a-1.png)

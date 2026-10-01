---
marks: 8
topics: [timer-pwm]
kind: numerical
mandatory: true
source: {page: 19}
note: "OCR1B is printed as 'oxFF'."
---
Suppose TIMER 1 of ATMega32 is operating in the Fast PWM mode. Here, TOP is OCR1A. TOV1 flag is set when TOP is reached by the counter and OCR1A gets updated at the BOTTOM. Assume that the prescaler is 64. The value of OCR1A is 0xFFF and OCR1B is oxFF. OC1B is configured to be set on compare match and clear at BOTTOM. Please calculate the duty cycle and frequency of OC1B.

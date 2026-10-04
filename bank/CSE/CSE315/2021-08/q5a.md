---
marks: 13
topics: [adc-registers]
kind: code
source: {page: 48}
---
Suppose an imaginary pressure sensor is connected to Atmega32. The pressure sensor produces an output of 0V to 5V for 0 Pa to $10^{5}$ Pa linearly. Write a C code to measure pressure (Pa) continuously. Store the pressure value in a variable named "pressure". Use interrupt mode, right adjusted ADC (code: 0), internal reference voltage 5V (code: 01), prescaler 4 (code: 010). Sensor is connected to ADC1 (code: 00001).

**Registers (from the attached list)**

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| ADMUX | REFS1 | REFS0 | ADLAR | MUX4 | MUX3 | MUX2 | MUX1 | MUX0 |
| ADCSRA | ADEN | ADSC | ADATE | ADIF | ADIE | ADPS2 | ADPS1 | ADPS0 |

Attached sheet: [list of registers](figures/sheet-1.png).

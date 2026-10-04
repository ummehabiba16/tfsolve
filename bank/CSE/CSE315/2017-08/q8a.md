---
marks: 15
topics: [adc-registers]
kind: code
source: {page: 73}
note: "Printed as 'output of 0V to 3.3 for 0 degree', 'Write A C code' and 'prescalar'."
---
Suppose you are using a particular temperature sensor which produces an output of 0V to 3.3 for 0 degree to 330 degree Celsius linearly.

Write A C code to use ATmega32 ADC in polling mode to read the sensor value and determine the temperature using (i) by reading only ADCH (ii) by reading ADCH and ADCL. Just store the temperature in a variable.

Assume that you are using internal reference voltage of 5V (code: 0x1) and a prescalar of 2 (code: 0x1). The sensor is connected to the pin ADC0 (code: 0x0).

**Registers (from Table 1)**

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| ADMUX | REFS1 | REFS0 | ADLAR | MUX4 | MUX3 | MUX2 | MUX1 | MUX0 |
| ADCSRA | ADEN | ADSC | ADATE | ADIF | ADIE | ADPS2 | ADPS1 | ADPS0 |

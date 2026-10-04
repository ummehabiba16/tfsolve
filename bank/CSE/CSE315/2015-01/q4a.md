---
marks: 15
topics: [adc-registers]
kind: code
source: {page: 87}
note: "The input pin is printed with a slashed zero (ADC0)."
---
Major relevant registers for ATmega32 ADC subsystem are-

| ADCH (8 bits) | ADCL (8 bits) |
|:-:|:-:|

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| ADCSRA | ADEN | ADSC | ADATE | ADIF | ADIE | ADPS2 | ADPS1 | ADPS0 |
| ADMUX | REFS1 | REFS0 | ADLAR | MUX4 | MUX3 | MUX2 | MUX1 | MUX0 |

-write a **complete C program** that takes analog input in **ADC0** pin, uses external $V_{ref}$ in **AREF** pin and shows the digital output using **PORTA** and **PORTB**. You have to use the **interrupt** approach for the ADC conversion.

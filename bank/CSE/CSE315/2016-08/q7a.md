---
marks: 20
topics: [adc-auto-trigger]
kind: numerical
source: {page: 77}
note: "Sampling frequency printed as '20000 kHz' (20 kHz is likely meant, as in the ADC slide example)."
---
Suppose you need to sample an analog signal precisely at sampling frequency 20000 kHz using the on-chip ADC peripheral of ATmega32 microcontroller. Assume system clock frequency = 16 MHz and Timer0 prescaler = 8. Answer the following questions:

(i) How can you use Timer0 Compare Match event of ATmega32 to ensure proper ADC conversion timing? Mention the ADC registers that must be properly configured for this purpose?

(ii) Calculate the appropriate value of OCR0 register.

(iii) Calculate the **optimal** value of ADC prescaler.

(iv) How many ISRs you need to write for this purpose? Draw the flowchart for each ISR.

**Registers (from Table 1)**

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| ADMUX | REFS1 | REFS0 | ADLAR | MUX4 | MUX3 | MUX2 | MUX1 | MUX0 |
| ADCSRA | ADEN | ADSC | ADATE | ADIF | ADIE | ADPS2 | ADPS1 | ADPS0 |
| SFIOR | ADTS2 | ADTS1 | ADTS0 | - | ACME | PUD | PSR2 | PSR10 |

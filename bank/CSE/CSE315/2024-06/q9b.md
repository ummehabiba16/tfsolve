---
marks: 10
topics: [adc-registers]
kind: code
mandatory: true
source: {page: 19}
note: "Printed as 'explain those issues is brief'."
---
The C code in *Listing 1* is supposed to be an interrupt-driven program to perform ADC and display the result on the LEDs. The reference voltage is 4.0 V. The analogue input signal, that is continuously changing, is connected to the pin ADC5. ADC output is left justified and the prescaler is 8. The system clock frequency is 1 MHz. Please read the code carefully and write down all the issues that will prevent it from achieving the desired output. Kindly explain those issues is brief.

**Listing 1: C program for question 9(b)**

```c
#include<avr/io.h>
#include<avr/interrupt.h>

uint16_t adc_value; // uint16_t means a 16-bit unsigned integer

ISR(ADC_vect) {
    adc_value = (ADCH << 2) | (ADCL >> 6);
}

int main(void) {
    DDRA = 0xFF;    // set port A for output
    ADMUX = 0b11100000;
    ADCSRA = 0b10000101;

    while(1) {
        ADCSRA |= (1 << ADSC);
        // show the higher 8-bits of the 10-bit adc output
        PORTA = (unsigned char) adc_value >> 2;
    }
}
```

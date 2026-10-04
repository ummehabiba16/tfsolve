---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "ADMUX = 0b01000001 (AVCC 5 V, right adjusted, ADC1), ADCSRA = 0b11001010 (ADEN, ADSC, ADIE, prescaler 4); in ISR(ADC_vect): pressure = ADC x 100000 / 1024 Pa (97.66 Pa per count), then start the next conversion."
sources: ["EHP 6. AVR ADC slides 16, 20-27, 29-36 (ADMUX, ADCSRA, result formula, ADC interrupt example)"]
---
**Scaling.** 0-5 V corresponds to 0-$10^5$ Pa, and the 10-bit ADC with $V_{ref}$ = 5 V gives $ADC = V_{in} \times 1024/5$. So

$$\text{pressure} = \frac{V_{in}}{5} \times 10^5 = ADC \times \frac{10^5}{1024}\ \text{Pa} \approx ADC \times 97.66\ \text{Pa}$$

**Register values**

| Register | Value | Meaning |
|:--|:--|:--|
| ADMUX | 0b01000001 | REFS1:0 = 01 (5 V), ADLAR = 0 (right adjusted), MUX4:0 = 00001 (ADC1) |
| ADCSRA | 0b11001010 | ADEN = 1, ADSC = 1 (start), ADATE = 0, ADIF = 0, ADIE = 1 (interrupt), ADPS2:0 = 010 (/4) |

**Code**

```c
#include <avr/io.h>
#include <avr/interrupt.h>

volatile uint32_t pressure;              // in Pa

ISR(ADC_vect)                            // conversion complete
{
    uint16_t result = ADC;               // reads ADCL first, then ADCH
    pressure = (uint32_t)result * 100000UL / 1024;   // Pa
    ADCSRA |= (1 << ADSC);               // start the next conversion (continuous)
}

int main(void)
{
    DDRA &= ~(1 << PA1);                 // ADC1 (PA1) as input
    ADMUX  = 0b01000001;                 // 5 V reference, right adjust, ADC1
    ADCSRA = 0b11001010;                 // enable, start, interrupt, prescaler 4
    sei();                               // enable interrupts globally

    while (1) {
        // pressure is always up to date; other work can be done here
    }
}
```

*Notes:* the multiplication is done in 32 bits because $1023 \times 100000$ does not fit in 16 bits. With the 1 MHz default clock, prescaler 4 gives a 250 kHz ADC clock, a little above the 200 kHz recommended for full 10-bit accuracy, but it is the value the question specifies. Free-running mode (ADATE = 1) would also give continuous conversions without restarting in the ISR.

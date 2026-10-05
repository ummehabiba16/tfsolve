---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "0-5 V for 0-20 C with Vref 5 V: ADC = T x 51.2, so 4 C = 1.0 V = 204.8 and 10 C = 2.5 V = 512. ADMUX = 0x40 (AVCC, right adjust, ADC0), ADCSRA = 0x81 (enable, prescaler 2). Poll: start, wait for ADIF, read ADC; ADC < 205 -> heater (PB0) on, ADC > 512 -> cooler (PB1) on, else both off; after turning either on wait 20 s."
sources: ["EHP 6. AVR ADC slides 16, 20-33 (ADMUX, ADCSRA, polling example)", "EHP 6. AVR ADC slides 37-44 (temperature sensor with the ADC)"]
---
**Scaling.** The sensor gives 0-5 V for 0-20 °C, i.e. 0.25 V/°C. With $V_{ref}$ = 5 V and 10 bits,

$$ADC = \frac{V \times 1024}{5} = T \times \frac{0.25 \times 1024}{5} = 51.2\,T$$

| Temperature | Voltage | ADC |
|:-:|:-:|:-:|
| 4 °C | 1.0 V | 204.8 |
| 10 °C | 2.5 V | 512 |

So: **ADC < 205** (below 4 °C) $\to$ heater on; **ADC > 512** (above 10 °C) $\to$ cooler on; otherwise both off.

**Registers**

| Register | Value | Meaning |
|:--|:--|:--|
| ADMUX | 0b01000000 = 0x40 | REFS = 01 (5 V), ADLAR = 0 (right adjusted), MUX = 00000 (ADC0) |
| ADCSRA | 0b10000001 = 0x81 | ADEN = 1, ADSC = 0, ADATE = 0, ADIE = 0 (polling), ADPS = 001 (/2) |
| DDRB | 0b00000011 | PB0 heater, PB1 cooler |

**Code**

```c
#define F_CPU 1000000UL
#include <avr/io.h>
#include <util/delay.h>

uint16_t read_adc(void)
{
    ADCSRA |= (1 << ADSC);                 // start conversion
    while ((ADCSRA & (1 << ADIF)) == 0);   // poll until done
    ADCSRA |= (1 << ADIF);                 // clear ADIF (write 1)
    return ADC;                            // ADCL then ADCH
}

void wait_20s(void)
{
    for (uint8_t i = 0; i < 20; i++) _delay_ms(1000);
}

int main(void)
{
    uint16_t t;
    DDRB  = 0b00000011;          // PB0 = heater, PB1 = air cooler
    PORTB = 0x00;                // both off
    DDRA &= ~(1 << PA0);         // ADC0 input
    ADMUX  = 0x40;
    ADCSRA = 0x81;

    while (1) {
        t = read_adc();
        if (t < 205) {                       // below 4 C
            PORTB = (PORTB & ~0x02) | 0x01;  // heater on, cooler off
            wait_20s();
        } else if (t > 512) {                // above 10 C
            PORTB = (PORTB & ~0x01) | 0x02;  // cooler on, heater off
            wait_20s();
        } else {
            PORTB &= ~0x03;                  // within 4-10 C: both off
        }
    }
}
```

*Notes:* 1 MHz system clock is assumed (prescaler 2 gives a 500 kHz ADC clock, faster than the 200 kHz recommended for full accuracy, but it is the value the question specifies). The device that is on stays on until a later reading is back in range.

---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Sensor: 10 mV per degree. Vref = 5 V. (i) ADLAR = 1, read ADCH (8 bits): T = ADCH x 5/256/0.01 = ADCH x 500/256 (about 1.95 C per count). (ii) ADLAR = 0, read ADC (10 bits): T = ADC x 500/1024 (about 0.49 C per count). ADMUX = 0x60 or 0x40, ADCSRA = 0x81, poll ADIF."
sources: ["EHP 6. AVR ADC slides 20-33, 37-44 (ADMUX, ADCSRA, polling example, temperature sensor, reading only ADCH)"]
---
**Scaling.** 0-3.3 V for 0-330 °C is **10 mV/°C**, so $T = V/0.01$.

- 8-bit (ADCH only): $V = ADCH \times 5/256$, so $T = ADCH \times \dfrac{500}{256} \approx 1.953 \times ADCH$ °C.
- 10-bit: $V = ADC \times 5/1024$, so $T = ADC \times \dfrac{500}{1024} \approx 0.488 \times ADC$ °C.

| Register | (i) ADCH only | (ii) ADCH and ADCL |
|:--|:--|:--|
| ADMUX | 0b01100000 = 0x60 (REFS = 01, **ADLAR = 1**, ADC0) | 0b01000000 = 0x40 (REFS = 01, **ADLAR = 0**, ADC0) |
| ADCSRA | 0b10000001 = 0x81 (ADEN, prescaler 2, no interrupt) | same |

**(i) Reading only ADCH**

```c
#include <avr/io.h>

int main(void)
{
    float temperature;
    ADMUX  = 0x60;                         // 5 V ref, left adjusted, ADC0
    ADCSRA = 0x81;                         // enable, prescaler 2
    while (1) {
        ADCSRA |= (1 << ADSC);             // start conversion
        while (!(ADCSRA & (1 << ADIF)));   // poll
        ADCSRA |= (1 << ADIF);             // clear flag
        temperature = ADCH * 500.0 / 256;  // 8-bit result
    }
}
```

**(ii) Reading ADCL and ADCH**

```c
#include <avr/io.h>

int main(void)
{
    float temperature;
    uint16_t result;
    ADMUX  = 0x40;                         // 5 V ref, right adjusted, ADC0
    ADCSRA = 0x81;
    while (1) {
        ADCSRA |= (1 << ADSC);
        while (!(ADCSRA & (1 << ADIF)));
        ADCSRA |= (1 << ADIF);
        result  = ADCL;                    // ADCL first ...
        result |= (uint16_t)ADCH << 8;     // ... then ADCH
        temperature = result * 500.0 / 1024;
    }
}
```

The 10-bit version resolves about 0.49 °C instead of 1.95 °C. (The sensor's maximum of 3.3 V gives ADC $\approx$ 676 and ADCH $\approx$ 169, so 1/3 of the range is unused with a 5 V reference.)

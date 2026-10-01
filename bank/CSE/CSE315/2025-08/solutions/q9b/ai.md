---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Differential ADC3-ADC2, gain 10: ADMUX = 0b01101101 (AVCC 5V, left adjust, MUX 01101); ADCSRA = 0b10001100 (enable, interrupt, prescaler 16); read ADCL then ADCH in ISR(ADC_vect)."
sources: ["EHP 6. AVR ADC slides 20-36 (ADMUX, Vref, input source table, ADCH/ADCL, ADCSRA, prescaler, ADC interrupt example)"]
---
**Step 1: configure the ADC** (following the slide checklist)

- **ADC source:** voltage difference PA3 $-$ PA2, gain 10. From the MUX table, ADC3 (+) and ADC2 ($-$) with 10x is **MUX4:0 = 01101**.
- **Reference voltage:** 5 V, so AVCC with an external capacitor at AREF: **REFS1:0 = 01**.
- **Align:** left justified: **ADLAR = 1**.
- **Auto-trigger:** disable (ADATE = 0). **ADC interrupt:** enable (ADIE = 1).
- **Prescaler:** 16, so ADPS2:0 = 100. The ADC clock is 1 MHz / 16 = 62.5 kHz.

| Register | Bits | Value |
|:--|:--|:-:|
| ADMUX | REFS1 REFS0 ADLAR MUX4..MUX0 = 0 1 1 0 1 1 0 1 | 0b01101101 |
| ADCSRA | ADEN ADSC ADATE ADIF ADIE ADPS2..0 = 1 0 0 0 1 1 0 0 | 0b10001100 |

Assumptions: AVCC = 5 V with a capacitor on AREF; PA2 and PA3 are inputs (DDRA bits 2, 3 = 0). The top 8 bits of the result are also shown on 8 LEDs on PORT B.

**Steps 2 and 3: start the conversion, read the result in the ISR**

```c
#include <avr/io.h>
#include <avr/interrupt.h>

volatile int16_t result;            // 10-bit signed difference

ISR(ADC_vect){
    uint8_t low  = ADCL;            // read ADCL first
    uint8_t high = ADCH;            // then ADCH
    // left adjusted: D9..D2 in ADCH, D1..D0 in ADCL[7:6]
    result = ((int16_t)((high << 8) | low)) >> 6;  // two's complement, -512..+511
    PORTB = high;                   // show top 8 bits on LEDs
    ADCSRA |= (1 << ADSC);          // start next conversion
}

int main(void){
    DDRA = 0x00;                    // PA2, PA3 as input
    DDRB = 0xFF;                    // LEDs

    // REFS1:0 = 01 -> AVCC (5 V) as reference
    // ADLAR   = 1  -> left adjust
    // MUX4:0  = 01101 -> ADC3(+) - ADC2(-), gain 10x
    ADMUX = 0b01101101;

    // ADEN = 1: enable ADC, ADSC = 0, ADATE = 0
    // ADIE = 1: enable ADC interrupt
    // ADPS2:0 = 100: prescaler 16
    ADCSRA = 0b10001100;

    sei();                          // enable interrupts globally
    ADCSRA |= (1 << ADSC);          // start the first conversion

    while(1){
        // other work; result is updated by the ISR
    }
}
```

The differential result is in two's complement (0x200 = $-512$ to 0x1FF = $+511$):

$$ADC = \frac{(V_{PA3}-V_{PA2})\times 10\times 512}{5\text{ V}}$$

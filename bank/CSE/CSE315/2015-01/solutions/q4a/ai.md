---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "ADMUX = 0b00000000 (REFS = 00: external AREF, right adjusted, ADC0). ADCSRA = 0b11001011 (ADEN, ADSC, ADIE, prescaler 8). ISR(ADC_vect): PORTA = ADCL (low 8 bits), PORTB = ADCH (bits 9-8), then start the next conversion; DDRA = DDRB = 0xFF; sei()."
sources: ["EHP 6. AVR ADC slides 20-36 (ADMUX reference selection, ADCSRA, interrupt-driven ADC example)"]
---
**Register values**

| Register | Value | Meaning |
|:--|:--|:--|
| ADMUX | 0b00000000 | REFS1:0 = 00: **external voltage on AREF**; ADLAR = 0 (right adjusted); MUX4:0 = 00000: **ADC0** |
| ADCSRA | 0b11001011 | ADEN = 1, ADSC = 1 (start), ADATE = 0, ADIF = 0, **ADIE = 1** (interrupt), ADPS2:0 = 011 (prescaler 8: 125 kHz at 1 MHz) |

The 10-bit result is shown with the low 8 bits (ADCL) on PORTA and the upper 2 bits (ADCH) on PORTB.

```c
#include <avr/io.h>
#include <avr/interrupt.h>

ISR(ADC_vect)                    // conversion complete
{
    PORTA = ADCL;                // bits 7-0 (read ADCL first)
    PORTB = ADCH;                // bits 9-8
    ADCSRA |= (1 << ADSC);       // start the next conversion
}

int main(void)
{
    DDRA = 0xFF;                 // PORTA output (as the question asks; see note)
    DDRB = 0xFF;                 // PORTB output
    ADMUX  = 0b00000000;         // AREF, right adjust, ADC0
    ADCSRA = 0b11001011;         // enable, start, interrupt, /8
    sei();                       // enable interrupts globally
    while (1);                   // CPU free for other work
}
```

**Important note on pins:** on the ATmega16/32 the ADC inputs are Port A pins (ADC0 = PA0). Making all of PORTA an output, as the question asks, drives PA0 and spoils the ADC0 input. In a real circuit the low byte should go to another port, e.g. replace `DDRA = 0xFF; PORTA = ADCL;` by `DDRC = 0xFF; PORTC = ADCL;` (and keep DDRA bit 0 = 0). Assumptions: 1 MHz clock and a reference voltage connected to AREF.

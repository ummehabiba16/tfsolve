---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Issues: wrong reference (REFS = 11 is internal 2.56 V; need 00 with 4 V on AREF), wrong channel (MUX 00000, need 00101), ADIE not set, prescaler 32 not 8, no sei(), adc_value not volatile, ADCH read before ADCL, cast applied before the shift, and LEDs on PORTA clash with ADC5 (PA5)."
sources: ["EHP 6. AVR ADC slides 20-36 (ADMUX, Vref, MUX table, ADCH/ADCL read order, ADCSRA, prescaler, interrupt example)", "EHP ATmega32 Interrupt slides 13, 27-29 (sei, volatile)"]
---
| Line | Issue | Fix |
|:--|:--|:--|
| 12 | REFS1:0 = 11 selects the **internal 2.56 V** reference, but Vref must be **4.0 V**. That can only come from an external voltage on AREF. | REFS1:0 = **00** (AREF, internal Vref off), with 4.0 V applied to AREF |
| 12 | MUX4:0 = 00000 selects **ADC0**, but the signal is on **ADC5**. | MUX4:0 = **00101** |
| 12 | ADLAR = 1 (left justified) is correct. | `ADMUX = 0b00100101;` |
| 13 | ADCSRA = 1000 0101: **ADIE = 0**, so the ADC interrupt is never generated and the ISR never runs. | ADIE = 1 |
| 13 | ADPS2:0 = 101 is a prescaler of **32**, but it must be **8**. | ADPS2:0 = 011, giving `ADCSRA = 0b10001011;` (ADC clock 1 MHz / 8 = 125 kHz) |
| (missing) | No `sei()`, so global interrupts are disabled and the ISR cannot run. | add `sei();` before the loop |
| 4 | `adc_value` is shared between the ISR and main but is not `volatile`, so the compiler may keep a stale copy in the loop. | `volatile uint16_t adc_value;` |
| 7 | `(ADCH << 2) \| (ADCL >> 6)`: C does not fix which operand is read first. **ADCL must be read before ADCH**, otherwise the registers can come from different conversions or block the update. | read `ADCL` into a variable first, then `ADCH` |
| 11, 18 | **ADC5 is pin PA5**, but `DDRA = 0xFF` makes all of PORT A outputs, and PORTA drives the LEDs. PA5 is then driven by the LED value and cannot sense the analogue signal. | connect the LEDs to another port, e.g. PORT B, and keep PA5 as input |
| 18 | `(unsigned char) adc_value >> 2`: the cast is applied **first**, so the low 8 bits are kept and then shifted. The result is not the higher 8 bits. | `(unsigned char)(adc_value >> 2)`, or simply use ADCH |
| 16 | ADSC is set again on every pass of the loop, even while a conversion is running. | start the next conversion from the ISR (or once before the loop) |

**Corrected code**

```c
#include <avr/io.h>
#include <avr/interrupt.h>

volatile uint16_t adc_value;          // shared with ISR

ISR(ADC_vect) {
    uint8_t low  = ADCL;              // ADCL first
    uint8_t high = ADCH;              // then ADCH
    adc_value = ((uint16_t)high << 2) | (low >> 6);
    ADCSRA |= (1 << ADSC);            // next conversion
}

int main(void) {
    DDRB = 0xFF;                      // LEDs on PORT B
    DDRA = 0x00;                      // PA5 = ADC5 input
    ADMUX  = 0b00100101;              // AREF (4.0 V), left adjust, ADC5
    ADCSRA = 0b10001011;              // ADEN, ADIE, prescaler 8
    sei();
    ADCSRA |= (1 << ADSC);            // first conversion

    while(1) {
        // show the higher 8-bits of the 10-bit adc output
        PORTB = (unsigned char)(adc_value >> 2);
    }
}
```

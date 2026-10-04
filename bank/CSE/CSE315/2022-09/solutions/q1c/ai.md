---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "S (digital 0/5 V) on INT0 (PD2), T (analog) on ADC0 (PA0), LED on PB0. INT0 on any change starts an ADC conversion only when smoke appears; the ADC interrupt turns the LED on if ADC > 716 (70 C = 3.5 V with AVCC = 5 V) and repeats while smoke lasts; the CPU sleeps (idle) otherwise."
sources: ["EHP 6. AVR ADC slides 16, 20-36 (single-ended ADC, ADMUX, ADCSRA, ADC interrupt example)", "EHP ATmega32 Interrupt slides 13-23 (INT0, MCUCR, GICR)", "ATmega32 datasheet, Power Management and Sleep Modes (idle mode)"]
---
**i. Circuit**

```text
                         ATmega32
                  +----------------------+
 Smoke sensor S   |                      |
  out (0 / 5 V) ->| PD2 (INT0)           |
                  |                      |
 Temp sensor T    |                 PB0  |---[330R]---|>|--- GND
  out (0-5 V) --->| PA0 (ADC0)           |              LED
                  |                      |
         +5 V --->| AVCC, AREF via 100nF |
                  | VCC, GND             |
                  +----------------------+
 (both sensors also connected to +5 V and GND for power)
```

- S is a **digital** signal (0 V or 5 V), so it goes to an external interrupt pin, **INT0 (PD2)**, instead of being polled.
- T is **analog**, so it goes to an ADC channel, **ADC0 (PA0)**.
- The LED (with a series resistor) is on **PB0**.

**Threshold.** T gives 0-5 V for 0-100 °C, i.e. 50 mV/°C, so 70 °C = 3.5 V. With $V_{ref}$ = AVCC = 5 V:

$$ADC_{70} = \frac{3.5 \times 1024}{5} = 716.8$$

The temperature is above 70 °C when **ADC > 716**.

**Energy-efficient design**

- No polling loop: the smoke sensor wakes the CPU through **INT0**.
- The ADC is started **only while smoke is present**. With no smoke the temperature is never measured.
- Between interrupts the CPU sleeps in **idle mode**.

**ii. Code**

```c
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>

#define T70 716                       // 3.5 V -> 716.8 counts (AVCC = 5 V)

ISR(INT0_vect)                        // smoke sensor changed
{
    if (PIND & (1 << PD2))            // smoke appeared (0 V -> 5 V)
        ADCSRA |= (1 << ADSC);        // measure the temperature
    else                              // smoke gone
        PORTB &= ~(1 << PB0);         // LED off, ADC stays idle
}

ISR(ADC_vect)                         // temperature conversion finished
{
    uint16_t t = ADC;                 // reads ADCL then ADCH
    if ((PIND & (1 << PD2)) && t > T70)
        PORTB |= (1 << PB0);          // smoke AND above 70 C: LED on
    else
        PORTB &= ~(1 << PB0);
    if (PIND & (1 << PD2))            // keep watching temperature only while smoke lasts
        ADCSRA |= (1 << ADSC);
}

int main(void)
{
    DDRB |=  (1 << PB0);              // LED output
    DDRD &= ~(1 << PD2);              // S input
    DDRA &= ~(1 << PA0);              // T input (ADC0)

    ADMUX  = 0b01000000;              // REFS = 01 (AVCC), ADLAR = 0, MUX = 00000 (ADC0)
    ADCSRA = 0b10001011;              // ADEN = 1, ADIE = 1, prescaler 8 (125 kHz at 1 MHz)

    MCUCR = (MCUCR & 0b11111100) | (1 << ISC00);   // INT0 on any logical change
    GICR  = (1 << INT0);              // enable INT0

    set_sleep_mode(SLEEP_MODE_IDLE);
    sei();
    if (PIND & (1 << PD2))            // smoke already present at power-up
        ADCSRA |= (1 << ADSC);

    while (1)
        sleep_mode();                 // sleep until INT0 or ADC interrupt
}
```

*Notes:* assumptions are AVCC = AREF = 5 V, 1 MHz clock and an active-high LED. Idle mode is used because INT0 on an edge can wake the CPU from it and the ADC keeps running. ADC noise reduction mode would also work for the ADC but needs a level interrupt on INT0 to wake up.

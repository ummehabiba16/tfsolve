---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) Auto-trigger mode: the conversion must start at an exact instant, because the voltage lasts only briefly; software start or free running cannot guarantee it. (ii) Timer0 in CTC with OCR0 = 199 (1 MHz, no prescaler) gives a compare match every 200 us; ADC prescaler 8 (13.5 x 8 = 108 us < 200 us). (iii) Timer/Counter0 compare match (ADTS2:0 = 011). (iv) Three ISRs: TIMER0_COMP (clears OCF0 so the next match can trigger), ADC (store the result, put it in the transmit buffer, enable UDRIE), USART_UDRE (send buffered bytes, disable UDRIE when empty). (v) Configure ADMUX, ADCSRA, SFIOR, TCCR0/OCR0/TIMSK, UCSRA/B/C/UBRR, sei()."
sources: ["EHP 6. AVR ADC slides 45-55 (auto trigger, SFIOR, Timer0 compare match sampling, ADC prescaler choice)", "EHP Serial Communication slides 64-68 (UDRE interrupt-driven transmission)"]
---
**(i) ADC mode: auto-trigger mode.** The analog value is present only for a very short time, every 200 µs, so the conversion must start at **exactly** the right instant. A software start (single conversion) depends on program timing, and free-running mode runs at its own rate (13 ADC clocks), not locked to 200 µs. In **auto-trigger mode** a hardware event starts each conversion, so the sample-and-hold captures the input at precise times without CPU involvement.

**(ii) Sampling exactly every 200 µs.** Use **Timer0 in CTC mode**: at 1 MHz with no prescaler (1 µs per tick), a compare match every 200 µs needs 200 counts:

$$OCR0 = 200 - 1 = 199$$

Each compare match triggers one conversion. The conversion must finish before the next trigger: an auto-triggered conversion takes 13.5 ADC clocks, so the ADC clock period must be $\le 200/13.5 = 14.8$ µs. **ADC prescaler 8** (125 kHz, 8 µs) gives $13.5 \times 8 = 108$ µs < 200 µs (prescaler 16 would need 216 µs, too long).

**(iii) Triggering event:** the **Timer/Counter0 compare match** (OCF0 rising), selected by **ADTS2:0 = 011** in SFIOR.

**(iv) ISRs (no polling anywhere): three**

1. **`TIMER0_COMP_vect`:** entering it clears OCF0. The ADC is triggered by the *rising edge* of the flag, so the flag must be cleared for the next match to trigger again. (Can be empty.)
2. **`ADC_vect`:** runs when a conversion completes: reads the result (ADCL then ADCH, or ADCH only if 8 bits are enough), stores it in a transmit buffer and enables the UDRE interrupt.
3. **`USART_UDRE_vect`:** sends the next byte from the buffer by writing UDR; when the buffer is empty it disables UDRIE (otherwise it would fire continuously).

**(v) Configuration steps**

| Step | Register | Action |
|:-:|:--|:--|
| 1 | ADMUX | REFS1:0 (e.g. 01 = AVCC), ADLAR (1 if only ADCH is sent), MUX4:0 = input channel (e.g. 00000 = ADC0) |
| 2 | SFIOR | ADTS2:0 = 011: trigger = Timer0 compare match |
| 3 | ADCSRA | ADEN = 1, ADATE = 1 (auto trigger), ADIE = 1, ADPS2:0 = 011 (prescaler 8) |
| 4 | TCCR0, OCR0 | CTC mode (WGM01:00 = 10), no prescaler (CS02:00 = 001); OCR0 = 199 |
| 5 | TIMSK | OCIE0 = 1 (compare match interrupt, to clear OCF0) |
| 6 | UBRRH/UBRRL, UCSRA | baud rate (fast enough: one 10-bit frame per sample needs > 50 kbps, e.g. U2X = 1 with UBRR = 1: 62.5 kbps at 1 MHz) |
| 7 | UCSRC | URSEL = 1, async, no parity, 1 stop, 8 data bits (0x86) |
| 8 | UCSRB | TXEN = 1 (UDRIE is enabled by the ADC ISR when data is ready) |
| 9 | SREG | `sei()` to enable interrupts globally; then the main loop can sleep (idle) |

*Note:* sending a 10-bit result as 2 bytes every 200 µs would need about 100 kbps, which is not reachable accurately at a 1 MHz clock, so 8-bit results (ADLAR = 1, ADCH) are assumed.

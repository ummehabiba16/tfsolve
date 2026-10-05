---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Taking 20 kHz (50 us between samples): run Timer0 in CTC mode and let its compare match auto-trigger the ADC (ADCSRA: ADEN, ADATE, ADIE, prescaler; SFIOR: ADTS2:0 = 011; ADMUX: reference/channel). OCR0 = 50 us / (8/16 MHz) - 1 = 99. Auto-triggered conversion = 13.5 ADC clocks <= 50 us, so ADC clock >= 270 kHz: largest prescaler is 32 (500 kHz, 27 us). Two ISRs: TIMER0_COMP_vect (clears OCF0 so the next match re-triggers) and ADC_vect (read and store the result)."
sources: ["EHP 6. AVR ADC slides 45-55 (SFIOR, auto trigger logic and sources, Timer0 CTC for 20 kHz sampling, OCR0 = 99, ADC prescaler 32)"]
---
*Note:* the paper prints "20000 kHz"; 20 MHz sampling is far beyond the ATmega32 ADC (about 15 kSPS at full resolution), so **20 kHz** is assumed, as in the slide example with the same 16 MHz clock and Timer0 prescaler 8.

**(i) Using the Timer0 compare match**

- Run **Timer0 in CTC mode** so that a **compare match** happens exactly every sampling period (50 µs).
- Use the ADC's **auto-trigger** feature: the rising edge of the Timer0 compare-match flag (OCF0) starts a conversion in hardware, so the sampling instants are exact and do not depend on software timing.

Registers to configure:

| Register | Setting |
|:--|:--|
| ADMUX | reference voltage (REFS1:0), result adjustment (ADLAR), input channel (MUX4:0) |
| ADCSRA | ADEN = 1, **ADATE = 1** (auto trigger), ADIE = 1 (interrupt at end of conversion), ADPS2:0 = prescaler |
| SFIOR | **ADTS2:0 = 011**: trigger source = Timer/Counter0 compare match |
| TCCR0, OCR0 | Timer0 CTC mode, prescaler 8, OCR0 (below) |

**(ii) OCR0**

Timer0 tick $= 8/16\ \text{MHz} = 0.5\ \mu s$. Sampling period $= 1/20\ \text{kHz} = 50\ \mu s$:

$$\frac{50\ \mu s}{0.5\ \mu s} = 100\ \text{counts (0 to 99)} \ \Rightarrow\ OCR0 = \mathbf{99}$$

(99, not 100, because in CTC mode the counter goes 0, 1, ..., OCR0, i.e. OCR0 + 1 counts per period.)

**(iii) Optimal ADC prescaler**

An auto-triggered conversion takes **13.5 ADC clock cycles**, and it must finish within one sampling period (50 µs), leaving time to store the result:

$$13.5 \times \frac{N}{16\ \text{MHz}} \le 50\ \mu s \ \Rightarrow\ N \le 59.3$$

The available prescalers are 2, 4, 8, 16, 32, 64, 128. The **largest** that fits (slowest ADC clock, so best accuracy) is **N = 32**: ADC clock 500 kHz, conversion $13.5 \times 2\ \mu s = 27\ \mu s < 50\ \mu s$. (N = 64 would need 54 µs, too long.)

**(iv) ISRs: two**

1. **TIMER0_COMP_vect.** The ADC is triggered by the **rising edge** of OCF0. If the flag is not cleared, it stays 1 and there is no new rising edge, so only one conversion would happen. Entering this ISR clears OCF0 in hardware, so the ISR can be empty.
2. **ADC_vect.** Runs when a conversion is complete: reads the result (ADCL then ADCH, or ADCH only) and stores it in a buffer. ADIF is cleared on entry.

```text
 TIMER0_COMP_vect               ADC_vect
 +------------------+           +---------------------------+
 | enter: hardware  |           | enter: ADIF cleared       |
 | clears OCF0      |           +-------------+-------------+
 +--------+---------+                         v
          v                     +---------------------------+
 +------------------+           | result <- ADC (ADCL, ADCH)|
 | (nothing else)   |           +-------------+-------------+
 +--------+---------+                         v
          v                     +---------------------------+
 +------------------+           | buffer[i++] <- result     |
 |      RETI        |           | (wrap i at buffer size)   |
 +------------------+           +-------------+-------------+
                                              v
                                +---------------------------+
                                |          RETI             |
                                +---------------------------+
```

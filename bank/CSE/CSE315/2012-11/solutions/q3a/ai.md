---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "1 MHz, no prescaler (1 us ticks). CTC: WGM = 0100, toggle OC1A (COM1A = 01), OCR1A = 499 (toggle every 500 us): TCCR1A = 0x40, TCCR1B = 0x09. Fast PWM: WGM = 1110, ICR1 = 999, OCR1A = 499, COM1A = 10: TCCR1A = 0x82, TCCR1B = 0x19. Phase correct PWM: WGM = 1010, ICR1 = 500 (period 2 x 500 us), OCR1A = 250, COM1A = 10: TCCR1A = 0x82, TCCR1B = 0x11."
sources: ["EHP Timer_Part_2 slides 22-52 (CTC, fast PWM and phase correct PWM, custom waveform with ICR1/OCR1A)", "ATmega32 datasheet, Timer/Counter1 waveform generation formulas"]
---
Target: period 1000 µs, duty 50%. At 1 MHz with no prescaler, one tick = 1 µs. OC1A (PD5) must be an output: `DDRD |= (1 << PD5);`.

| Mode | WGM13:10 | TOP | Compare value | COM1A1:0 | TCCR1A | TCCR1B |
|:--|:-:|:--|:--|:-:|:-:|:-:|
| CTC | 0100 | OCR1A = **499** | (same) | 01 toggle | 0b01000000 = 0x40 | 0b00001001 = 0x09 |
| Fast PWM | 1110 | ICR1 = **999** | OCR1A = **499** | 10 non-inverting | 0b10000010 = 0x82 | 0b00011001 = 0x19 |
| Phase correct PWM | 1010 | ICR1 = **500** | OCR1A = **250** | 10 non-inverting | 0b10000010 = 0x82 | 0b00010001 = 0x11 |

**CTC:** TCNT1 counts 0-499 (500 µs) and is cleared; OC1A toggles at each match, so it is high 500 µs and low 500 µs: $f = 10^6/(2 \times 500) = 1$ kHz, 50%.

**Fast PWM:** TCNT1 counts 0-999 (1000 µs period); OC1A is set at BOTTOM and cleared at the match with 499, so it is high for 500 counts: 50%.

**Phase correct PWM:** TCNT1 counts 0 $\to$ 500 $\to$ 0, so the period is $2 \times 500 = 1000$ µs; OC1A is high while TCNT1 < 250, i.e. 2 $\times$ 250 = 500 µs: 50%.

```text
CTC (TOP = OCR1A = 499, toggle):
   499|                  **                  **                  **                  **
      |             *****               *****               *****               *****
      |        *****               *****               *****               *****
      |   *****               *****               *****               *****
     0|***                 ***                 ***                 ***                 *
OC1A 1|                    --------------------                    --------------------
     0|--------------------                    --------------------                    -

Fast PWM (TOP = ICR1 = 999, OCR1A = 499):
   999|                                   *****                                   *****
      |                         **********                              **********
   499|               **********                              **********
      |     **********                              **********
     0|*****                                   *****                                   *
OC1A 1|--------------------                    --------------------                    -
     0|                    --------------------                    --------------------

Phase correct PWM (TOP = ICR1 = 500, OCR1A = 250):
   500|                  *****                                   *****
      |             *****     *****                         *****     *****
   250|        *****               *****               *****               *****
      |   *****                         *****     *****                         *****
     0|***                                   *****                                   ***
OC1A 1|----------                     -------------------                     ----------
     0|          ---------------------                   ---------------------
       (1 column = 25 us; period 1000 us in all three)
```

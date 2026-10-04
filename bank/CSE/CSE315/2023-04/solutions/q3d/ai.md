---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "CTC with TOP = OCR1A = 32768, tick = 64 us: one timer cycle = 32769 x 64 us = 2.097 s; both pins toggle once per cycle, so both have period 4.194 s, f = 0.2384 Hz and 50% duty; OC1B (toggles at 15625, t = 1.0 s) leads OC1A (toggles at 32768, t = 2.097 s) by 1.097 s."
sources: ["EHP Timer_Part_2 slides 27-30 (CTC mode, OCR1A = 15625 / OCR1B = 7812 toggle example)", "ATmega32 datasheet, Timer/Counter1, CTC Mode (f = fclk / (2 N (1 + OCR1A)))"]
---
**Setup.** WGM = 0100 is **CTC mode with TOP = OCR1A = 32768**: TCNT1 counts 0, 1, ..., 32768 and is cleared to 0 on the match with OCR1A. Both OC1A and OC1B **toggle** on their compare match.

Assumption: system clock 1 MHz (paper default). Prescaler 64 gives

$$t_{tick} = \frac{64}{1\ \text{MHz}} = 64\ \mu s$$

One timer cycle (0 to 32768) is $32768 + 1 = 32769$ ticks:

$$T_{cycle} = 32769 \times 64\ \mu s = 2\,097\,216\ \mu s \approx 2.097\ \text{s}$$

**Wave shapes** (both pins start low, TCNT1 = 0 at t = 0)

- OC1B toggles every time TCNT1 = 15625: at $t = 15625 \times 64\ \mu s = 1.000$ s, then every 2.097 s (3.097 s, 5.195 s, ...).
- OC1A toggles every time TCNT1 = 32768 (TOP): at $t = 32768 \times 64\ \mu s = 2.097$ s, then every 2.097 s (4.194 s, 6.292 s, ...).

```text
TCNT1                                   (1 column = 0.15 s)
32768 |             *             *             *             *
      |           **            **            **            **
      |         **            **            **            **
15625 |      ***           ***           ***           ***
      |    **            **            **            **
      |  **            **            **            **
    0 |**            **            **            **            **
OC1B 1|       --------------              --------------
     0|-------              --------------              ---------
OC1A 1|              --------------              --------------
     0|--------------              --------------              --
       0      1.0    2.097  3.1    4.194  5.2    6.29   7.3      t (s)
```

**Frequency and duty cycle**

Each pin toggles **once per timer cycle**, so a full period (high + low) is two timer cycles:

$$T_{OC1A} = T_{OC1B} = 2 \times 32769 \times 64\ \mu s = 4.194\ \text{s}$$

$$f_{OC1A} = f_{OC1B} = \frac{f_{clk}}{2\,N\,(1 + OCR1A)} = \frac{10^6}{2 \times 64 \times 32769} = \mathbf{0.2384\ Hz}$$

Each pin is high for one timer cycle and low for one timer cycle, so

$$D_{OC1A} = D_{OC1B} = \frac{2.097}{4.194} = \mathbf{50\%}$$

OCR1B does **not** change the frequency or the duty cycle of OC1B (TOP is set only by OCR1A); it only sets the **phase**: OC1B leads OC1A by $(32768 - 15625) \times 64\ \mu s = 1.097$ s, about $94^\circ$.

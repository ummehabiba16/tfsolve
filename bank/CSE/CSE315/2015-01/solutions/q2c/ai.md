---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "32 kHz square wave: period 31.25 us, the pin is toggled every half period = 15.625 us. At 8 MHz without prescaler one count = 0.125 us, so 15.625/0.125 = 125 counts: TCNT0 = 256 - 125 = 131 = 0x83 (reloaded after each overflow)."
sources: ["EHP Timer_Part_1 slides 7, 22-27 (normal mode, overflow, delay calculation)", "Mazidi, AVR Microcontroller and Embedded Systems, Ch. 9 (Timer0 square wave by toggling on overflow)"]
---
A 32 kHz square wave is made by **toggling** an output pin every **half period** with the Timer0 overflow.

$$T = \frac{1}{32\ \text{kHz}} = 31.25\ \mu s, \qquad \frac{T}{2} = 15.625\ \mu s$$

With an 8 MHz clock and no prescaler, one timer count takes

$$t_{count} = \frac{1}{8\ \text{MHz}} = 0.125\ \mu s$$

$$\text{counts per half period} = \frac{15.625\ \mu s}{0.125\ \mu s} = 125$$

Timer0 is 8-bit and overflows when it rolls over from 255 to 0 (256 counts from 0), so to overflow after 125 counts:

$$TCNT0 = 256 - 125 = 131 = \mathbf{0x83}$$

**Use:** TCCR0 = 0x01 (normal mode, no prescaler); load TCNT0 = 0x83; on each overflow (TOV0) toggle the pin, clear TOV0 and reload TCNT0 = 0x83.

```c
DDRB |= (1 << PB0);
while (1) {
    TCNT0 = 0x83;                    // 125 counts
    TCCR0 = 0x01;                    // normal mode, no prescaler
    while (!(TIFR & (1 << TOV0)));   // wait 15.625 us
    TCCR0 = 0;                       // stop
    TIFR  = (1 << TOV0);             // clear flag
    PORTB ^= (1 << PB0);             // toggle: 32 kHz square wave
}
```

(The few instruction cycles for reloading make the real frequency slightly lower; they are ignored here. If the timer were reloaded only once per full period, TCNT0 would be 256 - 250 = 6.)

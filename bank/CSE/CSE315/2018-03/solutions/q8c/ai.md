---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Set the mode in SM2:0 (000 idle, 001 ADC noise reduction, 010 power-down, 011 power-save, 110 standby, 111 extended standby) and SE = 1 in MCUCR, then execute SLEEP; the clocks of unused modules stop, and an enabled interrupt (or reset) wakes the MCU, which runs the ISR and continues after SLEEP."
sources: ["ATmega32 datasheet, Power Management and Sleep Modes (MCUCR SE, SM2:0, wake-up sources)", "EHP Intro to micro slide 5 (emphasis on power consumption)"]
---
**How sleep works.** To save power the ATmega32 can stop its CPU clock (and, depending on the mode, other clocks) with the `SLEEP` instruction:

1. Choose a mode with **SM2:0** in MCUCR and set **SE** (sleep enable) = 1.
2. Execute `SLEEP`. The CPU stops; the modules still clocked in that mode keep working.
3. An enabled interrupt (or reset) **wakes** the MCU: it is halted 4 cycles (plus start-up time in deep modes), runs the ISR, then continues with the instruction after `SLEEP`. SE should be cleared after waking to avoid accidental sleep.

| SM2:0 | Mode | Still running / wake-up sources |
|:-:|:--|:--|
| 000 | Idle | timers, USART, SPI, ADC, interrupts; any interrupt wakes |
| 001 | ADC noise reduction | ADC, timer 2, external interrupts; ADC conversion complete wakes |
| 010 | Power-down | only external level interrupts, INT2, TWI address match, watchdog |
| 011 | Power-save | as power-down plus asynchronous timer 2 |
| 110 | Standby | power-down with the oscillator kept running (fast wake-up) |
| 111 | Extended standby | power-save with the oscillator kept running |

**Example:** toggle LEDs on every press of a button on INT0, sleeping in power-down between presses.

```c
#include <avr/io.h>
#include <avr/interrupt.h>

ISR(INT0_vect) {                     // wakes the MCU
    PORTB = ~PORTB;
}

int main(void) {
    DDRB  = 0xFF;
    PORTD |= (1 << PD2);             // pull-up on INT0
    MCUCR &= ~((1 << ISC01) | (1 << ISC00));   // low level (can wake from power-down)
    GICR  = (1 << INT0);
    sei();

    while (1) {
        MCUCR = (MCUCR & 0x0F) | (1 << SE) | (1 << SM1);  // SE = 1, SM2:0 = 010 power-down
        asm volatile ("sleep");       // CPU stops here until INT0
        MCUCR &= ~(1 << SE);          // clear SE after waking
    }
}
```

*Note:* only a **level** interrupt on INT0 can wake the MCU from power-down, so the ISR repeats while the button is held; a real program would wait for release (or disable INT0) inside the ISR.

(The avr-libc macros `set_sleep_mode(SLEEP_MODE_PWR_DOWN); sleep_mode();` do the same steps.)

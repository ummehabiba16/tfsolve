---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "When the button is not pressed the input is floating (connected to nothing), so it reads random 0/1. Fix 1: external pull-up resistor (about 10 k) from the pin to Vcc. Fix 2: internal pull-up: DDRx bit = 0 and PORTx bit = 1. Then the pin reads 1 when released and 0 when pressed (active low)."
sources: ["EHP ATMega32 Basic IO slides 28-36 (problem with the button connection, pull-up resistors, internal pull-up)"]
---
**What is wrong.** When the button is **pressed**, the microcontroller pin is connected to ground and reads 0. When the button is **released**, the pin is connected to **nothing**: it is **floating**. A high-impedance CMOS input picks up noise, so its level is undefined and may read 0 or 1 at random. The program cannot reliably tell "not pressed".

**Way 1: external pull-up resistor**

```text
        Vcc
         |
        [R]  ~10 k
         |
 pin ----+-----o  o----- GND
                button
```

Released: R pulls the pin to Vcc, so it reads **1**. Pressed: the pin is grounded and reads **0** (a small current Vcc/R flows). R must be neither too small (wasted current) nor too large (weak, noisy high level).

**Way 2: internal pull-up resistor of the ATmega16/32**

Configure the pin as an input and write 1 to its PORT bit; this switches on the internal pull-up (about 20-50 k$\Omega$):

```c
DDRA  &= ~(1 << PA0);   // input
PORTA |=  (1 << PA0);   // enable internal pull-up
...
if (!(PINA & (1 << PA0))) { /* pressed (active low) */ }
```

No extra component is needed. In both cases the button becomes **active low**.

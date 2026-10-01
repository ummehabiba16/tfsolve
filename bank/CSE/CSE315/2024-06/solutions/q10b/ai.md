---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Active-low: switch to GND with a pull-up resistor to Vcc (reads 1 when released, 0 when pressed). Active-high: switch to Vcc with a pull-down to GND (reads 0 when released, 1 when pressed)."
sources: ["EHP ATMega32 Basic IO slides 28-36 (push buttons, pull-up, pull-down, internal pull-up)"]
---
```text
  Active-low (pull-up)              Active-high (pull-down)

       +5V                                +5V
        |                                  |
       [R] pull-up (or internal)           o
        |                                   \  push button
        +-------> to MCU pin (e.g. PD2)    o
        |                                  |
        o                                  +-------> to MCU pin (e.g. PD3)
         \  push button                    |
        o                                 [R] pull-down (4.7k)
        |                                  |
       GND                                GND
```

**Difference in function:**

| | Active-low | Active-high |
|:--|:--|:--|
| Not pressed | pin pulled **high** by the pull-up, reads 1 | pin pulled **low** by the pull-down, reads 0 |
| Pressed | pin connected to GND, reads **0** | pin connected to Vcc, reads **1** |
| Press / release edge | press = falling edge, release = rising edge | press = rising edge, release = falling edge |
| Resistor | to Vcc; the ATmega32 internal pull-up can be used (DDRxn = 0, PORTxn = 1) | external resistor to GND (no internal pull-down) |

In both circuits the resistor prevents a **floating** input when the switch is open, and limits the current when it is closed.

---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "To give input pins a defined logic level: an open switch leaves the pin floating (reads random 0/1); a pull-up/pull-down fixes the idle level and limits current when the switch closes."
sources: ["EHP ATMega32 Basic IO slides 28-37 (push buttons, pull-up/pull-down, internal pull-up, unused pins)"]
---
- A push button connected only between the input pin and GND (or Vcc) defines the pin's level **only while it is pressed**. When it is open, the pin is connected to nothing: it is **floating**. Because the input has very high impedance, it picks up noise and may read 0 or 1 randomly.
- A **pull-up resistor** (to Vcc) or a **pull-down resistor** (to GND) gives the pin a **defined default level** when the switch is open: 1 with a pull-up, 0 with a pull-down. Pressing the switch overrides it.
- The resistor also **limits the current** from Vcc to GND when the switch is closed. A direct connection would be a short circuit. Its value is a trade-off: too small wastes current, too large makes the level weak and slow.
- The ATmega32 has **internal pull-ups**: write PORTxn = 1 with DDRxn = 0. They are also recommended on unused pins so that they have a defined level.

---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) After Timer1 overflow number 61 (ovfCount reaches 60 and one more overflow sets sleepNow), about 61 x 65.536 ms = 4.0 s at 1 MHz; ovfCount is never reset, so later sleeps start one overflow (65.5 ms) after each wake-up. (ii) Power-down: only a low level on INT0 (PD2) here (or reset/watchdog/INT2/TWI match). (iii) After the start-up delay it executes the INT0 ISR, then continues after sleep_cpu() with sleep_disable(). (iv) None: in power-down clk_CPU, clk_FLASH, clk_I/O, clk_ADC and clk_ASY are all stopped. (v) Line 38 sets SE, line 40 executes SLEEP; without line 39 the MCU sleeps with interrupts disabled and INT0 cannot wake it (only a reset)."
sources: ["ATmega32 datasheet, Power Management and Sleep Modes (power-down, active clock domains, wake-up sources)", "avr-libc <avr/sleep.h> documentation (sleep_enable, sleep_cpu, sei before sleep)", "EHP Timer_Part_1 slides 25-27 (Timer1 overflow every 65.536 ms at 1 MHz)"]
---
*Assumption:* 1 MHz system clock (no prescaler), so Timer1 overflows every $65536\ \mu s \approx 65.5$ ms.

**(i) When does it sleep?** Each overflow ISR increments `ovfCount` until it reaches MAX = 60; the next (61st) overflow sets `sleepNow = 1`. The main loop then puts the MCU to sleep. First sleep: after about $61 \times 65.536\ \text{ms} \approx 4.0$ s of running. Since `ovfCount` is never reset (only TCNT1 is), it stays at 60, so after each wake-up the MCU sleeps again at the next overflow, about 65.5 ms later.

**(ii) How to wake it?** The mode is **power-down**. Only asynchronous events can wake it: here, a **low level on INT0 (PD2)** (e.g. a button to ground, since the pull-up is on). An external reset, brown-out, watchdog, INT2 edge or TWI address match would also wake it, but only INT0 is set up in this program.

**(iii) First thing after waking.** The MCU waits for the oscillator start-up time, then (the I-bit being set) it **executes the INT0 interrupt routine** (empty here). After `RETI` it continues with the instruction after `sleep_cpu()`: `sleep_disable()`, then `sleepNow = 0` and `TCNT1 = 0`.

**(iv) Active clock domains.** In power-down **all** clocks are stopped: clk$_{CPU}$, clk$_{FLASH}$, clk$_{I/O}$, clk$_{ADC}$ and clk$_{ASY}$ are **all inactive**. Only asynchronous logic (external interrupt level detection, TWI address match, watchdog oscillator) runs. That is why a low-level (not edge) INT0 is used.

**(v) Lines 38-40**

- **Line 38, `sleep_enable()`**: sets the **SE** bit in MCUCR, allowing the SLEEP instruction to take effect.
- **Line 40, `sleep_cpu()`**: executes the **SLEEP** instruction, which enters the mode selected by `set_sleep_mode()` (power-down).
- **Line 39, `sei()`**: interrupts were disabled by `cli()` at the start of the loop body (so that `sleepNow` is tested safely). `sei()` re-enables them just before sleeping; the AVR always executes the instruction after SEI before any interrupt, so no interrupt can slip in between and the MCU is guaranteed to sleep. **If line 39 were removed,** the MCU would go to sleep with the global interrupt bit cleared: the INT0 interrupt could not be serviced, so the program would never wake up from power-down (only a reset would restart it).

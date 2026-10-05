---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "The hardware clears the I-bit when an ISR starts (RETI sets it again), so nesting is off by default. Re-enable global interrupts inside the ISR with sei() (or declare ISR(vector, ISR_NOBLOCK)); then a higher (or any) pending interrupt can interrupt the running ISR."
sources: ["EHP ATmega32 Interrupt slide 25 (nested interrupts)", "EHP ATMega32_Core slides 16-17 (interrupt execution and RETI)"]
---
When an interrupt is accepted, the ATmega16/32 **clears the global interrupt enable bit (I in SREG)** in hardware, so no other interrupt can run inside the ISR: nested interrupts are **disabled by default**. `RETI` at the end of the ISR sets I again.

**To enable nesting**, set the I-bit again at the start of the ISR:

```c
ISR(TIMER1_OVF_vect)
{
    sei();              // global interrupts on again: other ISRs may now interrupt this one
    /* ... longer work ... */
}                       // RETI
```

or let the compiler do it: `ISR(TIMER1_OVF_vect, ISR_NOBLOCK) { ... }`.

The individual interrupts must of course be enabled (GICR, TIMSK, ...) and `sei()` called in `main()`. Take care that the stack is large enough, that a level-triggered source is cleared before `sei()` (otherwise the same ISR re-enters at once), and that shared variables are `volatile`.

---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "ISRs cannot take arguments or return values, so they share data through global variables. Since main() never calls the ISR, the compiler may keep such a variable in a register or remove a loop that tests it; 'volatile' forces every access to read/write memory, so changes made by the ISR are seen."
sources: ["EHP ATmega32 Interrupt slides 27-29 (use of volatile, tick example)"]
---
**Why it is needed**

- An ISR is not called from `main()`, so it **cannot take arguments or return a value**. Data is exchanged through **global variables**.
- The compiler optimizes `main()` by looking only at code that `main()` can reach. If nothing in a loop changes a variable, it may **load it into a register once** and keep using that copy, or even **remove the test** as always true/false. The ISR's changes to the variable in memory are then never seen.
- Declaring the variable **`volatile`** tells the compiler that it can change at any time outside the visible code, so **every** access must read it from (or write it to) memory, and it may not be optimized away.

**Example (slides)**

```c
volatile uint8_t tick;          // keep tick out of registers!

ISR(TIMER1_OVF_vect) {
    tick++;                     // changed only by the ISR
}

int main(void) {
    /* timer set-up, sei() ... */
    while (tick == 0x00) {      // wait for the first overflow
        /* ... */
    }
    /* continue */
}
```

Without `volatile`, the compiler sees that nothing inside the `while` loop changes `tick` and may turn it into an infinite loop. With `volatile`, `tick` is re-read from memory on each pass, and the loop ends after the first overflow.

**Other applications:** counters of overflows for elapsed-time measurement, flags set by an external-interrupt ISR and polled in `main()`, buffers filled by a USART receive ISR, ADC results stored in `ADC_vect`. (Multi-byte volatile variables should also be read with interrupts disabled, so the ISR cannot change them half-way through.)

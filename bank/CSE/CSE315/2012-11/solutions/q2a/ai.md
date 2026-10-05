---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "TCNT1 is accessed through an 8-bit TEMP register shared by the 16-bit timer registers. Write: high byte first (goes into TEMP), then low byte: the low-byte write copies TEMP and the low byte into TCNT1 in the same clock. Read: low byte first: TCNT1L is read and TCNT1H is copied into TEMP in the same clock; then reading TCNT1H returns TEMP. Disable interrupts around the pair so an ISR cannot use TEMP in between."
sources: ["ATmega32 datasheet, Timer/Counter1: accessing 16-bit registers (TEMP register, write high byte first, read low byte first)", "EHP ATmega32 Interrupt slide 24 (disable interrupts when reading/writing 16-bit values like TCNT1)"]
---
**How a 16-bit register is accessed on an 8-bit bus**

Timer1 has one 8-bit **TEMP** register, shared by all its 16-bit registers (TCNT1, OCR1A, OCR1B, ICR1).

- **Write:** the CPU first writes the **high byte**; it is stored in **TEMP**. When the CPU then writes the **low byte**, the low byte and TEMP are written into **TCNT1 together in the same clock cycle**.
- **Read:** the CPU first reads the **low byte**; at that same clock the **high byte is copied into TEMP**. The following read of the high byte returns TEMP. So both bytes belong to the same 16-bit value, even though TCNT1 keeps counting.

The order (write high first, read low first) is essential. Because TEMP is shared, an interrupt that accesses any 16-bit Timer1 register between the two byte accesses would corrupt TEMP, so interrupts are disabled during the access (an **atomic** operation).

**(i) Write 0x3F55 to TCNT1**

```text
    in   r18, SREG        ; save the global interrupt flag
    cli                   ; disable interrupts
    ldi  r17, 0x3F
    ldi  r16, 0x55
    out  TCNT1H, r17      ; high byte first -> TEMP
    out  TCNT1L, r16      ; low byte: TCNT1 = 0x3F55 in one clock
    out  SREG, r18        ; restore interrupt flag
```

**(ii) Read TCNT1 into r15 (low) and r16 (high)**

```text
    in   r18, SREG        ; save interrupt flag
    cli
    in   r15, TCNT1L      ; low byte first; TCNT1H copied to TEMP
    in   r16, TCNT1H      ; high byte (from TEMP)
    out  SREG, r18        ; restore interrupt flag
```

(r18 is used as a scratch register; any free register works. `ldi` needs r16-r31, so the constant is loaded into r16/r17.)

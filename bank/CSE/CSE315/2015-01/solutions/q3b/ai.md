---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "RET pops the return address into the PC (end of a subroutine). RETI does the same and also sets the global interrupt flag I in SREG (end of an ISR). In a subroutine called with interrupts enabled, RETI behaves like RET (I is already 1). But RET at the end of an ISR leaves I = 0 (it was cleared on entry), so all further interrupts stay disabled."
sources: ["EHP ATmega32 Interrupt slide 25 (global interrupt disabled on entry, set again by RETI)", "EHP ATMega32_Core slides 16-17 (RETI pops PC and sets I)"]
---
| | RET | RETI |
|:--|:--|:--|
| Used at the end of | a subroutine (after CALL/RCALL) | an interrupt service routine |
| Pops return address into PC | yes | yes |
| Sets the global interrupt flag I (SREG bit 7) | **no** | **yes** |

**Why RETI can replace RET (usually).** In a normal subroutine called while interrupts are enabled, I is already 1. RETI pops the PC just like RET and "sets" I, which changes nothing, so the program works the same. (Only if the subroutine was deliberately called with interrupts disabled would RETI wrongly enable them.)

**Why RET cannot replace RETI.** When an interrupt is accepted, the hardware **clears I** so the ISR is not interrupted. The ISR must return with RETI to set I again. If it ends with **RET**, the PC is restored but **I stays 0**: the global interrupt system remains disabled, so **no further interrupt will ever be serviced** (until the program executes SEI). The interrupt-driven parts of the program silently stop working.

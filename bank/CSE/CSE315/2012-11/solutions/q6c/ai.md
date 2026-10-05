---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "When a call gate raises privilege, using the caller's stack is unsafe: the less privileged caller controls it (it may be too small, invalid, or shared with other code that could read/modify the inner routine's data and return addresses). Solution: each privilege level has its own stack; the processor switches to SS:ESP for the target level from the TSS (SS0:ESP0, SS1:ESP1, SS2:ESP2), saves the caller's SS:ESP on the new stack and copies the declared number of parameters (gate word count); RET restores the old stack."
sources: ["Intel 80386 Programmer's Reference Manual, Sec. 6.3.4.1 (stack switching), Sec. 7.1 (TSS stack fields)"]
---
**The problem**

When a call gate transfers control to **more privileged** code, that code would normally keep using the caller's stack. This is dangerous:

1. **Not enough or invalid stack:** the less privileged caller controls its own SS:ESP. It may be almost full, point to an invalid or read-only segment, or be deliberately bad. A stack fault inside the operating system could crash the whole system.
2. **Protection leak:** data that the privileged routine pushes (return addresses, saved registers, local variables) would be on a stack that less privileged code can read and **modify** (e.g. change a return address while the kernel is running, from another thread).
3. **Parameters:** the parameters are on the caller's stack, which the privileged routine should not have to address through the caller's segment.

**How it is solved**

- **Separate stack for every privilege level.** The TSS of each task stores **SS0:ESP0, SS1:ESP1, SS2:ESP2**, stacks prepared by the operating system for levels 0, 1 and 2.
- On a CALL through a gate to a more privileged level $n$, the processor **automatically switches** to SS$n$:ESP$n$ from the TSS (checking that the new stack segment is valid and has DPL = $n$).
- It **pushes the caller's SS and ESP** on the new stack, then **copies the number of parameters given in the gate's word-count field** from the old stack to the new one, then pushes CS:EIP.
- On return (`RET n`), the processor removes the parameters, **restores the caller's SS:ESP** and the outer privilege level.

So privileged code always runs on a trusted, sufficiently large stack that the calling code cannot touch.

---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) PL: the handler needs privileged/IOPL-sensitive instructions (CLI to block interrupts while it works, reading CR2, CLTS, I/O, HLT), so it must run at PL0. ST1/ST2: save the interrupted program's registers (PUSHAD, segment registers) and restore them (and remove an error code) before IRET, so the program resumes unchanged. (ii) Alt 1: enter through an interrupt gate, which clears IF automatically, so no CLI section is needed. Alt 2: make the handler a separate task via a task gate: the task switch saves/restores all registers in the TSSs (no ST1/ST2), but after IRET the handler task needs a JMP back to its start because the next invocation resumes after the IRET."
sources: ["Intel 80386 Programmer's Reference Manual, Sec. 9.6 (interrupt tasks and procedures; interrupt gate vs trap gate; handler tasks loop with IRET followed by JMP)", "Brey, The Intel Microprocessors, Sec. 17-5 and 17-6 (80386 interrupts, TSS)"]
---
**(i) Purpose of the sections**

- **Section PL (privileged instructions).** An exception/interrupt handler usually has to do things only the operating system may do: disable interrupts with **CLI** so that the handler is not re-entered while it saves state, read **CR2** (faulting address), use **CLTS**, access I/O ports, or **HLT**. These instructions are privileged (CPL = 0) or IOPL-sensitive, so the handler runs at PL0 and contains them.
- **Section ST1 (stack operations at the start).** The handler will change registers. Before that it **saves** the interrupted program's state on the stack: `PUSHAD`, `PUSH DS`, `PUSH ES`, ... (the processor itself saved only EFLAGS, CS, EIP, and SS, ESP when the level changed).
- **Section H** handles the interrupt.
- **Section ST2 (stack operations at the end).** **Restores** the saved registers in reverse order (`POP ES`, `POP DS`, `POPAD`) and, for exceptions that push an **error code**, removes it (`ADD ESP, 4`) so that ESP points at the saved EIP.
- **Section IR (IRET)** returns: pops EIP, CS, EFLAGS (and ESP, SS on a level change), so the program continues exactly where it stopped.

**(ii) The two alternatives**

**Alternative #1: no Section PL.** Enter the handler through an **interrupt gate** in the IDT instead of a trap gate. For an interrupt gate the processor **clears IF automatically** when it enters the handler (and IRET restores the old IF from the saved EFLAGS), so the privileged `CLI` (and the matching `STI`) is not needed. (Similarly, any other privileged work, such as reading CR2, can be left to a separate kernel routine.)

**Alternative #2: no Sections ST1 and ST2, but one instruction after IRET.** Make the handler a **separate task**, entered through a **task gate** in the IDT:

- The interrupt causes a **task switch**: the processor stores **all** registers of the interrupted task in its TSS and loads the handler task's registers from the handler's TSS. Nothing has to be pushed or popped by software, so ST1 and ST2 disappear.
- `IRET` with NT = 1 switches back to the interrupted task, restoring all its registers from its TSS.
- At that switch the handler task's own state is saved in its TSS, with EIP pointing to the instruction **after the IRET**. The next time the interrupt occurs, the handler task resumes there, not at its beginning. So one more instruction is needed after Section IR: **`JMP HANDLER_START`**, which loops back to the start of the handler for the next interrupt.

```text
HANDLER_START:
    ...           ; Section H
    IRET          ; Section IR: task switch back to the interrupted task
    JMP HANDLER_START   ; runs on the next interrupt
```

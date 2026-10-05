---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "CPL changes only through gates and returns: a far CALL through a call gate (or an interrupt/exception through an interrupt or trap gate) to a more privileged non-conforming code segment sets CPL = target DPL and switches to that level's stack from the TSS (SS0:ESP0 ...), copying parameters and saving the old SS:ESP, CS:EIP; RET/IRET to an outer level restores them and nulls more-privileged data selectors. Task switches load a new CPL from the new TSS."
sources: ["Brey, The Intel Microprocessors, Sec. 17-4 to 17-6 (80386 protection: call gates, privilege levels, TSS)", "Intel 80386 Programmer's Reference Manual, Ch. 6 (protection: control transfer, gates, stack switching)", "MHE 80386-updated slides 14-20 (protected mode, descriptors)"]
---
**Privilege levels.** The 80386 has 4 levels, PL0 (most privileged, OS kernel) to PL3 (applications). The **CPL** (current privilege level) is the RPL field of CS (= DPL of the code segment being run, except for conforming segments). Every segment and gate has a **DPL**, and every selector an **RPL**.

**Ordinary far transfers do not change CPL.** A direct far `JMP`/`CALL` to a code segment is allowed only if the target is non-conforming with DPL = CPL, or conforming with DPL $\le$ CPL (then CPL stays the same). So the privilege level can change only in the following controlled ways.

**1. CALL through a call gate (to a more privileged level)**

- The selector in `CALL sel:offset` points to a **call gate** descriptor (in GDT/LDT), which holds the **destination selector**, the **entry offset**, the gate **DPL** and a **parameter count**. The offset in the instruction is ignored.
- Checks: $\max(CPL, RPL) \le$ gate DPL (the caller may use the gate) and target code segment DPL $\le$ CPL (it is equal or more privileged).
- If the target is a **non-conforming** segment with DPL < CPL, the processor:
  1. sets **CPL = target DPL**;
  2. loads a **new stack** for that level from the current **TSS** (SS0:ESP0, SS1:ESP1 or SS2:ESP2);
  3. pushes the caller's **SS:ESP**, copies **parameter count** words/dwords from the old stack to the new one, then pushes the caller's **CS:EIP**;
  4. loads CS:EIP from the gate (entry point).
- Only `CALL` can raise privilege through a gate; a `JMP` through a gate keeps the same level.

**2. Interrupts and exceptions (interrupt/trap gates in the IDT)** work the same way: the handler segment may be more privileged, CPL becomes its DPL, the stack is switched from the TSS, and EFLAGS, CS, EIP (and SS, ESP) are pushed. (Software `INT n` also needs CPL $\le$ gate DPL.)

**3. Return to an outer (less privileged) level: `RET n` / `IRET`.**
The processor pops CS:EIP, checks that the return CS has RPL $\ge$ CPL, sets **CPL = RPL of the returned CS**, pops the old **SS:ESP** (switching back to the outer stack), and **loads null** into DS, ES, FS, GS if they hold selectors of segments more privileged than the new CPL, so the outer code cannot keep access to inner data.

**4. Task switch** (JMP/CALL to a TSS or task gate, or interrupt through a task gate): all registers, including CS (and so CPL), are loaded from the new task's TSS.

This design means privilege can be raised only at entry points chosen by the operating system (gates) and lowered only by returning, with a separate, protected stack for each level.

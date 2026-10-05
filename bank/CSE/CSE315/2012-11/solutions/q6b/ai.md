---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "A program can use a call gate if max(CPL, RPL of the gate selector) <= gate DPL (numerically), and the gate's target code segment must have DPL <= CPL (so the gate leads to equal or more privileged code; a CALL may raise privilege, a JMP only to the same level)."
sources: ["Intel 80386 Programmer's Reference Manual, Sec. 6.3.4.1 (privilege rules for gates)"]
---
Two checks decide whether a call through a gate is allowed:

1. **Access to the gate itself:**

$$\max(CPL,\ RPL_{gate\ selector}) \le DPL_{gate}$$

(numerically; 0 is the most privileged). The gate's DPL is therefore the **least privileged level allowed to use it**: e.g. a gate with DPL 3 can be used by applications at PL3, while a gate with DPL 0 can be used only by PL0 code.

2. **Destination code segment:**

$$DPL_{target\ code} \le CPL$$

The gate may lead only to code of the **same or higher** privilege; never to less privileged code.

   - With **CALL**, a non-conforming target with DPL < CPL raises the privilege (CPL becomes the target DPL, with a stack switch).
   - With **JMP** through a gate, the target must be non-conforming with DPL = CPL (or conforming with DPL $\le$ CPL); no privilege change.

If either check fails, a general protection fault occurs. By placing gates with suitable DPLs, the OS controls exactly which programs may call which privileged entry points.

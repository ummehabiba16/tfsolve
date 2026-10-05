---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) T; (ii) F (calls go to equal or more privileged code; less privileged only by return); (iii) F (near transfers load no selector); (iv) F (the caller's data segments have DPL >= 2); (v) F (RPL is not forced to 00; more-privileged selectors are nulled); (vi) F (conforming code: CPL can exceed DPL); (vii) F (also interrupt/trap gates, task switches, RET/IRET); (viii) F (only the gate's entry point); (ix) F (JMP may use a call gate, without privilege change); (x) F (a gate with DPL 3, interrupt gates, conforming code)."
sources: ["Intel 80386 Programmer's Reference Manual, Ch. 6 (privilege levels, control transfers, gates, conforming segments, return checks)", "Brey, The Intel Microprocessors, Sec. 17-4 (80386 protection)"]
---
| | Answer | Justification |
|:-:|:-:|:--|
| (i) | **True** | Privilege levels 0, 1, 2, 3 (0 most privileged), encoded in 2-bit DPL/RPL/CPL fields. |
| (ii) | **False** | It is the opposite: a CALL/JMP can go only to code of **equal** privilege (or, through a call gate or conforming segment, **more** privileged, numerically lower). Control reaches **less** privileged code only by a return (RET/IRET), never by CALL/JMP. |
| (iii) | **False** | A **near** JMP/CALL/RET stays in the same code segment and loads no selector, so only the limit is checked. Selector validation happens only for far transfers. |
| (iv) | **False** | A call through a gate does **not** change DS, ES, FS, GS. They still hold the caller's data segments, which PL2 code could load only if their DPL $\ge$ 2. So they have DPL $\ge$ 2, not DPL < 1. |
| (v) | **False** | On return to PL2 the processor checks DS, ES, FS, GS: any selector for a segment with DPL < 2 (accessible only to the more privileged callee) is replaced by the **null selector**. It never sets RPL to 00; a valid DS keeps the RPL it had. |
| (vi) | **False** | The first half is true (RPL of CS = CPL). But for a **conforming** code segment, CPL stays the caller's level, which can be numerically larger than the segment's DPL, so RPL of CS need not equal the DPL. |
| (vii) | **False** | CPL also changes through **interrupt and trap gates** (interrupts/exceptions), **task switches** (new CS from the TSS), and **RET/IRET** returning to an outer level. |
| (viii) | **False** | The gate fixes both the destination selector **and the entry offset**; the offset in the instruction is ignored. Control can go only to that one entry point, which is the whole point of a gate. |
| (ix) | **False** | A far JMP can go through a call gate, but only to a code segment of the **same** privilege (non-conforming DPL = CPL, or conforming); a JMP never raises privilege. |
| (x) | **False** | From PL2 any call gate with DPL $\ge$ 2 is usable, e.g. a gate with **DPL = 3** leading to PL0 code. A PL2 program can also reach more privileged code through an **interrupt/trap gate** (`INT n`, gate DPL $\ge$ 2), a **task gate**, or a **conforming** code segment with DPL < 2 (run at CPL 2). |

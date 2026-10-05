---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "CALL sel:off where sel points to a call gate (GDT/LDT). The gate holds the destination selector, entry offset, DPL and parameter count; the offset in the instruction is ignored. Checks: max(CPL, RPL) <= gate DPL and target code DPL <= CPL. If the target is more privileged non-conforming code: CPL = target DPL, new SS:ESP from the TSS for that level, push old SS:ESP, copy the parameters, push CS:EIP, jump to the entry point. RET n reverses it (checks, restores the outer stack, nulls inner data selectors)."
sources: ["Intel 80386 Programmer's Reference Manual, Sec. 6.3.4 (call gates, stack switching, returning)", "Brey, The Intel Microprocessors, Sec. 17-4"]
---
**Call gate descriptor (8 bytes)**

| Bits | 63-48 | 47 | 46-45 | 44-40 | 36-32 | 31-16 | 15-0 |
|:--|:--|:-:|:-:|:-:|:-:|:--|:--|
| Field | offset 31-16 | P | DPL | type (01100 = 386 call gate) | word count | **destination selector** | offset 15-0 |

**Mechanism**

```text
 CALL gate_sel : (offset ignored)
        |
        v
 GDT/LDT[gate_sel] = CALL GATE {dest selector, entry offset, DPL, count}
        |                  check: max(CPL, RPL) <= gate DPL
        v
 GDT/LDT[dest selector] = CODE SEGMENT descriptor {base, limit, DPL}
        |                  check: code DPL <= CPL
        v
 more privileged? --yes--> new SS:ESP from TSS (SS_n:ESP_n, n = code DPL)
        |                   push old SS, ESP; copy 'count' parameters;
        |                   CPL = code DPL
        v
 push old CS, EIP
        v
 CS:EIP = dest selector : entry offset  --> execution starts at base + entry offset
```

1. The selector in `CALL selector:offset` refers to a **call gate** descriptor. The offset in the instruction is **not used**.
2. **Gate check:** the caller may use the gate only if $\max(CPL, RPL) \le$ gate DPL.
3. The gate's **destination selector** is used to read the **code segment** descriptor; it must be present and have DPL $\le$ CPL (same or more privileged).
4. **Privilege change** (non-conforming target with DPL < CPL):
   - the processor takes the new stack **SS:ESP for the target level from the current TSS**;
   - pushes the caller's **SS and ESP** on the new stack;
   - copies **word-count** parameters (dwords for a 386 gate) from the caller's stack;
   - **CPL becomes the target DPL**.
   With no privilege change the current stack is used.
5. The return address, the caller's **CS and EIP**, is pushed.
6. CS:EIP is loaded with the gate's **destination selector : entry offset**, so the called procedure starts at its single, OS-defined entry point.

**Return:** `RET n` (far) pops EIP and CS, checks that the return is to an equal or outer level, removes $n$ parameter bytes, pops the outer **SS:ESP** if the level changes (and removes the parameters there too), sets CPL to the caller's level and loads null into DS/ES/FS/GS if they refer to segments more privileged than the new CPL.

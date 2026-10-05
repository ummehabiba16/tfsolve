---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Selector 0010h = GDT index 2, RPL 0. Since execution starts at 0020:00004672, descriptor 2 must be a call gate whose destination selector is 0020h (GDT index 4) and entry offset 00004672h; the offset 12345678h in the instruction is ignored. After the gate and privilege checks (and a stack switch from the TSS if the target is more privileged), CS = 0020h (RPL = new CPL) and EIP = 00004672h."
sources: ["Intel 80386 Programmer's Reference Manual, Sec. 6.3.4 (call gates; offset in the instruction is not used)", "Brey, The Intel Microprocessors, Sec. 17-4 (80386 call gates)"]
---
**Decode the selector in the instruction**

0010h = 0000 0000 0001 0 | 0 | 00:

| Field | Value |
|:--|:--|
| Index (bits 15-3) | 2 |
| TI (bit 2) | 0: GDT |
| RPL (bits 1-0) | 00 |

So the processor reads **GDT descriptor 2** (at GDTR base + $2 \times 8$ = base + 10h).

**Why execution continues at 0020:00004672 and not at 0010:12345678**

If descriptor 2 were a normal code segment, execution would start at offset 12345678h in it. It did not, and no task switch occurred (so it is not a TSS or task gate). Therefore descriptor 2 is a **call gate**. A call gate contains its own **destination selector and entry offset**; when a CALL goes through a gate, the **offset in the instruction (12345678h) is ignored**. Here the gate holds:

- destination selector = **0020h** (index 4, TI = 0: GDT descriptor 4, RPL 0), a code segment;
- entry offset = **00004672h**.

**What the processor does**

1. Reads GDT[2]: type = 386 call gate, present. Checks **$\max(CPL, RPL = 0) \le$ gate DPL**: the caller may use the gate.
2. Reads the destination code segment descriptor GDT[4] (selector 0020h). Checks that it is a present code segment with **DPL $\le$ CPL** (same or more privileged).
3. If GDT[4] is non-conforming and its DPL < CPL (privilege increase):
   - CPL becomes GDT[4].DPL;
   - the new stack SS:ESP for that level is loaded from the current **TSS** (e.g. SS0:ESP0);
   - the old SS and ESP are pushed on the new stack, and the number of parameters given in the gate's count field is copied from the old stack.

   Otherwise (same level) the current stack is used.
4. The return address, the caller's **CS and EIP**, is pushed.
5. CS is loaded with **0020h** (its RPL set to the new CPL) and the descriptor cache with GDT[4]'s base/limit/rights; EIP is loaded with **00004672h**.

So the next instruction is fetched from **0020:00004672**, the linear address GDT[4].base + 00004672h. A later far `RET` returns to the caller (switching the stack back if the level changed).

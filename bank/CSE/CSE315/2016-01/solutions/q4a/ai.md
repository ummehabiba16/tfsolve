---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Superscalar = more than one instruction issued per clock. The Pentium has two integer pipelines (U and V, 5 stages each) and can issue two simple, independent instructions per clock ('pairing'), plus a pipelined FPU; separate code and data caches and branch prediction keep both pipes fed. The 80486 had one pipeline (at most one instruction per clock)."
sources: ["Brey, The Intel Microprocessors, Ch. 18 (Pentium: superscalar, U and V pipelines, pairing rules)"]
---
A **superscalar** processor has **more than one execution pipeline** and can **issue and complete more than one instruction in the same clock cycle**.

The **Pentium** is superscalar because:

1. **Two integer pipelines, U and V.** Each is a 5-stage pipeline (prefetch, decode 1, decode 2, execute, write-back). In every clock the decoder can send **two instructions**, one to U and one to V, so up to **2 instructions per clock**.
2. **Instruction pairing.** Two consecutive instructions go together when both are "simple" (e.g. MOV, ADD, INC, PUSH, CMP, short jumps), there is **no dependency** between them (the second does not use the first's result register), and neither has both an immediate and a displacement. Otherwise only the U pipe is used that clock.

```text
clock:     1    2    3    4    5    6
U pipe:   PF   D1   D2   EX   WB              (ADD AX, BX)
V pipe:   PF   D1   D2   EX   WB              (MOV CX, DX)   paired
U pipe:        PF   D1   D2   EX   WB
V pipe:        PF   D1   D2   EX   WB
```

3. A pipelined **floating-point unit** (8 stages), much faster than the 486's.
4. Support for feeding two pipes: separate 8 KB **code and data caches** (dual-ported data cache, so both pipes can access data in the same clock), a 64-bit data bus, and **branch prediction** (branch target buffer) so the pipelines are not flushed on most branches.

The 80486 has a single pipeline and can complete at most one instruction per clock (scalar); the Pentium nearly doubles integer throughput at the same clock rate.

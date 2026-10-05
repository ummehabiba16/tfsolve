---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) Pentium Pro: P6 dynamic execution: x86 instructions decoded into micro-ops, out-of-order and speculative execution with register renaming and a 40-entry reorder buffer, 3 micro-ops/clock, 12-14 stage pipeline, L2 cache in the package at full speed, 36-bit address bus. (ii) Pentium II: P6 core + MMX, 32 KB L1, 512 KB half-speed L2 on an SEC cartridge (Slot 1), 233-450 MHz."
sources: ["Brey, The Intel Microprocessors, Ch. 18 (Pentium Pro and Pentium II)"]
---
Notes on two of the three (answering (i) and (ii)):

**(i) Pentium Pro (1995)**

- First processor with Intel's **P6 microarchitecture ("dynamic execution")**.
- **Three decoders** translate x86 instructions into simple RISC-like **micro-operations**, up to 3 per clock.
- **Out-of-order execution:** micro-ops wait in a reservation station and are dispatched to **5 execution ports** when their operands are ready; a **40-entry reorder buffer** and **register renaming** (40 physical registers) remove false dependencies; results retire **in order**, 3 per clock.
- **Speculative execution** with a 512-entry branch target buffer.
- **12-14 stage superpipeline**, 150-200 MHz.
- **L2 cache (256 KB-1 MB) in the same package**, on a dedicated full-speed backside bus; 16 KB L1 (8 KB code + 8 KB data).
- **36-bit address bus** (64 GB physical), up to 4 processors on one bus; best for 32-bit server/workstation code.

**(ii) Pentium II (1997)**

- The **P6 core** of the Pentium Pro (better for 16-bit code) plus the **MMX** instructions (57 integer SIMD instructions).
- L1 doubled to **32 KB** (16 KB + 16 KB).
- **512 KB L2** on a small board inside a **Single Edge Contact cartridge**, running at **half the core speed** (cheaper than the Pro's in-package cache).
- Cartridge plugs into **Slot 1**.
- 233-450 MHz; front-side bus 66 MHz, later 100 MHz. Variants: Celeron (low cost) and Xeon (servers).

(For (iii), the Pentium III adds SSE: 70 instructions and eight 128-bit XMM registers for SIMD floating point, a processor serial number, and in the Coppermine version a 256 KB full-speed on-die L2, reaching about 1 GHz.)

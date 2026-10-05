---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Pentium II: P6 (Pentium Pro) core plus MMX, 32 KB L1, 512 KB L2 on an SEC cartridge (Slot 1) running at half core speed, 233-450 MHz, 66/100 MHz bus. Pentium III: P6 core plus SSE (70 new instructions, eight 128-bit XMM registers for SIMD floating point), processor serial number, 450 MHz to over 1 GHz; Coppermine moved 256 KB full-speed L2 on die (0.18 um), Slot 1 then Socket 370."
sources: ["Brey, The Intel Microprocessors, Ch. 18 (Pentium II, Pentium III)"]
---
**(i) Pentium II (1997)**

- **Core:** the **P6** dynamic-execution core of the Pentium Pro (out-of-order, speculative, 3 micro-ops/clock), improved for 16-bit code, plus the **MMX** multimedia instructions (57 integer SIMD instructions using the FPU registers as 64-bit MMX registers).
- **Caches:** L1 doubled to **32 KB** (16 KB code + 16 KB data). The **512 KB L2 cache** was moved off the die onto a small board inside a **Single Edge Contact (SEC) cartridge**, connected by a backside bus running at **half the core speed** (cheaper than the Pentium Pro's in-package L2).
- **Package:** the cartridge plugs into **Slot 1** (242 contacts).
- **Speeds:** 233-450 MHz; system (front-side) bus 66 MHz, later **100 MHz**.
- Variants: Celeron (low cost, small or no L2) and Xeon (full-speed large L2, multiprocessor servers).

**(ii) Pentium III (1999)**

- **Core:** still the P6 core with MMX, plus **SSE (Streaming SIMD Extensions)**: 70 new instructions and **eight 128-bit XMM registers**, each holding four single-precision floating-point numbers, for 3D graphics, video and speech processing.
- **Processor serial number** (a unique ID readable by software; controversial for privacy, later disabled).
- **Katmai** (0.25 µm): 512 KB half-speed L2 on the cartridge, Slot 1, 450-600 MHz.
- **Coppermine** (0.18 µm): **256 KB L2 on the die at full core speed** with a wider cache bus, moved to the cheaper **Socket 370 (FC-PGA)** package, 500 MHz to 1.13 GHz; 100/133 MHz front-side bus. Tualatin (0.13 µm) reached 1.4 GHz.

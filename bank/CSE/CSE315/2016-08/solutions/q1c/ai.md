---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Two modes: real address mode (8086-compatible, 1 MB) and protected virtual address mode (16 MB physical, 1 GB virtual, protection). Real to protected: build GDT/IDT, LGDT/LIDT, set PE in the MSW with LMSW, then a far JMP to load CS and reload the segment registers. Protected to real: no instruction; only a processor reset (hardware reset, or a triple fault/keyboard-controller reset with a shutdown code so the BIOS resumes the program)."
sources: ["MHE 80286 slides (modes, MSW, PE bit)", "MHE 80386-updated slide 2 (80286 must be restarted to return to real mode)", "Brey, The Intel Microprocessors, Sec. 17-1"]
---
The 80286 has **two modes of operation**:

1. **Real address mode** (after reset): works like a fast 8086. 20-bit addresses (1 MB), segment $\times$ 16 + offset, no protection.
2. **Protected virtual address mode (PVAM):** 24-bit physical addresses (16 MB), 1 GB virtual address space per task, segment descriptors, privilege levels, task switching.

**Real $\to$ protected**

1. In real mode, build the **GDT** (and IDT, LDTs, TSS) in memory.
2. Load **GDTR and IDTR** with `LGDT` / `LIDT`.
3. Set the **PE bit** (bit 0) of the **Machine Status Word**: `MOV AX, 1` / `LMSW AX` (with the other MSW bits).
4. Immediately do a **far JMP** to a code-segment selector: it flushes the prefetch queue and loads CS with a valid protected-mode descriptor. Then load DS, ES, SS with valid selectors.

**Protected $\to$ real**

The 80286 has **no instruction** to clear PE: once set, `LMSW` cannot clear it. The only way back to real mode is a **reset** of the processor:

- a hardware reset, or
- a software-caused reset (e.g. the PC/AT asks the keyboard controller to pulse the CPU's RESET line, or a deliberate triple fault causes shutdown), after storing a "shutdown code" in CMOS so that the BIOS, after reset, jumps back to the program instead of rebooting.

This is slow and awkward, and it was one of the main limitations fixed by the 80386 (which can clear PE and also has virtual-8086 mode).

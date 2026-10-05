---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) Inquire cycle: a bus cycle in which another bus master drives an address into the Pentium (EADS' asserted, A31-A5 as inputs) so the Pentium checks its internal cache; it answers HIT'/HITM' and writes back a modified line, keeping caches coherent. (ii) Virtual 8086 mode: VM = 1 lets 8086 real-mode programs run as protected tasks at CPL 3 with segment x 16 addressing, paging and a monitor. (iii) NMI: non-maskable interrupt pin, rising edge, type 2, cannot be disabled by IF, used for power failure or memory errors."
sources: ["Brey, The Intel Microprocessors, Ch. 18 (Pentium inquire cycles, EADS, HIT, HITM)", "MHE 80386-updated slides 14-15 (virtual 86 mode)", "MHE INTR slide 18 (NMI type 2)"]
---
**(i) Inquire cycle**

The Pentium has an internal write-back cache. When another bus master (DMA controller or another processor) accesses main memory, it must find out whether the Pentium's cache holds a copy of that location. It does so with an **inquire (snoop) cycle**:

- The other master puts the address on the bus and asserts **$\overline{EADS}$**; the Pentium's address lines **A31-A5 act as inputs** (that is why the Pentium address bus is bidirectional).
- The Pentium looks up the address in its cache and answers on **$\overline{HIT}$** (line present) and **$\overline{HITM}$** (line present and modified).
- If the line is modified, the Pentium **writes it back** to memory first; if INV is asserted, it invalidates the line.

This keeps memory and caches **coherent** in multiprocessor and DMA systems.

**(ii) Virtual 8086 mode**

A protected-mode mode (VM = 1 in EFLAGS) in which **8086 real-mode programs run as protected tasks**. Addresses are formed as segment $\times$ 16 + offset (1 MB), but paging can place that 1 MB anywhere in memory, and the task runs at **CPL 3**. Privileged and I/O-sensitive instructions and all interrupts trap to a protected-mode **monitor**, so several DOS programs can run safely together with protected-mode programs (e.g. DOS windows in Windows). Entered by IRET or a task switch with VM = 1, left on any interrupt.

**(iii) NMI (non-maskable interrupt)**

- A hardware interrupt input pin triggered by a **rising edge** (it must stay high for a few clocks).
- It **cannot be disabled** by the IF flag (`CLI` has no effect); it is always **type 2** (vector at 00008H in real mode, IDT entry 2 in protected mode).
- It has higher priority than INTR. While its handler runs, further NMIs are held off until IRET.
- Used for **critical events**: power failure (save data before the supply drops), memory parity errors, watchdog timers.

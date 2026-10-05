---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Processor size is set by how many bits the ALU and general registers handle at once. The 8086 has 16-bit registers (AX...) and a 16-bit ALU, so it is 16-bit; the Pentium has 32-bit registers (EAX...) and a 32-bit ALU, so it is 32-bit, even though its external data bus is 64 bits wide."
sources: ["MHE Intro slides ('What is an n-bit processor?')", "Brey, The Intel Microprocessors, Ch. 2 and 18 (8086 and Pentium registers, Pentium 64-bit data bus)"]
---
A processor is called **n-bit** by the number of bits its **ALU and general-purpose registers** can process in one operation, not by its address bus or external data bus.

- **8086:** registers AX, BX, CX, DX, SP, BP, SI, DI are **16 bits** and its ALU adds, subtracts and moves 16-bit data at once (e.g. `ADD AX, BX`). So it is a **16-bit processor** (its 20-bit address bus does not change this).
- **Pentium:** has the 80386-style **32-bit** registers EAX, EBX, ..., ESP and a 32-bit integer ALU (`ADD EAX, EBX`), so it is a **32-bit processor**. Its external **data bus is 64 bits** wide, but that only lets it fetch 8 bytes per bus cycle (for the cache), and its address bus is 32 bits; neither makes it a 64-bit processor.

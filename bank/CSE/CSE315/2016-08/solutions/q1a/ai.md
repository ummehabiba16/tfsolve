---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "The width of the data the processor can operate on at once, i.e. its ALU and general-register (internal data path) width, not the address bus or the external data bus. 8086/8088 (16-bit ALU and registers) are 16-bit; 80386DX and 80386SX (32-bit EAX... and ALU) are 32-bit even though the 8088 and 386SX have narrower external buses."
sources: ["MHE Intro slides ('What is an n-bit processor?': ALU size determines the size of the processor)", "MHE 80386-updated slides 3-4 (80386 32-bit ALU; 386SX with 16-bit data bus)"]
---
A processor is called **n-bit** according to the amount of data it can **process at one time**: the width of its **ALU** and of its **general-purpose registers / internal data bus**. If it can add, subtract or move 16 bits in one operation it is a 16-bit processor; if 32 bits, a 32-bit processor.

It is **not** decided by:

- the **address bus** width (8086: 20 bits, 80286: 24 bits, both 16-bit processors);
- the **external data bus** width: the **8088** has an 8-bit external bus but a 16-bit ALU and registers, so it is a **16-bit** processor; the **80386SX** has a 16-bit external bus but 32-bit registers (EAX, EBX, ...) and a 32-bit ALU, so it is a **32-bit** processor.

| Processor | ALU / registers | External data bus | Class |
|:--|:-:|:-:|:-:|
| 8088 | 16-bit | 8-bit | 16-bit |
| 8086, 80286 | 16-bit | 16-bit | 16-bit |
| 80386SX | 32-bit | 16-bit | 32-bit |
| 80386DX, 80486 | 32-bit | 32-bit | 32-bit |

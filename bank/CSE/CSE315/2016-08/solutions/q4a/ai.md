---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Earlier x86 chips (up to the Pentium) execute instructions in program order in fixed pipelines (Pentium: two in-order U/V pipes). The Pentium Pro (P6) uses dynamic execution: three decoders turn x86 instructions into RISC-like micro-ops, a reservation station and 40-entry reorder buffer with register renaming execute them out of order and speculatively (deep branch prediction) on 5 execution ports, retiring 3 per clock in order; 12-14 stage superpipeline; L2 cache in the same package on a full-speed backside bus; 36-bit address bus (64 GB)."
sources: ["Brey, The Intel Microprocessors, Ch. 18 (Pentium Pro: internal structure, dynamic execution)"]
---
**Earlier processors.** The 8086-80486 execute instructions strictly **in program order**, one after another through a pipeline. The Pentium added a second integer pipeline (**U and V**, superscalar), but both pipelines are still **in-order**: if one instruction waits for memory, everything behind it waits.

**Pentium Pro (P6 microarchitecture): dynamic execution**

```text
 L2 cache (same package, full-speed backside bus)
        |
 L1 I-cache --> fetch/decode unit: 3 decoders --> micro-ops (uops)
                                                     |
                                    register alias table (renaming)
                                                     |
                               reorder buffer (40 uops) + reservation station
                                                     |
                     5 ports: 2 integer, FPU, load, store address/data
                                                     |
                               retirement unit (3 uops/clock, in order)
```

Differences from earlier processors:

1. **Micro-operations (RISC-like core).** Complex x86 instructions are translated by **three decoders** (two simple, one complex, plus a microcode sequencer) into simple fixed-format **micro-ops**; up to 3 instructions are decoded per clock.
2. **Out-of-order execution.** Micro-ops wait in a **reservation station** and are sent to any of **5 execution ports** as soon as their operands are ready, not in program order. A **reorder buffer** (40 entries) keeps track of them, and a **retirement unit** commits up to 3 results per clock **in program order**, so the program sees correct results.
3. **Register renaming.** The 8 x86 registers are mapped onto 40 internal registers, removing false dependencies between instructions that reuse the same register.
4. **Speculative execution with deep branch prediction.** A 512-entry branch target buffer predicts branches, and instructions beyond them are executed speculatively; wrong-path results are discarded at retirement.
5. **Superpipelined:** 12-14 stages, allowing higher clock rates (150-200 MHz).
6. **On-package L2 cache** (256 KB-1 MB) on a dedicated full-speed **backside bus**, separate from the system bus.
7. **36-bit address bus** (64 GB physical memory with PAE) and support for up to 4 processors on one bus.

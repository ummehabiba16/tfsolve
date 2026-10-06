---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A precise interrupt leaves the machine in a well-defined state (PC saved, earlier instructions done, later ones not started, state of the PC instruction known); an imprecise one does not, which complicates the OS."
sources: ["Tanenbaum MOS 4e, sec. 5.1.5 (interrupts revisited)"]
---
**Precise interrupt:** an interrupt that leaves the machine in a **well-defined state**:

1. the **PC is saved** in a known place;
2. **all instructions before** the one pointed to by the PC have completely executed;
3. **no instruction after** the one pointed to by the PC has executed;
4. the **execution state of the instruction pointed to by the PC is known**.

The OS can then simply restart the program at the saved PC.

**Imprecise interrupt:** a pipelined/superscalar CPU issues instructions out of order, so when the interrupt arrives some later instructions may have finished while earlier ones have not, and the machine state is **not well defined** (the PC may not tell which instructions completed). The CPU must dump a large amount of internal state for the OS, which has to work out what happened; this makes the OS code **slower, larger and more complicated**.

**Trade-off:** precise interrupts require much **complex hardware** (e.g. reorder buffers to retire instructions in order), which is why some machines (e.g. old Cray/early superscalar designs) used imprecise interrupts; today most general-purpose CPUs provide precise interrupts despite the cost, because they make the OS much simpler.

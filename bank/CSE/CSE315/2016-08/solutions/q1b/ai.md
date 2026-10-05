---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "In protected mode every segment is described by a descriptor (base, limit, access rights). Protection: limit checks (offset <= limit), type checks (no writing code or executing data, read-only data), four privilege levels with CPL/DPL/RPL rules (data: max(CPL, RPL) <= DPL; code transfers only to equal level or through call gates), separate task address spaces through LDTs, task switching through TSS, I/O protection by IOPL; violations raise exceptions (e.g. general protection fault 13)."
sources: ["MHE 80286 slides (protected mode, selectors, descriptors, access rights byte, privilege levels, IOPL)", "Brey, The Intel Microprocessors, Sec. 2-3 and 17-4 (protected-mode memory, protection)"]
---
In **protected mode** the 80286 checks every memory access against information stored in **descriptors**, so that programs cannot interfere with each other or with the operating system.

**1. Segment descriptors (base, limit, access rights).** A segment register holds a selector that points to a descriptor in the GDT (shared) or LDT (per task). The descriptor gives the segment's 24-bit base, 16-bit limit and access-rights byte (P, DPL, S, E, ED/C, R/W, A).

**2. Limit checking.** Each offset must be $\le$ the limit (or above it for expand-down stack segments). Otherwise a **general protection fault** (exception 13) or stack fault (12) occurs. A program cannot run outside its segments.

**3. Type checking.**

- Code segments can be executed and optionally read, but **never written**.
- Data segments can be read and optionally written, but **never executed**.
- Only valid descriptor types may be loaded into each register (e.g. CS must get a code segment, SS a writable data segment).
- A not-present segment (P = 0) causes exception 11, which the OS can use to load the segment (virtual memory).

**4. Privilege levels (0 = highest ... 3 = lowest).**

- **CPL** (current privilege level of the running code), **DPL** (in each descriptor), **RPL** (in each selector).
- **Data access:** allowed only if $\max(CPL, RPL) \le DPL$ (numerically): a program can use data at its own or a less privileged level.
- **Code transfer:** a direct JMP/CALL may go only to code of the same privilege (or conforming code); to call more privileged code (OS services) a program must use a **call gate**, which fixes the entry point, and the processor switches to a stack for that level (from the TSS).
- Privileged instructions (LGDT, LIDT, LMSW, HLT, ...) work only at CPL 0.

**5. Task isolation.** Each task can have its own **LDT**, so its segments are invisible to other tasks; the **TSS** stores its state and the processor switches tasks with checks.

**6. I/O protection.** The **IOPL** field in the flags sets the least privileged level allowed to execute IN, OUT, CLI, STI; other levels get a protection fault.

Any violation causes an exception, and the operating system decides what to do (e.g. terminate the program).

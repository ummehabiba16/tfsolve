---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "The page-fault exception (14) pushes an error code whose bits give the nature of the fault: P (0 = page not present, 1 = protection violation), W/R (0 = read, 1 = write), U/S (0 = supervisor, 1 = user mode). The offending linear address is loaded into CR2."
sources: ["MHE 80386-updated slides 9, 12 (CR2 used in paging, type 14 page fault)", "Intel 80386 Programmer's Reference Manual, Sec. 9.8.14 (page fault error code and CR2)"]
---
**Nature of the fault: the error code.** For a page fault (exception 14) the 80386 pushes a 32-bit **error code** on the handler's stack (after EFLAGS, CS, EIP). Its low three bits describe the fault:

| Bit | Name | 0 | 1 |
|:-:|:--|:--|:--|
| 0 | P | the page (directory or table entry) was **not present** | a **protection violation** on a present page |
| 1 | W/R | the access was a **read** | the access was a **write** |
| 2 | U/S | the processor was in **supervisor** mode (CPL 0-2) | the processor was in **user** mode (CPL 3) |

From these bits the handler knows, e.g., "a user-mode write to a present but read-only page" (P = 1, W/R = 1, U/S = 1), or "a supervisor read of a page not in memory" (P = 0, W/R = 0, U/S = 0), and can decide whether to load the page from disk, do copy-on-write, or terminate the program. The saved CS:EIP points to the faulting instruction, so it can be restarted after the fix.

**The offending address: CR2.** The processor loads the **linear address** that caused the fault into control register **CR2** (the page fault linear address register). The handler reads it with `MOV EAX, CR2`.

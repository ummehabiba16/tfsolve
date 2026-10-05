---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "TSS holds SS0:ESP0, SS1:ESP1, SS2:ESP2 so that each privilege level 0-2 gets its own stack when entered through a gate or interrupt: the inner level cannot be crashed or spied on through a stack controlled by less privileged code, and it always has enough valid stack. Shutdown: if ESP0/SS0 are invalid (e.g. not-present stack page), an interrupt from PL3 faults while pushing (stack/page fault), invoking that handler needs the same PL0 stack and faults again (double fault), and the double-fault handler faults again (triple fault): the processor shuts down."
sources: ["Intel 80386 Programmer's Reference Manual, Sec. 6.3.4.1 and 7.1 (stack switching, TSS), Sec. 9.8.8 (double fault and shutdown)", "MHE 80386-updated slide 12 (type 8 double fault)", "Brey, The Intel Microprocessors, Sec. 17-6 (TSS)"]
---
**Why three sets of stack registers**

The TSS contains **SS0:ESP0, SS1:ESP1 and SS2:ESP2**, one stack pointer for each of the privilege levels 0, 1 and 2.

- When control moves to a **more privileged** level through a call gate, interrupt gate or trap gate, the processor **switches stacks**. It loads the new SS:ESP for the target level from the TSS and saves the caller's SS:ESP on the new stack.
- Each level needs its own stack because a less privileged program controls its own stack: it could have too little space left, point it at an invalid segment, or read/write data left there. If the kernel used the caller's stack it could crash or leak/accept tampered data. A separate, OS-prepared stack per level protects the inner levels.
- There is no SS3:ESP3: level 3 is never entered by a call to a more privileged level (it is entered only by returning), and its SS:ESP is saved on the inner stack (and in the TSS's normal SS/ESP fields at a task switch).

**Scenario: a stack fault leading to shutdown**

1. A user program (PL3) is interrupted (or calls the kernel through a gate). The processor switches to the PL0 stack given by **SS0:ESP0** in the TSS.
2. Suppose SS0:ESP0 is bad: the stack segment is not present, ESP0 is beyond its limit, or the stack page is not present. Pushing the return information causes a **stack fault (#12)** or **page fault (#14)**.
3. To handle that fault the processor must again push onto the **same PL0 stack**, which fails again. Two contributory faults while invoking a handler give a **double fault (#8)**.
4. The double-fault handler is a PL0 interrupt/trap gate that also uses the same bad stack, so invoking it causes yet another fault.
5. A fault while invoking the double-fault handler is not recoverable: the processor enters **shutdown** (it stops executing and signals shutdown on the bus; in a PC this usually resets the system).

(To avoid it, the double-fault handler is usually reached through a **task gate**, so a task switch gives it a completely fresh, known-good stack.)

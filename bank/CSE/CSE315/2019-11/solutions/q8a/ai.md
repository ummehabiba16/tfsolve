---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "The return pops in the wrong order: the stack is LIFO, so IRET must pop IP, then CS, then FLAGS. Popping CS first swaps CS and IP; it still works only when the saved CS and IP values are equal."
sources: ["MHE INTR slides 11-12 (function of 8086 during interrupts)", "Brey, The Intel Microprocessors, Sec. 12-1 (interrupt processing, IRET)"]
---
**What is wrong.** On an interrupt the 8086 pushes **FLAGS, then CS, then IP** (and clears IF and TF). The stack is **LIFO**, so the return (IRET) must pop in the **reverse** order:

```text
POP IP      ; pushed last, popped first
POP CS
POP FLAGS
```

The figure pops **CS first, then IP**. The first POP takes the saved **IP** from the top of the stack into CS, and the second takes the saved **CS** into IP. CS and IP are **swapped**, so execution returns to $IP_{old} \times 10H + CS_{old}$ instead of $CS_{old} \times 10H + IP_{old}$. FLAGS is still restored correctly because it is popped last.

**When it still works.** Only when the **saved CS and IP are equal** (e.g. CS = IP = 1234H at the moment of the interrupt). Swapping two equal values changes nothing, so the program resumes at the correct place.

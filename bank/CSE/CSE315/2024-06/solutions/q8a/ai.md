---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Yes: the stack is LIFO, so the return must be POP IP, POP CS, POP FLAGS (IRET). The figure pops CS first, which swaps CS and IP; it still works only when the saved CS and IP values are equal."
sources: ["MHE INTR slides 11-12 (function of 8086 during interrupts)"]
---
**Yes, there is a mistake.** On an interrupt the 8086 pushes in the order FLAGS, CS, IP (then clears IF and TF and fetches the ISR address). The stack is **LIFO**, so the return (IRET) must pop in the **reverse order**:

```text
POP IP      ; last pushed, first popped
POP CS
POP FLAGS
```

The figure pops **CS first and then IP**. The first POP takes the saved **IP** value from the top of the stack and loads it into CS, and the second takes the saved **CS** value into IP. CS and IP are swapped, so execution returns to the wrong address $IP_{old}\times10H + CS_{old}$ instead of $CS_{old}\times10H + IP_{old}$. FLAGS is still restored correctly because it is popped last.

**When it still works:** only when the **saved CS and IP values are equal** (CS = IP at the moment of the interrupt, e.g. CS = IP = 1234H). Swapping two equal values changes nothing, so the program resumes at the correct place.

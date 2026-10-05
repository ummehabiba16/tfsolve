---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Top of stack = SS x 10H + SP = 12340H + 4321H = 16661H."
sources: ["MHE 8086-Memory_Organization slides 11-13 (physical address calculation; SS with SP)"]
---
The top of the stack is at SS:SP. Physical address = segment $\times$ 10H + offset:

$$12340H + 4321H = \mathbf{16661H}$$

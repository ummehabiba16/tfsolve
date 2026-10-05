---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Real mode (8086, and 286/386 in real mode): the interrupt vector table at 00000H-003FFH has 256 four-byte vectors; type n is at 4n: IP = [4n], CS = [4n + 2]. Protected mode (286/386): the IDT, located by IDTR (base, limit), has 8-byte gate descriptors; entry n at IDTR.base + 8n is an interrupt, trap or task gate giving the selector and offset of the ISR (the selector is then looked up in the GDT/LDT)."
sources: ["MHE INTR slides 13-15 (interrupt vector table)", "Brey, The Intel Microprocessors, Sec. 12-1 and 17-3 (vector table; IDT and interrupt descriptors)"]
---
Every interrupt has a **type number** $n$ (0-255). The processor uses $n$ to find the ISR address in a table.

**8086 (and 80286/80386 in real mode): Interrupt Vector Table**

- The table is at **00000H-003FFH** (first 1 KB of memory): 256 vectors of **4 bytes**.
- Vector $n$ is at address **$4n$**: the **IP** (offset) is the word at $4n$ and the **CS** (segment) is the word at $4n + 2$.
- ISR address = CS $\times$ 10H + IP.

*Example:* type 21H: vector at $4 \times 21H = 84H$; IP = word [00084H], CS = word [00086H].

**80286 / 80386 in protected mode: Interrupt Descriptor Table (IDT)**

- The IDT can be anywhere in memory; its base and limit are in the **IDTR** register (loaded with `LIDT`).
- Each entry is an **8-byte gate descriptor**; entry $n$ is at **IDTR.base + $8n$**.
- The gate (interrupt gate, trap gate or task gate) contains a **code-segment selector** and an **offset** (16-bit on the 286, 32-bit on the 386) of the ISR, plus DPL and type.
- The selector is looked up in the GDT/LDT to get the segment base; ISR address = base + offset. A task gate instead names a TSS, and the processor switches to that task.

```text
 real mode:       n --> 4n --> [IP][CS] --> ISR = CS x 10H + IP
 protected mode:  n --> IDTR.base + 8n --> gate {selector, offset}
                    --> GDT/LDT descriptor base + offset = ISR
```

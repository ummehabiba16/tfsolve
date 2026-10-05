---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Each interrupt has a type n (0-255): fixed for internal ones and NMI (2), given in INT n, or read from the data bus during the INTA' cycles for INTR. The ISR address is in the interrupt vector table at 00000H-003FFH: IP = word at 4n, CS = word at 4n + 2; ISR = CS x 10H + IP."
sources: ["MHE INTR slides 13-15 (interrupt vectors and vector table, type numbers)"]
---
1. **Type number.** Every interrupt has a **type number** $n$ from 0 to 255:
   - predefined internal interrupts and NMI have fixed types (divide error 0, single step 1, NMI 2, breakpoint 3, overflow 4);
   - a software interrupt gives it in the instruction: `INT n`;
   - for a hardware interrupt on **INTR**, the 8086 runs two $\overline{INTA}$ bus cycles and the interrupting device (or an 8259A) puts $n$ on D7-D0 in the second one.
2. **Interrupt vector table (IVT).** The first 1 KB of memory, **00000H-003FFH**, holds 256 **interrupt vectors** (pointers) of 4 bytes each.
3. **Locate the vector:** vector $n$ starts at address $4n$:
   - **IP** (offset of the ISR) = word at $4n$ (low word);
   - **CS** (segment of the ISR) = word at $4n + 2$ (high word).
4. After pushing FLAGS, CS and IP and clearing IF and TF, the 8086 loads these values, so execution jumps to the **ISR at CS $\times$ 10H + IP**.

*Example:* `INT 21H`: $4 \times 21H = 84H$. If [00084H] = 1234H and [00086H] = 5000H, the ISR starts at 5000H:1234H = 51234H.

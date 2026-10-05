---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Change only the call gate (entry 4) offset field: new entry 4 = 0000 EC00 0028 1234, so the CALL goes to 0028:00001234 (within limit F000h). FF12 is not possible: entry 5's limit is F000h (G = 0), so offset FF12h > F000h causes a general protection fault, and fixing the limit would need a second entry change."
sources: ["Table B and Table C of the paper", "Intel 80386 Programmer's Reference Manual, Sec. 6.3.4 (call gates), Sec. 6.3.1 (limit checking)"]
---
**Modification for offset 1234h**

With a call gate, the entry offset comes from the **gate**, not from the instruction. So only the gate, **GDT entry 4**, must change: its destination offset bits 15-0 (and 63-48) are set to 0000 1234h; the selector (0028h), P, DPL and type stay the same.

| Entry | Old value | New value |
|:-:|:-:|:-:|
| 4 | 0000 EC00 0028 4672 | **0000 EC00 0028 1234** |

Now `call 0020:00ABCDEF` goes through the gate to **0028:00001234**. The offset 1234h $\le$ limit F000h of entry 5, so it is valid (linear address 021FFFFFh + 1234h = 02201233h).

**Is offset FF12h possible?** **No.** The destination segment (entry 5) has limit 0F000h with G = 0 (byte granularity), so valid offsets are 0000h-F000h. FF12h > F000h, so the processor would raise a **general protection fault** when it loads EIP. Making it work would require also raising the limit of entry 5 (e.g. to FFFFh), i.e. changing a **second** GDT entry, which is not allowed. The base cannot help either, because the offset itself is what is checked against the limit.

*Note:* the scanned digit may be read as FE12h; that is also above F000h, so the answer is the same.

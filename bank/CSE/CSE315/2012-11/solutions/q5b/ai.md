---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) GDT = 4 entries x 8 bytes = 32 bytes, so GDTR.limit = 001FH. (ii) DS = 000BH: index 1, TI = 0, RPL 3 -> GDT entry 1 = base 0010FFFFH, limit 10000H, access E1H = P 1, DPL 3, S = 0, type 1: a system (16-bit available TSS) descriptor, not a data segment, so loading DS causes a general protection fault: the instruction does not execute. (iii) No: the only entry covering the GDT is entry 3 (base 0000FFFFH = GDTR base), but it is also a system (TSS) descriptor, so no data segment register can map the GDT; an entry with a data-type access byte (e.g. F2H) would be needed."
sources: ["MHE 80286 slides (selector, access right byte bits P, DPL, S, E, ED, W)", "MHE 80386-updated slides 17-20 (descriptor format)", "Intel 80386 Programmer's Reference Manual, Sec. 6.3.1.1 and Table 6-1 (loading segment registers; system descriptor types)"]
---
**Decoding the GDT entries** (Table B layout: base 31-24 | G D 0 AV lim 19-16 | access | base 23-0 | limit 15-0)

| Entry | Value | Base | Limit (G = 0) | Access byte | Meaning |
|:-:|:--|:-:|:-:|:-:|:--|
| 1 | 0031 E1 10FFFF 0000 | 0010FFFFH | 10000H | E1H = 1 11 0 0001 | P = 1, DPL = 3, **S = 0**, type 1 |
| 2 | 0031 E1 01FFFF 0000 | 0001FFFFH | 10000H | E1H | same type |
| 3 | 0031 E1 00FFFF 0000 | 0000FFFFH | 10000H | E1H | same type |

S = 0 means a **system** descriptor; type 0001 is an **available 16-bit TSS**. None of the three is a code or data segment.

**(i) GDTR limit.** The GDT has 4 entries (0-3) of 8 bytes = 32 bytes, so

$$\text{GDTR.limit} = 4 \times 8 - 1 = \mathbf{001FH}$$

**(ii) Using DS = 000BH**

000BH = 0000 0000 0000 1 | 0 | 11: **index 1**, TI = 0 (GDT), **RPL = 3**.

- The descriptor is inside the GDT limit (offset 8-15 $\le$ 1FH) and present, and its DPL 3 satisfies $\max(CPL, RPL) \le DPL$ for any CPL.
- **But it is a system descriptor (TSS), not a data segment.** DS, ES, FS and GS may be loaded only with data segments (or readable code segments). Loading DS with this selector causes a **general protection fault (#GP)**, so the instruction will **not execute successfully** for reading or writing data.

(If the access byte were F1H/F3H instead, i.e. a data segment with DPL 3, the access would succeed: base 0010FFFFH, offsets up to 10000H.)

**(iii) Reading the GDT itself**

The GDT starts at linear address 0000FFFFH (GDTR.base) and is 32 bytes long. To read it with normal instructions, a **data segment descriptor whose range covers 0000FFFFH-0001001EH** must be loaded into a data segment register.

- **Entry 3** has exactly the right range (base 0000FFFFH = GDTR.base, limit 10000H), but it is a TSS (system) descriptor, so it cannot be loaded into DS/ES/FS/GS.
- Entries 1 and 2 do not cover the GDT and are also system descriptors.

So with this configuration it is **not possible** to read the GDT. It would become possible by changing entry 3's access byte to a data type, e.g. **F2H** (present, DPL 3, writable data) or 92H (DPL 0), and then loading DS = 0018H/001BH (index 3) so that DS:0000-DS:001F addresses the GDT.

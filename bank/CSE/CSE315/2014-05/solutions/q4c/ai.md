---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "80386 extends the 286 registers: 32-bit EAX-EDI, ESP, EBP, EIP and EFLAGS (new VM and RF flags); two extra data segment registers FS and GS; descriptor caches with 32-bit base and limit; control registers CR0 (286 MSW extended with PG etc.), CR2 and CR3 for paging; debug registers DR0-DR7 and test registers TR6-TR7; GDTR/IDTR with 32-bit bases."
sources: ["MHE 80386-updated slides 8-10 (registers overview: extended registers, FS/GS, descriptor registers, CR0-CR3, debug registers, VM and RF flags, test registers)"]
---
| Register group | 80286 | 80386 |
|:--|:--|:--|
| General purpose | 16-bit AX, BX, CX, DX, SP, BP, SI, DI | **32-bit** EAX, EBX, ECX, EDX, ESP, EBP, ESI, EDI (low 16 bits still usable as AX ...) |
| Instruction pointer | 16-bit IP | **32-bit EIP** |
| Flags | 16-bit FLAGS (with IOPL, NT) | **32-bit EFLAGS**, new **VM** (virtual 8086 mode) and **RF** (resume) flags |
| Segment registers | CS, DS, ES, SS | CS, DS, ES, SS plus **FS and GS** (two more data segments) |
| Descriptor caches (invisible) | 24-bit base, 16-bit limit | **32-bit base, 32-bit limit** + attributes (73 bits each) |
| Control registers | 16-bit MSW (PE, MP, EM, TS) | **CR0** (32-bit, MSW in the low half, plus **PG**, ET), **CR2** (page-fault linear address), **CR3** (page directory base); CR1 reserved |
| System address registers | GDTR, IDTR (24-bit base), LDTR, TR | GDTR, IDTR with **32-bit base**, LDTR, TR |
| Debug registers | none | **DR0-DR7** (4 hardware breakpoint addresses, status, control) |
| Test registers | none | **TR6, TR7** (testing the TLB) |

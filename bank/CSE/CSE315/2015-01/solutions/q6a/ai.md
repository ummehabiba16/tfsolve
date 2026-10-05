---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "80286 memory management = segmentation with descriptors (no paging). Real mode: 1 MB, segment x 16 + offset. Protected mode: segment registers hold selectors (index, TI, RPL) pointing to 8-byte descriptors in the GDT or LDT (GDTR, LDTR) with 24-bit base, 16-bit limit and access rights, cached in hidden registers; physical = base + offset (16 MB). Provides relocation, protection (limits, types, privilege levels), task isolation via LDTs, and virtual memory of 1 GB per task via the present bit and segment swapping."
sources: ["MHE 80286 slides (real and protected mode, selectors, GDT/LDT, descriptors, shadow registers, privilege levels)", "Brey, The Intel Microprocessors, Sec. 2-3 and Ch. 17"]
---
**Real address mode:** the 80286 behaves like an 8086: 20-bit address = segment $\times$ 10H + offset, 1 MB, no protection.

**Protected virtual address mode:** memory is managed by **segmentation with descriptors**.

1. **Selectors.** A segment register holds a 16-bit selector: index (13 bits), TI (0 = GDT, 1 = LDT), RPL (2 bits).
2. **Descriptor tables.**
   - **GDT** (global): system-wide segments, located by **GDTR** (24-bit base, 16-bit limit).
   - **LDT** (local): one per task, located through **LDTR** (a selector to an LDT descriptor in the GDT).
   - **IDT**: interrupt gates, located by **IDTR**.
3. **Descriptors (8 bytes):** 24-bit **base**, 16-bit **limit** (segments up to 64 KB), **access rights** (present, DPL, code/data, readable/writable, accessed).
4. **Descriptor cache (shadow registers).** When a selector is loaded, the descriptor is copied into the segment register's hidden part, so translation is fast.
5. **Address translation:** physical address = descriptor base + offset (offset $\le$ limit), anywhere in **16 MB** (24-bit address bus).

```text
 selector --> GDT/LDT[index] --> {base, limit, rights} --> base + offset = physical (24-bit)
```

**Features provided**

- **Relocation:** a segment can be moved by changing only its descriptor base.
- **Protection:** limit checks, type checks (no writing code, no executing data), 4 **privilege levels** (CPL/DPL/RPL, call gates for entering more privileged code), IOPL for I/O.
- **Task isolation and switching:** separate LDTs per task; TSS and task switching in hardware.
- **Virtual memory:** a task can address 8K global + 8K local segments of 64 KB = **1 GB** virtual. A descriptor with P = 0 marks a segment that is on disk; accessing it causes a "segment not present" exception, so the OS loads it (segment swapping).

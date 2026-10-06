---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "TLB = hardware cache of VPN-to-PFN translations (fully associative); on a context switch flush it or tag entries with an ASID."
sources: ["OSTEP ch. 19 (TLBs, figs 19.1-19.2, context switches)"]
---
**What it is.** The **translation-lookaside buffer** is a small, fast, hardware cache of recent virtual-to-physical translations that is part of the MMU. Without it every memory reference would first need an extra memory access to read the page-table entry (PTE).

**Structure.** A TLB is usually *fully associative*: any translation can be in any entry and all entries are searched in parallel. An entry looks like

| VPN | PFN | valid | protection bits | dirty | ASID |
|:-:|:-:|:-:|:-:|:-:|:-:|
| virtual page number | physical frame number | entry in use? | r/w/x | written? | address-space id |

**Control flow** (hardware-managed TLB, OSTEP Fig. 19.1):

```text
VPN = (VirtualAddress & VPN_MASK) >> SHIFT
(Success, TlbEntry) = TLB_Lookup(VPN)
if (Success == True)                      // TLB hit
    if (CanAccess(TlbEntry.ProtectBits) == True)
        Offset   = VirtualAddress & OFFSET_MASK
        PhysAddr = (TlbEntry.PFN << SHIFT) | Offset
        Register = AccessMemory(PhysAddr)
    else
        RaiseException(PROTECTION_FAULT)
else                                       // TLB miss
    PTEAddr = PTBR + (VPN * sizeof(PTE))
    PTE = AccessMemory(PTEAddr)
    if (PTE.Valid == False)
        RaiseException(SEGMENTATION_FAULT)
    else if (CanAccess(PTE.ProtectBits) == False)
        RaiseException(PROTECTION_FAULT)
    else
        TLB_Insert(VPN, PTE.PFN, PTE.ProtectBits)
        RetryInstruction()
```

**Context switches.** The TLB contains translations for the *current* process only; the same VPN means different frames in different processes. Two solutions:

1. **Flush** the TLB on every context switch (set all valid bits to 0). Simple, but the new process starts with a cold TLB and suffers many misses.
2. Add an **address-space identifier (ASID)** to each entry. The hardware compares the ASID with the current process's ASID (kept in a register), so entries of several processes can coexist and nothing needs to be flushed. Shared pages can even appear twice with different ASIDs, pointing to the same PFN.

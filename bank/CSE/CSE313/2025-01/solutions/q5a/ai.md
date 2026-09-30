---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
changes:
  - "2026-09-30 (import review): added the reading where the process's own pages are counted too."
---
This is the OSTEP "small address space" example: $16$KB $/$ $64$B pages $=256$ pages, so VPN is 8 bits, offset is 6 bits. PTE $=4$B.

**(i) Single-level page table.** Must have one entry for every possible VPN regardless of use: $256\times4\text{B}=\mathbf{1024\,B\;(1\,KB)}$.

**(ii) Two-level page table.** Split the 8-bit VPN into a 4-bit page-directory (PD) index and a 4-bit page-table (PT) index (16 entries each -- this makes each page-table page exactly $16\times4\text{B}=64$B, i.e. exactly one page, the standard OSTEP design choice).

- Code (VPN 0,1): PD index $=0$.

- Heap (VPN 4--32, 29 pages): PD index $0$ (VPN 4--15, 12 pages), PD index $1$ (VPN 16--31, 16 pages, fully populated), PD index $2$ (VPN 32, 1 page).

- Stack (VPN 254,255): PD index $=15$.

So valid PD entries $=\{0,1,2,15\}$ -- **4** out of 16.

- **Page directory**: always fully allocated, $16\times4\text{B}=64$B.

- **Page tables**: one per valid PD entry $\to 4$ tables $\times64$B (16 entries$\times$ 4B) $=256$B.

**Total** $=64+256=\mathbf{320\,B}$.

*If* "physical memory used by the process" is read as page tables **plus** the process's own pages: it uses $2+29+2=33$ pages $\times\,64$B $=2112$B, giving $1024+2112=3136$B (single-level) and $320+2112=2432$B (two-level). The page-table comparison is the point of the question either way.

(Compare: 1024B single-level vs. 320B two-level -- again the saving comes from not allocating page-table space for the large unused middle region of the 256-page address space.)

---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
Disk $=16$TB, block $=4$KB $\Rightarrow$ number of blocks $=\dfrac{16\text{TB}}{4\text{KB}}=\dfrac{2^{44}}{2^{12}}=2^{32}$ blocks, so a block address needs exactly $32$ bits $=4$ bytes -- i.e. each pointer (direct or indirect) is $4$B.

Pointers per indirect block $=\dfrac{4096\text{B (block size)}}{4\text{B (pointer size)}}=1024$.

**Direct pointers (6):** $6\times4\text{KB}=24{,}576$B.

**Single-indirect pointers (2):** each single-indirect block holds 1024 pointers to data blocks $\Rightarrow$ each covers $1024\times4\text{KB}=4$MB. With 2 of them: $2\times4\text{MB}=8$MB $=8{,}388{,}608$B.

**Double-indirect pointers (5):** each double-indirect block holds 1024 pointers to single-indirect blocks, each of which holds 1024 pointers to data blocks $\Rightarrow$ each double-indirect pointer covers $1024\times1024\times4\text{KB}=4$GB. With 5 of them: $5\times4\text{GB}=20$GB $=21{,}474{,}836{,}480$B.

**Maximum file size** $=24{,}576 + 8{,}388{,}608 + 21{,}474{,}836{,}480 = \mathbf{21{,}483{,}249{,}664\text{ bytes} \approx 20.006\text{ GiB} \approx 20\text{ GB}}$.

This ($\approx20$GB) is the binding limit imposed by the inode's own pointer structure, far smaller than the 16TB disk itself -- i.e. the file-size ceiling here comes from the addressing scheme, not from available disk capacity.

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(12 + 1024 + 1024^2) blocks x 4 KB = 4,299,210,752 bytes, about 4.004 GB."
sources: ["OSTEP ch. 40 (multi-level index)", "Tanenbaum MOS 4e, sec. 4.3.2 (i-nodes)"]
---
Block size $=4\text{ KB}$; a block address is 32 bits $=4$ bytes, so a pointer block holds $4096/4 = 1024$ pointers.

| Pointers | Data blocks addressed |
|:--|:-:|
| 12 direct | 12 |
| 1 single indirect | $1024$ |
| 1 double indirect | $1024^2 = 1{,}048{,}576$ |
| **Total** | $1{,}049{,}612$ |

$$\text{max file size} = 1{,}049{,}612\times 4096\text{ B} = 4{,}299{,}210{,}752\text{ B}$$

$$= 48\text{ KB} + 4\text{ MB} + 4\text{ GB} \approx \mathbf{4.004\ GB}$$

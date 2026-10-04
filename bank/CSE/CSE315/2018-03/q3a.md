---
marks: 20
topics: [call-gates, privilege-protection]
kind: conceptual
source: {page: 65-66}
---
Identify whether the following statements are True or False and justify your answer.

| Serial | Statement |
|:-:|:--|
| (i) | There are a total of 4 Privilege levels. |
| (ii) | You can transfer control only to a code that is equal or lower in privilege than yours |
| (iii) | Transferring control always triggers selector validation. |
| (iv) | When you (with PL = 2) have passed through a call gate and the control has just been transferred to a higher PL code (PL = 1), your data segments will initially have DPL < 1. |
| (v) | Suppose a caller code (PL = 2) used a call gate to run a callee code at PL = 1. When the control will have returned to the caller, the RPL field of the DS register will have 00. |
| (vi) | RPL of CS is always maintained to be the CPL, hence, RPL will always match the DPL of the current code segment. |
| (vii) | The only way to change the CPL is to use Call Gate. |
| (viii) | When you have a call gate, you can transfer the control anywhere in the segment pointed by the destination selector of the call gate. |
| (ix) | You can never use a FAR JMP to use a call gate. |
| (x) | If you are at PL2 and there is no call gate with gate DPL = 2, you will never be able to transfer control to a code segment with PL < 2. |

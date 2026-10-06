---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Instructions are 8 bytes, actions 80 bytes. m: 100 LD SP,#1000; 108 action 1; 188 ADD SP,SP,#128; 196 ST *SP,#212; 204 BR 400; 212 SUB SP,SP,#128; 220 action 2; 300 HALT. p: 400 action 3; 480 BR *0(SP)."
sources: ["KMS Chapter 8 slides (target code for procedures, stack allocation)", "Dragon book 2e sec. 7.3.3, 8.3.2 (code for stack allocation)"]
---
**Assumptions.** The target machine is byte addressable with an 8-byte word; each instruction occupies **one word (8 bytes)**; an *action* occupies **80 bytes**. The registers `SP` (stack pointer) holds the address of the activation record of the running procedure. The activation record of `m` is 128 bytes and that of `p` is 256 bytes; the first word of a record holds the return address. The calling sequence of `m` (the caller) increments `SP` by the size of its own record, stores the return address at the top of the new record, and jumps; the return sequence of `p` jumps back through the saved address (Dragon book sec. 7.3.3, 8.3.2).

**Target code with comments:**

| Address | Code | Comment |
|:-:|:--|:--|
| | `/* code for m */` | |
| 100 | `LD SP, #1000` | initialise the stack: the first record (that of `m`) starts at 1000 |
| 108 | `action 1` | 80 bytes: addresses 108 to 187 |
| 188 | `ADD SP, SP, #128` | start of the call sequence: `SP` moves past `m`'s record (128 bytes), so it points to the new record of `p` (address 1128) |
| 196 | `ST *SP, #212` | store the **return address** (212 = address of the instruction after the call) in the first word of `p`'s record |
| 204 | `BR 400` | **call** `p`: jump to the code of `p` |
| 212 | `SUB SP, SP, #128` | after the return: restore `SP` to `m`'s record (1000) |
| 220 | `action 2` | 80 bytes: addresses 220 to 299 |
| 300 | `HALT` | end of the program |
| | `/* code for p */` | |
| 400 | `action 3` | 80 bytes: addresses 400 to 479 |
| 480 | `BR *0(SP)` | **return**: jump to the address stored at the top of `p`'s record (212) |

**Address arithmetic.** $100 + 8 = 108$; $108 + 80 = 188$; $188 + 8 = 196$; $196 + 8 = 204$; $204 + 8 = 212$ (so 212 is the instruction after `BR 400`, the return address); $212 + 8 = 220$; $220 + 80 = 300$; $400 + 80 = 480$.

**Stack during the call.** `m`'s record: 1000 to 1127. After `ADD SP, SP, #128`, `SP = 1128`: `p`'s record occupies 1128 to 1383 (256 bytes); the return address 212 is at 1128. The size of `p`'s record (256) would be used by `p` in its own calling sequence if it called another procedure; here `p` calls none, so only `m`'s size appears in the code.

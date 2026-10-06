---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "An activation record (frame) is the block of storage, usually on the run-time stack, holding the information for one execution (activation) of a procedure. It typically contains actual parameters, the returned value, a control link (caller's record), an access link (non-local data), saved machine status (return address, registers), local data, and temporaries."
sources: ["KMS Chapter 7 slides 17-18 (Activation Records)", "Dragon book 2e sec. 7.2.3 (Fig. 7.5)"]
changes:
  - "2026-10-06: added TikZ figure (figures/record.png) for the activation record layout; the answer itself is unchanged."
---
**Activation record.** Each call (activation) of a procedure needs storage for its parameters, local variables and bookkeeping information. This block of storage is the **activation record** (or frame). In a language with stack allocation, an activation record is pushed on the control stack when the procedure is called and popped when it returns. The record of the currently running procedure is on top.

**Data usually stored** (a typical layout, from the caller's side down):

| Field | Contents |
|:--|:--|
| Actual parameters | Values supplied by the caller (often passed in registers when possible) |
| Returned value | Space for the value the callee returns (also often a register) |
| Control link | Points to the activation record of the **caller** |
| Access link | Points to the record of the lexically enclosing procedure, to reach non-local data (needed in languages with nested procedures) |
| Saved machine status | Return address (value of the program counter to return to) and the contents of registers to be restored |
| Local data | The procedure's local variables |
| Temporaries | Intermediate values of expressions, e.g. those that could not be kept in registers |

![Layout of an activation record](figures/record.png)

Not every language or compiler uses every field; for example, C needs no access links.

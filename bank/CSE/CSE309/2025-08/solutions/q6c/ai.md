---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "An activation record holds actual parameters, returned value, control link, access link, saved machine status (return address, registers), local data and temporaries. The calling sequence allocates the AR and fills it in (caller: parameters, return address, old top\\_sp; callee: saved registers, locals); the return sequence restores the machine state and returns control (callee stores the result, restores top\\_sp and registers, jumps to the return address; caller reads the result). Principles: values exchanged between caller and callee go at the start of the callee's AR, fixed-length items (control link, access link, machine status) in the middle, variable-length items at the end, and top\\_sp points to the end of the fixed-length fields."
sources: ["KMS Chapter 7 slides 17-27 (Activation Records, Calling and Return Sequence, Principles of Designing Calling Sequences)", "Dragon book 2e sec. 7.2.3-7.2.4 (Figs. 7.5, 7.7)"]
---
**Contents of an activation record (AR)** for one call of a procedure, from the caller's end to the callee's end:

| Field | Purpose |
|:--|:--|
| Actual parameters | Values (or addresses) passed by the caller |
| Returned value | Space for the value returned to the caller |
| Control link | Pointer to the caller's AR (dynamic link) |
| Access link | Pointer to the AR of the enclosing procedure, for non-local data (nested languages) |
| Saved machine status | Return address (old program counter) and registers that must be restored |
| Local data | The procedure's local variables |
| Temporaries | Values of expressions that do not fit in registers |

**Calling sequence:** the code that **allocates** an AR on the stack and **enters** information in its fields when a procedure is called. Part is executed by the caller, part by the callee:

1. The caller evaluates the actual parameters and stores them in the callee's AR.
2. The caller stores the return address and the old value of `top_sp` in the callee's AR, then increments `top_sp` past the caller's locals and the callee's fixed fields.
3. The callee saves register values and other status information.
4. The callee initialises its local data and begins execution.

**Return sequence:** the code that **restores the machine state** so the caller can continue:

1. The callee places the return value next to the parameters.
2. Using the information in the machine-status field, the callee restores `top_sp` and the other registers, then branches to the return address the caller placed there.
3. The caller copies the returned value into its own AR (it knows where it is relative to `top_sp`), although `top_sp` has been decremented.

**Guiding principles for calling sequences and AR layout:**

1. **Values communicated between caller and callee are placed at the beginning of the callee's AR**, as close as possible to the caller's AR. The caller can then compute their addresses without knowing the callee's full layout (e.g. its number of locals).
2. **Fixed-length items** (control link, access link, machine-status fields) are placed **in the middle**. The same code can save and restore them for every call, and debuggers can decode the stack.
3. **Items whose size may not be known early** (local arrays with dynamic size, temporaries) are placed **at the end** of the AR.
4. **`top_sp` points to the end of the fixed-length fields** (the start of the local data). Fixed fields are then reached at fixed negative offsets and locals at fixed positive offsets, while variable-length data can follow.
5. **Division of work:** do as much as possible in the **callee**. Its code appears once, while the calling-sequence code is repeated at every call site, so this keeps programs smaller.

---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Activations must be properly nested in time: if p calls q, q's activation ends before p's (LIFO), and no local value is needed after its activation ends. Violated by first-class nested functions/closures that outlive their creator (e.g. a function returning an inner function that uses the outer function's local variable, as in ML, JavaScript, Python), and by coroutines/threads. Calling sequence: code that allocates an activation record and fills in its fields at a call; return sequence: code that restores the caller's state and returns control."
sources: ["KMS Chapter 7 slides 9-29 (Stack Allocation, Activation Tree, Calling and Return Sequence, Procedures Not Nesting in Time)", "Dragon book 2e sec. 7.2, 7.3.5"]
---
**Condition for stack allocation (6 marks).** Procedure activations must be **properly nested in time**: if an activation of $p$ calls $q$, then that activation of $q$ ends **before** the activation of $p$ ends. Lifetimes follow a last-in, first-out order, so they can be represented by an activation tree. The activation records can then be pushed when a procedure is called and popped when it returns, and the space for an activation's local data can be reused as soon as it returns.

Equivalently: **no local data of an activation is needed after that activation has ended**. Otherwise, popping the record would destroy values that are still in use.

**A feature that violates it (6 marks): first-class nested functions (closures)** that can outlive the activation that created them, e.g. in ML, JavaScript or Python:

```javascript
function makeCounter() {
    var count = 0;              // local of makeCounter
    return function () {        // inner function uses count
        count = count + 1;
        return count;
    };
}
var c = makeCounter();          // makeCounter's activation has ended ...
c(); c();                       // ... but count is still used: 1, 2
```

After `makeCounter` returns, its activation record would be popped, but the returned function still refers to `count`. So the record (or at least `count`) must stay alive, for example on the **heap**, and cannot live purely on a runtime stack. Other examples: coroutines and generators, which suspend and resume an activation; threads; and returning a pointer to a local variable in C, which is an error precisely because the stack is used.

**Calling and return sequences (5 marks).**

- **Calling sequence:** the code that **allocates an activation record** on the stack and **enters information** into its fields when a procedure is called. The caller evaluates the actual parameters, stores them and the return address, saves the old `top_sp`, and advances `top_sp`. The callee saves registers and status information and initialises its local data.
- **Return sequence:** the code that **restores the state of the machine** so the caller can continue. The callee places the return value, restores `top_sp` and the saved registers, and jumps to the return address. The caller then picks up the returned value.

The work is split between caller and callee. Since the callee's code appears only once, as much as possible is put there.

---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Backpatching generates the jump instructions of short-circuit code without knowing their targets: each jump is emitted as 'goto _' and put on a truelist or falselist; when the target label becomes known the lists are patched. Scheme: B -> B1 || M B2 {backpatch(B1.falselist, M.instr); B.truelist = merge(...); B.falselist = B2.falselist}, B -> B1 && M B2, B -> E1 rel E2 {makelist(nextinstr), makelist(nextinstr+1); emit if/goto}, M -> eps {M.instr = nextinstr}."
sources: ["KMS Chapter 6 slides 104-114 (Backpatching)", "Dragon book 2e sec. 6.6.2, 6.7.1-6.7.2"]
---
**Short-circuit code** evaluates a boolean expression by jumps alone: in $B_1 \mathbin{\vert\vert} B_2$, if $B_1$ is true the whole expression is true without evaluating $B_2$; in $B_1 \,\&\&\, B_2$, if $B_1$ is false the expression is false (Dragon book sec. 6.6.2).

**The problem.** In one pass, when a jump is generated its target label may not exist yet (it is a forward jump). With inherited labels $B.true$ and $B.false$ we need to know them before translating $B$, which is not possible in bottom-up parsing.

**Backpatching** (sec. 6.7): emit each incomplete jump as `goto _` (target left blank) and remember its instruction index in a **list**; when the target becomes known, fill the target into all instructions on the list. Each boolean expression $B$ gets two **synthesized** attributes:

- $B.truelist$: indexes of the jumps that must go to the code run when $B$ is true;
- $B.falselist$: the same for false.

Helper functions: $makelist(i)$ creates a list containing instruction $i$; $merge(p_1, p_2)$ concatenates two lists; $backpatch(p, i)$ sets the target of every instruction on $p$ to $i$. $nextinstr$ is the index of the next instruction to be generated. A marker nonterminal $M \to \epsilon$ records the index of the instruction that starts $B_2$.

**Translation scheme.**

| Production | Action |
|:--|:--|
| $B \to B_1\ \vert\vert\ M\ B_2$ | $backpatch(B_1.falselist, M.instr);\ B.truelist = merge(B_1.truelist, B_2.truelist);\ B.falselist = B_2.falselist$ |
| $B \to B_1\ \&\&\ M\ B_2$ | $backpatch(B_1.truelist, M.instr);\ B.truelist = B_2.truelist;\ B.falselist = merge(B_1.falselist, B_2.falselist)$ |
| $B \to !\ B_1$ | $B.truelist = B_1.falselist;\ B.falselist = B_1.truelist$ |
| $B \to (\ B_1\ )$ | $B.truelist = B_1.truelist;\ B.falselist = B_1.falselist$ |
| $B \to E_1\ rel\ E_2$ | $B.truelist = makelist(nextinstr);\ B.falselist = makelist(nextinstr + 1);$ emit(`if` $E_1.addr$ $rel.op$ $E_2.addr$ `goto _`); emit(`goto _`) |
| $B \to \textbf{true}$ | $B.truelist = makelist(nextinstr);$ emit(`goto _`) |
| $B \to \textbf{false}$ | $B.falselist = makelist(nextinstr);$ emit(`goto _`) |
| $M \to \epsilon$ | $M.instr = nextinstr$ |

**Example: `x < 100 || x > 200 && x != y`**, instructions starting at 100.

1. `x < 100` ($B_1$) emits `100: if x < 100 goto _` and `101: goto _`; truelist $\{100\}$, falselist $\{101\}$.
2. $M_1.instr = 102$.
3. `x > 200` emits `102: if x > 200 goto _`, `103: goto _`; truelist $\{102\}$, falselist $\{103\}$.
4. $M_2.instr = 104$.
5. `x != y` emits `104: if x != y goto _`, `105: goto _`; truelist $\{104\}$, falselist $\{105\}$.
6. `&&` reduces: $backpatch(\{102\}, 104)$, so 102 jumps to 104 (if `x > 200` is true, test `x != y`); truelist $\{104\}$, falselist $\{103, 105\}$.
7. `||` reduces: $backpatch(\{101\}, 102)$, so 101 jumps to 102 (if `x < 100` is false, try the right operand); truelist $\{100, 104\}$, falselist $\{103, 105\}$.

```text
100: if x < 100 goto _        (true: truelist)
101: goto 102
102: if x > 200 goto 104
103: goto _                    (false: falselist)
104: if x != y goto _          (true: truelist)
105: goto _                    (false: falselist)
```

The lists $\{100, 104\}$ and $\{103, 105\}$ are patched later, when the code for the `then` part and the code following the statement are known. No inherited attributes were needed, so the scheme works in a single pass with an LR parser.

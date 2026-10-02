---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Procedures S() (a/d: A() match a; b: match b B() match b; c: match c), A() (a: match a A(); d: match d match d), B() (b: match b; e: match e B() match e; else eps). For bebeb: S sees b, uses S -> bBb; B sees e, uses B -> eBe; inner B sees b, uses B -> b; then e and b are matched: accepted. Note the grammar is not LL(1) (b and e are in FOLLOW(B)), so using eps only as the default can fail on other inputs such as bb."
sources: ["MMA basic concepts of parsing slides 23-49 (Predictive Parsing, When to Use eps-Productions)", "Dragon book 2e sec. 2.4.2-2.4.3, 4.4.1"]
---
**FIRST/FOLLOW used for the choices:**

| Nonterminal | Alternatives (FIRST) | FOLLOW |
|:--|:--|:--|
| $S$ | $Aa$: {a, d}; $bBb$: {b}; $c$: {c} | {\$} |
| $A$ | $aA$: {a}; $dd$: {d} | {a} |
| $B$ | $b$: {b}; $eBe$: {e}; $\epsilon$ | {b, e} |

**Parser (8 marks):**

```c
int lookahead;                 /* current token */

void match(int t) {
    if (lookahead == t) lookahead = nextToken();
    else error();
}

void S() {
    switch (lookahead) {
    case 'a': case 'd': A(); match('a'); break;          /* S -> A a   */
    case 'b': match('b'); B(); match('b'); break;        /* S -> b B b */
    case 'c': match('c'); break;                         /* S -> c     */
    default:  error();
    }
}

void A() {
    if (lookahead == 'a') { match('a'); A(); }          /* A -> a A */
    else if (lookahead == 'd') { match('d'); match('d'); } /* A -> d d */
    else error();
}

void B() {
    if (lookahead == 'b') match('b');                    /* B -> b     */
    else if (lookahead == 'e') { match('e'); B(); match('e'); } /* B -> e B e */
    /* else B -> eps (default) */
}

int main() {
    lookahead = nextToken();
    S();
    if (lookahead == '$') accept(); else error();
}
```

**Parsing `bebeb` (7 marks):**

| Call / action | Lookahead | Remaining input | Production used |
|:--|:-:|:--|:--|
| `S()` | b | bebeb\$ | $S \to bBb$ |
| `match('b')` | b | bebeb\$ | |
| `B()` | e | ebeb\$ | $B \to eBe$ |
| `match('e')` | e | ebeb\$ | |
| `B()` (nested) | b | beb\$ | $B \to b$ |
| `match('b')` | b | beb\$ | |
| return to outer `B()`; `match('e')` | e | eb\$ | |
| return to `S()`; `match('b')` | b | b\$ | |
| `main`: lookahead is \$ | \$ | \$ | accept |

The calls trace the parse tree **top-down** from the root $S$, expanding children left to right, so the productions used are a **leftmost derivation**:

$$S \Rightarrow bBb \Rightarrow beBeb \Rightarrow bebeb$$

The run-time call stack plays the role of the parse stack.

```text
          S
        / | \
       b  B  b
        / | \
       e  B  e
          |
          b
```

**Remark.** FOLLOW($B$) = {b, e} overlaps FIRST($b$) and FIRST($eBe$), so the grammar is **not LL(1)**. The parser above uses $B \to \epsilon$ only as a default, which works for `bebeb`. For an input like `bb` (via $S \to bBb$, $B \to \epsilon$), `B()` would wrongly choose $B \to b$, and a backtracking or different grammar would be needed.

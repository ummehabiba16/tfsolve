---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Goals: report errors clearly and accurately, recover quickly so later errors are found, and add little cost to the processing of correct programs. Strategies: panic-mode, phrase-level, error productions, global correction. Panic mode: discard input symbols until a synchronizing token (such as ; or end) is found, then resume parsing."
sources: ["MMA syntax analysis slides 2-24 (syntax errors, error recovery)", "Dragon book 2e sec. 4.1.3-4.1.4, 4.4.5"]
---
**Goals of an error-handling strategy** (Dragon book sec. 4.1.3). The error handler of a parser should:

1. **Report the presence of errors clearly and accurately** (the position and the nature of the error);
2. **Recover from each error quickly enough** to detect later errors, and not stop at the first one;
3. **Not significantly slow down** the processing of correct programs.

**Error-recovery strategies in the syntax-analysis phase** (sec. 4.1.4):

| Strategy | Idea |
|:--|:--|
| **Panic-mode recovery** | on an error, discard input symbols one at a time until a *synchronizing token* (delimiters such as `;` or `}`, `end`) is found; then continue |
| **Phrase-level recovery** | perform a local correction of the remaining input: replace a prefix by a string that lets the parser continue (replace `,` by `;`, delete an extra `;`, insert a missing `;`) |
| **Error productions** | extend the grammar with productions for common mistakes so the parser can recognise them and give a diagnostic |
| **Global correction** | choose a minimal sequence of changes that turns the input into a correct program (costly, mostly theoretical) |

**Panic-mode recovery with an example.** The parser skips input until it meets a token from a *synchronizing set* (often $\text{FOLLOW}$ of the nonterminal being parsed, plus statement terminators), then pops stack entries or resumes at that point. Take the statements

```text
a = b + * c ;  d = 5 ;
```

The parser reads `a = b +`, then expects an operand but finds `*`: **error**. In panic mode it reports the error and **discards** `*` and `c` until the synchronizing token `;` is found; it consumes the `;`, treats the statement as finished and resumes by parsing `d = 5 ;` normally. In this way a single error does not hide the following ones. Its advantages: simple, never loops forever; its drawback: it may skip a lot of input (and miss errors in it).

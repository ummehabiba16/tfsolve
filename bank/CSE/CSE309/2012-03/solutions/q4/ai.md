---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(a) aaabccabbb: rule 1 matches aaab (tie with rule 2 on 4 characters, first rule wins) prints 1; cc prints 3; abbb (rule 2 matches 4 characters, rule 1 only 2) prints 2: output 132. (b) cbbbbabc: 3, then bbbbab (rule 2, 6 chars) prints 2, then c prints 3: output 323. (c) cbabc: 3, bab prints 2, c prints 3: output 323."
sources: ["MMA lexical analysis slides 111-148 (Lex conflict resolution)", "Dragon book 2e sec. 3.5.3"]
---
Lex's rules (Dragon book sec. 3.5.3): at each position, take the pattern that matches the **longest** prefix of the remaining input; if several patterns match the same length, take the one listed **first**. The three rules are:

1. `a*b`, action: prints `1`;
2. `(a|b)*b`, action: prints `2`;
3. `c*`, action: prints `3`.

(The patterns cannot match the empty string at a position where a character is available, because a longer or other match exists; no input character is left unmatched here, since every character is `a`, `b` or `c`.)

**(a) `aaabccabbb`**

| Remaining input | Rule 1 | Rule 2 | Rule 3 | Winner | Output |
|:--|:--|:--|:--|:--|:-:|
| `aaabccabbb` | `aaab` (4) | `aaab` (4) | none | tie, first rule: **1** | `1` |
| `ccabbb` | none | none | `cc` (2) | **3** | `3` |
| `abbb` | `ab` (2) | `abbb` (4) | none | longest: **2** | `2` |

Output: **`132`**.

**(b) `cbbbbabc`**

| Remaining input | Rule 1 | Rule 2 | Rule 3 | Winner | Output |
|:--|:--|:--|:--|:--|:-:|
| `cbbbbabc` | none | none | `c` (1) | **3** | `3` |
| `bbbbabc` | `b` (1) | `bbbbab` (6) | none | longest: **2** | `2` |
| `c` | none | none | `c` (1) | **3** | `3` |

Output: **`323`**.

**(c) `cbabc`**

| Remaining input | Rule 1 | Rule 2 | Rule 3 | Winner | Output |
|:--|:--|:--|:--|:--|:-:|
| `cbabc` | none | none | `c` (1) | **3** | `3` |
| `babc` | `b` (1) | `bab` (3) | none | longest: **2** | `2` |
| `c` | none | none | `c` (1) | **3** | `3` |

Output: **`323`**.

*Check:* the three rules were compiled with `flex` and run on the three strings (without a trailing newline); the outputs are `132`, `323` and `323`.

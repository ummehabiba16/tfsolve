---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Make the symbol table key independent of case: convert each identifier to a canonical form (all lower case) before hashing/lookup and insertion, so abc, ABC and aBc map to the same entry; the original spelling may be stored in the entry for messages."
sources: ["MMA compiler phases slides 40-98 (symbol table)", "Dragon book 2e sec. 2.7, 3.1.2"]
---
In a case-insensitive language all spellings of an identifier denote one entity, so they must all find the **same symbol-table entry**. Design:

1. **Normalise the key.** Before every insertion and lookup, convert the lexeme to a canonical form, usually **all lower case** (or all upper case). `abc`, `ABC` and `aBc` all become `abc`. The hash function and the string comparison are applied only to the canonical form (or use a case-insensitive hash and comparison function).
2. **Where to do it.** Either in the **lexical analyzer** (when it recognises an identifier it lower-cases the lexeme before calling the symbol-table routine, and the attribute value of the token is the table entry), or inside the symbol-table `lookup` and `insert` routines. Doing it in the lexer also normalises keywords, so `BEGIN`, `Begin` and `begin` match the same entry of the reserved-word table.
3. **Keep the original spelling** (optional) in a field of the entry (the spelling at the first declaration) for error messages and cross references; it is never used as the key.

```text
lookup("aBc")  ->  key = tolower("aBc") = "abc"  ->  hash("abc")  ->  entry for abc
insert("ABC")  ->  key = "abc" already present   ->  reported as a redeclaration of abc
```

This costs one pass over each identifier to fold its case and needs no change in the rest of the compiler.

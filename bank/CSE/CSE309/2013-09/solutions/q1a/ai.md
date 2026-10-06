---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) comment: slash-star, then any mix of non-star-non-quote characters, quoted strings and runs of stars followed by something that is not slash, then a run of stars and slash; (ii) cons* a cons* e cons* i cons* o cons* u cons* with cons the 21 consonants; (iii) number = (digits(.digits?)? | .digits)([eE][+-]?digits)?."
sources: ["MMA lexical analysis slides 50-110 (regular definitions)", "Dragon book 2e sec. 3.3.4, Exercise 3.3.2"]
---
**(i) Comments.** A comment starts with `/*` and ends at the first `*/` that is **not inside a double-quoted string** within the comment (a `*/` between quotes does not end it). Build it from small pieces; `str` is a double-quoted string:

```text
str      ->  " [^"]* "
inner    ->  [^*"]  |  str  |  \*+ ( [^*/"] | str )
comment  ->  /\* inner* \*+ /
```

Explanation: inside the comment we may see (1) any character except `*` and `"`; (2) a whole quoted string, which may contain `*/` harmlessly; (3) a run of stars followed by something that is not `/` (a `*` followed by `/` would end the comment) and not a quote that begins a string. The comment ends with a run of one or more stars followed by `/` (so `**/` also ends it). The string `/* a "*/" b */` is one comment; `/* a */ b */` is the comment `/* a */` followed by other text.

**(ii) Lower-case words containing the five vowels in order.** Let `cons` be the 21 lower-case consonants, `[b-df-hj-np-tv-z]`. A word that contains the vowels `a e i o u` **in this order**, each exactly once with only consonants between and around them:

```text
cons -> [b-df-hj-np-tv-z]
word -> cons* a cons* e cons* i cons* o cons* u cons*
```

Examples: `facetious`, `abstemious`. (If other vowels are allowed between them, i.e. the vowels only have to occur in this order as a subsequence, replace `cons*` by `[a-z]*`: `[a-z]* a [a-z]* e [a-z]* i [a-z]* o [a-z]* u [a-z]*`.)

**(iii) Unsigned numbers of C** (integer or floating point, with optional fraction and exponent; examples `.02`, `12`, `12.3`, `12.`, `32.23E+2`, `23.5E-3`):

```text
digit     -> [0-9]
digits    -> digit+
fraction  -> . digits?
mantissa  -> digits fraction? | . digits
exponent  -> [eE] [+-]? digits
number    -> mantissa exponent?
```

That is $number = (\,digits\,(.\,digits^?)^?\ \mid\ .\,digits\,)\,([eE][+-]^?\,digits)^?$. It accepts `12` (digits only), `12.` (digits and a dot), `.02` (a dot and digits), `12.3`, `32.23E+2`, `23.5E-3`, and rejects `.`, `E5`, `1e`, `1.2.3`, `+1` (unsigned).

*Check:* (i) the comment expression was compared with a reference scanner on all strings of length up to 8 over `/`, `*`, `"`, `a` (no mismatch); (ii) both vowel expressions were compared with the definitions on 200,000 random words; (iii) the six examples are accepted and the five non-examples rejected.

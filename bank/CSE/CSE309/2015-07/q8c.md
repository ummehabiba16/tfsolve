---
marks: 20
topics: [first-follow, ll1, table-driven-ll]
kind: numerical
source: {page: 54}
note: "The input string is blurred in the scan; read as 'bcba' because the grammar has no terminal 'e'."
---
Consider the following grammar:

$$S \to aAa \mid BAa \mid \epsilon$$

$$A \to cA \mid bA \mid \epsilon$$

$$B \to b$$

Construct the predictive parsing table corresponding to this grammar. Then, using this table show the sequence of moves made by the parser on input "bcba".

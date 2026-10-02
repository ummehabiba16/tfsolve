---
marks: 15
topics: [recursive-descent]
kind: code
source: {page: 37}
note: "Marks printed as (8+7)."
---
Construct procedure based recursive-descent parser for the grammar given below:

$$S \to Aa \mid bBb \mid c$$

$$A \to aA \mid dd$$

$$B \to b \mid eBe \mid \epsilon$$

Now, parse the string `bebeb` using the constructed parser and show how this parser actually implements a top-down parsing.
